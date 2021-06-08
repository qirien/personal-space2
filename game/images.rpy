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

    image nullimage = Null()

    # TODO: replace with actual CGs
    image baby_cg:
        "images/cgs/chapter-baby.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 0.9 yalign 0.5
        linear 5.0 zoom 0.75

    image toddler_cg:
        "images/cgs/chapter-toddler.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 0.7 yalign 0.5
        linear 5.0 zoom 0.75       

    image child_cg:
        "images/cgs/chapter-child.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 0.7 yalign 0.5
        linear 5.0 zoom 0.75

    image tween_cg:
        "images/cgs/chapter-tween.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 0.9 yalign 0.5
        linear 5.0 zoom 0.75

    image yteen_cg:
        "images/cgs/chapter-teen.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 0.9 yalign 0.5
        linear 5.0 zoom 0.75

    image jellymother_cg:
        "images/cgs/jellymother.png"
        linear 15.0 zoom 0.5

    image harvest_cg:
        "images/cgs/hallowgiving.png"
        xalign 0.9 yalign 0.5 zoom 0.75
        linear 5.0 xalign 0.5 yalign 0.5
        linear 5.0 zoom 0.5

    image mountain_cg:
        "images/cgs/mountain.png"
        linear 10.0 zoom 0.5

    image ending1_cg:
        "images/cgs/ending1.png"
        xalign 0.0 yalign 0.4
        linear 5.0 xalign 0.8 yalign 0.5
        linear 5.0 zoom 0.5

    image ending2_cg:
        "images/cgs/ending2.png"
        xalign 0.8 yalign 0.3
        linear 5.0 xalign 0.0 yalign 0.2
        linear 5.0 zoom 0.5

    image ending3_cg:
        "images/cgs/ending3.png"
        xalign 0.0 yalign 0.2
        linear 5.0 zoom 0.75
        linear 5.0 zoom 0.5

    image ending4_cg:
        "images/cgs/ending4.png"
        xalign 0.0 yalign 0.5
        linear 5.0 xalign 1.0 yalign 0.5
        linear 5.0 zoom 0.5

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
        kid_expressions = ["angry", "annoyed", "blush", "cry", "concerned", "determined", "excited", "explaining", "flirting", "happy", "laugh", "nervous", "normal", "sad", "shifty", "surprised", "yell", "sleeping"]
        simple_expressions = ["happy", "normal", "sad", "angry", "excited"]
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("kid", expression_name), ConditionSwitch(
                "year <= BABY_MAX", "kid-sprites/baby_%s.png" % expression_name,
                "year <= TODDLER_MAX", "kid-sprites/toddler_%s.png" % expression_name,
                "year <= CHILD_MAX", "kid-sprites/kid_%s.png" % expression_name,
                "year <= TWEEN_MAX", "kid-sprites/tween_%s.png" % expression_name,
                "True", "kid-sprites/teen_%s.png" % expression_name)) 
        
        renpy.image(("side", "kid"), ConditionSwitch(
                "year <= BABY_MAX", "kid-sprites/side_baby.png",
                "year <= TODDLER_MAX", "kid-sprites/side_toddler.png",
                "year <= CHILD_MAX", "kid-sprites/side_kid.png",
                "year <= TWEEN_MAX", "kid-sprites/side_tween.png",
                "True", "kid-sprites/side_teen.png"))

        # Define images for bro (baby, toddler, young, tween, teen)
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("bro", expression_name), ConditionSwitch(
                "year <= 12", "bro-sprites/baby_%s.png" % expression_name,
                "(year-bro_birth_year) <= TODDLER_MAX", "bro-sprites/toddler_%s.png" % expression_name,
                "(year-bro_birth_year) <= CHILD_MAX", "bro-sprites/kid_%s.png" % expression_name,
                "True", "bro-sprites/tween_%s.png" % expression_name))

        renpy.image(("side", "bro"), ConditionSwitch(
                "year <= 12", "bro-sprites/side_baby.png", 
                "(year-bro_birth_year) <= TODDLER_MAX", "bro-sprites/side_toddler.png",
                "(year-bro_birth_year) <= CHILD_MAX", "bro-sprites/side_kid.png",
                "True", "bro-sprites/side_tween.png"))

        # Images for Oleg
        for expression_name in simple_expressions:
            renpy.image(("oleg", expression_name), ConditionSwitch(
                "year <= CHILD_MAX", "oleg-sprites/kid %s.png" % expression_name,
                "year <= TWEEN_MAX", "oleg-sprites/tween %s.png" % expression_name,
                "True", "oleg-sprites/teen %s.png" % expression_name))    
        renpy.image(("side", "oleg"), "oleg-sprites/side_kid.png")     
        # TODO: We need Oleg as a teen if his hair remains different; wait until Oleg teen sprites redone.           

        # Images for Travis
        for expression_name in simple_expressions:
            renpy.image(("travis", expression_name), ConditionSwitch(
                "year <= CHILD_MAX", "travis-sprites/kid %s.png" % expression_name,
                "year <= TWEEN_MAX", "travis-sprites/tween %s.png" % expression_name,
                "True", "travis-sprites/teen %s.png" % expression_name))       
        renpy.image(("side", "travis"), "travis-sprites/side_kid.png")                                         

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

    layeredimage family_photo:
        if True:
            "family_photo_bg"

        if ((year == 12) and family12_shaved_head):
            pos(480,80)
            "him bald"
        elif (year <= BABY_MAX and ((get_parenting_style == "neglectful") or (get_parenting_style() == "authoritarian"))):
            pos(450, 80)
            "him baby sad"
        elif (year <= BABY_MAX):
            pos(450, 80)            
            "him baby happy"
        elif (get_parenting_style() == "authoritative"):
            pos(450, 80)
            #align(0.3, 1.0)
            "him content"
        elif (get_parenting_style() == "authoritarian"):
            pos(450, 80)
            "him pout"
        elif (get_parenting_style() == "permissive"):
            pos(480, 80)
            "him normal"
        elif (year <= BABY_MAX):
            pos(480, 80)
            "him determined"
        # if neglectful, he is not in the picture at all, unless needed to hold a baby

        if has_strong_marriage():
            pos(600, 120)
            #align(0.7, 1.0)
            "her happy"
        elif (marriage_strength > 0):
            pos(600, 120)
            "her normal"
        else:
            pos(600, 120)
            "her determined coat"

        group kid:
            pos(320, 250)
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
            attribute baby:
                "nullimage"

        #align(0.6, 1.0)
        if ((bro_age >= 0) and (get_parenting_style() == "authoritative")):
            pos(680, 250)
            #align(0.6, 1.0)
            "bro happy"
        elif ((bro_age >= 0) and (get_parenting_style() == "authoritarian")):
            pos(680, 250)
            #align(0.6, 1.0)
            "bro concerned"
        elif ((bro_age >= 0) and (get_parenting_style() == "permissive")):
            pos(680, 250)
            #align(0.6, 1.0)
            "bro normal"
        elif ((bro_age >= 0) and (get_parenting_style() == "neglectful")):
            pos(680, 250)
            #align(0.6, 1.0)
            "bro sad"
        elif (bro_age >= 0):
            pos(680, 250)
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
