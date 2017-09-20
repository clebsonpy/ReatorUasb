from afluente import Afluente
from exception import Altura, Volume, Velocidade
from entrada import Entrada
import math


class Reator(object):


    def __init__(self, populacao, producao, tdh):
        self.tdh = tdh
        self.afluente = Afluente(populacao, producao)
    

    def volume(self):
        volumeMedia = (self.tdh * (self.afluente.vazaoMedia)/24) 
        return volumeMedia


    def nCelula(self, nCel = 1):
        volumeCelula = self.volume()/nCel
        try:
            if volumeCelula > 500:
                nCel += 1
                raise Volume
            else:
                return nCel

        except Volume:
            return self.nCelula(nCel)


    def volume_cada_reator(self):
        return self.volume()/self.nCelula()
    

    def altura_do_reator(self, altura = 5.5):
        velocidade = altura / self.tdh
        tdhm = (self.volume()/(self.afluente.vazaoMaxima/24))
        velocidadeMax = altura / tdhm

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
        area = self.volume_cada_reator()/self.altura_do_reator()
        return area


    def largura_comprimento(self):
        la = math.sqrt(self.area_util()/1.25)
        com = 1.25 * la
        return round(la,1), round(com,1)


    def verificar_tdh(self):
        volume = self.altura_do_reator() * self.largura_comprimento()[0] * self.largura_comprimento()[1]
        tdh2 = volume*3 / ((self.afluente.vazaoMedia)/24)
        if round(tdh2,1) == round(self.tdh,1):
            self.altura = self.altura_do_reator()
            self.largura = self.largura_comprimento()[0]
            self.comprimento = self.largura_comprimento()[1]
        else:
            return False
        
    def carga_hidraulica_volumetrica(self):
        carga = self.afluente.vazaoMedia / self.volume_reator()[0]
        return carga


    def carga_organica_volumetrica(self):
        concentaracaoSubstrato = Entrada('Concentração Substrato').input
        carga = (self.afluente.vazaoMedia * concentaracaoSubstrato)/self.volume_reator()[0]
        return carga


    def tempo_detencao_maxima(self):
        return self.volumeTotal / self.afluente.vazaoMaxima
