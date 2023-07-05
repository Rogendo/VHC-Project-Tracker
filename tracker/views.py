from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login,authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from tracker.models import  Contractor, Project, Checklist, Procurement_Department,ProjectProgress
from django.shortcuts import render
from tracker.forms import *


def detail(request,pk):
    project=get_object_or_404(Project,pk=pk)
    projectprogress=get_object_or_404(ProjectProgress,pk=pk)

    return render (request,'tracker/detail.html',{
        'project':project,
        'projectprogress':projectprogress,

    })


def completed(request):
    projects = Project.objects.all()
    contractor = Contractor.objects.all()
    return render(request, 'tracker/completed_projects.html',{
                  'contractor':contractor,
                  'projects':projects,})

def home(request):
    projects = Project.objects.all()
    contractor = Contractor.objects.all()
    return render(request, 'tracker/index.html',{
                  'contractor':contractor,
                  'projects':projects,})
    
# def contact(request):
#     return render(request, 'tracker/contact.html')
    
def privacy_policy(request):
    return render(request,'tracker/privacy_policy.html')

def terms_and_conditions(request):
    return render(request,'tracker/terms_conditions.html')

# def about(request):
#     return render(request,'tracker/about.html')

# def staff_registration(request):
#     if request.method == 'POST':
#         form = StaffRegistrationForm(request.POST)
#         if form.is_valid():
#             staff = form.save()
#             return redirect ('login')
#         else:
#             form = StaffRegistrationForm()
#         return render(request , 'tracker/registration.html', {'form':form})
    
# def staff_login(request):
#     if request.method == 'POST':
#         form = StaffLoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username,password=password)
            
#             if user is not None:
#                 login(request, user)
#                 return redirect('admin')
#             else:
#                 form.add_error(None, 'Invalid username or password')
#         else:
#             form = StaffLoginForm()
#         return render(request ,'tracker/login.html',{'form':form})
                
    