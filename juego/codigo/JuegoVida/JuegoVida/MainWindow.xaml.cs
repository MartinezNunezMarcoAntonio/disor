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
using System.Threading;

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
            siguiente.Content = "Next";
            siguiente.Click += new RoutedEventHandler(clickeado);
            this.grid.Children.Add(siguiente);


        }

        private void clickeado(object sender, RoutedEventArgs e)
        {
            var seed = Environment.TickCount;
            var random = new Random(seed);
            SolidColorBrush blanco = new SolidColorBrush(Colors.White);
            SolidColorBrush negro = new SolidColorBrush(Colors.Black);

            for (int i = 0; i <= 100; i++)
            {
                var value = random.Next(0, 702);
                if( malla[value].Background == negro )
                {
                    malla[value].Background = blanco;
                }
                else
                {
                    malla[value].Background = negro;
                }
                
            }
            for (int i = 0; i <= 250; i++)
            {
                var value = random.Next(0, 702);
                malla[value].Background = blanco;

            }
        }
    }
}
