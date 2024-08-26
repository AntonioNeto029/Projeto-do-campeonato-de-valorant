from django.db import models


class Menu(models.Model):
    nome = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

class Player(models.Model):
    nome = models.CharField(max_length=200)
    pontos_totais = models.IntegerField(default=50)
    partidas_jogadas = models.IntegerField(default=0)
    acs = models.IntegerField(default=0)
    

    def media_de_pontos_partidas(self):
        if self.partidas_jogadas > 0:
            return self.acs/self.partidas_jogadas
        return 0

    def soma_de_pontos(self):
        return self.pontos_totais
    
    def __str__(self):
        return self.name

class Mapa(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Time_1(models.Model):
    jogador_1 = models.ForeignKey(Player, related_name='time1_jogador1', on_delete=models.CASCADE) 
    jogador_2 = models.ForeignKey(Player, related_name='time1_jogador2', on_delete=models.CASCADE)
    jogador_3 = models.ForeignKey(Player, related_name='time1_jogador3', on_delete=models.CASCADE)
    jogador_4 = models.ForeignKey(Player, related_name='time1_jogador4', on_delete=models.CASCADE)
    jogador_5 = models.ForeignKey(Player, related_name='time1_jogador5', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Time 1: {self.jogador_1}, {self.jogador_2}, {self.jogador_3}, {self.jogador_4}, {self.jogador_5}"
        
class Time_2(models.Model):
    jogador_1 = models.ForeignKey(Player, related_name='time2_jogador1', on_delete=models.CASCADE)
    jogador_2 = models.ForeignKey(Player, related_name='time2_jogador2', on_delete=models.CASCADE)
    jogador_3 = models.ForeignKey(Player, related_name='time2_jogador3', on_delete=models.CASCADE)
    jogador_4 = models.ForeignKey(Player, related_name='time2_jogador4', on_delete=models.CASCADE)
    jogador_5 = models.ForeignKey(Player, related_name='time2_jogador5', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Time 2: {self.jogador_1}, {self.jogador_2}, {self.jogador_3}, {self.jogador_4}, {self.jogador_5}"
        
class Partida(models.Model):
    mapa_jogado = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    time_1 = models.ForeignKey(Time_1, on_delete=models.CASCADE)
    time_2 = models.ForeignKey(Time_2, on_delete=models.CASCADE)
    placar_time_1 = models.IntegerField(default=0)
    placar_time_2 = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.time_1, self.placar_time_1} vs {self.time_2, self.placar_time_2} - {self.mapa_jogado}"
    
class JogadorPartida(models.Model):
    jogador = models.ForeignKey(Player, on_delete=models.CASCADE)
    Partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    acs = models.IntegerField(default=0)
    pontos_partida = models.IntegerField(default=0)   
    
    def __str__(self):
        return f"{self.jogador} - {self.Partida} - {self.acs} - {self.pontos_partida}"