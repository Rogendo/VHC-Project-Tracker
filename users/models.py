# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import timedelta


# # CREATING THE DATA TABLES
class Contractor(models.Model):
    company_name = models.CharField(max_length=100,unique=True)
    company_ID_no = models.CharField(max_length=12,unique=True)
    company_email  = models.EmailField(null=True,unique=True)
    chief_contractor = models.CharField(max_length=100,unique=True)
    chief_contractor_phone_no = models.CharField(max_length=12,unique=True)
    contracting_team_member_1 = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.company_name
 
# PROCURING DEPARTMENTS
class Procurement_Department(models.Model):
    department_name = models.CharField(max_length=100,unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.department_name
    
    class Meta:
        # db_table = 'Tables'
        # change model name in admin
        verbose_name = "Department"
    

class Project(models.Model):
      
    PAYMENT_STATUS=(
            (0,"Paid"),
            (1,"Pending")
        )    
    WORK_STATUS=(
        (0,"started"),
        (1,"completed")
        )
    project_name = models.CharField(max_length=100,unique=True)
    project_location = models.CharField(max_length=100)
    sqm_rate_or_lm = models.CharField(max_length=50)
    commencement_date = models.DateTimeField()
    tender_no = models.CharField(max_length=20, unique=True)
    company_name = models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='contracting_company')
    # main_contractor = models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='contractor_name')
    procurrement_department = models.ForeignKey(Procurement_Department, on_delete=models.CASCADE,related_name='procurement')
    site_location = models.CharField(max_length=80)
    floor_area = models.CharField(max_length=20)
    contract_sum = models.CharField(max_length=20)
    payments_made = models.CharField(max_length=20)    
    payment_status = models.BooleanField(choices=PAYMENT_STATUS, default=1)
    work_status = models.BooleanField(choices=WORK_STATUS,default=0)
    completed = models.BooleanField(default=False)

    updated_on = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    contract_period_months = models.PositiveIntegerField()

    
    def save(self, *args, **kwargs):
        if self.pk is None:
            current_date=timezone.now().date()
            self.date += relativedelta(months= self.contract_period_months)
        super().save(*args,**kwargs)
        
    class Meta:
        ordering = ['-updated_on']
    
    def __str__(self):
        return self.project_name
   

class Checklist(models.Model):
    # checklist_id = models.CharField(unique=True,max_lenth=50)
    checklist_name = models.CharField(max_length=80,unique=True)
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="project")
    procurrement_department = models.ForeignKey(Procurement_Department,on_delete=models.CASCADE,related_name="procuring_dpt")
    main_contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE,related_name="contractor")
    checklist_document = models.FileField(upload_to='Checklist_Documents/',blank=True,null=True)
    # checklist_document_submitted = models.BooleanField()
    contract_period_months = models.PositiveIntegerField()
    date = models.DateField()

# CHECKLIST DOCEMTENT SUBMITED? TRUE OR FALSE
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            current_date=timezone.now().date()
            self.date += relativedelta(months= self.contract_period_months)
        super().save(*args,**kwargs)
        
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.checklist_name
   
class ProjectProgress(models.Model):
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projectname')
    company_name = models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='companyname')
    # chief_contractor = models.ForeignKey(Contractor,to_field="chief_contractor",on_delete=models.CASCADE)
    description = models.CharField(max_length=600)
    images = models.ImageField(upload_to='Progress_Images/')
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Progress for {self.project_name}"
    
    class Meta:
        # db_table = 'Tables'
        # change model name in admin
        verbose_name = "Project Progres"

