from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, CreateTrackItem
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Item


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username OR password is incorrect")
            return render(request, 'tracker/login.html')
    return render(request, 'tracker/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account has been created for {username}")
            return redirect(request, 'login')
    return render(request, 'tracker/register.html', {'form': form})


@login_required(login_url='login')
def home(request):
    tracked_items = Item.objects.filter(user=request.user)
    form = CreateTrackItem()
    if request.method == "POST":
        url = request.POST.get("url")
        new_item = form.save(commit=False)
        new_item.url = url
        new_item.user = request.user
        new_item.save()
        return redirect('home')
    return render(request, 'tracker/home.html', {'tracked_items': tracked_items, 'form': form})

