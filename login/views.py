from django.shortcuts import render
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import signUpForm, loginForm, customers
from django.http import HttpResponseRedirect, HttpResponse, request, JsonResponse
from .models import Profile
from django.shortcuts import render, redirect, reverse
# Create your views here.
from django.contrib import messages

def index(request):
	return render(request,'base.html')

def login(request):
	return render(request,'login.html')

def register(request):
	form = signUpForm()
	if request.method=="POST":
		form = signUpForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('login:index')
			
	context = {
		"form":form
	}	
	return render(request,'register.html',context)


def about(request):
	return render(request,'about.html')

def logout(request):
	return HttpResponse("You are logged out")



