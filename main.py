from reator import Reator


if __name__ == '__main__':
 
 
    pop = float(input("População Atendida: "))
    prod = float(input("Esgoto por pessoa (m³/dia): "))
    tdh = float(input("Tempo de detenção hidráulica (h): "))
    reator = Reator(pop, prod, tdh)
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
    print("Carga Aplicada: ", reator.carga_hidraulica_volumetrica())
    print("Velocidade Ascensional: ", reator.velocidade_ascencional())