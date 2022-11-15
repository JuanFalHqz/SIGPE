from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

import SIGPE.settings


# Create your views here.
class Login(LoginView):
    template_name = 'login.html'

    # Si intentan loguearse, estando logueado retorna al dashboard
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard_root')
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
