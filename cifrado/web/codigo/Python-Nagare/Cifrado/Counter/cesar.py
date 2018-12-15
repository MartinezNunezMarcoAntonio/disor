
class Cesar:

    def __init__(self ):
        self.palabra = ""
        self.salto = 0
        self.resultado = "..."
        self.alfabeto = self.Crearalfabeto()

    def cifrar(self):
        self.resultado = self.proceso( self.palabra ,self.salto )
        
    def proceso(self,orig, cont):
        e = self.alfabeto
        return "".join(list(map(lambda x: self.sustituir(x, e, cont), list(orig))))

    def sustituir(self,letra, lista, avanze):
        indice = lista.index(letra)
        tam = len(lista)
        if indice + avanze >= tam:
            return lista[(indice - tam) + avanze]
        return lista[indice + avanze]

    def Crearalfabeto(self):
        return list(map(chr, range(32, 254)))