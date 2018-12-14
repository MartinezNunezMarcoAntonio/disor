using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using CifradosGenerico.Cifrados;

namespace CifradosGenerico
{
    class Gestor
    {
        public Cesar cesar;
        public Reverse reverse;
        public ReverseG reverseG;
        

        public Gestor()
        {
            cesar = new Cesar();
            reverse = new Reverse();
            reverseG = new ReverseG();
        }
        public void cifrar( String pala )
        {
            cesar.palabra = pala;
            reverse.palabra = pala;
            reverseG.palabra = pala;

            cesar.Cifrar();
            reverse.Cifrar();
            reverseG.Cifrar();
        }
        public void cifrarSinActualizacion()
        {
            cesar.Cifrar();
            reverse.Cifrar();
            reverseG.Cifrar();
        }
    }
}
