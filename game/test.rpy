# Test functions to ensure various parts of the game are working
# Not called in the actual game. Intended for development use only.
label tests:
    menu:
        "Which test would you like to run?"
        "Jump to Year":
            jump test_jump_year
        "Test Farming Screen":
            jump test_farming_screen
        "Crop Events.":
            call test_crops from _call_test_crops
        "Family Events.":
            call test_family from _call_test_family
        "Community Events":
            call test_community from _call_test_community
        "Graphics Tests":
            menu:
                "Which graphics test?"
                "Test Family Photo":
                    call test_family_photo from _call_test_family_photo
                "Emoji":
                    call test_emoji from _call_test_emoji
                "Sprites":
                    call test_sprites from _call_test_sprites
                "Positions":
                    call test_positions from _call_test_positions
                "Screenshots":
                    call screenshots from _call_screenshots
                "CGs":
                    call test_cgs from _call_test_cgs

        "Dialogue Test":
            call test_dialogue from _call_test_dialogue
        "Message Board":
            call test_message_board from _call_test_message_board
        "Trailer":
            jump trailer
        "Test Endings":
            call test_endings from _call_test_endings
        "Test Poetry":
            call test_poems from _call_test_poems
        "Test Credits":
            $ year = 30
            $ bro_birth_year = 8
            $ total_mavericks = 8
            $ total_miners = 8
            $ total_colonists = 8
            $ total_attachment = 25
            $ total_competence = 10
            call credits from _call_credits_1
        "Demo":
            call demo from _call_demo
        "Quit":
            return

    jump tests
    return    

label test_cgs:
    "Here are the CGs we have in the game."
    show text "End Baby Years"
    window auto hide
    $ renpy.pause(1.5)
    show baby_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    scene stars with fade
    show text "End Toddler Years"
    $ renpy.pause(1.5)
    show toddler_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    scene stars with fade
    show text "End Childhood Years"
    $ renpy.pause(1.5)
    show child_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    scene stars with fade
    show text "End Tween Years"
    $ renpy.pause(1.5)
    show tween_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    scene stars with fade
    show text "End Young Teen Years"
    $ renpy.pause(1.5)
    show yteen_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    "Other CGs"
    show harvest_cg
    pavel sad "It's a shame we don't have any chocolate to give them."
    natalia happy "I miss it too."
    julia angry "This is better than Halloween. They're actually helping people instead of running around with entitled threats."
    thuc happy "They still sound pretty entitled to me!"
    him laugh "Some things never change."
    window auto hide
    $ renpy.pause()

    show mountain_cg
    "Pete still wasn't happy about the tremors the mining caused, and it irked Brennan to leave so much easy ore untouched."
    "However, the mining continued without incident."

    show jellymother_cg
    "It came closer to the surface, and I could see part of it."
    "It had way more than ten tentacles and was a little larger than our rowboat."

    "Endings"
    
    "Ending 1/4."
    window auto hide
    show ending1_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    "Ending 2/4."
    window auto hide
    show ending2_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    "Ending 3/4."
    window auto hide
    show ending3_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    "Ending 4/4 (Oleg)."
    window auto hide
    show ending4o_cg
    $ renpy.pause(6.0)
    $ renpy.pause()

    "Ending 4/4 (Travis)."
    window auto hide
    show ending4t_cg
    $ renpy.pause(6.0)
    $ renpy.pause()
    return

label test_family_photo:
    $ i = 0
    $ bro_birth_year = 6
    while (i < len(TRANSITION_YEARS)):
        $ year= TRANSITION_YEARS[i]
        $ bro_years = year - bro_birth_year
        $ bro_age = get_earth_years(year - bro_birth_year)
        scene stars with fade
        "Scrapbook time! Aren't we cute?"
        $ authoritarian = 10
        $ marriage_strength = 10
        show family_photo_small Aci at center,kid_pos with moveinright

        "We weren't ready..."

        $ authoritarian = 0
        $ permissive = 10
        $ marriage_strength = 0
        show family_photo_small acI at center,kid_pos with moveinright

        "She has her eyes closed..."

        $ permissive= 0
        $ neglectful = 10
        $ marriage_strength = 1
        show family_photo_small aCI at center,kid_pos with moveinright

        "We weren't ready..."
        $ i += 1


    return

label test_poems:
    "Time for a poetry fest! Make 3 poems!"
    "ready... set... GO!"
    $ word_board.set_wordpack(basic_words, family_words, baby_words)
    call make_poem from _call_make_poem_6
    "OK, that one was pretty good. Time for another!"
    $ word_board.set_wordpack(basic_words, family_words, talaam_words)
    call make_poem from _call_make_poem_7
    "Not bad, not bad. Last one will be the best though!"
    $ word_board.set_wordpack(basic_words, family_words, talaam_words, separation_words)
    call make_poem from _call_make_poem_8
    "OK, now that you've made three poems, let's look at them."
    call screen poetry_display(word_board, True)
    "You looked at your poems. Now save your game, load it, and see if they are still there."
    "Saving... Displaying poems"
    call screen poetry_display(word_board, True)
    "Testing complete!"

    return

label test_endings:
    $ year = 30
    $ bro_birth_year = 8

    call ending_CMiMa from _call_ending_CMiMa_1
    call ending_CMima from _call_ending_CMima_1
    call ending_CmiMa from _call_ending_CmiMa_1
    call ending_Cmima from _call_ending_Cmima_1
    call ending_cMiMa from _call_ending_cMiMa_1
    call ending_cMima from _call_ending_cMima_1
    call ending_cmiMa from _call_ending_cmiMa_1
    call ending_cmima from _call_ending_cmima_1

    call ending_ac from _call_ending_ac_1
    call ending_aC from _call_ending_aC_1
    call ending_Ac from _call_ending_Ac_1
    call ending_AC from _call_ending_AC_1
    
    return

label test_parenting_style:
    # watch(authoritative, authoritarian, permissive, neglectful)
    while True:
        $ authoritative = renpy.random.randint(0,20)
        $ authoritarian = renpy.random.randint(0,20)
        $ permissive = renpy.random.randint(0,20)
        $ neglectful = renpy.random.randint(0,20)
        $ pstyle = get_parenting_style()
        "Parenting style: [pstyle]"

label test_emoji:
    "First we'll test the parenting style emoji."
    $ get_parenting_style()
    $ authoritative = 10
    "Authoritative"
    $ get_parenting_style()
    $ authoritarian = 20
    "Authoritarian"
    $ get_parenting_style()    
    $ permissive = 30
    "Permissive"
    $ get_parenting_style()    
    $ neglectful = 40
    "Neglectful"
    $ get_parenting_style()
    "And next we'll test message board emoji."

    nvl clear
    him_c "I don't usually use emoji...{emoji=blush}" 
    sara_c "But I do! {emoji=happy} All the time!"
    him_c "Yes, yes, we know. {emoji=grimace}"
    brennan_c "Were you talking about me? {emoji=grin}"
    him_c "...no. {emoji=shocked}"
    her_c "{emoji=hearteyes} {emoji=music} {emoji=celebrate}"
    brennan_c "{emoji=sad}"
    ilian_c "What are we going to do with all these turnips?! {emoji=worried}"
    thuc_c "Turnips? .... {emoji=yuck}"
    natalia_c "I love them! {emoji=yum}"
    nvl clear

return

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
        $ total_competence = year
        $ earth_year = get_earth_years(year)
        if (year > 1):
            $ years_yield = farm.process_crops()
            if (year >= MONEY_YEAR):
                $ modify_credits(farm.calculate_income(years_yield))
                $ modify_credits(-(get_expenses_required(year-1)  - KELLY_SALARY))
                if (allowance_amount != 0):
                    $ modify_credits(allowance_amount * 7)
        $ farm.reset_crops(farm_size)
        $ read_messages = False
        $ show_year = year
        call screen plan_farm
        # label test_continue:
        #     if (renpy.random.random()  > 0.8):
        #         $ farm_size += 1
        #     $ year += 1
        #     $ notifications = ""
    return

label demo:
    scene title with fade
    "\"Space to Grow\" has farming and parenting parts of the game. This demo has a small sample of both."
    # setup variables
    $ demo_mode = True
    $ year6_have_baby = True
    $ year = 4
    $ earth_year = get_earth_years(year)
    $ is_liaison = False

    $ total_attachment = 2
    $ total_competence = 5
    $ total_independence = 3
    $ authoritarian = 0
    $ authoritative = 0
    $ permissive = 0
    $ neglectful = 0
    $ mavericks = 0
    $ colonists = 0
    $ miners = 0
    $ total_mavericks = 0
    $ total_colonists = 0
    $ total_miners = 0 

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
    call interscene_text(year, "Family") from _call_interscene_text_3
    play music parenting
    call family4 from _call_family4

    # $ bro_birth_year = 8
    # $ year = 14
    # $ earth_year = get_earth_years(year)
    # call interscene_text(year, "Community")
    # play music community
    # call community14

    $ year = 18
    $ earth_year = get_earth_years(year)
    $ kid_work_slider = 70
    call interscene_text(year, "Work") from _call_interscene_text_4
    play music farming
    call spinach2 from _call_spinach2
    $ year = 23
    $ earth_year = get_earth_years(year)
    call interscene_text(year, "Family") from _call_interscene_text_5
    play music parenting
    call family23 from _call_family23
    scene stars with fade
    $ parenting_style = get_parenting_style()
    $ favorite_faction = strongest_faction()
    "Based on your decisions, your parenting style was [parenting_style]."#" and your favorite faction was the [favorite_faction]."
    "That's it for the demo! Signup on our email list if you're interested in hearing more about \"Space to Grow\""
    jump demo
    return

label screenshots:
    # 1 happy baby moment
    $ year = 1
    "#1"
    scene farm_interior with fade
    show her baby happy at center
    show him content at midleft
    with dissolve
    him "She's almost asleep..."

    # 5 baby bro born
    $ year = 5
    "#2"
    scene bedroom with fade
    show her nervous at center, squatting
    show him sad baby at midleft
    show kid annoyed at midright, squatting
    show bedroom_overlay
    him "It's a boy!"

    # 11 Miners (Brennan) arrive
    $ year = 11
    "#3"
    scene plain with fade
    show miners at left
    show him pout at center
    show bro normal at center, baby_pos
    show her surprised at midright
    show kid surprised at midright
    show brennan flirting at midleft
    brennan "No one told you I was coming?"

    # 15 Naomi dies (maybe CG with all the dead ppl - Martin, Lily, Naomi, Pavel)
    $ year = 14
    "#4"
    scene community_center with fade
    show lily happy at quarterleft
    show naomi happy at midleft
    show pavel happy at center
    show martin happy at midright
    with dissolve
    pavel "We will always remember..."

    # 17 Harvest Festival, showing ppl from favorite faction
    $ year = 17
    "#5"
    scene community_center with fade
    "Did this already"

    # 17 Riding Lettie with bro
    $ year = 17
    "#6"
    scene path with fade
    show horse at center
    show him content at center
    show bro happy at center
    with dissolve
    "Quest complete!"

    # 21 trip to beach with community
    $ year = 21
    "#7"
    scene ocean_sunset with fade
    show purplelight at random_pulse_alpha
    show purplelight as light0 at random_pulse_alpha with dissolve
    show purplelight as light1 at random_pulse_alpha with dissolve
    show purplelight as light2 at random_pulse_alpha with dissolve
    show purplelight as light3 at random_pulse_alpha with dissolve
    show purplelight as light4 at random_pulse_alpha with dissolve
    show her laugh at midleft
    show him laugh at center
    show bro happy at center, squatting
    show kid happy at midright
    with dissolve
    her "Wait, what?!"
    
    # 27 talking to jellypeople - we need a jellyperson for this I think!!
    $ year = 27
    "#8"
    #MiMa
    scene bonfire with fade
    show pete happy at midright
    show him laugh at center
    show brennan explaining at midleft
    brennan "...and that's why you should never trust a skinny chef."

    #Mi
    scene bonfire with fade
    show him laugh at center
    show brennan explaining at midleft
    show thuc happy at midright
    brennan "I think I've told this joke before."

    #Ma
    scene bonfire with fade
    show pete happy at midright    
    show thuc happy at midleft
    show him laugh at center
    pete "I ain't never heard that one before!"

    #C
    scene bonfire with fade
    show thuc happy at midleft
    show him normal at center
    show ilian normal at midright
    ilian "That was almost funny."


    # 30 family group hug if authoritative, permissive; clinic scene if authoritarian; subdued family photo without Terra if she left
    $ year = 30    
    "#9"
    scene farm_interior with fade
    show him normal at midleft 
    show her normal at midright
    show bro normal at midright, squatting 
    show kid normal at center
    him "group hug!"

    scene hospital with fade
    show her surprised coat at midright
    show kid concerned at center
    with dissolve
    her "Not quite."

    scene farm_interior with fade
    show him concerned at midleft
    show her concerned at midright
    show bro concerned at center
    bro "I miss her..."
    

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
    call bedroom_scene(True) from _call_bedroom_scene_7
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


label test_dialogue:
    if (mp.jack_name):
        $ his_name = mp.jack_name
    else:
        $ his_name = "Jack"
    if (mp.kelly_name):
        $ her_name = mp.kelly_name
    else:
        $ her_name = "Kelly"        
    if (mp.baby_name):
        $ kid_name = mp.baby_name
    else:
        $ kid_name = "Terra"
    if (mp.bro_name):
        $ bro_name = mp.bro_name
    else:
        $ bro_name = "Aeron"

    $ year = 25
    $ bro_birth_year = 8
    scene farm_interior with fade
    show him normal at midright
    show her happy at midleft
    with dissolve
    her happy "Thanks so much for taking my turn tonight! I had a crazy day."
    him flirting "I'll cook for you any time!"
    show kid normal at center
    show bro normal at quarterleft
    with moveinleft
    kid surprised "WHAT is THAT?!"
    show her surprised with dissolve    
    him pout "It's dinner."
    kid annoyed "Yeah, but what is it?!"
    bro concerned "Is it... crabird?"
    him annoyed "No!"

    scene yurt_interior with fade
    show naomi normal at midright
    show pavel normal at midleft
    with dissolve
    naomi sad "[his_name] brought over something for dinner..."
    pavel sad "What in the world could it be?"

    scene mine with fade
    show brennan normal at midright
    show chaco normal at midleft
    with dissolve
    brennan surprised "Did someone... grow this?"
    chaco sad "Maybe?"

    scene fields with fade
    show natalia normal at midright
    show martin normal at midleft
    with dissolve
    natalia happy "I heard [his_name] brought us dinner!"
    martin angry "If you could call it that."

    scene shack with fade
    show sara normal at midright
    show ilian normal at center
    show oleg normal at midleft    
    with dissolve
    sara sad "Where did you say you got this?"
    oleg angry "[his_name] was giving them away..."
    ilian angry "Just because it's free doesn't mean it's any good!"

    scene path with fade
    show julia normal at midright, flip
    show thuc normal at midleft
    with dissolve
    julia angry "I hope you didn't pay money for this!"
    thuc happy "I can't tell if I'm supposed to eat it or bury it!"

    scene cave with fade
    show pete normal at midright
    show helen normal at midleft
    show travis normal at center
    show lily normal at quarterleft
    with dissolve
    travis angry "Am I seriously supposed to eat this?!"
    helen sad "It's what we have, sweetie."
    pete angry "You ain't eating anything with that attitude! Better say 'thank you' first!"
    lily angry "I require independent verification of edibility first."

    scene cabins with fade
    show kevin normal at midright
    show zaina normal at midleft
    with dissolve
    kevin sad "Could it be for dissolving pipe blockages?"
    zaina sad "[his_name] made it sound like you could eat it..."

    scene farm_interior with fade
    show him determined at midright
    show her concerned at midleft
    show kid annoyed at center
    show bro concerned at quarterleft
    with dissolve
    
    him yell "Don't tell me everyone's too scared to try a new food?!"
    kid determined "I'm not afraid of anything. I'll try it."
    her surprised "What does it taste like?"
    kid surprised "It tastes like..."
    him surprised "..."
    kid happy "Garlic spinach cheese sauce?"
    her normal "Wait, did you make pesto?"
    him annoyed "Yes! I worked all day on that and shared it with everyone in town and you're acting like I'm making you eat mud!"
    bro normal "I think it looks more like--"
    him angry "Careful-- I'm not giving any to people that disparage my cuisine!"
    bro happy "---like something I want to try."
    him happy "That's better!"
    scene stars with fade
    return

label test_message_board:
    nvl clear
    her_c "We are testing all the characters on the message board. {emoji=happy}"
    him_c "Just so see what they look like"
    kid_c "And make sure it looks good!"
    bro_c "I don't have to do anything, right?"
    naomi_c "I'm sure it's fine."
    pavel_c "I agree."
    lily_c "But testing is important."
    sara_c "Don't worry so much!!! {emoji=grin}"
    thuc_c "You got this, bro."
    ilian_c "Yes, keep saying it and maybe it will come true."
    brennan_c "Positive thinking, right?"
    pete_c "You gotta start somewhere."
    natalia_c "But you also need to finish!"
    helen_c "..."
    chaco_c "Why?"
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
        call interscene_text(i, "Message Board") from _call_interscene_text_6
        $ message = "message" + `i`
        call expression message from _call_expression_5
        $ i += 1
    return

label test_jump_year:
    $ year_str = renpy.input("What year should we jump to?")
    $ year = int(year_str)
    $ earth_year = get_earth_years(year)
    $ bro_birth_year = 8 #6
    $ year8_have_baby = True #$ year6_have_baby = True #
    $ credits = 1000
    $ total_miners = renpy.random.randint(0,year)
    $ total_mavericks = renpy.random.randint(0,year-total_miners)
    $ total_colonists = year - total_miners - total_mavericks
    menu:
        "What type of parent are you?"
        "Authoritarian":
            $ total_attachment = 0
            $ total_competence = year * (COMPETENCE_HIGH/float(MAX_YEARS))
            $ total_independence = year * (INDEPENDENCE_HIGH/float(MAX_YEARS))
            $ authoritarian = year
            $ authoritative = 0
            $ permissive = 0
            $ neglectful = 0
        "Authoritative":
            $ total_attachment = year * (ATTACHMENT_HIGH/float(MAX_YEARS))
            $ total_competence = year * (COMPETENCE_HIGH/float(MAX_YEARS))
            $ total_independence = year * (INDEPENDENCE_HIGH/float(MAX_YEARS))
            $ authoritarian = 0
            $ authoritative = year
            $ permissive = 0
            $ neglectful = 0
        "Permissive":
            $ total_attachment = year * (ATTACHMENT_HIGH/float(MAX_YEARS))
            $ total_competence = 0
            $ total_independence = 0
            $ authoritarian = 0
            $ authoritative = 0
            $ permissive = year
            $ neglectful = 0
        "Neglectful":
            $ total_attachment = 0
            $ total_competence = 0
            $ total_independence = 0
            $ authoritarian = 0
            $ authoritative = 0
            $ permissive = 0
            $ neglectful = year
        "Random":
            $ total_attachment = renpy.random.randint(0,ATTACHMENT_MAX)
            $ total_competence = renpy.random.randint(0,COMPETENCE_MAX)
            $ total_independence = renpy.random.randint(0,INDEPENDENCE_MAX)
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
    call test_sprite("kid") from _call_test_sprite
    $ year = 3
    "Toddler"
    call test_sprite("kid") from _call_test_sprite_1
    $ year = 7
    "Young Kid"
    call test_sprite("kid") from _call_test_sprite_2
    $ year = 13
    "Older Kid"
    call test_sprite("kid") from _call_test_sprite_3
    $ year = 23
    "Teen"
    call test_sprite("kid") from _call_test_sprite_4

    # Test Adult Sprites
    call test_sprite("him") from _call_test_sprite_5
    call test_sprite("her") from _call_test_sprite_6

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
    $ testing_mode = True
    $ year = 1

    while (year <= MAX_YEARS):
        $ total_competence = year
        $ earth_year = get_earth_years(year)
        if (bro_birth_year != 0):
            $ bro_years = year - bro_birth_year
            $ bro_age = get_earth_years(bro_years)
        if (year > 1):
            $ years_yield = farm.process_crops()
            if (year > MONEY_YEAR):
                $ income = farm.calculate_income(years_yield)
                $ modify_credits(income)
                $ modify_credits(-(get_expenses_required(year-1) - KELLY_SALARY)) # We want this for the PREVIOUS year.
                if (allowance_amount != 0):
                    $ modify_credits(allowance_amount * 7)
        if (crop_enabled("wheat")):
            $modify_credits(-WHEAT_COST)
        $ farm.reset_crops(farm_size)
        $ read_messages = False
        $ show_year = year
        call screen plan_farm
        label test_continue:
            $ notifications = ""
            $ current_work = get_work_available()
            $ total_work = farm.get_total_work()

            # MALNUTRITION EVENT (optional)
            if (farm.low_vitamins() and (year > NUTRITION_YEAR)):
                call bad_nutrition from _call_bad_nutrition_1
            $ work_event = get_next_work_event()
            call expression work_event from _call_expression_6
            $ year += 1

    jump ending
    return



label test_family:

    $ year = 1
    $ attachment = 0
    $ competence = 0
    $ independence = 0
    $ authoritative = 0
    $ authoritarian = 0
    $ permissive = 0
    $ neglectful = 0

    while (year <= 30):
        $ farm.reset_crops(farm_size)
        $ farm.crops.setDefault()
        $ renpy.notify("Year [year]")
        call expression "family" + str(year) from _call_expression_7
        # Increase child stats based on this year's parenting decisions
        call increase_stats from _call_increase_stats_1

        # Reset our variables while keeping a running total
        call reset_variables from _call_reset_variables_1

        $ year += 1

    jump ending
    return

label test_community:
    $ year = 1
    while (year <= 30):
        $ farm.reset_crops(farm_size)
        $ farm.crops.setDefault()
        $ renpy.notify("Year [year]")
        call expression "community" + str(year) from _call_expression_8

        call increase_stats from _call_increase_stats_2
        call reset_variables from _call_reset_variables_2
        $ year += 1

    jump ending
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

screen countdown():
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.02), false=[Hide('countdown'), Jump(timer_jump)])
