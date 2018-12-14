
from cesar import Cesar
from reverse import Reverse
from reverseG import ReverseG


class Gestor:
    def __init__(self):
        self.cesar = Cesar()
        self.reverse = Reverse()
        self.reverse_g = ReverseG()
        self.pala = "";

    def cifrar(self):
        self.cesar.palabra = self.pala
        self.reverse.palabra = self.pala
        self.reverse_g.palabra = self.pala

        self.cesar.cifrar()
        self.reverse.cifrar()
        self.reverse_g.cifrar()

    def cifrarSinActualizacion(self):
        self.cesar.cifrar()
        self.reverse.cifrar()
        self.reverse_g.cifrar()
