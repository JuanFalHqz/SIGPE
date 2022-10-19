from Core.ProjectProcesses.models import Project
from django.db import models


# Create your models here.
class Evidence(models.Model):
    evidence_name = models.CharField(verbose_name='Nombre', max_length=150)
    media = models.ImageField(upload_to='evidences/%Y/%m/%d', null=True, blank=True)#pendiente
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Evidence'
        verbose_name_plural = 'Evidences'
        db_table = 'Evidence'
    def __str__(self):
        return "%s" % (self.evidence_name)
