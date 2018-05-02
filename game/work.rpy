## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting."
    return

# Year 1, 3 mo. old
label work_intro:
    scene fields with fade
    "[kid_name] wasn't the only thing I was taking care of, though. I was also responsible for our entire farm."
    "Over the past two years, with a lot of trial and error, I'd found crops and varieties that worked well."
    "I still had a lot of decisions to make, though, from how much of each crop to plant, to what field it should be planted on, to how to deal with problems."
    menu:
        "Would you like to see the Farming Tutorial?"
        "Yes.":
            # TODO: Show screenshots to illustrate this.
            "The middle of the screen shows the farm layout."
            "On the right is the current farm's stats."
            "Below that, I can choose what crops should go where."
            "On the left, I can see stats for the selected crop."
            "I need a certain amount of calories, and I only have a certain amount of work I can do. Other than that, I can choose whatever crops I want."
        "No.":
            $ pass
    return

# Year 2, 9 months old
label work2:
    scene farm_interior with fade
    show him at midleft
    show her at midright
    show kid at center
    with dissolve
    her surprised "Are you going somewhere?"
    him determined "Yeah, I said I'd help Kevin and Zaina with their garden."
    her flirting "It wasn't as easy as the video games made it seem, huh?"
    him happy "Yeah, turns out there's actually a lot of things that you can't learn just from simulations!"
    her normal "All right, good luck."
    show path with fade
    "I headed off towards the mountains. I could just barely see their house from our land, but it took me a while to walk there."
    show farm with fade
    show kevin at midright
    show zaina at center
    with dissolve
    show him at midleft with moveinleft

    zaina "Thanks for coming, [his_name]. I can't believe I ever thought growing my own food would be easy!"
    him "Well, some parts aren't too hard. But it helps if you know what you're doing."
    "I walked through their fields with them, pointing out plants that needed different location, or different irrigation, or different nutrients in the soil. Some were more sensitive to solar flares than others, too."
    kevin "This information was not in the farming guide I was given."
    him "Yeah, you can't learn everything about alien farming from a book."
    kevin "That is unfortunate. Perhaps such a book should be made."
    him "If you want to write it, go right ahead."
    zaina "I think we'll be too busy taking care of these plants to write much about it right now!"
    kevin "Perhaps at a future time."
    zaina "Anyway, thanks for helping us out. Our trees didn't bear many plums, but here's a few of the ones we got. Maybe you can plant the seeds after you eat them?"
    him surprised "Plums? That'll be delicious; thank you!"
    zaina "Thank you, [his_name]!"

    # TODO: Finis this, make plums permanent, use plums+ in future years.
    # Have a little tutorial about how you can't move plums once they're planted, and how they take less work in future years.
    $ enable_crop("plums")
    return


# Year 4, 2 years old
label work4:
    "Want some bees? They'll permanently use one square but will yield honey with a moderate amount of work and may increase yield of some other squares."
    return

# Year 6, 3.5 years old
label work6:
    "You can now have [kid_name] help on the farm. Her effectiveness depends on her competence."
    "And, her competence increases as she helps."
    return

# Year 8, 4.8 years old
label work8:
    "Your family reacts to crops you've been planting."
    return

# Year 10, 6.2 years old
label work10:
    "Do you participate in the seed exchange with one faction or expand your farm with a different faction?"
    return

# Year 12, 7.4 years old
label work12:
    "You had a decent harvest, but a salesman from RET offers some hybrid wheat seeds that he claims will be the most productive crop you've ever seen."
    "The only problem is, the seeds are infertile, so you'd have to buy them every year."
    "In fact, he'll only sell them to you if you sign a contract to buy some from him every year for the next ten Talaam years."
    menu:
        "Sign a wheat contract?"
        "Yes":
            $ colonists += 1
            # you sold your soul but can now grow wheat.
        "No":
            $ luddites += 1
            # the luddites approve and offer to get you started with some of their heirloom wheat instead. It's not as good - more work, less yield

    return

# Year 14, 8.7 years old
label work14:
    "Take your daughter to work day... is every day."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "She is pretty helpful and gets a lot done!"
    elif (style == "authoritarian"):
        "She does every thing you ask, but you have to ask her to do each little thing. She doesn't take any initiative to do things on her own."
    else:
        "She sulks and you have to threaten and cajole her to do anything.  It would have been faster to do it yourself!"
    "Terra helps out with some simple things, but she isn't very good at it. Do you redo it, make her redo it, or spend some time teaching her better? Do you have her help in the future?"
    return

# Year 16, 10 years old
label work16:
    "Do you participate in the seed exchange with one faction or expand your farm with a different faction?"
    return

# Year 18, 11.1 years old
label work18:
    "Add on addition to the house as family grows and Terra needs her own space?"
    return

# Year 20, 12 years old
label work20:
    "Miners want cheap/fast/calorie-dense food. Will you cater to their needs?"
    "Also, Terra likes it as she is eating more and growing taller than ever."
    return

# Year 22, 13.6 years old
label work22:
    "Someone from your favorite faction gives you cool seeds!"
    return

# Year 24, 14.8 years old
label work24:
   "Terra accidentally flips the tractor over while doing her chores, and gets hurt."
   "[her_name] argues that you shouldn't have her do such dangerous chores."
   menu:
       "That's the only way to learn!":
           $ pass
       "You're right":
           $ pass
       "I just need to teach her better.":
           $ pass
   "This turns into an argument about Terra's future - [her_name] doesn't want her stuck on this backward planet working on a farm for the rest of her life, and you ask 'what's wrong with working on a farm for the rest of your life?!'"
   "The truth is [her_name] still misses Earth and wants Terra to be able to experience it.  Discussion about college/training/future."
   return

# Year 26, 16.1 years old
label work26:
    "You throw out your back."
    "People from your favorite faction and your family help you, or not."
    return

# Year 28, 17.3 years old
label work28:
    "Terra either wants her own farm, or wants to quit working for you! Do you hire someone else or try and get her to stay?"
    return

# Year 30, 18 years old
label work30:
    "Summary of how awesome your farm is (or not)"
    return
