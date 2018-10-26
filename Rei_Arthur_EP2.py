import re

def verifica_encalhada(Lista_escolhas_damas):


    return 1


with open (".\casamento.txt","r") as casamento:
    damas_nomes,damas_c, cavaleiros_nomes, damas_escolhas, temp, index = [], [], [], [], [], 0
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
    print ("\n Escolha das damas com cavaleiros: '{0}'".format( damas_escolhas))


    # Função recursiva para escolha dos candidatos
    for escolha in damas_escolhas: #Percorrer o array de nomes guardados -> [['Jessica Adriano'], ['Fernanda Bruno Gabriel Leandro'], ['Pamela Adriano Diogo Leandro'], ['Renata Adriano Walber']]
        escolha = list(escolha[0].split())  #Remover os espacos em branco para separar as palavras de -> ['Jessica Adriano'] para -> ['Jessica', 'Adriano']      
        for verifica_disponibilidade in (escolha[1:]): #O escolha[1:] Faz ignorar o primeiro dado do Array Ex.: ['Jessica', 'Adriano']  para ['Adriano'] 
            temp = []
            temp = set(verifica_disponibilidade) #Criando a lista em modo SET para verificar os conjuntos
            if (temp.issubset(cavaleiros_nomes)): #Verificando se o nome do cavaleiro faz parte do conjunto dos cavaleiros, caso seja verdadeiro irei remover da lista de referencia atestando como disponivel e escolhido, caso contrario Verifico o proximo cavaleiro disponvel escolhido pela dama
                print ("o nome '{0}' está na lista: \n '{1}".format(verifica_disponibilidade, cavaleiros_nomes))
            else:
                print ("o nome '{0}' NÃO está na lista: \n '{1}'".format(verifica_disponibilidade, cavaleiros_nomes))
                #VERIFICAR PORQUE ESTA CAINDO TUDO NO ELSE!
    
    casamento.close()


"""with open (".\cavaleiros.txt","r") as cavaleiros:
    mesa = cavaleiros.readlines()

    cavaleiros.close()"""
