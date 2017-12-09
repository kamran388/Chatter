# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Chat

class IndexView(generic.ListView):
    template_name = 'chat/home.html'
    context_object_name = 'chat_list'

    def get_queryset(self):
        return Chat.objects.select_related('created_by').order_by('-created_on')[:20]


class DetailView(generic.DetailView):
    model = Chat
    template_name = 'chat/detail.html'
    context_object_name = 'chat'


class MyView(IndexView):

    def get_queryset(self):
        return Chat.objects.filter(created_by=self.request.user.id).order_by('-created_on')[:20]

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MyView, self).dispatch(*args, **kwargs)

class NewChatView(generic.edit.CreateView):
    model = Chat
    fields = ['text', 'via']
    success_url = "/my/"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(NewChatView, self).form_valid(form)

class EditChatView(generic.edit.UpdateView):
    model = Chat
    fields = ['text', 'via']
    success_url = "/my/"

    def get_queryset(self):
        base_qs = super(EditChatView, self).get_queryset()
        return base_qs.filter(created_by = self.request.user)
