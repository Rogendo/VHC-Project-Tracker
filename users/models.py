# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import timedelta

# Create your models here.

# CREATING THE USERS.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    is_minister = models.BooleanField(default=False)
    is_accountant = models.BooleanField(default=False)
    
class Accountant(models.Model):
    email=models.EmailField(User)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='accountant')
    first_name = models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    ID_no = models.IntegerField()
    staff_no = models.IntegerField()
    created_at=models.DateTimeField(default=timezone.now)

class Minister(models.Model):
    email=models.EmailField(User)
    user=models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True, related_name='minister')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ID_no = models.IntegerField()
    ministry = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)

# CREATING THE DATA TABLES
class Contractor(models.Model):
    company_name = models.CharField(max_length=100)
    ID_no = models.CharField(max_length=12)
    # ID_no = models.CharField(max_length=12,unique=True
    main_contractor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.company_name
 
# PROCURING DEPARTMENTS
class Procurement_Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department_name
    
    class Meta:
        db_table = 'Tables'
        # change model name in admin
        verbose_name = "Procurement Department"
    
# class ContractImplementationTeam():
    # name=
    # ID_no=
    # phone_no=
    
# Tenders Table
# class Tenders(models.Model):
#     tender_ID = models.CharField(primary_key=True,unique=True,max_length=30)
#     tender_name = models.CharField(unique=True,max_length=60)
#     created_on = models.DateTimeField()
#     project_name = models.CharField(max_length=100)
    
    
PAYMENT_STATUS=(
        (0,"Paid"),
        (1,"Pending")
    )    
WORK_STATUS=(
    (0,"started"),
    (1,"completed")
    
    
)
class Project(models.Model):
    project_name = models.CharField(max_length=100)
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
    checklist_name = models.CharField(max_length=80)
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="project")
    procurrement_department = models.ForeignKey(Procurement_Department,on_delete=models.CASCADE,related_name="procuring_dpt")
    main_contractor = models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name="contractor")
    checklist_document = models.FileField(upload_to='Checklist_Documents/')
    contract_period_months = models.PositiveIntegerField()
    date = models.DateField()


    
    def save(self, *args, **kwargs):
        if self.pk is None:
            current_date=timezone.now().date()
            self.date += relativedelta(months= self.contract_period_months)
        super().save(*args,**kwargs)
        
    class Meta:
        ordering = ['-date']
    
    def __str__(self):
        return self.checklist_name
   
    

  