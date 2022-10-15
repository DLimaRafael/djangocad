from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # CADASTRO DE USUÁRIOS
    path('', include('cadastro.urls')),
    path('cadastro/', include('cadastro.urls')),
    # CONSULTA
    path('consulta/', include('consulta.urls')),
    # ADMIN
    path('admin/', admin.site.urls),
]
