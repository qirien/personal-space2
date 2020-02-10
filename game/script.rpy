## Our Personal Space 2
## MAIN

## The game starts here.
#
# TODO: Add another parenting class before Naomi dies?
# TODO: Warn halfway for bad/inconsistent parenting?
# TODO: Make disabled choices visible, but disabled. Use a 🔒 symbol
#       the first time through, and second time through show what you'd need
#       to get that choice.
#       A later version of Ren'Py should support this automatically...
# TODO: Autosave/resume does not work well right now.
##

label start:

    # Initialize dynamic variables that need to be saved with saved game state.
    # These have to be here instead of in an init block to tell Ren'Py that they will change and should be saved with the game state.

    # GAME ENGINE
    python:
        demo_mode = False
        trailer_mode = False
        testing_mode = False
        save_name = "Intro"
        notifications = ""
        read_messages = False
        word_board = Board(basic_words, family_words, farm_words)
        year11_poem = ""
        year18_poem = ""

    # PARENTS
    python:
        # Demanding and Reponsive may change by more or less than 1 each year
        # Positive indicates high expectations and reponsibilities for child; negative indicates indulgence and undiscpline
        # Max for each is about 30
        demanding = 0
        total_demanding = 0
        # Positive indicates high emotional attachment and empathy; negative indicates aloofness and dismissiveness of child's feelings
        responsive = 0
        total_responsive = 0

        # When you give your child opportunities to do things for herself, you show confidence in her. This increases her independence.
        confident = 0
        total_confident = 0

        # The Four Parenting Styles
        # Only one of these should be increased each year, maximum value at the end of the game is 30
        authoritarian = 0
        authoritative = 0
        permissive = 0
        neglectful = 0
        trust = 0

        # Default names
        his_name = "Jack"
        her_name = "Kelly"
        his_nickname = "dear"
        her_nickname = "lover"
        kid_name = "Terra"
        bro_name = "Aeron"

        bro_birth_year = 0
        bro_age = 0
        year6_have_baby = False
        year8_have_baby = False
        family12_shaved_head = False
        family27_no_work = False
        plays_trombone = False

        marriage_strength = 0

    # CHILD
    python:
        # CHILD STATS.
        # Amount of emotional intelligence, how loved and secure child feels
        attachment = 0
        # Reponsibility and ability to work hard, practical knowledge
        competence = 0
        # Confidence, autonomy
        independence = 0

        kid_work_slider = 0
        kid_other_work = 0

        sex_ed_biology = False
        sex_ed_commitment = False
        sex_ed_babycreation = False
        sex_ed_goodfeeling = False
        sex_ed_birthcontrol = False

        allowance_amount = 0


    # COMMUNITY
    python:
        is_liaison = False
        asked_only_medicine = False
        trade_with_mavericks = False
        invited_mavericks = False
        invited_miners = False
        whole_harvest_to_storehouse = False
        town_hall_games = False
        no_luxuries = False #used in community 8 and community 11
        # Community groups. The higher the variable, the better your relationship with that group is.
        colonists = 0
        miners = 0
        mavericks = 0
        jellies = 0
        require_whole_harvest = False
        rationing = False
        lily_mad_at_RET = False
        c18_no_help_pete = False
        ate_jellyfish = False
        thuc_has_cattle = False
        ilian_has_cattle = False
        thuc_sells_food = False
        cave_explored = False
        talked_to_Natalia = False
        talked_to_Thuc = False
        talked_to_Sara = False
        talked_to_Kevin = False
        talked_to_Pavel = False
        community_11_kidsonfarm = False
        community_17_planparty = False
        community_22_mining_stopped = False
        community_22_forced_mavericks_leave = False
        community_22_compromise = False
        community_22_mined_anyway = False
        touched_jellystar_25 = False
        jellypeople_happy = False
        kevin_elected = False
        ban_firegrass = False
        study_published_23 = False
        helen_dead = False

    # FARM
    python:
        year = 1
        earth_year = 1

        # Work/crops
        farm_size = 12
        farm = Field(farm_size, FARM_SIZE_MAXIMUM);
        selected_crop_index = 0

        # Yield of most recent set of crops, in percentages
        years_yield = [100] * farm_size

        # Dictionary containing the number of events seen for each crop
        number_events_seen = {"fallow":0, "corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "beans":0, "peanuts":0, "carrots":0, "turnips":0, "onions":0, "garlic":0, "spinach":0, "broccoli":0, "goats":0, "honey":0}
        credits = 0
        crop_info_index = 2  # This is the currently selected crop. It needs to be one that is valid at the beginning of the game.
        # Tuple containing the crop name, calories, nutrition, value, work, nitrogen_usage, currently enabled, persistent/perennial, pollinated, and maximum allowed.
        crop_info =     (#Name          CAL NUT VAL WK  NIT ENABLED PERRENIAL   POLL    MAX
                        ["fallow",       0, 0, 0, 0, Field.NITROGEN_FALLOW, True, False, False, 100],
                        ["corn",         9, 3, 7, 7, 50, False, False, False, 100],    # Grains/Starches
                        ["potatoes",     10, 4, 6, 6, 40, True, False, False, 100],
                        ["wheat",        9, 5, 8, 10, 20, False, False, False, 100],
                        ["peppers",      2, 7, 5, 5, 25, False, False, True, 100],    # "Fruits"
                        ["tomatoes",     3, 6, 6, 6, 15, True, False, True, 100],
                        ["plums",        3, 3, 7, 7, 5, False, True, True, 1],
                        ["plums+",       3, 3, 7, 2, 0, False, True, True, 0],    # Perennials are easier after year 1, but can't be moved
                        ["squash",       4, 6, 2, 4, 15, True, False, True, 100],
                        ["strawberries", 1, 2, 6, 4, 5, False, True, True, 1],
                        ["strawberries+",1, 2, 6, 2, 0, False, True, True, 0],
                        ["beans",        6, 6, 4, 7, -20, True, False, True, 100],   # Legumes
                        ["peanuts",      7, 8, 5, 8, -40, False, False, False, 100],
                        ["carrots",      3, 6, 3, 3, 10, True, False, False, 100],   # Root Vegetables
                        ["turnips",      3, 5, 1, 4, 10, False, False, False, 100],
                        ["onions",       4, 2, 5, 4, 5, False, False, False, 100],
                        ["garlic",       1, 3, 5, 2, 4, False, False, False, 100],
                        ["spinach",      1, 6, 3, 2, 10, True, False, False, 100],   # Leafy greens
                        ["broccoli",     3, 7, 2, 3, 15, False, False, False, 100],
                        ["goats",        8, 8, 9, 5, Field.NITROGEN_GOATS, True,  False, False, 1],   # Miscellaneous
                        ["honey",         2,  2,  8, 2, Field.NITROGEN_FALLOW, False, False, False, 1])
        crop_descriptions = {
            "fallow" : "Let this field rest to restore nitrogen and get rid of pests.",
            "corn" : "A starchy, versatile grain. Needs lots of nitrogen.",
            "potatoes" : "A starchy root vegetable with a lot of calories that doesn't take too much work.",
            "wheat" : "A nutritious grain, usually made into bread.",
            "peppers" : "A vegetable with lots of vitamins A and C. Can be spicy!",
            "tomatoes" : "A popular, versatile fruit useful raw or cooked.",
            "plums" : "A sweet fruit that can be dried into prunes or eaten raw. Grows on a tree that can't be moved.",
            "squash" : "This hearty vegetable keeps well and is easy to grow.",
            "strawberries" : "Small, sweet, and delicious! They come back every year.",
            "beans" : "These legumes are tough to harvest, but keep well and are very nutritious. They also fix nitrogen in the soil.",
            "peanuts" : "This legume takes hard work to harvest, shell, and boil, but keeps well and makes peanut butter.",
            "carrots" : "These crunchy root vegetables are healthy and easy to grow.",
            "turnips" : "These nutritious root vegetables are healthy, but not everyone likes them.",
            "onions" : "These useful bulb vegetables are good raw or cooked. They keep well, too.",
            "garlic" : "Their pungent flavor is versatile and sought after.",
            "spinach" : "This leafy vegetable is healthy and good for salads or cooking.",
            "broccoli" : "This vegetable is easy to grow and nutritious. You eat the flower buds and the stems!",
            "goats" : "Goats restore nitrogen, eat pests, and provide nutritious milk and meat.",
            "honey" : "Bees help pollinate flowering crops and provide valuable honey."
            }
        # Got rid of blueberries, snow peas, beets, garlic, cabbage

        total_calories = 0
        total_nutrition = 0
        total_value = 0
        total_work = 0

        current_work = 0

        overwork_count = 0
        overwork_colonists = 0
        overwork_miners = 0
        overwork_family = 0
        overwork_mavericks = 0
        overwork_self = 0

        bad_nutrition_count = 0
        seen_low_cam = False
        seen_low_ca = False
        seen_low_c = False
        seen_low_a = False
        seen_low_m = False

        year28_promised_potatoes = False

        # Crop event variables
        crop_temporarily_disabled = ""
        squash2_method = ""

    #######################################################################
    # Prologue
    #######################################################################
    $ change_cursor("default") # Reset to default cursor, just in case
    scene stars with fade
    $ _quit_slot = "quitsave"
    menu:
        "Demo":
            jump demo
        "Beta":
            $ pass
        "Testing":
            call tests

    "Welcome to the beta of Space to Grow! Please report any bugs/inconsistencies to andrea@icecavern.net. You can take a screenshot with the 's' key and attach it or just describe the bug."
    "Parts of this game deal with pregnancy loss, euthanasia, mental and physical disabilities, sexual education, and drug policies. We have tried to depict these situations sensitively."

    show path
    show her flirting at midleft
    show him happy at midright
    show child at center
    #show computer_pad
    show polaroid
    with dissolve

    if (mp.jack_name):
        $ his_name = mp.jack_name
    if (mp.kelly_name):
        $ her_name = mp.kelly_name
    if (mp.baby_name):
        $ kid_name = mp.baby_name
    "This is a pretty good family picture of us. There's my wife [her_name], looking gorgeous and sassy, as usual, and our daughter [kid_name]."
    "She's actually smiling in this picture, though we had to take thirty or so to get one good one." # TODO: show some of the outtakes
    "And me, of course. [his_name]. Though, these days I'm more often called 'Dad'."
    menu name_change_loop:
        "[his_name], [her_name], and [kid_name]... Are those names correct?"
        "Yes, continue.":
            $ pass
        "No, change names.":
            $his_name = renpy.input("Husband's Name", default=his_name)
            $her_name = renpy.input("Wife's Name", default=her_name)
            $kid_name = renpy.input("Baby girl's Name", default=kid_name)
            jump name_change_loop

    scene stars_animated with fade
    play music upbeat
    "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    "Of course, I knew it'd be a lot of work too. I thought I was ready for that."
    "But being a dad was a different kind of work than I had ever done before..."

    # TODO: show some sort of inter-scene screen

    # Introduction Scenes
    call family_intro
    call community_intro
    call work_intro

    scene stars with fade
    "In some ways, life was pretty repetitive. Planting and harvesting didn't change much from year to year."
    "But [kid_name] changed, and our community changed as new settlers arrived and situations changed."
    "I suppose I changed, too."

    #####################################################################
    # The Loop of Life                                                  #
    #####################################################################
label life_loop:
    while (year <= MAX_YEARS):
        $ save_name = "Year %d" % year
        $ earth_year = get_earth_years(year)

        # TODO: One time bro appeared in the transient and farm screens before he was born...?
        if (bro_birth_year != 0):
            $ bro_age = year - bro_birth_year

        # FARMING CHOICES
        $ renpy.random.shuffle(audio.computer)
        play music audio.computer fadein 2.0
        hide screen say
        #scene stars with fade
        if (year > 1):
            $ years_yield = farm.process_crops()
            # TODO: Right now, special events still modify credits, so you could start with a credit/debit. Is this what we want?
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
        call screen plan_farm with fade with fade

        label yearly_events:
            if demo_mode:
                jump demo_continue
            if trailer_mode:
                jump trailer_continue
            if testing_mode:
                jump test_continue
            $ notifications = ""
            $ current_work = get_work_available()
            $ total_work = farm.get_total_work()

            # MALNUTRITION EVENT (optional)
            if farm.low_vitamins():
                call bad_nutrition

            # WORK EVENTS (farming)
            play music farming fadeout 3.0 fadein 3.0
            call interscene_text(year, "Work")
            #show screen interscene(year, "Work") # with moveinleft #TODO: uncomment this with new version of Ren'Py
            # hide screen interscene #with dissolve
            $ work_event = get_next_work_event()
            call expression work_event

            # FAMILY EVENTS (parenting/home life)
            play music parenting fadeout 3.0 fadein 3.0
            call interscene_text(year, "Family")
            call expression "family" + str(year)

            # COMMUNITY EVENTS (building community, helping factions)
            play music community fadeout 3.0 fadein 3.0
            call interscene_text(year, "Community")
            call expression "community" + str(year)

            # Increase child stats based on this year's parenting decisions
            stop music fadeout 3.0
            call interscene_text(year, "End")
            call increase_attachment
            call increase_competence
            call increase_independence
            #$ renpy.notify(notifications)
            scene black with fade
            call screen yearly_summary with fade with fade

            # Reset our variables while keeping a running total
            $ total_demanding += demanding
            $ demanding = 0
            $ total_responsive += responsive
            $ responsive = 0
            $ total_confident += confident
            $ confident = 0

            # Autosave
            $ renpy.force_autosave(take_screenshot=True)
            $ renpy.notify("Autosaving...")

            $ year += 1
    jump ending
    return
