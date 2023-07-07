# Generated by Django 4.2.2 on 2023-07-07 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100, unique=True)),
                ('company_email', models.EmailField(max_length=254, unique=True)),
                ('chief_contractor', models.CharField(max_length=100, unique=True)),
                ('chief_contractor_phone_no', models.CharField(max_length=12, unique=True)),
                ('contracting_team_member_1', models.CharField(max_length=100, unique=True)),
                ('contracting_team_member_2', models.CharField(max_length=100, unique=True)),
                ('contracting_team_member_3', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_4', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_5', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_6', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_7', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_8', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_9', models.CharField(blank=True, max_length=100, unique=True)),
                ('contracting_team_member_10', models.CharField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procurement_Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Department',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, unique=True)),
                ('project_location', models.CharField(max_length=100)),
                ('sqm_rate_or_lm', models.CharField(max_length=50)),
                ('commencement_date', models.DateTimeField()),
                ('site_location', models.CharField(max_length=80)),
                ('floor_area', models.CharField(max_length=20)),
                ('contract_sum', models.CharField(max_length=20)),
                ('payments_made', models.CharField(max_length=20)),
                ('payment_status', models.CharField(choices=[('Fully Paid', 'Fully Paid'), ('Partially Paid', 'Partially Paid'), ('Pending', 'Pending')], default='Pending', max_length=20)),
                ('work_status', models.CharField(choices=[('Started', 'started'), ('Completed', 'completed')], default='Started', max_length=20)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('contract_period_months', models.PositiveIntegerField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracting_company', to='tracker.contractor')),
                ('procurrement_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procurement', to='tracker.procurement_department')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='ProjectProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phase', models.CharField(choices=[('Approval', 'Approval'), ('Start', 'Start'), ('Foundation', 'Foundation'), ('Completion', 'Completion')], default='Approval', max_length=10)),
                ('description', models.CharField(max_length=600)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('main_images', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('document_1', models.FileField(blank=True, upload_to='Progress_Documents/')),
                ('document_2', models.FileField(blank=True, upload_to='Progress_Documents/')),
                ('document_3', models.FileField(blank=True, upload_to='Progress_Documents/')),
                ('document_4', models.FileField(blank=True, upload_to='Progress_Documents/')),
                ('document_5', models.FileField(blank=True, upload_to='Progress_Documents/')),
                ('image_1', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_2', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_3', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_4', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_5', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_6', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_7', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_8', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_9', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_10', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_11', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_12', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_13', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_14', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_15', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_16', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_17', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_18', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_19', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_20', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_21', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_22', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_23', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_24', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_25', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_26', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_27', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_28', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_29', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_30', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_31', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('image_32', models.ImageField(blank=True, upload_to='Progress_Images/')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projectname', to='tracker.project')),
            ],
            options={
                'verbose_name': 'Project Progres',
                'verbose_name_plural': 'Project Progress',
            },
        ),
        migrations.CreateModel(
            name='ProjectDeliveryAcceptanceTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_no', models.CharField(max_length=12, unique=True)),
                ('comment', models.CharField(max_length=100)),
                ('project_status', models.CharField(choices=[('Approved', 'Approved'), ('Not Approved', 'Not Approved')], default='Not Approved', max_length=100)),
                ('project_checked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.project')),
            ],
            options={
                'verbose_name': 'Project Acceptance Delivery Team',
            },
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checklist_name', models.CharField(max_length=80, unique=True)),
                ('checklist_document', models.FileField(upload_to='Checklist_Documents/')),
                ('contract_period_months', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('main_contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractor', to='tracker.contractor')),
                ('procurrement_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procuring_dpt', to='tracker.procurement_department')),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to='tracker.project')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]