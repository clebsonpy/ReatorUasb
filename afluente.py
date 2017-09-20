from entrada import Entrada


class Afluente(object):

    def __init__(self, populacao, producao):
        """
        populacao: População Atendida;
        producao: Esgoto produzido por pessoa
        """
        self.populacao = populacao
        self.producao = producao
        self.vazaoMedia = self.vazao_media()
        self.vazaoMaxima = self.vazao_maxima()

    def vazao_media(self):
        """
        return: Vazão Média de esgoto (m³/dia)
        """
        return self.populacao * self.producao

    def vazao_maxima(self):
        """
        return: Vazão Máxima de esgoto (m³/dia)
        """
        return self.vazaoMedia * 1.5 * 1.2

    def concentracao_diaria(self):
        """
        input: Concentração de DBO ou DQO (kg/m³)
        return: A estimativa das concentrações diária de 
                DBO e DQO no afluente (kg/dia)
        """
        concentracao = Entrada('Concentração').input
        return (self.vazaoMedia * concentracao, self.vazaoMaxima * concentracao)