from django import forms
from .models import Player, Mapa, Time, Time, Partida, JogadorPartida, Menu


class MenuForm(forms.Form):
    class Meta:
        model = Menu
        fields = ['nome', 'link']

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['nome', 'pontos_totais', 'partidas_jogadas', 'acs']

class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nome']

class timeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['jogador_1', 'jogador_2', 'jogador_3', 'jogador_4', 'jogador_5']

class Time2Form(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['jogador_1', 'jogador_2', 'jogador_3', 'jogador_4', 'jogador_5']

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ['mapa_jogado', 'time_1', 'time_2', 'placar_time_1', 'placar_time_2']

class JogadorPartidaForm(forms.ModelForm):
    class Meta:
        model = JogadorPartida
        fields = ['jogador', 'partida', 'acs', 'pontos_partida']
