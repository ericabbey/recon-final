__author__ = 'cyberrick'

from django.conf.urls import url

from .views import (nxt, events, prev,detail)

urlpatterns = [
    url(r'^$', events),
    url(r'^n/$', nxt, name="next"),
    url(r'^p/$', prev, name="previous"),
    url(r'^detail/$', detail, name="detail"),
    ]