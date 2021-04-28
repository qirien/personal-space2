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




# No longer used as an ending, but unlocked as a BONUS after beating the game.
label ending_extra:
    if (mp.jack_name):
        $ his_name = mp.jack_name
    else:
        $ his_name = "Jack"
    if (mp.baby_name):
        $ kid_name = mp.baby_name
    else:
        $ kid_name = "Terra"
    $ year = 30
    "You would originally get this ending if you were a neglectful parent but [kid_name] was very independent. That is pretty hard to do, so we ended up deleting it."
    play music tense
    scene stars with fade
    "Even though [kid_name] still lives on Talaam, I worry a lot about her."
    "She's got more competition with deliveries and now it's harder for her to get business."
    "I worry that she moved in with Travis because she needed a job and a place to stay, not because she really loves him."
    "I worry that she'll be too prideful to ask for help when she needs it."
    "And I worry that I didn't teach her enough for her to be out on her own already."
    "And the worst part about these worries is that, for the most part, I can't do anything about them."
    "I try to talk to her, to be there for her..."
    "...but she doesn't want anything to do with me."

    scene restaurant with fade
    show travis angry at quarterright
    show kid determined at midright
    with dissolve
    show him concerned at midleft
    with moveinleft
    him concerned "Hey, [kid_name]."
    kid annoyed "Dad. What are you doing here?"
    him sad "I just had some extra pickles and thought you might like some."
    "I held them out like I used to hold carrots out for Lettie when I was training her."
    "She looked at Travis, who shrugged and walked off."
    hide travis with moveoutright
    show kid at center with move
    "She took the pickles but didn't get too close."
    show kid at midright with move
    kid concerned "Thanks."
    him determined "If there's anything you need help with--"
    kid annoyed "Dad, I'm fine."
    him surprised "How's Travis?"
    kid nervous "Good."
    him normal "You still have lots of deliveries to make?"
    kid determined "Some. But the miners that left were my best customers."
    menu:
        "What should I say?"
        "What are you going to do?":
            him surprised "So...what are you going to do?"
            kid annoyed "Something else, I guess. Don't worry about it, dad -- it's my life."
            him sad "I'm your dad; I can't not worry about you."
        "Come home.":
            him sad "Come home, [kid_name]. Your room is still there, waiting for you--"
            kid angry "So you can boss me around? No thanks, dad."
            him annoyed "I wouldn't--"
            kid annoyed "Yeah, you would. You don't know any other way to be."
            "That was unfair. But I couldn't think of a good retort."
            kid determined "And that's fine, but I can't live there anymore."
            him determined "You could."
        "Travis doesn't deserve you.":
            him annoyed "Travis doesn't deserve you. Why are you still hanging around him?"
            kid annoyed "You don't even know him! He works hard!"
            him angry "He runs a bar!"
            kid nervous "Look, you had your chance to be my dad when I was little and I didn't have a choice. It's too late to start caring now."
            him angry "I've cared for you your whole life!"
    kid sad "Ugh, Dad, can we not?"
    him sad "..."
    kid determined "Just... just let me live my life, okay? I'm going to make mistakes."
    kid surprised "Maybe I'll be unemployed, maybe I'll trust the wrong person and have my heart broken, maybe I'll go hungry and eat nothing but potatoes for a month, or maybe I'll hunt crabirds and die alone in the wilderness!"
    kid determined "But if I don't try, if I don't get a chance to make those mistakes for myself...what's the point of being alive?"
    show him surprised with dissolve
    "I wanted to embrace her, to give her a father's comfort. But I didn't think I could take it if she pushed me away."
    him concerned "I understand."
    "I turned to leave."
    kid nervous "Dad?"
    him surprised "Yes?"
    kid normal "Thanks for the pickles."
    him normal "Anytime."

    "Ending, Mistakes to Call My Own."
    return



####################################################
# Code for a minigame to punch people.
# Not very sophisticated.
####################################################
init python:
    class Punchable(renpy.store.object):
        def __init__(self, name, hitpoints=5):
            self.name = name
            self.maxHP = hitpoints
            self.currentHP = hitpoints
            
        def punch(self, damage=1):
            self.currentHP -= damage
            return
    
        def HP_left(self):
            return self.currentHP
            
        def getImage(self):
            return Image("images/sprites/" + self.name.lower() + " flirting.png")
            
        def getMadImage(self):
            return Image("images/sprites/" + self.name.lower() + " angry.png")

init -1 python:
    punchBrennan = None
    
    def punch_him():
        renpy.notify("POW!")
        punchBrennan.punch()            


label fight_brennan:
    scene path with fade
    show him angry at midright
    show brennan normal at midleft
    $ punchBrennan = Punchable("Brennan", 7)
    "Ready? Fight!"
    call screen punch(punchBrennan)
    show brennan sad
    show him determined
    with dissolve    
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


