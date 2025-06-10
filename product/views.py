from django.shortcuts import render, redirect
from product.product import ProductCRUD
from django.contrib import messages
from django.urls import reverse
from .models import Product, Client, Selling
from django.db import transaction
from django.utils.dateparse import parse_datetime
from collections import OrderedDict
from django.db.models import Q



from datetime import datetime


# Create your views here.
def create(request):
      product = ProductCRUD(request)
      product.create()

      return redirect('product')

def read(request):
      template_name = 'site/tables.html'
      ctx = {}

      product = ProductCRUD(request)
      products = product.paginate()

      sellings = Selling.objects.filter(produto__empresa=request.user)

      ctx['products'] = products
      ctx['sellings'] = sellings

      return render(request, template_name, ctx)

def delete(request, slug):
      product = ProductCRUD(request)
      is_deleted = product.delete(slug)

      if not is_deleted:
            messages.add_message(request, messages.ERROR, 'Produto nao encontrado')
      
      return redirect('read_product')
      
def update(request, slug):
      product = ProductCRUD(request)
      product_edit = product.update(slug)

      print(product_edit)
      return redirect(reverse('product'))

def selling(request, slug):
      template_name = 'site/selling.html'
      ctx = {}
      
      if request.method == 'GET':

            product = Product.objects.filter(slug=slug)
            if not product.exists():
                  return redirect('read_product')
            
            product = product.first()

            ctx['product'] = product

            return render(request, template_name, ctx)

      if request.method == 'POST':
            client = request.POST.get('client')
            product = Product.objects.get(slug=slug)
            date_sell = str(request.POST.get('date_sell'))

            

            quantity = str(request.POST.get('quantity'))
            if not quantity.isnumeric():
                  return redirect('read_product')
            
            if int(quantity) > product.stoque:
                  return redirect('read_product')
            
            print('Chegou ate aqui')

            date_sell = parse_datetime(date_sell)
            quantity = int(quantity)
            with transaction.atomic():
                  product.stoque -= quantity
                  print('Meu produto', product)
                  product.save()

                  client = Client(bi=client)
                  client.save()

                  print(date_sell)
                  
                  sell = Selling(client=client, produto=product, quantity=quantity, date_sell=date_sell)
                  sell.save()


            return redirect('read_product')


def dashboard(request):
      products = Product.objects.all()
      template_name = 'site/dashboard.html'
      ctx = {}

      
      l = {}
      for product in products:
            s = Selling.objects.filter(Q(produto=product) & Q(produto__empresa=request.user))
            if s:
                  l.update({s.first().produto.name: s.count()})

      product_ordered = OrderedDict(sorted(l.items(), key=lambda item:item[1], reverse=True))
      ctx['labels']=list(product_ordered.keys())
      ctx['values']=list(product_ordered.values())

      
      return render(request, template_name, ctx)


                  
            
      

