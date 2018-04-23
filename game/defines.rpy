# Declare global static variables, images, characters, etc.
# DO NOT declare variables that will change or should be saved
# in saved games here! Those go in script.rpy
init -100:

    # Static layout variables
    define LEFT_COLUMN_WIDTH = 320
    define MIDDLE_COLUMN_WIDTH = 480
    define RIGHT_COLUMN_WIDTH = 320

    # Static indices that will never change
    define MAX_FARM_SIZE = 25

    define NAME_INDEX = 0
    define CALORIES_INDEX = 1
    define NUTRITION_INDEX = 2
    define VALUE_INDEX = 3
    define WORK_INDEX = 4
    define NITROGEN_INDEX = 5
    define ENABLED_INDEX = 6
    define PERENNIAL_INDEX = 7
    define MAXIMUM_INDEX = 8
    define DESCRIPTION_INDEX = 9

    define CROP_STATS_MAX = 10

    # Calorie data
    define CALORIES_BASE = 50
    define NUTRITION_BASE = 50
    define WORK_BASE = 60

    # GUI display sizes
    define CROP_ICON_SIZE = 50
    define CROP_LAYOUT_BAR_SIZE = CROP_ICON_SIZE + 8
    define CROP_LAYOUT_BAR_WIDTH = CROP_ICON_SIZE / 10

    # Static variables used for endings
    # TODO: Tweak these so all endings are possible.
    define ATTACHMENT_HIGH = 45
    define COMPETENCE_HIGH = 45
    define INDEPENDENCE_HIGH = 30

    define MAX_YEARS = 30

    # Variables persistent across all Metasepia games
    define mp = MultiPersistent("MetasepiaGames")

    ##
    # Music
    ##

    # Activity themes
    define audio.maintheme = "music/12-Found-Jeff Wahl_.ogg"
    define audio.parenting = "music/05-Before the Time Slips Away-Jeff Wahl_.ogg"
    define audio.community = "music/11-Wiseman's View-Ken Bonfield_.ogg"
    define audio.farming = "music/11-In My Life-Ray Montford_.ogg"
    define audio.computer = ["music/03-Gaja-Amfibia_.ogg"]

    # Emotional themes
    define audio.thoughtful = "music/13-The Summer that Never Quite Ended-Jeff Wahl_.ogg"
    define audio.tense = "music/03-Centerline-Ken Bonfield_.ogg"
    define audio.tender = "music/15-Surrender-Jeff Wahl_.ogg"
    define audio.sad = "music/01-May It Begin-Ray Montford_.ogg"
    define audio.happy = "music/11-Saturday Morning-Jeff Wahl_.ogg"
    define audio.sea = "music/17-The Sea-Jeff Wahl_.ogg"


    ##
    # Declare characters
    ##

    # TODO: Remove unused
    define narrator = Character(ctc="ctc_blink", ctc_position="nestled")

    define her = DynamicCharacter("her_name", color="#84b766", image="her", ctc="ctc_blink", ctc_position="nestled") #light mint green
    define him = DynamicCharacter("his_name", color="#bc1e0e", image="him", ctc="ctc_blink", ctc_position="nestled") #red
    define kid = DynamicCharacter("kid_name", color="#e361ef", image="kid", ctc="ctc_blink", ctc_position="nestled") #pinkish purple
    define bro = DynamicCharacter("bro_name", color="#4a9be0", image="kid", ctc="ctc_blink", ctc_position="nestled") #baby blue

    define naomi = Character("Sister Naomi Grayson", color="#bf98ff", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define pavel = Character("Mayor Pavel Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #dark gray
    define lily = Character("Dr. Lily Kealoha", color="#6763b5", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
    define sara = Character("Sara Hill-Andrevski", color="#e25057", image="sara", ctc="ctc_blink", ctc_position="nestled")  # salmon pink
    define thuc = Character("Thuc Nguyen", color="#a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
    define ilian = Character("Ilian Andrevski", color="#d2d099", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
    define oleg = Character("Oleg Hill-Andrevski", color="#42f4bf", image="oleg", ctc="ctc_blink", ctc_position="nestled") #mint green
    define brennan = Character("Brennan Callahan", color="#33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
    define pete = Character("Pete Jennings", color="#ee7755", image="pete", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define natalia = Character("Natalia Perón", color="#f3ca14", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
    define helen = Character("Helen Jennings", color="#77b8ef", image="helen", ctc="ctc_blink", ctc_position="nestled") #icy gray
    define travis = Character("Travis Jennings", color="#ee7755", image="trevor", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define julia = Character("Julia Nguyen", color="#e7b1cb", image="julia", ctc="ctc_blink", ctc_position="nestled") #icy blue
    define martin = Character("Martín Perón", color="#9b5b1d", image="martin", ctc="ctc_blink", ctc_position="nestled")  #dark red

    define miranda = Character("Miranda Nguyen", color="#7788fc", image="miranda", ctc="ctc_blink", ctc_position="nestled")
    define chaco = Character("Chaco", color="#ee670b", image="van", ctc="ctc_blink", ctc_position="nestled") #pumpkin orange
    define kevin = Character("Kevin", color="#3333cc", image="kevin", ctc="ctc_blink", ctc_position="nestled")#periwinkle blue
    define zaina = Character("Zaina", color="#ffcc00", image="zaina", ctc="ctc_blink", ctc_position="nestled") #mustard yellow
    define bandile = Character("Bandile", color="#d35400", image="bandile", ctc="ctc_blink", ctc_position="nestled") #tan brown


    define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")
    define computer = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")

    ##
    # Custom transitions, positions, etc.
    ##
    define fade = Fade(0.2, 0.2, 0.2)
    define irisout = CropMove(0.5, "irisout")
    define irisin = CropMove(0.5, "irisin")
    define topcenter = Position(xpos=0.5, ypos=0.0, yanchor=0.0)
    define midleft = Position(xpos=0.35, xanchor=0.5)
    define midright = Position(xpos=0.65, xanchor=0.5)
    define quarterleft = Position(xpos=0.22, xanchor=0.5)
    define quarterright = Position(xpos=0.78, xanchor=0.5)
    define farleft = Position(xpos=-0.30, xanchor=0)
    define farright = Position(xpos=1.0, xanchor=0)
    define sitting = Position(ypos=0.45, yanchor=0)
    define squatting = Position(ypos=0.25, yanchor=0)
    define standing = Position(ypos= 1.0, yanchor = 1.0)

    # Baby positions for being held
    define baby_ypos = 540
    define rightbaby = Position(xpos=1.0, xanchor=1.0, ypos=baby_ypos)
    define quarterrightbaby = Position(xpos=0.78, xanchor=0.5, ypos=baby_ypos)
    define midrightbaby = Position(xpos=0.65, xanchor=0.5, ypos=baby_ypos)
    define centerbaby = Position(xpos=0.5, xanchor=0.5, ypos=baby_ypos)
    define midleftbaby = Position(xpos=0.35, xanchor=0.5, ypos=baby_ypos)
    define quarterleftbaby = Position(xpos=0.22, xanchor=0.5, ypos=baby_ypos)
    define leftbaby = Position(xpos=0, xanchor=0.0, ypos=baby_ypos)

    # Kid positions for really short people
    define centerkid = Position(xpos = 0.5, xanchor = 0.5, ypos = 0.75)

    # Slide in from the right to the left, pause, then fade out. Used for monthly interscene screen
    transform slideinpausefade:
        xalign 1.25
        yalign 0.05
        linear 1.5 xalign 0.05
        pause 2.0
        linear 1.0 alpha 0.0

    # Highlight when moused over
    transform highlight_imagebutton:
        xanchor 0.5
        yanchor 0.5
        xalign 0.5
        yalign 0.5
        on hover:
            zoom 1.0
            alpha 1.0
        on idle:
            zoom 0.8
            alpha 0.8

    # Transform to randomly pace quickly back and forth
    transform pace_back_and_forth:
        choice:
            linear random_float() xalign 0.5
            pause 0.1
        choice:
            linear random_float() xalign 0.25
            pause 0.1
        choice:
            linear random_float() xalign 0.75
            pause 0.1
        choice:
            linear random_float() xalign random_float()
            pause 0.1
        repeat
