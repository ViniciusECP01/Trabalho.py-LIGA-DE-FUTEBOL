from dados_liga import pesquisar_equipa, atualizar_golos # type: ignore


def atribuir_pontos(liga, nome, pontos):
    equipa = pesquisar_equipa(liga, nome)
    if equipa:
        equipa["pontos"] += pontos
        return True
    return False


def registar_vitoria_derrota_empate(liga, nome, resultado):
    equipa = pesquisar_equipa(liga, nome)
    if equipa:
        if resultado == "vitoria":
            equipa["vitorias"] += 1
        elif resultado == "empate":
            equipa["empates"] += 1
        elif resultado == "derrota":
            equipa["derrotas"] += 1
        return True
    return False


def processar_resultado(golos_casa, golos_fora):
    if golos_casa > golos_fora:
        return "casa"
    elif golos_fora > golos_casa:
        return "fora"
    else:
        return "empate"


def registar_jogo(liga, eq_casa, golos_c, eq_fora, golos_f):
    resultado = processar_resultado(golos_c, golos_f)

    atualizar_golos(liga, eq_casa, golos_c, golos_f)
    atualizar_golos(liga, eq_fora, golos_f, golos_c)

    if resultado == "casa":
        atribuir_pontos(liga, eq_casa, 3)
        registar_vitoria_derrota_empate(liga, eq_casa, "vitoria")
        registar_vitoria_derrota_empate(liga, eq_fora, "derrota")

    elif resultado == "fora":
        atribuir_pontos(liga, eq_fora, 3)
        registar_vitoria_derrota_empate(liga, eq_fora, "vitoria")
        registar_vitoria_derrota_empate(liga, eq_casa, "derrota")

    else:
        atribuir_pontos(liga, eq_casa, 1)
        atribuir_pontos(liga, eq_fora, 1)
        registar_vitoria_derrota_empate(liga, eq_casa, "empate")
        registar_vitoria_derrota_empate(liga, eq_fora, "empate")

    return liga