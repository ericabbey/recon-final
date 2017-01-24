from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from posts.models import Post

from .models import Contact


def index(request):
    queryset_list = Post.objects.all()
    paginator = Paginator(queryset_list, 3)

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
    }
    if not request.user.is_authenticated():
        user = authenticate(username='Guest', password='qazwsxedc')
        login(request, user)
    print(request.user)
    return render(request, "index.html", context)


def gallery(request):
    return render(request, "gallery.html")


def galleryVid(request):
    return render(request, "gallery-vid.html")


def galleryAud(request):
    return render(request, "gallery-aud.html")


def contactForm(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['message']
        message = content + " by" + name

        Contact.objects.create(
            name=name,
            email=email,
            content=message
        )
        return HttpResponse('')
    if not request.user.is_authenticated():
        user = authenticate(username='Reconciler', password='qazwsxedc')
        login(request, user)
    print(request.user)
    return render(request, "contact.html")


def about(request):
    if not request.user.is_authenticated():
        user = authenticate(username='Reconciler', password='qazwsxedc')
        login(request, user)
    print(request.user)
    return render(request, "about.html")