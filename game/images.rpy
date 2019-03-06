# Most images are automatically detected by Ren'Py if they are in the
# images/ directory. This is for special images we need to define
# manually, such as transforms, etc.

init -10:
    # BACKGROUNDS
    image farm_exterior flip = im.Flip("images/bg/farm_exterior.jpg", horizontal = True)
    image farm_interior flip = im.Flip("images/bg/farm_interior.jpg", horizontal = True)
    image stars_animated:
        "images/bg/stars.jpg"
        zoom 0.75
        linear 10.0 zoom 1.25

    # GUI
    image roundrect_darkgray = Frame("gui/roundrect-darkgray.png", 10, 10)
    image roundrect_lightgray = Frame("gui/roundrect-lightgray.png", 10, 10)
    image roundrect_medgreen = Frame("gui/roundrect-medgreen.png", 10, 10)
    image soil = Frame("gui/soil.jpg")

    image computer_pad = "gui/computer pad.png"
    image computer_pad_with_screen = LiveComposite(
        (1280, 720),
        (0,0), "images/bg/stars.jpg",
        (0,0), "gui/computer pad.png"
        #(0,0), "gui/computer pad screen.png"
        )

    # Special Sprites
    image baby = "kid-sprites/baby normal.png"
    image toddler = "kid-sprites/toddler normal.png"
    image child = "kid-sprites/kid normal.png"
    image tween = "kid-sprites/tween normal.png"
    image teen = "kid-sprites/teen normal.png"
    image goat_flip = im.Flip("images/sprites/goat.png", horizontal = True)

    # DYNAMIC SPRITES
    # Define images for kid (baby, toddler, young, tween, teen)
    init python:
        kid_expressions = ["angry", "annoyed", "cry", "concerned", "determined", "happy", "laugh", "nervous", "normal", "sad", "shifty", "surprised", "yell"]
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("kid", expression_name), ConditionSwitch(
                "year <= BABY_MAX", "kid-sprites/baby %s.png" % expression_name,
                "year <= TODDLER_MAX", "kid-sprites/toddler %s.png" % expression_name,
                "year <= CHILD_MAX", "kid-sprites/kid %s.png" % expression_name,
                "year <= TWEEN_MAX", "kid-sprites/tween %s.png" % expression_name,
                "True", "kid-sprites/teen %s.png" % expression_name))

    image ctc_blink:
           "gui/ctc.png"
           linear 0.5 alpha 1.0
           pause 0.25
           linear 0.5 alpha 0.0
           pause 0.25
           repeat
