class Counter
  include Inesita::Component

  def cifrar(e)
    gestor.cifrar( e.target.value.to_s )
    render!
  end

  def saltos(e)
    gestor.cesar.salto = e.target.value.to_i
    gestor.cifradoSinActualizacion()
    render!
  end

  def grupos(e)
    gestor.reverse_g.grupo = e.target.value.to_i
    gestor.cifradoSinActualizacion()
    render!
  end

  ##############################COMPONENTS###############

  def render
    
    h3 "Cifrar"
    input onkeyup: method(:cifrar) 
    
    h3 "Cesar"
    select onchange: method(:saltos) do
      ary = (0..10).to_a
      ary.each do |i|
        option i.to_s
      end
    end
    input value: gestor.cesar.resultado
    
    h3 "Reverse"
    input value: gestor.reverse.resultado
    
    h3 "Reverse Group"
    select onchange: method(:grupos) do
      ary = (0..10).to_a
      ary.each do |i|
        option i.to_s
      end
    end
    input value: gestor.reverse_g.resultado


    
  end
end
