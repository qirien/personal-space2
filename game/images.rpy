# Most images are automatically detected by Ren'Py if they are in the
# images/ directory. This is for special images we need to define
# manually, such as transforms, etc.

init -10:
    # BACKGROUNDS
    image farm_exterior flip = im.Flip("images/bg/farm_exterior.jpg", horizontal = True)
    image farm_interior flip = im.Flip("images/bg/farm_interior.jpg", horizontal = True)
    image irrigation flip = im.Flip("images/bg/irrigation.jpg", horizontal = True)
    image fields flip = im.Flip("images/bg/fields.jpg", horizontal = True)
    image bro_bedroom = im.Flip("images/bg/kid_bedroom.jpg", horizontal = True)
    image aurora_animated:
        "images/bg/aurora.jpg"
        xalign 1.0 yalign 1.0
        linear 10.0 xalign 0.0 yalign 0.0
        linear 10.0 zoom 0.67
    image stars_animated:
        "images/bg/stars.png"
        zoom 0.75
        linear 10.0 zoom 1.25
    image rain:
        "images/bg/rain1.png"
        0.1
        "images/bg/rain2.png"
        0.1
        "images/bg/rain3.png"
        0.1
        repeat

    # GUI
    image roundrect_darkgray = Frame("gui/roundrect-darkgray.png", 16, 16)
    image roundrect_lightgray = Frame("gui/roundrect-lightgray.png", 16, 16)
    image roundrect_medgreen = Frame("gui/roundrect-medgreen.png", 10, 10)
    image leaves_branches = Frame("gui/choice-button.png", 10, 10)
    image soil = Frame("gui/soil.png")

    image computer_pad = "gui/computer pad.png"
    image computer_pad_with_screen = Composite(
        (1280, 720),
        (0,0), "images/bg/stars.png",
        (0,0), "gui/computer pad.png"
        )

    # Special Sprites
    image baby = "kid-sprites/baby_normal.png"
    image toddler = "kid-sprites/toddler_normal.png"
    image child = "kid-sprites/kid_normal.png"
    image tween = "kid-sprites/tween_normal.png"
    image teen = "kid-sprites/teen_normal.png"
    image goat_flip = im.Flip("images/sprites/goat.png", horizontal = True)

    # Temporary Sprites: TODO delete these
    image oleg normal = im.MatrixColor("images/sprites/boy sad.png", im.matrix.brightness(-0.5))
    image travis normal = "images/sprites/boy normal.png"
    image baby_laugh = "kid-sprites/baby_laugh.png"
    image toddler_happy = "kid-sprites/toddler_happy.png"
    image toddler_shifty = "kid-sprites/toddler_shifty.png"
    image kid_happy = "kid-sprites/kid_happy.png"
    image tween_annoyed = "kid-sprites/tween_annoyed.png"
    image teen_flirting = "kid-sprites/teen_flirting.png"
    image teen_surprised = "kid-sprites/teen_surprised.png"    
    image bro_kid_normal = "bro-sprites/kid_normal.png"    

    # DYNAMIC SPRITES
    # Define images for kid (baby, toddler, young, tween, teen)
    init python:
        kid_expressions = ["angry", "annoyed", "cry", "concerned", "determined", "flirting", "happy", "laugh", "nervous", "normal", "sad", "shifty", "surprised", "yell"]
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("kid", expression_name), ConditionSwitch(
                "year <= BABY_MAX", "kid-sprites/baby_%s.png" % expression_name,
                "year <= TODDLER_MAX", "kid-sprites/toddler_%s.png" % expression_name,
                "year <= CHILD_MAX", "kid-sprites/kid_%s.png" % expression_name,
                "year <= TWEEN_MAX", "kid-sprites/tween_%s.png" % expression_name,
                "True", "kid-sprites/teen_%s.png" % expression_name)) 

        # Define images for bro (baby, toddler, young, tween, teen)
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("bro", expression_name), ConditionSwitch(
                "year <= 12", "bro-sprites/baby_%s.png" % expression_name,
                "(year-bro_birth_year) <= TODDLER_MAX", "bro-sprites/toddler_%s.png" % expression_name,
                "(year-bro_birth_year) <= CHILD_MAX", "bro-sprites/kid_%s.png" % expression_name,
                "True", "bro-sprites/tween_%s.png" % expression_name))

    define photo_scale_factor = 0.7

    # Background of the family photo
    image family_photo_bg = ConditionSwitch(
        "(year // 2) == 0", "images/bg/path.jpg",
        "(year // 2) == 1", "images/bg/fields.jpg",        
        "(year // 2) == 2", "images/bg/barn.jpg", 
        "(year // 2) == 3", "images/bg/pond.jpg", 
        "(year // 2) == 4", "images/bg/hospital.jpg",
        "(year // 2) == 5", "images/bg/farm_exterior.jpg",
        "(year // 2) == 6", "images/bg/plain.jpg",       
        "(year // 2) == 7", "images/bg/canyon.jpg",
        "(year // 2) == 8", "images/bg/community_center.jpg",
        "(year // 2) == 9", "images/bg/irrigation.jpg",
        "(year // 2) == 10", "images/bg/ocean.jpg",        
        "(year // 2) == 11", "images/bg/cave.jpg",
        "(year // 2) == 12", "images/bg/library.jpg",
        "(year // 2) == 13", "images/bg/ocean_sunset.jpg",
        "((year // 2) == 14) and miners_strong()", "images/bg/mine.jpg",
        "((year // 2) == 14) and mavericks_strong()", "images/bg/cave.jpg",
        "(year // 2) == 14", "images/bg/community_center.jpg",
        "True", "images/bg/restaurant.jpg"
    )

    # TODO: use relative positions when they are fixed
    layeredimage family_photo:
        if True:
            "family_photo_bg"

        if (get_parenting_style() == "authoritative"):
            pos(320, 80)
            #align(0.3, 1.0)
            "him content"
        elif (get_parenting_style() == "authoritarian"):
            pos(320, 80)
            #align(0.3, 1.0)
            "him pout"
        elif (get_parenting_style() == "permissive"):
            pos(350, 80)
            #align(0.3, 1.0)
            "him normal"
        elif (year <= BABY_MAX):
            pos(320, 80)
            "him determined"
        # if neglectful, he is not in the picture at all, unless needed to hold a baby

        if has_strong_marriage():
            pos(650, 150)
            #align(0.7, 1.0)
            "her happy"
        elif (marriage_strength > 0):
            pos(650, 150)
            "her normal"
        else:
            pos(650, 150)
            "her nervous coat"

        group kid:
            pos(400, 250)
            #align(0.45, 1.0)
            attribute ACI:
                "kid happy"
            attribute ACi:
                "kid normal"
            attribute AcI:
                "kid shifty"
            attribute Aci:
                "kid surprised"
            attribute aCI:
                "kid determined"
            attribute aCi:
                "kid concerned"
            attribute acI:
                "kid annoyed"
            attribute aci:
                "kid sad"

        #align(0.6, 1.0)
        if ((bro_age >= 0) and (get_parenting_style() == "authoritative")):
            pos(670, 300)
            #align(0.6, 1.0)
            "bro happy"
        elif ((bro_age >= 0) and (get_parenting_style() == "authoritarian")):
            pos(670, 300)
            #align(0.6, 1.0)
            "bro concerned"
        elif ((bro_age >= 0) and (get_parenting_style() == "permissive")):
            pos(670, 300)
            #align(0.6, 1.0)
            "bro normal"
        elif ((bro_age >= 0) and (get_parenting_style() == "inconsistent")):
            pos(670, 300)
            #align(0.6, 1.0)
            "bro sad"
        elif (bro_age >= 0):
            pos(670, 300)
            "bro determined"
        if True:
            "polaroid"

    image family_photo_small = LayeredImageProxy("family_photo", Transform(crop=(306,22,675,680), zoom=photo_scale_factor))

    image ctc_blink:
           "gui/ctc.png"
           linear 0.5 alpha 1.0
           pause 0.25
           linear 0.5 alpha 0.0
           pause 0.25
           repeat

    python:
        # Here is our custom text tag for emoji.  It converts {emoji=happy} into {image=happy.png}
        def emoji_tag(tag, argument):

            return [
                (renpy.TEXT_TAG, "image=gui/emoji/" + argument + ".png")
                ]

        config.self_closing_custom_text_tags["emoji"] = emoji_tag
