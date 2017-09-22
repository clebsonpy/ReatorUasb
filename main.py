from reator import Reator


if __name__ == '__main__':
 
 
    pop = float(input("População Atendida: "))
    prod = float(input("Esgoto por pessoa (m³/dia): "))
    tdh = float(input("Tempo de detenção hidráulica (h): "))
    reator = Reator(pop, prod, tdh)
    print("Volume Total: ", reator.volume())
    print("Celulas: ", reator.nCelula())
    print("Volume de cada Reator: ", reator.volume_cada_reator())
    reator.verificar_tdh()
    print("Tempo TDH: ", reator.tdh)
    print("Altura: ", reator.altura)
    print("Comprimento: ", reator.comprimento)
    print("Largura: ", reator.largura)
    print("Carga Aplicada: ", reator.carga_hidraulica_volumetrica())