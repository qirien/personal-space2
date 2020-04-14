# Malnutrition Event for if you don't have enough nutrition
label bad_nutrition:
    $ bad_nutrition_count += 1
    if (bad_nutrition_count == 1):
        scene farm_interior with fade
        show her concerned coat at midright
        show him determined at midleft
        $ common_food = farm.most_frequent_crop()
        if (has_strong_marriage()):
            her normal coat "[his_name], I wanted to thank you for always growing plenty of food for our family. We've always had enough to eat."
            him surprised "Oh. I'm, uh, glad you appreciate it."
            her concerned coat "But I'm worried that we are not eating a balanced diet with these foods. The human body needs more than 30 different vitamins, minerals, and nutrients. We can't get all those with just [common_food]."
        else:
            her concerned coat "[his_name], I don't want to tell you how to do your job..."
            him annoyed "Why do I get the feeling you're about to tell me how to do my job?"
            her annoyed coat "We can't live on just [common_food]! The human body needs more than 30 different vitamins, minerals, and nutrients."
        him angry "There's a lot of factors here! Sometimes crops fail, I have limited types of seeds, and I have to balance everything right or crops won't grow at all!"
        her concerned coat "I know, I'm sure you're doing the best you can. But it's especially important for the kids."
        him annoyed "They're not starving, right?"
        her annoyed coat "No. But we often don't get enough of vitamins A and C, and magnesium is sometimes low, too."
        him concerned "A, C, magnesium... is there anything we ARE getting enough of?!"
        her determined coat "Actually, yes, we get plenty of the B vitamins, iodine, iron, calcium, vitamin D, potassium..."
        him surprised "OK, I get the picture. But couldn't we just take vitamin supplements?"
        her concerned coat "Right now they're by prescription only, for serious nutrition problems. I don't want us to get to that point."
        him determined "I guess I could plant a few different things next year..."

        # are we using currency yet?
        if (year >= MONEY_YEAR):
            her determined coat "And for now let's get a few things at the storehouse."
            $ modify_credits(-50)
        else:
            her determined coat "And for now let's trade for a few different foods."

        # TODO: add screenshot here
        "I added [her_name]'s nutrition information to my farm planning app so that I could keep track of that better."
        return

    # TODO: add in a random element here also?
    #$ renpy.random.randint(1,20)
    if (bad_nutrition_count >= 2):
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
            him concerned "Sorry, [her_name]. I feel like I failed you."
            her determined "We're all alive and kicking, so no one's failed yet. Just... please try better next time, okay?"
            $ modify_credits(-50)

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
            if (require_whole_harvest):
                ilian_c "Shouldn't you be bringing all that to the storehouse?"
                if is_liaison:
                    "He caught me there. I was being pretty hypocritical, going around the system I was telling everyone else to follow."
                    menu:
                        "What should I say?"
                        "You're right.":
                            him_c "You're right, Ilian. Sorry, guys, I'm going to have to back out. I'm taking the goat's milk to the storehouse where you can buy it from Ilian."
                            $ modify_credits(-50)
                            "I ended up paying a premium for peppers and squash for the family diet."
                            return
                        "We should only bring extra.":
                            him_c "You know; I've changed my mind. We shouldn't have to do that. Everyone should just bring their extra to the storehouse."
                            $ rationing = True
                            $ require_whole_harvest = False
                            ilian_c "Really? You're changing it, just like that?"
                            him_c "Being the liaison has to be good for something."
                            natalia_c "I'm not complaining."
                        "(Don't say anything)":
                            "I didn't say anything. Everyone knew that requirement was mostly for show, right?"
                            $ mavericks += 1
                            $ colonists -= 1
                            $ miners -= 1
                else:
                    sara_c "He's right. If you have extra, bring it to the storehouse and we can distribute it fairly. {emoji=cry}"
                    pete_c "And at a high price."
            nvl clear
            "I was glad I was able to work out a trade this time. Next time, though, I might not be so lucky."

            # test for vitamin C
        elif (farm.low_vitamin_c() and (not seen_low_c)):
            $ seen_low_c = True
            "I felt weak and sore, like I was coming down with the flu."
            "It got bad enough that I decided to ask [her_name] about it."
            scene hospital with fade
            show her concerned coat at midright with dissolve
            show him concerned at midleft with moveinleft
            her "You feel tired and sore, and have a low grade fever. On Earth I'd call this the flu, but..."
            him annoyed "The flu is not supposed to exist here."
            her surprised coat "Do you have any other symptoms? Sore throat, runny nose, cough, indigestion?"
            him normal "No, none of those. Well, maybe a little stomachache, but I ache all over."
            her determined coat "Here, let me check your gums..."
            him annoyed "Ow!"
            her concerned coat "Gums bleed easily... let me look at your skin..."
            him surprised "Oh, where did that bruise come from? I don't remember getting hurt..."
            her determined coat "Aha! You have scurvy."
            him normal "Scurvy? Like, scurvy-sea-dog scurvy?"
            her annoyed coat "Like, someone-didn't-plant-enough fruits-and-vegetables scurvy."
            him surprised "How come you and [kid_name] don't have it?"
            her concerned coat "I don't know... we eat a lot of the same foods... though I think we get more applesauce since sometimes Helen will bring some in."
            him annoyed "And you don't share it with me?!"
            her annoyed coat "There's not very much... Anyway, here's some vitamins -- they should help you start feeling better in a few days. And next time, try planting more peppers, squash, or broccoli. Even potatoes have some vitamin C in them."
            him happy "Yeah, I guess I should. Man, I'm totally a pirate now!"
            her flirting coat "Don't go bragging about it or everybody will want to get scurvy."
            him flirting "I don't think that's something we need to worry about."
            $ achieved("Scurvy Dog")

        elif (farm.low_vitamin_a() and (not seen_low_a)):
            $ seen_low_a = True
            scene farm_interior with fade
            show him determined at midright with dissolve
            "My skin was always dry and for some reason I couldn't see well at night."
            "I didn't think to ask [her_name] about it, though, until she came to me."
            show her concerned coat at midleft with moveinleft
            her concerned coat "[his_name]... have you been having trouble seeing at night?"
            him surprised "Yeah, how did you know??"
            her determined coat "I have the same problem, and I think [kid_name] does, too."
            him concerned "Do you know why? Is it a disease? Some kind of alien parasite?"
            her annoyed coat "No. I'm pretty sure we haven't been getting enough vitamin A."
            him surprised "Vitamin A?"
            her determined coat "Yes. I got us all a supplement from the clinic for now, but you need to plant more vegetables like carrots, squash, and spinach."
            him concerned "Aw man, I hate pills."
            her annoyed coat "Which do you hate more: pills, or being able to see?"
            him surprised "It's that bad?"
            her angry coat "Yes! Prolonged vitamin A deficiency can lead to blindness in kids!"
            him angry "Okay, okay! I'll try and plant better crops next time."
            her sad coat "Sorry, [his_name]. I know you're doing the best you can..."
            him determined "If it's not good enough, I'll do better."

        elif (farm.low_magnesium() and (not seen_low_m)):
            $ seen_low_m = True
            scene farm_interior with fade
            show her concerned coat at midright
            show kid concerned at center
            if (bro_age > 0):
                show bro concerned at quarterleft
            show him concerned at midleft with dissolve
            her annoyed coat "I just can't take it anymore!!"
            him surprised "Whoa, whoa, calm down."
            her angry coat "I'm supposed to be calm?! This is insane! How did we ever think living here was going to work?!"
            him concerned "I thought it was working pretty well..."
            kid surprised "Mom, are you okay?"
            her sad coat "I don't know what's wrong with me... I just feel so crazy lately."
            him determined "You have been a bit more... volatile."
            her concerned coat "I can't stop worrying and I just feel so stressed out all the time but I don't even have that much to be stressed out about!"
            him concerned "Is it PMS?"
            kid concerned "Are you sick?"
            her surprised coat "I... I don't think so, but... now that you mention it, there are some conditions that can cause these symptoms..."
            him surprised "Are there some tests you can run?"
            her concerned coat "Yeah... will you come with me?"
            if (has_strong_marriage()):
                him concerned "Of course."
                scene hospital with fade
                show her concerned coat at midright
                show him concerned at center
                show kid concerned at quarterleft
                if (bro_age > 0):
                    show bro at midleft
                with moveinleft
                her determined coat "I just need to swab under my tongue..."
                kid surprised "Does it hurt?"
                her annoyed coat "No, it's just...awkward... here, [his_name], you do it."
                him surprised "Oh! Uh, okay..."
                her determined coat "Just scrape it a little. Right here."
                "She opened her mouth and held still. [kid_name] watched, fascinated."
                him determined "Okay, done. Hopefully I did that right."
                her annoyed coat "It'll do. If this doesn't turn up anything we'll need blood and urine samples."
                him surprised "Hopefully you don't need me to help with those."
                her determined coat "It'll take a few minutes for me analyze the spectrometer's results."
                "I talked with [kid_name] while we waited for [her_name] to finish."
            else:
                if (bro_age > 0):
                    him concerned "I'll stay here with the kids while you do it."
                else:
                    him concerned "I'll stay here with [kid_name] while you do it."
                her sad "Okay..."
                hide her with moveoutleft
                "She was gone for about an hour."
                show her normal coat at midright with moveinleft
            her concerned coat "This confirms it. I have a magnesium deficiency."
            him surprised "Magnesium??"
            her determined coat "Yes. Normally we get plenty from nuts, beans, and eggs. But we haven't been eating many of those lately."
            him sad "Probably because I didn't plant enough..."
            her concerned coat "Yes, well... you probably all have it, too, so you'll need to take this supplement."
            him surprised "Why didn't we notice this earlier?"
            her determined coat "The symptoms are so subtle that it's usually hard to detect until it starts to cause more severe problems, like diabetes or heart failure."
            him normal "Well then, I'm glad you caught it."
            her normal coat "This supplement is just a short-term solution. We'll need to buy some beans or nuts."
            him determined "Okay."
            $ modify_credits(-50)

        else:
            # seen all the events that would apply
            "The crops I planted didn't provide the vitamins and minerals we needed."
            if (year > 5):
                "I had to spend money at the storehouse to buy some different foods."
                $ modify_credits(-50)
            else:
                "I had to trade with other farmers to get a better variety of food."

        if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
            scene fields with fade
            "I thought that if my farm was bigger, I might have more room to plant crops with better nutrients."
            "I was able to add another field."
            $ modify_farm_size(1)
        return

    # fall through for times without a special event.
    "The crops I planted didn't provide the vitamins and minerals we needed."

    if (year > 5):
        "I had to spend money at the storehouse to buy some different foods."
        $ modify_credits(-50)
    else:
        "I had to trade with other farmers to get a better variety of food."

    if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        scene fields with fade
        "I thought that if my farm was bigger, I might have more room to plant crops with better nutrients."
        "I was able to add another field."
        $ modify_farm_size(1)

    return
