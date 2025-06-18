from django.urls import path
from controls.views import (
    signup,
    signout,
    SiginView
)

urlpatterns = [
    path('', SiginView.as_view(), name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
]
