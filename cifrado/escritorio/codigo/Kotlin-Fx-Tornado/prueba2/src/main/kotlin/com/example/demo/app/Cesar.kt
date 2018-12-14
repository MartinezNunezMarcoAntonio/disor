package com.example.demo.app

class Cesar
{
    var palabra = ""
    var salto = 0
    var resultado = ""
    
    fun preCifrado( salto:Int )
    {
        this.salto = salto
    }
    fun cifrar()
    {
        resultado = crear( palabra ,salto )
    }

    fun crear(orig:String,avanze:Int):String
    {
        var nuevo = ""
        for(letra in orig)
        {
            var aux = Character.toString(letra)
            nuevo += sustituir(aux, crearAlfabeto(), avanze)
        }
        return nuevo
    }

    fun sustituir(letra:String,lista:ArrayList<String>,avanze:Int):String
    {
        var indice = lista.indexOf(letra)
        var tam = lista.size
        if( indice + avanze >= tam)
            {return lista[(indice - tam) + avanze]}
        return lista[indice + avanze]
    }

    fun crearAlfabeto():ArrayList<String>
    {
        val list: ArrayList<String> = ArrayList()
        
        var caract: Char
        caract = ' '
        while (caract <= 'Ñ') {
            list.add(Character.toString(caract))
            ++caract
        }
        return list
    }

}