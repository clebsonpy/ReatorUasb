import math

from afluente import Afluente
from exception import Altura, Volume, Velocidade
from entrada import Entrada


class Reator():


    def __init__(self, populacao, producao, tdh):
        self.tdh = tdh
        self.afluente = Afluente(populacao, producao)
        self.volume_total = self.volume()
        self.nCel = self.nCelula()
        self.volume_reator = self.volume_cada_reator()
        self.altura_reator = self.altura_do_reator()
        self.largura_reator = self.largura_do_reator()
        self.comprimento_reator = self.comprimento_do_reator()
    

    def volume(self):
        volumeMedia = (self.tdh * (self.afluente.vazaoMedia)/24) 
        return round(volumeMedia, 2)


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
        return self.volume_total / self.nCel
    

    def altura_do_reator(self, altura = 5):
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
        return round(area, 1)


    def largura_do_reator(self):
        la = math.sqrt(self.area_util() / 1.25)
        return round(la, 1)


    def comprimento_do_reator(self):
        compri = 1.25 * self.largura_reator
        return round(compri, 1)

    def verificar_tdh(self):
        volume = self.altura_reator * self.largura_reator * self.comprimento_reator
        tdh2 = (volume * self.nCel) / ((self.afluente.vazaoMedia) / 24)

        if round(tdh2, 1) == round(self.tdh, 1):
            self.altura_reator = self.altura_do_reator()
            self.largura_reator = self.largura_do_reator()
            self.comprimento_reator = self.comprimento_do_reator()
            self.volume_total = self.nCel * (self.altura_reator * self.largura_reator * self.comprimento_reator)
        else:
            self.tdh = round(tdh2, 1)
            self.verificar_tdh()

        
    def carga_hidraulica_volumetrica(self):
        carga = self.afluente.vazaoMedia / self.volume_total
        return round(carga, 2)
    

    def velocidade_ascencional(self):
        velocidade = self.altura_reator / self.tdh
        return round(velocidade, 2)


    def carga_organica_volumetrica(self):
        carga = (self.afluente.vazaoMedia * self.afluente.concentracao) / self.volume_total
        return carga