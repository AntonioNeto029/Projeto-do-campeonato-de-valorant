from django.db import models



class Player(models.Model):
    nome = models.CharField(max_length=200)
    pontos_totais = models.IntegerField(default=50)
    partidas_jogadas = models.IntegerField(default=0)
    acs = models.IntegerField(default=0)
    

    def media_de_pontos_partidas(self):
        return self.acs/self.partidas_jogadas

    def soma_de_pontos(self):
        return self.pontos_totais
    
    def __str__(self):
        return self.name

class Mapa(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome
    
class Partida(models.Model):
    mapa_jogado = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    time_1 = models.CharField(max_length=100)
    time_2 = models.CharField(max_length=100)
    placar_time_1 = models.IntegerField(default=0)
    placar_time_2 = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.time_1} vs {self.time_2} - {self.mapa_jogado}"
    
class JogadorPartida(models.Model):
    jogador = models.ForeignKey(Player, on_delete=models.CASCADE)
         