from django.contrib import admin
from .models import User, Accountant, Minister, Contractor, Project, Checklist, Procurement_Department

# Register your models here.
# admin.site.register(User)
# admin.site.register(Accountant)
# admin.site.register(Minister)

class ContractorAdmin(admin.ModelAdmin):
    list_display = ('company_name','ID_no')
    
admin.site.register(Contractor,ContractorAdmin)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name','project_location','company_name','contract_period_months','contract_sum','work_status')

    def status(self, obj):
        return obj.work_status == 1
    status.boolean = True

admin.site.register(Project,ProjectAdmin)

class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('project_name','procurrement_department','date','contract_period_months')
    
admin.site.register(Checklist,ChecklistAdmin)

admin.site.register(Procurement_Department)

# add search feature to search for records
