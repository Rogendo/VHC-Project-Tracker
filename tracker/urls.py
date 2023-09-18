from django.urls import path
from tracker import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

urlpatterns = [
    path("",views.home,name="home"),
    path('items/<int:pk>/',views.detail, name='detail'),
    path('completed/',views.completed , name='completed'),
    path('404',views.custom_404,name='my_custom_view'),
    path('privacy/',views.privacy_policy,name='privacy'),
    path('terms/',views.terms_and_conditions,name='terms'),
    path('create/', views.UserCreateView.as_view(), name='create_account'),
#     path('create/', views.register, name='create_account'),
    path('export/csv/', views.export_csv, name='export_csv'),


    path('admin/', views.adminpanel,name='login'),
    
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
