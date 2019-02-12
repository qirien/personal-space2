# Declare global static variables, images, characters, etc.
# DO NOT declare variables that will change or should be saved
# in saved games here! Those go in script.rpy
init -100:
    # Variables giving max age of stage in Talaam years
    define BABY_MAX = 3
    define TODDLER_MAX = 8
    define CHILD_MAX = 16
    define TWEEN_MAX = 22
    define YTEEN_MAX = 25

    # Static layout variables
    define LEFT_COLUMN_WIDTH = 320
    define MIDDLE_COLUMN_WIDTH = 480
    define RIGHT_COLUMN_WIDTH = 320

    define COMPUTER_SUB_HEIGHT = 400

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

    # Nutritional data
    define VITAMIN_A_CROPS = {"fallow":0, "corn":0, "potatoes":0, "wheat":0, "peppers":2, "tomatoes":1, "plums":1, "squash":9, "strawberries":0, "beans":0, "peanuts":0, "carrots":9, "turnips":0, "onions":0, "spinach":7, "broccoli":2, "goats":1, "honey":0}
    define VITAMIN_A_LOW = 15

    define VITAMIN_C_CROPS = {"fallow":0, "corn":1, "potatoes":6, "wheat":0, "peppers":9, "tomatoes":3, "plums":1, "squash":4, "strawberries":1, "beans":0, "peanuts":0, "carrots":1, "turnips":4, "onions":1, "spinach":3, "broccoli":9, "goats":0, "honey":0}
    define VITAMIN_C_LOW = 20

    define MAGNESIUM_CROPS = {"fallow":0, "corn":1, "potatoes":2, "wheat":0, "peppers":1, "tomatoes":1, "plums":1, "squash":2, "strawberries":0, "beans":6, "peanuts":5, "carrots":0, "turnips":0, "onions":0, "spinach":4, "broccoli":1, "goats":1, "honey":0}
    define MAGNESIUM_LOW = 10

    # Calorie data
    define CALORIES_BASE = 50
    define NUTRITION_BASE = 50
    define WORK_BASE = 60

    # Money data
    define ANNUAL_EXPENSES_BASE = 2500
    define KELLY_SALARY = 2000
    define CALORIES_TO_MONEY_MULTIPLIER = 14
    define MONEY_YEAR = 5
    define KID_WORK_YEAR = 6

    # GUI display sizes
    define CROP_ICON_SIZE = 50
    define CROP_LAYOUT_BAR_SIZE = CROP_ICON_SIZE + 8
    define CROP_LAYOUT_BAR_WIDTH = CROP_ICON_SIZE / 10

    # Static variables used for endings
    # TODO: Tweak these so all endings are possible.
    define ATTACHMENT_HIGH = 45 #Max is ~60
    define ATTACHMENT_MAX = 60
    define COMPETENCE_HIGH = 45 #Max is ~60
    define COMPETENCE_MAX = 60
    define INDEPENDENCE_HIGH = 20 #Max is ~32
    define INDEPENDENCE_MAX = 32

    define MAX_YEARS = 30

    # Variables persistent across all Metasepia games
    define mp = MultiPersistent("MetasepiaGames")

    ##
    # Music
    ##

    # Activity themes
    define audio.maintheme = "music/12-Found-Jeff Wahl_.ogg"
    #define audio.maintheme = ""
    define audio.parenting = "music/05-Before the Time Slips Away-Jeff Wahl_.ogg"
    define audio.community = "music/11-Wiseman's View-Ken Bonfield_.ogg"
    define audio.farming = "music/11-In My Life-Ray Montford_.ogg"
    define audio.computer = ["music/03-Gaja-Amfibia_.ogg", "music/08-Skyhawk Beach-Blue Wave Theory_.ogg"]

    # Emotional themes
    # Happy/excited
    define audio.exciting = "music/01-Colorado-Jeff Wahl_.ogg"
    define audio.upbeat = "music/01-Learning Patience-Jeff Wahl_.ogg"
    define audio.happy = "music/11-Saturday Morning-Jeff Wahl_.ogg"
    define audio.working = "music/04-Reservoir Ridge-Jeff Wahl_.ogg"

    # Tender/thoughtful
    define audio.tender = "music/15-Surrender-Jeff Wahl_.ogg"
    define audio.thoughtful = "music/13-The Summer that Never Quite Ended-Jeff Wahl_.ogg"

    # Sad/Mad
    define audio.sea = "music/17-The Sea-Jeff Wahl_.ogg"
    define audio.worried = "music/06-Nightfall-Ken Bonfield_.ogg"
    define audio.sad = "music/01-May It Begin-Ray Montford_.ogg"
    define audio.tense = "music/03-Centerline-Ken Bonfield_.ogg"


    ##
    # Declare characters
    ##

    # TODO: Remove unused
    define narrator = Character(ctc="ctc_blink", ctc_position="nestled")

    define her = DynamicCharacter("her_name", color="#84b766", image="her", ctc="ctc_blink", ctc_position="nestled") #light mint green
    define him = DynamicCharacter("his_name", color="#bc1e0e", image="him", ctc="ctc_blink", ctc_position="nestled") #red
    define kid = DynamicCharacter("kid_name", color="#ca67ac", image="kid", ctc="ctc_blink", ctc_position="nestled") #reddish purple
    define bro = DynamicCharacter("bro_name", color="#4a9be0", image="bro", ctc="ctc_blink", ctc_position="nestled") #baby blue

    define naomi = Character("Sister Naomi Grayson", color="#bf98ff", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define pavel = Character("Mayor Pavel Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #dark gray
    define lily = Character("Dr. Lily Kealoha", color="#6763b5", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
    define sara = Character("Sara Hill-Andrevski", color="#e25057", image="sara", ctc="ctc_blink", ctc_position="nestled")  # salmon pink
    define thuc = Character("Thuc Nguyen", color="#a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
    define ilian = Character("Ilian Andrevski", color="#d2d099", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
    define oleg = Character("Oleg Hill-Andrevski", color="#f3e6bc", image="oleg", ctc="ctc_blink", ctc_position="nestled") #khaki
    define brennan = Character("Brennan Callahan", color="#33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
    define pete = Character("Pete Jennings", color="#ee7755", image="pete", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define natalia = Character("Natalia Perón", color="#f3ca14", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
    define helen = Character("Helen Jennings", color="#77b8ef", image="helen", ctc="ctc_blink", ctc_position="nestled") #icy gray
    define travis = Character("Travis Jennings", color="#ee7755", image="travis", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
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
    transform midleft:
        xpos 0.35 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform midright:
        xpos 0.65 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform quarterleft:
        xpos 0.22 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform quarterright:
        xpos 0.78 xanchor 0.5 ypos 1.0 yanchor 1.0

    transform sitting:
        ypos 0.45 yanchor 0.0
    transform squatting:
        ypos 0.25 yanchor 0.0
    transform standing:
        ypos 1.0 yanchor 1.0
    transform jumping:
        yoffset -50
    transform jumpinghigh:
        linear 0.7 yoffset -150
        linear 0.7 yoffset 0


    # Baby positions for being held
    define baby_ypos = 540
    transform baby_pos:
        ypos baby_ypos yanchor 1.0
    transform centerbabybed:
        xpos 0.5, xanchor 0.5, ypos baby_ypos, yanchor 1.0
    transform standingbaby:
        ypos baby_ypos yanchor 1.0

    # Kid positions for really short people
    transform kid_pos:
        ypos 0.75 yanchor 1.0

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

    # A Transform to randomly pace quickly back and forth
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

    transform upside_down:
        linear 0.5 rotate 180

    transform up_and_down:
        linear 0.7 yoffset 100
        linear 0.7 yoffset -100

# TODO: remove this if we decide not to make people orange with Displayable Prefixes
#     image him happy orange = "orange:him happy"
#    image kid happy orange = "orange:kid happy"

# init -10 python:
#     def orangify(img):
#         return im.MatrixColor(img, im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.7))
#
#     config.displayable_prefix["orange"] = orangify

    define childs_mind = {
    "baby": "My world is small -- my family, blanket, and milk. So when something goes wrong it's like my whole world is collapsing! That's why I cry so much. \n\nI am learning so much every day, but it probably seems slow to you. I'm learning to focus my vision, touch and grab things, make sounds and decode their meaning, and who I can trust to take care of me. Soon I'll even move my whole body and understand a little of what you are saying, and make sounds that mean things. \n\nPlease be patient with me and show me a lot of love; I'm learning as fast as I can!",

    "toddler": "Now that I'm crawling and walking, my world is so much bigger! There's new foods, new faces, and new sensations every day. All this stuff is old to you, but to me it's all new -- the sound of a spoon on a pot, or the touch of sand, or the funny look on your face when I blow a raspberry. \n\nI want to do things myself but I am still clumsy and learning, so please help me explore safely and teach me even when it takes a long time for me to learn. I don't understand water, fire, electricity, or poison so help me be safe from these dangerous things while letting me explore as much as possible!",

    "preschooler": "I am learning how to do even cooler things! I can hop on one foot and name colors and sort toys! I have a great imagination and can benefit from playing with other kids and talking to lots of different people. I am still learning about politeness and what behavior is okay for different situations. \n\nI love rules because then I know what to do, but I get mad if other people don't follow them! Sometimes I think I can do things I can't really do yet, so help me improve my skills while still watching me. I am learning how to decide some things for myself, so please help me learn to make good choices by letting me decide some things!",

    "child": "I can do a lot of things that you can do! I can learn complex skills like doing math, playing sports, and making crafts. I am starting to think more about other people and what will happen in the future, but I'm not very good at it yet. Friends are important to me, but sometimes I don't get along with other people, so help me learn how to be a good friend and fix my mistakes. \n\nPlease support my growing independence by letting me do things for myself and giving me responsibilities!",

    "tween": "I am starting to think more abstractly. I am learning not just about what the world is, but why it is the way it is. When I was little, I thought I was the best person ever, but now I'm starting to see that I'm not. Please help me to recognize my strengths and deal with my weaknesses. \n\nWhat my friends think is becoming more important, but I still want to hear what you have to say. I might argue with you, but please be patient and love me and I'll think about what you say. My body is changing a lot now, too, and I'm starting to wonder what kind of person I want to be.",

    "yteen": "I might be rude to you and push you away when you try to show me affection like you did when I was a kid. I don't want you to tell me what to do. I will probably make some stupid choices and be hard on myself. Usually I don't need you to rescue me, but I need you to support and love me no matter what. \n\nI need to separate myself from you as I'm learning independence, so my words, appearance, music, and friends might seem really strange! \n\nPlease be interested in me and my world without trying to rule over it, and keep loving me and setting limits to protect me while I'm learning.",

    "teen": "I often have difficult questions, and I don't want easy answers. I am really thinking about these things and looking at a lot of different perspectives. If you listen to me, I will show you the same respect and hear what you have to say. If you are rude or try to tell me what to do, I will go somewhere else for answers. I want to find things out for myself. \n\nI'm learning about how to love and be a good friend and be on my own, and a lot of my emotions are still very strong. Please recognize my feelings and help me prepare to live on my own."
    }
