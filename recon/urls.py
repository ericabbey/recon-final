"""recon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from accounts.views import *
from base.views import (gallery, galleryAud, galleryVid, index, about, contactForm  )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', include("posts.urls", namespace="posts")),
    url(r'^events/', include("calend.urls", namespace="events")),
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout_view, name='logout'),
    url(r'^gallery/', gallery, name='gallery'),
    url(r'^videos', galleryVid, name='videos'),
    url(r'^audios', galleryAud, name='audios'),
    url(r'^contact/', contactForm, name='contact'),
    url(r'^about/', about, name='about'),
    url(r'^profile/', profile, name='profile'),
    url(r'^$', index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
