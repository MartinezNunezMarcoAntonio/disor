using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CifradosGenerico.Cifrados
{
    interface ICifrados
    {
        int CargarRequerimientos(List<String> req);
        int Cifrar(String texto);
        int Desifrar(String texto);
    }
}
