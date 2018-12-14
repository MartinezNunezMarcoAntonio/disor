# require Inesita
require 'inesita'
require 'inesita-router'

# require main parts of application
require 'router'
require 'store'
require 'gestor'

require_tree './components'


class Application
  include Inesita::Component

  inject Router
  inject Store
  inject Gestor

  def render
    div.container do
      component NavBar
      component router
    end
  end
end


Inesita::Browser.ready? do
  Application.mount_to(Inesita::Browser.body)
end
