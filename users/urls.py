from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accountant/", views.accountant_home, name="accountant-home"),
    path("minister/", views.minister_home, name="minister-home"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("signup/accountant/", views.AccountantSignUpForm.as_view(), name="accountant-signup"),
    path("signup/minister/", views.MinisterSignUpForm.as_view(), name="minister-signup"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    ]
