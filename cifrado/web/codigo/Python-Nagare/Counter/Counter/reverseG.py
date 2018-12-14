class ReverseG:

    def __init__(self ):
        self.palabra = ""
        self.grupo = 0
        self.resultado = "..."

    def cifrar(self):
        self.resultado = self.proceso(self.palabra ,self.grupo)

    def proceso(self,txt,group):
        if group <2:
            self.res = txt
            return
        if group >= len(txt):
            self.res = txt[::-1]
            return

        lis = zip(*([iter(txt)]*group))
        part = [ "".join(i)[::-1] for i in lis  ]
        if len(txt)%group != 0:
            self.res = "".join(part) + txt[-(len(txt)%group):]
        else:
            self.res = "".join(part)