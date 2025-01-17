# Generated by Django 4.1.2 on 2022-11-01 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MembersProcesses', '0001_initial'),
        ('ProjectProcesses', '0001_initial'),
        ('ActivitiesProcesses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MembersProcesses.member'),
        ),
        migrations.AddField(
            model_name='activitie',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ProjectProcesses.project'),
        ),
    ]
