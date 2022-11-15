from builtins import super

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView


# Create your views here.

class DashboardView(TemplateView):
    template_name = 'Dashboard.html'
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)