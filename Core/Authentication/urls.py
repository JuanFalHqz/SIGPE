from django.urls import path,include
from Core.Authentication.views import *
urlpatterns = [
    path('', Login.as_view(), name='login_root')
]
