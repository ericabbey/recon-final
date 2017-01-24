import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404,redirect

from accounts.models import UserProfile
from comment.forms import CommentForm
from comment.models import Comment
from .forms import PostForm
from .models import Post

@login_required(login_url='/login/')
def post_create(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.title)
    if profile.title == "editor":
        if not request.user.is_authenticated:
            raise Http404
        form = PostForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
             "form": form,
        }
    else:
        return redirect('index')
    return render(request, "post_form1.html", context)


def post_detail(request, id):
    instance = get_object_or_404(Post, id=id)
    com_user = get_object_or_404(User, id=request.user.id),
    initial_data = {
        'blog': instance,
        'user':com_user
    }
    form = CommentForm(request.POST or None, initial=initial_data)
    form_valid = request.user.is_authenticated
    idFromPage = request.POST.get("id")
    current_user = request.user.id
    detail_url = request.path
    exists = instance.votes.exists(idFromPage)
    voteCount = instance.votes.count()
    print(com_user )
    if idFromPage:
        if not exists:
            instance.votes.up(idFromPage)
            voteCount = instance.votes.count()
        else:
            instance.votes.down(idFromPage)
            voteCount = instance.votes.count()
        data = {'result': voteCount}
        return HttpResponse(json.dumps(data), content_type="application/json")
    if form.is_valid():
        c_type = instance
        user = request.user
        content_data = form.cleaned_data.get('content')
        new_comment, created = Comment.objects.get_or_create(
            user=user,
            blog=c_type,
            content=content_data,
        )
        return HttpResponseRedirect(request.path)
    
    context = {
        'title': instance.title,
        'instance': instance,
        'form': form,
        'form_valid': form_valid,
        'voteCount': voteCount,
        'current_user': current_user,
        'detail_url': detail_url
    }
    return render(request, "post_detail.html", context)


def post_list(request):
    queryset = Post.objects.all()  # .order_by("-timestamp")
    profile = UserProfile.objects.filter(user=request.user)
    query = request.GET.get("q")
    current_user = request.user.id
    if query:
        queryset = queryset.filter(Q(title__icontains=query) | Q(author__icontains=query)).distinct()
    obj_count = queryset.count()
    context = {
        "object_list": queryset,
        "title": "list",
        "current_user": current_user,
        "pro": profile,
        'obj_count': obj_count
    }
    return render(request, "blogs.html", context)


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)
    profile = get_object_or_404(UserProfile, user=request.user)
    print(profile.title)
    if profile.title == "editor":
        if not request.user.is_authenticated:
            raise Http404
        form = PostForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return HttpResponseRedirect(instance.get_absolute_url())
        context = {
             "form": form,
             "instance": instance
        }
    else:
        return redirect('index')
    return render(request, "post_form.html", context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("posts:list")
