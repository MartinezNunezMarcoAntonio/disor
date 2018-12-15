# Juego de la vida

## Contemplaciones de escalabilidad - FALCON EYE y NET HACK
1. Celdas en tiempo de ejecucion
2. forma de la malla
3. Relacion entre mallas
4. Reglas que se aplican y a las celulas que se aplican
5. La forma en que los turnos funcionan y puede que algo <br>pase a otro turno o un filtro se cumpla cada N turnos


## Observaciones
* Idea de eventos como parte de el diseño
* cada Celula debe saber sobre sus vecinos y debe notificar cada vez que se salga de la malla

# Eventos
* Recibira por parte de una celula una señal de solicitud
* Recibira por parte de una celula señal de solicitud Salida
#### Evento llegada
*  Gestionar la solicitud de las celulas y llevarlas a cabo o no
#### Evento Salida
* Evaluar la solicitud de la celula y aprobarla o rechazarla

# Celula
* Conoce a sus vecinos otras celulas
* Notifica cada vez que va a abandonar el siguiente turno
* Notifica a todos los vecinos que ha llegado
    
#### Solicitud
* Proceso por el cual la celula realiza la peticion esta solicitud le son asignadas diferentes reglas para ser aprobada o no y finalmente el evento decidir si aprobarla o no
#### DimensionPosition
* Almacenará una celula 
* Posicion en un espacio del cual organizará a las celulas esto sirve en caso de que la posicion de una celula se vuelva mas compleja y no sea la celula la encargada de esa tarea

# Reglas
    Modelo de abstraccion para cada clase que sea una regla y esta en general se aplicara a todas las celulas pero brindando la posibilidad de no aplicar ciertas reglas a ciertas celulas
#### Filtro Reglas
    Caracteristicas que cumplen ciertas celulas para que se les aplique las reglas
    
# Turno
#### Turno1
    Clase ecargada de guardar turnos anteriores y ademas dar los pasos para los siguientes calculos
# Ejecucion
#### Malla
    Conjunto de DimensionPositions que pueden ser ocupados por una celula
#### Gestor
    Clase encargada de relacionar


### Abstraccion de Vecinos
    EL vecino debe ser un concepto asignado y de abstraccion ya que los vecinos
    asignarVecinos( )
    donde unicamente hay que agregar nuevas ideas de vecindad y restricciones para que estas celulas almacenen a sus vecinos
