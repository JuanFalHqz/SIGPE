from django.urls import path
from Core.ProjectProcesses.views import *
urlpatterns = [
    path('', ListViewProjects.as_view(), name='project_list_root'),
    path('create/', CreateViewProjects.as_view(), name='project_create_root'),
    path('update/<int:pk>/', UpdateViewProject.as_view(), name='project_update_root'),
    path('delete', DeleteViewProject.as_view(), name='project_delete_root'),
]
