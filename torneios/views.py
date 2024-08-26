from django.shortcuts import render, redirect, get_object_or_404
from .models import Jogador, Time, Mapa, Tabela_de_partidas, Tabela_de_jogadores
from .forms import JogadorForm, TimeForm, MapaForm, Tabela_de_partidasForm, Tabela_de_jogadoresForm


def home(request):
    return render(request, 'paginas/index.html')

#CRUD Jogador

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

def remover_jogador(request, pk):
    jogador = get_object_or_404(Jogador, pk=pk)
    jogador.delete()
    return redirect('listar_jogadores')

#CRUD Time

def listar_times(request):
    times = Time.objects.all()
    return render(request, 'paginas/listar_times.html', {'times': times})

def adicionar_time(request):
    if request.method == 'POST':
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_times')
    else:
        form = TimeForm()
    return render(request, 'paginas/adicionar_time.html', {'form': form})

def editar_time(request, pk):
    time = get_object_or_404(Time, pk=pk)
    if request.method == 'POST':
        form = TimeForm(request.POST, instance=time)
        if form.is_valid():
            form.save()
            return redirect('listar_times')
    else:
        form = TimeForm(instance=time)
    return render(request, 'paginas/editar_time.html', {'form': form})

def remover_time(request, pk):
    time = get_object_or_404(Time, pk=pk)
    time.delete()
    return redirect('listar_times')

#CRUD Mapa

def listar_mapas(request):
    mapas = Mapa.objects.all()
    return render(request, 'paginas/listar_mapas.html', {'mapas': mapas})

def adicionar_mapa(request):
    if request.method == 'POST':
        form = MapaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_mapas')
    else:
        form = MapaForm()
    return render(request, 'paginas/adicionar_mapa.html', {'form': form})

def editar_mapa(request, pk):
    mapa = get_object_or_404(Mapa, pk=pk)
    if request.method == 'POST':
        form = MapaForm(request.POST, instance=mapa)
        if form.is_valid():
            form.save()
            return redirect('listar_mapas')
    else:
        form = MapaForm(instance=mapa)
    return render(request, 'paginas/editar_mapa.html', {'form': form})

def remover_mapa(request, pk):
    mapa = get_object_or_404(Mapa, pk=pk)
    mapa.delete()
    return redirect('listar_mapas')

#CRUD Tabela_de_partidas

def listar_partidas(request):
    partidas = Tabela_de_partidas.objects.all()
    return render(request, 'paginas/listar_partidas.html', {'partidas': partidas})

def adicionar_partida(request):
    if request.method == 'POST':
        form = Tabela_de_partidasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_partidas')
    else:
        form = Tabela_de_partidasForm()
    return render(request, 'paginas/adicionar_partida.html', {'form': form})

def editar_partida(request, pk):
    partida = get_object_or_404(Tabela_de_partidas, pk=pk)
    if request.method == 'POST':
        form = Tabela_de_partidasForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('listar_partidas')
    else:
        form = Tabela_de_partidasForm(instance=partida)
    return render(request, 'paginas/editar_partida.html', {'form': form})

def remover_partida(request, pk):
    partida = get_object_or_404(Tabela_de_partidas, pk=pk)
    partida.delete()
    return redirect('listar_partidas')

#CRUD Tabela_de_jogadores

def listar_jogadores_tabela(request):
    jogadores_tabela = Tabela_de_jogadores.objects.all()
    return render(request, 'paginas/listar_jogadores_tabela.html', {'jogadores_tabela': jogadores_tabela})

def adicionar_jogador_tabela(request):
    if request.method == 'POST':
        form = Tabela_de_jogadoresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores_tabela')
    else:
        form = Tabela_de_jogadoresForm()
    return render(request, 'paginas/adicionar_jogador_tabela.html', {'form': form})

def editar_jogador_tabela(request, pk):
    jogador_tabela = get_object_or_404(Tabela_de_jogadores, pk=pk)
    if request.method == 'POST':
        form = Tabela_de_jogadoresForm(request.POST, instance=jogador_tabela)
        if form.is_valid():
            form.save()
            return redirect('listar_jogadores_tabela')
    else:
        form = Tabela_de_jogadoresForm(instance=jogador_tabela)
    return render(request, 'paginas/editar_jogador_tabela.html', {'form': form})

def remover_jogador_tabela(request, pk):
    jogador_tabela = get_object_or_404(Tabela_de_jogadores, pk=pk)
    jogador_tabela.delete()
    return redirect('listar_jogadores_tabela')


