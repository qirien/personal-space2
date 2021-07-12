# Declare global static variables, images, characters, etc.
# DO NOT declare variables that will change or should be saved
# in saved games here! Those go in script.rpy
init -100:
    # Variables giving max age of stage in Talaam years
    define BABY_MAX = 3
    define TODDLER_MAX = 8
    define CHILD_MAX = 15
    define TWEEN_MAX = 22
    define YTEEN_MAX = 25
    define TRANSITION_YEARS = [1, BABY_MAX+1, TODDLER_MAX+1, CHILD_MAX+1, TWEEN_MAX+1, YTEEN_MAX+1]

    # Talaam Events
    define MINERS_ARRIVE_YEAR = 11
    define MARTIN_DIES_YEAR = 11
    define PETE_LEAVES_YEAR = 14
    define NAOMI_DIES_YEAR = 15
    define LILY_DIES_YEAR = 20
    define PETE_LEAVES_CAVES_YEAR = 22
    define PAVEL_DIES_YEAR = 28

    # Static layout variables
    define LEFT_COLUMN_WIDTH = 300
    define MIDDLE_COLUMN_WIDTH = 480
    define RIGHT_COLUMN_WIDTH = 310
    define TOP_SECTION_HEIGHT = 520
    define COMPUTER_SUB_HEIGHT = 500

    # Farming parameters
    define FARM_SIZE_MAXIMUM = 25
    define FARM_SIZE_MINIMUM = 9
    define UNDERWORK_THRESHOLD = 5
    define USE_PESTS = False

    # Static indices that will never change
    define NAME_INDEX = 0
    define CALORIES_INDEX = 1
    define VITA_INDEX = 2
    define VITC_INDEX = 3
    define VITM_INDEX = 4
    define VALUE_INDEX = 5
    define WORK_INDEX = 6
    define NITROGEN_INDEX = 7
    define ENABLED_INDEX = 8
    define PERENNIAL_INDEX = 9
    define POLLINATED_INDEX = 10
    define MAXIMUM_INDEX = 11

    define CROP_STATS_MAX = 10
    define CROP_INFO_INDEX_NAMES = ["Name", "Calories", "Vitamin A", "Vitamin C", "Magnesium", "Value", "Work", "Nitrogen", "Enabled", "Perennial", "Pollinated", "Maximum"]
    define STAT_ICON_BASE = "gui/emoji/"

    # Nutritional data
    define VITAMINS_BASE = 20
    define VITAMIN_A_LOW = 20
    define VITAMIN_C_LOW = 20
    define MAGNESIUM_LOW = 10

    # Calorie data
    define CALORIES_BASE = 50
    define NUTRITION_BASE = 50
    define WORK_BASE = 60
    define WHEAT_COST = 200

    # Money data
    define KELLY_SALARY = 2000
    define CALORIES_TO_MONEY_MULTIPLIER = 14
    define MONEY_YEAR = 6
    define KID_WORK_YEAR = 7
    define NUTRITION_YEAR = 10

    # GUI display sizes
    define CROP_ICON_SIZE = 64
    define CROP_LAYOUT_BAR_SIZE = CROP_ICON_SIZE + 8
    define CROP_LAYOUT_BAR_WIDTH = CROP_ICON_SIZE / 10
    define CROP_STATUS_ICON_SIZE = 32

    # Static variables used for endings
    # TODO: Tweak these so all endings are possible.
    define ATTACHMENT_HIGH = 25 #Max is ~60
    define ATTACHMENT_MAX = 50
    define COMPETENCE_HIGH = 25 #Max is ~60
    define COMPETENCE_MAX = 50
    define INDEPENDENCE_HIGH = 17 #Max is ~35
    define INDEPENDENCE_MAX = 35
    define FACTION_HIGH = 10
    define FACTION_MAX = 20
    define MINERS_MAX = 20
    define COLONISTS_MAX = 20
    define MAVERICKS_MAX = 20
    define MINERS_HIGH = 12
    define COLONISTS_HIGH = 12
    define MAVERICKS_HIGH = 12

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
    define audio.computer = ["music/03-Gaja-Amfibia_.ogg", "music/08-Skyhawk Beach-Blue Wave Theory_.ogg", "music/08-One More Sleep-Ray Montford.ogg", "music/LonePeakMusic-OpenSore.ogg", "music/CoolRock.mp3"]

    # Specialty one-off songs
    define audio.teenmusic = "music/06-The Fate of Canned Corn-Glen Bledsoe.mp3"
    define audio.OPS1 = "music/LinesBuildWalls.ogg"
    define audio.saxophone = "music/10-Wish You Could Stay-Christos Anestopoulos.mp3"
    define audio.saxophone_solo = "<from 289>music/10-Wish You Could Stay-Christos Anestopoulos.mp3"
    define audio.videogame = "music/08-Electrospective Skuz-Ambient Teknology.ogg"

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
    define audio.sea = "music/17-The Sea-Jeff Wahl_.ogg" #ambient, has ocean waves in it
    define audio.worried = "music/06-Nightfall-Ken Bonfield_.ogg" #slow, melancholy
    define audio.problems = "music/05-Providence-Ray Montford_.ogg" #
    define audio.sad = "music/01-May It Begin-Ray Montford_.ogg" #plodding through desert carrying a heavy sack of burdens
    define audio.tense = "music/03-Centerline-Ken Bonfield_.ogg" #something terrible is happening and I'm moving through molasses

    define audio.investigation = "music/05-Libre Penseur-Justin St-Pierre.ogg"
    #investigation? http://download.magnatune.com/artists/albums/justinstpierre-insulaire?song=6


    ##
    # Declare characters
    ##
    define narrator = Character(ctc="ctc_blink", ctc_position="nestled-close")

    define her = Character("[her_name]", who_color=rose, image="her", ctc="ctc_blink", ctc_position="nestled-close") 
    define him = Character("[his_name]", who_color=red_med, image="him", ctc="ctc_blink", ctc_position="nestled-close") 
    define kid = Character("[kid_name]", who_color=magenta, image="kid", ctc="ctc_blink", ctc_position="nestled-close") 
    define bro = Character("[bro_name]", who_color=blue_med, image="bro", ctc="ctc_blink", ctc_position="nestled-close") 

    define naomi = Character("Sister Naomi", who_color=lavendar_gray, image="naomi", ctc="ctc_blink", ctc_position="nestled-close") 
    define pavel = Character("Mayor Pavel", who_color=tan_dark, image="pavel", ctc="ctc_blink", ctc_position="nestled-close") 
    define lily = Character("Dr. Lily", who_color=lavendar, image="lily", ctc="ctc_blink", ctc_position="nestled-close") 
    define sara = Character("Sara", who_color=rose_dark, image="sara", ctc="ctc_blink", ctc_position="nestled-close")
    define ilian = Character("Ilian", who_color=yellow_light, image="ilian", ctc="ctc_blink", ctc_position="nestled-close")  
    define oleg = Character("Oleg", who_color=blue_mako, image="oleg", ctc="ctc_blink", ctc_position="nestled-close") 
    define brennan = Character("Brennan", who_color=green_med, image="brennan", ctc="ctc_blink", ctc_position="nestled-close")  
    define pete = Character("Pete", who_color=brown_light, image="pete", ctc="ctc_blink", ctc_position="nestled-close")  
    define helen = Character("Helen", who_color=gray_med, image="helen", ctc="ctc_blink", ctc_position="nestled-close")
    define travis = Character("Travis", who_color=red_light, image="travis", ctc="ctc_blink", ctc_position="nestled-close")    
    define natalia = Character("Natalia", who_color=orange_you_glad, image="natalia", ctc="ctc_blink", ctc_position="nestled-close")  
    define martin = Character("Martín", who_color=dust_of_the_earth, image="martin", ctc="ctc_blink", ctc_position="nestled-close")
    define thuc = Character("Thuc", who_color=green_sage, image="thuc", ctc="ctc_blink", ctc_position="nestled-close")  
    define julia = Character("Julia", who_color=blue_ice, image="julia", ctc="ctc_blink", ctc_position="nestled-close") 

    define chaco = Character("Chaco", who_color=blue_dusty_ice, image="chaco", ctc="ctc_blink", ctc_position="nestled-close") 
    define kevin = Character("Kevin", who_color=yellow, image="kevin", ctc="ctc_blink", ctc_position="nestled-close")
    define zaina = Character("Zaina", who_color=yellow_gold, image="zaina", ctc="ctc_blink", ctc_position="nestled-close") #golden yellow
    define jellysquid = Character("Jellysquid", kind=nvl, who_color="#614bb5", image="jellysquid", ctc="ctc_blink", ctc_position="nestled-close", what_font="fonts/KidZone.ttf")  #purple

    define tutorial = Character("Tutorial", who_color="#ededed", ctc="ctc_blink", ctc_position="nestled-close")  #light gray
    define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled-close")

    ##
    # Custom transitions, transforms, positions, etc.
    ##
    define fade = Fade(0.2, 0.2, 0.2)
    define slowfade = Fade(0.5, 0.5, 0.5)
    define whitefade = Fade(0,0,0.5,color=(255,255,255,255))
    define irisout = CropMove(0.1, "irisout")
    define irisin = CropMove(0.1, "irisin")
    define irisoutslow = CropMove(0.5, "irisout")
    define irisinslow = CropMove(0.5, "irisin")
    define slowmove = MoveTransition(1.25)
    
    transform midleft:
        xpos 0.35 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform midright:
        xpos 0.65 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform quarterleft:
        xpos 0.22 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform quarterright:
        xpos 0.78 xanchor 0.5 ypos 1.0 yanchor 1.0
    transform centered:
        xpos 0.5 ypos 0.5 xanchor 0.5 yanchor 0.5

    transform tinyphoto:
        size (370,350)
    transform smallphoto:
        zoom 0.5
    transform threefourths_size:
        zoom 0.8

    transform tilted:
        choice:
            rotate 0
        choice:
            rotate -10
        choice:
            rotate 10
        choice:
            rotate 5
        choice:
            rotate -5
        choice:
            rotate -8
        choice:
            rotate 8
        choice:
            rotate 3
        choice:
            rotate -3

    transform sitting:
        ypos 0.45 yanchor 0.0
    transform squatting:
        ypos 0.30 yanchor 0.0
    transform standing:
        ypos 1.0 yanchor 1.0
    transform jumping:
        yoffset -50
    transform jumpinghigh:
        linear 0.7 yoffset -150
        linear 0.7 yoffset 0
    transform flip:
        xzoom -1.0

    transform creepright:
        linear 10.0 xoffset 200
    transform creepreset:
        linear 10.0 xoffset 0

    transform closeup_baby:
        parallel:
            ease 10.0 zoom 2.0
        parallel:
            yalign 0.5
            ease 10.0 yalign 0.8

    transform driftdown:
        ypos 0.0 yanchor 1.0
        linear 10.0 ypos 1.0 yanchor 0.0


    # Baby positions for being held
    define baby_ypos = 520
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
        easein 1.0 xalign 0.1
        pause 1.5
        linear 1.0 alpha 0.0

    # Highlight when moused over
    transform highlight_imagebutton():
        on hover:
            alpha 1.0
        on idle:
            alpha 0.6    

    transform delay_fadein:
        alpha 0.0
        pause 0.5
        easein 0.5 alpha 1.0

    # A thumbnail version of a full screen image
    transform thumbnail:
        #zoom 0.22 #doesn't work if full screen
        size (282,159)

    # Display something the size of our screen
    transform full_screen:
        size (1280,720)

    # Slide something in from the left, and slide it back to the left when it's hidden
    transform popside:
        # When it's shown, slide it right and fade it in.
        on show:
            xoffset -200.0  alpha 0.0 xzoom 0.1
            linear 0.1 xoffset 0.0 alpha 1.0 xzoom 1.0

        # When it's hidden, slide it left and fade it out.
        on hide:
            linear 0.1 xoffset -200.0 alpha 0.0 xzoom 0.1

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

    transform tiny_bounce:
        easein 0.4 yoffset -3
        easeout 0.4 yoffset 3
        repeat

    transform random_pulse_alpha:
        xpos random_int(0,500)
        ypos random_int(200,500)
        easein random_int(1,3) alpha 0.1
        easeout random_int(1,3) alpha 0.8        
        repeat
    
    transform bounce:     
        easein 0.1 xoffset 30
        easein 0.1 xoffset 0
        easein 0.1 xoffset 15
        easein 0.1 xoffset 0

    # Setup ACHIEVEMENTS
    python:
        show_which = ""
        # Has achievement name, description, and spot for screenshot/icon
        if (not persistent.achievements):
            persistent.achievements = {
            # Game Progression
                "Carbon Copy": {"desc":"Trained Daughter in Farming", "file":"ach00"},
                "Binary System": {"desc":"Father of Two", "file":"ach01"},
                "Patience Grandmaster": {"desc":"Kept your Cool", "file":"ach02"},
                "Talked the Talk": {"desc":"Answered Her Biology Questions", "file":"ach03"},
                "Over the Hill": {"desc":"Turned 40", "file":"ach04"},
            # Special weird things
                "Scurvy Dog": {"desc":"Got Scurvy", "file":"ach05"}, 
                "Rich Dad": {"desc":"Saved a LOT of credits!", "file":"ach06"}, 
                "Poor Dad": {"desc":"Deep in debt", "file":"ach07"}, 
                "Blackberry & Asparagus": {"desc":"Good Marriage Relationship", "file":"ach08"}, 
                "Potato Papa": {"desc":"Planted almost all Potatoes", "file":"ach09"}, 
                "Mutant Ninja Berries": {"desc":"Had Mutated Strawberries", "file":"ach10"}, 
                "Chez Dad": {"desc":"Ate Alien Escargot", "file":"ach11"}, 
                "Family Beeswax": {"desc":"Got Bees", "file":"ach12"}, 
                "Lousy Haircut": {"desc":"Shaved Head to get rid of Lice", "file":"ach13"},
                "Super Farmer": {"desc":"Unlocked all crops", "file":"ach14"},
            # Achievements for Endings
                "Bring Back My Baby": {"desc":"Ending #1", "file":"ending1"},
                "Proving Herself": {"desc":"Ending #2", "file":"ending2"},
                "Forever My Little Girl": {"desc":"Ending #3", "file":"ending3"},
                "The Stars are Bright": {"desc":"Ending #4", "file":"ending4"},            
            # Achievements for each parenting style
                "Big Boss": {"desc":"Authoritarian Parent", "file":"ach19"},
                "Firm Yet Fair": {"desc":"Authoritative Parent", "file":"ach20"},
                "Who Needs Rules?": {"desc":"Permissive Parent", "file":"ach21"},
                "Hands-Off Approach": {"desc":"Neglectful Parent", "file":"ach22"},
            # Achievements for each community favored
                "Xenophiliac": {"desc":"Friend to the Jellies", "file":"ach23"},
                "Don't Tread on Me": {"desc":"Friend to the Mavericks", "file":"ach24"},
                "It Takes This Village": {"desc":"Friend to the Colonists", "file":"ach25"},
                "Miner Details": {"desc":"Friend to the Miners", "file":"ach26"},            
            }

        #Ordered list to show them in a specific order
        achievement_list = [
        # Game Progression
        "Carbon Copy", # trained your daughter in farming
        "Binary System", # became a father of two
        "Patience Grandmaster", # kept your cool around a toddler
        "Talked the Talk", # answered kid_name's sex ed questions
        "Over the Hill", # turned 40
        # Special weird things
        "Scurvy Dog", # got scurvy
        "Rich Dad", # saved a lot of money
        "Poor Dad", # been in debt
        "Blackberry & Asparagus", # had a good relationship with her_name
        "Potato Papa", # planted almost all potatoes
        "Mutant Ninja Berries", # had mutated strawberries
        "Chez Dad", # ate escargot
        "Family Beeswax", # got bees
        "Lousy Haircut", # shaved your head to get rid of lice
        "Super Farmer",
        # Achievements for each ending
        "Bring Back My Baby", "Proving Herself", "Forever My Little Girl",  "The Stars are Bright", 
        # Achievements for each parenting style
        "Big Boss", "Firm Yet Fair", "Who Needs Rules?", "Hands-Off Approach",
        # Achievements for each community favored
        "Xenophiliac", "Don't Tread on Me", "It Takes This Village", "Miner Details",
        ]

        for title in achievement_list:
            achievement.register(title)


    # Setup parenting manual
    define childs_mind = {
        "general": "Researchers have identified four main parenting styles:\n\n{emoji=authoritarian} {b}Authoritarian{/b}: Focused on rules, obedience, and control.\n\n{emoji=authoritative} {b}Authoritative{/b}: Firm limits and expectations while also showing love and understanding.\n\n{emoji=permissive} {b}Permissive{/b}: Focused on pleasing the child and trying to make the child like them.\n\n{emoji=neglectful} {b}Neglectful{/b}: Parents who are uninvolved with their children.",

        "baby": "My world is small -- my family, blanket, and milk. So when something goes wrong it's like my whole world is collapsing! That's why I cry so much. \n\nI am learning so much every day, but it probably seems slow to you. I'm learning to focus my vision, touch and grab things, make sounds and decode their meaning, and who I can trust to take care of me. Soon I'll even move my whole body and understand a little of what you are saying, and make sounds that mean things. \n\nPlease be patient with me and show me a lot of love; I'm learning as fast as I can!",

        "toddler": "Now that I'm crawling and walking, my world is so much bigger! There's new foods, new faces, and new sensations every day. All this stuff is old to you, but to me it's all new -- the sound of a spoon on a pot, or the touch of sand, or the funny look on your face when I blow a raspberry. \n\nI want to do things myself but I am still clumsy and learning, so please help me explore safely and teach me even when it takes a long time for me to learn. I don't understand water, fire, electricity, or poison so help me be safe from these dangerous things while letting me explore as much as possible!",

        "preschooler": "I am learning how to do even cooler things! I can hop on one foot and name colors and sort toys! I have a great imagination and can benefit from playing with other kids and talking to lots of different people. I am still learning about politeness and what behavior is okay for different situations. \n\nI love rules because then I know what to do, but I get mad if other people don't follow them! Sometimes I think I can do things I can't really do yet, so help me improve my skills while still watching me. I am learning how to decide some things for myself, so please help me learn to make good choices by letting me decide some things!",

        "child": "I can do a lot of things that you can do! I can learn complex skills like doing math, playing sports, and making crafts. I am starting to think more about other people and what will happen in the future, but I'm not very good at it yet. Friends are important to me, but sometimes I don't get along with other people, so help me learn how to be a good friend and fix my mistakes. \n\nPlease support my growing independence by letting me do things for myself and giving me responsibilities!",

        "tween": "I am starting to think more abstractly. I am learning not just about what the world is, but why it is the way it is. When I was little, I thought I was the best person ever, but now I'm starting to see that I'm not. Please help me to recognize my strengths and deal with my weaknesses. \n\nWhat my friends think is becoming more important, but I still want to hear what you have to say. I might argue with you, but please be patient and love me and I'll think about what you say. My body is changing a lot now, too, and I'm starting to wonder what kind of person I want to be.",

        "yteen": "I might be rude to you and push you away sometimes, and I don't want you to tell me what to do. I will probably make some stupid choices and be hard on myself. Try not to solve my problems for me, but support and love me no matter what. \n\nI need to separate myself from you as I'm learning independence, so my words, appearance, music, and friends might seem really strange! \n\nPlease be interested in me and my world without trying to rule over it, and keep loving me and setting limits to protect me while I'm learning.",

        "teen": "I often have difficult questions, and I don't want easy answers. I am really thinking about these things and looking at a lot of different perspectives. If you listen to me, I will show you the same respect and hear what you have to say. If you are rude or try to tell me what to do, I will go somewhere else for answers. I want to find things out for myself. \n\nI'm learning about how to love and be a good friend and be on my own, and a lot of my emotions are still very strong. Please acknowledge my point of view and help me prepare to live on my own."
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
    "\"We need to provide opportunities for children to experience responsibility in direct relationship to the privileges they enjoy.\"\n\nJane Nelson, {i}Positive Discipline{/i}", #14
    "\"Our children’s well-being affects ours, and ours affects theirs.\"\n\nMyla and John Kabat-Zinn, {i}Everyday Blessings: The Inner Work of Mindful Parenting{/i}", #15
    "\"When a child is in the midst of strong emotions, he cannot listen to anyone. He cannot accept advice or consolation or constructive criticism. He wants us to understand him.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #16
    "\"The power of empathy and acceptance is immense, and deeply transformative both for the person receiving them and for the person according them.\"\n\nMyla and John Kabat-Zinn, {i}Everyday Blessings: The Inner Work of Mindful Parenting{/i}", #17
    "\"Perhaps parenting styles are less important than people have been led to believe. Perhaps human nature is more robust than most people give it credit for — perhaps children are designed to resist whatever their parents do to them.\"\n\nJudith Rich Harris, \"Parenting Styles Have Changed But Children Have Not\"", #18
    "\"The best solution to any problem lies within the skin of the person who rightfully owns the problem.\"\n\nFoster W. Cline, {i}Parenting with Love and Logic{/i}", #19
    "\"A limit must be stated in a manner that is deliberately calculated to minimize resentment, and to save self-esteem. The very process of limit-setting should convey authority, not insult.\"\n\nHaim G. Ginott, {i}Between Parent and Child{/i}", #20
    "\"All research indicates that the most significant influence on the life of a teenager comes from his or her parents.\"\n\nGary Chapman, {i}The Five Love Languages of Teenagers{/i}", #21
    "\"Where did we ever get the crazy idea that in order to make children do better, first we have to make them feel worse? Think of the last time you felt humiliated or treated unfairly. Did you feel like cooperating or doing better?\"\n\nJane Nelson, {i}Positive Discipline{/i}", #22
    "\"Excessive control usually involves punishment which is humiliating to children. Permissiveness is humiliating to adults. Positive discipline is based on mutual respect and cooperation.\"\n\nJane Nelson, {i}Positive Discipline{/i}", #23
    "\"Good character is not formed in a week or a month. It is created little by little, day by day. Protracted and patient effort is needed.\"\n\nHeraclitus", #24
    "\"Parents’ efforts to verbally argue the teenager into submission are in reality pushing the teenager toward rebellion.\"\n\nGary Chapman, {i}The Five Love Languages of Teenagers{/i}", #25
    "\"When our partner or child is upset, that is our opportunity to build a deep relationship.\" \n\n-- Dr. John Gottman", #26
    "\"That is what parenthood is, a relationship… The secret is to honor our relationship with our children in all of our interactions with them.\"\n\n Neufeld and Maté, {i}Hold On to Your Kids{/i}", #27
    "\"But kids don't stay with you if you do it right. It's the one job where, the better you are, the more surely you won't be needed in the long run.\"\n\nBarbara Kingsolver, {i}Pigs in Heaven{/i}", #28
    "\"The visions we offer our children shape the future. It matters what those visions are. Often they become self-fulfilling prophecies. Dreams are maps.\"\n\nCarl Sagan", #29
    "\"Raising a child is in many ways a long process of saying goodbye.\"\n\nTuber, Steven, ed., {i}Parenting : Contemporary Clinical Perspectives{/i}", #30

]
