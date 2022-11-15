from django.urls import path,include
from Core.Authentication.views import *
from Core.Dashboard.views import DashboardView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard_root')
]
