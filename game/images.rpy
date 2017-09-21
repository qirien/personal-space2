# Most images are automatically detected by Ren'Py if they are in the
# images/ directory. This is for special images we need to define
# manually, such as transforms, etc.

init -10:
    # BACKGROUNDS
    image farm_exterior flip = im.Flip("bg/farm-exterior.jpg", horizontal = True)
    image farm_interior flip = im.Flip("bg/farm-interior.jpg", horizontal = True)    
    image stars_animated:
        "bg/stars.jpg"
        linear 10.0 zoom 0.5


    # GUI
    image tomato = "gui/cropicons/tomato.png"
    image beans = "gui/cropicons/beans.png"
    image carrot = "gui/cropicons/carrot.png"
    image goat = "gui/cropicons/goat.png"
    image potato = "gui/cropicons/potato.png"
    image spinach = "gui/cropicons/spinach.png"
    image squash = "gui/cropicons/squash.png"
    image ctc_blink:
           "gui/ctc.png"
           linear 0.75 alpha 1.0
           linear 0.75 alpha 0.0
           repeat 
           