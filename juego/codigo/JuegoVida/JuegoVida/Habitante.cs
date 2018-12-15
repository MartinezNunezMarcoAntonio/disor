using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoVida
{
    class Habitante
    {
        String identificador;
        String estado_previo_salida;
        IEnumerable<Habitante> vecinos;


        public void notificarLlegada()
        {
        }
        public void notificarAbandono()
        {

        }
    }
}
