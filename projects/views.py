# Create your views here.
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.http import HttpResponse
from .models import Project
from django.conf import settings

def project_index(request):
    projects = Project.objects.all()
    return render(request, 'base.html', {'projects': projects})

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'base.html', {'project': project})

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')

def work(request):
    return render(request, 'work.html')

def about(request):
    return render(request, 'about.html')

def index(request):
    return render(request, 'index.html')