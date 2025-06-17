from django import forms
from product.models import Product
from decimal import Decimal
from django.db import transaction

class ProductCreateForm(forms.Form):

      def __init__(self, request=None, *args, **kwargs):
            self.request = request
            super().__init__(*args, **kwargs)

      
      name = forms.CharField(
            max_length=300,
            required=True,
            widget=forms.TextInput(
                  attrs={
                        'name': "name",
                        'class': "placeholder:text-gray-500 text-sm focus:shadow-primary-outline leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-blue-500 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow",
                        'placeholder': "Ex: Notebook Dell",
                  }
            )
      )

      price = forms.DecimalField(
            decimal_places=2, max_digits=10,
            required=True,
            widget=forms.NumberInput(
                  attrs={
                        'step': "0.01",
                        'name': "price",
                        'class': "placeholder:text-gray-500 text-sm focus:shadow-primary-outline leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-blue-500 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow",
                        'placeholder': "Ex: 2500.00"
                  }
            )

      )

      stoque = forms.IntegerField(
            required=True,
            widget=forms.NumberInput(
                  attrs={
                        'name': "price",
                        'class': "placeholder:text-gray-500 text-sm focus:shadow-primary-outline leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-blue-500 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow",
                        'placeholder': "Ex: 20"
                  }
            )
      )
      
      date_valid = forms.DateField(
            widget=forms.DateInput(
                  attrs={
                        'type': 'date',
                        'class':"placeholder:text-gray-500 text-sm focus:shadow-primary-outline leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding py-2 px-3 font-normal text-gray-700 transition-all focus:border-blue-500 focus:bg-white focus:text-gray-700 focus:outline-none focus:transition-shadow"
                  }
            )
      )


      def clean_name(self):
            name: str = self.cleaned_data.get('name')

            if name.isnumeric():
                  raise forms.ValidationError('Value can not be only Numeric')
            return name
      
      def clean_price(self):
            price = self.cleaned_data.get('price')

            if not isinstance(price, Decimal):
                  raise forms.ValidationError('The price is not a decimal type')
            return price

      def clean_stoque(self):
            stoque = self.cleaned_data['stoque']

            if not stoque:
                  raise forms.ValidationError('O stoque nao foi informado')

            if isinstance(stoque, str) and str(stoque).isnumeric():
                  stoque = stoque
            
            return stoque


      def save(self):
            with transaction.atomic() as tr:
                  Product.objects.create(
                        name = self.cleaned_data['name'],
                        price = self.cleaned_data['price'],
                        stoque = self.cleaned_data['stoque'],
                        date_valid = self.cleaned_data['date_valid'],
                        empresa = self.request.user
                  )



