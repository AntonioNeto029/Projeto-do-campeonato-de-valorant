from django import forms
from .models import Player, Mapa, Time_1, Time_2, Partida, JogadorPartida, Menu


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

class Time1Form(forms.ModelForm):
    class Meta:
        model = Time_1
        fields = ['jogador_1', 'jogador_2', 'jogador_3', 'jogador_4', 'jogador_5']

class Time2Form(forms.ModelForm):
    class Meta:
        model = Time_2
        fields = ['jogador_1', 'jogador_2', 'jogador_3', 'jogador_4', 'jogador_5']

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ['mapa_jogado', 'time_1', 'time_2', 'placar_time_1', 'placar_time_2']

class JogadorPartidaForm(forms.ModelForm):
    class Meta:
        model = JogadorPartida
        fields = ['jogador', 'Partida', 'acs', 'pontos_partida']