## Our Personal Space 2
## MAIN

## The game starts here.

label start:

    scene bg stars with fade
    # TODO: import names, stats, etc from OPS1, or ask user to fill them in

    show him happy

    him "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    him normal "Of course, I knew it'd be a lot of work too. But, like most hard work, I figured it'd be worth it."
    him "Even now that you're grown, I still think about your childhood."
    him concerned "Was I there for you? Did I do enough? Was I the dad you needed?"
    him normal "If I could go back, would I change anything? I don't even know."
    him "When you were first born, it was a struggle just to get through each day."  
    # TODO: second person narrative working?
    
    # TODO: show some sort of inter-scene screen, with kids' ages and other info?
    scene bg farm_interior with fade
    show him concerned at midright
    show her concerned at midleft

    her "I just wish I knew why she was still crying! Even if I couldn't help her, at least I'd know I wasn't overlooking something."
    him sad "I know. It's been hours..."
    "I knew she was exhausted. Her body was still healing from the birth, and feeding [kid_name] took a lot of energy, too."
    "I wanted to help, but I had spent the whole day cleaning out the barn and was spent.  All I could think about was sleeping."
    "Sleeping..."
    show black with dissolve
    hide black with dissolve
    him serious "(I can't sleep now. They both need me. But what should I do?)"
    menu:
        "Take [kid_name] for a walk.":
            him concerned "Here, I'll take her for a walk. I know I could use some fresh air, and we've tried everything else."
            her concerned "It's not too cold out, is it?"
            him normal "She'll be fine wrapped up in her blanket. See if you can get some sleep."
            her sad "Are you sure? I know you're tired, too..."
            him happy "If she's still crying in a few hours, it'll be your turn."
            her happy "Okay, good idea."
            scene bg farm_exterior with fade
            show him normal at center with dissolve
            him normal "There now, little [kid_name], how's that?"
            "..."
            "She's still crying. I better get further from the house so I don't keep up [her_name]."
            scene bg fields with fade
            "The winters on Talaam were mild, but it was cold enough that I snuggled [kid_name] close to my chest as I walked, feeling her tiny warmth through my jacket."
            "I reminded myself that she wouldn't cry forever, that this was just one night, even as I felt like sobbing alongside her with exhaustion."
            "I hated feeling so helpless."
            "I wonder if [kid_name] felt the same way?"
            
        "Ask someone else for help.":
            "I wish I could ask my parents, but they're light years away. I'm not sure who else we could ask, though."
            him concerned "Maybe we should ask someone else for help. Someone who knows more about babies."
            her annoyed "Who's going to know more about [kid_name] than us?!"
            
        "Let [her_name] handle it.":
            "[her_name] knows more about this kind of thing than I do. I pushed open the door of our tiny house."
            her annoyed "Where are you going?!"
            him annoyed "You figure it out. I'm going for a walk."
            "Or maybe I'd try to get some sleep in the barn."
            her angry "You can't just leave me here with a screaming baby!"
            "[kid_name] wailed in unison, and their tears wrenched at my heart, but I just couldn't take it anymore."
            scene bg farm_exterior with fade
            "I stepped out into the night, closing the door gently with what little control I had left. I started to run."
            scene bg fields with fade
            "The crying faded from my ears the further I got from the house, but I could still hear the cries echoing in my head. I ran faster."
            scene bg moon with fade
            "I reached the end of our fields, out of breath, legs and chest aching. The pain felt good; I deserved it."
            "Maybe I wasn't cut out to be a dad. What kind of dad leaves when there's trouble?"
            "But this was a trouble I couldn't fix. What was the point in sticking around, when everything I did just seemed to make it worse?"
            
            
        "Let [kid_name] cry.":
            him normal "Sometimes babies cry. Since we're not helping, let's just set her down and take a break."
    
    
    
    return
