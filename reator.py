import math

from afluente import Afluente
from exception import Altura, Volume, Velocidade, Temperatura
from entrada import Entrada

class Reator():

    
    def __init__(self):
        
        self.afluente = Afluente()
        self.ent = Entrada()
        self.ent.reator()
        self.volume_total = self.volume()
        self.nCel = self.nCelula()
        self.volume_modulo = self.volume_cada_modulo()
        self.altura_reator = self.altura_do_reator()
        self.largura_modulo = self.largura_do_modulo()
        self.comprimento_reator = self.comprimento_do_reator()
        self.largura_cel = self.largura_do_modulo()
        self.area = self.area_modulo()
        self.pontos_descarga = self.pontos_de_descarga()
        self.eficienciaDQO = self.eficiencia_DQO()
        self.eficienciaDBO = self.eficiencia_DBO()
        self.efluenteDQO = self.DQO_efluente()
        self.efluenteDBO = self.DBO_efluente()
        self.prod_metano = self.prod_metano()
        self.biogas = self.prod_biogas()
        self.volume_lodo = self.prod_lodo()
        self.coletores_biogas = self.coletores_gas()
        self.abertura_simples_decan = self.abertura_para_decantador()
        self.lagura_decantacao = self.decantacao()
        
    
    
    def volume(self):
        V = (self.ent.tdh * (self.afluente.vazaoMedia)/24) 
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


    def volume_cada_modulo(self):
        return round((self.volume_total / self.nCel), 2)
    

    def altura_do_reator(self):
        velocidade = self.ent.altura / self.ent.tdh
        self.tdhm = (self.volume_total / (self.afluente.vazaoMaxima/24))
        velocidadeMax = self.ent.altura / self.tdhm

        try:
            if 4 <= self.ent.altura <= 6:
                try:
                    if round(velocidade, 2) <= 0.7 and round(velocidadeMax, 2) <= 1.2:
                        return round(self.ent.altura, 2)
                    else:
                        raise Velocidade
                except Velocidade:
                    self.ent.altura -= 0.1
                    return self.altura_do_reator()
            else:
                raise Altura
        except Altura:
            if self.ent.altura > 6:
                self.ent.altura -= 0.1
            else:
                self.ent.altura += 1
            return self.altura_do_reator()
                

    def area_modulo(self):
        area = self.volume_modulo / self.altura_reator
        return round(area, 2)


    def largura_do_modulo(self):
        la = math.sqrt(self.area_modulo() / 1.56)
        return round(la + 0.00499, 2)


    def comprimento_do_reator(self):
        compri = 1.56 * self.largura_modulo
        return round(compri + 0.00499, 2)

    def verificar_tdh(self):
        self.volume_reator = round(self.altura_reator * self.largura_modulo * self.comprimento_reator, 2)
        tdh2 = (self.volume_reator * self.nCel) / ((self.afluente.vazaoMedia) / 24)

        if round(tdh2, 1) == round(self.ent.tdh, 1):
            self.altura_reator = self.altura_do_reator()
            self.largura_reator = self.largura_do_modulo()
            self.comprimento_reator = self.comprimento_do_reator()
            self.volume_total = round(self.nCel * self.volume_reator, 2)
        else:
            self.ent.tdh = round(tdh2, 1)
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
        COV = (self.afluente.carga_diaria_media_DQO()) / self.volume_total
        return COV

    def pontos_de_descarga(self):
        raio = math.sqrt(self.ent.area_distr/3.1415)
        lado = raio*2
        nLarg = round(self.largura_modulo/lado)
        nComp = round(self.comprimento_reator/lado + 0.499)
        Nd = nComp * nLarg

        self.area_distr = self.area / Nd
        return round(Nd) * 2

    def eficiencia_DQO(self):
        E = 100*(1 - (0.68 * self.ent.tdh**(-0.35)))
        return round(E, 2)
    
    def eficiencia_DBO(self):
        E = 100*(1 - (0.70 * self.ent.tdh**(-0.5)))
        return round(E, 2)

    def DQO_efluente(self):
        return self.afluente.ent.DQO - (self.eficienciaDQO * self.afluente.ent.DQO)/100

    def DBO_efluente(self):
        return self.afluente.ent.DBO - (self.eficienciaDBO * self.afluente.ent.DBO)/100

    def prod_metano(self):
        aux = (self.afluente.ent.DQO/1000) - (self.efluenteDQO/1000)
        aux2 = self.afluente.ent.coef_prod_solidos_DQO * (self.afluente.ent.DQO/1000)
        dqo_metano = self.afluente.vazaoMedia * (aux-aux2)
        dqo_teo = 64/(0.08206 * (273 + self.afluente.ent.temperatura))

        return dqo_metano / dqo_teo

    def prod_biogas(self):
        return self.prod_metano / 0.75

    def prod_lodo(self):
        lodo = self.ent.coef_prod_solidos * self.afluente.carga_diaria_media_DQO()
        volume_lodo = lodo / (self.afluente.ent.densidade_lodo * (self.afluente.ent.concentração_esperada_lodo/100)) 
        return volume_lodo

    def coletores_gas(self):
        self.ent.coletores_gas()
        nCol = self.ent.nColetores * 2
        comprimento_col = nCol * self.largura_modulo
        area_coletores = comprimento_col * self.ent.largura_coletores
        if (self.prod_biogas()/24)/area_coletores < 1:
            return coletores_gas()

        return self.ent.largura_coletores

    def abertura_para_decantador(self):
        self.ent.abertura_para_decantador()
        abert_simples = 2 * self.nCel
        abert_duplas = (self.ent.nColetores - 1) * self.nCel
        nEquivalente_simples = abert_simples + abert_duplas * 2
        area_abertura = nEquivalente_simples * self.largura_modulo * self.ent.largura_abertura_decan
        
        velociade_med = (self.afluente.vazaoMedia/24) / area_abertura
        velociade_max = (self.afluente.vazaoMaxima/24) / area_abertura

        print(velociade_med)

        if  velociade_med > 2.5 and velociade_max > 4:
            return self.abertura_para_decantador()

        return self.ent.largura_abertura_decan

    def decantacao(self):
        comprimento_decan = self.nCel * self.largura_modulo * self.ent.nColetores
        largura_coletor_gas = self.coletores_biogas + 0.05
        largura_compartimento = round((self.comprimento_reator / self.ent.nColetores) + 0.00499, 2)
        largura_compartimento_util = largura_compartimento - 0.3
        area_decantadores = comprimento_decan * largura_compartimento_util
        velocidade_medio = (self.afluente.vazaoMedia/24)/area_decantadores
        velocidade_maximo = (self.afluente.vazaoMaxima/24)/area_decantadores
        altura_decantador =  

        #Separador
        angulo = 50
        largura_inclinada = (self.lagura_decantacao / 2) - self.ent.largura_abertura_decan
        altura_inclinada = math.tan(math.radians(angulo))*largura_inclinada
        


        if 0.6 < velociade_medio < 0.8 and velocidade_maximo < 1.2:
            return largura_compartimento_util
        
        
    def verificar_medidas(self, ):
        i
