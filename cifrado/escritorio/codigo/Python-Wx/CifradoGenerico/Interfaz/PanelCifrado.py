
from Interfaz.Cifrados.Cesar import PanelCifCesar
from Interfaz.Cifrados.Reverse import PanelCifReverse
from Interfaz.Cifrados.ReverseGroup import PanelCifReverseGrup
import wx

class PanelCifrados(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.panel_cesar = PanelCifCesar(self)
        self.panel_rever = PanelCifReverse(self)
        self.panel_reverG = PanelCifReverseGrup(self)

        self.__do_layout()
        self.__set_properties()

    def __do_layout(self):
        grilla = wx.BoxSizer(wx.HORIZONTAL)
        grilla.Add(self.panel_cesar,1,  wx.ALL|wx.EXPAND)
        grilla.Add(self.panel_rever,1,  wx.ALL|wx.EXPAND)
        grilla.Add(self.panel_reverG,1,  wx.ALL|wx.EXPAND)
        self.SetSizer(grilla)

    def __set_properties(self):
        pass