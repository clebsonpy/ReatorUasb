import math

from afluente import Afluente
from exception import Altura, Volume, Velocidade, Temperatura
from entrada import Entrada


class Reator():

    
    def __init__(self, populacao, producao, temperatura, concentracao = 0.6):
        self.afluente = Afluente(populacao, producao, temperatura, concentracao)
        self.tdh = self.tempo_detencao_hidraulica()
        self.volume_total = self.volume()
        self.nCel = self.nCelula()
        self.volume_reator = self.volume_cada_reator()
        self.altura_reator = self.altura_do_reator()
        self.largura_reator = self.largura_do_reator()
        self.comprimento_reator = self.comprimento_do_reator()
        self.area = self.area_util()
        self.pontos_descarga = self.pontos_de_descarga()
        self.eficienciaDQO = self.eficiencia_DQO()
        self.eficienciaDBO = self.eficiencia_DBO()
    
    def tempo_detencao_hidraulica(self):
        """
        return: Tempo de detenção hidráulica de acordo com a temperatura
        """
        try:
            if 16 <= self.afluente.temperatura < 20:
                return float(input("Tempo entre 9 < tdh <= 14: "))

            elif 20 <= self.afluente.temperatura < 26:
                return float(input("Tempo entre 6 < tdh <= 9: "))
            
            elif self.afluente.temperatura > 26:
                return float(input("Tempo entre tdh >= 6: "))

            else:
                raise Temperatura

        except Temperatura:
            self.afluente.temperatura = float(input("Nova Temperatura: "))
            return self.tempo_detencao_hidraulica()
            
            
    def volume(self):
        V = (self.tdh * (self.afluente.vazaoMedia)/24) 
        return round(V, 2)


    def nCelula(self, nCel = 1):
        volumeCelula = self.volume_total / nCel
        try:
            if volumeCelula > 500:
                nCel += 1
                raise Volume
            else:
                return nCel

        except Volume:
            return self.nCelula(nCel)


    def volume_cada_reator(self):
        return round((self.volume_total / self.nCel), 2)
    

    def altura_do_reator(self, altura = float(input("Altura do Reator (m): "))):
        velocidade = altura / self.tdh
        self.tdhm = (self.volume_total / (self.afluente.vazaoMaxima/24))
        velocidadeMax = altura / self.tdhm

        try:
            if 4 <= altura <= 6:
                try:
                    if round(velocidade, 2) <= 0.7 and round(velocidadeMax, 2) <= 1.2:
                        return round(altura, 2)
                    else:
                        raise Velocidade
                except Velocidade:
                    altura -= 0.1
                    return self.altura_do_reator(altura)
            else:
                raise Altura
        except Altura:
            if altura > 6:
                altura -= 0.1
            else:
                altura += 1
            return self.altura_do_reator(altura)
                

    def area_util(self):
        area = self.volume_reator / self.altura_reator
        return round(area, 2)


    def largura_do_reator(self):
        la = math.sqrt(self.area_util() / 1.25)
        return round(la + 0.00499, 2)


    def comprimento_do_reator(self):
        compri = 1.25 * self.largura_reator
        return round(compri + 0.00499, 2)

    def verificar_tdh(self):
        self.volume_reator = round(self.altura_reator * self.largura_reator * self.comprimento_reator, 2)
        tdh2 = (self.volume_reator * self.nCel) / ((self.afluente.vazaoMedia) / 24)

        if round(tdh2, 1) == round(self.tdh, 1):
            self.altura_reator = self.altura_do_reator()
            self.largura_reator = self.largura_do_reator()
            self.comprimento_reator = self.comprimento_do_reator()
            self.volume_total = round(self.nCel * self.volume_reator, 2)
        else:
            self.tdh = round(tdh2, 1)
            self.verificar_tdh()

        
    def carga_hidraulica_volumetrica_media(self):
        CHV = self.afluente.vazaoMedia / self.volume_total
        return round(CHV, 2)

    def carga_hidraulica_volumetrica_maxima(self):
        CHV = self.afluente.vazaoMaxima / self.volume_total
        return round(CHV, 2)
    

    def velocidade_superficial_fluxo_media(self):
        v = ((self.afluente.vazaoMedia/24) * self.altura_reator) / self.volume_total
        return round(v, 2)

    def velocidade_superficial_fluxo_maxima(self):
        v = ((self.afluente.vazaoMaxima/24) * self.altura_reator) / self.volume_total
        return round(v, 2)

    def carga_organica_volumetrica(self):
        COV = ((self.afluente.vazaoMedia/24) * self.afluente.concentracao) / self.volume_total
        return COV

    def pontos_de_descarga(self, area = float(input("Área de Influencia de cada distribuidor: "))):
        Nd = self.area / area
        return round(Nd) * 2

    def eficiencia_DQO(self):
        E = 100*(1 - (0.68 * self.tdh**(-0.35)))
        return round(E, 2)
    
    def eficiencia_DBO(self):
        E = 100*(1 - (0.70 * self.tdh**(-0.5)))
        return round(E, 2)