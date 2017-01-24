from django.contrib.auth import (
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect

from .forms import UserLoginForm, UserRegisterForm
from .models import UserProfile
from posts.models import Post

def login_view(request):
    print(request.user.is_authenticated())
    nxt = request.GET.get('next', 'index')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if nxt:
            return redirect(nxt)
        print(request.user.is_authenticated())
    return render(request, "Login_form.html", {"form": form})


def register_view(request):
    form = UserRegisterForm(request.POST or None)
    nxt = request.GET.get('next', '/home/')
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if nxt:
            return redirect(nxt)

    context = {
        "form": form
    }
    return render(request, "register.html", context)


def logout_view(request):
    logout(request)
    return redirect('/home/')


@login_required(login_url='/login/')
def profile(request):
    user = get_object_or_404(UserProfile, user=request.user)
    print(user.title)
    if user.title == "editor":
        post_by_user = Post.objects.filter(user=request.user)
        context = {
            'posts': post_by_user,
            'obj': user
        }
        return render(request, 'profile/profile.html', context)
