# Omake, unlocked after beating the game
# What really happened to Dr. Lily?
label jellysquid_logs:
    $ bios = Bios()
    $ year = 30
    scene lab with fade
    show kid normal at center
    with dissolve
    kid determined "I finally managed to recover some data from Dr. Lily's computer pad that the jellies recovered from the bottom of the ocean."
    kid concerned "I heard she died mysteriously several years ago..."
    kid normal "Maybe her logs have some clues? The water damage corrupted some files but there are some bits I can read..."

    nvl clear
    lily_c "2nd M$nth, Day 7\nJel1ysquid resp;nding positPvely to ^raining. AsYociati&n ind*x incre sing at a rat# indicatihg lejrning is taking place. See att^&Ch@# $tA."
    lily_c "4th Mon#h, Day 21\nInge&ting jellyst(rs or jellyJquid produce! interesting h_rmonal eff+cts in =umans - elevat3d oxytoc1n and ser9tonin. Ob,erved in?multi;le subjec*s. Bac3eria/v2rus/pheromon-s?? More st@dy~needed."
    lily_c "7th Month, Day 17\nDir3ct neural commu^ication 0ay be poss5ble. Tr*ining resulQs have>leveled.off; lCnguag@ is lim#ting factor. Sc8ba equi~ment request denieP."
    lily_c "C)pied all res5arch to Mira`da. EverythingEs in order. IfGneural link estab9ished as plan#ed, languZge cognitio7 should incre|se exponentiall'.\n\nsee you soYn, Winston."
    nvl clear

    kid surprised "Winston? I don't think there's anyone on the colony with that name..."

    kid_c "Hey mom, do you know of anyone on Talaam named Winston?"
    her_c "Winston? No... wait, I think he was one of the original researchers. Yes, he was Dr. Lily's husband, but he died before your dad and I arrived."
    kid_c "OK, thanks."

    kid determined "So she went to establish a neural link with the jellies, and thought she might die..."
    kid nervous "Well, I guess she did die."

    kid surprised "But wait, month 7, day 21?! That's right before she died, and also right around when we started being able to talk to the jellysquids on the computer pads..."
    kid excited "Maybe Dr. Lily's plan worked! The jellies learned our language from her neural link or whatever! I have to ask them!"

    scene rowboat with fade 
    show kid normal at midleft with dissolve

    nvl clear
    kid_c "Do you know Dr. Lily?"
    jellysquid "Yes."
    kid_c "Is she... still there?"
    jellysquid "Thinking parts, yes. Shell parts, no."
    kid surprised "So... like her brain is there but not the rest of her??"
    kid_c "You mean her brain?"
    jellysquid "Brain? Thinking parts. Yes."
    nvl clear

    kid happy "Amazing..."
    kid_c "Thank you, Dr. Lily!"
    jellysquid "Yes."
    scene stars with fade
    return


# No longer used as an ending, but unlocked as a BONUS after beating the game.
label ending_extra:
    $ bios = Bios()
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
    scene stars with fade
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


