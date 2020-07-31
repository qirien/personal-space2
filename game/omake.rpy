# Omake, unlocked after beating the game
# What do Terra and Aeron do when no one else is home...?
# TODO: write this
label omake:
    $ year = 15
    scene farm_interior with fade
    show kid normal at midright
    show bro normal at midleft
    with dissolve
    kid determined "And that's why you can't tell mom and dad, no matter what, okay?"
    bro concerned ""

    return

####################################################
# Code for a minigame to punch people.
# Not very sophisticated.
####################################################
#TODO: remove if we end up not using this


##
# DYNAMIC MOUSE CURSOR
##
init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "punch":
            setattr(config, "mouse", {"default": [("gui/punch.png", 6, 6)]})

    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)

    def random_float():
        return renpy.random.random()


init python:
    class Punchable(renpy.store.object):
        def __init__(self, name, hitpoints=10):
            self.name = name
            self.maxHP = hitpoints
            self.currentHP = hitpoints
            
        def punch(self, damage=1):
            self.currentHP -= damage
            return
    
        def HP_left(self):
            return self.currentHP
            
        def getImage(self):
            return Image("images/sprites/" + self.name.lower() + " normal.png")
            
        def getMadImage(self):
            return Image("images/sprites/" + self.name.lower() + " angry.png")

init -1 python:
    punchBrennan = None
    
    def punch_him():
        # TODO: if we actually use this, add in a "POW!" or something
        renpy.notify("POW!")
        punchBrennan.punch()            


label fight_brennan:
    scene path with fade
    show him angry at midright
    show brennan normal at midleft
    $ punchBrennan = Punchable("Brennan", 7)
    "Ready? Fight!"
    $ change_cursor("punch")
    call screen punch(punchBrennan)
    show brennan mad
    $ change_cursor("default")
    "That was some serious fighting."  
    return


screen punch(whom_to_punch):
    $ punchBrennan = whom_to_punch
    frame:
        background "path"
        yalign 0.5
        xalign 0.5
        xfill True
        yfill True
        $ brennan_hp = punchBrennan.HP_left()
        $ pos_x = renpy.random.randint(0,1200)
        $ pos_y = 50        
        imagebutton idle punchBrennan.getImage() hover punchBrennan.getMadImage() action punch_him ypos pos_y at pace_back_and_forth
        if (brennan_hp <= 0):
            textbutton "Finish Him!" xpos 0.5 ypos 0.5 xalign 0.5 yalign 0.5 text_size 100 text_color "#FF0000" action Return()


