# Most images are automatically detected by Ren'Py if they are in the
# images/ directory. This is for special images we need to define
# manually, such as transforms, etc.

init -10:
    # BACKGROUNDS
    image farm_exterior flip = im.Flip("images/bg/farm_exterior.jpg", horizontal = True)
    image farm_interior flip = im.Flip("images/bg/farm_interior.jpg", horizontal = True)
    image stars_animated:
        "images/bg/stars.jpg"
        linear 10.0 zoom 0.5


    # GUI
    image roundrect_darkgray = Frame("gui/roundrect-darkgray.png", 10, 10)
    image roundrect_lightgray = Frame("gui/roundrect-lightgray.png", 10, 10)

    image computer_pad = "gui/computer pad.png"
    image computer_pad_with_screen = LiveComposite(
        (1280, 720),
        (0,0), "images/bg/stars.jpg",
        (0,0), "gui/computer pad.png"
        #(0,0), "gui/computer pad screen.png"
        )
    
    # TODO: add different background? custom bg?

    image ctc_blink:
           "gui/ctc.png"
           linear 0.75 alpha 1.0
           linear 0.75 alpha 0.0
           repeat
