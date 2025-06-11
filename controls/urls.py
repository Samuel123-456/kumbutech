from django.urls import path
from controls.views import (
    signin,
    signup,
    signout
)

urlpatterns = [
    path('', signin, name='signin'),
    path('signup/', signup, name='signup'),
    path('signout/', signout, name='signout'),
]
