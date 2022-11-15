from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

from SIGPE import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('Core.Dashboard.urls')),
    path('login/',include('Core.Authentication.urls')),
    path('',include('Core.Home.urls')),
    path('projects/',include('Core.ProjectProcesses.urls')),
]
#Configuración que permite cargar archivos media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)