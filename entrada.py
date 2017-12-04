from exception import Temperatura


class Entrada(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.populacao = int(input('População: '))
            cls.contribuicao = float(input("Esgoto por pessoa (m³/dia): "))
            cls.temperatura = float(input("Temperatura (ºC): "))
        return cls._instance

    def afluente(self):
        self.DQO = float(input("DQO(mg/l): "))
        self.DBO = float(input("DBO(mg/l): "))
        self.coef_prod_solidos = float(
            input("Coefieciente de podução de sólidos(kgSST/kgDQO): "))
        self.coef_prod_solidos_DQO = float(input
            ("Coeficiente de produção de sólidos em DQO(kgDQO/kgDQO): "))
        self.concentração_esperada_lodo = float(input
            ("Concentração esperado para lodo descarte(%): "))
        self.densidade_lodo = float(input("Densidade do lodo(kgSST/m³): "))

    def reator(self):
        try:
            if 16 <= self.temperatura < 20:
                self.tdh = float(input("Tempo entre 9 < tdh <= 14: "))

            elif 20 <= self.temperatura < 26:
                self.tdh = float(input("Tempo entre 6 < tdh <= 9: "))

            elif self.temperatura > 26:
                self.tdh = float(input("Tempo entre tdh >= 6: "))
            else:
                raise Temperatura
        except Temperatura:
            self.temperatura = float(input("Temperatura (ºC): "))
            return self.reator()

        self.area_distr = float(input("Área de Influencia de cada distribuidor (m²): "))
        self.altura = float(input("Altura do Reator (m): "))


    def coletores_gas(self):
        self.nColetores = int(input("Quantidade de coletores por módulo: "))
        self.largura_coletores = float(input("Lagura de cada coletor de gás (m): "))

    def abertura_para_decantador(self):
        self.largura_abertura_decan = float(input("Largura de abertura decantador (m): "))

    def altura_decantador(self):
        self.altura_h1_inclinada = float(input("Altura parede inclinada (m): "))
        self.altura_h2_vertical = float(input("Altura da parede vertical (m): "))

    def trespasse(self):
        return float(input("Trespasse, min = 0.1 m: "))