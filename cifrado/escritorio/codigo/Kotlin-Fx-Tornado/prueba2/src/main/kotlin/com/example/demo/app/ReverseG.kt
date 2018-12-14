package com.example.demo.app

class ReverseG
{
    
    var palabra = ""
    var grupo = 0
    var resultado = ""
    fun preCifrado( grupo:Int )
    {
        this.grupo = grupo
    }
    fun cifrar()
    {
        resultado = proceso()
    }
    fun proceso():String
    {
        var parte = ""
        val list: ArrayList<String> = ArrayList()
        if(  grupo < 2 )
        {
            return palabra
        }
        if(grupo >= palabra.length)
        {
            return palabra.reversed()
        }
    
        for(vak in 0..palabra.length/grupo-1)
        {
            var aux = palabra.subSequence(vak*grupo,(vak*grupo)+grupo )
            list.add( aux.toString() )
        }
        
        for(vak in list)
        {
            parte += vak.reversed()
        }
        if( palabra.length % grupo != 0 )
        {
            return parte+ palabra.reversed().subSequence(0,palabra.length.rem(grupo) ).reversed()
        }
        else {
            return parte
        }

        
    }

}