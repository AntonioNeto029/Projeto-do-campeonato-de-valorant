from django.urls import path
from . import views

urlpatterns = [
    
    #URLs para Home
    path('', views.home, name='home'),
    
    # URLs para Jogadores
    path('jogadores/', views.lista_jogador, name='lista_jogador'),
    path('jogadores/criar/', views.criar_jogador, name='criar_jogador'),
    path('jogadores/<int:pk>/atualizar/', views.atualizar_jogador, name='atualizar_jogador'),
    path('jogadores/<int:pk>/deletar/', views.deletar_jogador, name='deletar_jogador'),

    # URLs para Mapas
    path('mapas/', views.lista_mapa, name='lista_mapa'),
    path('mapas/criar/', views.criar_mapa, name='criar_mapa'),
    path('mapas/<int:pk>/atualizar/', views.atualizar_mapa, name='atualizar_mapa'),
    path('mapas/<int:pk>/deletar/', views.deletar_mapa, name='deletar_mapa'),

    # URLs para Partidas
    path('partidas/', views.lista_partidas, name='lista_partidas'),
    path('partidas/criar/', views.criar_partida, name='criar_partida'),
    path('partidas/<int:pk>/atualizar/', views.atualizar_partida, name='atualizar_partida'),
    path('partidas/<int:pk>/deletar/', views.deletar_partida, name='deletar_partida'),
]
