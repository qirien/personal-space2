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
    scene farm_interior with fade
    show her normal at midright
    show him normal at midleft
    with dissolve
    "I harvested carrots, but many were bent and twisted."
    him happy "Want a carrot, [her_name]?"
    her annoyed "No, thanks."
    him surprised "They still taste good!"
    her surprised "Are they supposed to look like that?"
    him normal "Sometimes it's normal for a few of them to grow weird, but not this many..."

    menu:
        "What should I do?"
        "Till the soil better. Must be rocks." if (get_extra_work() >= 0):
            "I thought maybe I needed to till the soil better. Sometimes carrots would grow funny to try to get around rocks or hard soil in their way."
        "Must be something in the soil. Avoid planting carrots for a year.":
            "I could understand a few creepy carrots, but not so many. It must be something widespread."
            "I looked it up and found that some pests could cause carrots to grow like that."
            "I had no idea if it was an Earth pest or a Talaam creature causing it, though."
            "The simplest way to get rid of the pests would be to not plant carrots for a year. With nothing to eat, the pests would die."
            "It would take a while to see if it worked, though."
            # TODO: Don't allow carrots in farm screen.
            $ carrots_fallow = True
        "Who cares, they taste the same.":
            "I didn't have time to worry about oddly-shaped carrots."
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
                show kid normal at center
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
    scene fields with fade

    "I was glad I had managed to get rid of the pests on the carrots."
    "But this year, we had a ton. [kid_name] was eating them all the time, which is good, but her hands are starting to turn yellow... Is it healthy to eat that many carrots?!"
    menu:
        "What should I do?"
        "Ask [her_name].":
            scene hospital with fade
            show her normal at midright with dissolve
            show him normal at midleft with moveinleft
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
            "I probably shouldn't let [kid_name] eat so many of them..."
            scene farm_interior with fade
            show kid normal at midright with dissolve
            show him normal at midleft with moveinleft
            him surprised "Hey, [kid_name], it's not healthy to eat so many carrots. Try something else."
            kid annoyed "I like carrots!"
            $ parenting_style = get_parenting_style()
            if (parenting_style == "permissive"):
                him "Just don't eat too many."
            elif (parenting_style == "authoritative"):
                him "How about a limit of three per day?"
            elif (parenting_style == "authoritarian"):
                him "No more carrots."
            else:
                him "Too bad."
            return
        "Don't worry about it.":
            "There was probably nothing to worry about. In fact, my hands were looking a little orange, too..."
    # TODO: color them orange
    scene farm_interior with fade
    show him normal at midleft
    show kid normal at midright
    with dissolve

    him happy "Best carrots ever."
    kid happy "Yum!"

    return

label potatoes1:
    "I dug up a whole row of potatoes, but got interrupted before I could put them away. When I finally got back to them, they had a greenish tinge to them."
    "The green color is just chlorophyll, but sometimes it indicates increased solanine."
    "Solanine is poisonous; deadly so in large amounts. Usually if they're poisonous, the potatoes will also taste bad so it's easy to not eat them."
    "It wouldn't be a big deal, except I was going to give most of these to the storehouse, and I'm not sure everyone knows how to make sure potatoes are safe to eat."
    menu:
        "What should I do?"
        "Taste one and see if it's bitter.":
            "I figured I could test them on myself."
            "I cooked some up and they tasted fine, and I didn't get sick, so I figured there wasn't any problem."
            nvl clear
            sara_c "Hey, is it OK to eat green potatoes? Or is it just the sprouts you're not supposed to eat?"
            natalia_c "As long as they taste good they're OK."
            him_c "You can cut off the green parts if you're worried about it."
            sara_c "Okay, they just looked a little weird."
            nvl clear
        "Don't use any that have any green.":
            "I decided not to risk poisoning myself or others."
            "But even though they weren't good to eat, they would be fine for planting."
            # some kind of variable?  community_level?  farm_level? sustence?
            $ colonists += 1
            # TODO: no money from them.
        "Warn people about the risks of solanine.":
            nvl clear
            him_c "Just wanted to give everyone a heads up on potatoes."
            him_c "If they're green, you should peel them and get rid of any green parts."
            him_c "And don't eat them if they taste bad."
            him_c "Look up solanine poisoning if you want more information."
            sara_c "Why would we risk any sort of poisoning?!"
            him_c "They're probably fine!"
            natalia_c "Even supermarket potatoes sometimes had some green on them. It's not a big deal."
            julia_c "Unless you're wrong and our insides twist in knots and we start hallucinating."
            natalia_c "Well, I'll eat them if you won't."
            ilian_c "I'll discount them, but anyone taking them from the storehouse does so at their own risk."
            nvl clear
            "Wow, I didn't think that would be such a big deal."

            # TODO: less money gained for them.
            $ colonists -= 1
    return

label potatoes2:
    "I grew a lot of potatoes. In some ways, they were the perfect crop. They were protected from a lot of pests and weather since they were undeground."
    "They gave a high yield, and were a calorie- and nutrient-dense food."
    "But that also meant we ate them a lot."
    scene farm_interior with fade
    show him normal at center with dissolve
    "I wanted to do something different with them for dinner tonight..."

    menu:
        "Put them in a chowder":
            "There's nothing like a nice, hearty chowder. Goat's milk, onions, some grass crab meat, herbs, and of couse, lots of potatoes."
            show her at midleft with moveinleft
            her surprised "Mmmm, that smells so good! Like clam chowder!"
            him concerned "If only I had some bacon..."
            her flirt "How about some smoked crabird?"
            him normal "That's a start!"

        "Make potato chips":
            "I missed the satisfying crunch of potato chips. I really wanted to fry some up."
            "But first I'd need a lot of oil..."
            "More than the goat butter we had or the amount I pressed from squash seeds with our small oil press."
            scene storeroom with fade
            show ilian at midright with dissolve
            show him normal at midleft with moveinleft
            him "How much for some oil?"
            ilian "How much do you need?"
            him "About a liter."
            "He told me and I cringed, but I felt I had to have potato chips!"
            "Then an idea struck me."
            him "How much would you pay me for potato chips?"
            ilian "The storehouse doesn't take luxury goods like that. You'll have to ask around."
            him "Oh."
            ilian happy "But I, personally, would pay very well for such chips."
            "With the amounts he told me, I did some quick calculations in my head."
            him "Give me 10 liters of oil."
            ilian "Very well. Just make sure you bring some of those chips by here first, all right?"
            # TODO: money check: exact amounts?
            scene farm_interior with fade
            show him normal at midleft with moveinleft
            if (year >= 7):
                show kid normal at midright with moveinright
                kid "Is dinner ready yet?"
                him "No, but I'm making a special treat. You make us a salad, and I'm going to make a wonderful thing called potato chips."
                kid "That sounds gross. What, like wood chips?"
                him "Oh no, much, much better."
                kid "Okay..."
                hide kid with moveoutright
            "I sliced potatoes while I waited for the huge pot of oil to heat up."
            "It took longer than I thought because I tried to slice them very thinly."
            "Finally, they were ready to fry."
            "The first couple burned; the oil was too hot!"
            "The next batch was still a little too brown."
            "But the third time... they were perfect."
            him sleeping "Fresh, small batch, kettle cooked potato chips..."
            "That {i}crunch{/i} was the most beautiful symphony I'd ever heard."
            show her normal at midright with moveinright
            her surprised "Potato chips?! Mmmm, they're so good. But weren't they expensive?"
            him normal "We can't eat all of these; I need to bag and sell some to make back the money I spent on oil."
            "She looked at the huge vat of oil, and then at my pile of potatoes."
            her flirt "You're going to be in the kitchen for a long time."
            him "I could use some help..."
            her "I'll take care of everything else around the house; you just keep cooking potato chips!"
            "In the end we managed to make a little extra with the chips, though it was so much work I wasn't sure I'd do it all the time."
            # TODO add some money.

        "Make potato salad":
            "Potato salad was one of my favorite summer dishes back on Earth. I'd made it before and it wasn't too hard."
            "But there were a lot of things the storehouse didn't have here."
            scene farm_interior with fade
            show him annoyed at center with dissolve
            him "Mayonnaise, mustard, pickles, celery -- if I leave all those things out is it even still potato salad?!"
            "I'd have to make my own recipe."
            him concerned "I could use goat milk for creaminess, a little vinegar for a nice tang, and I do have some other herbs and spices..."
            him surprised "I have some homemade pickles I could chop up and put in there, and I have one egg I could boil..."
            "The end result was a potato salad, though it tasted nothing like the comfort food I remembered. I'd have to call it something else."
            show her normal at midleft with moveinleft
            show him normal at midright with move
            her surprised "Is that... dinner?"
            him normal "Yes, it's potato... uh, Cold Potato Mixup!"
            her flirt "You just made that up, didn't you?"
            him happy "Yeah! Want to try it with me?"
            her concerned "I am hungry..."
            him concerned "..."
            her surprised "..."
            him surprised "What do you think?"
            her concerned "It's... a different way to eat potatoes."
            him determined "It's not bad."
            her normal "No, it's kind of good... I think it needs some more salt, though."
            him flirt "More salt, coming right up!"
            her happy "It looks like a lot of work..."
            him concerned "Yeah, I kind of spent all afternoon on it."
            her concerned "It kind of reminds me of potato salad..."
            him surprised "Really?"
            her normal "Yeah... just a little."
            "That was good enough for me."

    return

label potatoes3:
    "I'll never forget the time it rained..."
    "And rained."
    "And rained."
    "It rained nonstop for two whole weeks."
    "Some rain is good from crops. It meant I didn't have to manually irrigate them."
    "But this much was terrible for my potatoes."
    scene fields with fade
    show him concerned at center with dissolve
    him "They've all rotted."
    "Instead of beautiful, firm, starchy potatoes, all I had were mushy brown foul-smelling lumps."
    "I had to dig them out anyway so they wouldn't contiminate the field."
    "They would make good compost for other plants."
    show him concerned at quarterleft with move
    "But every hour spent in the mud fishing them out felt oppresive and pointless."
    show him sad at center with move
    "I spent all season on them, and what did I have to show for it?"
    "Just foul-smelling mush."
    # TODO: Can he be covered in mud?
    show him determined at quarterright with move
    "I worked and worked all day, all afternoon, and into the evening."
    show night_overlay
    show him at midleft with move
    "I was so frustrated and mad that I just wanted to get it all done and forget about it."
    show him at midright with move
    "I couldn't see very well in the moonlight but I kept ripping up the plants and loading the rotten potatoes onto the trailer."
    "I slipped and fell in the mud right as [her_name] came walking up."
    show her concerned at midleft behind night_overlay
    show kid normal at center behind night_overlay
    if (bro_age > 0):
        show bro normal at midleft behind night_overlay
    with moveinleft
    her "Hey, we missed you at dinner. Everything okay?"
    menu:
        "What should I say?"
        "Fine.":
            him annoyed "Fine."
            if (year >= 7):
                kid sad "What's that smell?"
            else:
                her surprised "What's that smell?"
            him determined "Rotten potatoes."
            her concerned "Oh, all that rain... Are they okay?"
            him annoyed "Nope. Gotta clean them out of here."
            her sad "You've been out here working on them all day?"
            him determined "Pretty much."

        "We lost all the potatoes.":
            him concerned "No, all the potatoes are rotten, but I still have to clean them out, so it's been a pretty terrible day."

        "I'll finish up and then come home.":
            him determined "Yeah, I'm just finishing up. I'll meet you at home in a few minutes, okay?"
            her concerned "Okay...Wait, are these the potatoes?!"
            kid sad "I'm not eating those!"
            him concerned "I'm tossing them; they're all bad."


    her concerned "Oh, honey, I'm sorry..."
    if (marriage_strength >= 2):
        her surprised "Want some help?"
        him concerned "No, no, you've been working all day, too, I can't ask you to do that."
        her sad "Are you sure?"
    him normal "Yeah, I should probably quit for today anyway."
    her normal "We saved you some dinner..."
    him determined "As long as it's not potatoes."
    # TODO: lose money based on number of potato fields?
    return

# only happens if no bees
label squash1:
    scene fields with fade
    show him normal at center with dissolve
    "Most of my crops were self-pollinating or didn't need pollination."
    "But squash can't pollinate itself. Somehow, the pollen from the male flowers has to get over to the female flowers to fertilize them, otherwise you don't get any squash."
    "And Talaam didn't have the same insects we did on Earth to help pollinate plants."
    "I planted a variety that was supposed to not need as much pollination, but not many of the fruits were setting."
    "So if I wanted to get a decent squash harvest this year, I'd need to help them out."
    menu:
        "Pollinate by hand" if (get_extra_work() >= 0):
            him determined "I guess I'm Cupid's little helper today..."
            "I took a paintbrush and dabbed the pollen from the male flowers and then brushed it on the female flowers."
            "Since there were several flowers on each plant, and a whole field full of plants, it took quite a while."
            "But it wasn't difficult, and it did increase our squash yield dramatically."
            # TODO: increase yield/work?
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
            "Exterminate them all by hand!" if (get_extra_work() >= 0):
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
            "Slaughter for meat" if (get_extra_work() >= 0):
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
    # how many seeds to save?
    menu:
        "Pick it early":
            "Yum, smaller, more tender greens, but less food."
        "Wait until it's fully grown":
            "Larger harvest. more bitter taste.  more food/less happiness, seeds?"
    return

label spinach2:
    "Even with all our technology -- our hybrid tractors, our careful genetic modifications, our surveillance cameras and timed sprinkler systems -- we were still at Mother Nature's mercy."
    "It usually didn't get very warm on Talaam. Most of the time our proximity to the ocean kept the temperatures moderate."
    "But one year we had a terrible heat wave..."
    "...and the spinach seeds never came up."
    "They needed cool temperatures to germinate. The weather was cool again -- for now."
    "I had enough seeds to plant one more batch of spinach. But if those also failed, then next year I wouldn't have any spinach seeds at all."
    $ crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] = 1
    menu:
        "Plant them again now.":
            "I carefully looked at the weather, and when it looked like it would be nice and cool I planted them again."
            "And they did germinate -- little spinach sproutlings emerged from the soil."
            "But it got hot again."
            "The spinach didn't die, but it began to flower. I harvested the tiny, bitter leaves and got enough seeds to plant next year."
            scene farm_interior with fade
            show her annoyed at midright
            show kid annoyed at center
            show him annoyed at midleft
            her concerned "[his_name]...I can't eat this spinach."
            him concerned "..."
            her sad "Sorry..."
            him determined "I can't, either. But I know someone who will."
            show her surprised
            hide him with moveoutleft
            scene fields with fade
            show him determined at midright
            show goat at midleft
            with dissolve
            him annoyed "Enjoy your spinach, goats."
        "Save the seeds.":
            "If we had one heat wave, we could have another. The safest bet was to just save the seeds for next year."
            scene farm_interior with fade
            show her normal at midright
            show kid normal at center
            show him normal at midleft
            her surprised "Is the spinach ready yet? I wanted to make a salad to go with dinner."
            him concerned "Sorry, no spinach this year. It got too hot."
            her concerned "Oh...that's too bad."
    return

label spinach3:
    $ crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] += 1
    scene fields with fade
    "This year, I planted my spinach a little earlier to avoid any heat problems."
    "Now it's almost to full size."
    "But something has been eating the plants. I haven't seen anything, but when I checked the leaves, I could see bites taken out."
    $ spinach3_cameras = False
    menu spinach_3_menu:
        "Check the surveillance cameras" if (not spinach3_cameras):
            "I trained the farm's cameras on the spinach plot, but the next morning when I looked at the video, none of the motion sensors were triggered.  I scanned through the video but couldn't find anything out of the ordinary."
            $ spinach3_cameras = True
            jump spinach_3_menu
        "Check on your spinach at night":
            show night_overlay with dissolve
            show him annoyed at center with moveinleft
            "After [kid_name] and [her_name] went to bed, I snuck out of the house to examine the spinach plants.  My flashlight caught something small and slimy -- it looked like a snail!"
            "It's not exactly like an Earth snail -- its shell is hard, but instead of a spiral it's more of a dome, like a turtle. Its body is soft and squishy, but it has little feet protuberances like a caterpillar."
            menu:
                "What should I do?"
                "Hand pick them off":
                    "I spend several hours that night plucking off snails and putting them in a bucket. And the next night.  And the next night.  There's fewer each night, but it's tedious work."
                    if (get_work_kid() > 0):
                        show him determined at midright with move
                        show kid annoyed at midleft behind night_overlay with moveinleft
                        "I enlisted [kid_name]'s help. At first she was a little grossed out..."
                        show kid normal with dissolve
                        "...but eventually she got really good at it. With her shorter height, she was able to see the turtle-snails hiding under the leaves better than I could."
                    "At first the turtle-snails seemed endless, but after a few nights there were less and less of them."
                    "And we harvested a lot of wonderful spinach."
                "Make snail traps":
                    "I put some tasty smelling bait in the middle of a hole covered with boards."
                    scene field with fade
                    show him normal at midright with dissolve
                    "In the morning, the hole was full of turtle-snails, just waiting for me."
                    if (get_work_kid() > 0):
                        show kid surprised at midleft with dissolve
                        kid "What are you doing out here?"
                        him angry "I am about to dispense justice onto these vicious turtle-snails that have been murdering our spinach."
                        "She peered inside the trap."
                        kid annoyed "Yuck. How are you going to do that?"
                        him concerned "I haven't decided yet..."
                        kid nervous "They're kind of cute."
                        him annoyed "Cute as cockroaches."
                        kid concerned "You're not going to kill them, are you?!"
                        menu:
                            "What should I do?"
                            "Have [kid_name] help you move them.":
                                $ confident += 1
                                him determined "Not if you'll help me move them."
                                kid surprised "Okay, where?"
                                him normal "The other side of the river should be far enough."
                                "We got a bucket, filled it with snails, and she escorted them across the river."
                                hide kid with moveoutright
                                kid normal "There you go little buddies!"
                            "Have [kid_name] help you kill them.":
                                $ confident += 1
                                him determined "I'm not going to kill them. You are."
                                kid angry "What?! No. No way!"
                                him annoyed "If we don't, they'll destroy our crops. Not just this year, but next year, too."
                                kid sad "They just want to eat a little spinach."
                                him concerned "They will eat all our spinach, and they won't stop there."
                                if (is_independent()):
                                    call spinach3_eat_snails
                                elif (is_attached() and is_competent()):
                                    kid concerned "What do you want me to do?"
                                    him determined "Just drop them in this bucket of water and they'll probably drown."
                                    kid surprised "What if they don't?"
                                    him concerned "Then I'll take care of it."
                                    kid concerned "Okay. I'll do it."
                                else:
                                    kid cry "No, I won't do it!"
                                    hide kid with moveoutleft
                                    "She ran back to the house crying. Maybe this was one job I shouldn't delegate."
                                    "I dropped them in a bucket of water and that seemed to kill them."
                            "Send her away and kill them yourself.":
                                him determined "I'll take care of it. You just run along, now."
                                if (is_independent()):
                                    call spinach3_eat_snails
                                else:
                                    hide kid with moveouleft
                                    "She left, and I carried out the death sentence on the turtle-snails."

                    "I made some more traps and repeated the process until no more turtle-snails appeared."
                    "And we harvested a lot of wonderful spinach."
                "Just pick the spinach early":
                    call spinach3_pick_early
        "Just pick the spinach early":
            call spinach3_pick_early
    return

label spinach3_eat_snails:
    kid concerned "If we have to kill them, we should eat them."
    him surprised "Eat them?"
    kid surprised "Yeah, can we eat them?"
    him normal "Probably..."
    kid normal "Well, I'll just keep them until we figure it out. I'll make sure they don't get into the garden."
    "[kid_name] ran and got a shallow pan to keep them in."
    "We had the scientists run some tests and they said they were edible."
    "[her_name] did some research on escargot farming and we decided to try it."
    scene farm_interior with fade
    show him surprised at midright
    show kid surprised at center
    if (bro_age > 0):
        show bro surprised at quarterright
    show her surprised at midleft
    with dissolve
    her concerned "It's...interesting."
    kid nervous "It's...not bad."
    him concerned "I suppose... I could eat this."
    if (bro_age > 4):
        bro "I'm not eating it."
    "It was an interesting experiment, but ultimately we did not want to eat that many turtle-snails."
    return

label spinach3_pick_early:
    "It'd be too much work to kill all the snails. If I just harvested the spinach early then there wouldn't be anything for them to eat."
    "But spinach isn't the only thing turtle-snails like..."
    if ("beans" in farm.crops):
        $ snail_crop = "beans"
    elif ("peppers" in farm.crops):
        $ snail_crop = "peppers"
    elif ("squash" in farm.crops):
        $ snail_crop = "squash"
    elif ("broccoli" in farm.crops):
        $ snail_crop = "broccoli"
    elif ("cabbage" in farm.crops):
        $ snail_crop = "cabbage"
    elif ("strawberries" in farm.crops):
        $ snail_crop = "strawberries"
    elif ("carrots" in farm.crops):
        $ snail_crop = "carrots"
    elif ("snow peas" in farm.crops):
        $ snail_crop = "snow peas"
    else:
        $ snail_crop = "other crops"
    "After you picked the spinach, they moved on to your [snail_crop]."
    "This is something that you cannot forgive."
    "This means war."
    "Your nights are filled with killing turtle-snails."
    "They appear in your dreams, giant, house-sized turtle-snails with ever-chewing mouths, the entire earth disappearing beneath their slavering jaws until Talaam is just an empty spot in the vast blackness of space."
    "You think you see them everywhere you look -- in the fields, in the barn, in the outhouse."
    "Finally, their numbers are greatly reduced, and you can rest.  Until the next invasion..."
    return

label strawberries1:
    "Your strawberry plants did really well this year! Not only did you get extra strawberries, but you have enough runners that you could plant more next year if you wanted."
    $ strawberries_index = get_crop_index("strawberries")
    $ crop_info[strawberries_index][MAXIMUM_INDEX] += 1
    return
