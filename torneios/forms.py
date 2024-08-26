from django import forms
from .models import Jogador, Partida

class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'pontuacao']

from django import forms
from .models import Partida, Jogador

class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = '__all__'