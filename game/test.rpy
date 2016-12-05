# Test functions to ensure various parts of the game are working
# Not called in the actual game. Intended for development use only.

image toddler = "sprites/toddler.png"

label baby_positions:
    scene bg farm_interior with fade
    show him normal at midleft
    show toddler at midright 
    with dissolve
    "Here is the baby at midright"
    him annoyed  "I can't even see the baby on the floor"
    show toddler at midrightbaby with move
    him surprised "Ooh, levitating baby!"
    show her at midright behind toddler with moveinright
    her flirting "It looks better if I'm holding her."
    show toddler at rightbaby with move
    kid "But I could also sit on the bed!"
    
    show kid normal at midright with dissolve
    
    kid "I'm kinda short, but I have feet unlike everyone else, so it's OK!"
    show kid normal at centerkid with move
    kid "But I could stand farther up as long as I have feet!"
