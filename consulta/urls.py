# Para servir arquivos estáticos no desenvolvimento.
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.consulta_home),
    path('csv/', views.consulta_csv),
    path('json/', views.consulta_json),
    path('xlsx/', views.consulta_xlsx),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)