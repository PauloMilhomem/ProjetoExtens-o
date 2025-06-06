from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('doacao/', views.doacao, name='doacao'),
    path('atendimento/', views.atendimento, name='atendimento'),

    path('nossahistoria/', views.nossahistoria, name='nossahistoria'),

    path('governanca/', views.governanca, name='governanca'),

    path('transparencia/', views.transparencia, name='transparencia'),

    path('certificacoes/', views.certificacoes, name='certificacoes'),

    path('reabilitação/', views.reabilitacao, name='reabilitação'),

    path('sistema-restrito-afr/', views.sistema_restrito_afr, name='sistema-restrito-afr'),

    path('cooperacao/', views.cooperacao, name='cooperacao'),

    path('sac/', views.sac, name='sac'),

    path('visita/', views.visita, name='visita'),

    path('trabalheconosco/', views.trabalheconosco, name='trabalheconosco'),

    path('voluntariado/', views.voluntariado, name='voluntariado'),







]