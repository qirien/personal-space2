# Library of functions we call that have to do with game variables, etc.

##
# DYNAMIC MOUSE CURSOR 
##
#TODO: remove if we end up not using this
init 1 python:
    def change_cursor(type="default"):
        persistent.mouse = type
        if type == "default":
            setattr(config, "mouse", None)
        elif type == "punch":
            setattr(config, "mouse", {"default": [("gui/punch.png", 6, 6)]})
            
    if not hasattr(persistent, "mouse"):
        change_cursor()
    else:
        change_cursor(persistent.mouse)

    def random_float():
        return renpy.random.random()

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

label increase_attachment:
    # If we have extra time after taking care of farm, we assume some of it is spent playing with Terra and increasing attachment
    if (total_work < current_work):
        $ attachment += 1
    $ attachment += responsive
    return
    
label increase_competence:
    # If your kid spends more than half their time working, increase competence
    # TODO: Should we take out the int casting and allow more nuance?
    # Or have their work_slider affect how much demanding gets added?
    $ competence += int(kid_work_slider/50.0)
    $ competence += demanding
    return
    
label increase_independence:
    $ independence += (demanding + responsive) / 2.0
    return
    

init -100 python:

    # Returns the players current parenting style.
    # Should be one of authoritative, authoritarian, permissive, neglectful
    # or inconsistent if none are very high.        
    # Return the highest.  If two are equal, return the better one.
    def get_parenting_style():
        
        # If no stat is above year/3, return "inconsistent"
        if ((authoritative <= year/3) and
            (authoritarian <= year/3) and
            (permissive <= year/3) and
            (neglectful <= year/3)):
                return "inconsistent"
        else:
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
        return (attachment >= (year * (ATTACHMENT_HIGH/float(MAX_YEARS))))
        
    def is_competent():
        return (competence >= (year * (COMPETENCE_HIGH/float(MAX_YEARS))))
        
    def is_independent():
        return (independence >= (year * (INDEPENDENCE_HIGH/float(MAX_YEARS))))
        
    # Return the number of Earth years, given Talaam years.
    # There are 196 27-hour days per year on Talaam,
    #       (7 months in a year, 7 days in a week, 4 weeks in a month)
    # and 365 24-hour days on Earth    
    def get_earth_years(years):
        hours = years * 196.0 * 27.0
        earth_years = hours / 24.0 / 365.25
        earth_years = round(earth_years, 1)
        return earth_years
        
    # Find the right work event for this year
    def get_next_work_event():
        #Every even year there is a set event; other years are crop events.
        # This means we need 15 set events and at least 15 crop events.
        if ((year % 2) == 0): 
            # Call the next set event
            event_name = "work" + str(year)
            return event_name
        else:
            # Find a good crop event.
            # Make a set (no duplicates) of the next crop event for each crop in our field. Then, randomly pick one.
            possible_events = set()
            for crop_name in farm.crops:
                if (crop_name != ""):
                    #get the number of the next event for this crop
                    #print "Crop: " + crop_name
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
            
    # Calculate nutrition required for the family for this year.
    # TODO: right now this is the same as calories? Is that true?
    def get_nutrition_required():
        return get_calories_required()                
                
    # Calculate the calories required for the family for this year.
    # TODO: Kids use more calories if you make them do farm work?
    def get_calories_required():
        calories_kid = get_calories_kid(int(earth_year))
        calories_bro = 0
        if (bro_birth_year != 0):
            calories_bro = get_calories_kid(bro_age)
        return (CALORIES_BASE + calories_kid + calories_bro)
        
    def get_calories_kid(age = 0):        
        if (0 <= age <= 1):
            return 5
        if (2 <= age <= 4):
            return 10
        if (5 <= age <= 10):
            return 15
        if (11 <= age <= 13):
            return 20
        if (14 <= age):
            return 25
            
    # Calculate the amount of work available.
    def get_work_available():
        return WORK_BASE + get_work_kid(earth_year)
        
    def get_work_kid(age = 0):
        return int(competence * (kid_work_slider / 100.0))         
        
            
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
        show baby girl at centerbaby, squatting
    show bedroom_overlay
    show night_overlay
    with dissolve