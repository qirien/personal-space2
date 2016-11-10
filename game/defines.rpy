# Declare global variables, images, characters, etc.

define mp = MultiPersistent("MetasepiaGames")

# Declare characters used by this game .
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")

define her = DynamicCharacter("her_name", color="#84b766", image="her", ctc="ctc_blink", ctc_position="nestled") #light mint green
define him = DynamicCharacter("his_name", color="#bc1e0e", image="him", ctc="ctc_blink", ctc_position="nestled") #red 

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
define kid = Character("Kid", color="#7788fc", image="kid", ctc="ctc_blink", ctc_position="nestled")


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

# Variables used in the game
define is_nude = False
define is_pregnant = False
define wearing_dress = False # TODO: do we still use these in OPS2?