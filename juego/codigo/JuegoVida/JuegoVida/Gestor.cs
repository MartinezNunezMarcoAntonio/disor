using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace JuegoVida
{
    class Gestor
    {
        List<EspacioHabitacional> espacios;
        int lado = 1;
        int elementos = 0;

        public void creadorDeTableroDeEspacios( int numeroElementos )
        {
            elementos = obtenerElementosCuadratico( numeroElementos );
            espacios = insertarElementos( elementos );
            insertarCelulasEnEspacios( espacios, numeroElementos );
        }

        private void insertarCelulasEnEspacios(List<EspacioHabitacional> espacios, int numeroElementos)
        {
            foreach( EspacioHabitacional esp in espacios )
            {
                esp.setHabitante( new Habitante() );
            }
        }

        public int obtenerElementosCuadratico( int numeroElementos )
        {
            int elem = 0;
            while (lado * lado >= numeroElementos)
            {
                lado += 1;
                elem = lado * lado;
            }
            return elem;
        }

        public List<EspacioHabitacional> insertarElementos( int numeroElementos )
        {
            List<EspacioHabitacional> esp = new List<EspacioHabitacional>();
            foreach (int i in Enumerable.Range(0, numeroElementos))
            {
                esp.Add(new EspacioHabitacional(i + ""));
            }
            return esp;
        }

    }
}
