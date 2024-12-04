from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages



from .forms import LoginForm, CreateUserForm

# Create your views here.
def home(request):
    context = {
        'message': 'Hello from the server app!'
    }
    return render(request, 'server/home.html', context)

def about(request):
    context = {
        'message': 'Hello from the server app!'
    }
    return render(request, 'server/about.html', context)

def contact(request):
    context = {
        'message': 'Hello from the server app!'
    }
    return render(request, 'server/contact.html', context)

def services(request):
    context = {
        'message': 'Hello from the server app!'
    }
    return render(request, 'server/services.html', context)

# def login(request):
#     context = {
#         'message': 'Hello from the server app!'
#     }
#     return render(request, 'server/login.html', context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Authenticate the user
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('home')  # Redirect to the home page after login
            else:
                # Invalid login credentials
                messages.error(request, 'Invalid username or password')
        
        else:
            # Form is not valid
            messages.error(request, 'Invalid form submission')
            
            return redirect('home')  # Redirect to the home page after login (you can change this as needed)
    else:
        form = LoginForm()

    return render(request, 'server/profile.html', {'form': form})


def create_profile_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            
            return redirect('login')  # Redirect to the home page after profile creation
    else:
        form = CreateUserForm()

    return render(request, 'server/create_profile.html', {'form': form})

def profile(request):
    context={
        'message': 'Hello'
    }
    return render(request, 'server/profile.html', context)
