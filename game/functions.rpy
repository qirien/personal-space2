# Library of functions we call that have to do with game variables, etc.

# Add arguments to hyperlinks by overloading the hyperlink_clicked function
init python:

    def actionHyperlinkHandler(action_string):
        #print action_string
        return renpy.python.py_eval("renpy.run({})".format(action_string))

    config.hyperlink_handlers.update({"action": actionHyperlinkHandler})

##
# Menu Randomization
##

# we could change this to True to start shuffling menus
default shuffle_menu = False
init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        if (shuffle_menu):
            renpy.random.shuffle(items)
        return renpy_menu(items)

##
# Return the value bounded by min and max
##
init python:
    def bounded_value(val, min=0, max=100):
        if (val > max):
            return max
        elif (val < min):
            return min
        else:
            return val

init python:
    def random_float():
        return renpy.random.random()
    
    def random_int(min, max):
        return renpy.random.randint(min, max)

    def notification_add(var_name, amount):
        global notifications
        message = ""
        if (amount == 0):
            return
        elif (amount > 0):
            message += var_name + "{color=" + green_dark + "} +"
        else:
            message += var_name + "{color=" + red_dark + "} "
        message += str(amount) + "{/color}\n"

        notifications += message
        return

label reset_variables:
    $ total_attachment += attachment
    $ total_competence += competence    
    $ total_independence += independence  
    $ demanding = 0
    $ responsive = 0
    $ confident = 0
    $ attachment = 0
    $ competence = 0
    $ independence = 0

    # Community stats
    $ total_colonists += colonists
    $ total_mavericks += mavericks
    $ total_miners += miners
    $ colonists = 0
    $ mavericks = 0
    $ miners = 0

    #Have a minimum of 0 so you don't get too in the hole.
    if (total_colonists < 0):
        $ total_colonists = 0
    if (total_mavericks < 0):
        $ total_mavericks = 0
    if (total_miners < 0):
        $ total_miners = 0
    return

##
# PARENTING FUNCTIONS
##
label increase_stats:
    # Child stats
    call increase_attachment from _call_increase_attachment
    call increase_competence from _call_increase_competence
    call increase_independence from _call_increase_independence 
    return

# Increase attachment based on how responsive you were last year
label increase_attachment:
    $ inc_amount = 0
    $ inc_amount += responsive
    $ attachment += inc_amount
    return

# Increase competence based on how demanding you were last year
# and how much Terra worked
label increase_competence:
    $ inc_amount = 0
    # Sometimes increase competence with a probability proportional to how much they work. Use the equation probability = work^2/200
    if (renpy.random.random() <= (kid_work_slider*kid_work_slider/200.0/100.0)):
        $ inc_amount += 1
    $ inc_amount += demanding
    $ competence += inc_amount
    return

# Increase independence based on how much confidence you showed in her last year
label increase_independence:
    $ inc_amount = 0
    $ inc_amount += confident
    $ independence += inc_amount
    return

##
# Set things up for a scene in the bedroom
##
label bedroom_scene(show_baby=False, sleeping=True):
    scene bedroom with fade
    if (sleeping):
        show him sleeping at midleft, squatting
        show her sleeping at midright, squatting
    else:
        show him normal at midleft, squatting
        show her normal at midright, squatting
    if (show_baby):
        show kid normal at centerbabybed
    show bedroom_overlay
    show night_overlay
    with dissolve
    return

##
# Poem making function
##
#

label speak_poem(poem_to_speak):
    $ poem_lines = poem_to_speak.split("\n")
    if (len(poem_lines) <= 3):
        him determined "[poem_to_speak]"
    else:
        $ poem_line_count = 0
        while (poem_line_count < len(poem_lines)):
            $ poem_current_line = poem_lines[poem_line_count]
            $ poem_line_count += 1
            him determined "[poem_current_line]"
    return

label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board, True)
    return

init -100 python:

    # Returns the players current parenting style.
    # Should be one of authoritative, authoritarian, permissive, neglectful
    # or inconsistent if none are very high.
    # Return the highest.  If two are equal, return the better one.
    def get_parenting_style():
        parenting_style = "inconsistent"
        if ((authoritative >= authoritarian) and
           (authoritative >= permissive) and
           (authoritative >= neglectful)):
            parenting_style = "authoritative"
            if (year > TODDLER_MAX):
                achieved("Firm Yet Fair")
        elif ((authoritarian >= authoritative) and
              (authoritarian >= permissive) and
              (authoritarian >= neglectful)):
            parenting_style = "authoritarian"
            if (year > TODDLER_MAX):
                achieved("Big Boss")
        elif ((permissive >= authoritarian) and
              (permissive >= authoritative) and
              (permissive >= neglectful)):
            parenting_style = "permissive"
            if (year > TODDLER_MAX):
                achieved("Who Needs Rules?")
        elif ((neglectful >= authoritarian) and
              (neglectful >= authoritative) and
              (neglectful >= permissive)):
            parenting_style = "neglectful"
            if (year > TODDLER_MAX):
                achieved("Hands-Off Approach")

        
        pstyle = "{emoji=" + parenting_style + "} " + parenting_style.capitalize() + " parent"
        notify_change(pstyle)
        return parenting_style
        
    def notify_change(msg):
        if (renpy.get_screen("yearly_summary") or renpy.get_screen("save") or renpy.get_screen("plan_farm")):
            return
        else:
            renpy.show_screen("show_notification", msg)
        return

    # Get the person's first name from their display name.
    # Used in the message board - bios interface
    def get_nickname(name):
        if (not name):
            return name
        elif (name.startswith("Dr. Lily")):
            return "Lily"
        elif (name.startswith("Mayor Pavel")):
            return "Pavel"
        elif (name.startswith("Sister Naomi")):
            return "Naomi"
        elif (name.startswith(his_name)): # need to have these in here in case custom names have spaces in them
            return his_name
        elif (name.startswith(her_name)):
            return her_name
        elif (name.startswith(kid_name)):
            return kid_name
        elif (name.startswith(bro_name)):
            return bro_name

        else:
            return name.split()[0]

    # Returns whether kid is attached, competent, or indepedent for her age,
    # based on whether she is on track to reach the _HIGH value for
    # that stat.
    def is_attached():
        return (total_attachment >= roundint(year * (ATTACHMENT_HIGH/float(MAX_YEARS))))

    def is_competent():
        return (total_competence >= roundint(year * (COMPETENCE_HIGH/float(MAX_YEARS))))

    def is_independent():
        return (total_independence >= roundint(year * (INDEPENDENCE_HIGH/float(MAX_YEARS))))

    def get_kid_adjective():
        if is_independent():
            return "independent"
        elif (is_competent() and (total_competence >= total_attachment)): 
            return "capable"        
        elif (is_attached() and (total_attachment >= total_competence)):
            return "friendly"
        return "smart"

    def get_kid_type():
        if (is_attached()):
            if (is_competent()):
                if (is_independent()):
                    return "ACI"
                else:
                    return "ACi"
            else:
                if (is_independent()):
                    return "AcI"
                else:
                    return "Aci"
        else:
            if (is_competent()):
                if (is_independent()):
                    return "aCI"
                else:
                    return "aCi"
            else:
                if (is_independent()):
                    return "acI"
                else:
                    return "aci"

    # Return the number of Earth years, given Talaam years.
    # There are 196 27-hour days per year on Talaam,
    #       (7 months in a year, 7 days in a week, 4 weeks in a month)
    # and 365 24-hour days on Earth
    def get_earth_years(talaam_years):
        hours = float(talaam_years) * 196.0 * 27.0
        earth_years = hours / 24.0 / 365.25
        earth_years = round(earth_years, 1)
        return earth_years

    # Find the right work event for this year
    def get_next_work_event():
        global crop_temporarily_disabled, crop_info, number_events_seen
        # Enable any crops that were temporarily disabled
        if (crop_temporarily_disabled != ""):
            enable_crop(crop_temporarily_disabled, False)
            crop_temporarily_disabled = ""

        # Reset spinach if it was temporarily limited
        if (crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] <= 2):
            crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] = 100

        #Every even year there is a set event; other years are crop events.
        # This means we need 15 set events and at least 15 crop events (we have 28)

        # If you overworked yourself too much, you get an overwork event
        overwork_threshold = renpy.random.randint(-5, -1)
        if ((get_work_available() - get_work_needed()) <= overwork_threshold):
            return "overwork"

        # Is this an even year? then we have a set work event
        if ((year % 2) == 0):
            # Call the next set event
            event_name = "work" + str(year)
            return event_name

        # Otherwise, we get a random crop event
        else:
            # special potato event
            if ((year == 29) and (year28_promised_potatoes)):
                return "work29_potatoes"

            # Find a good crop event.
            # Make a set (no duplicates) of the next crop event for each crop in our field. Then, randomly pick one.
            possible_events = set()
            # If you have a lot of money, you might get an investment/charity opportunity
            if (credits > 1000):
                last_money_event = number_events_seen["money"]
                if (last_money_event == 0):
                    number_events_seen["money"] += 1
                    possible_events.add("money1")
                elif (last_money_event == 1):
                    number_events_seen["money"] += 1
                    possible_events.add("money2")
                
            for crop_name in farm.crops:
                if (crop_name != ""):
                    #get the number of the next event for this crop
                    #print("Crop: " + crop_name)
                    crop_name = crop_name.rstrip("+")
                    next_event = number_events_seen[crop_name] + 1
                    event_label = crop_name + str(next_event)
                    if renpy.has_label(event_label):
                        # Exclude crop events where characters would be too young or too old
                        if ((event_label == "honey1") and ((year < TODDLER_MAX) or (year > YTEEN_MAX))):
                            pass
                        elif ((event_label == "garlic1") and (year < CHILD_MAX)):
                            pass
                        elif ((event_label == "wheat1") and (year <= MINERS_ARRIVE_YEAR)):
                            pass
                        else:
                            possible_events.add(event_label)

            num_possible_events = len(possible_events)          
            if (num_possible_events > 0):
                random_event = renpy.random.choice(list(possible_events))
                crop_name = ''.join([i for i in random_event if not i.isdigit()])  # strip off the trailing numbers of the crop event to get back the original crop_name
                number_events_seen[crop_name] += 1
                #print "Picked event: " + random_event
                return random_event

        return "default_crop_event"         # If somehow we don't have any crop events, then just give a default one.

    # Change amount of credits you have
    def modify_credits(amount, show_notification=True):
        global credits, notifications
        amount = roundint(amount)
        if (year > MONEY_YEAR): # only if credits are used yet
            if show_notification:
                credit_msg = "{image=" + STAT_ICON_BASE + "value.png} " + str(amount)
                notify_change(credit_msg)
            credits += amount
        return

    def modify_farm_size(amount):
        global farm_size, notifications
        if ((farm_size+amount) < FARM_SIZE_MINIMUM):
            farm_size = FARM_SIZE_MINIMUM
            return False
        elif ((farm_size+amount) > FARM_SIZE_MAXIMUM):
            farm_size = FARM_SIZE_MAXIMUM
            return False
        else:
            farm_size += amount
            if (amount < 0):
                notify_change("Farm Size " + str(amount))
            else:
                notify_change("Farm Size +" + str(amount))
            #notification_add("Farm Size", amount)    
            return True

    # Calculate expenses required for the family for this year
    def get_expenses_required(year):
        return (annual_expenses_base + (get_calories_required(year) * CALORIES_TO_MONEY_MULTIPLIER))

    # Calculate value in credits from crop value
    def get_credits_from_value(crop_value):
        crop_credits = 0
        if (crop_value != 0):
            crop_credits = (crop_value * crop_value * 4 + 10)
        return crop_credits

    def get_credits_from_name(crop_name):
        return get_credits_from_value(crop_info[get_crop_index(crop_name)][VALUE_INDEX])

    # Calculate nutrition required for the family for this year.
    # Returns the amount of a vitamin required each year. Scale
    # is about half that of calories.
    def get_vitamins_required(year):
        earth_year = get_earth_years(year)
        return int(VITAMINS_BASE + 0.4 * get_calories_kids(earth_year))

    # Calculate the calories required for the family for this year.
    def get_calories_required(year):
        earth_year = get_earth_years(year)
        return int(CALORIES_BASE + get_calories_kids(earth_year))

    def get_calories_kids(earth_year):
        calories_kid = get_calories_kid(earth_year)
        calories_bro = 0
        if ((bro_birth_year != 0) and (bro_birth_year < year)):
            bro_age = year - bro_birth_year
            calories_bro = get_calories_kid(get_earth_years(bro_age))
        return (calories_kid + calories_bro)

    def get_calories_kid(age):
        if (0 <= age < BABY_MAX):
            return 2
        if (BABY_MAX <= age < TODDLER_MAX):
            return 5
        if (TODDLER_MAX <= age < CHILD_MAX):
            return 14
        if (CHILD_MAX <= age < YTEEN_MAX):
            return 19
        if (YTEEN_MAX <= age):
            return 23
        return 0

    # Calculate the amount of work available.
    def get_work_available():
        return WORK_BASE + work_increase + get_work_kid()

    def get_work_kid():
        return roundint(total_competence * 1.2 * (kid_work_slider / 100.0) - kid_other_work)

    def get_work_needed():
        total_work = 0
        for i in range(0, farm.crops.len()):
            crop_names = [row[NAME_INDEX] for row in crop_info]
            index = crop_names.index(farm.crops[i]) # find the crop's index in crop_info
            total_work += crop_info[index][WORK_INDEX]
        return total_work

    def get_extra_work():
        total_work = get_work_needed()
        work_available = get_work_available()
        if ((work_available - total_work) > 0):
            notify_change("{image=gui/emoji/work.png} Extra Work")
        return (work_available - total_work)

    # Return True if marriage is strong for the current year
    # A rate of 1 per 4 years is considered high given a current max of 10
    def has_strong_marriage():
        strong = (marriage_strength >= roundint(year / 4.5))
        if strong:
            notify_change("{emoji=heart} Strong Marriage")
        return strong

    # Return True if you have a good amount of trust
    def has_trust():
        return (trust > 0)

    # Return whether the relationship with a faction is "strong" or not
    # Optional parameter "strength" controls how strong the relationship has
    # to be to return TRUE.  Default is "strong", while "moderate" and 
    # "weak" have less stringent requirements.
    def mavericks_strong(strength="strong"):
        global total_mavericks, total_miners, total_colonists
        strong = faction_strong(total_mavericks, strength)
        if (strong):            
            notify_change("{emoji=friends} Mavericks")
        return strong
    def miners_strong(strength="strong"):
        strong = faction_strong(total_miners, strength)
        if (strong):
            notify_change("{emoji=friends} Miners")
        return strong
    def colonists_strong(strength="strong"):
        strong = faction_strong(total_colonists, strength)
        if (strong):
            notify_change("{emoji=friends} Colonists")
        return strong

    # Helper function for each faction to calculate whether they are "strong" or not.
    def faction_strong(faction_value, strength="strong"):
        # print("factionvalue=" + str(faction_value))
        global year
        strong = False
        if (strength == "weak"):
            strong = ((faction_value / (year / 7.0)) >= 1)
        elif (strength == "moderate"):
            strong = ((faction_value / (year / 5.0)) >= 1)
        else:
            strong = ((faction_value / (year / 3.0)) >= 1)
        return strong

    # Returns the strongest faction
    def strongest_faction():
        if ((total_colonists >= total_miners) and (total_colonists >= total_mavericks)):
            notify_change("{emoji=friends} Colonists")
            return "colonists"
        elif ((total_miners >= total_colonists) and (total_miners >= total_mavericks)):
            notify_change("{emoji=friends} Miners")
            return "miners"
        elif ((total_mavericks >= total_colonists) and (total_mavericks >= total_miners)):
            notify_change("{emoji=friends} Mavericks")
            return "mavericks"
        else:
            return "colonists"

    # Return who has the highest relationship, or "" if none are greater than 0
    def get_boyfriend_name():
        if ((oleg_points <= 0) and (travis_points <=0) and (lorant_points <= 0)):
            return ""

        # If they are all equal, base it on the strongest faction
        if (oleg_points == travis_points):
            if (oleg_points == lorant_points):
                if (strongest_faction() == "miners"):
                    return "Lorant"
                elif (strongest_faction() == "mavericks"):
                    return "Travis"
                else:
                    return "Oleg"            

        # Otherwise, whichever is greatest, giving priority to Oleg and Travis
        if (oleg_points >= lorant_points):
            if (oleg_points >= travis_points):
                return "Oleg"
            else:
                return "Travis"
        elif (travis_points >= oleg_points):
            return "Travis"        
        else:
            return "Lorant"
        return ""

    # Returns a fuzzy description of the given percentage.
    # Used for nitrogen and pest levels.
    def get_level_fuzzy(percentage):
        if (percentage < 0.05):
            return "{color=#0f0}Good{/color}"
        elif (percentage < 0.33):
            return "{color=#fff}OK{/color}"
        elif (percentage < 0.66):
            return "{color=#ff0}Warning{/color}"
        else:
            return "{color=#f00}Danger{/color}"

    # Return bee boosting overlay if it applies to this square
    # Otherwise return null image
    def get_boost_image(index):
        if (index in farm.get_boosted_squares()):
            return Image("gui/emoji/bee boost.png")
        else:
            return Null()

    # Return bee boosting overlay if it could boost this crop
    # Otherwise return null image
    def get_boosted_image(crop_name, crop_index):
        if (crop_enabled("honey")):
            if (crop_info[get_crop_index(crop_name)][POLLINATED_INDEX]):
                if bee_adjacent(crop_index, farm.crops.len()):
                    return Image("gui/emoji/bee boost.png")
        return Null()

    # Return whether there is honey next to this crop or not.
    def bee_adjacent(crop_index, max_size):
        adjacent = get_adjacent(crop_index, max_size)
        for square_index in adjacent:
            if (square_index > max_size):
                print "OUT OF BOUNDS: " + str(square_index)
            elif (farm.crops[square_index] == "honey"):
                return True
        return False

    # Return the number of currently enabled crops
    def count_enabled_crops():
        count = 0
        for i in range(0, len(crop_info)):
            if crop_info[i][ENABLED_INDEX]:
                count += 1
        return count

    # Return the pest overlay image correlated to the pest_factor
    def get_pest_image(pest_factor):
        if (pest_factor < 0.05):
            return Null(CROP_ICON_SIZE, CROP_ICON_SIZE)
        elif (pest_factor < 0.33):
            return Image("gui/crop icons/pest-low.png")
        elif (pest_factor < 0.66):
            return Image("gui/crop icons/pest-med.png")
        else:
            return Image("gui/crop icons/pest-high.png")

    def roundint(number):
        return int(round(number))

    def achieved(a_name):
        if (achievement.has(a_name)):
            return
        else:
            achievement.grant(a_name)
            achievement.sync()            
            notify_change("Achievement Unlocked!\n" + a_name)
            #if (not renpy.mobile): # take a screenshot for later use
            #    renpy.call("photo", a_name)

        return