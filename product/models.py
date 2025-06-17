from django.db import models
from secrets import token_urlsafe
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
      name = models.CharField(max_length=100, verbose_name='Nome da Categoria')
      date = models.DateTimeField(verbose_name='Data de Criacao')

      def __str__(self):
            return self.name



class Product(models.Model):
      name = models.CharField(max_length=300, verbose_name='Nome do Produto')
      price = models.DecimalField(verbose_name='Preco do Produto', decimal_places=2, max_digits=10)
      #categoria = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
      stoque = models.IntegerField(verbose_name='Quantidade')
      
      slug = models.SlugField(default=None, editable=False)

      date_entry = models.DateTimeField(verbose_name='Data de entrada', default=None)
      date_valid = models.DateField(verbose_name='Data De exporacao')
      empresa = models.ForeignKey(User, on_delete=models.CASCADE)

      state = models.BooleanField(verbose_name='Estato', default=True)

      def save(self, *args, **kwargs):
            if not self.slug:
                  self.slug = token_urlsafe()
            if not self.date_entry:
                  self.date_entry = timezone.now()
            return super().save(*args, **kwargs)
      
      def __str__(self):
            return self.name + f'({self.empresa.username})'

      def parce_date_valid(self):
            return datetime.strftime(self.date_valid, '%Y-%m-%d')
      
      def parce_date_entry(self):
            return datetime.strftime(self.date_entry, '%Y-%m-%d %H:%M')
      
class Client(models.Model):
      bi = models.CharField(max_length=100, verbose_name='Numbero do BI')


# class Cart(models.Model):
#       client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
#       date_create = models.DateTimeField()


class Selling(models.Model):
      client = models.ForeignKey(Client, on_delete=models.CASCADE)
      produto = models.ForeignKey(Product, on_delete=models.CASCADE)
      quantity = models.IntegerField()
      date_sell = models.DateTimeField()

      def get_total_money(self):
            return self.quantity * self.produto.price