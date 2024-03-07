# restaurant_app/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from .forms import FeedbackForm

def home_view(request):
    return render(request, 'home.html')

# views.py
def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your feedback is submitted.")
            return redirect('home')  # Create a success_page URL in your urls.py
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})


def products_view(request):
    return render(request, 'products.html')

def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
	return render(request, 'about.html', {})	

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You Have Been Logged In!")
                return redirect('home')
            else:
                messages.error(request, "Invalid login credentials. Please try again.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def signup_view(request):
	form = SignupForm()
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# log in user
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Username Created"))
			return redirect('home')
		else:
			messages.success(request, ("Whoops! There was a problem Registering, please try again..."))
			return redirect('signup')
	else:
		return render(request, 'signup.html', {'form':form})