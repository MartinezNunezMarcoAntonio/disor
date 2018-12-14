package com.example.vok

class Gestor
{
    var palabra = ""
    var cesar = Cesar()
    var reverse = Reverse()
    var reverse_g = ReverseG()

    fun cifrar(palab:String)
    {
        cesar.palabra = palab
        reverse.palabra = palab
        reverse_g.palabra = palab

        cesar.cifrar()
        reverse.cifrar()
        reverse_g.cifrar()
    }

    fun cifradoSinActualizacion()
    {
        cesar.cifrar()
        reverse.cifrar()
        reverse_g.cifrar()
    }
    
}