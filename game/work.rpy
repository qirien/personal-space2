## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting."
    return

label bad_nutrition:
    $ bad_nutrition_count += 1
    if (bad_nutrition_count == 1):
        scene farm_interior with fade
        show her concerned at midright
        show him determined at midleft
        if (has_strong_marriage()):
            her normal "[his_name], I wanted to thank you for always growing plenty of food for our family. We've always had enough to eat."
            him surprised "Oh. I'm glad you appreciate it."
            her concerned "But I'm worried that we are not eating a balanced diet with these foods. The human body needs more than 30 different vitamins, minerals, and nutrients."
        else:
            her concerned "[his_name], I don't want to tell you how to do your job..."
            him annoyed "Why do I get the feeling you're about to tell me how to do my job?"
            her annoyed "We can't live on just one or two foods! The human body needs more than 30 different vitamins, minerals, and nutrients."
        him angry "There's a lot of factors here! Sometimes crops fail, I have a limited amount of seeds, and I have to balance everything right or crops won't grow at all!"
        her concerned "I know, I'm sure you're doing the best you can. But it's especially important for the kids."
        him annoyed "They're not starving, right?"
        her annoyed "No. But I've made a list of deficiencies of our current diet and foods that could help meet them."
        him surprised "Don't we have vitamin supplements we could take?"
        her concerned "Right now they're by prescription only, for serious nutrition problems. I don't want us to get to that point."
        him determined "I guess I could buy some of these foods at the storehouse..."

        # are we using currency yet?
        if (year > 5):
            her determined "Or I could.  And maybe next year we can plant a better variety of vegetables and fruits so we don't need to spend our money on that."
            # TODO: subtract some money
        else:
            her determined "Or I could.  And maybe next year we can plant a better variety of vegetables and fruits so we don't need to trade as much."
        return

    if (bad_nutrition_count >= 3):
        # someone else has iodine deficiency. You trade them goat products for something with vitamin A/C
        # test for vitamin C
        if  (farm.low_vitamin_c() and farm.low_vitamin_a() and farm.low_magnesium()):
            "I felt like I was sick all the time. I had no energy, my gums were always bleeding, and I felt weak and cranky."
        elif (farm.low_vitamin_c()):
            "I felt weak and sore, like I was coming down with the flu."
            "It got bad enough that I decided to ask [her_name] about it."
            scene hospital with fade
            show her concerned at midright with dissolve
            show him concerned at midleft with moveinleft
            her concerned "You feel tired and sore, and have a low grade fever. On Earth I'd call this the flu, but..."
            him annoyed "The flu is not supposed to exist here."
            her surprised "Do you have any other symptoms? Sore throat, runny nose, cough, indigestion?"
            him normal "No, none of those. Well, maybe a little stomachache, but I ache all over."
            her determined "Here, let me check your gums..."
            him annoyed "Ow!"
            her concerned "Gums bleed easily... let me look at your skin..."
            him surprised "Oh, where did that bruise come from? I don't remember getting hurt..."
            her determined "You have scurvy."
            him normal "Scurvy? Like, scurvy-sea-dog scurvy?"
            her annoyed "Like, someone didn't plant enough fruits and vegetables scurvy."
            him surprised "How come you and [kid_name] don't have it?"
            her concerned "I don't know... we eat a lot of the same foods... though I think we get more applesauce since sometimes Helen will bring some in."
            him annoyed "And you don't share it with me?!"
            her annoyed "There's not very much... Anyway, here's some vitamins -- they should help you start feeling better in a few days. And next time, try planting more peppers, squash, or broccoli. Even potatoes have some vitamin C in them."
            him happy "Yeah, I guess I should. Man, I'm totally a pirate now!"
            her flirting "Don't go bragging about it or everybody will want to get scurvy."
            him flirting "I don't think that's something we need to worry about."

        elif (farm.low_vitamin_a()):
            scene farm_interior with fade
            show him determined at midright with dissolve
            "My skin was always dry and for some reason I couldn't see well at night."
            "I didn't think to ask [her_name] about it, though, until she came to me."
            show her concerned at midleft with moveinleft
            her concerned "[his_name]... have you been having trouble seeing at night?"
            him surprised "Yeah, how did you know??"
            her determined "I have the same problem, and I think [kid_name] does, too."
            him concerned "Do you know why? Is it a disease? Some kind of alien parasite?"
            her annoyed "No. I'm pretty sure we haven't been getting enough vitamin A."
            him surprised "Vitamin A?"
            her determined "Yes. I got us all a supplement from the clinic for now, but you need to plant more vegetables, like carrots, squash, and spinach."
            him concerned "Aw man, I hate pills."
            her annoyed "Which do you hate more: pills, or being able to see?"
            him surprised "It's that bad?"
            her angry "Yes! Prolonged vitamin A deficiency can lead to blindness in kids!"
            him angry "Okay, okay! I'll try and plant better crops next time."
            her sad "Sorry, [his_name]. I know you're doing the best you can..."
            him determined "If it's not good enough, I'll do better."

        elif (farm.low_magnesium()):
            scene farm_interior with fade
            show her concerned at midright
            show kid concerned at center
            if (bro_age > 0):
                show bro at quarterleft
            show him concerned at midleft with dissolve
            her annoyed "I just can't take it anymore!!"
            him surprised "Whoa, whoa, calm down."
            her angry "I'm supposed to be calm?! This is insane! How did we ever think living here was going to work?!"
            him concerned "I thought it was working pretty well..."
            kid surprised "Mom, are you okay?"
            her sad "I don't know what's wrong with me... I just feel so crazy lately."
            him determined "You have been a bit more... volatile."
            her concerned "I can't stop worrying and I just feel so stressed out all the time but I don't even have that much to be stressed out about!"
            kid concerned "Are you sick?"
            her surprised "I... I don't think so, but... now that you mention it, there are some conditions that can cause these symptoms..."
            him surprised "Are there some tests you can run?"
            her concerned "Yeah... will you come with me?"
            # TODO: finish this

        else:
            "I couldn't pinpoint exactly what was wrong with my crops, but I felt sluggish and had low energy."


    # fall through for times without a special event.
    "The crops I planted didn't provide the vitamins and minerals we needed."

    if (year > 5):
        "I had to spend money at the storehouse to buy better food."
        # TODO: currency check, subtract some money
    else:
        "I had to trade with other farmers to get better food."
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
# Help Kevin and Zaina and get a plum tree
label work2:
    scene farm_interior with fade
    show him normal at midleft
    show her normal at midright
    show kid normal at midright, baby_pos
    with dissolve
    her surprised "Are you going somewhere?"
    him determined "Yeah, I said I'd help Kevin and Zaina with their garden."
    her flirt "It wasn't as easy as the video games made it seem, huh?"
    him happy "Yeah, turns out there's actually a lot of things that you can't learn just from simulations!"
    her normal "All right, good luck."
    show path with fade
    "I headed off towards the mountains. I could just barely see their house from our land, but it took me a while to walk there."
    show farm with fade
    show kevin at midright
    show zaina at center
    with dissolve
    show him normal at midleft with moveinleft

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

    # TODO: Have a little tutorial about how you can't move plums once they're planted, and how they take less work in future years.
    $ enable_crop("plums")
    return


# Year 4, 2 years old
# Show off at the Fall Festival or increase the size of your farm?
label work4:
    nvl clear
    pavel_c "The Fall Festival will be next weekend! Show off your best crops and animals. There will be games and music, too!"
    sara_c "I hope everyone can come!"
    nvl clear
    him "Hmmm... I was going to get a new field ready to expand the size of my farm, but I always like to go to the Fall Festival..."
    $ random_crop = farm.crops.random_crop(include_animals = False)
    $ work4_showoff = False
    menu:
        "What should I do?"
        "Show off my [random_crop] at the festival.":
            $ work4_showoff = True
            "It was fun to show off my hard work. And it was a good chance to hang out with the other farmers and see what they were doing."

        "Go, but don't bring anything.":
            "I didn't want to miss the Fall Festival. I worked hard to prepare and plow one new field, and then I headed over."
            $ farm_size += 1
            tutorial "Your farm is now size [farm_size]!"

        "Don't go. Expand fields instead.":
            $ farm_size += 4
            "The festival was fun, but my farm was more important. Maybe I'd go next year..."
            "I worked hard to rip out the native vegetation and plow the new fields."
            tutorial "Your farm is now size [farm_size]!"
            return

    scene bg community_center with fade
    show natalia at quarterleft
    show pete at center
    show thuc at quarterright
    show goat at right
    with dissolve
    show him normal at left with moveinleft
    "Everyone brought their best crops to display."
    "Natalia had beautiful ears of corn, and free samples of corn on the cob."
    show him surprised at midleft with move
    "Pete brought several kinds of cheeses and cider."
    show him normal at midright with move
    "Thuc brought the cutest baby goat I've ever seen. His daughter had taught it to stand on its hind legs, bleat, and jump through a hoop."
    thuc "This goat is almost as smart as [kid_name]!"
    him happy "And probably more obedient!"

    if (work4_showoff):
        thuc "Hey, is that your [random_crop] on display over there?"
        him normal "Yes it is!"
        thuc "They turned out really well. How often do you fertilize them?"
        "We talked about [random_crop] for a while, and then I had an idea."
        him surprised "Hey, do you want some seeds for [random_crop]?"
        thuc "They grow pretty well?"
        him normal "Yeah!"
        thuc "Sure, that would be great. Do you want a strawberry plant?"
        him surprised "Strawberries?"
        thuc "Yeah, they're pretty easy and they come back every year so they don't take much work. We don't usually get a lot of them but the kids love them."
        him happy "Sure, thanks!"
        tutorial "You can now grow strawberries!"
        #$ enable_crop("strawberries")
    return

# Year 6, 3.5 years old
# Terra begins to help!
label work6:
    scene farm_interior with fade
    show her normal at midright
    show kid normal at center
    show him normal at midleft
    with dissolve
    $ random_crop = farm.crops.random_crop(include_animals = False)
    him normal "Well, I'm off to plant [random_crop] today."
    kid surprised "Is it fun?"
    him concerned "Kind of? Not as fun as harvesting, but you do get to dig in the dirt and drop in seeds..."
    kid nervous "Can I help?"
    him surprised "Sure, if you want to."
    "I'd had [kid_name] help me out on the farm before -- mostly harvesting, or just digging in the dirt 'helping' me while I got the real work done."
    "But she was getting old enough to be slightly more of a help than a hindrance, for some things."
    scene farm_exterior with fade
    show him normal at midright
    show kid normal at midleft
    with moveinleft
    him normal "First we have to give the goats water."
    kid laugh "I'll help!"
    him determined "Here, you can fill it up with the pump."
    "It took all her strength to lift the pump handle, and she had to hang on it with her whole weight to get it to come down, but she did it."
    show kid concerned with dissolve
    "She tried to carry the bucket, but it was too heavy."
    him "Here, I'll carry the bucket. You carry the seeds."
    kid happy "Okay, daddy!"
    hide him
    hide kid
    with moveoutright

    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    with moveinleft
    him normal "I'll poke a hole in the dirt, and you put three seeds in, okay?"
    kid surprised "Okay...One, two, free!"
    him happy "Good!"
    "We worked together all afternoon. When she got tired, I let her play in the dirt at the end of a row while I worked. I'm not sure if she helped me be any faster, but she was excited to make plants grow."

    tutorial "You can now choose how much [kid_name] helps on the farm. Her effectiveness depends on her {color=#ff0}competence{/color}."
    tutorial "And, her competence increases as she helps." # TODO: does it?
    return

# Year 8, 4.8 years old
# The outhouse is full...
label work8:
    scene farm_exterior with fade
    "Here's one thing not everyone gets about being a farmer."
    "I'm not just a farmer; I take care of {b}everything{/b}."
    "So I'm also a carpenter, vet, trucker, landscaper, and handyman, as needed."
    "But today I'm a plumber."
    "The outhouse was one of the first things we built when we moved here. Most of the time I didn't even think about it."
    "But lately..."
    him annoyed "Ugh, that smell!"
    "I had an exhaust pipe that was supposed to pipe the noxious fumes outside, but for some reason it wasn't working."
    him determined "Time to figure out the problem."
    "I checked the top of the pipe. It didn't seem to be clogged at all."
    "I didn't want to, but I had to check the other side of the pipe. The one inside the pit."
    "I lifted off the seat and the top panel, and it was immediately obvious what had happened."
    him surprised "Our outhouse is full!"
    "It was so full that it had started blocking the exhaust pipe."
    "I sat down and thought for a few minutes. I had a few choices..."
    $ work8_choice = ""
    menu:
        "What should I do?"
        "Clean out the pit.":
            $ work8_choice = "clean"
            "It was a gross job, but the best thing to do was just clean out the pit. Then I could keep using this same outhouse."
            "Since we had been adding some ashes to the pit after using it, the sewage had started decomposing, but it was still sewage. I tied a handkerchief over my nose and mouth to cut the smell down."
            "I borrowed an auger from the community tool library and used it to transport everything up and into my wheelbarrow."
            "When the wheelbarrow was full, I dumped the waste in a far corner away from fields and water sources. Eventually it would be good fertilizer, but it hadn't decomposed enough yet."
            "Then I went back for another load."
            "It took all day..."
        "Relocate the outhouse.":
            $ work8_choice = "relocate"
            "There was no way I was going to clean out the pit of the outhouse."
            "We had plenty of land; I'd just build a new pit somewhere else and move the outhouse structure on top of it. Then I could bury the waste in the old pit and let Mother Nature take care of it for me."
            "First, I dug a new pit."
            "Then I took apart the outhouse so it I could carry it over piece by piece and put it back together again."
            "I covered the old pit with the dirt from the new one."
            "It took all day..."
        "Build a better outhouse that provides fertilizer." if (get_extra_work() >= 0):
            $ work8_choice = "improve"
            "I remembered Thuc telling me about how they had a special treatment regimen that allowed them to treat sewage from their pit and use it as fertilizer."
            "I could always use more fertilizer, and this would also make it so I wouldn't have to clean out the outhouse in the future, either."
            "He sent me some plans and a short book on the subject. I didn't even notice it was written by his wife, Julia, until I finished reading it."
            "I ended up building a new outhouse on top of a small hill, with a container for the waste that could be rotated."
            "I built a couple of containers so that two could be decomposing into compost while the other was being actively used."
            "It took several days, and the new outhouse would be a bit more work to maintain, but I felt like it was worth it to solve the problem the right way."

    scene farm_interior with fade
    show her normal at midright
    show kid normal at center
    with dissolve
    show him concerned at midleft with moveinleft
    her concerned "You look beat. And you smell like..."
    kid surprised "Like poop!"
    him determined "Yeah... the outhouse was full."
    her surprised "Oh! I guess that would happen eventually..."
    if (work8_choice == "clean"):
        him concerned "I mucked the whole thing out."
        kid angry "Gross!"
        her concerned "Wow... that sounds awful."
    else:
        him concerned "I had to build a new one."
        her normal "Okay, wow, that sounds like a lot of hard work."

        him normal "It's done now, anyway."
        if has_strong_marriage():
            her normal "Why don't you go take a bath and I'll make dinner tonight?"
            kid shifty "{b}I{/b} don't need a bath."
            him happy "Then you can help Mom with dinner. I'll be back soon!"
        else:
            her concerned "Well...thanks."
            kid shifty "You need a bath!"
            him surprised "I do need a bath! And then I'll come home and make dinner. Unless Mom wants to do it...?"
            her annoyed "Yeah, I'll make dinner. I don't want to wait that long."
            him happy "Thanks, sweetie!"

    return

# Year 10, 6.2 years old
# Bees?!
label work10:
    scene community_center with fade
    show kevin at midright
    show him normal at midleft
    with dissolve
    if (farm.crop_enabled("plums") or farm.crop_enabled("plums+")):
        kevin "[his_name]. How are your plum trees?"
        if "plums+" not in farm.crops:
            if "plums" in farm.crops: # we just barely planted plums, but it didn't work.
                him concerned "I tried to plant them a couple weeks ago, but they didn't germinate. It had probably been too long."
                kevin "Yes, that is possible."
            else:
                him concerned "I, uh, I'm afraid I never planted them."
                kevin "I see. They are most likely no longer viable."
        $ disable_crop("plums")
        $ disable_crop("plums+")

    him "How's your garden coming, Kevin?"
    kevin "It does provide some food, but I have noticed that plants here have an average of a 25% smaller yield than plants on Earth."
    him concerned "There could be several reasons for that..."
    kevin "After factoring out other issues such as soil quality, solar flares, and unreported crops, I have come to a conclusion."
    him surprised "What's that?"
    kevin "We need more pollinating insects. The native fauna of Talaam have not evolved to pollinate our plants."
    him normal "Like bees?"
    kevin "Precisely. Several colonies of bees are arriving on the next shuttle. I fear it is too many for my small garden. Would you be willing to reserve some land for them on your farm?"

    menu:
        "What should I say?"
        "Sure, I'd love bees!":
            him happy "I'd love bees! Better pollination, honey, that sleepy buzzing sound on summer afternoons..."
            kevin "Very well. I shall mark you down for bees."
            $ enable_crop("bees")
            tutorial "You can now assign bees to one of your plots of land."
            tutorial "They will boost production of neighboring squares and require just a little work."
            tutorial "However, once placed, they cannot be moved."
        "No thanks.":
            him concerned "No thanks; I already have enough to worry about."
            kevin "Very well. I shall ask someone else."
    return

# Year 12, 7.4 years old
label work12:
    nvl clear
    brennan_c "I have a special offer for all you farmers out there."
    julia_c "Oh, this'll be good."
    sara_c ":-O"
    pete_c "Let the man talk."
    brennan_c "I have the newest pest-resistant, high-yield, nutirent-packed wheat seeds from Earth. They grow fast, they don't need much water, and they can thrive in almost any climate."
    thuc_c "That sounds good, but..."
    julia_c "What's the catch?"
    brennan_c "Well, because they're a patented seed design, the wheat berries they produce are sterile."
    julia_c "Meaning we couldn't save some seeds to plant next year."
    brennan_c "Right. You'd need to buy them from me. Well, from RET, really."
    if (community11_kidsonfarm):
        natalia_c "Hmm, I might get some for Joanna to try. If they're as good as you say..."
    else:
        natalia_c "Hmm, I might have to try those, if they're really as easy to grow as you say..."
    brennan_c "Well, that's the thing. If you're going to grow them, you need to sign a 20 year contract. We have a set amount and we need reliable buyers."
    natalia_c "Twenty years? Some of us might not even be alive then."
    brennan_c "Twenty Talaam years. More like 12 Earth years. You'd agree to pay us a certain amount every year and we'll provide you with seeds." # TODO: currency check, how much?
    julia_c "That's ridiculous. Who would want to rely on you for their seeds?"
    brennan_c "You're a tough customer, Julia, but let's let everyone decide for themselves. Come see me if you want in on this great deal."
    nvl clear
    menu:
        "What should I do?"
        "Sign a wheat contract.":
            $ miners += 1
            scene miners_camp
            show brennan at midright with dissolve
            show him at midleft with moveinleft
            him normal "I'm interested in the wheat."
            brennan "Good, good. Seems like you're smarter than you look."
            him annoyed "Don't make me change my mind."
            brennan "Ah, can't you take a joke?"
            him determined "..."
            brennan "...Right. Here's your wheat."
            $ enable_crop("wheat")
            # TODO: implement annual fee
            # you sold your soul but can now grow wheat.
        "Don't sign a wheat contract":
            $ luddites += 1
            him_c "No thanks, Brennan."
            "Later, Natalia came over for a visit."
            natalia "I need something for my farm that's easier to grow. Do you have any suggestions?"
            him "You've been growing corn, right?"
            natalia "Yes, and it's quite time-intensive."
            him "Have you tried potatoes?"
            natalia "No, do they do well here?"
            him "As long as you keep them dry, they're great! Do you want some seed potatoes to get started?"
            natalia "Oh, you're too kind. That would be wonderful. I have seed corn, if you'd like some in exchange."
            him "That would be great!"
            $ enable_crop("corn")

    "I was looking forward to growing something new."
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
