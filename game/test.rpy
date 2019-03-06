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
    $ independence = INDEPENDENCE_HIGH/2
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
    $ year = 6
    call interscene_text(year, "Work")
    play music farming fadeout 3.0 fadein 3.0
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
    call family27
    $ year = 30
    call interscene_text(year, "Ending")
    call ending
    return

label trailer:
    $ trailer_mode = True
    image title = "images/bg/title.jpg"
    image metasepia = "images/bg/metasepia-logo.jpg"
    play music maintheme fadein 1.0
    scene black with fade
    $ renpy.pause(1.0)
    scene title with fade
    $ renpy.pause(2.5)
    scene metasepia with fade
    $ renpy.pause(2.0)

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}a sci-fi parenting simulation\nvisual novel{/font}{/size}"
    $ renpy.pause(2.0)

    $ year = 1
    call bedroom_scene(True)
    "All [kid_name] needed at first was a clean diaper, milk, and some love."
    show kid sad with dissolve
    show him nude concerned
    show her nude concerned
    with dissolve
    "It wasn't always that simple, though."

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}Raise Your Daughter{/font}{/size}"
    $ renpy.pause(1.0)

    $ year = 4
    scene farm_interior with fade
    show him determined at midright
    show her determined at midleft
    show kid annoyed at center
    with dissolve
    her annoyed "Rice is what's for dinner, sweetie."
    kid concerned "Yucky."

    $ time = 2
    $ timer_range = 2
    $ timer_jump = "trailer_after_dinner"
    show screen countdown
    menu:
        "What should I say?"
        "You must eat this dinner.":
            $ pass
        "I'll see if I can get you some applesauce.":
            $ pass
        "(Say nothing.)":
            $ pass
        "You can eat it or not, but there won't be more dinner.":
            $ pass

label trailer_after_dinner:
    hide screen countdown
    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}Plan Your Farm{/font}{/size}"
    $ renpy.pause(1.0)
    $ farm_size = 9
    call screen plan_farm

label trailer_continue:
    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}Lead Your Community{/font}{/size}"
    $ renpy.pause(1.0)

    scene community_center with fade
    show lily normal at midright
    show him determined at midleft
    with dissolve
    lily angry "Tell them to delay mining on that branch until we can fully explore it."
    him concerned "I can send the insta-com, but they might not respond in time."

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}Will you parent with an iron fist...{/font}{/size}"
    $ renpy.pause(1.0)

    $ year = 4
    scene farm_interior with fade
    show him determined at midright
    show kid annoyed at center
    him angry "You're not leaving the table until you eat all of this food!"
    show kid at up_and_down
    kid angry "No! No no no no no no!"
    show her surprised at midleft with moveinleft

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}...or indulge your daughter's whims...{/font}{/size}"
    $ renpy.pause(1.0)

    $ year = 17
    scene farm_interior with fade
    show him surprised at midleft
    show kid normal at midright
    kid concerned "Dad, I really want an allowance."
    him normal "You can have ten credits a week."
    kid happy "Really? Awesome! I'll be able to buy all sorts of stuff!"

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}...or something else entirely?{/font}{/size}"
    $ renpy.pause(1.0)

    $ year = 9
    scene kid_bedroom with fade
    show him annoyed at midright
    show kid annoyed at midleft
    kid angry "No! I won't clean up!"
    "I took a deep  breath. I realized I had some other options."
    $ time = 2
    $ timer_range = 2
    $ timer_jump = "trailer_after_cleanup"
    show screen countdown
    menu:
        "What should I do?"
        "Ask for details.":
            $ pass
        "Take her toys away if she doesn't clean them up.":
            $ pass
        "Sympathize with her":
            $ pass
        "Make cleaning up a game.":
            $ pass

label trailer_after_cleanup:
    hide screen countdown
    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}Create a space for her to grow{/font}{/size}"
    $ renpy.pause(1.0)

    scene black with fade
    $ year = BABY_MAX
    show kid normal with dissolve
    hide kid with dissolve
    $ year = TODDLER_MAX
    show kid normal with dissolve
    hide kid with dissolve
    $ year = CHILD_MAX
    show kid normal with dissolve
    hide kid with fade
    $ year = TWEEN_MAX
    show kid normal with dissolve
    hide kid with fade
    $ year = YTEEN_MAX
    show kid normal with dissolve
    hide kid with fade

    scene black with fade
    show text "{size=60}{font=fonts/SP-Marker Font.otf}with protection, nourishment, and love.{/font}{/size}"
    $ renpy.pause(1.0)

    scene farm_exterior with fade
    show kid happy at center
    show him normal at midright
    show her normal at midleft
    "I felt [kid_name]'s hand on my back, which used to be so small and helpless, and now was strong and callused like mine."
    him happy "Out of all the things we've grown over the years... this family is the best."

    scene title with fade
    $ renpy.pause(10.0)

    scene black with fade
    $ renpy.pause(5.0)

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

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false=[Hide('countdown'), Jump(timer_jump)])
