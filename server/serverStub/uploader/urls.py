from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.listall, name='list'),
    url(r'^(?P<uuid>[0-9a-fA-F\-]+)/$', views.upload, name='uploadFile'),
]
