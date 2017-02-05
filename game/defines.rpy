init -100:
# Declare global variables, images, characters, etc.
    
    define mp = MultiPersistent("MetasepiaGames")
    
    # Declare gameplay variables
    
    # PARENT
    
    # Positive indicates high expectations and reponsibilities for child; negative indicates indulgence and undiscpline
    define demanding = 0
    define total_demanding = 0
    # Positive indicates high emotional attachment and empathy; negative indicates aloofness and dismissiveness of child's feelings
    define responsive = 0
    define total_responsive = 0
    
    # CHILD
    
    # Amount of emotional intelligence, how loved and secure child feels
    define attachment = 0
    # Reponsibility and ability to work hard, practical knowledge
    define competence = 0
    # Confidence, autonomy
    define independence = 0
    
    define sex_ed_biology = False
    define sex_ed_commitment = False
    define sex_ed_babycreation = False
    define sex_ed_goodfeeling = False
    define sex_ed_birthcontrol = False
    
    
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
    
    
    define tutorial = Character("Tutorial", color="#ededed", ctc="ctc_blink", ctc_position="nestled")  #light gray
    define note = Character("note", kind=nvl, ctc="ctc_blink", ctc_position="nestled")
    
    # Default names
    define his_name = "Jack"
    define her_name = "Kelly"
    define his_nickname = "dear"
    define her_nickname = "lover"
    define kid_name = "Terra"
    
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
    define is_nude = False
    define is_pregnant = False
    define wearing_dress = False # TODO: do we still use these in OPS2?
    define is_liason = False
    define asked_only_medicine = False
    define trade_with_luddites = False
    
    # Work/crops
    define crops = []
    # Dictionary containing the number of events seen for each crop 
    define number_events_seen = {"corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "blueberries":0, "beans":0, "snow peas":0, "peanuts":0, "carrots":0, "beets":0, "turnips":0, "onions":0, "garlic":0, "cabbage":0, "spinach":0, "broccoli":0, "goats":0}
    # Tuple containing the crop name, calories, nutrition, fun, and work (scale of 0-10)
    define crop_info = (["corn",         8, 4, 8, 7],    # Grains
                        ["potatoes",     8, 5, 7, 6],
                        ["wheat",        8, 6, 8, 10],
                        ["peppers",      2, 6, 5, 5],    # "Fruits"
                        ["tomatoes",     3, 5, 6, 6],
                        ["plums",        3, 3, 8, 7],
                        ["plums2",       3, 3, 8, 2],    # Perennials are easier after year 1
                        ["squash",       4, 5, 5, 4],
                        ["strawberries", 1, 3, 7, 6],
                        ["strawberries2",1, 3, 7, 6],
                        ["blueberries",  3, 3, 9, 9],
                        ["blueberries2", 3, 3, 9, 4],
                        ["beans",        6, 7, 2, 7],   # Legumes
                        ["snow peas",    3, 5, 2, 4],
                        ["peanuts",      7, 6, 5, 8],
                        ["carrots",      3, 5, 4, 4],   # Root Vegetables
                        ["beets",        3, 4, 4, 4],
                        ["turnips",      3, 5, 3, 4],
                        ["onions",       4, 3, 7, 4],
                        ["garlic",       3, 4, 7, 4],
                        ["cabbage",      2, 4, 4, 3],   # Leafy greens
                        ["spinach",      3, 6, 4, 4],
                        ["broccoli",     3, 5, 3, 3],
                        ["goats",       10, 7, 7, 5])   # Miscellaneous
    
    # Community. The higher the variable, the better your relationship with that group is.
    define colonists = 0
    define miners = 0
    define luddites = 0
    define jellies = 0