from reator import Reator

if __name__ == '__main__':
    
    
    
    reator = Reator()
    reator.verificar_tdh()
    print("Volume Total (m³): ", reator.volume_total)
    print("Celulas: ", reator.nCel)
    print("Volume do módulo (m³): ", reator.volume_reator)
    print("Tempo TDH (h): ", reator.ent.tdh)
    print("Carga Hidráulica (m³/m³.d): ", reator.carga_hidraulica_volumetrica_media())
    print("Carga Orgânica (kgDQO/m³.d): ", reator.carga_organica_volumetrica())
    print("Velocidade Superficial (m/h): ", reator.velocidade_superficial_fluxo_media())
    print("Velocidade Superficial Máxima (m/h): ", reator.velocidade_superficial_fluxo_maxima())
    print("Eficiência DQO (%): ", reator.eficienciaDQO)
    print("Eficiência DBO (%): ", reator.eficienciaDBO)
    print("DQO Efluente (mgDQO/L): ", reator.efluenteDQO)
    print("DBO Efluente (mgDBO/L): ", reator.efluenteDBO)
    print("Produção Metano (m³/d): ", reator.prod_metano)
    print("Produção Biogás (m³/d): ", reator.biogas)
    print("Produção de lodo (m³/d): ", reator.volume_lodo)
    print("Volume decantação: ", reator.volume_dec)
    print("================Médidas Reator======================")
    print("Altura do reator (m): ", reator.altura_reator)
    print("Comprimento do reator (m): ", reator.comprimento_reator)
    print("Largura do módulo (m): ", reator.largura_modulo)
    print("Largura dos coletores de gás (m): ", reator.coletores_biogas)
    print("Área Distribuidores (m²): ", reator.area_distr)
    print("Pontos de Distribuição: ", reator.pontos_descarga)
    reator.largura_decantacao()
    print("Lagura compartimento decantação: ", reator.largura_compartimento_util)
    print("a: largura da abertura simples de passagem para o decantador (m): ", reator.abertura_simples_decan)
    print("b: trespasse do defletor de gases, em relação à abertura de passagem para o decantador (m): ", reator.trespasse_do_defletor)
    print("c: largura da abertura dupla de passagem para o decantador (m): ", reator.abertura_simples_decan*2)
    print("alpha: ângulo de inclinação da parede(aba) (m): ", reator.angulo)
    print("h1: altura da parede inclinada do compartimento de decantação (m): ", reator.ent.altura_h1_inclinada)
    print("h2: altura da parede vertical do compartimento de decantacao (m): ", reator.ent.altura_h2_vertical)
    print('Altura digestão (m): ', reator.altura_reator - (reator.ent.altura_h1_inclinada + reator.ent.altura_h2_vertical))
    
    