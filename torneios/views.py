from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogador, Partida
from .forms import JogadorForm, PartidaForm
import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'paginas/index.html')

# CRUD Jogador

def listar_jogadores(request):
    jogadores = Jogador.objects.all()
    return render(request, 'paginas/listar_jogadores.html', {'jogadores': jogadores})

def adicionar_jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores')
    else:
        form = JogadorForm()
    return render(request, 'paginas/adicionar_jogador.html', {'form': form})

def editar_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores')
    else:
        form = JogadorForm(instance=jogador)
    return render(request, 'paginas/editar_jogador.html', {'form': form})

# def remover_jogador(request, pk):
#     jogador = get_object_or_404(Jogador, pk=pk)
#     jogador.delete()
#     return redirect('listar_jogadores')

# CRUD Partida

def listar_partidas(request):
    partidas = Partida.objects.all()
    return render(request, 'paginas/listar_partidas.html', {'partidas': partidas})

def adicionar_partida(request):
    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            try:
                partida = form.save()
                logger.info(f"Partida adicionada com sucesso! ID: {partida.id}")
                return redirect('listar_partidas')
            except Exception as e:
                logger.error(f"Erro ao salvar a partida: {str(e)}")
        else:
            logger.warning(f"Formulário inválido: {form.errors}")
    else:
        form = PartidaForm()
    return render(request, 'paginas/adicionar_partida.html', {'form': form})

def editar_partida(request, pk):
    partida = get_object_or_404(Partida, pk=pk)
    if request.method == 'POST':
        form = PartidaForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('listar_partidas')
    else:
        form = PartidaForm(instance=partida)
    return render(request, 'paginas/editar_partida.html', {'form': form, 'partida': partida})

# def remover_partida(request, pk):
#     partida = get_object_or_404(Partida, pk=pk)
#     partida.delete()
#     return redirect('listar_partidas')