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
    "She must be exhausted.  Her body is still healing from birth, and feeding [kid_name] takes energy, too."
    "I want to help, but I'm exhausted, too.  All I can think about is sleeping."
    "Sleeping..."
    show black with dissolve
    hide black with dissolve
    "I can't sleep now. They both need me. But what should I do?"
    menu:
        "Take [kid_name] for a walk.":
            him concerned "Here, I'll take her for a walk. I know I could use some fresh air; we've tried everything else."
        "Ask someone else for help.":
            "I wish I could ask my parents, but they're light years away. I'm not sure who else we could ask, though."
            him concerned "Maybe we should ask someone else for help. Someone who knows more about babies."
            her annoyed "Who's going to know more about [kid_name] than us?!"
            
    
    
    
    return
