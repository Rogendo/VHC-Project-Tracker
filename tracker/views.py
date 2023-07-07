from django.views.generic.edit import CreateView
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView
from django.contrib.auth import login,authenticate
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy

from django.shortcuts import render
from .forms import *
from django.template import RequestContext
from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.http import Http404,HttpResponseNotFound


class UserCreateView(CreateView):
    model = User
    template_name = 'tracker/registration.html'
    form_class = RegistrationForm
    # success_url = reverse_lazy('success')
    success_url = reverse_lazy('login')
    
    def form_valid(self,form):
        response = super().form_valid(form)
        return response

def adminpanel(request):
    return render(request,admin.site.urls)


def custom_404(request,exception):
    return  redirect("tracker/404.html")
    
def detail(request,pk):
    try:
        project=get_object_or_404(Project,pk=pk)
        projectprogress=get_object_or_404(ProjectProgress,pk=pk)


        return render (request,'tracker/detail.html',{
            'project':project,
            'projectprogress':projectprogress,

        })
    except Http404:
        return render(request,'tracker/error_404.html')
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
                
    
