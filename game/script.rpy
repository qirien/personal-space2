## Our Personal Space 2
## MAIN

## The game starts here.
#
# TODO: Add parenting class tutorial near the beginning
# TODO: Parenting variables for each style, detect inconsistent parenting. Warn halfway.
# TODO: Make variables more object oriented?
# TODO: Make inter-scene screens overlays coming in the upper left corner to make the interface take less time and be less annoying?
# TODO: Use "window hide" and "window show" during interscene screens if needed

label start:
    
    # Initialize dynamic variables that need to be saved with saved game state.
    # These have to be here instead of in an init block to tell Ren'Py that they will change and should be saved with the game state.
    
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
        
        # The Four Parenting Styles
        # Only one of these should be increased each year (each type of event?)
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
        
        marriage_strength = 0
        
    # CHILD    
    python:
        # CHILD STATS. Maximum at end-game is 30.
        # Amount of emotional intelligence, how loved and secure child feels
        attachment = 0
        # Reponsibility and ability to work hard, practical knowledge
        competence = 0
        # Confidence, autonomy
        independence = 0
        
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
        # Community groups. The higher the variable, the better your relationship with that group is.
        colonists = 0
        miners = 0
        luddites = 0
        jellies = 0    
        
    # FARM
    python:
        year = 1
        earth_year = 1
        
        # Work/crops
        farm_size = 16
        crops = []
        test_crops = [    "potatoes", "potatoes", "beans", "beans", 
                            "carrots", "carrots", "spinach", "spinach", 
                            "goats", "squash", "squash", "squash", 
                            "potatoes", "potatoes", "", ""]
        crop_index = 0
        # Dictionary containing the number of events seen for each crop 
        number_events_seen = {"corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "blueberries":0, "beans":0, "snow peas":0, "peanuts":0, "carrots":0, "beets":0, "turnips":0, "onions":0, "garlic":0, "cabbage":0, "spinach":0, "broccoli":0, "goats":0}
        # Tuple containing the crop name, calories, nutrition, fun, and work (scale of 0-10).  Also whether the crop is currently enabled or not.
        # TODO: add income
        # TODO: add limits to maximum amount allowed
        crop_index = 1
        crop_info = (["corn",         8, 4, 8, 7, False, 100],    # Grains
                            ["potatoes",     8, 5, 7, 6, True,  100],
                            ["wheat",        8, 6, 8, 10,False, 100],
                            ["peppers",      2, 6, 5, 5, False, 100],    # "Fruits"
                            ["tomatoes",     3, 5, 6, 6, True,  100],
                            ["plums",        3, 3, 8, 7, False, 1],
                            ["plums+",       3, 3, 8, 2, False, 1],    # Perennials are easier after year 1
                            ["squash",       4, 5, 5, 4, True,  100],
                            ["strawberries", 1, 3, 7, 6, False, 2],
                            ["strawberries+",1, 3, 7, 6, False, 2],
                            ["blueberries",  3, 3, 9, 9, False, 2],
                            ["blueberries+", 3, 3, 9, 4, False, 2],
                            ["beans",        6, 7, 2, 7, True,  100],   # Legumes
                            ["snow peas",    3, 5, 2, 4, False, 100],
                            ["peanuts",      7, 6, 5, 8, False, 100],
                            ["carrots",      3, 5, 4, 4, True,  100],   # Root Vegetables
                            ["beets",        3, 4, 4, 4, False, 100],
                            ["turnips",      3, 5, 3, 4, False, 100],
                            ["onions",       4, 3, 7, 4, False, 100],
                            ["garlic",       3, 4, 7, 4, False, 100],
                            ["cabbage",      2, 4, 4, 3, False, 100],   # Leafy greens
                            ["spinach",      3, 6, 4, 4, True,  100],
                            ["broccoli",     3, 5, 3, 3, False, 100],
                            ["goats",       10, 7, 7, 5, True,  1])   # Miscellaneous        
        
        total_calories = 0
        total_nutrition = 0
        total_fun = 0
        total_work = 0
        
        # Crop event variables
        carrots_fallow = False
           
    # Prologue
    scene stars with fade
    if (mp.his_name):
        $ his_name = mp.jack_name
        $ her_name = mp.kelly_name
        if (mp.kid_name):
            $ kid_name = mp.baby_name           
        
    show path
    show her normal at midleft
    show kid at center
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
        
    scene stars_animated with fade                
    show him happy
    him "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    him normal "Of course, I knew it'd be a lot of work too. But, like most hard work, I figured it'd be worth it."
    him "Even now that you're grown, I still think about your childhood."
    him concerned "Was I there for you? Did I do enough? Was I the dad you needed?"
    him normal "If I could go back, would I change anything? I don't even know."
    him "When you were first born, it was a struggle just to get through each day."  
    
    # TODO: show some sort of inter-scene screen

    # Introduction Scenes
    call family_intro
    call work_intro
    call community_intro    
    
    # Initial farm setup
    $ crops = [""] * farm_size
    call screen plan_farm
    
    scene stars with fade
    "In some ways, life was pretty repetitive. Planting and harvesting didn't change much from year to year."
    "But you changed, [kid_name], and our community changed as new settlers arrived and situations changed."
    "I suppose I changed, too."
    
    #####################################################################    
    # The Loop of Life                                                  #
    #####################################################################
    
    while (year <= 30):
        $ earth_year = get_earth_years(year)
        
        if (bro_birth_year != 0):
            $ bro_age = year - bro_birth_year            
        
        # WORK EVENTS (farming)
        window hide
        scene black with fade
        centered "Year [year]\n\nWork"
        scene black with fade        
        $ work_event = get_next_work_event()
        window show        
        call expression work_event
        
        # FAMILY EVENTS (parenting/home life)
        window hide
        scene black with fade
        centered "Year [year]\n\nFamily"
        scene black with fade
        window show
        call expression "family" + str(year)
        
        # COMMUNITY EVENTS (building community, helping factions)
        window hide
        scene black with fade
        centered "Year [year]\n\nCommunity"
        scene black with fade
        window show
        call expression "community" + str(year)
        
        # Increase child stats based on this year's parenting decisions
        call increase_attachment
        call increase_competence
        call increase_independence

        # Reset our variables while keeping a running total
        $ total_demanding += demanding
        $ demanding = 0
        $ total_responsive += responsive
        $ responsive = 0        
        
        # Autosave
        $ renpy.force_autosave(take_screenshot=True)
        $ renpy.notify("Autosaving...")
        # CHOOSE FOR NEXT YEAR
        
        $ crops = [""] * farm_size
        call screen plan_farm
        
        $ year += 1
   
    return