from django.shortcuts import render
from django.http import HttpResponse
from .models import Home

# Create your views here.

def home(request):

    home= Home.objects.all().first()

    context= {
        'name' : home.name,
        'role1' : home.role1,
        'role2' : home.role2,

    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request,'contact.html')
