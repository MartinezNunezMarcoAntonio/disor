
import wx

class PanelCifReverse(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent ,style=wx.SUNKEN_BORDER)
        self.label_texto = wx.StaticText(self, -1,style = wx.ALIGN_CENTER)
        self.txt_plano = wx.TextCtrl(self,size = (1,50),style = wx.TE_MULTILINE)

        self.__do_layout()
        self.__set_properties()

    def __do_layout(self):
        grilla = wx.BoxSizer(wx.VERTICAL)
        grilla.Add(self.label_texto,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10)
        grilla.Add(self.txt_plano,1,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
        self.SetSizer(grilla)

    def __set_properties(self):
        self.label_texto.SetLabel("Cifrado Reverse")

    def setValue(self,res):
        self.txt_plano.SetValue(res)
