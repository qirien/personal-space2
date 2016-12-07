# Work events defined

init python:
    # If no other event matches up, run the default
    event("work_default", event.solo(), priority=200)
    
    # Sequential events that don't depend on specific crops
    # They have a lower priority (higher priority value) because we'd rather do specific crop events
    event("work1", event.once(), event.only(), priority=150)
    for i in range(2,9):
        event("work" + `i`,
              event.once(),
              event.only(),
              event.happened("work" + `i-1`), 
              priority=150)

    # Crop events
    # for each crop
    # find all events with that crop's name
    # set the first one as an event.once()
    # set all subsequent events as depending on the prior event
    
    event("potato1", event.once(), event.only(), "potatoes == True")
    event("potato2", event.once(), event.only(), "potatoes == True", event.happened("potato1"))

