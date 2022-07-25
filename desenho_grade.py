def print_desenho_grade(tabuleiro):
    letras_grade = "    A   B   C    D   E   F    G   H   I    "
    linha_fina_grade = " ++---+---+---++---+---+---++---+---+---++ "
    linha_grossa_grade = " ++===+===+===++===+===+===++===+===+===++ "
    matriz_linhas = [["1||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||1"],
                     ["2||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||2"],
                     ["3||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||3"],
                     ["4||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||4"],
                     ["5||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||5"],
                     ["6||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||6"],
                     ["7||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||7"],
                     ["8||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||8"],
                     ["9||", "a", "|", "b", "|", "c", "||", "d", "|", "e" ,"|", "f", "||", "g", "|", "h" ,"|", "i", "||9"]]

    print(letras_grade)  # Desenho do tabuleiro começa aqui
    print(linha_fina_grade)

    conti_tab = 0  # Variáveis de controle
    contj_tab = 0
    conti_grade = 1
    contj_grade = 0
    coluna = 0

    for j in matriz_linhas:  # Percorro a matriz onde só tem os desenhos que ficarão os valores
        for i in j:
            if i in "abcdefghi" and conti_tab < 9:  # Percorre linha e coluna da grade nova do tabuleiro e verifica apenas letras na iteração
                if tabuleiro[contj_tab][conti_tab] == 0:  # Se nas coordenadas do desenho onde tem letra tiver um zero no tabuleiro matriz original...
                    matriz_linhas[contj_grade][conti_grade] = " "  # ...substitui a letra por um espaço vazio
                else:  # Se não...
                    matriz_linhas[contj_grade][conti_grade] = tabuleiro[contj_tab][conti_tab]  # ...substitui a letra pelo valor que está no tabuleiro matriz original
                conti_tab = conti_tab + 1  # Avanço 1 no tabuleiro original pra direita
                conti_grade = conti_grade + 2  # Avanço de 2 em 2 no desenho da grade pra direita (pois tem caracteres tipo | ou ||)
        contj_tab = contj_tab + 1  # Avanço 1 no tabuleiro original pra baixo
        contj_grade = contj_grade + 1  # Avanço 1 na matriz do desenho da grade
        conti_grade = 1  # Reseto o valor do contador horizontal de volta pro início pro desenho da grade, a fim de percorrer a próxima coluna.
        conti_tab = 0  # Reseto o valor do contador horizontal de volta pro início pro tabuleiro original, a fim de percorrer a próxima coluna.
        print(" ".join(j))  # CRUCIAL: Cada lista iterada eu junto todos os valores para uma string só. Caso contrário, imprimiria lista por lista.
        coluna = coluna + 1  # Incremento 1 em coluna...
        if coluna == 3 or coluna == 6:  # E se chegar na coluna 3 ou 6, coloca a linha mais grossa que ajuda a separar os quadrantes
            print(linha_grossa_grade)
        else:  # Se não, simplesmente printa a linha mais fina.
            print(linha_fina_grade)

    print(letras_grade)  # Parte de baixo do desenho da grade.

# UNUSED ###############################################################################################################
# def substituicao_letras(tabuleiro, linha_vazia, cont_tabuleiro_j, cont_grade):
#     cont_tabuleiro_i = 0
#     for elemento in linha_vazia:
#         if elemento in "abcdefghi":
#             if tabuleiro[cont_tabuleiro_j][cont_tabuleiro_i] == 0:
#                 linha_vazia[cont_grade] = " "
#             else:
#                 linha_vazia[cont_grade] = tabuleiro[cont_tabuleiro_j][cont_tabuleiro_i]
#             cont_tabuleiro_i =+ 1
#             cont_grade =+ 2
#     linha_vazia = " ".join(linha_vazia)
#     return linha_vazia
########################################################################################################################