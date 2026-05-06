# motor_jogo.py

import dados


def atribuir_pontos(liga, nome, pontos):
    """
    Soma os pontos à equipa.
    """
    if nome in liga:
        liga[nome]["pontos"] += pontos
    else:
        print(f"Equipa '{nome}' não encontrada.")


def registar_vitoria_derrota_empate(liga, nome, resultado):
    """
    Atualiza os contadores de vitórias, empates ou derrotas.
    """
    if nome not in liga:
        print(f"Equipa '{nome}' não encontrada.")
        return

    if resultado == "vitoria":
        liga[nome]["vitorias"] += 3

    elif resultado == "empate":
        liga[nome]["empates"] += 1

    elif resultado == "derrota":
        liga[nome]["derrotas"] += 0


def processar_resultado(golos_casa, golos_fora):
    """
    Devolve o resultado do jogo.
    """
    if golos_casa > golos_fora:
        return "casa"

    elif golos_fora > golos_casa:
        return "fora"

    else:
        return "empate"


def registar_jogo(liga, eq_casa, golos_c, eq_fora, golos_f):
    """
    Função principal para atualizar a liga após um jogo.
    """

    resultado = processar_resultado(golos_c, golos_f)

    # Atualizar golos
    liga[eq_casa]["golos_marcados"] += golos_c
    liga[eq_casa]["golos_sofridos"] += golos_f

    liga[eq_fora]["golos_marcados"] += golos_f
    liga[eq_fora]["golos_sofridos"] += golos_c

    # Vitória equipa da casa
    if resultado == "casa":
        atribuir_pontos(liga, eq_casa, 3)

        registar_vitoria_derrota_empate(
            liga, eq_casa, "vitoria"
        )

        registar_vitoria_derrota_empate(
            liga, eq_fora, "derrota"
        )

    # Vitória equipa visitante
    elif resultado == "fora":
        atribuir_pontos(liga, eq_fora, 3)

        registar_vitoria_derrota_empate(
            liga, eq_fora, "vitoria"
        )

        registar_vitoria_derrota_empate(
            liga, eq_casa, "derrota"
        )

    # Empate
    else:
        atribuir_pontos(liga, eq_casa, 1)
        atribuir_pontos(liga, eq_fora, 1)

        registar_vitoria_derrota_empate(
            liga, eq_casa, "empate"
        )

        registar_vitoria_derrota_empate(
            liga, eq_fora, "empate"
        )