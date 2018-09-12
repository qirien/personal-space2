style pp_vpgrid is vpgrid:
    spacing 5

style pp_text is text:
    color "#000000"

style pp_button:
    idle_background Frame("gui/poetry/pp_idle.png", 5, 5)
    hover_background Frame("gui/poetry/pp_hover.png", 5, 5)
    padding (5,5,8,8)

style pp_button_text:
    size 18
    xalign 0.5
    idle_color "#000000"
    hover_color green_dark
    font "fonts/LiberationSerif.ttf"

style pp_label is label:
    xalign 0.5

style pp_label_text is label_text:
    color green_dark
    font "fonts/DejaVuSerif.ttf"
