def pista_coord_para_indices(matriz_pistas):
    for percorrer in matriz_pistas:
        if percorrer[0] == 'A':
            percorrer[0] = 0
        elif percorrer[0] == 'B':
            percorrer[0] = 1
        elif percorrer[0] == 'C':
            percorrer[0] = 2
        elif percorrer[0] == 'D':
            percorrer[0] = 3
        elif percorrer[0] == 'E':
            percorrer[0] = 4
        elif percorrer[0] == 'F':
            percorrer[0] = 5
        elif percorrer[0] == 'G':
            percorrer[0] = 6
        elif percorrer[0] == 'H':
            percorrer[0] = 7
        elif percorrer[0] == 'I':
            percorrer[0] = 8

        if percorrer[1] == '1':
            percorrer[1] = 0
        elif percorrer[1] == '2':
            percorrer[1] = 1
        elif percorrer[1] == '3':
            percorrer[1] = 2
        elif percorrer[1] == '4':
            percorrer[1] = 3
        elif percorrer[1] == '5':
            percorrer[1] = 4
        elif percorrer[1] == '6':
            percorrer[1] = 5
        elif percorrer[1] == '7':
            percorrer[1] = 6
        elif percorrer[1] == '8':
            percorrer[1] = 7
        elif percorrer[1] == '9':
            percorrer[1] = 8

    return matriz_pistas


def entrada_coord_para_indices(entrada_lista):
    if entrada_lista[0] == 'A' or entrada_lista[0] == 'a':
        entrada_lista[0] = 0
    elif entrada_lista[0] == 'B' or entrada_lista[0] == 'b':
        entrada_lista[0] = 1
    elif entrada_lista[0] == 'C' or entrada_lista[0] == 'c':
        entrada_lista[0] = 2
    elif entrada_lista[0] == 'D' or entrada_lista[0] == 'd':
        entrada_lista[0] = 3
    elif entrada_lista[0] == 'E' or entrada_lista[0] == 'e':
        entrada_lista[0] = 4
    elif entrada_lista[0] == 'F' or entrada_lista[0] == 'f':
        entrada_lista[0] = 5
    elif entrada_lista[0] == 'G' or entrada_lista[0] == 'g':
        entrada_lista[0] = 6
    elif entrada_lista[0] == 'H' or entrada_lista[0] == 'h':
        entrada_lista[0] = 7
    elif entrada_lista[0] == 'I' or entrada_lista[0] == 'i':
        entrada_lista[0] = 8

    if entrada_lista[1] == '1':
        entrada_lista[1] = 0
    elif entrada_lista[1] == '2':
        entrada_lista[1] = 1
    elif entrada_lista[1] == '3':
        entrada_lista[1] = 2
    elif entrada_lista[1] == '4':
        entrada_lista[1] = 3
    elif entrada_lista[1] == '5':
        entrada_lista[1] = 4
    elif entrada_lista[1] == '6':
        entrada_lista[1] = 5
    elif entrada_lista[1] == '7':
        entrada_lista[1] = 6
    elif entrada_lista[1] == '8':
        entrada_lista[1] = 7
    elif entrada_lista[1] == '9':
        entrada_lista[1] = 8

    return entrada_lista

