from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from chat import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view(), name= "homepage"),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name="detail"),
    url(r'^login/$', auth_views.login, name="login"),
    url(r'^logout/$', auth_views.logout, name="logout"),
    url(r'^my/$', views.MyView.as_view(), name="myview"),
    url(r'^create/$', views.NewChatView.as_view(), name = "newchat"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.EditChatView.as_view(), name = "editchat"),
]
