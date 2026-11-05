def contar_palavras(palavras):
    dic = {}
    if palavras != "":
        lista = palavras.split(" ")
        for palavra in lista:
            dic[palavra] = 1
    return dic
