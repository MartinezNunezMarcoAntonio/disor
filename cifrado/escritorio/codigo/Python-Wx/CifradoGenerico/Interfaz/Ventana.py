
from Gestor.Gestor import Gestor
from Interfaz.TabOne import TabOne
import wx

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Cifrar")
        self.pestana_1 = wx.Panel(self)
        self.pestanas = wx.Notebook(self.pestana_1)

        Gest = Gestor()

        self.tab_1 = TabOne(self.pestanas,Gest)

        self.pestanas.AddPage(self.tab_1, "Tab 1")

        self.__do_layout()
        self.__set_properties()

    def __do_layout(self):
        sizer = wx.BoxSizer()
        sizer.Add(self.pestanas, 1, wx.EXPAND)
        self.pestana_1.SetSizer(sizer)

    def __set_properties(self):
        self.SetSize((1200, 750))



if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()