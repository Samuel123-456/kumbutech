from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login, authenticate


# Create your views here.
def signin(request):
      template_name = 'controls/signin.html'
      
      if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = User.objects.filter(email=email).first()            
            user_authenticated = authenticate(request, username=user.username, password=password)      

            if not user_authenticated:
                  messages.add_message(request, messages.ERROR, 'Credencias invalida')
                  return redirect(reverse('signin'))
            
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login feito com sucesso')
            
            return render(request, 'site/dashboard.html')
      return render(request, template_name)

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