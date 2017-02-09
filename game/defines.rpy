init -100:
# Declare global variables, images, characters, etc.
    
    define mp = MultiPersistent("MetasepiaGames")
    
    # Declare gameplay variables
    
    # PARENT
    
    # Positive indicates high expectations and reponsibilities for child; negative indicates indulgence and undiscpline
    $ demanding = 0
    $ total_demanding = 0
    # Positive indicates high emotional attachment and empathy; negative indicates aloofness and dismissiveness of child's feelings
    $ responsive = 0
    $ total_responsive = 0
    
    # CHILD
    
    # Amount of emotional intelligence, how loved and secure child feels
    $ attachment = 0
    # Reponsibility and ability to work hard, practical knowledge
    $ competence = 0
    # Confidence, autonomy
    $ independence = 0
    
    $ sex_ed_biology = False
    $ sex_ed_commitment = False
    $ sex_ed_babycreation = False
    $ sex_ed_goodfeeling = False
    $ sex_ed_birthcontrol = False
    
    
    # Declare characters used by this game .
    define narrator = Character(ctc="ctc_blink", ctc_position="nestled")
    
    define her = DynamicCharacter("her_name", color="#84b766", image="her", ctc="ctc_blink", ctc_position="nestled") #light mint green
    define him = DynamicCharacter("his_name", color="#bc1e0e", image="him", ctc="ctc_blink", ctc_position="nestled") #red
    define kid = DynamicCharacter("kid_name", color="#e361ef", image="kid", ctc="ctc_blink", ctc_position="nestled") #pinkish purple
    
    define naomi = Character("Sister Naomi Grayson", color="#bf98ff", image="naomi", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define pavel = Character("Mayor Pavel Grayson", color="#cccccc", image="pavel", ctc="ctc_blink", ctc_position="nestled")   #dark gray
    define lily = Character("Dr. Lily Kealoha", color="#6763b5", image="lily", ctc="ctc_blink", ctc_position="nestled")  #purple
    define sara = Character("Sara Hill-Andrevski", color="#e25057", image="sara", ctc="ctc_blink", ctc_position="nestled")  # salmon pink
    define thuc = Character("Thuc Nguyen", color="#a9ff22", image="thuc", ctc="ctc_blink", ctc_position="nestled")  #lime green
    define ilian = Character("Ilian Andrevski", color="#d2d099", image="ilian", ctc="ctc_blink", ctc_position="nestled") #tangerine
    define brennan = Character("Brennan Callahan", color="#33b533", image="brennan", ctc="ctc_blink", ctc_position="nestled")  #irish green
    define pete = Character("Pete Jennings", color="#ee7755", image="pete", ctc="ctc_blink", ctc_position="nestled")  #rusty brown
    define natalia = Character("Natalia Perón", color="#f3ca14", image="natalia", ctc="ctc_blink", ctc_position="nestled")  #yellow
    define helen = Character("Helen Jennings", color="#77b8ef", image="helen", ctc="ctc_blink", ctc_position="nestled") #icy gray
    define julia = Character("Julia Nguyen", color="#e7b1cb", image="julia", ctc="ctc_blink", ctc_position="nestled") #icy blue
    define martin = Character("Martín Perón", color="#9b5b1d", image="martin", ctc="ctc_blink", ctc_position="nestled")  #dark red
    
    define van = Character("Van Nguyen", color="#7788fc", image="van", ctc="ctc_blink", ctc_position="nestled")
    define ian = Character("Ian", color="#ee670b", image="van", ctc="ctc_blink", ctc_position="nestled") #pumpkin orange
    
    define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")
    
    # Default names
    $ his_name = "Jack"
    $ her_name = "Kelly"
    $ his_nickname = "dear"
    $ her_nickname = "lover"
    $ kid_name = "Terra"
    
    # Custom transitions, positions, etc.
    define fade = Fade(0.2, 0.2, 0.2)
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
    define rightbaby = Position(xpos=1.0, xanchor=1.0, ypos=430)
    define quarterrightbaby = Position(xpos=0.78, xanchor=0.5, ypos=430)
    define midrightbaby = Position(xpos=0.65, xanchor=0.5, ypos=430)    
    define centerbaby = Position(xpos=0.5, xanchor=0.5, ypos=430)
    define midleftbaby = Position(xpos=0.35, xanchor=0.5, ypos=430)  
    define quarterleftbaby = Position(xpos=0.22, xanchor=0.5, ypos=430)
    define leftbaby = Position(xpos=0, xanchor=0.0, ypos=430)
    
    # Kid positions for really short people
    define centerkid = Position(xpos = 0.5, xanchor = 0.5, ypos = 0.75)
    
    # Variables used in the game
    $ is_nude = False
    $ is_pregnant = False
    $ wearing_dress = False # TODO: do we still use these in OPS2?
    $ is_liason = False
    $ asked_only_medicine = False
    $ trade_with_luddites = False
    
    # FARM 
    # Work/crops
    $ farm_size = 16
    $ crops = []
    $ crop_index = 0
    # Dictionary containing the number of events seen for each crop 
    $ number_events_seen = {"corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "blueberries":0, "beans":0, "snow peas":0, "peanuts":0, "carrots":0, "beets":0, "turnips":0, "onions":0, "garlic":0, "cabbage":0, "spinach":0, "broccoli":0, "goats":0}
    # Tuple containing the crop name, calories, nutrition, fun, and work (scale of 0-10).  Also whether the crop is currently enabled or not.
    # TODO: add income
    # TODO: add limits to maximum amount allowed
    define crop_info = (["corn",         8, 4, 8, 7, False],    # Grains
                        ["potatoes",     8, 5, 7, 6, True],
                        ["wheat",        8, 6, 8, 10,False],
                        ["peppers",      2, 6, 5, 5, False],    # "Fruits"
                        ["tomatoes",     3, 5, 6, 6, True],
                        ["plums",        3, 3, 8, 7, False],
                        ["plums+",       3, 3, 8, 2, False],    # Perennials are easier after year 1
                        ["squash",       4, 5, 5, 4, True],
                        ["strawberries", 1, 3, 7, 6, False],
                        ["strawberries+",1, 3, 7, 6, False],
                        ["blueberries",  3, 3, 9, 9, False],
                        ["blueberries+", 3, 3, 9, 4, False],
                        ["beans",        6, 7, 2, 7, True],   # Legumes
                        ["snow peas",    3, 5, 2, 4, False],
                        ["peanuts",      7, 6, 5, 8, False],
                        ["carrots",      3, 5, 4, 4, True],   # Root Vegetables
                        ["beets",        3, 4, 4, 4, False],
                        ["turnips",      3, 5, 3, 4, False],
                        ["onions",       4, 3, 7, 4, False],
                        ["garlic",       3, 4, 7, 4, False],
                        ["cabbage",      2, 4, 4, 3, False],   # Leafy greens
                        ["spinach",      3, 6, 4, 4, True],
                        ["broccoli",     3, 5, 3, 3, False],
                        ["goats",       10, 7, 7, 5, True])   # Miscellaneous
    
    define CALORIES_INDEX = 1
    define NUTRITION_INDEX = 2
    define FUN_INDEX = 3
    define WORK_INDEX = 4
    define ENABLED_INDEX = 5
    
    $ total_calories = 0
    $ total_nutrition = 0
    $ total_fun = 0
    $ total_work = 0
    
    # Community. The higher the variable, the better your relationship with that group is.
    $ colonists = 0
    $ miners = 0
    $ luddites = 0
    $ jellies = 0