from django.contrib.auth.models import AbstractUser
from django.db import models

from Helpers.helpers import Media
from SIGPE.settings import MEDIA_URL, STATIC_URL


class User(AbstractUser):
    image = models.ImageField(upload_to='images/users/%Y/%m/%d', null=True, blank=True)
    number_phone = models.CharField(verbose_name='Teléfono movil', max_length=8, unique=True)
    ci = models.CharField(verbose_name='Carnet de identidad', max_length=11, unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
        db_table='User'

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'dist/img/empty.png')