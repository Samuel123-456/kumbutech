from django.urls import path
from product.views import (
    ProductCreateView
)
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('create/', login_required(ProductCreateView.as_view(), login_url='signin'), name='create-product')
]
    