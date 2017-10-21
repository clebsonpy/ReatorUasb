from entrada import Entrada


class Afluente(object):

    def __init__(self, populacao, producao, temperatura, concentracao = 0.6):
        
        self.populacao = populacao
        self.producao = producao
        self.concentracao = concentracao
        self.temperatura = temperatura
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

    def concentracao_diaria_maxima(self):
        """
        return: A estimativa das concentrações diária máxima de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMaxima * self.concentracao

    def concentracao_diaria_media(self):
        """
        return: A estimativa das concentrações diária média de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMedia * self.concentracao
