from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import  CustomUserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages


def index(request):
    return HttpResponse("Look space")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    return render(request, 'lookapp/register.html', {'form': form})

