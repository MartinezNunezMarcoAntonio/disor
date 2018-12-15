
from __future__ import with_statement

import os
import datetime
from nagare import presentation,var


class Counter(object):
    def __init__(self):
        self.cesar = Cesar("cesar")
        self.reverse = Reverse("reverse")
        self.resultados = []
        self.ejemplo = "antes"
        self.nb = 0

    def setPalabra(self, msg):
        self.ejemplo = msg
        self.cesar.asignarPalabra(msg)
        self.reverse.asignarPalabra(msg)
    
    def setVarCesar(self,msg):
        self.cesar.cifrar(msg)
        self.resultados.append(str( self.cesar.resultado ))

    def setVarReverse(self,msg):
        self.reverse.cifrar(msg)
        self.resultados.append(str( self.reverse.resultado ))


class Cesar:
    def __init__(self,pal):
        self.palabra = pal
        self.resultado = ""
    
    def asignarPalabra(self,msg):
        self.palabra = msg
    
    def cifrar(self,msg):
        self.resultado = self.palabra + str(msg)

class Reverse:
    def __init__(self,pal):
        self.palabra = pal
        self.resultado = ""

    def asignarPalabra(self,msg):
        self.palabra = msg

    def cifrar(self,msg):
        self.resultado = self.palabra + str(msg)



@presentation.render_for(Counter)
def render(self, h, *args):

    with h.form:
        h << 'Palabra a cifrar:' << h.br
        h << h.textarea.action(self.setPalabra) << h.br
        h << h.select(h.option(str(i)) for i in range(0,10) ).action(self.setVarCesar) <<h.br
        h << h.select(h.option(str(i)) for i in range(0,10) ).action(self.setVarReverse) <<h.br
        h << h.input(type='submit', value='Cifrar')
    with h.div:
        for msg in self.resultados:
            h << h.blockquote(msg) << h.hr

            

    return h.root

# ---------------------------------------------------------------

app = Counter
