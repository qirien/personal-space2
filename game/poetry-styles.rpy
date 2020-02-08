##
# You can change the look and feel of the poetry buttons and boards here
##

style pp_vpgrid is vpgrid:
    spacing 5

style pp_text is text:
    color "#000000"

style pp_button:
    padding (5,5,8,8)
    idle_background Frame("gui/poetry/pp_idle.png", 5, 5)
    hover_background Frame("gui/poetry/pp_hover.png", 5, 5)

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

style pp_frame is frame:
    background gray_light

##
# Next follows variants for mobile devices
##

style pps_vpgrid is pp_vpgrid:
    spacing 10

style pps_text is pp_text
style pps_button is pp_button
style pps_button_text is pp_button_text:
    size 28

style pps_label is pp_label
style pps_label_text is pp_label_text
style pps_frame is pp_frame
