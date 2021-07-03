## Our Personal Space 2: Space to Grow
#  by Metasepia Games, http://metasepiagames.com
## MAIN
label start:

    # Initialize dynamic variables that need to be saved with saved game state.
    # These have to be here instead of in an init block to tell Ren'Py that they will change and should be saved with the game state.

    # GAME ENGINE
    default demo_mode = False
    default trailer_mode = False
    default testing_mode = False
    default save_name = "Intro"
    default notifications = ""
    default read_messages = False
    default read_handbook = False
    $ word_board = Board(basic_words, family_words, farm_words)
    default year11_poem = ""
    default year18_poem = ""
    default photos = []

    # PARENTS
    # Demanding and Reponsive may change by more or less than 1 each year
    # Positive indicates high expectations and reponsibilities for child; negative indicates indulgence and undiscpline
    # Max for each is about 30
    default demanding = 0
    # Positive indicates high emotional attachment and empathy; negative indicates aloofness and dismissiveness of child's feelings
    default responsive = 0
    # When you give your child opportunities to do things for herself, you show confidence in her. This increases her independence.
    default confident = 0
    # The Four Parenting Styles
    # Only one of these should be increased each year, maximum value at the end of the game is 30
    default authoritarian = 0
    default authoritative = 0
    default permissive = 0
    default neglectful = 0
    default trust = 0
    default parenting_style = "permissive"

    # Default names
    default his_name = "Jack"
    default her_name = "Kelly"
    default his_nickname = "dear"
    default her_nickname = "lover"
    default kid_name = "Terra"
    default bro_name = "Aeron"

    default bro_birth_year = 0
    # YEARS is Talaam time; AGE is Earth time
    default bro_years = -1
    default bro_age = -1
    default year6_have_baby = False
    default year8_have_baby = False
    default family12_shaved_head = False
    default family27_no_work = False
    default plays_trombone = False
    default parenting_classes = 0

    default marriage_strength = 0

    # CHILD
    # Amount of emotional intelligence, how loved and secure child feels
    default attachment = 0
    default total_attachment = 0
    # Reponsibility and ability to work hard, practical knowledge
    default competence = 0
    default total_competence = 0
    # Confidence, autonomy
    default independence = 0
    default total_independence = 0

    default kid_work_slider = 0
    default kid_other_work = 0

    default sex_ed_biology = False
    default sex_ed_commitment = False
    default sex_ed_babycreation = False
    default sex_ed_goodfeeling = False
    default sex_ed_birthcontrol = False

    default allowance_amount = 0

    # variables for boy relationships for Terra
    default boyfriend_name = ""
    default travis_points = 0
    default lorant_points = 0
    default oleg_points = 0

    default family30_leaving = True


    # COMMUNITY
    default met_jennings = False
    default met_grayson = False
    default met_kealoha = False
    default met_nguyen = False
    default met_andrevski = False
    default met_peron = False

    default is_liaison = False
    default asked_only_medicine = False
    default trade_with_mavericks = False
    default invited_mavericks = False
    default invited_miners = False
    default whole_harvest_to_storehouse = False
    default town_hall_games = False
    default no_luxuries = False #used in community 8 and community 11
    default lily_briefed = False #community 20, community 21, community 25, and community 27

    # Community groups. The higher the variable, the better your relationship with that group is.
    default total_colonists = 0
    default colonists = 0
    default total_miners = 0
    default miners = 0
    default total_mavericks = 0
    default mavericks = 0
    default jellies = 0 # TODO: we don't actually use this variable
    
    default require_whole_harvest = False
    default rationing = False
    default lily_mad_at_RET = False
    default c18_no_help_pete = False
    default ate_jellyfish = False
    default thuc_has_cattle = False
    default ilian_has_cattle = False
    default thuc_sells_food = False
    default cave_explored = False
    default talked_to_Natalia = False
    default talked_to_Thuc = False
    default talked_to_Sara = False
    default talked_to_Kevin = False
    default talked_to_Pavel = False
    default community11_kidsonfarm = False
    default community_17_planparty = False
    default community_22_mining_stopped = False
    default community_22_forced_mavericks_leave = False
    default community_22_compromise = False
    default community_22_mined_anyway = False
    default touched_jellystar_25 = False
    default no_euthanasia_26 = False
    default jellypeople_happy = False
    default kevin_elected = False
    default ban_firegrass = False
    default study_published_23 = False
    default helen_dead = False
    default bought_tt = False
    default c_end = ""
    $ bios = Bios()
    $ bios.activate("[his_name]")
    $ bios.activate("[her_name]")
    $ bios.activate("[kid_name]")
    default show_person = "Thuc"

    # FARM
    default year = 1
    default earth_year = 1

    # Work/crops
    default farm_size = 12
    if (persistent.times_beaten):
        $ farm_size = min(12 + (persistent.times_beaten*2), FARM_SIZE_MAXIMUM)
    default farm = Field(farm_size, FARM_SIZE_MAXIMUM)
    default selected_crop_index = 0
    default terra_overwork_count = 0
    default sortby = "calories"
    default show_sort = False

    # Yield of most recent set of crops, in percentages
    default credits = 0
    default years_yield = [100] * farm_size
    default annual_expenses_base = 2500
    default debt_consecutive_years = 0
    default debt_event_count = 0
    default seen_miners_debt = False
    default seen_mavericks_debt = False
    default seen_colonists_debt = False
    default low_calories_count = 0

    default number_events_seen = {}
    default crop_info = ()


    python:
        # Dictionary containing the number of events seen for each crop
        number_events_seen = {"fallow":0, "corn":0, "potatoes":0, "wheat":0, "peppers":0, "tomatoes":0, "plums":0, "squash":0, "strawberries":0, "beans":0, "peanuts":0, "carrots":0, "turnips":0, "onions":0, "garlic":0, "spinach":0, "broccoli":0, "goats":0, "honey":0, "money":0}
        crop_info_index = 2  # This is the currently selected crop. It needs to be one that is valid at the beginning of the game.

        # Tuple containing the crop name, calories, nutrition, value, work, nitrogen_usage, currently enabled, persistent/perennial, pollinated, and maximum allowed.
        crop_info =     (#Name          CAL VA VC VM VAL WK  NIT ENABLED PERRENIAL   POLL    MAX
                        ["fallow",       0, 0, 0, 0, 0, 0, Field.NITROGEN_FALLOW, True, False, False, 100],
                        ["corn",         10, 3, 2, 2, 7, 7, 50, False, False, False, 100],    # Grains/Starches
                        ["potatoes",     10, 0, 6, 2, 6, 6, 40, True, False, False, 100],
                        ["wheat",        10, 5, 5, 7, 9, 9, 20, False, False, False, 2],
                        ["peppers",      2, 2, 9, 1, 5, 5, 25, False, False, True, 100],    # "Fruits"
                        ["tomatoes",     3, 3, 4, 1, 6, 6, 15, True, False, True, 100],
                        ["plums",        3, 1, 1, 1, 7, 7, 15, False, True, True, 1],
                        ["plums+",       3, 1, 1, 1, 7, 2, 0, False, True, True, 0],    # Perennials are easier after year 1, but can't be moved
                        ["squash",       4, 8, 3, 2, 2, 4, 15, True, False, True, 100],
                        ["strawberries", 1, 0, 2, 0, 6, 4, 15, False, True, True, 1],
                        ["strawberries+",1, 0, 2, 0, 6, 2, 0, False, True, True, 0],
                        ["beans",        6, 0, 0, 6, 4, 7, -20, True, False, True, 100],   # Legumes
                        ["peanuts",      7, 0, 0, 6, 5, 8, -40, False, False, False, 100],
                        ["carrots",      3, 10, 1, 0, 3, 3, 10, True, False, False, 100],   # Root Vegetables
                        ["turnips",      3, 0, 6, 1, 1, 4, 10, False, False, False, 100],
                        ["onions",       4, 0, 3, 1, 5, 4, 5, False, False, False, 100],
                        ["garlic",       1, 0, 7, 2, 5, 2, 4, False, False, False, 2],
                        ["spinach",      1, 6, 3, 2, 3, 2, 10, True, False, False, 100],   # Leafy greens
                        ["broccoli",     3, 2, 10, 1, 2, 3, 15, False, False, False, 100],
                        ["goats",        8, 1, 0, 1, 9, 5, Field.NITROGEN_GOATS, True,  False, False, 1],   # Miscellaneous
                        ["honey",        2, 0, 0, 0, 8, 2, Field.NITROGEN_FALLOW, False, False, False, 1])
        crop_descriptions = {
            "fallow" : "Let this field rest to restore nitrogen.",
            "corn" : "A starchy, versatile grain. Needs lots of nitrogen.",
            "potatoes" : "A starchy root vegetable with a lot of calories that doesn't take too much work.",
            "wheat" : "A nutritious grain, usually made into bread.",
            "peppers" : "A vegetable with lots of vitamins A and C. Can be spicy!",
            "tomatoes" : "A juicy, versatile fruit; can be eaten raw or cooked.",
            "plums" : "A sweet fruit that can be dried into prunes or eaten raw. Grows on a tree that can't be moved.",
            "squash" : "This hearty vegetable keeps well and is easy to grow.",
            "strawberries" : "Small, sweet, and tangy! They come back every year.",
            "beans" : "These legumes are tough to harvest, but keep well and are very nutritious. They fix nitrogen in the soil.",
            "peanuts" : "This legume takes hard work to harvest, shell, and boil. Fixes nitrogen in the soil.",
            "carrots" : "These crunchy root vegetables are full of vitamin A and easy to grow.",
            "turnips" : "These nutritious root vegetables are healthy, but not everyone likes them.",
            "onions" : "These useful bulb vegetables are good raw or cooked. They keep well, too.",
            "garlic" : "Their pungent flavor is versatile and sought after.",
            "spinach" : "This leafy vegetable is healthy and good for salads or cooking.",
            "broccoli" : "This vegetable is easy to grow and full of vitamin C. Eat the flower buds and the stems!",
            "goats" : "Goats restore nitrogen, eat pests, and provide calorie-dense milk and meat.",
            "honey" : "Bees help pollinate flowering crops and provide valuable honey."
            }

    default total_calories = 0
    default total_nutrition = 0
    default total_value = 0
    default total_work = 0
    default current_work = 0

    default overwork_count = 0
    default overwork_colonists = 0
    default overwork_miners = 0
    default overwork_family = 0
    default overwork_mavericks = 0
    default overwork_self = 0

    default bad_nutrition_count = 0
    default seen_low_cam = False
    default seen_low_ca = False
    default seen_low_c = False
    default seen_low_a = False
    default seen_low_m = False

    default work8_choice = ""
    default year28_promised_potatoes = False

    # Crop event variables
    default crop_temporarily_disabled = ""
    default squash2_method = ""

    #######################################################################
    # Prologue
    #######################################################################
    scene stars with fade
    $ _quit_slot = "quitsave"
    # menu:
    #     "Beta":
    #         $ pass
    #     "Testing":
    #         jump tests

    # TODO: Take this out when beta testing is over
    "Welcome to the beta of Space to Grow! Please report any bugs/inconsistencies/typos to andrea@icecavern.net. You can take a screenshot with the 's' key and attach it or just describe the bug."

    if (persistent.times_beaten):
        "Welcome back to Space to Grow! Since you've played it before, you can use the Skip button to skip past text you've already seen. We'll also increase your starting farm size and enable crops you've unlocked."
        if (persistent.crops_unlocked):
            $ i = 0
            while (i < len(crop_info)):
                if crop_info[i][NAME_INDEX] in persistent.crops_unlocked:
                    $ enable_crop(crop_info[i][NAME_INDEX], False)
                $ i += 1
        "Choices you've made before will show up in italics so you can decide if you want to see something different."
        "Unavailable choices will show up crossed out so you can see what they are."
        $ renpy.hide_screen("show_notification") #Just in case this got stuck on or something

    else:
        "Parts of this game deal with pregnancy loss, euthanasia, mental and physical disabilities, sexual education, and drug policies. We have tried to depict these situations sensitively."
        if (not mp.jack_name):
            "If you haven't played Our Personal Space 1, it's available for free at http://www.metasepiagames.com and takes place right before this game. You don't have to have played it to enjoy Space to Grow."
        if (not renpy.mobile):
            "You can press the ESC key or right-click at any time to bring up the menu to change options or save your game."
            "If you miss something, you can scroll backwards and forwards using the mousewheel."
        else:
            "You can use the tab at the right to bring up more options, like auto advance, preferences, and a conversation log."

    scene stars with fade
    show familyphoto0 at center, baby_pos with dissolve

    if (mp.jack_name):
        $ his_name = mp.jack_name
    if (mp.kelly_name):
        $ her_name = mp.kelly_name
    if (mp.baby_name):
        $ kid_name = mp.baby_name

    "Thirty years ago, when [kid_name] was first born, I had no idea what I was getting into."
    "Thirty years sounds like a long time, but because our planet's rotation is different from Earth's, that's only about eighteen Earth years."
    "This is a pretty good family picture of us. There's my wife [her_name], looking gorgeous and sassy, as usual, and our daughter [kid_name]. Though she's much older now."
    "[kid_name]'s actually smiling in this picture, though I remember it took us a long time to get one good one."
    scene stars with fade
    show familyphoto1 at tinyphoto, left, tilted, baby_pos with moveinright
    $ renpy.pause(0.2)
    show familyphoto2 at tinyphoto, center, baby_pos with moveinright
    $ renpy.pause(0.2)
    show familyphoto3 at tinyphoto, right, tilted, baby_pos with moveinright
    "Last, there's me, of course. [his_name]. Though, she usually calls me 'Dad', even now."
    menu name_change_loop:
        "[his_name], [her_name], and [kid_name]... Are those names correct?"
        "Yes, continue.":
            $ pass
        "No, change names.":
            $his_name = renpy.input("Husband's Name", default=his_name)
            $her_name = renpy.input("Wife's Name", default=her_name)
            $kid_name = renpy.input("Baby girl's Name", default=kid_name)
            jump name_change_loop

    $ bios.changeName("[his_name]", his_name)
    $ bios.changeName("[her_name]", her_name)
    $ bios.changeName("[kid_name]", kid_name)

    scene stars_animated with fade
    play music upbeat
    "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    "Of course, I knew it'd be a lot of work too. I thought I was ready for that."
    "But being a dad was a different kind of work than I had ever done before."

    # Introduction Scenes
    call family_intro from _call_family_intro
    call community_intro from _call_community_intro
    call work_intro from _call_work_intro

    scene stars with fade

    #####################################################################
    # The Loop of Life                                                  #
    #####################################################################
label life_loop:
    while (year <= MAX_YEARS):
        $ save_name = "Year %d" % year
        $ earth_year = get_earth_years(year)

        if (bro_birth_year != 0):
            $ bro_years = year - bro_birth_year
            $ bro_age = get_earth_years(year - bro_birth_year)

        # FARMING CHOICES
        $ renpy.random.shuffle(audio.computer)
        play music audio.computer fadein 2.0
        hide screen say
        #scene stars with fade
        if (year > 1):
            $ years_yield = farm.process_crops()
            if (year > MONEY_YEAR):
                $ income = farm.calculate_income(years_yield)
                if (income < get_expenses_required(year-1)):
                    $ debt_consecutive_years += 1
                $ modify_credits(income, False)
                $ modify_credits(-(get_expenses_required(year-1) - KELLY_SALARY), False) # We want this for the PREVIOUS year.
                if (allowance_amount != 0):
                    $ modify_credits(-allowance_amount * 7)

                # Check for credit Achievements
                if (credits >= 2000):
                    $ achieved("Rich Dad")
                elif (credits <= -1000):
                    $ achieved("Poor Dad")

        if (crop_enabled("wheat")):
            $ modify_credits(-WHEAT_COST)

        # TUTORIALS FOR NEW STUFF
        if (year == MONEY_YEAR):
            "I now earn credits for the crops I choose, after deductions for expenses."
            scene tutorial-credits with fade
            "This part of the screen shows how much I'll earn and how much my expenses are."
            "Hopefully I can stay out of debt..."
        if (year == KID_WORK_YEAR):
            "[kid_name] is old enough to start helping on the farm."
            scene tutorial-kid-work with fade
            "I can choose how much she should work on the farm. The more she works, the more total Work we will have for crops on the farm. The more competent she is, the more efficient her work will be."
        $ farm.reset_crops(farm_size)
        $ read_messages = False
        $ read_handbook = False
        $ show_year = year

        # Autosave
        $ renpy.block_rollback()
        $ renpy.force_autosave(take_screenshot=True)
        $ renpy.notify("Autosaving...")

        call screen plan_farm() with fade

        label yearly_events:
            $ renpy.block_rollback()
            scene stars
            if demo_mode:
                jump demo_continue
            if trailer_mode:
                jump trailer_continue
            if testing_mode:
                jump test_continue
            $ notifications = ""
            $ current_work = get_work_available()
            $ total_work = farm.get_total_work()

            # Achievement for planting mostly potatoes
            if (farm.crops.count("potatoes") >= (farm.crops.len() - 4)):
                $ achieved("Potato Papa")

            play music farming fadeout 3.0 fadein 3.0

            # LOW CALORIES EVENT (optional)
            if (farm.low_calories()):
                call low_calories from _call_low_calories

            # MALNUTRITION EVENT (optional)
            if farm.low_vitamins():
                call bad_nutrition from _call_bad_nutrition

            # Debt event if your credits have decreased for 3
            # years in a row and your credits are < -100
            if ((debt_consecutive_years >= 3) and (credits < -100)):
                call debt_event from _call_debt_event

            # Terra work events (optional)
            if ((year > TODDLER_MAX) and (kid_work_slider >= 70)):
                $ probability = 4/3.0*kid_work_slider - 80
                if (renpy.random.random() < probability/100.0):
                    $ next_event = terra_overwork_count + 1
                    $ event_label = "terra_overwork" + str(next_event)
                    if renpy.has_label(event_label):
                        call expression event_label from _call_expression

            # WORK EVENTS (farming)
            call interscene_text(year, "Work") from _call_interscene_text
            $ work_event = get_next_work_event()
            call expression work_event from _call_expression_1

            # FAMILY EVENTS (parenting/home life)
            play music parenting fadeout 3.0 fadein 3.0
            call interscene_text(year, "Family") from _call_interscene_text_1
            call expression "family" + str(year) from _call_expression_2

            # COMMUNITY EVENTS (building community, helping factions)
            play music community fadeout 3.0 fadein 3.0
            #show screen interscene(year, "Community")
            call interscene_text(year, "Community") from _call_interscene_text_2
            call expression "community" + str(year) from _call_expression_3

            # Increase child stats based on this year's parenting decisions
            stop music fadeout 3.0
            scene stars
            window hide
            call increase_stats from _call_increase_stats

            $ parenting_style = get_parenting_style()
            call screen yearly_summary with slowfade

            # Reset our variables for a new year while keeping a running total
            call reset_variables from _call_reset_variables

            if (year == BABY_MAX):
                scene stars with fade
                show text "End Baby Years"
                $ renpy.pause(1.5)
                show baby_cg
                $ renpy.pause(6.0)
                $ renpy.pause()

            if (year == TODDLER_MAX):
                scene stars with fade
                show text "End Toddler Years"
                $ renpy.pause(1.5)
                show toddler_cg
                $ renpy.pause(6.0)
                $ renpy.pause()

            if (year == CHILD_MAX):
                scene stars with fade
                show text "End Childhood Years"
                $ renpy.pause(1.5)
                show child_cg
                $ renpy.pause(6.0)
                $ renpy.pause()

            if (year == TWEEN_MAX):
                scene stars with fade
                show text "End Tween Years"
                $ renpy.pause(1.5)
                show tween_cg
                $ renpy.pause(6.0)
                $ renpy.pause()

            if (year == YTEEN_MAX):
                scene stars with fade
                show text "End Young Teen Years"
                $ renpy.pause(1.5)
                show yteen_cg
                $ renpy.pause(6.0)
                $ renpy.pause()

            $ year += 1
            if (persistent.max_year < year):
                $ persistent.max_year = year
                $ renpy.save_persistent()
            scene stars
            $ renpy.hide_screen("show_notification") #Just in case this got stuck on or something

    jump ending
    return
