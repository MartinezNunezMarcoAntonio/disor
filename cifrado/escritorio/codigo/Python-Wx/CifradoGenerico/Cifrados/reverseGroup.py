
from Cifrados.reverse import Reverse

class ReverseGroup:

    def __init__(self , Texto, valor):
        self.txt = Texto
        self.grup = valor
        self.res = ""
        self.cifradoAnterior = ""

    def cifrar(self,txt,group):
        if group <2:
            self.res = txt
            return
        if group >= len(txt):
            self.res = Reverse("").cifra(txt)
            return

        lis = zip(*([iter(txt)]*group))
        part = [ Reverse("").cifra("".join(i)) for i in lis  ]
        if len(txt)%group != 0:
            self.res = "".join(part) + txt[-(len(txt)%group):]
        else:
            self.res = "".join(part)