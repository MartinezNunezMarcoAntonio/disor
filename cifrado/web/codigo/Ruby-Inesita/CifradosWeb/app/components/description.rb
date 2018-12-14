class Description
  include Inesita::Component

  def render
    div.jumbotron.text_center.bg_light do
      p do
        text %{
          Contenido de Pestaña 2
        }
      end
    end
  end
end
