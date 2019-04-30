from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth import authenticate,login,get_user_model

from .forms import ContactForm, LoginForm, RegisterForm

def home_view(request):
	return render(request,'home.html')


def contact_view(request):
	contact = ContactForm()

	return render(request,'contact.html',{"form":contact})

def about_view(request):
	return render(request,"about.html",{})

def login_view(request):
	form = LoginForm(request.POST or None)
	context= {"form":form}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)
		if user is not None:
			context['form'] = LoginForm()
			login(request,user)
			print(request.user.is_authenticated()) 
		else:
			print("Error")
		
	return render(request,"auth/login.html",context)
User = get_user_model()
def register_view(request):
	form = RegisterForm(request.POST or None)
	context= {"form":form}
	if form.is_valid():
		print(form.cleaned_data)
		username = form.cleaned_data.get("username")
		email = form.cleaned_data.get("email")
		password = form.cleaned_data.get("password")
		new_user = User.objects.create_user(username,email,password)
		print(new_user)

	return render(request,"auth/register.html",context)