from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .models import User
from .forms import AccountantSignUpForm, MinisterSignUpForm, LoginForm
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .decorators import accountant_required,minister_required
from users.models import Accountant, Minister, Contractor, Project, Checklist, Procurement_Department,ProjectProgress

def detail(request,pk):
    project=get_object_or_404(Project,pk=pk)
    return render (request,'users/detail.html',{
        'project':project
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

# Create your views here.
class AccountantSignUpForm(CreateView):
    model = User
    form_class = AccountantSignUpForm
    template_name = 'users/accountant_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'accountant'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accountant-home')


class MinisterSignUpForm(CreateView):
    model = User
    form_class = MinisterSignUpForm
    template_name = 'users/minister_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'minister'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('minister-home')


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.is_accountant:
                return reverse('accountant-home')
            elif user.is_minister:
                return reverse('minister-home')
        else:
            return reverse('login')


@login_required
@accountant_required
def accountant_home(request):
    
    return render(request, 'users/accountant_home.html')


@login_required
@minister_required
def minister_home(request):
    
    return render(request, 'users/minister_home.html')

