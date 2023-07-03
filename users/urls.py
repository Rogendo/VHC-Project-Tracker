from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path('items/<int:pk>/',views.detail, name='detail'),
    path('completed/',views.completed , name='completed'),
    path('about/',views.about,name='about'),
    path("contact/",views.contact,name='contact'),
    path('privacy/',views.privacy_policy,name='privacy'),
    path('terms/',views.terms_and_conditions,name='terms'),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
