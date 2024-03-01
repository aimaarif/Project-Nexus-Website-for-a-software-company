
# Create your views here.
# restaurant_app/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def home_view(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Implement your login logic here
            return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Implement your signup logic here
            return redirect('home')
    else:
        form = SignupForm()

    return render(request, 'signup.html', {'form': form})

