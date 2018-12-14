class Cesar
    attr_accessor :palabra
    attr_accessor :salto
    attr_accessor :resultado
    
    ALFABETO = ((0...36).map { |i| i.to_s 36 }  + " ,/;'[]\=-!@#.$%^&*<>?:{}|".chars) * 10

    def initialize 
        @palabra = ""  
        @salto = 0  
        @resultado = ""
      end 
    
    def precifrado( value )
        @salto = value
    end

    def cifrar
        @resultado = cesar(@palabra ,@salto)
    end

    def cesar(msg,n)
        nuevo = msg.chars.map { |c| C(TRUE,c,n.to_i) }.join('')
        return nuevo
    end
    def C(s,x,n)
        return s ? ALFABETO[ (ALFABETO.index(x) + n) % ALFABETO.count] : ALFABETO[ (ALFABETO.index(x) - n) % ALFABETO.count]
    end
end