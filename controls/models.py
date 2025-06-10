from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Control(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      profile = models.FileField(verbose_name='Foto de Perfil', upload_to='profile')
      address = models.CharField(max_length=300, verbose_name='Endereco')
      city = models.CharField(max_length=100, verbose_name='Cidade')
      bi = models.CharField(max_length=100, verbose_name='Numero Do BI')
      about = models.TextField(max_length=500, verbose_name='Sobre')

      def __str__(self):
            return self.user.username