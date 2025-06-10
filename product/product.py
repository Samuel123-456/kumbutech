from product.models import Product
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.shortcuts import redirect

class ProductCRUD:
      def __init__(self, request=None):
            self.request = request
            self.current_page_paginator = 1

      def _update_current_page_paginator(self):
            num_page = self.request.GET.get('page', '1')
            if not num_page.isnumeric():
                  num_page = 1
            self.current_page_paginator = int(num_page)
            return self.current_page_paginator

      def create(self):
            if not self.request.user.is_authenticated:
                  return None
            name = self.request.POST.get('name')
            price = self.request.POST.get('price')
            #categoria = self.request.POST.get('categoria')
            stoque = self.request.POST.get('stoque')
            date_entry = self.request.POST.get('date_entry')
            date_valid = self.request.POST.get('date_valid')
            empresa = self.request.user

            product = Product(
                  name=name,
                  price=price,
                  stoque=stoque,
                  date_entry=date_entry,
                  date_valid=date_valid,
                  empresa=empresa
            )

            product.save()

            print('Product Register SUccessefully')


      def read(self):
            search = self.request.GET.get('q', None)

            produts = Product.objects.filter(empresa=self.request.user)
      
            return produts.filter(Q(name__contains=search)) if search else produts
      
        
      
      def delete(self, slug):
            product = Product.objects.filter(slug=slug)
            if not product.exists():
                  return False
            print(product)
            product = product.first()
            product.state = False
            product.save()
            
            return True
      
      def update(self, slug=None):
            product = Product.objects.filter(Q(slug=slug))
            if not product.exists():
                  return redirect('read_product')

            product = product.first()
            
            name = self.request.POST.get('name')
            price = self.request.POST.get('price')
            stoque = self.request.POST.get('stoque')
            date_entry = self.request.POST.get('date_entry')
            date_valid = self.request.POST.get('date_valid')

            product.name = name
            product.price = price
            product.stoque = stoque
            product.date_entry = date_entry
            product.date_valid = date_valid

            product.save()
            return product

      def paginate(self):
            products = self.read().filter(Q(state=True))

            paginator = Paginator(products, 3)

            product_page_paginator = paginator.get_page(self._update_current_page_paginator())

            return product_page_paginator

