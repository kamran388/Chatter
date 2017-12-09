from django.conf.urls import url, patterns, include
from django.contrib import admin
from chat import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
