"""
Esse módulo é usado apenas para o MODO BATCH
Ele existe pois o print no console precisa ser diferente para mostrar as coordenadas originais de A...I e 1...9.
Por isso, foi criada a função abaixo, que converte de volta para as coordenadas originais.

A princípio, as funções usadas são praticamente as mesmas dos outros módulos.
A diferença é o uso da função em outras funções que converte índices de 0...8 para coordenadas de A...I <col> e 1...9
<lin>, que não é bem interpretada pelo programa.
"""


def entrada_indices_para_coord(entrada_lista):
    if entrada_lista[0] == 0:
        entrada_lista[0] = 'A'
    elif entrada_lista[0] == 1:
        entrada_lista[0] = 'B'
    elif entrada_lista[0] == 2:
        entrada_lista[0] = 'C'
    elif entrada_lista[0] == 3:
        entrada_lista[0] = 'D'
    elif entrada_lista[0] == 4:
        entrada_lista[0] = 'E'
    elif entrada_lista[0] == 5:
        entrada_lista[0] = 'F'
    elif entrada_lista[0] == 6:
        entrada_lista[0] = 'G'
    elif entrada_lista[0] == 7:
        entrada_lista[0] = 'H'
    elif entrada_lista[0] == 8:
        entrada_lista[0] = 'I'

    if entrada_lista[1] == 0:
        entrada_lista[1] = '1'
    elif entrada_lista[1] == 1:
        entrada_lista[1] = '2'
    elif entrada_lista[1] == 2:
        entrada_lista[1] = '3'
    elif entrada_lista[1] == 3:
        entrada_lista[1] = '4'
    elif entrada_lista[1] == 4:
        entrada_lista[1] = '5'
    elif entrada_lista[1] == 5:
        entrada_lista[1] = '6'
    elif entrada_lista[1] == 6:
        entrada_lista[1] = '7'
    elif entrada_lista[1] == 7:
        entrada_lista[1] = '8'
    elif entrada_lista[1] == 8:
        entrada_lista[1] = '9'

    return entrada_lista


def percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro):
    minj = None
    maxj = None
    mini = None
    maxi = None
    if quadrante == 1:
        minj = 0
        maxj = 3
        mini = 0
        maxi = 3
    elif quadrante == 2:
        minj = 0
        maxj = 3
        mini = 3
        maxi = 6
    elif quadrante == 3:
        minj = 0
        maxj = 3
        mini = 6
        maxi = 9
    elif quadrante == 4:
        minj = 3
        maxj = 6
        mini = 0
        maxi = 3
    elif quadrante == 5:
        minj = 3
        maxj = 6
        mini = 3
        maxi = 6
    elif quadrante == 6:
        minj = 3
        maxj = 6
        mini = 6
        maxi = 9
    elif quadrante == 7:
        minj = 6
        maxj = 9
        mini = 0
        maxi = 3
    elif quadrante == 8:
        minj = 6
        maxj = 9
        mini = 3
        maxi = 6
    elif quadrante == 9:
        minj = 6
        maxj = 9
        mini = 6
        maxi = 9
    for j in range(minj, maxj):
        for i in range(mini, maxi):
            if entrada_convertido_indices[2] == tabuleiro[j][i]:
                printar_coordenadas = entrada_convertido_indices
                printar_coordenadas = entrada_indices_para_coord(printar_coordenadas)  # Uso da função para converter os índices em coordenadas originais
                print(f"A jogada ({printar_coordenadas[0]},{printar_coordenadas[1]}) = {printar_coordenadas[2]} eh invalida!")
                return True
    return False


def repeticoes_quadrante_jogada(entrada_convertido_indices, tabuleiro):
    if 0 <= entrada_convertido_indices[0] <= 2 and 0 <= entrada_convertido_indices[1] <= 2:
        quadrante = 1
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 3 <= entrada_convertido_indices[0] <= 5 and 0 <= entrada_convertido_indices[1] <= 2:
        quadrante = 2
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 6 <= entrada_convertido_indices[0] <= 8 and 0 <= entrada_convertido_indices[1] <= 2:
        quadrante = 3
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 0 <= entrada_convertido_indices[0] <= 2 and 3 <= entrada_convertido_indices[1] <= 5:
        quadrante = 4
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 3 <= entrada_convertido_indices[0] <= 5 and 3 <= entrada_convertido_indices[1] <= 5:
        quadrante = 5
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 6 <= entrada_convertido_indices[0] <= 8 and 3 <= entrada_convertido_indices[1] <= 5:
        quadrante = 6
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 0 <= entrada_convertido_indices[0] <= 2 and 6 <= entrada_convertido_indices[1] <= 8:
        quadrante = 7
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 3 <= entrada_convertido_indices[0] <= 5 and 6 <= entrada_convertido_indices[1] <= 8:
        quadrante = 8
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)
    elif 6 <= entrada_convertido_indices[0] <= 8 and 6 <= entrada_convertido_indices[1] <= 8:
        quadrante = 9
        return percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro)


###########################################################
###########################################################


def repeticoes_linha_coluna_jogada(entrada_convertido_indices, tabuleiro):
    for j in range(9):  # Verifica valores horizontais
        if entrada_convertido_indices[1] == j:
            for valor in tabuleiro[j]:
                if valor == entrada_convertido_indices[2]:
                    printar_coordenadas = entrada_convertido_indices
                    printar_coordenadas = entrada_indices_para_coord(printar_coordenadas)
                    print(f"A jogada ({printar_coordenadas[0]},{printar_coordenadas[1]}) = {printar_coordenadas[2]} eh invalida!")
                    return True

    tabuleiro_transposto = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for i in range(9):  # Transpostando a matriz pra verificar repetições em colunas
        for j in range(9):
            tabuleiro_transposto[i][j] = tabuleiro[j][i]

    for j in range(9):  # Verifico repetições em colunas
        if entrada_convertido_indices[0] == j:
            for valor in tabuleiro_transposto[j]:
                if valor == entrada_convertido_indices[2]:
                    printar_coordenadas = entrada_convertido_indices
                    printar_coordenadas = entrada_indices_para_coord(printar_coordenadas)
                    print(f"A jogada ({printar_coordenadas[0]},{printar_coordenadas[1]}) = {printar_coordenadas[2]} eh invalida!")
                    return True
    return False
