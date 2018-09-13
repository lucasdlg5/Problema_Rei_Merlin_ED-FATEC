import re
with open (".\casamento.txt","r") as casamento:
    damas = casamento.readlines()
    for dama in damas:
        #d = dama.split(" ")
        print (re.findall(r"[\w']+",dama))
        #print (d)
    
    casamento.close()


"""with open (".\cavaleiros.txt","r") as cavaleiros:
    mesa = cavaleiros.readlines()

    cavaleiros.close()"""
