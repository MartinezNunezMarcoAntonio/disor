require 'fox16'
include Fox
require_relative 'gestor'

class Main < FXMainWindow
  def initialize(app)
    gestor = Gestor.new()
    super(app, "Password generator", :width => 1300, :height => 768)
    

    vFrame1 = FXVerticalFrame.new(self)

    _label_cifrado = FXLabel.new(vFrame1, "Palabra a Cifrar")
    _txt_cifrado = FXTextField.new(vFrame1,200)

    vFrame2 = FXHorizontalFrame.new(self, :opts => LAYOUT_FILL)

    hFrameCesar = FXVerticalFrame.new(vFrame2, :opts => LAYOUT_FILL)
    _label_cesar = FXLabel.new(hFrameCesar, "Cifrado Cesar")
    _saltos = FXComboBox.new(hFrameCesar,10)
    (0..10).each do |itemString|
      _saltos.appendItem(itemString.to_s)
    end
    _resultado_cesar = FXText.new(hFrameCesar, :opts => LAYOUT_FILL | TEXT_READONLY | TEXT_WORDWRAP)


    hFrameReverse = FXVerticalFrame.new(vFrame2, :opts => LAYOUT_FILL)
    _label_reverse = FXLabel.new(hFrameReverse, "Cifrado Reverse")
    _resultado_reverse = FXText.new(hFrameReverse, :opts => LAYOUT_FILL | TEXT_READONLY | TEXT_WORDWRAP)


    hFrameReverseG = FXVerticalFrame.new(vFrame2, :opts => LAYOUT_FILL)
    _label_reverse_g = FXLabel.new(hFrameReverseG, "Cifrado Reverse Group")
    _grupo = FXComboBox.new(hFrameReverseG,10)
    (0..10).each do |itemString|
      _grupo.appendItem(itemString.to_s)
    end
    _resultado_reverse_g = FXText.new(hFrameReverseG, :opts => LAYOUT_FILL | TEXT_READONLY | TEXT_WORDWRAP)


    ######################EVENTS########################################
    _txt_cifrado.connect(SEL_KEYRELEASE) do
    gestor.cifrar( _txt_cifrado.to_s )
    _resultado_cesar.removeText(0, _resultado_cesar.length)
    _resultado_cesar.appendText( gestor.cesar.resultado )

    _resultado_reverse.removeText(0, _resultado_reverse.length)
    _resultado_reverse.appendText( gestor.reverse.resultado )

    _resultado_reverse_g.removeText(0, _resultado_reverse_g.length)
    _resultado_reverse_g.appendText( gestor.reverse_g.resultado )
    end

    _saltos.connect(SEL_COMMAND) do
      gestor.cesar.salto = _saltos.to_s.to_i
      gestor.cifradoSinActualizacion( )

      _resultado_cesar.removeText(0, _resultado_cesar.length)
      _resultado_cesar.appendText( gestor.cesar.resultado )

    end

    _grupo.connect(SEL_COMMAND) do
      gestor.reverse_g.grupo = _grupo.to_s.to_i
      gestor.cifradoSinActualizacion( )
  
      _resultado_reverse_g.removeText(0, _resultado_reverse_g.length)
      _resultado_reverse_g.appendText( gestor.reverse_g.resultado )
    end


  end


  def create
    super
    show(PLACEMENT_SCREEN)
  end
end

if __FILE__ == $0
  FXApp.new do |app|
    Main.new(app)
    app.create
    app.run
  end
end