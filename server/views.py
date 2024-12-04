from django.shortcuts import render
from django.http import HttpResponse

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

def login(request):
    context = {
        'message': 'Hello from the server app!'
    }
    return render(request, 'server/login.html', context)