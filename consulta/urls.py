from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.consulta_home),
    path('csv/', views.consulta_csv),
    path('json/', views.consulta_json),
    path('xlsx/', views.consulta_xlsx),
]