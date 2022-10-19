from Core.MembersProcesses.models import Member
from Core.ProjectProcesses.models import Project
from django.db import models


# Create your models here.

class Activitie(models.Model):
    activitie_name = models.CharField(verbose_name='Nombre', max_length=150)
    descriptions = models.TextField(verbose_name='Descripción')
    realization_date = models.DateField(verbose_name='Fecha de realización')
    count_persons = models.SmallIntegerField(verbose_name="Cantidad de personas",default=0)

    manager = models.ForeignKey(Member,on_delete=models.SET_NULL,null = True)
    project = models.ForeignKey(Project,on_delete=models.SET_NULL,null = True)
    # estado(dada la fecha: realizada, por_realizar, no_realizadas)
    class Meta:
        verbose_name = 'Activitie'
        verbose_name_plural = 'Activities'
        db_table = 'Activitie'
    def __str__(self):
        return "%s" % (self.activitie_name)

