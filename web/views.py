from django.shortcuts import render, redirect
from django.urls import reverse
from product.models import Product
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='signin')
def tables(request):
      template_name = 'site/tables.html'
      return render(request, template_name)

@login_required(login_url='signin')
def product(request):
      template_name = 'site/product.html'
      ctx = {}
      if request.method == 'GET':
            slug_product = request.GET.get('slug')
            update_product = Product.objects.filter(slug=slug_product)
            update_product = update_product.first() if update_product.exists() else None
            
            ctx['update_product'] = update_product

      return render(request, template_name, ctx)


