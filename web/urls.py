from django.urls import path
from web.views import (
    tables,
    product,
)

urlpatterns = [
    path('tables/', tables, name='tables'),
    path('product/', product, name='product'),

]
