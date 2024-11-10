from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ProfileForm
from .models import Post

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'forum/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'forum/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'forum/profile.html', {'user': request.user})

def home_page(request):
    posts = Post.objects.all()
    return render(request,'forum/home.html',{'posts': posts})

def post_detail(request,id):
    post = get_object_or_404(Post,id=id)
    return render(request,'forum/post_detail.html',{'post': post})

def logout(request):
    posts = Post.objects.all()
    return render(request,'forum/home.html',{'posts': posts})