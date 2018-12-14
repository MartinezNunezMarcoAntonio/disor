class NavBar
  include Inesita::Component

  def render
    nav.navbar.navbar_expand_lg.navbar_light.bg_light do
      span.navbar_brand do
        text 'CifradosWeb'
      end
      div.collapse.navbar_collapse do
        ul.nav.navbar_nav.mr_auto do
          li.nav_item class: class_names(active: router.current_url?(:home)) do
            a.nav_link href: router.url_for(:home) do
              text 'Cifrado'
            end
          end
          li.nav_item class: class_names(active: router.current_url?(:description)) do
            a.nav_link href: router.url_for(:description) do
              text 'Descripcion'
            end
          end
        end
      end
    end
  end
end
