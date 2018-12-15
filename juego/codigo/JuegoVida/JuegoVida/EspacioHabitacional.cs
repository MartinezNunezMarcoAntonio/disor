using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoVida
{
    class EspacioHabitacional
    {
        String identificador;
        String actual = "Habitado, disponible";

        Habitante habitante_actual;

        public void setHabitante( Habitante hab )
        {
            this.habitante_actual = hab;
        }

        public EspacioHabitacional(String id)
        {
            this.identificador = id;
            this.actual = "disponible";
        }
    }
}
