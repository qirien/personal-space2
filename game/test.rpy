# Test functions to ensure various parts of the game are working
# Not called in the actual game. Intended for development use only.

label tests:
    menu:
        "Which test would you like to run?"
        "Family Events.":
            call test_family
        "Positions":
            call test_positions
            call baby_positions
        "Omake":
            call omake

    return

label test_family:

    $ year = 1
    $ attachment = 0
    $ competence = 0
    $ independence = 0
    $ total_demanding = 0
    $ total_responsive = 0
    $ authoritative = 0
    $ authoritarian = 0
    $ permissive = 0
    $ neglectful = 0

    while (year <= 30):
        $ farm.reset_crops(farm_size)
        $ farm.crops.setDefault()
        $ renpy.notify("Year [year]")
        call expression "family" + str(year)
        # Increase child stats based on this year's parenting decisions
        call increase_attachment
        call increase_competence
        call increase_independence

        # Reset our variables while keeping a running total
        $ total_demanding += demanding
        $ demanding = 0
        $ total_responsive += responsive
        $ responsive = 0

        $ year += 1

    "The end"
    jump ending
    return

label test_community:
    $ year = 1
    while (year <= 30):
        $ renpy.notify("Year [year]")
        call expression "community" + str(year)
        $ year += 1

    "Game complete."
    "Luddites: [luddites]\nColonists: [colonists]\nMiners: [miners]\nJellies: [jellies]."
    return

image toddler = "sprites/toddler.png"

label baby_positions:
    scene farm_interior with fade
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


label test_positions:
    "left"
    show her normal at left
    "quarterleft"
    show him normal at quarterleft
    "midleft"
    show pavel at midleft, behind sara
    "center"
    show sara at center
    "midright"
    show lily at midright
    "quarterright"
    show brennan at quarterright
    "right"
    show natalia at right
    "end test positions"
    return
