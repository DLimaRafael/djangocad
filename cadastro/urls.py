# Para servir arquivos estáticos no desenvolvimento.
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)