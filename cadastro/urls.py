from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrar_pessoa, name='formulario'),
    path('sucesso/', views.sucesso, name='sucesso'),
    path('qualquer/', views.pagina_qualquer, name='pagina_qualquer')
]
