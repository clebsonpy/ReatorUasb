from reator import Reator


if __name__ == '__main__':
 
 
    pop = float(input("População Atendida: "))
    prod = float(input("Esgoto por pessoa (m³/dia): "))
    temperatura = float(input("Temperatura (ºC): "))
    reator = Reator(pop, prod, temperatura)
    print("Volume Total: ", reator.volume_total)
    print("Celulas: ", reator.nCel)
    print("Volume de cada Reator: ", reator.volume_reator)
    print("Altura: ", reator.altura_reator)
    print("Comprimento: ", reator.comprimento_reator)
    print("Largura: ", reator.largura_reator)
    reator.verificar_tdh()
    print("Volume Total: ", reator.volume_total)
    print("Celulas: ", reator.nCel)
    print("Volume de cada Reator: ", reator.volume_reator)
    print("Altura: ", reator.altura_reator)
    print("Comprimento: ", reator.comprimento_reator)
    print("Largura: ", reator.largura_reator)
    print("Tempo TDH: ", reator.tdh)
    print("Carga Aplicada: ", reator.carga_hidraulica_volumetrica_media())
    print("Carga Orgânica: ", reator.carga_organica_volumetrica())
    print("Velocidade Ascensional: ", reator.velocidade_superficial_fluxo_media())
    print("Velocidade Ascensional Máxima: ", reator.velocidade_superficial_fluxo_maxima())
    print("Pontos: ", reator.pontos_descarga)
    print("Eficiência DQO: ", reator.eficiencia_DQO())
    print("Eficiência DBO: ", reator.eficiencia_DBO())