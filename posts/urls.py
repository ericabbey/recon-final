from django.conf.urls import url
from django.contrib import admin

from .views import (
    post_create,
    post_detail,
    post_list,
    post_update,
    post_delete,
)

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<id>\d+)/$', post_detail, name="detail"),
    url(r'^edit/(?P<id>\d+)/$', post_update),
    url(r'^delete/(?P<id>\d+)/$', post_delete),
]
