from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

import SIGPE.settings


# Create your views here.
class Login(LoginView):
    template_name = 'login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['u'] = SIGPE.settings.STATIC_URL
        return context

class LogoutView(LogoutView):
    template_name = 'login.html'