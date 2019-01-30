## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting."
    $ enable_crop("squash")
    return

# Malnutrition Event for if you don't have enough nutrition
label bad_nutrition:
    $ bad_nutrition_count += 1
    if (bad_nutrition_count == 1):
        scene farm_interior with fade
        show her concerned at midright
        show him determined at midleft
        if (has_strong_marriage()):
            her normal "[his_name], I wanted to thank you for always growing plenty of food for our family. We've always had enough to eat."
            him surprised "Oh. I'm, uh, glad you appreciate it."
            $ common_food = farm.most_frequent_crop()
            her concerned "But I'm worried that we are not eating a balanced diet with these foods. The human body needs more than 30 different vitamins, minerals, and nutrients. We can't get all those with just [common_food]."
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
        him determined "I guess I could get some of these foods at the storehouse..."

        # are we using currency yet?
        if (year > 5):
            her determined "Or I could.  And maybe next year we can plant a better variety of vegetables and fruits so we don't need to spend our money on that."
            # TODO: subtract some money
        else:
            her determined "Or I could.  And maybe next year we can plant a better variety of vegetables and fruits so we don't need to trade as much."
        return

    if (bad_nutrition_count >= 3):
        # All nutrients low
        if  (farm.low_vitamin_c() and farm.low_vitamin_a() and farm.low_magnesium() and (not seen_low_cam)):
            $ seen_low_cam = True
            "I felt like I was sick all the time. I had no energy, my gums were always bleeding, and I felt weak and cranky."
            "Finally, I went to see [her_name]."
            him determined "Help me, doc."
            her concerned "What's wrong?"
            him concerned "I don't know; maybe it's nothing. I just feel like I'm a little bit sick all the time."
            her determined "Oh, really?"
            him sad "Yeah. So if I'm just making it up, tell me and I'll get back to work. But if there is something wrong, maybe you can help me."
            $ common_food = farm.most_frequent_crop()
            her angry "I know exactly what's wrong with you!  You've been eating nothing but [common_food] and your body's sick!"
            him surprised "This is all from my diet?"
            her annoyed "Yes, I warned you about this!"
            him sad "Oh."
            her concerned "..."
            him concerned "Are the kids okay?"
            her annoyed "Yes, I've been supplementing their diet."
            him annoyed "But not mine."
            her angry "No! I wanted you to understand how serious this is!"
            him surprised "Can't we just buy what we need from the storehouse?"
            her annoyed "Yes, but it gets expensive. Here's a list."
            "She had made a list of foods we needed to buy."
            # TODO: currency check
            him concerned "Sorry, [her_name]. I feel like I failed you."
            her determined "We're all alive and kicking, so no one's failed yet. Just... please try better next time, okay?"

        # Low Vitamin A & C
        elif (farm.low_vitamin_c() and farm.low_vitamin_a() and (not seen_low_ca)):
            $ seen_low_ca = True
            # someone else has iodine deficiency. You trade them goat products for something with vitamin A and C
            "I hadn't been feeling well lately. I had no energy and it was harder to see at night."
            "I wondered if I should ask [her_name] about it, but I figured she'd probably just tell me to eat better."

            nvl clear
            her_c "I've seen several people lately with nutrient deficiencies. If you don't have much dairy, eggs, or seafood in your diet, you may be at risk for iodine deficiency."
            "Hmmm, we eat plenty of goat's milk so that's probably not what's bothering me."
            her_c "Here's a list of other deficiencies and foods you can eat to remedy them."
            pete_c "I've got cow's milk, if anyone would like to trade."
            him surprised "Trading would be more efficient than buying from Ilian..."
            "Looking at the crops I was growing and my symptoms, I figured I was probably low on vitamins A and C."
            "If I could trade with someone that needed iodine, it would be great."
            him_c "Looking to trade goat's milk for vitamin A and C foods."
            natalia_c "I'll trade you bell peppers and squash for those."
            pete_c "I thought you grew squash and peppers, [his_name]?"
            if ("squash" in farm.crops):
                him_c "Not enough, apparently."
            else:
                him_c "Not this year. Maybe next year, though."
            pete_c "Natalia, I'd like the same trade for cow's milk if you have enough."
            natalia_c "Sure; I'll bring tomatoes, too."
            if (whole_harvest_required):
                ilian_c "Shouldn't you be bringing all that to the storehouse?"
                if is_liason:
                    "He caught me there. I was being pretty hypocritical, going around the system I was telling everyone else to follow."
                    menu:
                        "What should I say?"
                        "You're right.":
                            him_c "You're right, Ilian. Sorry, guys, I'm going to have to back out. I'm taking the goat's milk to the storehouse where you can buy it from Ilian."
                            # TODO: currency check?
                            "I ended up paying a premium for peppers and squash for the family diet."
                            return
                        "We should only bring extra.":
                            him_c "You know; I've changed my mind. We shouldn't have to do that. Everyone should just bring their extra to the storehouse."
                            $ rationing = True
                            $ require_whole_harvest = False
                            ilian_c "Really? You're changing it, just like that?"
                            him_c "Being the liason has to be good for something."
                            natalia_c "I'm not complaining."
                        "(Don't say anything)":
                            "I didn't say anything. Everyone knew that requirement was mostly for show, right?"
                            $ luddites += 1
                            $ colonists -= 1
                            $ miners -= 1
                else:
                    sara_c "He's right. If you have extra, bring it to the storehouse and we can distribute it fairly. 😥"
                    pete_c "And at a high price."
            nvl clear
            "I was glad I was able to work out a trade this time. Next time, though, I might not be so lucky."

            # test for vitamin C
        elif (farm.low_vitamin_c() and (not seen_low_c)):
            $ seen_low_c = True
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

        elif (farm.low_vitamin_a() and (not seen_low_a)):
            $ seen_low_a = True
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

        elif (farm.low_magnesium() and (not seen_low_m)):
            $ seen_low_m = True
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
            if (has_strong_marriage()):
                him concerned "Of course."
                scene hospital with fade
                show her concerned at midright
                show him concerned at center
                show kid concerned at quarterleft
                if (bro_age > 0):
                    show bro at midleft
                with moveinleft
                her determined "I just need to swab under my tongue..."
                kid surprised "Does it hurt?"
                her annoyed "No, it's just...awkward... here, [his_name], you do it."
                him surprised "Oh! Uh, okay..."
                her determined "Just scrape it a little. Right here."
                "She opened her mouth and held still. [kid_name] watched, fascinated."
                him determined "Okay, done. Hopefully I did that right."
                her annoyed "It'll do. If this doesn't turn up anything we'll need blood and urine samples."
                him surprised "Hopefully you don't need me to help with those."
                her "It'll take a few minutes for me analyze the spectrometer's results."
                "I talked with kid_name while we waited for [her_name] to finish."
            else:
                him concerned "I'll stay here with the kids while you do it."
                her sad "Okay..."
                hide her with moveoutleft
                "She was gone for about an hour."
                show her at midright with moveinleft
            her concerned "This confirms it. I have a magnesium deficiency."
            him surprised "Magnesium??"
            her determined "Yes. Normally we get plenty from nuts, beans, and eggs. But we haven't been eating many of those lately."
            him sad "Probably because I didn't plant enough..."
            her concerned "Yes, well... you probably all have it, too, so you'll need to take this supplement."
            him surprised "Why didn't we notice this earlier?"
            her determined "The symptoms are so subtle that it's usually hard to detect until it starts to cause more severe problems, like diabetes or heart failure."
            him normal "Well then, I'm glad you caught it."
            her normal "This supplement is just a short-term solution. We'll need to buy some beans or nuts."
            him determined "Okay."
            # TODO: currency check
        return

    # fall through for times without a special event.
    "The crops I planted didn't provide the vitamins and minerals we needed."

    if (year > 5):
        "I had to spend money at the storehouse to buy some different foods."
        # TODO: currency check, subtract some money
    else:
        "I had to trade with other farmers to get a better variety of food."
    return

# TODO: Have an event for not making enough money

# Year 1, 3 mo. old
label work_intro:
    scene fields with fade
    "[kid_name] wasn't the only thing I was taking care of, though. I was also responsible for our entire farm."
    "Over the past two years, with a lot of trial and error, I'd found crops and varieties that worked well."
    "I still had a lot of decisions to make, though, from how much of each crop to plant, to what field it should be planted on, to how to deal with problems."
    call farm_tutorial
    return

label farm_tutorial:
    # TODO: Show screenshots to illustrate this.
    menu:
        "Would you like to see the Farming Tutorial?"
        "Yes.":
                "The left part of the screen shows information about my family and colony."
                "The middle of the screen shows the farm layout."
                "On the right is the current farm's stats."
                "When I click on a farm space, I can choose what crop should go there and see information about each crop."
                "The background color of each space shows how much nitrogen is in this field. If it's a dark color, there's plenty of nitrogen for crops."
                "If it's a light color, nitrogen in that field is running low. I should put something there that will add nitrogen, like goats or beans, or I can leave the field fallow to rest."
                "I need a certain amount of calories, and I only have a certain amount of work I can do. Other than that, I can choose whatever crops I want."
                if (year > MONEY_YEAR):
                    "Some crops are worth more money than others. If I don't choose crops well, I could end up losing credits."
                "That's it for the farming tutorial."
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
    her flirting "It wasn't as easy as the video games made it seem, huh?"
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
    sara_c "I hope everyone can come! 😊"
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
        thuc "Hey, are those your [random_crop] on display over there?"
        him normal "Yes it is!"
        thuc "They turned out really well. How often do you fertilize them?"
        "We talked about [random_crop] for a while, and then I had an idea."
        him surprised "Hey, do you want to grow your own [random_crop]?"
        thuc "You'd help me get started?"
        him normal "Yeah!"
        thuc "Sure, that would be great. Do you want a strawberry plant?"
        him surprised "Strawberries?"
        thuc "Yeah, they're pretty easy and they come back every year so they don't take much work. We don't usually get a lot of them but the kids love them."
        him happy "Sure, thanks!"
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
    kid annoyed "No! I want to carry the bucket!"
    "She staggered a few steps with the bucket and it dropped, spilling half the water onto the ground."
    him "Let's try that again..."
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
        "Build a better outhouse that provides fertilizer." if (get_extra_work() > 0):
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
    if (crop_enabled("plums") or crop_enabled("plums+")):
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
    else:
        him "Pretty good! We're even starting to get a few plums on them."
        kevin "That is good."

    him "How's your garden coming, Kevin?"
    kevin "It does provide some food, but I have noticed that plants here have an average of a 25\% smaller yield than plants on Earth."
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
            $ enable_crop("honey")
            tutorial "Bees will boost production of neighboring squares and require just a little work."
            tutorial "However, once placed, they cannot be moved."
            # TODO: implement these!!
        "No thanks.":
            him concerned "No thanks; I already have enough to worry about."
            kevin "Very well. I shall ask someone else."
            "I didn't have room or time for bees."
    return

# Year 12, 7.4 years old
# Brennan's GMO sterile wheat
label work12:
    scene farm interior with fade
    show him determined at center with dissolve
    nvl clear
    brennan_c "I have a special offer for all you farmers out there."
    julia_c "Oh, this'll be good."
    sara_c "😲"
    pete_c "Let the man talk."
    brennan_c "I have the newest pest-resistant, high-yield, nutrient-packed wheat seeds from Earth. They grow fast, they don't need much water, and they can thrive in almost any climate."
    thuc_c "That sounds good, but..."
    julia_c "What's the catch?"
    brennan_c "Well, because they're a patented seed design, the wheat berries they produce are sterile."
    julia_c "Meaning we couldn't save seeds to plant next year."
    brennan_c "Right. You'd need to buy them from me. Well, from RET, really."
    if (community11_kidsonfarm):
        natalia_c "Hmm, I might get some for Joanna to try. If they're as good as you say..."
    else:
        natalia_c "Hmm, I might have to try those, if they're really as easy to grow as you say..."
    brennan_c "Well, that's the thing. If you're going to grow them, you need to sign a 20 year contract. We have a set amount and we need reliable buyers."
    natalia_c "Twenty years? Some of us might not even be alive then."
    brennan_c "Twenty Talaam years. More like 12 Earth years. You'd agree to pay us a certain amount every year and we'll provide you with seeds." # TODO: currency check, how much?
    julia_c "That's ridiculous. Who would want to rely on you for their seeds?"
    brennan_c "You're a tough customer, Julia; I love that about you! But let's let everyone decide for themselves. Come see me if you want in on this great deal."
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
# Milking Goats
label work14:
    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    "I never realized how much I knew about farming until I had to teach someone else."
    "Even though she grew up on our farm, there was still so much [kid_name] didn't know."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "...but she's learning fast!"
        "I love seeing her grow more independent. When she's done feeding the goats, she doesn't sit around waiting for me to tell her what to do."
        "She looks around and starts doing whatever is needed, whether it's a fence that needs repairing, weeds that need to be pulled, or produce that needs to be harvested."
        "Sometimes she's a little too independent."
        kid "I want to milk the goats!"
        him surprised "You do?"
        kid "Yeah! I bet I can do it all by myself!"
        "She'd watched me many times, but the technique is a little tricky."

    elif (style == "authoritarian"):
        "...like how to do what needs to be done without me having to tell her every detail."
        "She's pretty good at feeding the goats every day, but when she's done I'll often find her playing with them instead of moving on to what really needs to be done."
        "But I really wanted her to learn how to milk the goats."

    else:
        "...like how to work hard."
        "I don't know if she doesn't remember or just doesn't care, but she 'forgets' to feed the goats all the time."
        "And it seems like whenever there's work to be done, she's nowhere to be found."
        "I often end up just doing it myself. It's faster and less of a hassle."
        "But I really wanted her to learn how to milk the goats."

    him normal "You're old enough to learn how to milk goats. Come with me."
    scene barn with fade
    show goat at center
    show him normal at midright
    show kid normal at midleft
    with moveinleft
    "I showed her how to lead the goat to the milking stand, wash off her udder, and set up some food for her."
    "I helped her practice the finger motions needed to squirt the milk into the bucket."
    "She was tentative at first, but she seemed to be figuring it out."
    "I left for a minute to check on something, but I wasn't gone for more than five minutes when I heard a scream."
    hide him with moveoutright
    "I dashed back into the barn and saw [kid_name] crying, the bucket tipped over, and the goat lying down, looking quite satisfied."
    show him at midright with moveinright

    menu:
        "What should I do?"
        "Scold [kid_name]":
            him angry "[kid_name]!"
            $ demanding += 1
        "Ask what happened":
            him surprised "What happened here?"
        "Help her clean it up":
            "I righted the bucket and lifted the goat up to standing. We found a towel and mopped up the milk."
            $ responsive += 1

    kid cry "It's not my fault! It's that stupid goat! I was almost done and then she just lied down and messed it all up!"
    him annoyed "That's because she ran out of food. You've got to be faster than that."
    kid annoyed "Well how was I supposed to know that?!"

    menu:
        "What should I do?"
        "Show her how to do it right." if (get_extra_work() > 0):
            him normal "It's okay, it takes some practice. Here, let me show you."
            "I showed her how to put an upside down bucket under the front of the goat so she couldn't just lie down."
            "We put a bit more food in the goat's trough, and [kid_name] got ready to try again."
            him normal "That's it. Yeah, you've got a nice rhythm going now."
            kid concerned "I'm worried she's going to kick it over again!"
            him determined "You just watch her back legs, and if she starts getting antsy, you whisk that bucket away. You're almost done now, though."
            kid surprised "How do you know when you're done?"
            him normal "Well, less milk is coming out, for one. But you can also see how the udder doesn't look full anymore."
            kid normal "Yeah, it's kind of floppy and wrinkly."
            him happy "Okay, I think you're done! Well, done with the goat, anyway. We have a few things to do with the milk, first."
            kid happy "This wasn't too hard..."
            him normal "Yeah, you learned a lot! Of course the first few times are kind of rough, so don't worry too much about spilled milk or anything."
            kid surprised "So am I done?"
            him determined "Not quite. I'll show you how to filter the milk and wash the bucket."

            $ authoritative += 1
            $ confident += 1
        "Finish it for her." if (get_extra_work() > 0):
            him concerned "Just go home. I'll take care of it."
            him sad "Oh-okay."
            "I finished milking, put the goat away, filtered the milk, and washed the equipment."
            "It would be so nice if [kid_name] could learn to do this, but maybe she just wasn't ready yet."
            $ permissive += 1
        "Tell her to try again.":
            him determined "Try again."
            kid angry "No way! I've had enough of this crazy goat!"
            menu:
                "What should I say?"
                "You will finish the job!":
                    him annoyed "You will stay here until the job is done!"
                    kid sad "Fine, then I guess I'll stay in here all night because this goat is never going to listen to me!"
                    him determined "It's your job to milk this cow. Now do it."
                    hide him with moveoutright
                    "I left to finish up my work. Her sobs followed me around the farm everywhere I went."
                    "I wanted to teach her to be independent, to do things for herself. I guess I needed to push her a bit to get her to learn that..."
                    scene barn with fade
                    show him at center with moveinright
                    "When I came back after a half hour, the goat was put away and there was about a cup of milk in the pail. The goat looked happy, so she must have been milked enough."
                    "But [kid_name] was going to need a lot more practice..."
                    $ authoritarian += 1
                "Leave if you're not going to help.":
                    him annoyed "If you're not going to help, then get out of my way."
                    kid cry "Fine, I will!"
                    hide kid with moveoutleft
                    "I ended up just doing myself. It wasn't that hard; maybe she just wasn't old enough..."
                    $ neglectful += 1
    return

# Year 16, 10 years old
# Seed exchange or increase size of farm
label work16:
    nvl clear
    sara_c "There will be a seed exchange this weekend! Bring some seeds to trade! 😋"
    natalia_c "I'm bringing chile seeds - they're a little bit sweet and a little bit spicy!"
    kevin_c "I plan on bringing some plum pits."
    pavel_c "Wonderful! I hope everyone will participate."

    $ random_crop = farm.crops.random_crop(include_animals = False)
    "A seed exchange could be good; I could share my great [random_crop] and get something new to plant in the future."
    "But Pete was already planning to come over and fence a new section of land for farming."
    "Last week I helped him expand his cattle paddock with a bigger fence and he was planning to return the favor."
    menu:
        "What should I do?"
        "Go to the seed exchange.":
            him_c "I'll be there, too!  I'm bringing [random_crop] seeds!"
            sara_c "Oooh, great! 😃"
            nvl clear
            scene community_center with fade
            show pavel at quarterleft
            show sara at midleft
            show natalia at center
            show kevin at quarterright
            show zaina at right
            with dissolve
            show him normal at left with moveinleft
            "There were a lot of people at the seed exchange!"
            pavel "Welcome, [his_name]! Good to see you!"
            him normal "Thanks. Where should I put these [random_crop] seeds?"
            sara "There's an empty spot on the table there. Oh, you brought a sign. Perfect."
            $ colonists += 1
            show him at midright with move
            him surprised "You said your chile peppers are spicy and sweet?"
            natalia "Oh yes. If you pick them green, they're a little bitter and more savory. If you wait until they turn red, they're sweeter. But the spiciness is the same either way."
            him normal "Sounds very flavorful!"
            kevin "[his_name], are those your [random_crop] seeds? Would you recommend that crop?"
            menu:
                "What should I say?"
                "Yeah, you'll like them!":
                    him happy "Yeah! You'll love them."
                    kevin "Then perhaps I shall try planting some."
                "No, you should try something else.":
                    him concerned "I'm not sure they're the best crop for you..."
                    kevin "Really? Why do you say that?"
                    menu:
                        "What should I say?"
                        "They're too much work.":
                            him annoyed "They're too much work, especially for the yield you get."
                        "They don't really taste good.":
                            him concerned "Well, they don't really taste very good, so no one wants to eat them."
                            kevin "I like [random_crop]."
                            him surprised "Well, maybe they'd be good for you."
                        "They're not worth very much.":
                            him concerned "They don't sell for very much, so unless you love eating them yourself it's probably not worth it."
                            kevin "I like [random_crop]."
                            him surprised "Well, maybe they'd be good for you."
                        "They're not very nutritious.":
                            him annoyed "They just aren't that nutritious. Not many vitamins and minerals."
                            kevin "Oh. I had not considered that."

            if (not (crop_enabled("plums") or crop_enabled("plums+"))):
                him surprised "You don't mind if I take a few plum pits, do you?"
                kevin "Please do. They are hardy and productive plants."
                $ enable_crop("plums")
                him happy "Great! I love fruit."
            else:
                "Kevin took some of my seeds, and I decided to take some of the chile pepper seeds."
                natalia "You won't be disappointed!"
                $ enable_crop("peppers")

        "Expand your farmland.":
            $ luddites += 1
            "I had already worked everything out with Pete. I'd have to miss this seed exchange. Hopefully they'd have more in the future."
            scene fields with fade
            show him normal at midleft with dissolve
            show pete at midright with moveinright
            pete "You ready to make this fence?"
            him determined "You bet!"
            "It took us all day, but now I had four more fields for planting!"
            $ farm_size += 4
    return

# Year 18, 11.1 years old
# Roof leak and solar flare
label work18:
    scene farm_interior with fade
    show him normal at midright
    show her normal at quarterright
    show kid normal at midleft
    show bro normal at quarterleft
    with dissolve
    "There was one thing I absolutely had to get done today -- fix a small leak in the roof."
    "Well, it didn't seem so small when it was dripping water on my bed in the middle of the night."
    "We spent half the night moving things around so we wouldn't be right under the leak."
    "I wanted it fixed right away."
    "I don't know how it got a hole in it - the waterproof roof material was really pretty sturdy. Maybe a crabird managed to poke a hole in it with its claws or the wind blew a branch into it."
    "There was just one problem..."
    nvl clear
    if (year <= 20):
        lily_c "Major solar flare predicted sometime this morning."
    else:
        zaina_c "We've got a major solar flare this morning. It'll be short, but strong."
    pavel_c "Please stay at your homes! School and all other community buildings will be closed until after noon."
    nvl clear
    him annoyed "Guess I won't be fixing the roof this morning..."
    kid happy "Yay, no school!"
    bro concerned "No school?"
    kid surprised "You're not sad that school's cancelled, are you?!"
    bro sad "I like school."
    him surprised "Do you think I have time to run and get some rope from the barn?"
    her concerned "I don't know; it sounds like they weren't sure of the exact time."
    him annoyed "I really wish you could see the solar flares somehow..."
    kid normal "Yeah, it looks so nice outside. Hey, what if there's not actually any solar flares, but they're actually doing top secret stuff and don't want anyone messing with it?"
    him surprised "What kind of top secret stuff would that be?"
    kid happy "I don't know; maybe aliens?? Or maybe they found some super valuable ore right under the school and they're blasting it away with dynamite right now!"
    her flirting "I don't think that is going to happen."
    bro concerned "There could be aliens though, right?"
    him determined "I think if there were aliens on Talaam they would have said hi by now. We've been here for years."
    kid shifty "Unless they're just watching us. To see if we're worth enslaving. And any day now, they'll come and attack us in our sleep!"
    "She tickled [bro_name] excitedly. He flinched and tried to push her hands away."
    bro concerned "Stop!"
    her annoyed "[kid_name]..."
    kid annoyed "What?! I'm just trying to play with him! Too bad he hates me."
    him annoyed "He doesn't hate you, he just hates being tickled. Leave him alone."

    "Okay, I did not want to spend my whole morning playing police officer. I needed something for these kids to do."
    "I had the perfect chore -- cleaning the kitchen."
    "It wasn't covered with food or anything, but it'd been awhile since it really got cleaned."

    him determined "Okay, as long as we're stuck inside, we're going to get some work done!"
    her concerned "I have some analysis to do..."
    kid surprised "I think maybe I have homework?"
    bro concerned "I don't want to do anything..."

    menu:
        "What should I do?"
        "Make the kids clean the kitchen.":
            him normal "Kids, your job is to clean the kitchen."
            kid concerned "It looks pretty clean to me..."
            him determined "I want the stove and the wall wiped down with soap and water and the floor swept and mopped."
            bro sad "What?!"
            kid annoyed "What are you going to do, just sit around?!"
            him annoyed "Of course not. I've got some other work to do. That's what I need you two to do."
            $ confident += 1
            "She tried the whole time to convince me that her only work should be school work and it was unfair of me to make the kids do all the work, so I didn't get to concentrate much on my own work."
            "But they did finally get the kitchen clean. Well, cleaner than it had been."
            jump work18_after_clean
        "Assign a kitchen-cleaning job to everyone.":
            him determined "[her_name], your job is to wipe the stove. [kid_name], sweep the floor. [bro_name], you've got cleaning the walls, and I'll take mopping."
            show her annoyed
            "[her_name] gave me a look. I guess I shouldn't order her around like I do the kids."
            him concerned "Or, [her_name], I'd be happy to trade if you'd rather do the mopping."
            her determined "I would."
            him determined "Fine."
            $ confident += 1
        "Write the jobs on pieces of paper and have each person choose randomly.":
            him happy "Okay, it's time for the kitchen cleaning lottery!"
            kid annoyed "I already know I don't want to win."
            him normal "In this box are four chores. Each person will choose one randomly and that will be their chore for the morning!"
            him flirting "[her_name], would you like to go first?"
            her annoyed "...Sure."
            "We each pulled a slip of paper."
            $ confident += 1
        "Just clean it yourself." if (get_extra_work() > 0):
            him determined "Well, I don't know about you guys, but I'm cleaning the kitchen. Anyone want to help?"
            "I've never seen people disappear so fast. Suddenly everyone really wanted to read a book or do their homework or whatever it was they were doing."
            "That was fine with me."
            jump work18_after_clean

    "[her_name] put some peppy music on, and we all got to work."
    "[kid_name] soon quit pouting when she realized it wasn't going to change anything, though she did try to get away with doing the least amount possible."
    "[bro_name] didn't want to get wet, so I helped him wring out the cloth as much as possible before wiping down the wall."

label work18_after_clean:
    "We had a quick lunch together, and then, since the solar flare was over, we each went our separate ways."
    "And I could finally get to fixing the roof!"
    return

# Year 20, 12 years old
label work20:
    "Miners want cheap/fast/calorie-dense food. Will you cater to their needs?"
    "Also, Terra likes it as she is eating more and growing taller than ever."
    "or, solar panels are wearing out due to solar flares."
    return

# Year 22, 13.6 years old
# A surprise 40th birthday party
label work22:
    scene community_center with fade
    show night_overlay with dissolve
    show him determined at left behind night_overlay with moveinleft
    # TODO: show silhouettes?
    him determined "Why did [her_name] want to meet me here? It makes no sense..."
    him annoyed "And the light's are off, which means she's not even here...?"
    hide night_overlay with dissolve
    show her laughing at quarterleft
    show bro happy at quarterleft
    show kid happy at midleft
    show thuc happy at center
    show pete happy at midright
    show ilian happy at quarterright
    show sara happy at right
    show oleg at right
    with dissolve
    "Everybody" "Happy Birthday, [his_name]!"
    him surprised "Whoa! What are you guys all doing here in the dark??"
    her happy "Waiting for you, silly! You were supposed to be here fifteen minutes ago!"
    him normal "Sorry, I didn't know this was a time-limited event. Is it really my birthday?"
    her flirting "It is on Earth. You'd be--"
    him flirting "--old enough that my age is boring. I can't believe you got all the awesome people in one place at the same time for my birthday."
    her concerned "Well, Brennan and Julia couldn't make it."
    him happy "Like I said, all the awesome people are here!"
    kid normal "You looked so surprised."
    bro normal "Did you even know we were here?"
    him normal "Nope! You were like stealthy birthday ninjas!"
    "The kids ran off to the a table covered with a variety of foods -- looks like [her_name] organized a potluck. I made a mental note to visit it very soon."
    hide bro
    hide kid
    with moveoutleft
    show him at midleft with move
    him happy "Thanks for coming, Thuc!"
    thuc normal "I'll come to a party anytime. So is it true? Is this the big Four Oh?"
    him surprised "Um, maybe? I don't really keep track of my age, plus we spent that year on the shuttle that only felt like several months, so..."
    sara normal "Well, the colony database says you're 40, so I think it counts!"
    thuc normal "Don't worry; being 40 isn't so bad."
    him normal "You would know, huh?"
    thuc happy "It's 50 you have to worry about!"
    him happy "Yeah, well, at least I have the satisfaction of knowing I'll never be as old as you."
    pete normal "If it makes you feel better, you don't look a day over 39."
    him normal "Uhhh... thanks?"
    her flirting "I think you look as handsome as ever."
    ilian normal "Hmmm, I wonder what [his_name]'s midlife crisis will be?"
    sara sad "That's kind of depressing talk for a birthday, isn't it?"
    menu:
        "What should I say?"
        "A midlife crisis sounds depressing.":
            him annoyed "Yeah, can we talk about something besides my age?"
            her surprised "Oleg, I heard you're getting to be quite the programmer! What's your latest project?"
            oleg "Uh, not much."
            sara "It's okay; tell everyone about your game."
            thuc "You made a game?"
            oleg "Not really. I mean, kind of. It's not very good."
            sara "It's pretty fun! It's like a farming game, except that everything's underground and you have to protect crops from monsters and craft UV lights and sprinkler systems and stuff."
            oleg "It's not finished yet..."
            him happy "That sounds awesome. I'd like to play it when you're done."
            oleg "O-okay."
        "A midlife crisis sounds funny.":
            him happy "No, it's funny! Go ahead, tell me what you think I'll do."
            pete "You don't strike me as a flashy car kind of guy..."
            ilian "Anyway, those are currently in dismally short supply."
            if (is_liason):
                sara "You're already the RET liaison, so you don't need to seek a position of power."
            else:
                sara "Maybe he'll seek a position of power in the community? Run for mayor?"
                pete "Pavel'd better watch out."
            if (get_extra_work() <= 0):
                thuc "He is kind of a workaholic..."
            else:
                thuc "Maybe he'll become a workaholic and we'll never see him around."
                ilian "We already don't see him around."

            pete "Maybe he'll run off and have a wild fling with a hot alien chick."
            sara "Uh, wow, where did that come from?"
            him surprised "Wait, there's hot alien chicks here? Where?"
            if has_strong_marriage():
                thuc "No way. Their marriage is rock solid."
                him flirting "I already have all the hot alien chicks I need."
                her surprised "You do?"
                him happy "Oh yeah. You're on a planet that's not Earth, so you're an alien. And all I need is you."
                "I kissed her, right in front of everybody."
                sara "Awwwww! Sweet cheese!"
                her flirting "It's not cheesy if it's true, right?"
                pete "Nope. It's still cheesy."
            else:
                her concerned "I guess I'm lucky we haven't encountered aliens yet."
            sara "What about music? Maybe he'll start a punk metal band."
            her normal "He does write some pretty hardcore poetry..."
            him happy "Nah, I'm a terrible singer."
            # TODO: add some foreshadowing for the ending here?
            sara "You might not have a midlife crisis."
            him normal "I'm not planning on it!"

    "I finally got to make my way over to the snacks. Pete had brought two kinds of cheeses, and Ilian had dug a few tiny pieces of chocolate out of the storehouse."
    "There were fresh fruits and vegetables and even some soft, homemade, whole wheat bread with jam and butter."
    "I savored every bite."
    hide thuc
    hide sara
    hide pete
    hide oleg
    hide ilian
    with dissolve
    show him normal at midleft
    show her normal at midright
    with move
    him surprised "Did you plan all this?"
    her normal "Well, I had the initial idea, but I had a lot of help from your friends."
    $ helping_faction = strongest_faction()
    show her at center with move
    if (helping_faction == "colonists"):
        show thuc at midright with moveinleft
        her happy "Especially Thuc!"
        thuc "If I don't embarrass you for turning 40, who else will?"
        her flirting "I don't know; he's pretty good at embarrassing himself."
        him flirting "Hey, shouldn't you be a little nicer to me on my birthday?"
        thuc "Which reminds me... I brought you a little something."
        him surprised "You did?"
        if crop_enabled("onions"):
            thuc "Yeah, I brought you some turnip seeds. They're not worth much because nobody likes them, but maybe you'd have a use for them?"
            him concerned "Ummm... maybe?"
            thuc "Sorry; it's the only thing I could think of that you didn't already have."
            him happy "No, this is great! I love more variety. Thanks, Thuc."
            $ enable_crop("turnips")
        else:
            thuc "Try not to tear up... I brought you this bag of onions."
            him sad "Oh, Thuc. They're so beautiful. I just can't help crying!"
            her annoyed "..."
            thuc "You can plant them if you want."
            him normal "I will; thank you!"
            $ enable_crop("onions")
    elif (helping_faction == "luddites"):
        show pete at midright with moveinleft
        her happy "Especially Pete!"
        pete "I thought you'd get a kick outta a surprise party."
        him happy "Yeah, it's awesome!!!"
        pete "I also wanted to give you these."
        him surprised "What kind of seeds are these?"
        pete "Broccoli."
        her surprised "Do you like broccoli a lot?"
        pete "How're we gonna raise decent kids if they don't learn to eat their broccoli?"
        her laughing "So true! And it's really healthy, too."
        him happy "Great, thank you Pete! It's always good to have some more variety."
        $ enable_crop("broccoli")
    else:
        show chaco at midright with moveinleft
        her happy "Especially Chaco!"
        "He didn't say anything, but a slight smile tugged at the corner of his mouth."
        "Coming from Chaco, that was like a big bear hug."
        chaco "Here."
        "He handed me some credits."
        him happy "Oh! Wow. Thank you, Chaco; this is a very generous gift!"
        chaco "Wanted to thank you."
        # TODO: add money
    return

# Year 24, 14.8 years old
# Tractor accident
label work24:
    "[kid_name] was big enough to do real work on the farm, now. She could help a mama goat give birth, knew which plants were weeds, and could build a fence out of almost anything."
    "But her favorite way to help was driving the tractor."
    scene fields with fade
    "We were using the front loader attachment to add manure and to the fields."
    kid nervous "Please let me do the driving, dad! I know how to do it!"
    him annoyed "You haven't driven with the front loader attachment. The feel is totally different."
    kid annoyed "Well, how am I going to learn about it if you don't let me try it?!"
    "She had a good point. It wasn't really something you could learn just by watching."
    "But I wanted to keep her safe, too."
    him determined "I'll do the first run while you rake the manure into a pile. Then I'll decide if you can drive."
    kid concerned "Ugh. Fine."
    "I filled the front loader full of manure and drove down to the field we were preparing. I slowed down to turn to the side, and dumped the load on top of the dirt."
    "Then I drove back."
    him normal "Your turn. Watch out for the ditch on the side."
    kid annoyed "Of course, dad, it's only been there my whole life."
    "She got a load of manure into the bucket and headed down towards the field. The bucket was a lot higher than I usually put it."
    him annoyed "Lower the bucket!"
    kid nervous "What?"
    "She couldn't hear me. I started running, following the tractor."
    him concerned "The bucket's too high! Lower the bucket!"
    "I was too late. She turned the corner, going a little too fast. I felt like time slowed down as I started running. I could see the tractor starting to tip."
    "I reached out, but I was helpless to stop it. The high, heavy bucket dragged the whole tractor over onto its side."
    kid surprised "Ahhhhhhh!"
    him surprised "[kid_name]! Dammit!"
    "I ran as fast as I could. [kid_name] was quiet, which worried me even more than if she had been screaming."
    "When I finally reached her, she was unconscious and her leg was pinned under the tractor. I bent over her face and felt her breath."
    him determined "[kid_name]! [kid_name], wake up!"
    "I could probably lift the tractor off her, but if she couldn't scoot herself out it was pointless."
    him angry "[kid_name]!"
    "She stirred."
    him determined "Come on, [kid_name]. You're going to be okay."
    "She tried to get up, but could only sit. Good, at least her spine was okay."
    kid nervous "Wha-what? I can't - I can't move my leg!"
    him concerned "I know. It'll be okay. Now, on the count of three, I'm going to lift the tractor, and you need to get out of there, okay?"
    kid determined "It hurts!"
    him sad "I know it hurts, but we gotta get you out of there. I don't know if your leg will move, so you might have to use your arms."
    kid determined "Okay. Ow. Okay. I think I can do that."
    him angry "1...2...3!"
    "I heaved up and tilted the tractor. I couldn't tip it all the way back to standing, but hopefully it was enough..."
    him annoyed "Now, now, now! Out now!"
    kid nervous "Okay! I'm doing it...I'm clear!"
    "I set the tractor back down as gently as possible, my arms shaking and aching."
    "I looked down at my daughter. Her lower leg was bloody and her pants were ripped. She had a bump on her head from where she had hit the ground."
    kid concerned "Ohhh. Oh, that hurts!"
    "Her colorful curse surprised me. Looking at her leg, though, I couldn't really blame her."
    $ work24_stopped_bleeding = False
    $ work24_walk = False
    menu work24_first_aid:
        "What should I do?"
        "Stop the bleeding." if not work24_stopped_bleeding:
            him determined "First we better stop the bleeding."
            "I took off my shirt and wrapped it tightly around her leg."
            him concerned "Hold this on there, okay?"
            kid sad "Okay..."
            $ work24_stopped_bleeding
            jump work24_first_aid
        "Carry her to the clinic.":
            him determined "Let's get you to mom."
            "I couldn't take the tractor since it had tipped over. I'd get Thuc or someone to help me set it back up later."
            "I lifted her up in my arms, something I hadn't done for years and years."
            "She was a lot heavier now."
            kid sad "Ow! My leg!"
            him concerned "Sorry...I'll try not to move it."
            "She rested her head on my chest, and I started on the long walk into town."
            "My arms, already strained from lifting the tractor, felt heavy and numb, but I walked on."
            "Finally we arrived at the clinic."
            scene clinic with fade
            show her surprised at midright with dissolve
            show him determined at midleft
            show kid determined at center
            with moveinleft
            her surprised "[his_name]? What's wrong?"

        "See if she can walk." if not (work24_stopped_bleeding or work24_walk):
            him surprised "Can you stand up?"
            kid determined "Maybe... ugh. No, not really."
            "As she tried to stand up, more blood trickled down her leg."
            $ work24_walk = True
            jump work24_first_aid
        "Get some help.":
            him determined "I'm going to see if I can get some help, okay?"
            kid sad "Okay..."
            him concerned "Attention, this is [his_name]. [kid_name] is injured and needs transport to the clinic."
            "No one answered. I tried again."
            him determined "I need transport into town for [kid_name] who is injured. She might have broken her leg. Can anyone help?"
            "[her_name] on the radio" "[his_name]?! Is she okay?"
            him determined "She's conscious, but bleeding and her leg's hurt."
            "[her_name] on the radio" "Can't you take the tractor?"
            him concerned "Nope. That's how she got hurt; tractor tipped over."
            "Natalia on the radio" "I'm on my way."
            "[her_name] on the radio" "Thank you, Natalia!"
            "Natalia arrived on her tractor with the trailer attachment. I nestled in the back with [kid_name] while she drove."
            kid concerned "Ow!"
            "Every bump made her leg hurt more. I tried to protect her from the worst bumps but it was a long, rough ride."
            "When we arrived, [her_name] was ready for us."
            scene clinic with fade
            show her surprised at midright with dissolve
            show him determined at midleft
            show kid determined at center
            with moveinleft

    "[her_name] ran over, taking in [kid_name]'s injuries."
    her concerned "Okay. It's probably not too bad. Set her on the bed here."
    "I told her the whole story while she and the nurse cleaned and examined the wound. She felt [kid_name]'s leg carefully, noting every wince. She examined the rest of her, too."
    "[kid_name] was clearly in pain, but also fascinated by what [her_name] was doing."
    her determined "Broken tibia. Transverse. Fibula seems to be okay. Concussion."
    "She looked me in the eyes for the first time since I arrived."
    her angry "We'll talk about why in the world she was the one driving the tractor later."
    him sad "Is it bad?"
    her concerned "She'll be okay, [his_name]. But I need to put her under to put in some pins, so why don't you head on home. [bro_name]'s probably wondering where you are."
    "He had been working on homework when I left, but that was hours ago..."
    him determined "Okay. Keep me posted."
    her determined "I will."
    scene farm_interior with fade
    "The next day, when they came home, [her_name] wanted to talk."
    show her annoyed at midright
    show him concerned at midleft
    with dissolve
    her angry "Why was [kid_name] driving that tractor? She's just a kid!"
    him annoyed "She's not just a kid! She's almost an adult and very capable!"
    her annoyed "Not capable enough, apparently."
    him determined "Does she still have some things to learn? Of course she does. But she drives the tractor all the time just fine."
    her concerned "I know, it's just... I want more for [kid_name]."
    him annoyed "Farming isn't good enough?"
    her sad "It's not that!  Well... maybe it is."
    him angry "We've been through this before. People will always need to eat! Growing food is one of the most important jobs people do!"
    her concerned "I know but... it's so dangerous. And she could do so much more."
    him annoyed "What could be more important than not starving to death??"
    her annoyed "How about not bleeding to death?"
    him concerned "Look, I don't want to have a whose-job-is-more-important argument with you. We need both jobs. What's this really about?"
    her concerned "I don't want her to spend the rest of her life digging in the dirt on this alien planet in the middle of nowhere."
    him annoyed "Isn't that what {b}we{/b} are doing?"
    her determined "Yes, but we chose this. She didn't."
    menu:
        "What should I say?"
        "You miss Earth.":
            $ marriage_strength += 1
            him concerned "You miss Earth still, don't you."
            her sad "Sometimes..."
            him sad "Sorry I dragged you way out here."
            her normal "No, no, it's good. I like the life we have here."
            her concerned "I just like Earth, too, and I'd love for her to be able to experience that part of humanity."
            him determined "If she wants to."
        "She might not have a choice.":
            him determined "Well, she's here, and it's not like you can just buy a bus ticket back to Earth. She may be stuck here."
        "There's nothing good on Earth.":
            $ marriage_strength -= 1
            him annoyed "I don't see any reason why she would want to go back to Earth. Good riddance to that crowded, noisy, frivolous, self-absorbed planet!"
            her annoyed "Some of us liked it."
            him determined "I still can't see why."

    her concerned "Look if she really wants to be a farmer here, and that's her passion, then great, teach her to be the best farmer ever."
    him annoyed "I'm trying to--"
    her annoyed "I know, that's what you are trying to do already. Just, let me finish. But we shouldn't expect her to do what we do. She needs to decide for herself."
    him determined "I know that."
    her concerned "And she needs to stay alive and whole long enough to find that out."
    him concerned "I'm sorry she got hurt, [her_name]."
    her determined "It was an accident..."
    menu:
        "What should I say?"
        "I need to teach her better.":
            him sad "I should have taught her better. Then maybe she wouldn't have gotten hurt."
            her sad "..."
            "I heard a faint voice from the other room."
            kid "Dad, it's not your fault. I was driving too fast. You tried to warn me."
            him concerned "Thanks, [kid_name]."
            "I hadn't meant for [kid_name] to overhear us, but maybe it was a good thing. Maybe it would help her understand what we were trying to do."

        "Sometimes you have to learn things the hard way.":
            him annoyed "You have to understand, this world is just dangerous. She needs to learn how to be careful; maybe this is the only way she could learn that."
            her annoyed "Maybe you could help her learn in some way that preserves all her limbs."
            him determined "I wouldn't be doing her any favors if I made everything safe. Then she would never learn how to be careful and solve her own problems."
            her angry "Well you won't be doing her any favors if she doesn't survive until adulthood, either!"
            him angry "She survived! She'll be just fine!"
            her annoyed "Oh, so it's normal to just break your leg once in a while working on the farm?"
            "I thought I heard [kid_name] trying to say something, but I wasn't sure."
            kid "Mom?"
            him annoyed "Yes. Yes, it's totally normal for stuff like this to happen when you're doing real work."
            her angry "Real work?! You think you're the only one doing real work?"
            kid "Mom!"
            "[kid_name] was calling from her room."
            her concerned "Yes, [kid_name]?"
            kid "Can you guys keep it down? I'm trying to go to sleep."
            her annoyed "Sorry, we will."
            kid "Also, it's not dad's fault. I drove too fast around the corner."
            her concerned "Don't worry about that."
            him determined "See? She learned something from this."
            her annoyed "I just wish I could say the same thing about you."

        "Maybe she shouldn't work on the farm.":
            him sad "Maybe she shouldn't work on the farm. I don't want to mess up the rest of her life."
            her concerned "No, I think usually it's good for her. Just... can you just be a little more careful?"
            him concerned "Yeah..."
            her determined "I know she looks like an adult, but inside she still has a lot of learning to do."
            him determined "Don't we all..."

    return

# Year 26, 16.1 years old
label work26:
    "You throw out your back."
    "People from your favorite faction and your family help you, or not."
    return

# Year 28, 17.3 years old
label work28:

    return

# Year 30, 18 years old
# Terra doesn't want to help! Pay rent?
label work30:
    scene farm_interior with fade
    show kid normal at midright
    show him normal at center
    show her normal at midleft
    "[kid_name] took a deep breath. I braced myself, sensing I was about to hear something I wouldn't like."
    kid determined "I don't want to work on this farm."
    him surprised "You don't?"
    her concerned "You don't have to..."
    kid concerned "I mean, I don't want the crops to fail or anything, but there's so many other things I want to do, too. And I need to know that you'll be okay without my help."
    "I thought about that for a bit. I suppose I had started taking [kid_name] for granted, assuming she'd just always be there."
    "Part of me wanted to make her stay -- we're farmers! Farming is what we do!"
    "...but another part of me knew that I couldn't force her to stay. Besides, [her_name] wasn't a farmer, either, so why should I expect [kid_name] to be one?"
    $ work28_rent = 0
    menu:
        "What should I say?"
        "If you don't work, you need to pay rent.":
            him determined "I'm not going to force you to work on the farm, but if you're not, then you'll need to pay rent."
            her annoyed "Really? You want to charge our own daughter {b}rent{/b}?"
            him annoyed "Like it or not, that's how the real world works. Everybody needs to do something useful."
            her surprised "What if she's taking classes?"
            him determined "Everybody should work. Even people taking classes."
            her angry "So are you going to charge me rent, too?!"
            him annoyed "That's different! You get paid, and we use the money together. Is [kid_name] going to turn over everything she makes to us?"
            kid annoyed "No!"
            him normal "Everyone in this family helps out. If you're not helping around the house or the farm, then you can help out with money."
            her annoyed "But--"
            kid determined "I can pay 150 per month."
            her concerned "No, [kid_name], you might need that money..."
            menu:
                "What should I say?"
                "That's too much.":
                    him normal "Hey, I don't think your tiny room here is worth that much. Let's say 100 and it'll be fine."
                    her normal "Oh. That's not that much."
                    kid determined "Okay, I can do that."
                    $ work28_rent = 100
                "That's a deal.":
                    him normal "Sounds like a deal."
                    $ work28_rent = 150
                "That's not enough.":
                    him annoyed "Are you kidding? You've got your own room, homecooked meals, and use of our resources. That's worth at least 250 credits."
                    her determined "No. No way. 150 is the max!"
                    kid determined "I can pay 200, but not 250."
                    him determined "Then I guess that will have to do."
                    $ work28_rent = 200
            her concerned "If you can't make it some month, come by the clinic and I can find some work for you."
            kid annoyed "I'll be fine, Mom."

        "If you want to live here, you'll need to help.":
            him determined "Everyone that lives here needs to help out in some way."
            her "Maybe not on the farm, but in other ways?"
            kid "Sure, I can do chores and stuff. I just don't want to be your fieldhand."
            "We worked out some things that [kid_name] could do that weren't farming -- making meals and running errands for [her_name] and I."
            him concerned "Hopefully I can still count on your help during harvest time."
            kid "Yeah, for now."
        "We can cut back gradually.":
            him determined "I need you until the harvest. After that, we can slowly cut things down."
            kid concerned "Okay..."
        "You don't have to work here.":
            him concerned "You don't have to work on the farm. But I could definitely use your help."
            kid concerned "Maybe just when you really need me."
            him determined "Okay. Thanks, [kid_name]."

    bro "I don't want to work on the farm, either."
    "I already didn't have [bro_name] doing much on the farm. He was a good kid, but he was timid and sensitive and I could tell he would never be the kind that enjoyed the rough hard work of farm life."
    "But the work needed to get done, somehow, and without [her_name] it would be too much just for me."
    menu:
        "What should I do?"
        "Reduce the size of my farm.":
            "The best thing to do was just to not plant as many crops. Then I wouldn't need as much help. Hopefully it would still be enough."
            $ farm_size -= 4
        "Hire some help.":
            if (work28_rent > 0):
                "With the extra money [kid_name] would be paying in rent, I could afford to hire some help. Surely there'd be someone who'd be willing to do some hard work in exchange for a little extra money."
            else:
                "It would cost me, but I thought the cost of hiring another worker would be less than the cost of reducing the field."
            $ work28_rent -= 100
        "Have [bro_name] help more.":
            him normal "Sorry, [bro_name]. With [kid_name] leaving, I need your help more than ever."
            bro "I don't want to..."
            him concerned "I know. But sometimes we all gotta do things we don't want to do."
    "I guess it was [kid_name]'s job to grow up and eventually leave us."
    "I wasn't quite ready for it to start, though."

    # TODO: actually subtract rent from final total
    return
