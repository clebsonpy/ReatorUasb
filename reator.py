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
        self.volume_dec = self.volume_decantacao()
        self.trespasse_do_defletor = self.ent.trespasse()

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
        return round(COV, 2)

    def pontos_de_descarga(self):
        raio = math.sqrt(self.ent.area_distr/3.1415)
        lado = raio*2
        nLarg = round(self.largura_modulo/lado)
        nComp = round(self.comprimento_reator/lado + 0.499)
        Nd = nComp * nLarg

        self.area_distr = round(self.area / Nd, 2)
        return round(Nd) * 2

    def eficiencia_DQO(self):
        E = 100*(1 - (0.68 * self.ent.tdh**(-0.35)))
        return round(E, 2)

    def eficiencia_DBO(self):
        E = 100*(1 - (0.70 * self.ent.tdh**(-0.5)))
        return round(E, 2)

    def DQO_efluente(self):
        dqo = self.afluente.ent.DQO - (self.eficienciaDQO * self.afluente.ent.DQO)/100
        return round(dqo, 2)

    def DBO_efluente(self):
        dbo = self.afluente.ent.DBO - (self.eficienciaDBO * self.afluente.ent.DBO)/100
        return round(dbo, 2)

    def prod_metano(self):
        aux = (self.afluente.ent.DQO/1000) - (self.efluenteDQO/1000)
        aux2 = self.afluente.ent.coef_prod_solidos_DQO * (self.afluente.ent.DQO/1000)
        dqo_metano = self.afluente.vazaoMedia * (aux-aux2)
        dqo_teo = 64/(0.08206 * (273 + self.afluente.ent.temperatura))

        return round(dqo_metano / dqo_teo, 2)

    def prod_biogas(self):
        return round(self.prod_metano / 0.75, 2)

    def prod_lodo(self):
        lodo = self.ent.coef_prod_solidos * self.afluente.carga_diaria_media_DQO()
        volume_lodo = lodo / (self.afluente.ent.densidade_lodo * (self.afluente.ent.concentração_esperada_lodo/100))
        return round(volume_lodo, 2)

    def coletores_gas(self):
        try:
            nCol = self.ent.nColetores * self.nCel
            comprimento_col = nCol * self.largura_modulo
            area_coletores = comprimento_col * self.ent.largura_coletores

            self.taxa_biogas = (self.prod_biogas()/24)/area_coletores
            if  self.taxa_biogas <= 1:
                self.ent.largura_coletores -= 0.005
                return self.coletores_gas()


            return round(self.ent.largura_coletores, 2)
        
        except AttributeError:
            self.ent.coletores_gas()
            return self.coletores_gas()


    def abertura_para_decantador(self):
        try:
            abert_simples = 2 * self.nCel
            abert_duplas = (self.ent.nColetores - 1) * self.nCel
            nEquivalente_simples = abert_simples + abert_duplas * 2
            area_abertura = nEquivalente_simples * self.largura_modulo * self.ent.largura_abertura_decan

            velociade_med = (self.afluente.vazaoMedia/24) / area_abertura
            velociade_max = (self.afluente.vazaoMaxima/24) / area_abertura
            if  velociade_med > 2.5 and velociade_max > 4:
                self.ent.largura_abertura_decan += 0.01
                print(self.ent.largura_abertura_decan)
                return self.abertura_para_decantador()

            return round(self.ent.largura_abertura_decan, 2)

        except AttributeError:
            self.ent.abertura_para_decantador()
            return self.abertura_para_decantador()


    def largura_decantacao(self):
        comprimento_decan = self.nCel * self.largura_modulo * self.ent.nColetores
        largura_coletor_gas = self.coletores_biogas + (2 * 0.025)
        largura_compartimento = round((self.comprimento_reator / self.ent.nColetores) + 0.00499, 2)
        largura_compartimento_util = largura_compartimento - largura_coletor_gas
        area_decantadores = comprimento_decan * largura_compartimento_util

        velocidade_med = (self.afluente.vazaoMedia/24)/area_decantadores
        velocidade_max = (self.afluente.vazaoMaxima/24)/area_decantadores

        if 0.6 < velocidade_med < 0.8 and velocidade_max < 1.2:
            return round(largura_compartimento_util, 2)

        elif self.taxa_biogas >= 1:
            if 0.6 > velocidade_med:
                sinal = 1
            elif 0.7 < velocidade_med:
                sinal = -1

            self.ent.largura_coletores += (0.005*sinal)
            self.coletores_gas()
            self.largura_decantacao()

    def volume_decantacao(self):
        #Separador
        try:
            self.largura_compartimento_util = self.largura_decantacao()
            self.laba_i = (self.largura_compartimento_util / 2) - self.abertura_simples_decan
            area_dec_1 = self.laba_i * self.ent.altura_h1_inclinada / 2
            area_dec_2 = self.ent.altura_h1_inclinada * (2 * self.abertura_simples_decan)
            area_dec_3 = self.ent.altura_h2_vertical * self.largura_compartimento_util
            area_dec = 2 * area_dec_1 + area_dec_2 + area_dec_3
            volume_dec = self.ent.nColetores * self.nCel * self.largura_modulo * area_dec

            self.angulo = round(math.degrees(math.atan(self.ent.altura_h1_inclinada/self.laba_i)), 2)
            
            if self.angulo < 50:
                self.ent.altura_h1_inclinada += 0.1
                self.volume_decantacao()
            else:
                tdh_dec_med = volume_dec / (self.afluente.vazaoMedia/24)
                tdh_dec_max = volume_dec / (self.afluente.vazaoMaxima/24)
                print("TDH: ", tdh_dec_med, tdh_dec_max)
                if tdh_dec_med <= 1.5 and tdh_dec_max <= 1:
                    if self.angulo == 50:
                        self.ent.altura_h2_vertical += 0.05
                        print(self.ent.altura_h2_vertical)
                        self.volume_decantacao()

                    else:
                        self.ent.altura_h1_inclinada += 0.1
                        self.volume_decantacao()


                return round(volume_dec, 2)

        except AttributeError:
            self.ent.altura_decantador()
            return self.volume_decantacao()