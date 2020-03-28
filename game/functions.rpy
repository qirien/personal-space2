# Library of functions we call that have to do with game variables, etc.


##
# Menu Randomization
##

# TODO: change this to True to start shuffling menus
default shuffle_menu = False
init python:
    renpy_menu = menu

    def menu(items):
        items = list(items)
        if (shuffle_menu):
            renpy.random.shuffle(items)
        return renpy_menu(items)

##
#
##
init python:
    def bounded_value(val, min=0, max=100):
        if (val > max):
            return max
        elif (val < min):
            return min
        else:
            return val
##
# PARENTING FUNCTIONS
##

# Increase attachment based on how responsive you were last year
label increase_attachment:
    # If we have extra time after taking care of farm, we assume some of it is spent playing with Terra and increasing attachment,
    # as long as Terra's work slider is under 90%
    # TODO: is this balanced?
    $ inc_amount = 0
    #if ((total_work < current_work) and (kid_work_slider < 90.0)):
    #    $ inc_amount += 1
    $ inc_amount += responsive
    if (inc_amount > 0):
        $ notifications += "Attachment +" + str(inc_amount) + "\n"
    $ attachment += inc_amount
    return

# Increase competence based on how demanding you were last year and how much Terra worked
label increase_competence:
    $ inc_amount = 0
    # If your kid spends more than half their time working, increase competence
    # TODO: Should we take out the int casting and allow more nuance?
    # Or have their work_slider affect how much demanding gets added?
    # TODO: try taking this and previous one out and see what happens.
    # $ inc_amount += int(kid_work_slider/50.0)
    $ inc_amount += demanding
    if (inc_amount > 0):
        $  notifications += "Competence +" + str(inc_amount) + "\n"
    $ competence += inc_amount
    return

# Increase independence based on how much confidence you showed in her last year
label increase_independence:
    $ inc_amount = 0
    $ inc_amount += confident
    if (inc_amount > 0):
        $  notifications += "Independence +" + str(inc_amount) + "\n"
    $ independence += inc_amount
    return


init -100 python:

    # Returns the players current parenting style.
    # Should be one of authoritative, authoritarian, permissive, neglectful
    # or inconsistent if none are very high.
    # Return the highest.  If two are equal, return the better one.
    def get_parenting_style():

        # If no stat is above year/3, return "inconsistent"
        # if ((authoritative <= year/3) and
        #     (authoritarian <= year/3) and
        #     (permissive <= year/3) and
        #     (neglectful <= year/3)):
        #         return "inconsistent"
        # else:
       if ((authoritative >= authoritarian) and
           (authoritative >= permissive) and
           (authoritative >= neglectful)):
            return "authoritative"
       elif ((authoritarian >= authoritative) and
              (authoritarian >= permissive) and
              (authoritarian >= neglectful)):
            return "authoritarian"
       elif ((permissive >= authoritarian) and
              (permissive >= authoritative) and
              (permissive >= neglectful)):
            return "permissive"
       elif ((neglectful >= authoritarian) and
              (neglectful >= authoritative) and
              (neglectful >= permissive)):
            return "neglectful"

       return "inconsistent"


    # Returns whether kid is attached, competent, or indepedent for her age,
    # based on whether she is on track to reach the _HIGH value for
    # that stat.
    def is_attached():
        return (attachment >= roundint(year * (ATTACHMENT_HIGH/float(MAX_YEARS))))

    def is_competent():
        return (competence >= roundint(year * (COMPETENCE_HIGH/float(MAX_YEARS))))

    def is_independent():
        return (independence >= roundint(year * (INDEPENDENCE_HIGH/float(MAX_YEARS))))

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
        global crop_temporarily_disabled, crop_info
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
        if (get_extra_work() <= overwork_threshold):
            return "overwork"

        # Is this an even year? then we have a set work event
        if ((year % 2) == 0):
            # Call the next set event
            event_name = "work" + str(year)
            return event_name

        # TODO: If you have a lot of money, have an investment opportunity?

        # Otherwise, we get a random crop event
        else:
            # special potato event
            if ((year == 29) and (year28_promised_potatoes)):
                return "work29_potatoes"

            # Find a good crop event.
            # Make a set (no duplicates) of the next crop event for each crop in our field. Then, randomly pick one.
            possible_events = set()
            for crop_name in farm.crops:
                if (crop_name != ""):
                    #get the number of the next event for this crop
                    #print "Crop: " + crop_name
                    crop_name = crop_name.rstrip("+")
                    next_event = number_events_seen[crop_name] + 1
                    event_label = crop_name + str(next_event)
                    if renpy.has_label(event_label):
                        possible_events.add(event_label)

            num_possible_events = len(possible_events)
            if (num_possible_events > 0):
                random_event = renpy.random.choice(list(possible_events))
                crop_name = ''.join([i for i in random_event if not i.isdigit()])  # strip off the trailing numbers of the crop event to get back the original crop_name
                number_events_seen[crop_name] += 1
                #print "Picked event: " + random_event
                return random_event
            else:
                return "default_crop_event"

    # Change amount of credits you have
    # TODO: We have a popout screen; do we also need this in notifications?
    def modify_credits(amount):
        global credits, notifications
        amount = roundint(amount)
        renpy.show_screen("show_credits", amount=amount)
        credits += amount
        message = "Credits "
        if (amount >= 0):
            message += "+"
        message = message + str(amount) + "\n"
        notifications += message


    def modify_farm_size(amount):
        global farm_size, notifications
        if ((farm_size+amount) < FARM_SIZE_MINIMUM):
            farm_size = FARM_SIZE_MINIMUM
            return False
        elif ((farm_size+amount) > FARM_SIZE_MAXIMUM):
            farm_size = FARM_SIZE_MAXIMUM
            return False
        else:
            if (amount >= 0):
                notifications += "Farm size +" + str(amount) + "\n"
            else:
                notifications += "Farm size " + str(amount) + "\n"
            farm_size += amount
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
        if (0 <= age < 2):
            return 5
        if (2 <= age < 5):
            return 10
        if (5 <= age < 11):
            return 15
        if (11 <= age < 14):
            return 20
        if (14 <= age):
            return 25
        return 0

    # Calculate the amount of work available.
    def get_work_available():
        return WORK_BASE + get_work_kid()

    def get_work_kid():
        return roundint(competence * (kid_work_slider / 100.0) - kid_other_work)

    def get_extra_work():
        total_work = 0
        for i in range(0, farm.crops.len()):
            crop_names = [row[NAME_INDEX] for row in crop_info]
            index = crop_names.index(farm.crops[i]) # find the crop's index in crop_info
            total_work += crop_info[index][WORK_INDEX]

        work_available = get_work_available()
        return (work_available - total_work)

    # Return True if marriage is strong for the current year
    # A rate of 1 per 4 years is considered high given a current max of 10
    def has_strong_marriage():
        return (marriage_strength >= roundint(year / 4.0))

    # Return True if you have a good amount of trust
    def has_trust():
        return (trust > 0)

    # Return strength of relationships given current year
    # 1 or greater means strong, less than 1 means weak
    def mavericks_strength():
        return (mavericks / (year / 3.0))
    def miners_strength():
        return (miners / (year / 3.0))
    def colonists_strength():
        return (colonists / (year / 3.0))

    # Returns the strongest faction
    def strongest_faction():
        if (colonists >= miners >= mavericks):
            return "colonists"
        elif (miners >= colonists >= mavericks):
            return "miners"
        elif (mavericks >= colonists >= miners):
            return "mavericks"
        else:
            return "colonists"

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

    # Sorting functions (Python 2.7)
    # For Python 3+, only return the value on which to sort.
    def sortby_calories(val1, val2):
        return val1[CALORIES_INDEX] - val2[CALORIES_INDEX]
    # def sortby_vitA(val):
    #     return val[VITAMINA_INDEX]
    def sortby_work(val1, val2):
        return val1[WORK_INDEX] - val2[WORK_INDEX]
    def sortby_nitrogen(val1, val2):
        return val1[NITROGEN_INDEX] - val2[NITROGEN_INDEX]
    def sortby_value(val1, val2):
        return val1[VALUE_INDEX] - val2[VALUE_INDEX]


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
label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board)
    return
