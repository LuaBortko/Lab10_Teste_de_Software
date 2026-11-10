class Fila:
    def __init__(self):
        self.normais = []
        self.prioritarias = []
        self.contador_normal = 0
        self.contador_prioritaria = 0
        self.prioritarias_seguidas = 0

    @property
    def aguardando(self):
        return len(self.normais) + len(self.prioritarias)

    def emitir(self, tipo):
        if tipo == "normal":
            self.contador_normal += 1
            senha = "N" + str(self.contador_normal)
            self.normais.append(senha)
            return senha

        elif tipo == "prioritaria":
            self.contador_prioritaria += 1
            senha = "P" + str(self.contador_prioritaria)
            self.prioritarias.append(senha)
            return senha

        else:
            raise ValueError("tipo invalido")

    def chamar(self):
        if self.aguardando == 0:
            raise IndexError("fila vazia")

        if self.prioritarias and (
            self.prioritarias_seguidas < 2 or not self.normais
        ):
            self.prioritarias_seguidas += 1
            return self.prioritarias.pop(0)

        self.prioritarias_seguidas = 0
        return self.normais.pop(0)
