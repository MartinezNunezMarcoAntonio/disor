from __future__ import with_statement

import os
import datetime
from nagare import presentation,var


class Counter(object):
    def __init__(self):
        self.nb = 0

    def clic(self):
        self.nb += 1



@presentation.render_for(Counter)
def render(self, h, *args):
    h << h.textarea.action(self.clic) << h.br
    h << h.p(
                'You haveeee ', h.a('clicked').action(self.clic),
                ' ', self.nb, ' times.'
              )

            

    return h.root

# ---------------------------------------------------------------

app = Counter