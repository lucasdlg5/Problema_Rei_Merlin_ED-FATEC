import re

"""with open (".\casamento.txt","r") as casamento:
    damas_nomes,damas_c, cavaleiros_nomes, damas_escolhas, temp, index, cont_noivas = [], [], [], [], [], 0, 0
    damas = casamento.readlines()
    for dama in damas:
        
        #Capturando e separando dados de Damas e cavaleiros

        damas_c = re.findall(r"[\w']+",dama) #Guardando lista de casamento das damas com cavaleiros
        temp = [] #Zerando vetor para receber somente a nova sequencia (Uma delas: (Fernanda Bruno Gabriel Leandro))
        temp.append(dama.rstrip()) #.rstrip() remove todos os padroes de quebra de linha ou espaços em branco de codigo (\n e \r)
        damas_escolhas.append(temp) #Guardando lista separada das escolhas das damas (Fernanda Bruno Gabriel Leandro)
        damas_nomes.append(damas_c[0]) #Guardando nome das damas
        for c in damas_c[1:]: #Percorrendo a lista de cavaleiros disponiveis escolhido pelas damas, ignorando a primeira casa
            cavaleiros_nomes.append(c) #Guardando nomes dos cavaleiros
        cavaleiros_nomes = list (set(cavaleiros_nomes)) #Removendo nomes duplicados da lista de cavaleiros disponiveis

    print ("\n Nome das damas: '{0}'" .format(damas_nomes))
    print ("\n Cavaleiros escolhidos pelas damas: '{0}'".format( cavaleiros_nomes))
    print ("\n Escolha das damas com cavaleiros: '{0}' \n".format( damas_escolhas))


    # Função recursiva para escolha dos candidatos
    for escolha in damas_escolhas: #Percorrer o array de nomes guardados -> [['Jessica Adriano'], ['Fernanda Bruno Gabriel Leandro'], ['Pamela Adriano Diogo Leandro'], ['Renata Adriano Walber']]
        escolha = list(escolha[0].split())  #Remover os espacos em branco para separar as palavras de -> ['Jessica Adriano'] para -> ['Jessica', 'Adriano']      
        for verifica_disponibilidade in (escolha[1:]): #O escolha[1:] Faz ignorar o primeiro dado do Array Ex.: ['Jessica', 'Adriano']  para ['Adriano'] 
            temp = []
            temp = set([verifica_disponibilidade]) #Criando a lista em modo SET para verificar os conjuntos OBS.: Foi obrigatorio inserir os colchetes na variavel do FOR para que a funcao do ISSUBSET funcionacsse para buscar se é um conjunto ou nao!
            if (temp.issubset(cavaleiros_nomes)): #Verificando se o nome do cavaleiro faz parte do conjunto dos cavaleiros, caso seja verdadeiro irei remover da lista de referencia atestando como disponivel e escolhido, caso contrario Verifico o proximo cavaleiro disponvel escolhido pela dama
                # print ("o nome '{0}' ESTÁ na lista: \n '{1}".format(verifica_disponibilidade, cavaleiros_nomes))
                # print ("O nome '{0}' ESTÁ na lista! Removendo. ".format(verifica_disponibilidade))
                cavaleiros_nomes.pop(cavaleiros_nomes.index(verifica_disponibilidade)) #Primeiro localizo a posicao do nome do cavaleiro no array usando cavaleiros_nomes.index("nome") para depois remover com o POP da lista
                # print (cavaleiros_nomes)
                cont_noivas +=1 #Faz a contagem se todas as noivas conseguiram seus pares!
                break #Precisa desse break para sair do FOR, senão ira percorrer todos os candidatos escolhido pelas damas e remover todos eles mesmo já com um disponivel
            # else:
                # print ("O nome '{0}' NÃO está na lista: \n '{1}'".format(verifica_disponibilidade, cavaleiros_nomes))
                # print ("A noiva '{0}' ficou sem par! Pois o '{1}' não estava disponivel.".format(escolha[:1],verifica_disponibilidade))
                
    if (cont_noivas != len(damas_escolhas)): #Atraves da contagem de quantas noivas sairam com pares, preciso confirmar se este numero condiz com a lista inicial!
        print ("A quantidade de escolhas '{0}' foi diferente de numero de noivas '{1}'".format (cont_noivas, len(damas_escolhas)))
    else:
        print("Todas as noivas tiveram seus pares!!")
    casamento.close()"""


with open (".\cavaleiros2.txt","r") as cavaleiros:
    sequencia, temp = [], []
    mesa = cavaleiros.readlines()
    for combinacao in mesa:
        sequencia.append(combinacao.split())
    print ("Total de combinacoes: '{0}'\n Lista: '{1}'".format(len(sequencia), sequencia))
    cavaleiros.close()
