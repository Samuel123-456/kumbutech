from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class SigninForm(forms.Form):


      email = forms.EmailField(
            widget=forms.EmailInput(
                  attrs={
                        'name':'email',
                        'type':'email',
                        'placeholder': 'Ex.: samuel@gmail.com',
                        'class': "focus:shadow-primary-outline dark:bg-gray-950 dark:placeholder:text-white/80 dark:text-white/80 text-sm leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding p-3 font-normal text-gray-700 outline-none transition-all placeholder:text-gray-500 focus:border-fuchsia-300 focus:outline-none"
                  }
            )
      )

      password = forms.CharField(
            widget=forms.PasswordInput(
                  attrs={
                        'name': 'passoword',
                        'type': 'password',
                        'placeholder': 'Password',
                        'class':'focus:shadow-primary-outline dark:bg-gray-950 dark:placeholder:text-white/80 dark:text-white/80 text-sm leading-5.6 ease block w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding p-3 font-normal text-gray-700 outline-none transition-all placeholder:text-gray-500 focus:border-fuchsia-300 focus:outline-none'
                  }
            )
      )

      def __init__(self, request=None, *args, **kwargs):
            self._username = None
            self._password = None
            self.request = request

            super().__init__(*args, **kwargs)

      def get_username(self) -> str:
            return self._username
      
      def get_password(self) -> str:
            return self._password
      
      def get_user_or_none(self) -> User | None:
            return  authenticate(self.request, username=self.get_username(), password=self.get_password())
            



      def get_username_by_email(self):
            email = self.cleaned_data['email']

            user = User.objects.filter(email=email).first()

            return user.username if user else None


      def clean(self):
            cleaned_data = super().clean()

            self._username = self.get_username_by_email()
            self._password = cleaned_data['password']

            return cleaned_data
      



