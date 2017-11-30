from entrada import Entrada


class Afluente():

    def __init__(self):
        self.ent = Entrada()
        self.ent.afluente()
        self.vazaoMedia = self.vazao_media()
        self.vazaoMaxima = self.vazao_maxima()

    def vazao_media(self):
        """
        return: Vazão Média de esgoto (m³/dia)
        """
        return self.ent.populacao * self.ent.contribuicao

    def vazao_maxima(self):
        """
        return: Vazão Máxima de esgoto (m³/dia)
        """
        return self.vazaoMedia * 1.5 * 1.2

    def carga_diaria_maxima_DQO(self):
        """
        return: A estimativa das concentrações diária máxima de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMaxima * (self.ent.DQO/1000)

    def carga_diaria_maxima_DBO(self):
        """
        return: A estimativa das concentrações diária máxima de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMaxima * (self.ent.DBO/1000)

    def carga_diaria_media_DQO(self):
        """
        return: A estimativa das concentrações diária média de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMedia * (self.ent.DQO/1000)

    def carga_diaria_media_DBO(self):
        """
        return: A estimativa das concentrações diária média de 
                DBO e DQO no afluente (kg/dia)
        """
        return self.vazaoMedia * (self.ent.DBO/1000)
