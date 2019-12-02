# Most images are automatically detected by Ren'Py if they are in the
# images/ directory. This is for special images we need to define
# manually, such as transforms, etc.

init -10:
    # BACKGROUNDS
    image farm_exterior flip = im.Flip("images/bg/farm_exterior.jpg", horizontal = True)
    image farm_interior flip = im.Flip("images/bg/farm_interior.jpg", horizontal = True)
    image irrigation flip = im.Flip("images/bg/irrigation.jpg", horizontal = True)
    image bro_bedroom = im.Flip("images/bg/kid_bedroom.jpg", horizontal = True)
    image stars_animated:
        "images/bg/stars.png"
        zoom 0.75
        linear 10.0 zoom 1.25

    # GUI
    image roundrect_darkgray = Frame("gui/roundrect-darkgray.png", 16, 16)
    image roundrect_lightgray = Frame("gui/roundrect-lightgray.png", 16, 16)
    image roundrect_medgreen = Frame("gui/roundrect-medgreen.png", 10, 10)
    image soil = Frame("gui/soil.png")

    image computer_pad = "gui/computer pad.png"
    image computer_pad_with_screen = LiveComposite(
        (1280, 720),
        (0,0), "images/bg/stars.png",
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

    # Temporary Sprites: TODO delete these
    image oleg normal = im.MatrixColor("images/sprites/boy sad.png", im.matrix.brightness(-0.5))
    image travis normal = "images/sprites/boy normal.png"

    # DYNAMIC SPRITES
    # Define images for kid (baby, toddler, young, tween, teen)
    init python:
        kid_expressions = ["angry", "annoyed", "cry", "concerned", "determined", "flirting", "happy", "laugh", "nervous", "normal", "sad", "shifty", "surprised", "yell"]
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        for expression_name in kid_expressions:
            renpy.image(("kid", expression_name), ConditionSwitch(
                "year <= BABY_MAX", "kid-sprites/baby %s.png" % expression_name,
                "year <= TODDLER_MAX", "kid-sprites/toddler %s.png" % expression_name,
                "year <= CHILD_MAX", "kid-sprites/kid %s.png" % expression_name,
                "year <= TWEEN_MAX", "kid-sprites/tween %s.png" % expression_name,
                "True", "kid-sprites/teen %s.png" % expression_name))

        # Define images for bro (baby, toddler, young, tween, teen)
        # For each expression, add a baby, toddler, young, tween, teen depending on current year
        # TODO: right now these are just kid's sprites. Change them to be unique.
        for expression_name in kid_expressions:
            renpy.image(("bro", expression_name), ConditionSwitch(
                "(year-bro_birth_year) <= BABY_MAX", "kid-sprites/baby %s.png" % expression_name,
                "(year-bro_birth_year) <= TODDLER_MAX", "kid-sprites/toddler %s.png" % expression_name,
                "(year-bro_birth_year) <= CHILD_MAX", "kid-sprites/kid %s.png" % expression_name,
                "(year-bro_birth_year) <= TWEEN_MAX", "kid-sprites/tween %s.png" % expression_name,
                "True", "kid-sprites/teen %s.png" % expression_name))

    # TODO: Add the family, with expressions depending on stats.
    # TODO: Have a different background for each year
    # TODO: Improve layout
    define photo_scale = 0.7
    image family_photo = Crop((306*photo_scale,22*photo_scale,675*photo_scale, 680*photo_scale), LiveComposite(
        (1280*photo_scale, 720*photo_scale),
        (0,0), im.FactorScale("images/bg/pond.jpg", photo_scale),
        (int(300*photo_scale), 80), im.FactorScale("images/sprites/her/her normal.png", photo_scale),
        (int(710*photo_scale), 50), im.FactorScale("images/sprites/him/him normal.png", photo_scale),
        (int(420*photo_scale), 150), im.FactorScale("kid-sprites/kid happy.png", photo_scale),
        (0,0), im.FactorScale("images/bg/polaroid.png", photo_scale)
        )
        )

    image ctc_blink:
           "gui/ctc.png"
           linear 0.5 alpha 1.0
           pause 0.25
           linear 0.5 alpha 0.0
           pause 0.25
           repeat

    python:
        # TODO: replace these with color images?
        #   {image=happy.png}
        def emoji_tag(tag, argument):
            if argument == "happy":
                emoji="😊"
            elif argument == "grin":
                emoji="😄"
            elif argument == "mad":
                emoji="😡"
            elif argument == "blush":
                emoji="😳"
            elif argument == "happycry":
                emoji="😂"
            elif argument == "surprised":
                emoji="😲"
            elif argument == "hearteyes":
                emoji="😍"
            elif argument == "scream":
                emoji="😱"
            elif argument == "sad":
                emoji="😞"
            elif argument == "cry":
                emoji="😢"
            elif argument == "worried":
                emoji="😟"
            elif argument == "shocked":
                emoji="😧"
            elif argument == "yum":
                emoji="😋"
            elif argument == "yuck":
                emoji="🤮"
            elif argument == "grimace":
                emoji="😬"
            elif argument == "heart":
                emoji="❤"
            elif argument == "celebrate":
                emoji="🎉"
            elif argument == "music":
                emoji="🎶"
            elif argument == "bugs":
                emoji="🐞"
            elif argument == "death":
                emoji="💀"
            elif argument == "strawberries":
                emoji="🍓"
            elif argument == "biohazard":
                emoji="☣"

            font_size = int(gui.text_size * 1.5)
            return [ (renpy.TEXT_TAG, "size={}".format(font_size)), (renpy.TEXT_TEXT, emoji), (renpy.TEXT_TAG, "/size") ]

        config.self_closing_custom_text_tags["emoji"] = emoji_tag
