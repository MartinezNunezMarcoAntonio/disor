package com.example.demo.view

import com.example.demo.app.Gestor
import javafx.beans.property.SimpleIntegerProperty
import javafx.beans.property.SimpleObjectProperty
import javafx.beans.property.SimpleStringProperty
import javafx.collections.FXCollections
import javafx.scene.control.TextArea
import javafx.scene.control.TextField
import tornadofx.*

class MainView : View()
{

    val gestor = Gestor()

    var res1:TextArea by singleAssign()
    var res2:TextArea by singleAssign()
    var res3:TextArea by singleAssign()

    val selectedSalto = SimpleIntegerProperty(0)
    val selectedGrupo = SimpleIntegerProperty(0)

    override val root = vbox {
        vbox {
            var etiqueta = label("Cifrar")
            textfield("") {
                textProperty().addListener { obs, old, new ->
                    gestor.cifrar(new)
                    actualizar()
                }
            }
        }
        hbox {
            vbox {
                label("Cesar")
                combobox(selectedSalto, (0..10).toList( )){
                    setOnAction {
                        gestor.cesar.salto = value.toInt()
                        gestor.cifradoSinActualizacion()
                        actualizar()
                    }
                }
                res1 = textarea("")
            }


            vbox {
                label("Reverse")
                res2 = textarea("")
            }


            vbox {
                label("Reverse Group")
                combobox(selectedGrupo, (0..10).toList( )){
                    setOnAction {
                        gestor.reverse_g.grupo = value.toInt()
                        gestor.cifradoSinActualizacion()
                        actualizar()
                    }
                }
                res3 = textarea("")
            }

        }
    }

    fun actualizar(){
        res1.text = gestor.cesar.resultado
        res2.text = gestor.reverse.resultado
        res3.text = gestor.reverse_g.resultado
    }


}
