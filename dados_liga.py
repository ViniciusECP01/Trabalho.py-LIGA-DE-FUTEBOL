def adicionar_equipa(liga, nome):
    equipa = {
        "nome": nome,
        "pontos": 0,
        "vitorias": 0,
        "empates": 0,
        "derrotas": 0,
        "gm": 0,
        "gs": 0
    }
    liga.append(equipa)
    return liga


def remover_equipa(liga, nome):
    for equipa in liga:
        if equipa["nome"] == nome:
            liga.remove(equipa)
            return True
    return False


def pesquisar_equipa(liga, nome):
    for equipa in liga:
        if equipa["nome"] == nome:
            return equipa
    return None


def atualizar_golos(liga, nome, marcados, sofridos):
    equipa = pesquisar_equipa(liga, nome)
    if equipa:
        equipa["gm"] += marcados
        equipa["gs"] += sofridos
        return True
    return False