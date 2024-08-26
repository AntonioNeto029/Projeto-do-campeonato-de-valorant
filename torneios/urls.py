from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='index'),  # Adiciona esta linha
 
#URLs Jogador
    path('jogadores/', views.listar_jogadores, name='listar_jogadores'),
    path('adicionar_jogador/', views.adicionar_jogador, name='adicionar_jogador'),
    path('editar_jogador/<int:pk>/', views.editar_jogador, name='editar_jogador'),
 
#URLs Partida
    path('listar_partidas/', views.listar_partidas, name='listar_partidas'),
    path('adicionar_partida/', views.adicionar_partida, name='adicionar_partida'),
    path('editar_partida/<int:pk>/', views.editar_partida, name='editar_partida'),
]