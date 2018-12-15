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

namespace JuegoVida
{
    public partial class MainWindow : Window
    {
        Gestor g = new Gestor();
        Button[] malla = new Button[702];
        Int32[] vec = new Int32[702];
        Boolean[] estado = new Boolean[702];

        public MainWindow()
        {
            InitializeComponent();

            g.creadorDeTableroDeEspacios(702);

            foreach (int i in Enumerable.Range(0,702))
            {
                Button button = new Button();
                malla[i] = button;
                button.Background = new SolidColorBrush(Colors.White);
                this.grid.Children.Add(button);
            }

            Button siguiente = new Button();
            siguiente.Background = new SolidColorBrush(Colors.Azure);
            siguiente.Content = "Avanzar";
            siguiente.Click += new RoutedEventHandler(clickeado);
            this.grid.Children.Add(siguiente);
        }

        private void clickeado(object sender, RoutedEventArgs e)
        {
            //Realizar la regla de vida o muerte
            //Actualizar Datos
        }
    }
}
