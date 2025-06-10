from django.contrib import admin
from product.models import (
      Category,
      Product,
      Selling,
      Client
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Selling) 