class Store
  include Inesita::Injection

  attr_accessor :counter
  attr_accessor :caden

  def init
    @counter = 0
    @caden = "Prueba"
  end

  def increase
    @counter += 1
  end

  def decrease
    @counter -= 1
  end
  def cambiar(arg1)
    @caden = "casa + " + arg1
  end
end
