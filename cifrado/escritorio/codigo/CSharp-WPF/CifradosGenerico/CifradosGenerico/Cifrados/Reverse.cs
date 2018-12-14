using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CifradosGenerico.Cifrados
{
    class Reverse 
    {

        public String palabra = "";
        public String resultado = "";

        public void Cifrar()
        {
            resultado = revert(palabra);
        }
        public int Desifrar(String s)
        {
            return 0;
        }

        /////////////////////////////////
        public string revert(string s)
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
