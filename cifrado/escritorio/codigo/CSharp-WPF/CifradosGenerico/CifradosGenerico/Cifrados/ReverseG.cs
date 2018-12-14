using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CifradosGenerico.Cifrados
{
    class ReverseG
    {

        public String palabra = "";
        public int grupo = 0;
        public String resultado = "";

        public int CargarRequerimientos(int valor)
        {
            return grupo = valor;
        }
        public void Cifrar()
        {
            resultado = proceso( palabra ,grupo );
        }
        public int Desifrar(String s)
        {
            return 0;
        }

        /////////////////////////////////

        public String proceso(String palabra ,int grupo)
        {
            String parte = "";
            ArrayList myAL = new ArrayList();
            if (  grupo < 2 )
            {
                return palabra;
            }
            if(grupo >= palabra.Length)
            {
                return revert(palabra);
            }
        
            foreach(int vak in Enumerable.Range(0, palabra.Length / grupo) )
            {
                String aux = palabra.Substring(vak * grupo,  grupo);
                myAL.Add(aux);
            }
        
            foreach(String vak in myAL)
            {
                parte += revert(vak);
            }
            if( palabra.Length % grupo != 0 )
            {
                return parte + " - " + palabra.Substring(parte.Length, (palabra.Length - parte.Length) );
            }
            else {
                return parte;
            }
        }

        public string revert(string s)
        {
            char[] charArray = s.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
