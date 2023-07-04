"""
projecttracker URL Configuration

"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.views.generic import TemplateView
from tracker.admin import  *
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("tracker.urls")),
    path("accountant/",accountant_admin_site.urls)
    # path("minister/",minister_admin_site.urls ),
]
# urlpatterns +=[re_path(r'^.*',TemplateView.as_view(template_name="tracker/index.html"))]

