# Test functions to ensure various parts of the game are working
# Not called in the actual game. Intended for development use only.

label demo:
    # setup variables
    $ demo_mode = True
    $ year6_have_baby = True
    $ bro_birth_year = 8
    $ years = [3,7,12,17,27]

    $ attachment = ATTACHMENT_HIGH
    $ competence = COMPETENCE_HIGH/2
    $ independence = INDEPENDENCE_HIGH/5
    $ total_demanding = 5
    $ total_responsive = 5
    $ total_confident = 5
    $ authoritarian = 2
    $ authoritative = 3
    $ permissive = 6
    $ neglectful = 1


    # FARMING CHOICES
    $ computer_song = renpy.random.choice(audio.computer)
    play music computer_song fadein 2.0
    hide screen say
    scene stars with fade
    if (year > 1):
        $ years_yield = farm.process_crops()
        if (year >= MONEY_YEAR):
            $ credits += farm.calculate_income(years_yield)
    $ farm.reset_crops(farm_size)
    $ read_messages = False
    $ show_year = year
    call screen plan_farm

label demo_continue:
    $ year = 3
    call interscene_text(year, "Family")
    call family3
    $ year = 4
    call interscene_text(year, "Community")
    call community4
    $ year = 6
    call interscene_text(year, "Work")
    call work6
    $ year = 10
    call interscene_text(year, "Community")
    call community10 # Finish this event
    $ year = 18
    $ kid_work_slider = 70
    call interscene_text(year, "Work")
    call spinach2
    $ year = 27
    call interscene_text(year, "Family")
    call family27 # Blocking for this event
    $ year = 30
    call ending
    return

label tests:
    menu:
        "Which test would you like to run?"
        "Crop Events.":
            call test_crops
        "Family Events.":
            call test_family
        "Community Events":
            call test_community
        "Baby Positions":
            #call test_positions
            call baby_positions
        "Omake":
            call omake
        "Sprites":
            call test_sprites
        "Message Board":
            call test_message_board
        "Quit":
            return

    jump tests
    return

label test_message_board:
    $ i = 1
    while (i <= MAX_YEARS):
        call interscene_text(i, "Message Board")
        $ message = "message" + `i`
        call expression message
        $ i += 1
    return

label test_jump_year:
    $ year_str = renpy.input("What year should we jump to?", default=1)
    $ year = int(year_str)
    menu:
        "What type of parent are you?"
        "Authoritarian":
            $ attachment = 0
            $ competence = year * (COMPETENCE_HIGH/float(MAX_YEARS))
            $ independence = year * (INDEPENDENCE_HIGH/float(MAX_YEARS))
            $ total_demanding = year
            $ total_responsive = 0
            $ total_confident = year/4
            $ authoritarian = year
            $ authoritative = 0
            $ permissive = 0
            $ neglectful = 0
        "Authoritative":
            $ attachment = year * (ATTACHMENT_HIGH/float(MAX_YEARS))
            $ competence = year * (COMPETENCE_HIGH/float(MAX_YEARS))
            $ independence = year * (INDEPENDENCE_HIGH/float(MAX_YEARS))
            $ total_demanding = year
            $ total_responsive = year
            $ total_confident = year
            $ authoritarian = 0
            $ authoritative = year
            $ permissive = 0
            $ neglectful = 0
        "Permissive":
            $ attachment = year * (ATTACHMENT_HIGH/float(MAX_YEARS))
            $ competence = 0
            $ independence = 0
            $ total_demanding = 0
            $ total_responsive = year
            $ total_confident = year/4
            $ authoritarian = 0
            $ authoritative = 0
            $ permissive = year
            $ neglectful = 0
        "Neglectful":
            $ attachment = 0
            $ competence = 0
            $ independence = 0
            $ total_demanding = 0
            $ total_responsive = 0
            $ total_confident = 0
            $ authoritarian = 0
            $ authoritative = 0
            $ permissive = 0
            $ neglectful = year
        "Random":
            $ attachment = renpy.random.randint(0,ATTACHMENT_MAX)
            $ competence = renpy.random.randint(0,COMPETENCE_MAX)
            $ independence = renpy.random.randint(0,INDEPENDENCE_MAX)
            $ total_demanding = renpy.random.randint(0,COMPETENCE_MAX)
            $ total_responsive = renpy.random.randint(0,ATTACHMENT_MAX)
            $ total_confident = renpy.random.randint(0,INDEPENDENCE_MAX)
            $ authoritarian = renpy.random.randint(0,year)
            $ authoritative = renpy.random.randint(0,year-authoritarian)
            $ permissive = renpy.random.randint(0,year-authoritarian-authoritative)
            $ neglectful = year-authoritarian-authoritative-permissive
    $ farm.crops.setDefault()
    jump life_loop

label test_sprites:
    scene farm_interior with fade

    # Test Kid sprites
    $ year = 1
    "Baby"
    call test_sprite("kid")
    $ year = 3
    "Toddler"
    call test_sprite("kid")
    $ year = 7
    "Young Kid"
    call test_sprite("kid")
    $ year = 13
    "Older Kid"
    call test_sprite("kid")
    $ year = 23
    "Teen"
    call test_sprite("kid")

    # Test Adult Sprites
    call test_sprite("him")
    call test_sprite("her")

    return

label test_sprite(sprite_name="kid"):
    scene farm_exterior with fade
    python:
        renpy.say(None, sprite_name)
        sprite_attributes = renpy.get_ordered_image_attributes(sprite_name)
        for attribute_name in sprite_attributes:
            renpy.show(sprite_name + " " + attribute_name)
            renpy.say(None, attribute_name)
    return

label test_crops:

    $ year = 1

    while (year <= 30):
        $ farm.reset_crops(farm_size)
        $ farm.crops.setDefault()
        $ renpy.notify("Year [year]")

        $ work_event = get_next_work_event()
        call expression work_event
        $ year += 1

    "The end"
    jump ending
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
        $ total_demanding = 0
        $ total_responsive += responsive
        $ total_responsive = 0

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
    show toddler at midright, baby_pos
    with dissolve
    "Here is the baby at midright"
    him annoyed  "I can't even see the baby on the floor"
    show toddler at midright, baby_pos with move
    him surprised "Ooh, levitating baby!"
    show her happy at midright behind toddler with moveinright
    her flirting "It looks better if I'm holding her."
    show toddler at right, baby_pos with move
    kid "But I could also sit on the bed!"

    show kid normal at midright with dissolve

    kid "I'm kinda short, but I have feet unlike everyone else, so it's OK!"
    show kid normal at center with move
    kid "But I could stand farther up as long as I have feet!"
    return

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
