require 'cesar.rb'
require 'reverse.rb'
require 'reverseG.rb'

class Gestor
    include Inesita::Injection

    attr_accessor :palabra
    attr_accessor :cesar
    attr_accessor :reverse
    attr_accessor :reverse_g

  
    def initialize
      @palabra = "gest"
      @cesar = Cesar.new
      @reverse = Reverse.new
      @reverse_g = ReverseG.new
    end

    def cifrar( pala )
        @cesar.palabra = pala
        @reverse.palabra = pala
        @reverse_g.palabra = pala

        @cesar.cifrar()
        @reverse.cifrar()
        @reverse_g.cifrar()

    end

    def cifradoSinActualizacion
        @cesar.cifrar()
        @reverse.cifrar()
        @reverse_g.cifrar()
    end
end


