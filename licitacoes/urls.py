from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_licitacoes, name='lista_licitacoes')
]
