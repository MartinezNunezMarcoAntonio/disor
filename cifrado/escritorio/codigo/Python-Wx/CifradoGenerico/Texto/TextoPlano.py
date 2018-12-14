
class TextoPlano:
    def __init__(self ,entrada):
        self.textoInicial = entrada
        self.textoDiferen = ""
        self.anterior = ""

    def __str__(self):
        return self.textoInicial

    def __eq__(self, other):
        return self.textoInicial == other.textoInicial

    def __ge__(self, other):
        return len(self.textoInicial) >= len(other.textoInicial)

    def __lt__(self, other):
        return len(self.textoInicial) < len(other.textoInicial)

    def backOne(self ,txtNuevo):
        return self.anterior == txtNuevo.textoInicial

    def step(self ,txtNuevo):
        return (len(self.textoInicial) == len(txtNuevo.textoInicial)-1)

    def diference(self, txtNuevo):
        if self.backOne( TextoPlano(txtNuevo) ):
            self.textoDiferen = self.textoInicial[:-1] if len(self.textoInicial) > 0 else ""
        else:
            self.textoDiferen = txtNuevo[-1] if len(txtNuevo)>0 else ""

    def refresh(self ,txtNuevo):
        self.anterior = self.textoInicial
        self.textoInicial = txtNuevo
