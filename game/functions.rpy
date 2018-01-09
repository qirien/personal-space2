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
# PARENTING FUNCTIONS
##

label increase_attachment:
    $ attachment += responsive
    return
    
label increase_competence:  
    $ competence += demanding
    return
    
label increase_independence:
    $ independence += (demanding + responsive) / 2.0
    return
    

init -100 python:

    # Returns the players current parenting style.
    # Should be one of authoritative, authoritarian, permissive, or passive
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
        
    

init python:
    ##
    # CROPS OBJECT
    #
    class Crops(renpy.store.object):
        # Initialize as an empty field of a certain size
        def __init__(self, size):
            self.items = [""] * size
            
        # Set the crop at [index] to [crop_name]
        def __setitem__(self, key, value):
            self.items[key] = value
            
        def __getitem__(self, key): 
            return self.items[key]
            
        def count(self, value):
            return self.items.count(value)
            
        def len(self):
            return len(self.items)
            
        # Randomly select from currently available crops, respecting maximums 
        def setDefault(self):
            available_crop_names = []
            for i in range(0, len(crop_info)):
                if (crop_info[i][ENABLED_INDEX]):
                    available_crop_names.append(crop_info[i][NAME_INDEX])
                
            for i in range(0, farm_size):
                crop_name = renpy.random.choice(available_crop_names)
                self[i] = crop_name
                
                # If we've reached the max, remove this crop from the ones that can be chosen
                if (self.items.count(crop_name) >= crop_info[get_crop_index(crop_name)][MAXIMUM_INDEX]):
                    available_crop_names.remove(crop_name)
            return
            
        def update_history(self, crop_history):
            for i in range(0, len(self.items)):
                crop_history[i] = [self[i]] + crop_history[i][0:-1]
            return
            
        # Return a random crop from our field
        # If weighted, then you will be more likely to get a crop the more times it is planted.
        def random_crop(self, weighted = True, include_animals = True):
            chosen_crop = ""
            while (chosen_crop == ""):
                if weighted:
                    chosen_crop = renpy.random.choice(self.items)
                else:
                    chosen_crop = renpy.random.choice(list(set(self.items)))
                if (not include_animals):
                    # TODO: include other animals, or base this on a flag or something
                    if (chosen_crop == "goats"):
                        chosen_crop = ""
                
            return chosen_crop
        
    
    # Return the index of a crop in crop_info given its name
    def get_crop_index(crop_name):
        crop_names = [row[0] for row in crop_info]
        index = crop_names.index(crop_name) # find the crop's index in crop_info
        return index

    # Return the number of Earth years given years Talaam years.
    # There are 196 27-hour days per year on Talaam, 
    # and 365 24-hour days on Earth        
    def get_earth_years(years):
        hours = years * 196.0 * 27.0
        earth_years = hours / 24.0 / 365.25
        earth_years = round(earth_years, 1)
        return earth_years
        
    # Find the right work event for this year
    def get_next_work_event():
        #Every 3 years there is a set event; other years are crop events.
        # This means we need 10 set events and at least 20 crop events.
        if ((year % 3) == 0): 
            # Call the next set event
            event_number = year // 3
            event_name = "work" + str(event_number)
            return event_name
        else:
            # Find a good crop event.
            # Make a set (no duplicates) of the next crop event for each crop in our field. Then, randomly pick one.
            possible_events = set()
            for crop_name in crops:
                if (crop_name != ""):
                    #get the number of the next event for this crop
                    print "Crop: " + crop_name
                    next_event = number_events_seen[crop_name] + 1
                    event_label = crop_name + str(next_event)
                    print "Event: " + event_label
                    if renpy.has_label(event_label):
                        print "Event found!"
                        possible_events.add(event_label) 
                    
            num_possible_events = len(possible_events)
            if (num_possible_events > 0):                
                random_event = renpy.random.choice(list(possible_events))
                crop_name = ''.join([i for i in random_event if not i.isdigit()])  # strip off the trailing numbers of the crop event to get back the original crop_name
                number_events_seen[crop_name] += 1
                print "Picked event: " + random_event
                return random_event
            else:
                return "default_crop_event"                                
        
    # Calculate how many crops we harvested in each square and update the field_health
    # TODO: we can't modify field_health; changes won't stick because it's passed by reference. Getting weird behavior.
    def process_crops(crops, field_health, field_history):
        final_yield = [100] * MAX_FARM_SIZE
        current_nitrogen = 0
        current_pests = 0
        for i in range(0, farm_size):
            pest_factor = 0
            nitrogen_factor = 0            
            crop_name = crops[i]
            current_nitrogen = field_health[i][NITROGEN_LEVEL_INDEX]
            current_pests = field_health[i][PEST_LEVEL_INDEX]
            print "Crop " + str(i) + " is " + crop_name + " and current_nitrogen: " + str(current_nitrogen) + ", current_pests: " + str(current_pests)

            if (crop_name == ""):
                # Reset health of fallow field
                print "RESETTING!"
                if (current_nitrogen < NITROGEN_FALLOW):
                    field_health[i][NITROGEN_LEVEL_INDEX] = NITROGEN_FALLOW
                if (current_pests > PEST_NONE):
                    field_health[i][PEST_LEVEL_INDEX] = PEST_NONE                                
                
            else:
                # Decrease yield based on randomness and number of times crop has been in that spot lately.
                # Set pest level of field after crops.
                pest_factor = current_pests + current_pests * renpy.random.random() * field_history[i].count(crop_name)
                field_health[i][PEST_LEVEL_INDEX] += pest_factor
                if (pest_factor > 100):
                    pest_factor = 100
                print "Pest Factor[" + str(i) + "] is " + str(pest_factor)            
                
                # Decrease yield if there's not enough nitrogen
                # Set nitrogen level of the field after crops
                new_nitrogen = current_nitrogen - crop_info[get_crop_index(crop_name)][NITROGEN_INDEX]
                print "New Nitrogen: " + str(new_nitrogen)
                if (new_nitrogen < 0):
                    nitrogen_factor = new_nitrogen / NITROGEN_FALLOW * -100
                    field_health[i][NITROGEN_LEVEL_INDEX] = 0
                else:
                    field_health[i][NITROGEN_LEVEL_INDEX] = new_nitrogen
                
                print "Nitrogen Factor[" + str(i) + "] is " + str(nitrogen_factor)
                final_yield[i] = final_yield[i] - pest_factor - nitrogen_factor
            
        return final_yield
        
##
#
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