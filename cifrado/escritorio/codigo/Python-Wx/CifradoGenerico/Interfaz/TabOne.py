
from Interfaz.PanelCifrado import PanelCifrados
from Interfaz.PanelTexto import PanelTexto
import wx

class TabOne(wx.Panel):
    def __init__(self, parent,Gest):
        wx.Panel.__init__(self, parent)
        self.Gest = Gest
        self.panel_2 = PanelCifrados(self)
        self.panel_1 = PanelTexto(self,self.panel_2 ,self.Gest)

        self.__do_layout()
        self.__set_properties()

    def __do_layout(self):
        grilla = wx.BoxSizer(wx.VERTICAL)
        grilla.Add(self.panel_1,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20)
        grilla.Add(self.panel_2,1,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 20)
        self.SetSizer(grilla)

    def __set_properties(self):
        pass