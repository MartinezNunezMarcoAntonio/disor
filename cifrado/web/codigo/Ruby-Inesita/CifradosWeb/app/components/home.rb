class Home
  include Inesita::Component

  def render
    div.jumbotron.text_center.bg_light do
      
      component Counter, props: {header: 'Inserte Texto'}
      
    end
  end
end
