from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Project(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=150)
    area = models.CharField(verbose_name='Área', max_length=150)
    start_date = models.DateField(verbose_name='Fecha de inicio')
    aprovate_date = models.DateField(verbose_name='Fecha de inicio')
    end_date = models.DateField(verbose_name='Fecha de fin')
    fundamentation = models.TextField(verbose_name='Fundamentación')
    evaluation = models.TextField(verbose_name='Evaluación')
    conclution = models.TextField(verbose_name='Conclución')
    recomendation = models.TextField(verbose_name='Recomendación')
    # estado(aprobado, pendiente, finalizado)
    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        db_table = 'Project'
    def __str__(self):
        return "%s" % (self.name)
