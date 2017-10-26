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
    
    image computer_pad = "gui/computer pad.png"
    image computer_pad_with_screen = LiveComposite( 
        (1280, 720),
        (0,0), "gui/computer pad.png",
        (0,0), "gui/computer pad screen.png")
    
    image ctc_blink:
           "gui/ctc.png"
           linear 0.75 alpha 1.0
           linear 0.75 alpha 0.0
           repeat 
           