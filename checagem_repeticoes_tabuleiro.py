def percorrer_quadrantes(quadrante, entrada_convertido_indices, tabuleiro):
    minj = None  # Variáveis de controle para verificar quadrantes
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
                print(F"O quadrante {quadrante} já tem um valor '{entrada_convertido_indices[2]}' inserido!")
                return True
    return False


def repeticoes_quadrantes_input(entrada_convertido_indices, tabuleiro):  # Defino os quadrantes e retorno se houve repetições ou não neles a partir da função de cima /\
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


#########################################


def repeticoes_linhas_colunas_input(entrada_convertida_indices, tabuleiro):
    for j in range(9):  # Verifica valores horizontais
        if entrada_convertida_indices[1] == j:  # Se coincidir com j...
            for i in tabuleiro[j]:  # ...percorre cada valor na linha j do tabuleiro original...
                if i == entrada_convertida_indices[2]: # ...e se coincidir com valor que o usuário inputou...
                    print(f"A linha passada já possui o valor {entrada_convertida_indices[2]}!")  # ...significa que a linha já tem um valor igual.
                    return True

    # Pra verificar colunas, como o python percorre primeiro de cima pra baixo, depois de esquerda pra direita em uma
    # matriz, não é possível fazer o inverso, a não ser fazendo a transposta da matriz do tabuleiro original que estamos
    # trabalhando.

    # Pra isso, crio um tabuleiro vazio que receberá a transposta do tabuleiro
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

    for i in range(9):  # Transpostando a matriz
        for j in range(9):
            tabuleiro_transposto[i][j] = tabuleiro[j][i]

    for j in range(9):  # Agora sim, verifico repetições em colunas usando o mesmo método que fiz com linhas.
        if entrada_convertida_indices[0] == j:
            for valor in tabuleiro_transposto[j]:
                if valor == entrada_convertida_indices[2]:
                    print(f"A coluna passada já possui o valor {entrada_convertida_indices[2]}!")
                    return True
    return False
