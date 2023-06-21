from django.contrib import admin
from .models import User, Accountant, Minister, Contractor, Project, Checklist, Procurement_Department

# Register your models here.
admin.site.register(User)
admin.site.register(Accountant)
admin.site.register(Minister)
admin.site.register(Contractor)
admin.site.register(Project)
admin.site.register(Checklist)
admin.site.register(Procurement_Department)
