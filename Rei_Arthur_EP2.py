import re
def verifica_encalhada(lista):
    return 1

with open (".\casamento.txt","r") as casamento:
    damas_nomes,damas_c, cavaleiros_nomes = [], [], []
    damas = casamento.readlines()
    for dama in damas:
        
        damas_c = re.findall(r"[\w']+",dama) #Guardando lista de casamento das damas com cavaleiros
        damas_nomes.append(damas_c[0]) #Guardando nome das damas
        for c in damas_c[1:]: #Percorrendo a lista de cavaleiros disponiveis escolhido pelas damas, ignorando a primeira casa
            cavaleiros_nomes.append(c) #Guardando nomes dos cavaleiros

        
    print ("Nome das damas: %s" % damas_nomes)
    print ("Nome dos cavaleiros: %s" % cavaleiros_nomes)
    casamento.close()


"""with open (".\cavaleiros.txt","r") as cavaleiros:
    mesa = cavaleiros.readlines()

    cavaleiros.close()"""
