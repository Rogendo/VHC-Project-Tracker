from typing import Optional
from django.contrib import admin
from django.http.request import HttpRequest
from .models import User, Accountant, Minister, Contractor, Project, Checklist, Procurement_Department,ProjectProgress
from django.contrib import messages
# Register your models here.
# admin.site.register(User)
# admin.site.register(Accountant)
# admin.site.register(Minister)

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','company_ID_no','company_email','company_email','chief_contractor','chief_contractor_phone_no')
    # adding search fields
    search_fields = ['company_name','company_ID_no']
    # list_filter = ['company_name']
    
admin.site.register(Contractor,ContractorAdmin)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_location','company_name','contract_period_months','contract_sum','work_status','completed')
    # adding search fields
    search_fields = ['project_name','company_name','contract_sum','work_status','completed']
    # list_filter = ['project_name']
    
    
    def status(self, obj):
        return obj.completed == 1
    status.boolean = True
    # adding more features in the admin panel
    def make_complete(modeladmin,request,queryset):
        queryset.update(completed=1,work_status=1)
        # queryset.update(work_status=1)
        messages.success(request, "Selected Record(s) Marked as Complete")

    def make_incomplete(modeladmin,request,queryset):
        queryset.update(completed=0,work_status=0)
        messages.success(request,"Selected Record(s) Marked as Incomplete")
        
    admin.site.add_action(make_complete, "Mark as Complete")
    admin.site.add_action(make_incomplete,"Mark as Incomplete")
    
    # removing the delete option in admin panel
    def has_delete_permission(self, request: HttpRequest, obj=None):
        return False
    
    
admin.site.register(Project,ProjectAdmin)

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('project_name','procurrement_department','date','contract_period_months')
     # adding search fields
    search_fields = ['project_name','procurrement_department','date']
    # list_filter = ['project_name']

class ProjectProgressAdmin(admin.ModelAdmin):
    list_display = ('project_name','company_name','updated_at')

admin.site.register(ProjectProgress,ProjectProgressAdmin)
admin.site.register(Checklist,ChecklistAdmin)

admin.site.register(Procurement_Department)

# add search feature to search for records
