def inserir_coordenada_tabuleiro(entrada_convertido_indices, tabuleiro):
    for j in range(9):  # Percorro 9x9
        for i in range(9):
            if j == entrada_convertido_indices[1] and i == entrada_convertido_indices[0]:  # Se coincidir as coordenadas que foram passadas pelo usuário...
                tabuleiro[j][i] = entrada_convertido_indices[2]  # ...com certeza é o valor a ser inserido no tabuleiro.
    return tabuleiro


def deletar_coordenada_tabuleiro(entrada_convertido_indices, tabuleiro, matriz_pistas_convertidas_com_indices):
    for j in range(9):  # Percorro 9x9
        for i in range(9):
            if j == entrada_convertido_indices[1] and i == entrada_convertido_indices[0]:  # Se coincidir as coordenadas que foram passadas pelo usuário...
                if tabuleiro[j][i] == 0:  # Se o valor nessas coordenadas, no tabuleiro, for 0...
                    print("Impossível deletar um espaço vazio!")  # ...não tem como deletar um espaço vazio.
                    return tabuleiro
                else:  # Porém, a coordenada pode ser uma pista...
                    for k in range(len(matriz_pistas_convertidas_com_indices)):  # ...então percorremos a quantidade de pistas que foram passadas.
                        if i == matriz_pistas_convertidas_com_indices[k][0] and j == matriz_pistas_convertidas_com_indices[k][1]:  # Se a coordenada <col> e <linha> coincidir com as coordenadas de qualquer pista...
                            print(f"O valor {matriz_pistas_convertidas_com_indices[k][2]} não pode ser deletado, pois é uma pista!")  # ...não tem como deletar, pois a coordenada é uma pista.
                            return tabuleiro
                    print(f"Valor {tabuleiro[j][i]} deletado com sucesso!")  # Em nenhum dos casos, é possível deletar.
                    tabuleiro[j][i] = 0  # Pra deletar, atribuo o valor a 0.
    return tabuleiro
