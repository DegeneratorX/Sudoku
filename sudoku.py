########################################################################################################################
# SUDOKU
# Autor do projeto: Victor Medeiros Martins
########################################################################################################################

import numbers  # unused
import sys  # usarei pra receber qualquer arquivo, por ordem. Utilizável apenas no linux ao compilar pelo terminal.
import re  # re.split pra retirar caracteres indesejados e criar novos valores para uma lista.
import inserir_deletar  # Módulo que insere valores no Tabuleiro Interativo
import checagem_repeticoes_pista  # Módulo que checa possíveis repetições dos valores da pista fornecidos pelo usuário nos quadrantes, linhas e colunas
import checagem_repeticoes_tabuleiro  # Módulo que checa possíveis repetições do valor inserido pelo usuário nos quadrantes, linhas e colunas
import conversao_coord_para_indice  # Substitui todas as coordenadas passadas (A a I, 1 a 9) por índices de 0 a 8, para que se possa trabalhar melhor. Tanto Pistas quando Entrada (do usuário).
import time  # Usando o time.
import desenho_grade  # Módulo que desenha a grade do tabuleiro do modo interativo.
import batch  # Módulo excuslivo do MODO BATCH que trabalha especificamente com o segundo arquivo de jogadas.



print("#"*40)
print("#"*16, "SUDOKU", "#"*16)  # Interface inicial de apresentação
print("#"*40)


while True:

    print()  # Escolher o modo de jogo
    modo_jogo_str = input("Selecione o tipo de jogo que você quer executar. Digite 1 para Modo Interativo, 2 para Modo Batch: ")

    try:  # Trata exceções de valores esquisitos, como strings, floats...
        modo_jogo = int(modo_jogo_str)
        if modo_jogo > 2 or modo_jogo < 1:  # Deve receber apenas 1 e 2.
            print("Erro: você digitou números fora do pedido!")
        else:
            break

    except ValueError:
        print("Erro: Você não digitou números válidos.")
        continue

modo_jogo = int(modo_jogo_str)  # Tudo certo, converto para inteiro. Assim posso escolher entre modo de jogo 1 (Interativo) ou 2 (Batch)

horizontal = "ABCDEFGHI"  # Iterável com as coordenadas hor
vertical = "123456789"  # Iterável com as coordenadas vert

########################################################################################################################
# MODO ITERATIVO #
# - Lê 1 arquivo de pistas fornecido pelo usuário
# - O jogador irá interagir com o tabuleiro até completar
########################################################################################################################

if modo_jogo == 1:  # Modo Iterativo
    # f = sys.argv[1]  # indice 0 = sudoku.py. indice 1 = arq_01_cfg.txt ... etc.
    # Recebe qualquer argumento que for compilado no terminal junto com o arquivo sudoku.py
    # Os índices acessam os respectivos argumentos em ordem aos quais foram passados.

    with open('arq_01_cfg.txt', 'r') as file:  # Abro o arquivo cfg
        dados_arquivo = file.read()  # passo os dados lidos para uma variável
        file.seek(0, 0)  # Ao ler, volto o cursor pra estaca 0

        if file.read() == "":  # Leio o arquivo novamente pra checar se ele está vazio. Se sim, sai do programa.
            print(f"Erro: Configuracao de dicas invalida - Arquivo vazio.")
            exit(1)
        file.seek(0, 0)  # Volto o cursor pro 0.
        linhas = file.read().split('\n')  # Separo cada \n do arquivo em novas listas! (Por enquanto listas com apenas 1 valor)
        matriz_pistas = []  # Matriz vazia que receberá cada lista nova criada
        print()

        for linha in linhas:  # Percorrendo as listas.
            linha_dividida = re.split(',|:', linha)  # Separo o valor de cada lista em novos valores, retirando caracteres. Ex: [C,2:8] => [C, 2, 8]
            numero = False  # VARIÁVEIS DE CONTROLE
            letra = True
            matriz_pistas.append(linha_dividida)  # Adiciono a uma lista vazia para criar uma matriz com os valores.
            for coord in linha_dividida:  # Percorro cada valor de dentro dessa lista nova de 3 valores
                #print(coord)
                if (coord not in horizontal and coord not in vertical) or len(linha_dividida) != 3:  # Se as coordenadas do arquivo não estiverem de acordo com o que foi pedido pelo trabalho, sai do programa.
                    print("Erro: Configuracao de dicas invalida - Arquivo com valores inválidos!")
                    exit(1)
                if not coord.isdigit() and letra:  # Verifica se o primeiro índice é uma letra e prepara para veficar se é um número no próximo valor lido
                    numero = True
                    letra = False
                    pass
                elif coord.isdigit() and numero:  # Verifica se é um número, no caso a coluna
                    pass
                else:
                    print("Erro: Configuracao de dicas invalida - arquivo com coordenadas inválidas ou trocadas!")  # Se algo tiver trocado, mesmo que dentro do escopo de A a I ou 1 a 9, cai aqui.
                    exit(1)

        if len(matriz_pistas) > 80 or len(matriz_pistas) < 1:  # Número de pistas deve respeitar 1 até 80
            print("Erro: Configuracao de dicas invalida - arquivo com mais de 80 pistas! (Ou nenhuma)")
            exit(1)

        ## ATENÇÃO: CÓDIGO EM DESUSO OPCIONAL : NO CASO DE RECUSAR PISTA COM COORDENADAS REPETIDAS ##
        # coord_repetidas = []
        # for item in matriz_pistas:
        #     hor, vert, valor = item
        #     concatenacao = hor+vert
        #     coord_repetidas.append(concatenacao)
        #
        # if len(coord_repetidas) != len(set(coord_repetidas)):
        #     print("Erro: pista fornecendo valores diferentes pra uma mesma coordenada! Encerrando...")
        #     exit(1)

        quad = []  # Crio um quadrante vazio temporário
        horizontal_vazio = [[],[],[],[],[],[],[],[],[]]  # Crio linhas vazias temporárias
        vertical_vazio = [[],[],[],[],[],[],[],[],[]]  # Crio colunas vazias temporárias

        checagem_repeticoes_pista.repeticoes_quadrantes_pista(quad, matriz_pistas)  # Verifica se há repetições de valores em quadrantes passados através do arquivo pista
        checagem_repeticoes_pista.repeticoes_linhas_colunas_pista(horizontal_vazio, vertical_vazio, matriz_pistas)  # Verifica se há repetições de valores em linhas e colunas através do arquivo pista

        matriz_pistas_convertidas_com_indices = conversao_coord_para_indice.pista_coord_para_indices(matriz_pistas)  # Substitui, das pistas, A...I e 1...9 por índices de 0 a 8 para o interpretador ler e trabalhar com listas e matriz 9x9.

        # CRIAÇÃO DO TABULEIRO ZERADO #
        tabuleiro = [
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

        for linha in matriz_pistas_convertidas_com_indices:  # Após validar a pista, começo a colocar os valores da pista fornecida na matriz vazia que corresponde ao tabuleiro.
            for i in range(9):
                for j in range(9):
                    if linha[0] == i and linha[1] == j:
                        tabuleiro[j][i] = linha[2]

        # OPCIONAL: CÓDIGO PRA VERIFICAR A MATRIZ ORIGINAL #
        # for i in tabuleiro:
        #     print(i)

    print("Arquivo com pistas válido! Vamos começar a jogar...")
    print("\n")
    time.sleep(1)

    # Interação do usuário começará aqui \/

    while True:

        desenho_grade.print_desenho_grade(tabuleiro)  # Conversão do tabuleiro (matriz pura) em desenho + print
        print()
        repetir_while = False  # VARIÁVEL DE CONTROLE
        deletar_coordenada = False  # VARIÁVEL DE CONTROLE

        print("Informe a linha de A a I, coluna de 1 a 9 e o valor, no formato COLUNA,LINHA:VALOR")
        print("Para deletar uma jogada, digite D como parâmetro inicial, depois coloque a coluna e linha. Exemplo: DA,3 deletará a coordenada [D,3]")
        entrada_bruta = input("COORDENADAS: ").replace(" ", "")  # Remoção e tolerância dos espaços

        if len(entrada_bruta) < 4:  # Se o tamanho da entrada for menor que 4, pede pro usuário digitar novamente.
            print("Parâmetros inválidos!")
            print()
            continue

        if not entrada_bruta[1] == ',' or not entrada_bruta[3] == ':':  # Verifica se obedece padrões de vírgula e dois pontos em certas posições da string.
            if (entrada_bruta[0] == 'D' or entrada_bruta[0] == 'd') and entrada_bruta[2] == ',':  # Se não, verifica se ao menos tem um D no começo (talvez o usuário queira deletar valores)
                deletar_coordenada = True  # VARIÁVEL DE CONTROLE

            if deletar_coordenada == False:  # Se detectou que o usuário não tem intenção de deletar valores, então possivelmente é inválido. Pede pro usuário digitar novamente.
                print("Parâmetros inválidos!")
                print()
                continue

        entrada_lista = re.split(",|:", entrada_bruta)  # Conversão direta da entrada em lista com 3 valores [col, lin, num], retirando caracteres especiais.

        if deletar_coordenada == False:  # Se for falso, verificar se os índices 0, 1 e 2 da nova lista estão dentro dos padrões
            if entrada_lista[0] not in horizontal+"abcdefghi" or entrada_lista[1] not in vertical:
                print("Coordenadas inválidas! As coordenadas devem ser de A a I e 1 a 9.")  # Checagem para saber se as coordenadas inseridas pelo usuário foram de A a I ou 1 a 9.
                print()
                continue

            if entrada_lista[2] not in vertical:
                print("Valor inválido! O valor passado deve ser de 1 a 9.")  # Checagem para saber se o valor atribuido a essa coordenada acima é de 1 a 9
                print()
                continue

        if deletar_coordenada:  # Se a intenção era deletar alguma coordenada...
            entrada_lista[0].capitalize()  # uppercase apenas na primeira letra, o D, para também aceitar d pequeno.
            entrada_lista[0] = entrada_lista[0][1:]  # Divido a string e removo o D apenas pra trabalhar com as coordenadas
            entrada_convertido_indices = conversao_coord_para_indice.entrada_coord_para_indices(entrada_lista)  # Converto os índices A...I e 1...9 para 0...8 para o interpretador trabalhar melhor.
            tabuleiro = inserir_deletar.deletar_coordenada_tabuleiro(entrada_convertido_indices, tabuleiro, matriz_pistas_convertidas_com_indices)  # Deleto do tabuleiro o valor atendendo as condições do trabalho.
            continue  # Deletado, pede pro usuário reinserir novos valores.

        entrada_convertido_indices = conversao_coord_para_indice.entrada_coord_para_indices(entrada_lista)  # Converto os índices A...I e 1...9 para 0...8 para o interpretador trabalhar melhor. Dessa vez é com a entrada definitiva (sem intenção de deletar)

        for i in matriz_pistas_convertidas_com_indices:
            if entrada_convertido_indices[:2] == i[:2]:  # checagem pra saber se a coordenada passada já tem uma pista inserida no tabuleiro.
                print("Jogada inválida: A coordenada já está preenchida com uma pista!")
                print()
                repetir_while = True  # VARIÁVEL DE CONTROLE
                break
        if repetir_while:
            continue

        if checagem_repeticoes_tabuleiro.repeticoes_quadrantes_input(entrada_convertido_indices, tabuleiro):  # Checagem pra ver se o quadrante informado no input já tem um valor igual passado pelo usuário.
            continue  # Se sim, a jogada é inválida, e pede pro usuário reinserir um novo valor.

        if checagem_repeticoes_tabuleiro.repeticoes_linhas_colunas_input(entrada_convertido_indices, tabuleiro):  # Checagem pra ver se a linha/coluna informada no input possui valores iguais ao que foi passado pelo usuário.
            continue  # Se sim, a jogada é inválida, e pede pro usuário reinserir um novo valor.

        tabuleiro = inserir_deletar.inserir_coordenada_tabuleiro(entrada_convertido_indices, tabuleiro)  # Se tudo deu certo, insere no tabuleiro o valor.

        for i in tabuleiro:
            if 0 not in i:  # Se não tiver zeros na matriz, é pq foi preenchida.
                print("A grade foi preenchida com sucesso!")
                time.sleep(1)
                exit(1)

########################################################################################################################
# MODO BATCH #
# - Lê 1 arquivo de pistas fornecido pelo usuário e 1 arquivo com jogadas prontas
# - Não há uma interação do usuário com o tabuleiro. O programa apenas irá verificar se as jogadas do segundo arquivo são válidas.
########################################################################################################################

else:

    ######################################################################
    # SEGUE O MESMO PRINCÍPIO DO OUTRO MODO PARA LER O ARQUIVO DE PISTAS #
    ######################################################################

    with open('arq_02_cfg.txt', 'r') as file:
        dados_arquivo = file.read()
        file.seek(0, 0)

        if file.read() == "":
            print(f"Erro: Configuracao de dicas invalida - Arquivo vazio.")
            exit(1)
        file.seek(0, 0)
        linhas = file.read().split('\n')
        matriz_pistas = []
        print()

        for linha in linhas:
            linha_dividida = re.split(',|:', linha)
            numero = False
            letra = True
            matriz_pistas.append(linha_dividida)
            for coord in linha_dividida:
                if (coord not in horizontal and coord not in vertical) or len(linha_dividida) != 3:
                    print("Erro: Configuracao de dicas invalida - arquivo com valores inválidos!")
                    exit(1)
                if not coord.isdigit() and letra:
                    numero = True
                    letra = False
                    pass
                elif coord.isdigit() and numero:
                    pass
                else:
                    print("Erro: Configuracao de dicas invalida - arquivo com coordenadas inválidas ou trocadas!")
                    exit(1)

        if len(matriz_pistas) > 80 or len(matriz_pistas) < 1:
            print("Erro: Configuracao de dicas invalida - arquivo com mais de 80 pistas! (Ou nenhuma)")
            exit(1)

        # ATENÇÃO: CÓDIGO EM DESUSO OPCIONAL : NO CASO DE RECUSAR PISTA COM COORDENADAS REPETIDAS #
        # coord_repetidas = []
        # for item in matriz_pistas:
        #     hor, vert, valor = item
        #     concatenacao = hor+vert
        #     coord_repetidas.append(concatenacao)
        #
        # if len(coord_repetidas) != len(set(coord_repetidas)):
        #     print("Erro: pista fornecendo valores diferentes pra uma mesma coordenada! Encerrando...")
        #     exit(1)

        quad = []
        horizontal_vazio = [[],[],[],[],[],[],[],[],[]]
        vertical_vazio = [[],[],[],[],[],[],[],[],[]]
        checagem_repeticoes_pista.repeticoes_quadrantes_pista(quad, matriz_pistas)
        checagem_repeticoes_pista.repeticoes_linhas_colunas_pista(horizontal_vazio, vertical_vazio, matriz_pistas)

        matriz_pistas_convertidas_com_indices = conversao_coord_para_indice.pista_coord_para_indices(matriz_pistas)

        tabuleiro = [
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

        for linha in matriz_pistas_convertidas_com_indices:
            for i in range(9):
                for j in range(9):
                    if linha[0] == i and linha[1] == j:
                        tabuleiro[j][i] = linha[2]

        # OPCIONAL: CÓDIGO PRA VERIFICAR A MATRIZ ORIGINAL #
        # for i in tabuleiro:
        #     print(i)

    print("Arquivo com pistas válido! Verificando arquivo de lista de jogadas...")
    print("\n")
    time.sleep(1)

    ################################################################################################################
    #  AGORA A DIFERENÇA ESTÁ AQUI. IREI LER O SEGUNDO ARQUIVO E TAMBÉM LER LINHA POR LINHA PARECIDO COM AS PISTAS #
    ################################################################################################################

    with open('arq_01_jog.txt', 'r') as file:  # Abro o arquivo de jogadas
        dados_arquivo_jog = file.read()  # Faço a mesma coisa como se fosse um arquivo pista...
        file.seek(0, 0)

        if file.read() == "":
            print(f"Erro: Configuracao de jogadas invalida - Arquivo vazio.")
            exit(1)
        file.seek(0, 0)
        linhas = file.read().split('\n')
        matriz_jogadas = []  # Crio uma matriz para armazenar as jogadas do arquivo recebido

        for linha in linhas:
            linha.replace(" ", "")
            linha_dividida = re.split(',|:', linha)
            numero = False
            letra = True
            matriz_jogadas.append(linha_dividida)  # Adiciono as novas listas na matriz de jogadas
            for coord in linha_dividida:
                if (coord not in horizontal+"abcdefghi" and coord not in vertical) or len(linha_dividida) != 3:  # Aqui tem uma diferença. Incluo também a verificação de letras minúsculas como coordenadas.
                    print(f"AVISO: A jogada '{linha}' nao pode ser lida")  # Caso a coordenada esteja irregular com a condição acima...
                    matriz_jogadas.pop()  # ...não quero que encerre o programa, eu dou um pop no elemento que acabou de ser adicionado e finjo que ele não existiu.
                    break
                if not coord.isdigit() and letra:
                    numero = True
                    letra = False
                    pass
                elif coord.isdigit() and numero:
                    pass
                else:
                    print(f"AVISO: A jogada '{linha}' nao pode ser lida")
                    matriz_jogadas.pop()  # Removo imediatamente o que foi colocado na matriz se algo estiver trocado ou fora do padrão
                    break

        print("Arquivo de jogadas recebido! Processando MODO BATCH...")
        time.sleep(1)
        print()

    ##########################################################################
    # ABAIXO É EQUIVALENTE AO while True: DO MODO INTERATIVO. SÓ QUE USAREI  #
    # for PRA ITERAR SOBRE CADA LINHA DO ARQUIVO DE JOGO, POIS NÃO SE PEDE   #
    # INTERAÇÃO DO USUÁRIO, JÁ QUE VERIFICA TUDO AUTOMÁTICO                  #
    ##########################################################################

    for linha in matriz_jogadas:

        # Funciona de forma semelhante ao interativo, porém o trabalho exige exibir as coordenadas inválidas, portanto
        # é necessário alguns ajustes e uso de um módulo exclusivo pro modo batch.

        repetir_while = False

        entrada_lista = linha

        if entrada_lista[0] not in horizontal + "abcdefghi" or entrada_lista[1] not in vertical:
            print(f"A jogada ({entrada_lista[0]},{entrada_lista[1]} = {entrada_lista[2]} eh invalida!)")  # Checagem para saber se as coordenadas da linha lida do arquivo de jogo está de A a I ou 1 a 9.
            continue  # Ao inválidar a linha, verifica a próxima linha da matriz com 'continue'.

        if entrada_lista[2] not in vertical:
            print(f"A jogada ({entrada_lista[0]},{entrada_lista[1]} = {entrada_lista[2]} eh invalida!)")  # Checagem para saber se o valor atribuido a essa coordenada é de 1 a 9
            continue

        entrada_convertido_indices = conversao_coord_para_indice.entrada_coord_para_indices(entrada_lista)  # Substitui, das pistas, A...I e 1...9 por índices de 0 a 8 para o interpretador ler e trabalhar com listas e matriz 9x9

        for i in matriz_pistas_convertidas_com_indices:
            if entrada_convertido_indices[:2] == i[:2]:  # checagem pra saber se a coordenada lida no arquivo de jogo já tem uma pista.
                printar_coordenadas = entrada_convertido_indices  # VARIÁVEL ESPECIAL BATCH: Faço uma cópia da entrada convertida em índices...
                printar_coordenadas = batch.entrada_indices_para_coord(printar_coordenadas)  # ...para poder converter de volta de 0...8 para A...I e 1...9 (lin,col),...
                print(f"A jogada ({printar_coordenadas[0]},{printar_coordenadas[1]}) = {printar_coordenadas[2]} eh invalida!")  # ...assim posso printar as suas coordenadas reais no console em caso de jogada inválida. Isso não é necessário no modo interativo, pois não é exigido no trabalho.
                repetir_while = True
                break
        if repetir_while:
            continue

        if batch.repeticoes_quadrante_jogada(entrada_convertido_indices, tabuleiro):  # Checagem de todos os quadrantes. Uso o módulo especial batch, pois preciso printar as coordenadas inválidas no MODO BATCH.
            continue

        if batch.repeticoes_linha_coluna_jogada(entrada_convertido_indices, tabuleiro):  # Mesma coisa aqui, usando módulo batch
            continue

        tabuleiro = inserir_deletar.inserir_coordenada_tabuleiro(entrada_convertido_indices, tabuleiro)  # Se tudo certo, insere o valor no tabuleiro

        for i in tabuleiro:
            if 0 not in i:  # Se não tiver zeros na matriz, fechou o jogo
                print("A grade foi preenchida com sucesso!")
                time.sleep(1)
                exit(1)

    print("A grade nao foi preenchida!")  # PRINT ESPECIAL BATCH: Em caso de acabar as linhas do arquivo de jogadas, se não preencheu os zeros do tabuleiro, acabou o jogo.
    exit(1)
