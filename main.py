from reator import Reator

if __name__ == '__main__':
    
    
    
    reator = Reator()
    reator.verificar_tdh()
    print("Volume Total (m³): ", reator.volume_total)
    print("Celulas: ", reator.nCel)
    print("Volume do módulo (m³): ", reator.volume_reator)
    print("Altura do reator (m): ", reator.altura_reator)
    print("Comprimento do reator (m): ", reator.comprimento_reator)
    print("Largura do módulo (m): ", reator.largura_modulo)
    print("Tempo TDH (h): ", reator.ent.tdh)
    print("Carga Hidráulica (m³/m³.d): ", reator.carga_hidraulica_volumetrica_media())
    print("Carga Orgânica (kgDQO/m³.d): ", reator.carga_organica_volumetrica())
    print("Velocidade Superficial (m/h): ", reator.velocidade_superficial_fluxo_media())
    print("Velocidade Superficial Máxima (m/h): ", reator.velocidade_superficial_fluxo_maxima())
    print("Área Distribuidores (m²): ", reator.area_distr)
    print("Pontos de Distribuição: ", reator.pontos_descarga)
    print("Eficiência DQO (%): ", reator.eficienciaDQO)
    print("Eficiência DBO (%): ", reator.eficienciaDBO)
    print("DQO Efluente (mgDQO/L): ", reator.efluenteDQO)
    print("DBO Efluente (mgDBO/L): ", reator.efluenteDBO)
    print("Produção Metano (m³/d): ", reator.prod_metano)
    print("Produção Biogás (m³/d): ", reator.prod_biogas())
    print("Largura dos coletores de gás (m): ", reator.coletores_gas())

