from django import forms
from .models import Jogador, Time, Mapa, Tabela_de_partidas, Tabela_de_jogadores

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'pontuacao', 'acs']  

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['jogador1', 'jogador2', 'jogador3', 'jogador4', 'jogador5', 'vencedor']

class MapaForm(forms.ModelForm):
    class Meta:
        model = Mapa
        fields = ['nome']
        
class Tabela_de_partidasForm(forms.ModelForm):
    class Meta:
        model = Tabela_de_partidas
        fields = ['mapa', 'data', 'time1', 'time2']
        
class Tabela_de_jogadoresForm(forms.ModelForm):
    class Meta:
        model = Tabela_de_jogadores
        fields = ['nickname', 'pontos_total', 'acs_total', 'media_de_acs', 'partidas_jogadas']
        
