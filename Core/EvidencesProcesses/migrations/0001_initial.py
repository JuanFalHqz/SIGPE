# Generated by Django 4.1.2 on 2022-11-01 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ProjectProcesses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence_name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('media', models.ImageField(blank=True, null=True, upload_to='evidences/%Y/%m/%d')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectProcesses.project')),
            ],
            options={
                'verbose_name': 'Evidence',
                'verbose_name_plural': 'Evidences',
                'db_table': 'Evidence',
            },
        ),
    ]
