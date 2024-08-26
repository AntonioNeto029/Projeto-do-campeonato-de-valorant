from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField()

    def __str__(self):
        return self.nome

class Partida(models.Model):
    mapa = models.CharField(max_length=100)
    data = models.DateField()
    
    jogador1_time1 = models.ForeignKey(Jogador, related_name='partidas_time1_jogador1', on_delete=models.CASCADE)
    jogador2_time1 = models.ForeignKey(Jogador, related_name='partidas_time1_jogador2', on_delete=models.CASCADE)
    jogador3_time1 = models.ForeignKey(Jogador, related_name='partidas_time1_jogador3', on_delete=models.CASCADE)
    jogador4_time1 = models.ForeignKey(Jogador, related_name='partidas_time1_jogador4', on_delete=models.CASCADE)
    jogador5_time1 = models.ForeignKey(Jogador, related_name='partidas_time1_jogador5', on_delete=models.CASCADE)
    
    jogador1_time2 = models.ForeignKey(Jogador, related_name='partidas_time2_jogador1', on_delete=models.CASCADE)
    jogador2_time2 = models.ForeignKey(Jogador, related_name='partidas_time2_jogador2', on_delete=models.CASCADE)
    jogador3_time2 = models.ForeignKey(Jogador, related_name='partidas_time2_jogador3', on_delete=models.CASCADE)
    jogador4_time2 = models.ForeignKey(Jogador, related_name='partidas_time2_jogador4', on_delete=models.CASCADE)
    jogador5_time2 = models.ForeignKey(Jogador, related_name='partidas_time2_jogador5', on_delete=models.CASCADE)
    
    acs1_time1 = models.IntegerField()
    acs2_time1 = models.IntegerField()
    acs3_time1 = models.IntegerField()
    acs4_time1 = models.IntegerField()
    acs5_time1 = models.IntegerField()
    
    acs1_time2 = models.IntegerField()
    acs2_time2 = models.IntegerField()
    acs3_time2 = models.IntegerField()
    acs4_time2 = models.IntegerField()
    acs5_time2 = models.IntegerField()

    def __str__(self):
        return f"Partida em {self.mapa} em {self.data}"