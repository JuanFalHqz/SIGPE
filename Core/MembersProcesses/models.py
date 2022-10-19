from django.contrib.auth.models import User
from django.db import models

from Core.User.models import User
from Core.ProjectProcesses.models import Project


# Create your models here.
class Member(User):
    #Hereda todos los datos de USER de django
    category = models.CharField(verbose_name='Categoría', max_length=50)
    #Buscar category
    area = models.CharField(verbose_name='Área', max_length=150)
    position = models.CharField(verbose_name='Cargo', max_length=150)
    project = models.ManyToManyField(Project)

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        db_table = 'Member'
