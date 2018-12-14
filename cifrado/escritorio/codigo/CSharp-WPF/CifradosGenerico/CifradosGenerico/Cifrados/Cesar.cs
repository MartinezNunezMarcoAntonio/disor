using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CifradosGenerico.Cifrados
{
    class Cesar 
    {
        public String palabra = "";
        public int salto = 0;
        public String resultado = "";



        public void CargarRequerimientos(int valor)
        {
            salto = valor;
        }
        public void Cifrar()
        {
            resultado = proce( palabra , salto );
        }
        public int Desifrar(String s)
        {
            return 0;
        }

        ////////////////////////////////////////////////////////////////
        static string abc = "abcdefghijklmñnopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890_-+,#$%&/()=¿?¡!|,.;:{}[]";
        static string proce(string mensaje, int desplazamiento)
         {
             String cifrado = "";
             if (desplazamiento > -1 && desplazamiento<abc.Length )
             {                
                 for (int i = 0; i<mensaje.Length; i++)
                 {
                     int posCaracter = getPosABC(mensaje[i]);
                     if (posCaracter != -1) 
                     {
                         int pos = posCaracter + desplazamiento;
                         while (pos >= abc.Length)
                         {
                             pos = pos - abc.Length;                           
                         }                   
                         cifrado += abc[pos];
                     }
                     else
                     {
                         cifrado += mensaje[i];
                     }            
                 }
 
             }
             return cifrado;
         }

        static int getPosABC(char caracter)
         { 
             for(int i=0; i<abc.Length ; i++)
             {
                 if (caracter == abc[i])
                 {
                     return i;
                 }
             }
             return -1;
         }

    }
}
