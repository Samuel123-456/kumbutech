from django.shortcuts import render

# Create your views here.
def signin(request):
      template_name = 'controls/signin.html'
      return render(request, template_name)

def signup(request):
      template_name = 'controls/signup.html'
      return render(request, template_name)