package com.example.vok

import com.vaadin.server.*
import com.github.mvysny.karibudsl.v8.*
import com.vaadin.navigator.View
import com.vaadin.ui.VerticalLayout
import com.vaadin.ui.themes.ValoTheme
import com.vaadin.navigator.ViewChangeListener.ViewChangeEvent


@AutoView("tab")
class MyWelcomeView: VerticalLayout(), View {
    init
    {
        val gestor = Gestor()
        
        var contenido = textField("Palabra a cifrar"){
            value = gestor.palabra
        }
        
        //##############RES1#####################
        var saltoCesar = comboBox<Int>("Salto Cifrado") {
            setItems((0..10).toList())
            isEmptySelectionAllowed = false
            value = 0
        }
        var resCesar = textField("Resultado Cesar"){
            value = gestor.cesar.resultado
        }
         //###############RES2####################
        var resReverse = textField("Resultado Reverse"){
            value = gestor.reverse.resultado
        }
         //###############RES3####################
        var agrupacionReverseG = comboBox<Int>("Agrupacion") {
            setItems((1..10).toList())
            isEmptySelectionAllowed = false
            value = 0
        }
        var resReverseGroup = textField("Resultado ReverseGroup"){
            value = gestor.reverse_g.resultado
        }

        //##############EVENTS#####################
        contenido.addValueChangeListener{
                var actu = contenido.value
                gestor.cifrar(actu)

                resCesar.value = gestor.cesar.resultado
                resReverse.value = gestor.reverse.resultado
                resReverseGroup.value = gestor.reverse_g.resultado
        }
        
        saltoCesar.addValueChangeListener {
            var actu = saltoCesar.value
            gestor.cesar.preCifrado(actu)
            gestor.cifradoSinActualizacion()
            resCesar.value = gestor.cesar.resultado
        } 

        agrupacionReverseG.addValueChangeListener {
             var actu = agrupacionReverseG.value
            gestor.reverse_g.preCifrado(actu)
            gestor.cifradoSinActualizacion()
            resReverseGroup.value = gestor.reverse_g.resultado
        }
    }
}