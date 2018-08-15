# Crop-specific work events

# TODO: First person or third person?
# TODO: Some crop events kind of assume that you'll get the next crop event
# the next year.  If you don't plant that crop the next year, some events
# should reset.

# Default crop event, if no other crop event can be found
label default_crop_event:
    "The year passed by in a blur: tilling, planting, weeding, harvesting.  The endless cycle of life on the farm."
    return

label carrots1:
    "I harvested carrots, but many are bent and twisted."
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
                "My carrots grew bigger than last time! I guess I got rid of the pests that were deforming them."
                scene farm_interior with fade
                show her normal at midright with dissolve
                show him normal at midleft with moveinleft
                him surprised "Aren't these carrots beautiful?"
                her surprised "Um... I guess so?"
                him happy "Look how straight and strong they are!"
                her concerned "Do they taste different."
                him concerned "Not really. But somehow beautiful straight carrots are more satisfying than gnarled twisted ones."
                her surprised "I suppose they might also be easier to work with."
                him happy "Exactly! I wonder if I can make sushi..."
                her normal "We have some smoked crabird meat... and you could get some rice and vinegar from the storehouse."
                him determined "Now all I need is some seaweed."
                her surprised "You're going to make nori?"
                him concerned "...maybe not this time. It'll be something kind of like sushi, anyway."
                her happy "Sounds delicious!"
                if (year >= 7):
                    scene black with fade
                    scene farm_interior with fade
                    show her normal at midright
                    show kid tween normal at center
                    show him normal at midleft
                    with dissolve
                    kid surprised "What are those?"
                    him happy "It's sushi! Well, it's kind of like sushi."
                    kid pout "It looks like eyeballs."
                    her normal "It's just rice wrapped around some meat and vegetables. Try it; it's good!"
                    kid shifty "Okay..."
                    him concerned "..."
                    her concerned "..."
                    kid nervous "It's kind of plain..."
                    him surprised "Yeah, I didn't get around to making spicy mayonaisse or soy sauce or anything. But... we have salt and pepper?"
                    her concerned "That's totally not authentic."
                    him determined "We're already making it with alien crustaceans and no seaweed... I think we can season it however we like."
                    kid happy "At least it doesn't taste like eyeballs!"

        else:
                "My carrots were growing, but they've stopped early, and now the leaves are turning yellow. Looks like the plants are dying."
                "I finally figured out there were some pests eating them. By that time, it was too late to fix the problem. So we wouldn't have any carrots this year."
                menu:
                    "What should I do next year?"
                    "Treat the carrots with pesticide":
                        "I decided to treat next year's carrots with pesticide. It'd be more work, but I didn't want to give up carrots."
                        # TODO: Make next year's carrots take more work?
                    "Don't plant carrots next year and let the pests die off.":
                        "The easiest thing to do was just not plant carrots for a year. Then the pests would die."
                        # TODO: Make carrots unavailable next year, and then come back??
        return

label carrots3:
    "I was glad I had managed to get rid of the pests on the carrots."
    "But this year, we had a ton. [kid_name] was eating them all the time, which is good, but her hands are starting to turn yellow... Is it healthy to eat that many carrots?!"
    menu:
        "What should I do?"
        "Ask [her_name].":
            him "Hey, Dr. [her_name], is it possible to eat too many carrots?"
            her "Are you talking about [kid_name]'s orange hands?"
            him "Yeah... is that bad?"
            her "No, not on its own. It's only bad if she's not getting other nutrients she needs because she's most just eating carrots."
            him "Okay, good to know."
            her "Don't you think I would have said something if there was something wrong?!"
            him "Well, I wasn't sure you noticed."
            her "Of course I noticed. And if you're not careful, the same thing will happen to you."
            menu:
                "What should I do?"
                "Keep eating carrots":
                    "I didn't care if my skin turned orange. These were good carrots!"
                "Try to eat other things.":
                    "I didn't want to look weird, so I took more carrots to the storehouse and tried to eat other things."
                    return
        "Don't let [kid_name] eat so many carrots.":
            kid "Dad, you're so mean!"
            return
        "Don't worry about it.":
            "There was probably nothing to worry about. In fact, my hands were looking a little orange, too..."
    # TODO: color them orange
    him "Best carrots ever."
    kid "Yum!"

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
                # Only allow if you got bees in work3?
                # TODO: something different happens if you do have bees? Someone else wants to borrow them?
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
            "Smuggle some to the Luddites": #only if you're past community_14
                $ luddites += 1
            "Send to the storehouse":
                $ colonists += 1
            "Slaughter for meat":
                $ pass #family happiness/food increase?
            "Allocate more land for goats":
                $ goats_index = get_crop_index("goats")
                $ crop_info[goats_index][MAXIMUM_INDEX] += 1
                # goats take up another square now.
    return

label goats2:
    "Making sausage out of goat/crabird meat. Charcuterie!"
    return

label goats3:
    "Making goat cheese?"

label goats4:
    "Your goats get out and destroy some neighboring farm land of someone else. What do you do?"
    return

label tomatoes1:
    $ tomatoes1_action = "none"
    "The tomatoes were looking so good, but a lot of them have sunken rotten areas on the bottom."
    menu:
        "Do some research":
            "Looks like blossom-end rot.  If I add some more calcium to the soil and water more evenly, this shouldn't happen next time."
            $ tomatoes1_action = "research"
        "Just cut it off":
            "Most of the tomato is fine.  I'm canning most of them, anyway, so who cares if I have to throw part away?"
            $ tomatoes1_action = "cut"
        "Add more fertilizer":
            "Next time I'll add more fertilizer; that should help."
            $ tomatoes1_action = "fertilize"
    return

label tomatoes2:
    $ tomatoes2_action = "none"
    if (tomatoes1_action == "research"):
        "The tomatoes look much better this year!"
        menu:
            "I can choose which fruits to save seeds from for planting next year."
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

    return

label plums1:
    "You don't get any harvest this year, but you tend your plums carefully."
    return

# Several years later
label plums2:
    "Finally, your spring is punctuated by beautiful pink blossoms on your plum trees."
    # Depending on pollination, you get a few or a lot of plums
    return

label beans1:
    "You had a good bean harvest this year.  Now that you've dried them, they will last a long time."
    return

label beans2:
    "It's been a cold spring. The bean plants haven't even germinated yet."
    return

label spinach1:
    "Your spinach is looking good!"
    menu:
        "Pick it early":
            "Yum, smaller, more tender greens, but less food."
        "Wait until it's fully grown":
            "Larger harvest. more bitter taste.  more food/less happiness"
    return

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
    $ spinach_cameras = False
    menu spinach_3_menu:
        "Check the surveillance cameras" if (not spinach_cameras):
            "You train the farm's cameras on the spinach plot, but the next day when you look at the video, none of the motion sensors were triggered.  You scan through the video but can't find anything that's eating them."
            "Looks like you'll have to find out the old-fashioned way."
            $ spinach_cameras = True
            jump spinach_3_menu
        "Check on your spinach at night":
            "After [kid_name] and [her_name] went to bed, you snuck out of the house to examine your spinach plants.  Your flashlight catches something small and slimy -- it looks like a slug!" #maybe these should be snails, since they might be able to deal with the radiation better? or am I overthinking it?
            menu:
                "Hand pick them off":
                    "You spend the night plucking off slugs and putting them in a bucket. And the next night.  And the next night.  There's fewer each night, but it's tedious work."
                    # TODO: Depending on Terra's age, maybe you enlist her help?
                    "Your reward is lots of great spinach."
                "Make slug traps":
                    "You put some tasty smelling bait in the middle of a hole covered with boards."
                    "In the morning, the hole was full of slugs, just waiting for you to murder them."
                    "You make some more traps and check them every morning."
                    "The slugs will regret their incursion into your domain."
                "Just pick the spinach early":
                    jump spinach_pick_early
        "Just pick the spinach early":
            jump spinach_pick_early

    return

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
    "Finally, their numbers are greatly reduced, and you can rest.  Until the next invasion..."
    return

label strawberries1:
    "Your strawberry plants did really well this year! Not only did you get extra strawberries, but you have enough runners that you could plant more next year if you wanted."
    $ strawberries_index = get_crop_index("strawberries")
    $ crop_info[strawberries_index][MAXIMUM_INDEX] += 1
