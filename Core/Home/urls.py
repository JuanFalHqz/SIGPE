from django.urls import path
from Core.Home.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home_root'),
]
