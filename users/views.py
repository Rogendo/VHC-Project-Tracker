from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from users.models import  Contractor, Project, Checklist, Procurement_Department,ProjectProgress
from django.shortcuts import render

def detail(request,pk):
    project=get_object_or_404(Project,pk=pk)
    projectprogress=get_object_or_404(ProjectProgress,pk=pk)

    return render (request,'users/detail.html',{
        'project':project,
        'projectprogress':projectprogress,

    })


def completed(request):
    projects = Project.objects.all()
    contractor = Contractor.objects.all()
    return render(request, 'users/completed_projects.html',{
                  'contractor':contractor,
                  'projects':projects,})

def home(request):
    projects = Project.objects.all()
    contractor = Contractor.objects.all()
    return render(request, 'users/index.html',{
                  'contractor':contractor,
                  'projects':projects,})
    
def contact(request):
    return render(request, 'users/contact.html')
    
def privacy_policy(request):
    return render(request,'users/privacy_policy.html')

def terms_and_conditions(request):
    return render(request,'users/terms_conditions.html')

def about(request):
    return render(request,'users/about.html')
