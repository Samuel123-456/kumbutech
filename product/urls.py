from django.urls import path
from product.views import (
    create,
    read,
    delete,
    update,
    selling,
    dashboard
)

urlpatterns = [
    path('create/', create, name='create_product'),
    path('read/', read, name='read_product'),
    path('delete/<slug:slug>', delete, name='delete_product'),
    path('update/<slug:slug>', update, name='update_product'),
    path('selling/<slug:slug>', selling, name='sell_product'),
    path('dashboard/', dashboard, name='dashboard'),
]
