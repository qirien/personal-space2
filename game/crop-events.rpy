# Crop-specific work events

label potato1:
    "Solanine in a batch of forgotten potatoes; how bad can they get before you toss them?"
    menu:
        "Taste one and see if it's bitter":
            "It tastes OK, so maybe it's safe to eat?"
            "You didn't get sick from it, so it's probably safe."
        "Throw out any that have any green":
            "No sense in risking solanine poisoning!  You throw out any that have any green on them, which ends up being the entire batch."
            # some kind of variable?  community_level?  farm_level? sustence?
        "Warn people to peel them first":
            "They're probably fine, but if people peel them they should get rid of the worst of it."
    return
    
label potato2:
    "Cooking potatoes that the family will like."
    menu:
        "Make mashed potatoes":
            $pass
        "Make fries":
            $pass
        "Make baked potatoes with goat cheese and onions":
            $pass
            
    return
    
    
label potato3:
    "A lot of rain leads to rotten potatoes.  :-("
    return
    
# only happens if no bees
label squash1:
    "Squash plants flower, but most don't bear fruit - need more pollination!"
    menu:
        "Pollinate by hand":
                $ pass # takes a lot of work
        "Ask to borrow some bees":
                $ pass # only successful if community level high enough?
        "Forget the squash for this season":
                $ pass # less food to eat
    return
    
label squash2:
    "Some squash plants are looking sickly... you recognize the pesky squash bugs from Earth!  They must have come in on a shuttle somehow!"
    menu:
            "Exterminate them all by hand!":
                $ pass #takes a lot of work
            "Apply pesticide":
                $ pass #does this really work? have side effects?
            "Ignore them":
                $ pass #they cause trouble later
            "Try and get the new folks to fix the problem. They started it, after all!":
                $ miners -= 1
                
    return
   
label squash3:
    "If you didn't get rid of the squash bugs, they come back stronger than ever!  You can't grow squash for several years."
    "If you did get rid of them, congratulations!  You have lots of squash."
    return
    
label goats1:
    "Your goats reproduced and now you have a lot of them!  Once all these kids grow up they will need more space."
    menu:
            "Smuggle some to the Luddites":
                $ luddites += 1
            "Send to the storehouse":
                $ colony += 1
            "Slaughter for meat":
                $ pass #family happiness/food increase?
            "Allocate more land for goats":
                $ pass # goats take up two squares now.
                
label goats2:
        "Make goat cheese or something."
        
label goats3:
    "Your goats get out and destroy some neighboring farm land of someone else. What do you do?"
    
label tomatoes1:
    "What do you make with your tomatoes?"
    
label tomatoes2:
    "You can breed your tomatoes for early harvest, size, or sweetness."
    
label tomatoes3:
    "Depending on what you picked, your tomatoes are good for different things."
    
label plums1:
    "You don't get any harvest this year, but you tend your plums carefully."
    
# Several years later
label plums2:
    "Finally, your spring is punctuated by beautiful pink blossoms on your plum trees."
    # Depending on pollination, you get a few or a lot of plums

label beans1:
    "You had a good bean harvest this year.  Now that you've dried them, they will last a long time."
    
label beans2:
    "It's been a cold spring. The bean plants haven't even germinated yet."
