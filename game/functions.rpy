# Library of functions we call that have to do with game variables, etc.

label increase_attachment:
    # if (responsive <= 0):
        # $ attachment += 1
    # else:
        # $ attachment += (responsive/(year/2.0)) * 2
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
            # Find a good crop event
            possible_events = []
            for crop_name in crops:
                if (crop_name != ""):
                    #get the number of the next event for this crop
                    print "Crop: " + crop_name
                    next_event = number_events_seen[crop_name] + 1
                    event_label = crop_name + str(next_event)
                    print "Event: " + event_label
                    if renpy.has_label(event_label):
                        print "Event found!"
                        possible_events.append(event_label) 
                    
            num_possible_events = len(possible_events)
            if (num_possible_events > 0):
                random_event = renpy.random.choice(possible_events)
                crop_name = ''.join([i for i in random_event if not i.isdigit()])  # strip off the trailing numbers of the crop event to get back the original crop_name
                number_events_seen[crop_name] += 1
                print "Picked event: " + random_event
                return random_event
            else:
                return "default_crop_event"