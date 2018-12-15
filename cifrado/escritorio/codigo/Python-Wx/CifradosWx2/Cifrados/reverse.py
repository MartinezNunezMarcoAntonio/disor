
class Reverse:

    def __init__(self , Texto):
        self.txt = Texto
        self.res = ""
        self.cifradoAnterior = ""

    def cifra(self,txtnew):
        self.cifradoAnterior = self.res
        self.res = txtnew[::-1]
        return self.res

    def front(self ,caracter):
        self.cifradoAnterior = self.res
        self.res = caracter +self.res

    def back(self):
        aux = self.cifradoAnterior
        self.cifradoAnterior = self.res
        self.res = aux

    def __str__(self):
        return self.res