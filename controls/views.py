from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate

from django.views import View
from controls.forms import SigninForm

# Create your views here.
class SiginView(View):
      template_name = 'controls/signin.html'

      def get(self, request):
            context = dict()

            formset = SigninForm(request=request)

            context['formset'] = formset
            return render(request, self.template_name, context)
      
      def post(self, request):
            formset = SigninForm(data=request.POST, request=request)

            if formset.is_valid():
                  user = formset.get_user_or_none()
                  if user:
                        login(request, user)
                        return redirect('create-product')
            
            messages.add_message(request, messages.ERROR, 'Credenciais Erradas.')
            return redirect(reverse('signin'))

#TODO: FAZER VALIDACOE AVANCADAS
def signup(request):
      template_name = 'controls/signup.html'

      if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            
            if User.objects.filter(Q(username=username) & Q(email=email)).exists():
                  messages.add_message(request, messages.ERROR, 'Usuario com esse nome ou email ja existe')
                  return redirect(reverse('signup'))

            if password != confirm_password:
                  messages.error(request, 'Palavra passes Diferentes')
                  return redirect(reverse('signup'))

            
            User.objects.create_user(username=username, email=email, password=password)

            return redirect('signin')
      
      return render(request, template_name)

def signout(request):
      logout(request)
      return redirect('signin')