from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def signin(request):
      template_name = 'controls/signin.html'
      return render(request, template_name)

def signup(request):
      template_name = 'controls/signup.html'



      print(messages.get_messages())
      if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            if password != confirm_password:
                  messages.add_message(request, messages.ERROR, 'Palavra passes Diferentes')
                  return redirect(reverse('signup'))
            User.objects.create_user(username=username, email=email, password=password)

            print(username, email, password, confirm_password)
      return render(request, template_name)

def teste_site(request):
      template_name = 'index.html'
      return render(request, template_name)