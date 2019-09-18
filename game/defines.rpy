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

    # Talaam Events
    define MINERS_ARRIVE_YEAR = 11
    define MARTIN_DIES_YEAR = 11
    define PETE_LEAVES_YEAR = 14
    define NAOMI_DIES_YEAR = 15
    define PETE_LEAVES_CAVES_YEAR = 22
    define PAVEL_DIES_YEAR = 28

    # Static layout variables
    define LEFT_COLUMN_WIDTH = 310
    define MIDDLE_COLUMN_WIDTH = 480
    define RIGHT_COLUMN_WIDTH = 310
    define TOP_SECTION_HEIGHT = 520
    define COMPUTER_SUB_HEIGHT = 400

    # Farming parameters
    define FARM_SIZE_MAXIMUM = 25
    define FARM_SIZE_MINIMUM = 9
    define UNDERWORK_THRESHOLD = 5
    define USE_PESTS = False

    # Static indices that will never change
    define NAME_INDEX = 0
    define CALORIES_INDEX = 1
    define NUTRITION_INDEX = 2
    define VALUE_INDEX = 3
    define WORK_INDEX = 4
    define NITROGEN_INDEX = 5
    define ENABLED_INDEX = 6
    define PERENNIAL_INDEX = 7
    define POLLINATED_INDEX = 8
    define MAXIMUM_INDEX = 9

    define CROP_STATS_MAX = 10
    define STAT_ICONS = ["","❤","💊","¤","‍🔧","💩"]

    # Nutritional data
    define VITAMIN_A_CROPS = {"fallow":0, "corn":0, "potatoes":0, "wheat":0, "peppers":2, "tomatoes":1, "plums":1, "squash":9, "strawberries":0, "beans":0, "peanuts":0, "carrots":9, "turnips":0, "onions":0, "garlic":0, "spinach":7, "broccoli":2, "goats":1, "honey":0}
    define VITAMIN_A_LOW = 15

    define VITAMIN_C_CROPS = {"fallow":0, "corn":1, "potatoes":6, "wheat":0, "peppers":9, "tomatoes":3, "plums":1, "squash":4, "strawberries":1, "beans":0, "peanuts":0, "carrots":1, "turnips":4, "onions":1, "garlic":1, "spinach":3, "broccoli":9, "goats":0, "honey":0}
    define VITAMIN_C_LOW = 20

    define MAGNESIUM_CROPS = {"fallow":0, "corn":1, "potatoes":2, "wheat":0, "peppers":1, "tomatoes":1, "plums":1, "squash":2, "strawberries":0, "beans":6, "peanuts":5, "carrots":0, "turnips":0, "onions":0, "garlic":0, "spinach":4, "broccoli":1, "goats":1, "honey":0}
    define MAGNESIUM_LOW = 10

    # Calorie data
    define CALORIES_BASE = 50
    define NUTRITION_BASE = 50
    define WORK_BASE = 60

    # Money data
    define ANNUAL_EXPENSES_BASE = 2500
    define KELLY_SALARY = 2000
    define CALORIES_TO_MONEY_MULTIPLIER = 14
    define MONEY_YEAR = 6
    define KID_WORK_YEAR = 7

    # GUI display sizes
    define CROP_ICON_SIZE = 64
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
    define audio.problems = "music/05-Providence-Ray Montford_.ogg"
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

    define naomi = Character("Sister Naomi Grayson", color="#bf98ff", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #lavendar
    define pavel = Character("Mayor Pavel Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #gray
    define lily = Character("Dr. Lily Kealoha", color="#655283", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
    define sara = Character("Sara Hill-Andrevski", color="#ff6767", image="sara", ctc="ctc_blink", ctc_position="nestled")  # salmon pink
    define thuc = Character("Thuc Nguyen", color="#a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
    define ilian = Character("Ilian Andrevski", color="#d2d099", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
    define oleg = Character("Oleg Hill-Andrevski", color="#d8a687", image="oleg", ctc="ctc_blink", ctc_position="nestled") #sandstone
    define brennan = Character("Brennan Callahan", color="#33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
    define pete = Character("Pete Jennings", color="#ee7755", image="pete", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define natalia = Character("Natalia Perón", color="#f3ca14", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
    define helen = Character("Helen Jennings", color="#77b8ef", image="helen", ctc="ctc_blink", ctc_position="nestled") #icy gray
    define travis = Character("Travis Jennings", color="#ee7755", image="travis", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define julia = Character("Julia Nguyen", color="#e7b1cb", image="julia", ctc="ctc_blink", ctc_position="nestled") #icy blue
    define martin = Character("Martín Perón", color="#9b5b1d", image="martin", ctc="ctc_blink", ctc_position="nestled")  #dark red

    define chaco = Character("Chaco", color="#ee670b", image="van", ctc="ctc_blink", ctc_position="nestled") #pumpkin orange
    define kevin = Character("Kevin", color="#324cc5", image="kevin", ctc="ctc_blink", ctc_position="nestled")#dark blue
    define zaina = Character("Zaina", color="#ffcc00", image="zaina", ctc="ctc_blink", ctc_position="nestled") #golden yellow
    define bandile = Character("Bandile", color="#d35400", image="bandile", ctc="ctc_blink", ctc_position="nestled") #tan brown


    define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")

    ##
    # Custom transitions, positions, etc.
    ##
    define fade = Fade(0.2, 0.2, 0.2)
    define irisout = CropMove(0.5, "irisout")
    define irisin = CropMove(0.5, "irisin")
    define slowmove = MoveTransition(1.25)
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

    transform creepright:
        linear 10.0 xoffset 200
    transform creepreset:
        linear 10.0 xoffset 0


    # Baby positions for being held
    define baby_ypos = 540
    transform babybackpack_pos:
        ypos baby_ypos-180 xoffset -80 yanchor 1.0
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
        linear 0.7 yoffset 0

# TODO: remove this if we decide not to make people orange with Displayable Prefixes
#     image him happy orange = "orange:him happy"
#    image kid happy orange = "orange:kid happy"

# init -10 python:
#     def orangify(img):
#         return im.MatrixColor(img, im.matrix.desaturate() * im.matrix.tint(1.0, 1.0, 0.7))
#
#     config.displayable_prefix["orange"] = orangify

    # Setup ACHIEVEMENTS
    python:
        # TODO: implement unlocking by calling achievement.grant(name)
        achievement_list = [
        # Achievements for each ending
        "Bring Back My Baby", "Mistakes to Call My Own", "Proving Herself", "Down to Earth", "Forever My Little Girl", "Extraterrestrial Life", "The Stars are Right", "The Future is Bright",
        # Achievements for each parenting style
        "Big Boss", "Firm Yet Fair", "Who Needs Rules?", "Father Failure",
        # Achievements for each community favored
        "Xenophiliac", "Don't Tread on Me", "Law & Order", "What's Yours is Mine",
        # Game Progression
        "Binary System", # became a father of two
        "Carbon Copy", # trained your daughter in farming
        "Patience Grandmaster", # kept your cool around a toddler
        "Talked the Talk", # answered kid_name's sex ed questions
        "Over the Hill", # turned 40
        # Special weird things
        "Scurvy Dog", # got scurvy
        "Rich Dad", # saved a lot of money
        "Poor Dad", # been in debt
        "Better Half", # had a good relationship with her_name
        "Potato Diet", # planted almost all potatoes
        "Mutant Ninja Berries", # had mutated strawberries
        "Chez Dad", # ate escargot
        "Family Beeswax" # got bees
        ]

        for title in achievement_list:
            achievement.register(title)


    # Setup parenting manual
    define childs_mind = {
    "baby": "My world is small -- my family, blanket, and milk. So when something goes wrong it's like my whole world is collapsing! That's why I cry so much. \n\nI am learning so much every day, but it probably seems slow to you. I'm learning to focus my vision, touch and grab things, make sounds and decode their meaning, and who I can trust to take care of me. Soon I'll even move my whole body and understand a little of what you are saying, and make sounds that mean things. \n\nPlease be patient with me and show me a lot of love; I'm learning as fast as I can!",

    "toddler": "Now that I'm crawling and walking, my world is so much bigger! There's new foods, new faces, and new sensations every day. All this stuff is old to you, but to me it's all new -- the sound of a spoon on a pot, or the touch of sand, or the funny look on your face when I blow a raspberry. \n\nI want to do things myself but I am still clumsy and learning, so please help me explore safely and teach me even when it takes a long time for me to learn. I don't understand water, fire, electricity, or poison so help me be safe from these dangerous things while letting me explore as much as possible!",

    "preschooler": "I am learning how to do even cooler things! I can hop on one foot and name colors and sort toys! I have a great imagination and can benefit from playing with other kids and talking to lots of different people. I am still learning about politeness and what behavior is okay for different situations. \n\nI love rules because then I know what to do, but I get mad if other people don't follow them! Sometimes I think I can do things I can't really do yet, so help me improve my skills while still watching me. I am learning how to decide some things for myself, so please help me learn to make good choices by letting me decide some things!",

    "child": "I can do a lot of things that you can do! I can learn complex skills like doing math, playing sports, and making crafts. I am starting to think more about other people and what will happen in the future, but I'm not very good at it yet. Friends are important to me, but sometimes I don't get along with other people, so help me learn how to be a good friend and fix my mistakes. \n\nPlease support my growing independence by letting me do things for myself and giving me responsibilities!",

    "tween": "I am starting to think more abstractly. I am learning not just about what the world is, but why it is the way it is. When I was little, I thought I was the best person ever, but now I'm starting to see that I'm not. Please help me to recognize my strengths and deal with my weaknesses. \n\nWhat my friends think is becoming more important, but I still want to hear what you have to say. I might argue with you, but please be patient and love me and I'll think about what you say. My body is changing a lot now, too, and I'm starting to wonder what kind of person I want to be.",

    "yteen": "I might be rude to you and push you away when you try to show me affection like you did when I was a kid. I don't want you to tell me what to do. I will probably make some stupid choices and be hard on myself. Usually I don't need you to rescue me, but I need you to support and love me no matter what. \n\nI need to separate myself from you as I'm learning independence, so my words, appearance, music, and friends might seem really strange! \n\nPlease be interested in me and my world without trying to rule over it, and keep loving me and setting limits to protect me while I'm learning.",

    "teen": "I often have difficult questions, and I don't want easy answers. I am really thinking about these things and looking at a lot of different perspectives. If you listen to me, I will show you the same respect and hear what you have to say. If you are rude or try to tell me what to do, I will go somewhere else for answers. I want to find things out for myself. \n\nI'm learning about how to love and be a good friend and be on my own, and a lot of my emotions are still very strong. Please recognize my feelings and help me prepare to live on my own."
    }

# Quotes to show at the end of each year.
define parenting_quotes = [
    "", #0 not needed
    "\"Love can change a person the way a parent can change a baby- awkwardly, and often with a great deal of mess.\"\n\nLemony Snicket, {i}Horseradish{/i}", #1
    "\"It is essential that a child's life not be ruled by the adult's need for efficiency. Efficiency is the enemy of infancy.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #2
    "\"Effective parenting centers around love: love that is not permissive, love that doesn’t tolerate disrespect, but also love that is powerful enough to allow kids to make mistakes and permit them to live with the consequences of those mistakes.\"\n\nFoster W. Cline, {i}Parenting with Love and Logic{/i}", #3
    "\"It is easier to build strong children than to repair broken men.\"\n\n -- Frederick Douglass", #4
    "\"We experience so much more joy, as well as positive results, when we remember to make sure that the message of love gets through.\"\n\nJane Nelson, {i}Positive Discipline{/i}", #5
    "\"When a parent is not sure of what to do, it is best to do nothing but think and clarify his own attitudes.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #6
    "\"Children are educated by what the grown-up is and not by his talk.\"\n\n -- Carl Jung", #7
    "\"At the end of the day, the most overwhelming key to a child's success is the positive involvement of parents.\"\n\nJane D. Hull", #8
    "\"Research has shown that the most effective way to reduce problem behavior in children is to strengthen desirable behavior through positive reinforcement rather than trying to weaken undesirable behavior using aversive or negative processes.\"\n\nS.W. Bijou, {i}The International Encyclopedia of Education{/i}", #9
    "\"Love is expressed in how we pass the bread, or how we say good morning, and not just in the big trip to Disney World.\"\n\nMyla and John Kabat-Zinn, {i}Everyday Blessings: The Inner Work of Mindful Parenting{/i}", #10
    "\"...communication with children is based on respect and on skill. It requires (a) that messages preserve the child's as well as the parent's self-respect; (b) that statements of understanding precede statements of advice and instruction.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #11
    "\"The right age to inform a child about sexual matters is when he asks questions….Our explanation should be factual but it does not need to give full account.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #12
    "\"Misbehavior of children must be recognized as a need to teach appropriate behavior, not an excuse to punish. Punishment is a terrible teacher. It only teaches children how not to behave.\"\n\nGlenn Latham, {i}The Power of Positive Parenting{/i}", #13
    "\"We often rob children of opportunities to feel belonging and significance in meaningful ways through responsible contributions and then complain and criticize them for not developing responsibility. We need to provide opportunities for children to experience responsibility in direct relationship to the privileges they enjoy.\"\n\nJane Nelson, {i}Positive Discipline{/i}", #14
    "\"Our children’s well-being affects ours, and ours affects theirs.\"\n\nMyla and John Kabat-Zinn, {i}Everyday Blessings: The Inner Work of Mindful Parenting{/i}", #15
    "\"When a child is in the midst of strong emotions, he cannot listen to anyone. He cannot accept advice or consolation or constructive criticism. He wants us to understand him.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #16
    "\"The power of empathy and acceptance is immense, and deeply transformative both for the person receiving them and for the person according them.\"\n\nMyla and John Kabat-Zinn, {i}Everyday Blessings: The Inner Work of Mindful Parenting{/i}", #17
    "\"Perhaps parenting styles are less important than people have been led to believe. Perhaps human nature is more robust than most people give it credit for — perhaps children are designed to resist whatever their parents do to them.\"\n\nJudith Rich Harris, \"Parenting Styles Have Changed But Children Have Not\"", #18
    "\"The best solution to any problem lies within the skin of the person who rightfully owns the problem.\"\n\nFoster W. Cline, {i}Parenting with Love and Logic{/i}", #19
    "\"A limit should be so stated that it tells the child clearly (a) what constitutes unacceptable conduct; (b) what substitute will be accepted…. A limit must be stated in a manner that is deliberately calculated to minimize resentment , and to save self-esteem. The very process of limit-setting should convey authority, not insult.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #20
    "\"All research indicates that the most significant influence on the life of a teenager comes from his or her parents.\"\n\nGary Chapman, {i}The Five Love Languages of Teenagers{/i}", #21
    "\"Where did we ever get the crazy idea that in order to make children do better, first we have to make them feel worse? Think of the last time you felt humiliated or treated unfairly. Did you feel like cooperating or doing better?\"\n\nJane Nelson, {i}Positive Discipline{/i}", #22
    "\"Excessive control usually involves punishment which is humiliating to children. Permissiveness is humiliating to adults. Positive discipline is based on mutual respect and cooperation. Positive discipline incorporates firmness with dignity and respect.\"\n\nJane Nelson, {i}Positive Discipline{/i}", #23
    "\"Good character is not formed in a week or a month. It is created little by little, day by day. Protracted and patient effort is needed.\"\n\n --Heraclitus", #24
    "\"Parents’ efforts to verbally argue the teenager into submission are in reality pushing the teenager toward rebellion.\"\n\nGary Chapman, {i}The Five Love Languages of Teenagers{/i}", #25
    "\"When children and adolescents who are in need of differentiating themselves from their caregivers engender hate in those caregivers, it is because they simultaneously need to be separate and need to stay attached. They accomplish this by creating a situation in which the caregiver separates from them (because of the \'hatred\'), but they themselves stay attached (by not directly expressing or even consciously feeling the hatred).\" \n\nTuber, Steven, ed., {i}Parenting : Contemporary Clinical Perspectives{/i}", #26
    "\"There is a cognitive bias that makes people overestimate their own importance and their own ability to influence how things turn out - not just in child-rearing but in everything they do.\"\n\n -- Judith R. Harris", #27
    "\"But kids don't stay with you if you do it right. It's the one job where, the better you are, the more surely you won't be needed in the long run.\"\n\nBarbara Kingsolver, {i}Pigs in Heaven{/i}", #28
    "\"When the child internalizes a secure internal working model of self in relation to caregivers, a remarkable thing can occur— the child can dare to turn their back on caregivers and walk away from them\"\n\nTuber, Steven, ed., {i}Parenting : Contemporary Clinical Perspectives{/i}", #29
    "\"Raising a child is in many ways is a long process of saying goodbye.\"\n\nTuber, Steven, ed., {i}Parenting : Contemporary Clinical Perspectives{/i}", #30

]
