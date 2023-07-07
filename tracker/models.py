from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.html import format_html


# import the required libraries
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from datetime import timedelta
from django.utils.html import format_html
import datetime
from django.urls import reverse
from django.views.generic import *
from datetime import date
from django.db import models
# from django.contrib.auth.models import AbstractUser,UserManager


# class CustomUserManager(UserManager):
#     pass
# class CustomUser(AbstractUser):
#     email=models.EmailField(unique=True)
#     USERNAME_FIELD='username'
#     REQUIRED_FIELDS = ['email']

#     objects = CustomUserManager



class Contractor(models.Model):
    company_name = models.CharField(max_length=100,unique=True)
    # company_ID_no = models.CharField(max_length=12,unique=True)
    company_email  = models.EmailField(unique=True)
    chief_contractor = models.CharField(max_length=100,unique=True)
    chief_contractor_phone_no = models.CharField(max_length=12,unique=True)
    contracting_team_member_1 = models.CharField(max_length=100,unique=True)
    contracting_team_member_2 = models.CharField(max_length=100,unique=True,)
    contracting_team_member_3 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_4 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_5 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_6 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_7 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_8 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_9 = models.CharField(max_length=100,blank=True,null=True)
    contracting_team_member_10 = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.company_name

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
    STARTED = 'Started'
    COMPLETED = 'Completed' 
    WORK_STATUS=[
        (STARTED,"started"),
        (COMPLETED,"completed"),
    ]
    
    FULLY_PAID = 'Fully Paid'
    PARTIALLY_PAID = 'Partially Paid'
    PENDING = 'Pending'
    
    PAYMENT_STATUS = [
        (FULLY_PAID,"Fully Paid"),
        (PARTIALLY_PAID,"Partially Paid"),
        (PENDING,"Pending"),
                ]
    
    project_name = models.CharField(max_length=100,unique=True)
    project_location = models.CharField(max_length=100)
    sqm_rate_or_lm = models.CharField(max_length=50)
    commencement_date = models.DateTimeField()
    company_name = models.ForeignKey(Contractor,on_delete=models.CASCADE,related_name='contracting_company')
    procurrement_department = models.ForeignKey(Procurement_Department, on_delete=models.CASCADE,related_name='procurement')
    site_location = models.CharField(max_length=80)
    floor_area = models.CharField(max_length=20)
    contract_sum = models.CharField(max_length=20)
    payments_made = models.CharField(max_length=20)    
    payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS, default=PENDING)
    work_status = models.CharField(max_length=20,choices=WORK_STATUS,default=STARTED)
    updated_on = models.DateTimeField(auto_now_add=True)
    start_date = models.DateField()
    end_date = models.DateField()    
    contract_period_months = models.PositiveIntegerField()
   
    def save(self, *args, **kwargs):
        if self.pk is None:
            current_date=timezone.now().date()
            
            self.start_date += relativedelta(months= self.contract_period_months)
        super().save(*args,**kwargs)
        
    class Meta:
        ordering = ['-updated_on']
    
    def __str__(self):
        return self.project_name
   
class Checklist(models.Model):
    checklist_name = models.CharField(max_length=80,unique=True)
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="project")
    procurrement_department = models.ForeignKey(Procurement_Department,on_delete=models.CASCADE,related_name="procuring_dpt")
    main_contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE,related_name="contractor")
    checklist_document = models.FileField(upload_to='Checklist_Documents/')
    contract_period_months = models.PositiveIntegerField()
    date = models.DateField()

    @property
    def pdf_preview(self):
        return format_html('<a href="{}" target="_blank">View Checklist PDF</a>',self.checklist_document.url)
    

    
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
    PHASE_1 = 'Approval'
    PHASE_2 = 'Start'
    PHASE_3 = 'Foundation'
    PHASE_4 = 'Completion'
    PROJECT_PHASES = [
        (PHASE_1,"Approval"),
        (PHASE_2,"Start"),
        (PHASE_3,"Foundation"),
        (PHASE_4,"Completion"),
    ]
    project_name = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projectname')
    
    phase = models.CharField(max_length=10,
                             choices=PROJECT_PHASES,
                             default=PHASE_1,)
    description = models.CharField(max_length=600)
    start_date = models.DateField()
    end_date = models.DateField()

    def get_remaining_days(self):
        today = date.today()
        remaining_days=(self.end_date - today).days
    
        if remaining_days >30:

            return format_html('<span style="color:blue;"><b>{}</b></span>',remaining_days)
        else:
            return format_html('<span style="color:red;"><b>{}</b></span>',remaining_days)
                
    main_image = models.ImageField(upload_to='Progress_Images/')

    document_1 = models.FileField(upload_to='Progress_Documents/',blank=True,null=True)
    document_2 = models.FileField(upload_to='Progress_Documents/',blank=True,null=True)
    document_3 = models.FileField(upload_to='Progress_Documents/',blank=True,null=True)
    document_4 = models.FileField(upload_to='Progress_Documents/',blank=True,null=True)
    document_5 = models.FileField(upload_to='Progress_Documents/',blank=True,null=True)
    image_1 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_2 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_3 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_4 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_5 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_6 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_7 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_8 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_9 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_10 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_11 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_12 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_13 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_14 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_15 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_16 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_17 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_18 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_19 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_20 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_21 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_22 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_23 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_24 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_25 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_26 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_27 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_28 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_29 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_30 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_31 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    image_32 = models.ImageField(upload_to='Progress_Images/',blank=True,null=True)
    # phase_1_image_1 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_2 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_3 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_4 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_5 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_6 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_7 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_8 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_9 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_10 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_11 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_12 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_13 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_14 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_15 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_16 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_17 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_18 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_19 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_20 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_21 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_22 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_23 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_24 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_25 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_26 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_27 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_28 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_29 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_30 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_31 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_1_image_32 = models.ImageField(upload_to='Progress_Images/',blank=True)

    # phase_2_image_1 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_2_image_2 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_2_image_3 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_2_image_4 = models.ImageField(upload_to='Progress_Images/',blank=True)
 
    # phase_3_image_1 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_3_image_2 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_3_image_3 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_3_image_4 = models.ImageField(upload_to='Progress_Images/',blank=True)
   
    # phase_4_image_1 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_4_image_2 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_4_image_3 = models.ImageField(upload_to='Progress_Images/',blank=True)
    # phase_4_image_4 = models.ImageField(upload_to='Progress_Images/',blank=True)
   

    updated_at = models.DateTimeField(auto_now_add=True)
    def get_absolute_url(self):
        return reverse("calendarapp:event-detail", args=(self.id,))

    @property
    def get_html_url(self):
        url = reverse("calendarapp:event-detail", args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'


    @property
    def image_preview(self):
        return format_html('<img src="{}" width="50" height="50" />',self.main_image.url)

    def __str__(self):
        return f"Progress for {self.project_name}"
    
    class Meta:

        # change model name in admin
        verbose_name = "Project Progres"
        verbose_name_plural = "Project Progress"

class ProjectDeliveryAcceptanceTeam(models.Model):
    APPROVED= 'Approved'
    NOT_APPROVED = 'Not Approved'
    PROJECT_STATUS = [
        (APPROVED,"Approved"),
        (NOT_APPROVED,"Not Approved"),
    ]
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_no = models.CharField(max_length=12,unique=True)
    project_checked = models.ForeignKey(Project,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    project_status = models.CharField(max_length=100,choices=PROJECT_STATUS,default=NOT_APPROVED)
    
    def __str__(self):
        return self.company_name
    class Meta:
    # db_table = 'Tables'
    # change model name in admin
        verbose_name = "Project Acceptance"
        verbose_name_plural = "Project Acceptance"