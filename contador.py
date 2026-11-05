def contar_palavras(palavras):
    dic = {}
    palavras2 = ""
    for letra in palavras:  # .,;:!?
        if letra != "." and letra != "," and letra != ";" and letra != ":" and letra != "!" and letra != "?":
            palavras2 += letra

    lista = palavras2.split(" ")
    for palavra in lista:
        if palavra != "":
            dic[palavra] = 1
    return dic
