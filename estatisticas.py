def calcular_total_jogos(liga):
    total = 0
    for equipa in liga:
        jogos = equipa["vitorias"] + equipa["empates"] + equipa["derrotas"]
        total += jogos
    return total // 2


def calcular_media_golos(liga):
    total_golos = 0
    total_jogos = calcular_total_jogos(liga)

    for equipa in liga:
        total_golos += equipa["gm"]

    if total_jogos == 0:
        return 0

    return total_golos / total_jogos


def obter_melhor_ataque(liga):
    if not liga:
        return None

    melhor = liga[0]
    for equipa in liga:
        if equipa["gm"] > melhor["gm"]:
            melhor = equipa

    return melhor


def ordenar_classificacao(liga):
    return sorted(liga, key=lambda e: e["pontos"], reverse=True)