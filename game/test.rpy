# Test functions to ensure various parts of the game are working
# Not called in the actual game. Intended for development use only.

label test_farming_screen:
    $ testing_mode = True
    # randomly enable crops
    if (renpy.random.random()  > 0.5):
        $ enable_crop("strawberries")
    if (renpy.random.random()  > 0.7):
        $ enable_crop("garlic")
    if (renpy.random.random()  > 0.8):
        $ enable_crop("broccoli")
    if (renpy.random.random()  > 0.6):
        $ enable_crop("onions")
    if (renpy.random.random()  > 0.5):
        $ enable_crop("plums")
    if (renpy.random.random()  > 0.2):
        $ enable_crop("honey")
    if (renpy.random.random()  > 0.5):
        $ enable_crop("peppers")
    if (renpy.random.random()  > 0.5):
        $ enable_crop("corn")
    if (renpy.random.random()  > 0.5):
        $ enable_crop("wheat")
    if (renpy.random.random()  > 0.5):
        $ enable_crop("peanuts")
    if (renpy.random.random()  > 0.9):
        $ enable_crop("turnips")
    while (year <= MAX_YEARS):
        $ competence = year
        $ earth_year = get_earth_years(year)
        if (year > 1):
            $ years_yield = farm.process_crops()
            if (year >= MONEY_YEAR):
                $ modify_credits(farm.calculate_income(years_yield))
                $ modify_credits(-(get_expenses_required()  - KELLY_SALARY))
                if (allowance_amount != 0):
                    $ modify_credits(allowance_amount * 7)
        $ farm.reset_crops(farm_size)
        $ read_messages = False
        $ show_year = year
        call screen plan_farm
        label test_continue:
            if (renpy.random.random()  > 0.8):
                $ farm_size += 1
            $ year += 1
            $ notifications = ""
    return

label demo:
    "\"Space to Grow\" is a farming and parenting game."
    "Each year you choose your crops and then experience events (farming, family, and community) where your choices determine the outcome."
    "The game takes place across 18 years, so here are a few types events from different years of the game."
    # setup variables
    $ demo_mode = True
    $ year6_have_baby = True
    $ year = 4
    $ earth_year = get_earth_years(year)
    $ is_liaison = False

    $ attachment = 2
    $ competence = 5
    $ independence = 3
    $ total_demanding = 5
    $ total_responsive = 5
    $ total_confident = 5
    $ authoritarian = 0
    $ authoritative = 0
    $ permissive = 0
    $ neglectful = 0
    $ mavericks = 0
    $ colonists = 0
    $ miners = 0


    # FARMING CHOICES
    play music audio.computer fadein 2.0
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
    $ year = 4
    $ earth_year = get_earth_years(year)
    call interscene_text(year, "Family")
    play music parenting
    call family4

    $ bro_birth_year = 8
    $ year = 14
    $ earth_year = get_earth_years(year)
    call interscene_text(year, "Community")
    play music community
    call community14

    $ year = 18
    $ earth_year = get_earth_years(year)
    $ kid_work_slider = 70
    call interscene_text(year, "Work")
    play music farming
    call spinach2
    $ year = 23
    $ earth_year = get_earth_years(year)
    call interscene_text(year, "Family")
    play music parenting
    call family23
    scene stars with fade
    $ parenting_style = get_parenting_style()
    $ favorite_faction = strongest_faction()
    "Based on your decisions, your parenting style was [parenting_style] and your favorite faction was the [favorite_faction]."
    "That's it for the demo! Pickup a card if you're interested in playing the whole game of \"Space to Grow\" when it comes out next year!"
    jump demo
    return

label screenshots:
    $ year = 8
    scene barn with fade
    show him annoyed at quarterleft
    show kid nervous at quarterright
    show boy sad at right
    menu:
        "[kid_name] hurt her friend's feelings."
        "A)  Make her apologize":
            $ pass
        "B)  Discuss how she can apologize":
            $ pass
        "C)  Apologize to his mom":
            $ pass
        "D)  Let it go":
            $ pass

    $ year = 9
    scene kid_bedroom with fade
    show him sad at quarterleft
    show kid annoyed at quarterright
    menu:
        "[kid_name] won't clean up."
        "A)  Take her toys away":
            $ pass
        "B)  Sympathize with her":
            $ pass
        "C)  Just clean them up":
            $ pass
        "D)  Do nothing":
            $ pass

    $ year = 17
    scene farm_interior with fade
    show him surprised at quarterleft
    show kid concerned at quarterright
    menu:
        "[kid_name] wants help with a hard video game."
        "A)  Remind her video games are a waste of time":
            $ pass
        "B)  Empathize with her, but let her figure it out":
            $ pass
        "C)  Help her beat the level":
            $ pass
        "D)  Ignore her":
            $ pass

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
    show him concerned
    show her concerned
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
    hide kid with dissolve
    $ year = TWEEN_MAX
    show kid normal with dissolve
    hide kid with dissolve
    $ year = YTEEN_MAX
    show kid normal with dissolve
    hide kid with dissolve

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
    nvl clear
    her_c "We are testing all the characters on the message board. 😃"
    him_c "Just so see what they look like"
    kid_c "And make sure it looks good!"
    naomi_c "I'm sure it's fine."
    pavel_c "I agree."
    lily_c "But testing is important."
    sara_c "Don't worry so much!!! :-D"
    thuc_c "You got this, bro."
    ilian_c "Yes, keep saying it and maybe it will come true."
    brennan_c "Positive thinking, right?"
    pete_c "You gotta start somewhere."
    natalia_c "But you also need to finish!"
    helen_c "..."
    julia_c "Practice makes perfect."
    martin_c "Finish before I croak already!"
    anya_c "what??"
    lewis_c "I don't know..."
    zaina_c "Interesting experiment."
    kevin_c "It lacks rigor."
    oleg_c "ghhghhh he said 'rigor'"
    travis_c "iknow right?"
    van_c "::sigh::"
    ret_c "This conversation is unproductive."
    nvl clear
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
    "mavericks: [mavericks]\nColonists: [colonists]\nMiners: [miners]\nJellies: [jellies]."
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
