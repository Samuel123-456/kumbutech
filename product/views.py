from django.shortcuts import render, redirect
from django.views import View
from product.forms import ProductCreateForm
from django.contrib import messages


class ProductCreateView(View):
      template_name = 'product/product.html'

      def get(self, request):
            context = dict()
            formset = ProductCreateForm(request=request)

            context['formset'] = formset
            return render(request, self.template_name, context)
      
      def post(self, request):
            formset = ProductCreateForm(data=request.POST, request=request)

            print('+++++++++++++++++++++++++++++++++++++++')

            if formset.is_valid():
                  formset.save()
                  messages.add_message(request, messages.SUCCESS, 'Produto Cadastrado com sucesso!')
                  return redirect('create-product')
            messages.add_message(request, messages.ERROR, 'Certifica que todos os compos estao bem preenchidos')
            return redirect('create-product')

