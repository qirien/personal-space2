## Our Personal Space 2
## MAIN

## The game starts here.

label start:

    scene bg stars with fade
    scene bg stars_animated
    # TODO: import names, stats, etc from OPS1, or ask user to fill them in; make this a screen
    if (mp.baby_name):
        $ his_name = mp.jack_name
        $ her_name = mp.kelly_name
        $ kid_name = mp.baby_name
        "Our Personal Space 1 data found. Please verify data."
        "Parents [his_name] and [her_name] gave birth to child [kid_name]"
        

    show him happy

    him "I always wanted to be a dad. I dreamed of teaching my kids, loving them, laughing together."
    him normal "Of course, I knew it'd be a lot of work too. But, like most hard work, I figured it'd be worth it."
    him "Even now that you're grown, I still think about your childhood."
    him concerned "Was I there for you? Did I do enough? Was I the dad you needed?"
    him normal "If I could go back, would I change anything? I don't even know."
    him "When you were first born, it was a struggle just to get through each day."  
    
    # TODO: show some sort of inter-scene screen
    # There are 196 27-hour days per year on Talaam, and 356 24-hour days on Earth
    $ year = 1
    while (year <= 30):
        # Autosave
        $ renpy.force_autosave(take_screenshot=True)
        $ renpy.choice_for_skipping()
        $ renpy.notify("{vspace=540}{color=#000}{space=40}Autosaving...{/color}")
        
        # Reset our variables while keeping a running total
        $ total_demanding += demanding
        $ demanding = 0
        $ total_responsive += responsive
        $ responsive = 0
        
        # FAMILY EVENTS (parenting/home life)
        scene black with fade
        centered "Year [year]\n\nFamily"
        scene black with fade
        call expression "family" + str(year)
        
        # Increase child stats based on this year's parenting decisions
        call increase_attachment
        call increase_competence
        call increase_independence
        
        # COMMUNITY EVENTS (building community, helping factions)
        scene black with fade
        centered "Year [year]\n\nCommunity"
        scene black with fade
        call expression "community" + str(year)
        
        # WORK EVENTS (farming)
        scene black with fade
        centered "Year [year]\n\nWork"
        scene black with fade
        
        $ work_event = get_next_work_event()        
        call expression work_event
        
        # CHOOSE FOR NEXT YEAR
        
        $ crops = [""] * farm_size
        call screen plan_farm
        
        $ year += 1
   
    return