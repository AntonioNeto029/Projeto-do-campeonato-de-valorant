from django.db import models

# Create your models here.
class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField(default=0)
    acs = models.IntegerField(default=0)
    
    def __str__(self):
        return self.nome
    
    def dados_jogador(self):
        return self.pontuacao + ' ' + self.acs 
        
class Time(models.Model):
    jogador1 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jogador1')
    jogador2 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jogador2')
    jogador3 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jogador3')
    jogador4 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jogador4')
    jogador5 = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='jogador5')
    vencedor = models.BooleanField()
    
    def dados_time(self):
        return self.jogador1.nome + ' ' + self.jogador2.nome + ' ' + self.jogador3.nome + ' ' + self.jogador4.nome + ' ' + self.jogador5.nome
    
    def vencedor_partida(self):
        if self.vencedor == True:
            return self.vencedor
        elif self.vencedor == False:
            return self.vencedor     
    
class Mapa(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    
class Tabela_de_partidas(models.Model):
    mapa = models.ForeignKey(Mapa, on_delete=models.CASCADE)
    data = models.DateField()
    time1 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time1')
    time2 = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='time2')
    
    def dados_partida(self):
        return self.mapa.nome + ' ' + self.data + ' ' + self.time1.dados_time() + ' ' + self.time1.vencedor_partida() + ' ' + self.time2.dados_time() + ' ' + self.time2.vencedor_partida()
    
    
class Tabela_de_jogadores(models.Model):
    nickname = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='nickname')
    pontos_total = models.IntegerField(default=50)
    acs_total = models.ForeignKey(Jogador, on_delete=models.CASCADE, related_name='acs_total')
    media_de_acs =models.IntegerField(default=0)
    partidas_jogadas = models.IntegerField(default=0)
        
    
    def avarege_acs(self):
        media_de_acs = int(self.acs_total.acs) / int(self.partidas_jogadas)
        return int(self.media_de_acs)
    
    def dados_jogadores(self):
        return self.nickname.nome + ' ' + (self.pontos_total) + ' ' + (self.media_de_acs) + ' ' + (self.partidas_jogadas)
    
    
    
  
    