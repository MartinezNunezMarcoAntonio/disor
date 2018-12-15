
import wx
from Gestor.Gestor import Gestor

class PanelTexto(wx.Panel):
    def __init__(self, parent,panel_cif,Gest):
        wx.Panel.__init__(self, parent)
        self.panel_cif = panel_cif
        self.Gest = Gest

        self.label_texto = wx.StaticText(self, -1,style = wx.ALIGN_CENTER)
        self.txt_plano = wx.TextCtrl(self,size = (1,50),style = wx.TE_MULTILINE)

        self.__do_layout()
        self.__event__()
        self.__set_properties()

    def __do_layout(self):
        grilla = wx.BoxSizer(wx.VERTICAL)
        grilla.Add(self.label_texto,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL)
        grilla.Add(self.txt_plano,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL)
        self.SetSizer(grilla)

    def __set_properties(self):
        self.label_texto.SetLabel("Texto Plano")

    def __event__(self):
        self.txt_plano.Bind(wx.EVT_CHAR, self.acc_main)

    def acc_main(self, event):
        if chr(event.GetKeyCode()).isprintable():
            txt = self.txt_plano.GetValue() + chr(event.GetKeyCode())
            salto = int(self.panel_cif.panel_cesar.getValue() )
            group = int(self.panel_cif.panel_reverG.getValue() )

            self.Gest.datoExternoTXT(txt,salto,group)
            self.panel_cif.panel_cesar.setValue(self.Gest.cifC.cif)
            self.panel_cif.panel_rever.setValue(self.Gest.cifRev.res)
            self.panel_cif.panel_reverG.setValue(self.Gest.cifRevG.res)

        event.Skip()