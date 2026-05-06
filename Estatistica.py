#Estatistia 
import dados
import motor_do_jogo

def calcular_total_jogos(liga):
    # Soma todos os jogos das equipas e divide por 2 (cada jogo envolve 2 equipas)
    total = sum(equipa["jogos"] for equipa in liga)
    return total // 2


def calcular_media_golos(liga):
    # Média de golos marcados no campeonato
    total_golos = sum(equipa["golos_marcados"] for equipa in liga)
    total_jogos = calcular_total_jogos(liga)
    
    if total_jogos == 0:
        return 0
    
    return total_golos / total_jogos


def obter_melhor_ataque(liga):
    # Equipa com mais golos marcados
    return max(liga, key=lambda equipa: equipa["golos_marcados"])


def ordenar_classificacao(liga):
    # Ordena por pontos (do maior para o menor)
    return sorted(liga, key=lambda equipa: equipa["pontos"], reverse=True)
