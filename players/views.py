from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Mapa, Time_1, Time_2, Partida, JogadorPartida
from .forms import PlayerForm, MapaForm, Time1Form, Time2Form, PartidaForm, JogadorPartidaForm

# CRUD para Jogadores
def lista_jogadores(request):
    jogadores = Player.objects.all()
    return render(request, 'torneio/lista_jogador.html', {'jogadores': jogadores})

def criar_jogador(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = PlayerForm()
    return render(request, 'torneio/form_jogador.html', {'form': form})

def criar_jogador(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = PlayerForm()
    return render(request, 'torneio/form_jogador.html', {'form': form})

def atualizar_jogador(request, pk):
    jogador = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('lista_jogadores')
    else:
        form = PlayerForm(instance=jogador)
    return render(request, 'torneio/form_jogador.html', {'form': form})

def deletar_jogador(request, pk):
    jogador = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        jogador.delete()
        return redirect('lista_jogadores')
    return render(request, 'torneio/deletar_jogador.html', {'jogador': jogador})

# CRUD para Mapas
def lista_mapas(request):
    mapas = Mapa.objects.all()
    return render(request, 'torneio/lista_mapa.html', {'mapas': mapas})

def criar_mapa(request):
    if request.method == 'POST':
        form = MapaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mapas')
    else:
        form = MapaForm()
    return render(request, 'torneio/form_mapa.html', {'form': form})

def atualizar_mapa(request, pk):
    mapa = get_object_or_404(Mapa, pk=pk)
    if request.method == 'POST':
        form = MapaForm(request.POST, instance=mapa)
        if form.is_valid():
            form.save()
            return redirect('lista_mapas')
    else:
        form = MapaForm(instance=mapa)
    return render(request, 'torneio/form_mapa.html', {'form': form})

def deletar_mapa(request, pk):
    mapa = get_object_or_404(Mapa, pk=pk)
    if request.method == 'POST':
        mapa.delete()
        return redirect('lista_mapas')
    return render(request, 'torneio/confirmar_deletar_mapa.html', {'mapa': mapa})

# CRUD para Partidas
def lista_partidas(request):
    partidas = Partida.objects.all()
    return render(request, 'torneio/lista_partidas.html', {'partidas': partidas})

def criar_partida(request):
    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partidas')
    else:
        form = PartidaForm()
    return render(request, 'torneio/form_partida.html', {'form': form})

def atualizar_partida(request, pk):
    partida = get_object_or_404(Partida, pk=pk)
    if request.method == 'POST':
        form = PartidaForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('lista_partidas')
    else:
        form = PartidaForm(instance=partida)
    return render(request, 'torneio/form_partida.html', {'form': form})

def deletar_partida(request, pk):
    partida = get_object_or_404(Partida, pk=pk)
    if request.method == 'POST':
        partida.delete()
        return redirect('lista_partidas')
    return render(request, 'torneio/deletar_partida.html', {'partida': partida})
