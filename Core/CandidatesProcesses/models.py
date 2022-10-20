from Core.ProjectProcesses.models import Project
from django.db import models

# Create your models here.
class Candidate(models.Model):
    projects = models.ManyToManyField(Project)
    name = models.CharField(verbose_name='Nombre',max_length=150)
    number_phone = models.CharField(verbose_name='Teléfono movil', max_length=8, unique=True)
    email = models.EmailField(verbose_name='Correo')
    category = models.CharField(verbose_name='Categoría', max_length=50)
    # Buscar category
    area = models.CharField(verbose_name='Área', max_length=150)
    position = models.CharField(verbose_name='Cargo', max_length=150)
