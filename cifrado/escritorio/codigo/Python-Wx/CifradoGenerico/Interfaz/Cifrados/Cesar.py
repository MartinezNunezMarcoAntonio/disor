
import wx

class PanelCifCesar(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent ,style=wx.SUNKEN_BORDER)
        elem = [str(i) for i in range(0,100)]
        self.label_texto = wx.StaticText(self, -1,style = wx.ALIGN_CENTER)
        self.label_advice = wx.StaticText(self, -1,style = wx.ALIGN_LEFT)
        self.txt_plano = wx.TextCtrl(self,size = (1,50),style = wx.TE_MULTILINE)
        self.combo = wx.ComboBox(self, -1, "3", (15, 30),wx.DefaultSize, elem, wx.CB_DROPDOWN)

        self.__do_layout()
        self.__event__()
        self.__set_properties()

    def __do_layout(self):
        grilla = wx.BoxSizer(wx.VERTICAL)
        grilla.Add(self.label_texto,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,10)
        grilla.Add(self.label_advice,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
        grilla.Add(self.combo,0,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
        grilla.Add(self.txt_plano,1,  wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL,5)
        self.SetSizer(grilla)

    def __set_properties(self):
        self.label_texto.SetLabel("Cifrado Cesar")
        self.label_advice.SetLabel("Numero de Pasos:")

    def __event__(self):
        self.combo.Bind(wx.EVT_COMBOBOX, self.OnCombo)

    def OnCombo(self, event):
        pass

    def getValue(self):
        return self.combo.GetValue()
    def setValue(self,res):
        self.txt_plano.SetValue(res)