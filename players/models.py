from django.db import models


class Menu(models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Player(models.Model):
    nome = models.CharField(max_length=100)
    pontos_totais = models.IntegerField(default=0)
    acs = models.IntegerField(default=0)
    partidas_jogadas = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Mapa(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Time(models.Model):
    jogador_1 = models.ForeignKey(Player, related_name='time_jogador1', on_delete=models.CASCADE) 
    jogador_2 = models.ForeignKey(Player, related_name='time_jogador2', on_delete=models.CASCADE)
    jogador_3 = models.ForeignKey(Player, related_name='time_jogador3', on_delete=models.CASCADE)
    jogador_4 = models.ForeignKey(Player, related_name='time_jogador4', on_delete=models.CASCADE)
    jogador_5 = models.ForeignKey(Player, related_name='time_jogador5', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Time: {self.jogador_1}, {self.jogador_2}, {self.jogador_3}, {self.jogador_4}, {self.jogador_5}"
        
class Partida(models.Model):
    mapa_jogado = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    time_1 = models.ForeignKey(Time, related_name='partidas_como_time1', on_delete=models.CASCADE)
    time_2 = models.ForeignKey(Time, related_name='partidas_como_time2', on_delete=models.CASCADE)
    placar_time_1 = models.IntegerField(default=0)
    placar_time_2 = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.time_1} {self.placar_time_1} vs {self.time_2} {self.placar_time_2} - {self.mapa_jogado}"

class JogadorPartida(models.Model):
    jogador = models.ForeignKey(Player, on_delete=models.CASCADE)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE, default=1)
    acs = models.IntegerField(default=0)
    pontos_partida = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.jogador} - {self.partida} - {self.acs} - {self.pontos_partida}"