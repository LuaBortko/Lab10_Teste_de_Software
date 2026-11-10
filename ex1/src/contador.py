def contar_palavras(texto):
    dic = {}
    texto = texto.lower()

    for sinal in ".,;:!?":
        texto = texto.replace(sinal, " ")

    lista = texto.split()

    for palavra in lista:
        if palavra not in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1

    return dic
