using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace CifradosGenerico
{
    public partial class MainWindow : Window
    {
        Gestor gestor = new Gestor();
        public MainWindow()
        {
            InitializeComponent();
            res_cesar.Text = gestor.cesar.resultado;
            res_reverse.Text = gestor.reverse.resultado;
            res_reverseg.Text = gestor.reverseG.resultado;
        }

        private void change(object sender, TextChangedEventArgs e)
        {
            gestor.cifrar(txt_cifrar.Text);
            actualizar();
        }

        private void eventoSalto(object sender, EventArgs e)
        {
            gestor.cesar.salto = Int32.Parse(cmb_cesar_1.Text);
            gestor.cifrarSinActualizacion();
            actualizar();
        }
        private void eventoGrupo(object sender, EventArgs e)
        {
            gestor.reverseG.grupo = Int32.Parse(cmb_reverseg_1.Text);
            gestor.cifrarSinActualizacion();
            actualizar();
        }


        ////////////////////////////////////////////////////////////////////////
        
        public void actualizar()
        {
            res_cesar.Text = gestor.cesar.resultado;
            res_reverse.Text = gestor.reverse.resultado;
            res_reverseg.Text = gestor.reverseG.resultado;
        }
    }
}
