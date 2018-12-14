

from __future__ import with_statement

import os
import datetime
from nagare import presentation,var
from gestor import Gestor


class Counter(object):
    def __init__(self):
        self.gestor = Gestor()
        self.resultados = []
        self.palabra = ""

    def setPalabra(self, msg):
        self.gestor.pala = msg
        self.palabra = msg
    
    def setVarCesar(self,msg):
        self.gestor.cesar.salto = int(msg)

    def setVarReverse(self,msg):
        self.gestor.reverse_g.grupo = int(msg)
        self.gestor.cifrar()

@presentation.render_for(Counter)
def render(self, h, *args):

    with h.form:
        h << 'Palabra a cifrar:' << h.br
        h << h.textarea.action( self.setPalabra) << h.br
        h << 'Cesar:' << h.br
        h << h.select(h.option(str(i)) for i in range(0,10) ).action(self.setVarCesar) <<h.br
        h << h.blockquote(self.gestor.cesar.resultado) << h.hr
        
        h << 'Reverse:' << h.br
        h << h.blockquote(self.gestor.reverse.resultado) << h.hr
        
        h << 'Reverse G:' << h.br
        h << h.select(h.option(str(i)) for i in range(0,10) ).action(self.setVarReverse) <<h.br
        h << h.blockquote(self.gestor.cesar.resultado) << h.br
        h << h.input(type='submit', value='Cifrar')
            

            

    return h.root

# ---------------------------------------------------------------

app = Counter

