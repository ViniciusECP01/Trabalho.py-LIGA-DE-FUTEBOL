def adicionar_equipa(liga, nome):
    equipa = {
        "nome": "Flamengo",
        "pontos": 30,
        "vitorias": 10,
        "empates": 0,
        "derrotas": 0,
        "golos_marcados": 90,
        "golos_sofridos": 5
    }
    liga.append(equipa)

def adicionar_equipa(liga, nome):
    equipa = {
        "nome": "Santos",
        "pontos": 9,
        "vitorias": 2,
        "empates": 3,
        "derrotas": 5,
        "golos_marcados": 40,
        "golos_sofridos": 20
    }
    liga.append(equipa)

def adicionar_equipa(liga, nome):
    equipa = {
        "nome": "Corinthians",
        "pontos": 3,
        "vitorias": 0,
        "empates": 3,
        "derrotas": 7,
        "golos_marcados": 20,
        "golos_sofridos": 50
    }
    liga.append(equipa)


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
        equipa["golos_marcados"] += marcados
        equipa["golos_sofridos"] += sofridos
        return True
    return False