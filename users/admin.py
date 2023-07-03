from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import  Contractor, Project, Checklist, Procurement_Department,ProjectProgress
from django.contrib import messages
# Register your models here.

class MinisterAdminSite(admin.AdminSite):
    site_header = "Minister Admin"
    site_title = "Minister Admin Site"
    
minister_admin_site = MinisterAdminSite(name="minister_admin")

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_ID_no','company_email','company_email','chief_contractor','chief_contractor_phone_no')
    # adding search fields
    search_fields = ['company_name','company_ID_no']
    # list_filter = ['company_name']
     
    def has_add_permission(self, request):
        return True   

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_location','company_name','contract_period_months','contract_sum','work_status','completed')
    # adding search fields
    search_fields = ['project_name','company_name','contract_sum','work_status','completed']
    # list_filter = ['project_name']
    
    
    def status(self, obj):
        return obj.completed == 1
    status.boolean = True
    

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('project_name','procurrement_department','date','contract_period_months')
     # adding search fields
    search_fields = ['project_name','procurrement_department','date']
    # list_filter = ['project_name']

class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project_name','company_name','updated_at')



class Procurement_DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name','created')

minister_admin_site.register(Contractor,ContractorAdmin)
minister_admin_site.register(Project,ProjectAdmin)
minister_admin_site.register(Checklist,ChecklistAdmin)
minister_admin_site.register(ProjectProgress,ProjectProgressAdmin)
minister_admin_site.register(Procurement_Department,Procurement_DepartmentAdmin)

# accountant
class AccountantAdmin(admin.AdminSite):
    site_header = "Accountant Admin"
    site_title = "Accountant Admin"
accountant_admin_site = AccountantAdmin(name="accountant_admin")

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_ID_no','company_email','company_email','chief_contractor','chief_contractor_phone_no')
    # adding search fields
    search_fields = ['company_name','company_ID_no']
    # list_filter = ['company_name']
     
    def has_add_permission(self, request):
        return True   

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_location','company_name','contract_period_months','contract_sum','work_status','completed')
    # adding search fields
    search_fields = ['project_name','company_name','contract_sum','work_status','completed']
    # list_filter = ['project_name']
    
    
    def status(self, obj):
        return obj.completed == 1
    status.boolean = True

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('project_name','procurrement_department','date','contract_period_months')
     # adding search fields
    search_fields = ['project_name','procurrement_department','date']
    # list_filter = ['project_name']

class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project_name','company_name','updated_at')


class Procurement_DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name','created')

accountant_admin_site.register(Contractor,ContractorAdmin)
accountant_admin_site.register(Project,ProjectAdmin)
accountant_admin_site.register(Checklist,ChecklistAdmin)
accountant_admin_site.register(ProjectProgress,ProjectProgressAdmin)
accountant_admin_site.register(Procurement_Department,Procurement_DepartmentAdmin)



# main admin
admin.site.register(Contractor)
admin.site.register(Project)
admin.site.register(Checklist)
admin.site.register( Procurement_Department)
admin.site.register(ProjectProgress)