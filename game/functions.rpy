# Library of functions we call that have to do with game variables, etc.

label increase_attachment:
    # if (responsive <= 0):
        # $ attachment += 1
    # else:
        # $ attachment += (responsive/(year/2.0)) * 2
    $ attachment += responsive / 2.0
    return
    
label increase_competence:
   
    $ competence += demanding / 2.0
    return
    
label increase_independence:
    $ independence += (demanding + responsive) / 2.0
    return
    

# Returns the players current parenting style.
# Should be one of authoritative, authoritarian, permissive, or passive
init -100 python:
    def get_parenting_style():
        if (total_attachment >= year):
            if (total_demanding >= year):
                return "authoritative"
            else:
                return "permissive"
        else:
           if (total_demanding >= year):
               return "authoritarian"
           else:
                return "passive"
        return "passive"
        
    
# commenting it out for now until I can come back and think about it some more
# This might have to be calculated on a case-by-case basis, since different "times" of the year will have different total possible stat totals.

# label get_attachment:
#   return $ responsive / 2.0 


# Function to find the right work event for this year
init python:
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
                #get the number of the next event for this crop
                #print "Crop: " + crop_name
                next_event = number_events_seen[crop_name] + 1
                event_label = crop_name + str(next_event)
                #print "Event: " + event_label
                if renpy.has_label(event_label):
                    #print "Event found!"
                    possible_events.append(event_label) 
                    
            num_possible_events = len(possible_events)
            if (num_possible_events > 0):
                random_event = renpy.random.choice(possible_events)
                crop_name = ''.join([i for i in random_event if not i.isdigit()])  # strip off the trailing numbers of the crop event to get back the original crop_name
                number_events_seen[crop_name] += 1
                #print "Picked event: " + random_event
                return random_event
            else:
                return "default_crop_event"