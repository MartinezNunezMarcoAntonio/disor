class ReverseG
    attr_accessor :palabra
    attr_accessor :grupo
    attr_accessor :resultado

    def initialize 
        @palabra = ""  
        @grupo = 0  
        @resultado = ""
      end 
    
    def precifrado( value )
        @grupo = value
    end

    def cifrar
        @resultado = cifgroup(@palabra ,@grupo)
    end

    def cifgroup(txt ,group)
        @parte = ""
        @lis = []
        if group <2
            return txt
        end
        if group >= txt.length
            return txt.reverse
        end

        @numero = txt.length/group
        (0..@numero.to_i-1).to_a.each do |vak|
            @lis.push(txt[vak*group,group ])
        end
        @lis.each do |vak|
            @parte += vak.reverse
        end

        if txt.length % group != 0 
            return @parte+ txt[-(txt.length% group),txt.length]
        end
        return @parte

    end
end