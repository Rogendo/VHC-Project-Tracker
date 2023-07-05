from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import  Contractor, Project, Checklist, Procurement_Department,ProjectProgress
from django.contrib import messages

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_email','company_email','chief_contractor','chief_contractor_phone_no')
    # adding search fields
    search_fields = ['company_name']
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
    list_display = ('project_name','procurrement_department','pdf_preview','date','contract_period_months')
     # adding search fields
    search_fields = ['project_name','procurrement_department','date']
    # list_filter = ['project_name']
    def pdf_preview(self,obj):
            return obj.pdf_preview
    pdf_preview.short_description = 'Checklist PDF'
        

class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project_name','phase','image_preview','updated_at')
    
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