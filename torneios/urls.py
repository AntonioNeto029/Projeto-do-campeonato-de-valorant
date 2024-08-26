from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='index'),  # Adiciona esta linha
 
#URLs Jogador
    path('listar_jogadores/', views.listar_jogadores, name='listar_jogadores'),
    path('adicionar_jogador/', views.adicionar_jogador, name='adicionar_jogador'),
    path('editar_jogador/<int:pk>/', views.editar_jogador, name='editar_jogador'),
    path('remover_jogador/<int:pk>/', views.remover_jogador, name='remover_jogador'),
 
#URLs Time
    path('listar_times/', views.listar_times, name='listar_times'),
    path('adicionar_time/', views.adicionar_time, name='adicionar_time'),
    path('editar_time/<int:pk>/', views.editar_time, name='editar_time'),
    path('remover_time/<int:pk>/', views.remover_time, name='remover_time'),
    
#URLs Partida
    path('listar_partidas/', views.listar_partidas, name='listar_partidas'),
    path('adicionar_partida/', views.adicionar_partida, name='adicionar_partida'),
    path('editar_partida/<int:pk>/', views.editar_partida, name='editar_partida'),
    path('remover_partida/<int:pk>/', views.remover_partida, name='remover_partida'),

#URLs Mapa
    path('listar_mapas/', views.listar_mapas, name='listar_mapas'),
    path('adicionar_mapa/', views.adicionar_mapa, name='adicionar_mapa'),
    path('editar_mapa/<int:pk>/', views.editar_mapa, name='editar_mapa'),
    path('remover_mapa/<int:pk>/', views.remover_mapa, name='remover_mapa'),

    
    
    
    
    
    
]