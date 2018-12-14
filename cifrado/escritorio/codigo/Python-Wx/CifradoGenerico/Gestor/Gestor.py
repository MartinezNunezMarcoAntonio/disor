
from Texto.TextoPlano import TextoPlano
from Cifrados.CifradoCesar import CifradoCesar
from Cifrados.reverse import Reverse
from Cifrados.reverseGroup import ReverseGroup

class Gestor:

    def __init__(self):
        self.text = TextoPlano("")
        self.cifC = CifradoCesar("", 3)
        self.cifRevG = ReverseGroup("", 3)
        self.cifRev = Reverse("")

    def datoExternoTXT(self, nuevo ,val ,val2):
        resp = TextoPlano(nuevo)
        self.text.diference(nuevo)

        self.ActualizarcifradoRev(resp,nuevo)
        self.ActualizarcifradoCesar(nuevo ,val)
        self.ActualizarcifradoRevGroup(nuevo ,val2)

        self.text.refresh(nuevo)

    def ActualizarcifradoRev(self ,resp,txt):
        if self.text.backOne(resp):
            self.cifRev.back()
        elif self.text.step(resp):
            self.cifRev.front(self.text.textoDiferen)
        else:
            self.cifRev.cifra(txt)

    def ActualizarcifradoCesar(self ,txt,salto):
        self.cifC.cifrar(txt,salto)

    def ActualizarcifradoRevGroup(self ,txt,group):
        self.cifRevG.cifrar(txt,group)


