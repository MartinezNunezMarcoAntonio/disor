class Reverse:

    def __init__(self):
        self.palabra = ""
        self.resultado = "..."

    def cifrar(self):
        self.resultado = self.palabra[::-1]
