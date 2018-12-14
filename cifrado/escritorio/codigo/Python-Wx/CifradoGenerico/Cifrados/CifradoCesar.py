
class CifradoCesar:

    def __init__(self , Texto, valor):
        self.cif = Texto
        self.avanze = valor
        self.cifradoAnterior = ""

        self.alfabeto = self.Crearalfabeto()

    def cifrar(self ,txtnew ,value):
        self.valor = value
        self.cifradoAnterior = self.cif
        self.cif = self.palabra(txtnew,value)

    def palabra(self,orig, cont):
        e = self.alfabeto
        return "".join(list(map(lambda x: self.sustituir(x, e, cont), list(orig))))

    def sustituir(self,letra, lista, avanze):
        indice = lista.index(letra)
        tam = len(lista)
        if indice + avanze >= tam:
            return lista[(indice - tam) + avanze]
        return lista[indice + avanze]

    def Crearalfabeto(self):
        return list(map(chr, range(32, 126)))