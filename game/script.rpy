## Our Personal Space 2
## MAIN

## The game starts here.
#
# TODO: Add parenting class tutorial near the beginning
# TODO: Warn halfway for bad/inconsistent parenting?
# TODO: Use scene stars instead of scene black most of the time?
##

label start:

    # Initialize dynamic variables that need to be saved with saved game state.
    # These have to be here instead of in an init block to tell Ren'Py that they will change and should be saved with the game state.

    # GAME ENGINE
    python:
        save_name = "Intro"
        notifications = ""

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

        # TODO: have a trust/honesty variable keeping track of how consistent/honest you are?

        # The Four Parenting Styles
        # Only one of these should be increased each year, maximum value at the end of the game is 30
        authoritarian = 0
        authoritative = 0
        permissive = 0
        neglectful = 0
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
        family27_no_work = False
        plays_saxophone = False

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

        sex_ed_biology = False
        sex_ed_commitment = False
        sex_ed_babycreation = False
        sex_ed_goodfeeling = False
        sex_ed_birthcontrol = False

        allowance_amount = 0


    # COMMUNITY
    python:
        is_liason = False
        asked_only_medicine = False
        trade_with_luddites = False
        invited_luddites = False
        invited_miners = False
        whole_harvest_to_storehouse = False
        town_hall_games = False
        no_luxuries = False #used in community 8 and community 11
        # Community groups. The higher the variable, the better your relationship with that group is.
        colonists = 0
        miners = 0
        luddites = 0
        jellies = 0
        require_whole_harvest = False
        rationing = False
        lily_mad_at_RET = False
        c18_no_help_pete = False
        ate_jellyfish = False
        thuc_has_cattle = False
        ilian_has_cattle = False
        thuc_sells_food = False
        community_22_mining_stopped = False
        community_22_forced_luddites_leave = False
        community_22_compromise = False
        community_22_mined_anyway = False

    # FARM
    python:
        year = 1
        earth_year = 1

        # Work/crops
        farm_size = 12
        farm = Field(farm_size, MAX_FARM_SIZE);
        selected_crop_index = 0

        # Yield of most recent set of crops, in percentages
        years_yield = [100] * farm_size

        # Dictionary containing the number of events seen for each crop
        number_events_seen = {"fallow":0, "corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "blueberries":0, "beans":0, "snow peas":0, "peanuts":0, "carrots":0, "beets":0, "turnips":0, "onions":0, "garlic":0, "cabbage":0, "spinach":0, "broccoli":0, "goats":0}
        # TODO: add income
        # TODO: make it so you can't move perennials once placed
        crop_info_index = 1  # This is the currently selected crop. It needs to be one that is valid at the beginning of the game.
        # Tuple containing the crop name, calories, nutrition, value, work, nitrogen_usage, currently enabled, persistent/perennial, and maximum allowed.
        crop_info =     (
                        ["fallow",       0, 0, 0, 0, Field.NITROGEN_FALLOW, True, False, 100],
                        ["corn",         9, 5, 8, 7, 50, False, False, 100],    # Grains
                        ["potatoes",     10, 5, 7, 6, 40, True, False, 100],
                        ["wheat",        9, 5, 9, 10, 20, False, False, 100],
                        ["peppers",      2, 7, 5, 5, 25, False, False, 100],    # "Fruits"
                        ["tomatoes",     3, 6, 6, 6, 15, True, False,  100],
                        ["plums",        3, 3, 8, 7, 5, False, True, 1],
                        ["plums+",       3, 3, 8, 2, 0, False, True, 1],    # Perennials are easier after year 1, but can't be moved
                        ["squash",       4, 5, 3, 4, 15, True, False, 100],
                        ["strawberries", 1, 2, 8, 6, 5, False, True, 2],
                        ["strawberries+",1, 2, 8, 5, 0, False, True, 2],
                        ["blueberries",  2, 3, 9, 9, 5, False, True, 2],
                        ["blueberries+", 2, 3, 9, 4, 0, False, True, 2],
                        ["beans",        6, 8, 4, 7, -20, True, False, 100],   # Legumes
                        ["snow peas",    3, 6, 3, 4, -35, False, False, 100],
                        ["peanuts",      7, 8, 5, 8, -50, False, False, 100],
                        ["carrots",      3, 6, 4, 4, 10, True, False,  100],   # Root Vegetables
                        ["beets",        3, 4, 2, 3, 5, False, False, 100],
                        ["turnips",      3, 5, 1, 4, 10, False, False, 100],
                        ["onions",       4, 2, 7, 4, 5, False, False, 100],
                        ["garlic",       3, 3, 7, 4, 5, False, False, 100],
                        ["cabbage",      2, 4, 3, 3, 15, False, False, 100],   # Leafy greens
                        ["spinach",      1, 6, 4, 3, 10, True, False,  100],
                        ["broccoli",     3, 5, 4, 3, 15, False, False, 100],
                        ["goats",        8, 10, 10, 5, Field.NITROGEN_GOATS, True,  False, 1],   # Miscellaneous
                        ["bees",         2,  2,  8, 3, 0, False, True, 1])
                        #TODO: have an axe crop that can only be placed on perennials to chop them down?
        crop_descriptions = {
            "fallow" : "Let this field rest to restore nitrogen and get rid of pests.",
            "corn" : "A starchy, versatile grain. Needs lots of nitrogen.",
            "potatoes" : "A starchy root vegetable with a lot of calories that doesn't take too much work.",
            "wheat" : "A nutritious grain, usually made into bread.",
            "peppers" : "A vegetable with lots of vitamins A and C. Can be spicy!",
            "tomatoes" : "A juicy, acidic fruit useful raw, in sauces, or salsas.",
            "plums" : "A sweet fruit that can be dried into prunes or eaten raw. Grows on a tree that can't be moved.",
            "squash" : "This vegetable keeps well and is easy to grow.",
            "strawberries" : "Small, sweet, and delicious! They come back every year.",
            "blueberries" : "Tiny and delicious; useful for jam or eating raw. These will come back every year.",
            "beans" : "These legumes are tough to harvest, but keep well and are very nutritious.",
            "snow peas" : "These crunchy legumes are good raw or lightly cooked.",
            "peanuts" : "This legume takes hard work to harvest, shell, and boil, but keeps well and makes peanut butter.",
            "carrots" : "These crunchy root vegetables are healthy and easy to grow.",
            "beets" : "These purple root vegetables will grow almost anywhere.",
            "turnips" : "These nutritious root vegetables are healthy, but not everyone likes them.",
            "onions" : "These useful bulb vegetables are good raw or cooked. They keep well, too.",
            "garlic" : "This bulb makes everything taste better.",
            "cabbage" : "Eat it raw, cooked, or fermented. Easy to grow.",
            "spinach" : "This leafy vegetable is healthy and good for salads or cooking.",
            "broccoli" : "This vegetable is easy to grow and nutritious. You eat the flower buds and the stems!",
            "goats" : "Goats restore nitrogen, eat weeds, and provide milk (and sometimes meat).",
            "bees" : "Bees help pollinate crops and provide honey, which sells for a high price."
            }

        total_calories = 0
        total_nutrition = 0
        total_value = 0
        total_work = 0

        current_work = 0

        # Crop event variables
        carrots_fallow = False

    #######################################################################
    # Prologue
    #######################################################################
    $ change_cursor("default") # Reset to default cursor, just in case
    scene stars with fade
    if (mp.his_name):
        $ his_name = mp.jack_name
        $ her_name = mp.kelly_name
        if (mp.kid_name):
            $ kid_name = mp.baby_name

    show path
    show her normal at midleft
    show kid happy at centerbaby
    show him normal at midright
    show computer_pad
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
        "Test Farming Screen":
            $ farm.reset_crops(farm_size)
            call screen plan_farm
        "Other Tests":
            jump tests

    scene stars_animated with fade
    "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    "Of course, I knew it'd be a lot of work too. I thought I was ready for that."
    "But being a dad was a different kind of work than I had ever done before."
    "If I could go back, would I change anything? I don't even know."
    "When [kid_name] was first born, it was a struggle just to get through each day..."

    # TODO: show some sort of inter-scene screen

    # Introduction Scenes
    call family_intro
    call work_intro
    call community_intro

    # Initial farm setup
    #play music computer
    scene gray_dark with fade
    $ farm.reset_crops(farm_size)
    call screen plan_farm
    $ current_work = get_work_available()
    $ total_work = farm.get_total_work()

    stop music
    "In some ways, life was pretty repetitive. Planting and harvesting didn't change much from year to year."
    "But [kid_name] changed, and our community changed as new settlers arrived and situations changed."
    "I suppose I changed, too."

    #####################################################################
    # The Loop of Life                                                  #
    #####################################################################
    while (year <= MAX_YEARS):
        $ earth_year = get_earth_years(year)

        if (bro_birth_year != 0):
            $ bro_age = year - bro_birth_year

        # WORK EVENTS (farming)
        #play music farming
        call interscene_text(year, "Work")
        #show screen interscene(year, "Work") # with moveinleft #TODO: uncomment this with new version of Ren'Py
        # hide screen interscene #with dissolve
        $ work_event = get_next_work_event()
        call expression work_event

        # FAMILY EVENTS (parenting/home life)
        #play music parenting
        call interscene_text(year, "Family")
        call expression "family" + str(year)

        # COMMUNITY EVENTS (building community, helping factions)
        #play music community
        call interscene_text(year, "Community")
        call expression "community" + str(year)

        # Increase child stats based on this year's parenting decisions
        $ notifications = ""
        scene stars with fade
        call increase_attachment
        call increase_competence
        call increase_independence
        $ renpy.notify(notifications)
        "The year passed by like a dream..."

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

        # Poetry time!
        #if (year % 3):
        "So much happened this year... I decided to write a poem about it."
        # Make the word board with appropriate words
        # TODO: Store poems better for later access.
        $ word_board = Board(basic_words, family_words, farm_words)
        call make_poem

        # CHOOSE FOR NEXT YEAR
        #play music computer
        hide screen say
        scene gray_dark with fade
        $ years_yield = farm.process_crops()
        $ farm.reset_crops(farm_size)
        call screen plan_farm
        $ current_work = get_work_available()
        $ total_work = farm.get_total_work()
        $ year += 1
        $ save_name = "Year %d" % year

    return
