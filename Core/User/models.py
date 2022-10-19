from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    image = models.ImageField(upload_to='users/%D/%m/%d', null=True, blank=True)
    number_phone = models.CharField(verbose_name='Teléfono movil', max_length=8, unique=True)
    ci = models.CharField(verbose_name='Carnet de identidad', max_length=11, unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table='User'
