
def repeticoes_quadrantes_pista(quad, matriz_pistas):
    for percorrer in matriz_pistas:  # Percorro todos os quadrantes
        i, j, valor = percorrer  # Desempacoto as listas iteradas
        if i in 'ABC' and j in '123':  # Primeiro quadrante 3x3 e assim sucessivamente...
            quad.append(valor)
    if len(quad) != len(set(quad)):  # Uso conjunto para verificar se valores estão repetidos. Conjunto elimina valores repetidos, e ai comparo com o original
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []  # Hard reset no quadrante pra verificar o próximo

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'ABC' and j in '456':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'ABC' and j in '789':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'DEF' and j in '123':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'DEF' and j in '456':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'DEF' and j in '789':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'GHI' and j in '123':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'GHI' and j in '456':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)
    quad = []

    for percorrer in matriz_pistas:
        i, j, valor = percorrer
        if i in 'GHI' and j in '789':
            quad.append(valor)
    if len(quad) != len(set(quad)):
        print("Erro: valores fornecidos da pista tem repetições em quadrantes! Encerrando o programa...")
        exit(1)


def repeticoes_linhas_colunas_pista(horizontal_vazio, vertical_vazio, matriz_pistas):
    for percorrer in matriz_pistas:
        i, j, valor = percorrer  # Desempacoto listas da matriz que contém listas de pistas
        if i == 'A':
            horizontal_vazio[0].append(valor)  # Adiciono em uma nova lista temporária todos as pistas na coordenada A,B,C...
        elif i == 'B':
            horizontal_vazio[1].append(valor)
        elif i == 'C':
            horizontal_vazio[2].append(valor)
        elif i == 'D':
            horizontal_vazio[3].append(valor)
        elif i == 'E':
            horizontal_vazio[4].append(valor)
        elif i == 'F':
            horizontal_vazio[5].append(valor)
        elif i == 'G':
            horizontal_vazio[6].append(valor)
        elif i == 'H':
            horizontal_vazio[7].append(valor)
        elif i == 'I':
            horizontal_vazio[8].append(valor)

    for i in range(9):
        if len(horizontal_vazio[i]) != len(set(horizontal_vazio[i])):  # Se algumas dessas colunas tem valores duplicados, encerra...
            print("Erro: valores fornecidos da pista tem repetições em LINHAS! Encerrando o programa...")
            exit(1)

    for percorrer in matriz_pistas:  # Mesma coisa faço agora para as linhas
        i, j, valor = percorrer
        if j == '1':
            vertical_vazio[0].append(valor)
        elif j == '2':
            vertical_vazio[1].append(valor)
        elif j == '3':
            vertical_vazio[2].append(valor)
        elif j == '4':
            vertical_vazio[3].append(valor)
        elif j == '5':
            vertical_vazio[4].append(valor)
        elif j == '6':
            vertical_vazio[5].append(valor)
        elif j == '7':
            vertical_vazio[6].append(valor)
        elif j == '8':
            vertical_vazio[7].append(valor)
        elif j == '9':
            vertical_vazio[8].append(valor)

    for i in range(9):
        if len(vertical_vazio[i]) != len(set(vertical_vazio[i])):
            print("Erro: valores fornecidos da pista tem repetições em COLUNAS! Encerrando o programa...")
            exit(1)

