from django.contrib import admin
from django.http.request import HttpRequest
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin

# Register your models here.
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     list_display = [
#         'first_name',
#         'last_name',
#         'email',
#         'is_staff',
#         'is_superuser',
#     ]
# admin.site.register(CustomUser,CustomUserAdmin)



class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_email','company_email','chief_contractor','chief_contractor_phone_no')
    # adding search fields
    search_fields = ['company_name']
    # list_filter = ['company_name']
     
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_location','company_name','contract_period_months','contract_sum','work_status','payments_made','payment_status')
    # adding search fields
    search_fields = ['project_name','company_name','contract_sum','work_status']
    # list_filter = ['project_name']
    
    
    def status(self, obj):
        return obj.completed == 1
    status.boolean = True

class ProjectDeliveryTeamAdmin(admin.ModelAdmin):
     list_display = ('name','email','project_checked','project_status','comment')

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('project_name','procurrement_department','pdf_preview','date','contract_period_months')
     # adding search fields
    search_fields = ['project_name','procurrement_department','date']
    # list_filter = ['project_name']
    def pdf_preview(self,obj):
            return obj.pdf_preview
    pdf_preview.short_description = 'Checklist PDF'
        

class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project_name','phase','image_preview','display_start_date','display_end_date','get_remaining_days')
    list_per_page = 20

    def display_start_date(self,obj):
         return format_html('<span style="color:green;"><b>{}</b></span>',obj.start_date.strftime('%Y-%m-%d'))
    display_start_date.short_description = 'Start Date'
   
    def display_end_date(self,obj):
         return format_html('<span style="color:red;">{}</span>',obj.end_date.strftime('%Y-%m-%d'))
    display_end_date.short_description = "End Date"

    
    def image_preview(self,obj):
            return obj.image_preview
    image_preview.short_description =  'Image Preview'
        

class Procurement_DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name','created')

# main admin
admin.site.register(Contractor,ContractorAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Checklist,ChecklistAdmin)
admin.site.register( Procurement_Department,Procurement_DepartmentAdmin)
admin.site.register(ProjectProgress,ProjectProgressAdmin)
admin.site.register(ProjectDeliveryAcceptanceTeam,ProjectDeliveryTeamAdmin)