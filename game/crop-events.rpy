# Crop-specific work events

# Default crop event, if no other crop event can be found
label default_crop_event:
    "The year passed by in a blur: tilling, planting, weeding, harvesting."   
    return

label carrots1:
    "You harvest carrots, but many are bent and twisted."
    menu:
        "Till the soil better. Must be rocks.":
                "Lots of work, next year better carrots."
        "Must be something in the soil. Avoid planting carrots for a year.":
                "No carrots allowed next year."
                $ carrots_fallow = True
        "Who cares, they taste the same.":
                "I didn't do anything about it.."
                
    return
                
label carrots2:
        if (carrots_fallow):
                "Your carrots are growing bigger than last time! Seems like you got rid of the pests that were deforming them."
        else:
                "Your carrots were growing, but they've stopped early, and now the leaves are turning yellow. Looks like the plants are dying."
                # take care of pests somehow
        return

label carrots3:
        "You have tons of carrots!  [kid_name] eats them all the time, which is good, but her hands are turning yellow..."
        menu: 
                "No more carrots!":
                        "Dad, you're so mean!"
                "It's harmless, she'll be fine.":
                        "You get some dirty looks from other parents, but you're pretty sure they're just jealous that they don't have as many carrots."
        return
        
label potatoes1:
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
    
label potatoes2:
    "Cooking potatoes that the family will like."
    menu:
        "Make mashed potatoes":
            $pass
        "Make fries":
            $pass
        "Make baked potatoes with goat cheese and onions":
            $pass
            
    return
        
label potatoes3:
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
    return
                
label goats2:
    "Make goat cheese or something."
    return
        
label goats3:
    "Your goats get out and destroy some neighboring farm land of someone else. What do you do?"
    return
    
label tomatoes1:
    $ tomatoes1_action = "none"
    "The tomatoes were looking so good, but a lot of them have sunken rotten areas on the bottom."
    menu:
        "Do some research":
            "Looks like blossom-end rot.  If you add some more calcium to the soil and water more evenly, this shouldn't happen next time."
            $ tomatoes1_action = "research"
        "Just cut it off":
            "Most of the tomato is fine.  You're canning most of them, anyway, so who cares if you have to throw a bit away."
            $ tomatoes1_action = "cut"
        "Add more fertilizer":
            "Next time you'll add more fertilizer; that should help."
            $ tomatoes1_action = "fertilize"            
    return
    
label tomatoes2:
    $ tomatoes2_action = "none"
    if (tomatoes1_action == "research"):
        "The tomatoes look much better this year!"
        menu:
            "You can choose which fruits to save seeds from for planting next year."
            "First tomatoes":
                $ tomatoes2_action = "early harvest"
            "Biggest tomatoes":
                $ tomatoes2_action = "size"
            "Sweetest tomatoes":
                $ tomatoes2_action = "sweetness"
    else:
        "The tomatoes have the same rotten bottom area as last time, only now it's even worse!"
        "You do some research and find out that usually that means there's too much nitrogen in the soil and not enough calcium.  Too bad most of the tomatoes for this year are useless."        
    return    
    
label tomatoes3:
    if (tomatoes2_action  == "early harvest"):
        "You have lots of tomatoes quickly!  So quickly, in fact, that you can squeeze in two plantings a year, effectively doubling your tomato harvest. They taste pretty good, too."
    elif (tomatoes2_action == "size"):
        "The tomatoes are slightly bigger than last year.  If you keep choosing the biggest tomatoes seeds to save, you are going to have tomatoes as big as melons!"
    elif (tomatoes2_action == "sweetness"):
        "These are so juicy and sweet that [her_name] likes to just go out and eat them for lunch."
    else:
        "Finally, you have a good tomato harvest.  Time for salsa, spaghetti sauce, and maybe even some pizza!"
    
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
    
label spinach1:
    "Your spinach is looking good!"
    menu:
        "Pick it early":
            "Yum, smaller, more tender greens, but less food."
        "Wait until it's fully grown":
            "Larger harvest. more bitter taste.  more food/less happiness"
    
label spinach2:
    "You had a heat wave and your spinach failed to germinate.  It doesn't usually get that hot, so maybe you could try again? But you only have enough seeds to plant one more batch."
    menu:
        "Plant them again and pray it doesn't get too hot.":
            "It was hot enough that the spinach started to flower before you could harvest it.  Once spinach flowers, it tastes really bitter.  But at least you can harvest the seeds for next year."
            "The goats enjoy your bitter spinach plants."
        "Save the seeds.":
            "It's not worth the effort.  You save the seeds for next year."            
    return
    
label spinach3:
    "You planted your spinach earlier and it's almost to full size."
    "But something has been eating the plants. You haven't seen anything, but when you check on the spinach, there's definitely bites taken out."
    menu:
        "Check the surveillance cameras":
            "You train the farm's cameras on the spinach plot, but the next day when you look at the video, none of the motion sensors were triggered.  You scan through the video but can't find anything that's eating them." 
            "Looks like you'll have to find out the old-fashioned way."
        "Check on your spinach at night":
            "After [kid_name] and [her_name] went to bed, you snuck out of the house to examine your spinach plants.  Your flashlight catches something small and slimy -- it looks like a slug!"
            menu:
                "Hand pick them off":
                    "You spend the night plucking off slugs and putting them in a bucket. And the next night.  And the next night.  There's fewer each night, but it's tedious work."
                    # TODO: Depending on Terra's age, maybe you enlist her help?                   
                    "Your reward is lots of great spinach."
                "Make slug traps":
                    "You put some tasty smelling bait in the middle of a hole covered with boards."
                    "In the morning, the hole was full of slugs, just waiting for you to murder them."
                    "You make some more traps and check them every morning."
                    "The slugs will regret their incursion into your garden."
                "Just pick the spinach early":
                    jump spinach_pick_early
        "Just pick the spinach early":
            jump spinach_pick_early

label spinach_pick_early:
    "It'd be too much work to kill all the slugs. You might as well just harvest the spinach early and then there won't be anything for them to eat."
    "But spinach isn't the only thing slugs like..."
    # TODO: Change this to get a currently-planted crop that slugs would eat, like cabbage, tomatoes, beans, 
    $ slug_crop = "cabbage"
    "After you picked the spinach, they moved on to your [slug_crop]."
    "This is something that you cannot forgive."
    "This means war."
    "Your nights are filled with killing slugs."
    "They appear in your dreams, giant slugs with ever-chewing mouths, the entire earth disappearing beneath their slavering jaws until Talaam is just an empty spot in the vast blackness of space."    
    return
