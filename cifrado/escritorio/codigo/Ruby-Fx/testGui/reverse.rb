class Reverse
    attr_accessor :palabra
    attr_accessor :resultado

    def initialize 
        @palabra = ""  
        @resultado = ""
      end 
    
    def precifrado( value )
    end

    def cifrar
        @resultado = @palabra.reverse
    end
end