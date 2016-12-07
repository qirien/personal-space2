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
