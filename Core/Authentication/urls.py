from django.urls import path
from Core.Authentication.views import *
urlpatterns = [
    path('', Login.as_view(), name='login_root'),
    path('logout/', LogoutView.as_view(), name='logout_root'),
]
