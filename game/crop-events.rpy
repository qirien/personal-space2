# Crop-specific work events

# TODO: First person or third person?
# TODO: Some crop events kind of assume that you'll get the next crop event
# the next year.  If you don't plant that crop the next year, some events
# should reset.

# Default crop event, if no other crop event can be found
label default_crop_event:
    "The year passed by in a blur: tilling, planting, weeding, harvesting; the endless cycle of life on the farm."
    return

# CARROTS1 - bent and twisted
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
            "It would be awhile before I could see if it helped, though."
        "Must be something in the soil. Avoid planting carrots for a year.":
            "I could understand a few creepy carrots, but not so many. It must be something widespread."
            "I looked it up and found that some pests could cause carrots to grow like that."
            "I had no idea if it was an Earth pest or a Talaam creature causing it, though."
            "The simplest way to get rid of the pests would be to not plant carrots for a year. With nothing to eat, the pests would die."
            "It would take a while to see if it worked, though."
            $ crop_temporarily_disabled = "carrots"
        "Who cares, they taste the same.":
            "I didn't have time to worry about oddly-shaped carrots."
            "I just chopped them up and cooked them and then nobody even noticed."
    return

# CARROTS2 - great carrots if fallow, otherwise find pests.
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
            # TODO: less money?
            menu:
                "What should I do next year?"
                "Treat the carrots with pesticide" if (get_extra_work() >= 0):
                    "I decided to treat next year's carrots with pesticide. It'd be more work, but I didn't want to give up carrots."
                "Don't plant carrots next year and let the pests die off.":
                    "The easiest thing to do was just not plant carrots for a year. Then the pests would die."
                    $ crop_temporarily_disabled = "carrots"
        return

# CARROTS3 - is there such a thing as too many carrots?
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
            her "No, not on its own. It's only bad if she's not getting other nutrients she needs because she's just eating carrots."
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

# POTATOES 1 - Solanine
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
            sara_c "Hey, is it OK to eat green potatoes? Or is it just the sprouts you're not supposed to eat? 😟"
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
            sara_c "Why would we risk any sort of poisoning?! 😱🤮"
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

# POTATOES2 - what to do with them
label potatoes2:
    "I grew a lot of potatoes. In some ways, they were the perfect crop. They were protected from a lot of pests and weather since they were undeground."
    "They gave a high yield, and were a calorie- and nutrient-dense food."
    "But that also meant we ate them a lot."
    scene farm_interior with fade
    show him normal at center with dissolve
    "I wanted to do something different with them for dinner tonight..."

    menu:
        "Put them in a chowder":
            "There's nothing like a nice, hearty chowder. Goat's milk, onions, some grass crab meat, herbs, and, of course, lots of potatoes."
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
                kid "What, like wood chips? That sounds gross."
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
            "The end result was sort of a potato salad, though it tasted nothing like the comfort food I remembered. I'd have to call it something else."
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

# POTATOES3 - Rotten potatoes
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

# SQUASH1 - not getting fertilized
label squash1:
    scene fields with fade
    show him normal at center with dissolve
    "Most of my crops were self-pollinating or didn't need pollination."
    "But squash can't pollinate itself. Somehow, the pollen from the male flowers has to get over to the female flowers to fertilize them, otherwise you don't get any squash."
    "And Talaam didn't have the same insects we did on Earth to help pollinate plants."
    "I planted a variety that was supposed to not need as much pollination, but not many of the fruits were setting."
    if ("honey" in farm.crops):
        "Luckily, I had bees to help out with pollination."
        "So we had an abundant squash harvest."
        "It felt like we were drowning in squash. We made roasted squash, sauteed squash, squash soup, squash with honey, and squash pie."
        "And when we got tired of squash, it was okay, because it would keep for months."
    else:
        "So if I wanted to get a decent squash harvest this year, I'd need to help them out."
        menu:
            "Pollinate by hand" if (get_extra_work() >= 0):
                him determined "I guess I'm Cupid's little helper today..."
                "I took a paintbrush and dabbed the pollen from the male flowers and then brushed it on the female flowers."
                "Since there were several flowers on each plant, and a whole field full of plants, it took quite a while."
                "But it wasn't difficult, and it did increase our squash yield dramatically."
                # TODO: increase yield/work?
            "Ask to borrow some bees" if (year > 10):
                "I thought I remembered someone saying something about bees, but I couldn't remember who."
                nvl clear
                him_c "Hey, anyone have extra bees? My squash needs pollination!"
                natalia_c "We got some from Kevin."
                julia_c "Send your kids to pollinate the plants by hand. The work will be good for them."
                kevin_c "I do have bees, but not extra."
                nvl clear
                "Maybe if I talked to Kevin in person we could work something out."
                scene farm_exterior_flip with fade
                show kevin at midright with dissolve
                show him normal at midleft with moveinleft
                him happy "Hey, Kevin! How's it going?"
                kevin "Satisfactorily."
                him normal "Good, good...hey, about those bees..."
                kevin "I apologize, but I do not have extra bees at this time."
                him concerned "Could I maybe, like, borrow them, just for a few weeks?"
                kevin "I could rent them to you."
                # TODO: currency check.
                menu:
                    "What should I say?"
                    "Could we trade?":
                        him surprised "Could we trade? Maybe for squash?"
                        kevin "Squash and goat's milk, in these quantities."
                        him normal "Looks reasonable. It's a deal."
                    "Okay, how about for 10?":
                        him normal "Okay, how about 10?"
                        kevin "That is insufficient. I propose 20."
                        him surprised "Maybe 15?"
                        kevin "18 is the lowest I will consider."
                        him normal "All right, 18 it is."
                    "I'll pay you 20.":
                        him normal "I'll pay you 20 for them."
                        kevin "That is acceptable."
                        him "It's a deal."
                kevin "Good. I will write up a contract."
                him annoyed "A contract, huh?"
                kevin "Yes. That way the terms are clear and unarguable by both sides."
                "I couldn't really argue with that."
                "I skimmed his legalese and it looked reasonable. For the consideration of the use of his bees, blah blah blah, the undersigned hereby agree to blah blah blah."
                "I transported his hive of bees at night, when most of them were sleeping, and in the morning they woke up to a new home."
                "They seemed to adjust pretty well, and went right for the squash blossoms."
                "I was kind of sad to give them back."
                "We harvested a lot of squash that season!"

            "Forget the squash for this season":
                "I didn't have time to baby the plants. They'd have to survive on their own."
                "Some of them produced fruit, but most didn't. What a waste..."
                # TODO: decrease food/income
    return

# SQUASH2 - squash bugs
label squash2:
    scene fields with fade
    show him normal at center with dissolve
    "I went to weed the squash plants, but as I was weeding, I noticed something."
    him surprised "These plants are a bit smaller than they should be...and some of the leaves have yellow spots on them."
    him angry "What the- squash bugs! I thought we left all those behind on Earth!"
    "Squash bugs were probably my least favorite insect of all time. They reproduced like crazy and devoured entire squash plants, leaves, flowers, fruits, and all."
    "They must have been transported on one of the shuttles -- maybe in some wood or fruit."
    "But I didn't have time to waste on being furious. I had to get rid of them!"
    menu:
        "Exterminate them all by hand!" if (get_extra_work() >= 0):
            $ squash2_method = "exterminate"
            if (year >= 10):
                "[kid_name] and I tried every way we could think of to get bugs off the plant -- we used duct tape to pick up eggs and tiny bugs, tweezers to squish them, and our hands to drop them into soapy water."
                "At first the vinegary smell of the squished bugs grossed [kid_name] out, but eventually she got over it."
            else:
                "I tried every way I could think of to get bugs off the plant -- I used duct tape to pick up eggs and tiny bugs, tweezers to squish them, and my hands to drop them into soapy water."

            "Up and down the rows of squash I stalked every day for a week."
            "The population had decreased, but there were still stragglers out there; I knew it."
            "And all it would take would be one batch of eggs I missed and the bugs would start up again."
            "I continued my diligence until the squash was harvested."
            "Then I burned the squash plants instead of composting them.  I didn't want to have this problem next year."
        "Apply pesticide.":
            $ squash2_method = "exterminate"
            if ("bees" in farm.crops):
                "I didn't want to hurt my plants or bees, so I decided to spray the bugs with soapy water."
            "I didn't want to hurt my plants, so I decided to spray the bugs with soapy water."
            if (year >= 10):
                "[kid_name] and I got spray bottles and sprayed every bug we saw, from the tiny eggs and nymphs to the larger adults."
            else:
                "I got a spray bottle and sprayed every bug I saw, from the tiny eggs and nymphs to the larger adults."
            "The spray seemed to work pretty well, though there were so many bugs I knew some of them were hiding."
            "We sprayed every day for a week."
            "It seemed to be working; we saw less bugs each time."
            "But we continued our daily squash bug patrol until we harvested the squash."
            "Then I burned the squash plants instead of composting them.  I didn't want to have this problem next year."
        "Ignore them":
            $ squash2_method = "ignore"
            "Ugh, I didn't want to deal with squash bugs. It was impossible to completely eradicate them, anyway."
            "Why start a battle I knew I couldn't win?"
            "But that meant I only havested one fourth of the squash I had planned on."
            # TODO: currency check: lose money
        "Try and get the new folks to fix the problem. They started it, after all!":
            $ squash2_method = "passthebuck"
            nvl clear
            him_c "Alright, who brought squash bugs to Talaam?!"
            if (year < 11):
                martin_c "Not squash bugs!"
            else:
                natalia_c "Oh no, not squash bugs!"
            sara_c "What are squash bugs????? 😮"
            natalia_c "A squash farmer's worst nightmare. I haven't seen any here yet, but if they're anywhere on the planet I'm sure they'll find all the squash plants."
            him_c "They found all of mine. But whoever brought them should be responsible for getting rid of them!"
            if (year < 15):
                naomi_c "Do you think someone brought them here on purpose?"
            else:
                sara_c "You're not saying someone brought them here on purpose?! 😵"
            him_c "Purpose or accident; it doesn't matter!"
            sara_c "But... how would you even figure out where they came from?"
            him_c "We know where they came from -- the shuttle!"
            if (year <= 11):
                kevin_c "And which of the hundred and six new colonists do you propose take care of your problem?"
                him_c "I don't know; all of them! Any of them!"
                kevin_c "I sympathize with your plight, but we cannot aid you."
                him_c "But...!"
            else:
                brennan_c "Are you implying some of my crew is sabotaging your crops?"
                him_c "I don't know exactly how it happened, but you've got to do something!"
                brennan_c "What do you want me to do? Send my miners over with some dynamite or jack hammers? You're the farmer, [his_name]."
                him_c "They don't have to be farmers to help me kill these bugs."
                brennan_c "Your proposal is ridiculous. We've got our own schedule to keep. We don't have time to stop and help every snivelling farmer with a pest problem."
                him_c "But...!"
                $ miners -= 1
            nvl clear
            sara_c "Oleg and I can come help you on Monday morning. We don't know anything about squash but we can kill bugs! 🐞😡💀"
            natalia_c "I'll help you Tuesday. If we can get rid of them on your farm, maybe they won't spread to mine."
            julia_c "Two of my children will assist you on Wednesday. Don't go easy on them."
            him_c "You guys... you don't have to do this. I know you have your own farms to work on..."
            kevin_c "I can spare a few hours on Thursday."
            pavel_c "I will stop by on Friday, though I don't know how long I can stay."
            him_c "You're too generous...I can't..."
            her_c "Just say thank you, [his_name]."
            him_c "...Thank you, everyone."
            nvl clear
            $ colonists += 1

    return

# SQUASH 3 - consequences of squash bug method.
label squash3:
    "I was curious to see how this next batch of squash would fare; given the trouble I had with squash bugs last time."
    if (squash2_method == "ignore"):
        "I didn't think it was possible, but there were even more squash bugs this year. The plants didn't even have a chance to set any fruit at all before they were completely devoured."
        "I couldn't plant squash again until at least a year had passed. Maybe if they didn't have any squash to eat, they'd all die out."
        $ crop_temporarily_disabled = "squash"
        # TODO: currency check, reduce income by squash amount
    else:
        "I checked the seedlings every day for signs of squash bugs. Nothing."
        "Was it possible I had exterminated all the squash bugs on the planet??"
        "No, I needed to stay vigilant!"
        "Sure enough, as the flowers bloomed and squash started to grow, I noticed one plant looking a little less healthy than the rest."
        "There were squash bugs on it!"
        "It was much easier to kill them all when they were all one plant. I scrutinized that section every day and got rid of all the bugs and eggs I saw."
        "The result was a bountiful squash harvest, even more than I had projected."
        # TODO: currency check, add bonus
        "Would it ever be possible to get rid of every single squash bug? I don't know. But the harvest made all the hard work worth it."
    return

# GOATS1 - GOAT CHEESE
label goats1:
    scene fields with fade
    show him normal at center with dissolve
    "When Thuc first brought over a few young goats, I used them mostly as lawnmowers and fertilizer producers."
    "But after a year or two, they were old enough to start breeding. And baby goats means milk!"
    "I milked our two mama goats every day, and they still had enough milk for their babies."
    "We didn't always drink a lot of milk, so sometimes I had a lot of extra..."
    nvl clear
    him_c "Hey, Thuc, what do you do with extra milk from your goats?"
    thuc_c "Cheese, mostly. It goes with everything and the kids like it."
    him_c "Your... kids?"
    thuc_c "Ha ha, I don't feed it to baby goats. I meant, my children like it."
    him_c "Heh, yeah. Do you have some starter culture I could borrow? Do I need rennet?"
    thuc_c "We actually weren't allowed to bring starter cultures -- they were worried we'd contaminate Talaam with too much Earth bacteria."
    him_c "Oh, I see. No yogurt then, huh?"
    thuc_c "Not yet. I've tried several ways of getting yogurt going with local bacteria but none of them have worked yet."
    him_c "How do you make the cheese, then?"
    thuc_c "You just need an acid, like vinegar. No rennet either. I'll send you the recipe."
    nvl clear

    "It was so simple I was suspicious. Just heat the milk, add some acid, and then pour it through a cheesecloth??"
    "But... it worked. I added salt and a few herbs and let it sit, and then we had delicious fresh chèvre."

    scene farm_interior with fade
    show him happy at midright
    show her normal at midleft
    with dissolve
    him happy "So... what do you think?!"
    her concerned "It tastes a little...goaty."
    him flirting "But also cheesy, right?"
    her normal "Yeah... it's pretty good. I think we need to eat it with something, though."
    him normal "I'm thinking baked potatoes."
    her happy "Oh yeah, that'll be so good!"
    "We made goat cheese almost every day after that."
    return

# GOATS 2 - male goats contaminating milk
label goats2:
    "Having goats was pretty great. They mostly took care of themselves, and they also took care of my weeds and gave milk."
    "But lately..."
    scene farm_interior with fade
    show her determined at midright
    show him normal at midleft
    with dissolve
    her concerned "This milk... doesn't taste right."
    him surprised "Really? Let me try..."
    "She was right. It tasted a bit sour, and more... goaty than usual."
    "We made it into cheese and the taste was less noticable."
    scene barn with fade
    show goat at midleft
    show him normal at midright
    with dissolve
    "The next time I milked the goats, I smelled that same smell, but not from the milk..."
    show goat_flip at quarterright with moveinright
    him "Hey!"
    "One of the male goats was peeing on his face, and a bunch of it got on me."
    "That was where the bad smell was coming from."
    "After some research I found out that the male goats got stinkier as they aged, and used that stinkiness to attract a mate."
    "I wasn't opposed to the goats mating -- that would mean more kids, and the does' milk production was decreasing since it had been a while since they had a kid."
    "But I didn't want the milk to taste like goat pee."
    "I decided to ask Thuc."
    nvl clear
    him_c "How do you keep the male goats from peeing on everything? It's pretty stinky."
    thuc_c "You can't. We keep the bucks separated from the rest of the herd, and only let them get together for romantic goat dates."
    him_c "You have two herds?"
    thuc_c "Yeah, it works better that way. Plus, then we know when the kids will be born."
    him_c "I only have one buck right now...He'd probably get lonely."
    thuc_c "What about all your bucklings? Did you castrate them?"
    him_c "No, should I have? They're still small..."
    thuc_c "They can mate after just a few months."
    him_c "Oh... we may end up with some surprise kids, then!"
    thuc_c "You, or your goats?"
    him_c "Ha ha, you know what I mean."
    nvl clear

    "So it sounded like I needed to separate or neuter the bucks. Or butcher them."

    menu:
        "Smuggle some to Pete" if (year >14): #only if Pete and his group have left
            "I felt bad for Pete. Maybe he would like some goats."
            "I couldn't send him a message; radio communications weren't private."
            "I'd have to just go over there."
            # TODO: background for Pete?  Like this? https://pixabay.com/en/barn-field-agriculture-countryside-238512/
            scene fields with fade
            show pete at midright with dissolve
            show him normal at midleft with moveinleft
            if (luddites_strength() >= 1):
                pete "Hey there, [his_name]. Good to see ya."
            else:
                pete "What do {b}you{/b} want?"
            him normal "Hey, Pete! I just wondered if you wanted some goats. The bucks are getting ornery and I really don't want to have two herds."
            pete "I got plenty of cows to take care of."
            him surprised "Really? Goats aren't much trouble. They just need a fence and a place to sleep. Or you could just eat them."
            pete "Well... actually, it might be good project for Trevor. But I'd need a doe, too."
            him "Sure, I can spare one. She's almost full grown."
            pete "Alrighty then. I'll have some beef to trade you for, alright?"
            him "Sounds good. Later, Pete."
            $ luddites += 1
        "Send the meat to the storehouse":
            "I didn't want to have two goat herds. That would just be too much work."
            "So I slaughtered them, cut up the meat, and sent it to the storehouse."
            "While I was there, I was able to pickup a bunch of foods my family had been craving."
            scene farm_interior with fade
            show her normal at midright
            show kid normal at center
            with dissolve
            show him normal at midright with moveinright
            him flirting "Too bad no one here likes applesauce. I guess I'll have to eat this all by myself."
            if (year >= 7):
                kid happy "Applesauce!"
            her happy "Delicious!"
            $ colonists += 1
        "Process the meat" if (get_extra_work() >= 0):
            "We had several goats to butcher, so I wanted to preserve the meat."
            "Plus, I had a craving for sausage."
            "After butchering, I ground up all the meat and separated it into two portions."
            "The first was for ground sausage. I seasoned it up and it'd be great with breakfast or in sauces."
            "The second portion was for pepperoni. I'd been craving pepperoni since we moved here -- pepperoni pizza, pepperoni on crackers, huge chunks of savory pepperoni..."
            "Anyway, I was going to try to make some out of goat meat."
            "I cleaned the intestines to use as casings, added spices and vinegar to the meat, and stuffed the mixture in."
            "Then I let the sausages hang from the ceiling for two months."
            "Every time I saw them my craving for pepperoni grew."
            "Finally, it was time to taste them."
            "I cut a thin slice and placed it on my tongue. Meaty? Yes. Salty? Yes. Peppery? Yes. Goaty? ...yes."
            "It was not quite the same as the pepperoni from Earth, but it was delicious just the same."
            "I sold two links of it at the storehouse and had enough money to buy wheat so we could make pizza."
            scene farm_interior with fade
            show him happy at midright with dissolve
            show kid normal at center
            show her normal at midleft
            with moveinleft
            him happy "Dinner's ready!"
            her surprised "Is this a... pepperoni pizza?! Ohhh, [his_name]!"
            if (year >= 7):
                kid "What's pepponi pitsa?"
                him determined "Only the best food ever invented."
                her concerned "It might taste weird to her, though."
                him happy "That's fine; I'll eat hers!"
                kid "I want to try it!"
            "We each took a slice. The goat cheese didn't really pull into long strings like mozzarella, but it had melted into nice medallions on the top."
            "The whole wheat crust was denser and less puffy than traditional pizza, too."
            "But after one bite, I was in heaven. The pizza was just slightly crunchy, with tangy tomato sauce, creamy cheese, and, best of all, big rounds of pepperoni that were just the slightest bit cripsy."
            kid "Hot!"
            her sleeping "Mmmm."
            him sleeping "Mmmmmmm."
            her happy "Wow. I haven't had pizza in so long! I'm glad your pepperoni turned out."
            him sleeping "Ummm."
            "I couldn't even talk. I was too entranced by the flavors, the textures, the memories..."
            "Pizza after a soccer game, pizza at a video game party with friends, pizza with [her_name] on a rainy night in, feeding each other and laughing and cuddling on the couch..."
            her surprised "Are... are you crying?"
            him sad "This... is the best pizza I've ever had. It tastes like... Earth."
            if (year >= 7):
                kid "Earth is spicy?"
                her concerned "Spicy and sweet and creamy and saucy and complicated."
                him flirting "Sounds like someone else I know."
                her flirting "Shut up and eat your pizza."
                if (year >= 20):
                    kid "Dad, that was so bad."
                    him surprised "Was it so bad it's... cheesy?"
                    kid "Ohhh, dad!"

        "Allocate more land for goats":
            "If we needed two herds, then I'd make two herds. It wasn't too much work to make another goat pen and feeding area."
            "And it would be better to control the goats' mating, so we didn't have goats getting pregnant too young or goat pee smell getting on the milk or things like that."
            "I'm sure we'd eat some of these goats eventually, but for now I just wanted to grow the herd."
            $ goats_index = get_crop_index("goats")
            $ crop_info[goats_index][MAXIMUM_INDEX] += 1
            # goats take up another square now.

# GOATS 3 - escaping goats
label goats3:
    "Our little goats were quite the escape artists. One time I left a barrel in their pen too close to the fence, and soon they had all jumped the fence and were terrorizing my garden."
    "Another time they dug one of my fence posts out and all snuck under the fence."
    "Luckily, each of these times I caught them pretty quick."
    "But not one time..."
    scene fields with fade
    show him normal at center with dissolve
    if (year > 7):
        show kid normal at midleft with dissolve
    him surprised "Hey, did the goats all go inside...?"
    "That seemed unlikely, so I went to go check it out."
    # TODO: some kind of goat pen background?
    hide him
    hide kid
    with moveoutleft
    scene fields with fade
    show him normal at center with moveinleft
    if (year > 7):
        show kid normal at midleft with moveinleft
    "The gate was wide open and all the goats were gone. Really gone. Not a goat in sight."
    if (year > 7):
        him annoyed "Did you leave this gate open?!"
        kid nervous "No, I know I closed it all the way!"
        "I wasn't sure if I believed her, but either way, we needed to find those goats."
    else:
        show him surprised
        "I know I had shut it all the way. Hadn't I?"
        him concerned "...I've gotta find those goats."
    "Luckily, they had left some tracks in the moist ground."
    $ random_crop = farm.crops.random_crop(include_animals=False)
    "I followed the tracks through a nibbled-on field of [random_crop] and onwards past our property."
    "My heart sank as I realized we were heading on towards the Nguyen's farm. Hopefully it would be Thuc I met first, and not Julia..."
    scene fields with fade
    show julia at quarterright
    show goat at midright
    with dissolve
    show him determined at midleft behind goat with moveinleft
    if (year > 7):
        show kid at quarterleft with moveinleft
    "Sure, enough, Julia was there scowling and flapping a dishtowel, trying to drive the goats away."
    show julia at midright with move
    show goat at center with move
    "They'd skitter a few steps away, then go right back to nibbling on some sweet potato vines."
    julia "There you are!"
    him concerned "Sorry about the goats. I just noticed they got out."
    julia "Well, they've been here all morning. I'm not sure my poor sweet potatoes will recover."
    him "I-"
    julia "I tried to reach you on the radio, but you didn't answer."
    "She looked pointedly at my radio on my belt -- it was turned off. I often 'forgot' to turn on my radio -- the truth is, I liked the peace and quiet."
    him "Must have forgotten to turn it on. Well, I'll just get these goats out of your way."
    hide him
    hide kid
    hide goat
    with moveoutleft
    scene fields with fade
    show him determined at center
    show goat at midleft
    with moveinright
    if (year > 7):
        "With me leading the way and [kid_name] chivvying them from behind, we managed to get the goats back in their pen."
    else:
        "I got the goats' attention and led them back to their pen. They recognized me as their herd leader and mostly followed, though they kept getting distracted by interesting plants along the way."

    "I examined the pen closely. The gate seemed to shut securely when I fastened it, and the fence was intact. There weren't any large objects the goats could climb on to jump out."
    "So how had they escaped?"
    menu:
        "What should I do?"
        "Watch the goats for a while.":
            "I decided to watch and see."
            "I observed them for fifteen minutes but didn't see anything out of the ordinary. Maybe it was just a fluke?"
            "I left to weed the [random_crop], but when I came back to check on the goats, they were out again."
            "These goats weren't stupid. Not only had they figured out how to escape a securely closed pen, but they knew not to do it while I was watching."
            "But did they know about my surveillance cameras?"
            "I went back to the house and reviewed the footage on my computer pad."
            "I couldn't believe it. One of the goats had figured out how to lift and slide the bolt with her horns!"
            "In fact, she was doing it right now."
            "I put the goats back {b}again{/b} and rigged the slide shut more securely with some wire."
            him determined "Now, let's see you open {b}that{/b}."
        "Recompense Julia.":
            "I was most worried about our relationship with the Nguyens. There was no way Julia would just forget about it."
            $ random_crop = farm.crops.random_crop(include_animals=False)
            "But maybe if I took them some [random_crop] she'd forgive me."
            scene fields with fade
            show julia at midright with dissolve
            show him determined at midleft with moveinleft
            him determined "I just wanted to apologize for my goats getting into your sweet potatoes. Here's some [random_crop] for you."
            julia "Hmph. It's a start, anyway."
            him surprised "A start?!"
            julia "I'll let you know in a week if the plants recover or not. If not, we'll need twice this amount to make up for it."
            "Sometimes, I couldn't believe this woman. How Thuc could stand being married to her, I had no idea."
            him annoyed "I guess we'll see then."
            julia "Yes, let's wait and see."
            hide him with moveoutleft
            scene fields with fade
            show him determined at center with moveinright
            "When I got back, the goats had escaped... again."
            "They hadn't made it to Julia's property yet, though."
            "This had to stop."
            "Then suddenly I rememberd the surveillance cameras. They could show me how the goats kept getting out!"
            "When I checked the footage from my farm surveillance cameras, I saw what had happened."
            "One of the goats lifted the bolt slide with her horns, slid it to the side, and opened the gate."
            him surprised "Guess I need to figure out a better gate!"
            "I added some wire to hold the slide bolt in place, and the goats stayed in their pen after that."
            him determined "Now, let's see you open {b}that{/b}."

        "Scold [kid_name]." if (year > 7):
            "It must have been [kid_name]. There's no other possibility."
            show kid at midright with moveinright
            him determined "[kid_name], I'm disappointed that you let the goats escape."
            kid sad "It wasn't me! I closed it all the way, I know I did!"
            him concerned "It's the only explanation that makes any sense."
            kid angry "What if the goats opened it?"
            him surprised "What if the goats opened what?"
            kid annoyed "The gate. Maybe they figured out how to open it?"
            "Was it possible? I thought the bolt was pretty goat-proof."
            menu:
                "What should I do?"
                "Make [kid_name] observe the goats.":
                    him annoyed "You stay here and watch them. I have work to do."
                    "I went back to weeding the [random_crop]. After an hour, I went back to check on [kid_name] and the goats."
                    him surprised "Well?"
                    kid annoyed "They haven't done anything weird... it's like they know I'm watching them."
                    him normal "Goats are pretty smart."
                    kid surprised "Isn't there some way we can watch them without them knowing?"
                    jump goat3_cameras
                "Observe the goats together.":
                    jump goat3_observe
                "Get back to work.":
                    him annoyed "That's not possible. One of must have not closed it all the way, and I know it wasn't me, so it had to be you. Time to get back to work."
                    kid concerned "Okay, but it wasn't me."
                    "I slid the bolt closed and pushed it down. At least this time the gate was secure."
                    "We went back to weeding the [random_crop] and after twenty minutes I went to check on the goats."
                    "They had escaped again."
                    "[kid_name] and I put them back in the pen again."
                    kid annoyed "See? They got out even when you closed it."
                    him concerned "Yeah..."
                    label goat3_observe:
                        "We watched them for a few minutes, but they didn't try to escape or anything. Just munched on grasses and walked around."
                    label goat3_cameras:
                        him happy "The cameras!"
                        "When we checked the footage from my farm surveillance cameras, we saw what had happened."
                        "One of the goats lifted the bolt slide with her horns, slid it to the side, and opened the gate."
                        him surprised "No way!"
                        kid happy "I told you!"
                        him normal "Guess we need to figure out a better gate!"
                        "We added some wire to hold the slide bolt in place, and the goats stayed in their pen after that."
                        him determined "Now, let's see you open {b}that{/b}."

    return

# TOMATOES 1 - blossom end rot
label tomatoes1:
    $ tomatoes1_action = "none"
    "There's nothing like fresh, juicy tomatoes straight from the vine. The sweet juice, the way the seeds squirt all over when you bite into them, their perfect roundness..."
    "But the best thing about growing tomatoes on Talaam was that there were no hornworms!"
    "As a kid I spent hours hunting those giant green caterpillars. I earned a bounty for every hornworm I destroyed."
    "In fact, it was a little bit sad that [kid_name] wouldn't have that opportunity..."
    "...but not too sad."
    "This year, my tomatoes were doing pretty well, but a lot of them had a sunken, mushy area on the bottom."
    menu:
        "Do some research." if (get_extra_work() >= 0):
            "I did a bit of research about tomato problems and found something that described my tomatoes exactly."
            "Blossom-end rot.  If I added some more calcium to the soil and watered more evenly, this shouldn't happen next time."
            $ tomatoes1_action = "research"
        "Just cut it off.":
            "Most of the tomato was fine.  I'd be canning most of them, anyway, so it didn't really matter."
            $ tomatoes1_action = "cut"
        "Add more fertilizer.":
            "I decided that they probably just needed more fertilizer.  So next time I'd add more."
            $ tomatoes1_action = "fertilize"
    return

# TOMATOES 2 - results of tomatoes 1
label tomatoes2:
    $ tomatoes2_action = "none"
    if (tomatoes1_action == "research"):
        "The tomatoes looked much better this year!"
        menu:
            "Now, I needed to choose which fruits to save seeds from for planting next year."
            "First tomatoes":
                $ tomatoes2_action = "early harvest"
            "Biggest tomatoes":
                $ tomatoes2_action = "size"
            "Sweetest tomatoes":
                $ tomatoes2_action = "sweetness"
    else:
        "The tomatoes have the same rotten bottom area as last time, only now it's even worse!"
        "You do some research and find out that usually that means there's too much nitrogen in the soil and not enough calcium."
        if (tomatoes1_action == "fertilize"):
            "So adding more fertilizer just made it worse."
        "Most of my tomatoes were useless..."
        # TODO: decreased yield/money
    return

# TOMATOES 3 - results of tomatoes 2
label tomatoes3:
    if (tomatoes2_action  == "early harvest"):
        "Because I made sure to always save seeds from the earliest tomatoes, the genetics of the tomato plants every year tended towards a fast harvest."
        "In fact, now I can squeeze in two plantings a year, effectively doubling my tomato harvest."
        # TODO: increase yield/money of tomatoes.
    elif (tomatoes2_action == "size"):
        "Since I only used seeds from the biggest tomatoes, the size of the tomatoes kept getting bigger and bigger."
        "Not only did they look impressive, but they were easier to process because I had less stems to cut off before canning them."
    elif (tomatoes2_action == "sweetness"):
        "As I selected for the sweetest tomatoes, my harvest got slowly sweeter and sweeter."
        "[her_name] will sometimes pack a lunch of just tomatoes and a little goat cheese."
        "And [kid_name] likes to eat them, too."
        "They were so sweet I used them like berries in dessert dishes."
    else:
        "Finally, I had a good tomato harvest. The tomatoes were firm all over and there were plenty of them."
        "Time for salsa, spaghetti sauce, and maybe even some pizza!"

    return

# PLUMS 1 - trees growing
label plums1:
    "I was happy to see the plum trees getting larger and larger."
    "They didn't have any fruit now, so it felt like a lot of work for nothing."
    "But I knew if I kept taking care of them and fertilizing them, eventually they would bear fruit."
    return

# Several years later
# Prunes or jam?
label plums2:
    scene fields with fade
    show him at center with dissolve
    "I'll never forget the first time the plum trees really bloomed..."
    "Thousands of pink blossoms covered the trees this spring, and when they fell, their petals covered the ground in a soft pink carpet."
    # TODO: plum blossom CG? bg?
    if ("honey" in farm.crops):
        "The bees helped the pollination a lot."
    else:
        "I had to pollinate them by hand, but my hard work paid off."
    "The ephemeral beauty of the plum blossoms was rivalled only by their later, more practical beauty..."
    "Plums!"
    "There were so many plums growing, I had to thin out some of the fruit so the branches wouldn't break under their load."
    "The only fresh fruit we had was what we grew ourselves, so I was really looking forward to eating the plums."
    "I watched them every week until the fruits had grown large and purple."
    "And, of course, I had to try one every few days to see if they were ripe."
    "The first few times the fruits were still sour."
    "But finally they started to soften and ripen, and when I ate one, the juice dribbled down my chin and my taste buds exploded with the tangy sweet, rich flavor."
    "No matter how tasty they were, though, there were still limits to the amount of plums a small family could eat at a time."
    "I'd need to do something with all these plums..."
    "I could just bring them to the storehouse, but they'd be worth more if I made them into prunes or jam first."

    $ make_item = "plums"
    menu:
        "What should I do?"
        "Make prunes" if (get_extra_work() >= 0):
            $ make_item = "prunes"
            "I pitted them and put them on a rack to dry."
            "I had to put a screen over them to keep pests away, but after several days I had some delicious prunes."
            show her normal at midleft with moveinleft
            show him at midright with move
            her surprised "Prunes? That's wonderful! I don't have much constipation medicine so it'll be great to have a natural remedy instead."
            him annoyed "You don't have to be constipated to enjoy some good prunes."
            her normal "They'll be good for [kid_name], too. Thanks, [his_name]."
            "I dropped most of them off at the storehouse and didn't think much about it for several days, until I got a visitor."
            scene farm_exterior with fade
            show him normal at midright with dissolve
            show thuc normal at midleft with moveinleft
            thuc "Man, I'm so glad you made prunes. Can I just say, everything around here is going a lot more smoothly?"
            him surprised "You like prunes?"
            thuc "Well, one of my kids really needed them. I don't want to embarrass them, so that's all I'm going to say. But thank you!"
            him normal "You're welcome, I guess."
            thuc "In fact, I brought you a little something."
            "He handed me a basket full of heads of garlic."
            him surprised "Oh, thanks!"
            thuc "This is nice and fresh, so you can plant it or eat it."
            him "Mmmm, this'll be good! Thank you!"
            "I couldn't wait to eat some, but even better, now I could grow my own."
            $ enable_crop("garlic")
            return

        "Make jam" if (get_extra_work() >= 0):
            $ make_item = "jam"
            "I decided to make jam."
            "My mother always made jam with sugar and pectin."
            "It would kind of defeat the purpose of making jam if I had to buy expensive sugar and pectin to make it work."
            "After some research, I found plums already have a fair amount of sugar and pectin in them. So I decided to slow cook them until they made a thick jam."
            "It was a bit sour, but very flavorful. And the jars should last at least a year."

            scene storehouse with fade
            show ilian at midright with dissolve
            show him normal at midleft with moveinleft
            him "Hey there, Ilian."
            ilian "Oh. Hello."
            him happy "How much can you give me for this plum jam?"
            ilian "I can only give you amount." # TODO: currency check.
            him surprised "What? Why is that?"
            ilian "I'm out of money. But if you'd like to exchange, I can give you onions or turnips."
            menu:
                "Which should I choose?"
                "Onions":
                    him "Give me the onions."
                    $ enable_crop("onions")
                "Turnips":
                    him "How about the turnips?"
                    $ enable_crop("turnips")
            ilian "Fine. Here you go."
            "My plum jam didn't make me rich, but at least I'd be able to plant something new now."
            return

        "Just bring the plums to the storehouse.":
            "I decided to just bring the plums to the storehouse. I didn't have time for anything else."

    if not (renpy.showing("storehouse")):
        scene storehouse with fade
        show ilian at midright
        show him normal at midleft with dissolve

    "While I was at the storehouse, I saw that they had a ton of onions for a good price."
    "If I bought them, I could plant some and grow my own..."
    menu:
        "What should I do?"
        "Buy onions.":
            # TODO: currency check, subtract amount for onions.
            "I decided to buy them. It's always good to have more crops to choose from, and onions go well with everything."
            $ enable_crop("onions")
        "Don't buy onions":
            "I decided not to buy them. I had enough crops to deal with."

    return

# BEANS 1 - How to harvest beans
label beans1:
    scene fields with fade
    show him normal at center with dissolve
    him happy "Look at all these beans!"
    him normal "And they're finally dry enough to harvest."
    "I drove the tractor down the rows so the puller attachment could pluck up the plants from the ground."
    "Then I fed them into the sheller to separate the pods from the beans."
    if (year >= 7):
        show kid normal at midleft with moveinleft
        kid "Can I turn the crank?"
        him happy "Of course!"
        "She only lasted for a few minutes, but it gave me a chance to move some things around so that the shelling would be more efficient."
        "When we got tired of turning the crank by hand I attached my drill to turn it for us. That went even faster."
        "We filled up barrels and barrels of dried beans."
    else:
        "When I got tired of turning the crank by hand I attached my drill to turn it for us. That went even faster."
        "I filled up barrels and barrels of dried beans."
    return

# BEANS 2 - Wet beans
label beans2:
    scene fields with fade
    show him concerned at center with dissolve
    him concerned "The beans are supposed to be drying so I can harvest them..."
    him annoyed "But it keeps raining."
    "I was worried that if the rain kept up, they might start to grow fungus or bacteria before they'd be dry enough to store."
    "But how could I get them dry when it was so wet outside?"
    $ harvest_factor = 1.0
    menu:
        "What should I do?"
        "Wait for the rain to stop.":
            "It couldn't rain forever...I decided just to wait."
            "But it rained for over a week."
            "When it was finally dry, I checked on the beans..."
            "...and most of them were moldy."
            him annoyed "That was a lot of work for nothing."
            $ harvest_factor = 0.25
        "Hang them up somewhere dry.":
            "I needed them to dry, so I decided to hang them up."
            "I strung clothesline zig-zagging around the house and in the barn."
            "I hung them upside down in bunches everywhere."
            show her at midleft with moveinleft
            her flirting "Trying your hand at interior design?"
            him annoyed "I'm trying my hand at saving our beans."
            her surprised "Saving them?"
            him normal "Yeah, if I leave them out in this rain they'll get moldy before we can harvest them."
            her concerned "I guess this planet has plenty of fungus, huh?"
            him determined "I don't know if we brought spores from Earth or if it's native, but there's definitely some types of fungus here that will grow on beans."
            her normal "Okay, I guess we can live with a bean canopy over our heads for a while."
            "I was able to hang up most of the bean plants, and after two weeks the beans were dry enough to harvest."
            $ harvest_factor = 1.0
        "Cover them with a tarp.":
            "I decided to just throw some tarps over them. That should keep them dry enough."
            "But it rained for over a week, and the rain seeped in under the tarp. The whole bottom layer was moldy."
            "At least the top layers dried out okay."
            $ harvest_factor = 0.65

    # TODO: currency check; subtract harvest_factor of the bean profit
    return

# SPINACH 1 - heat wave kills spinach seeds
label spinach1:
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

# SPINACH2 - turtle slugs
label spinach2:
    $ crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] += 1
    scene fields with fade
    "This year, I planted my spinach a little earlier to avoid any heat problems."
    "Now it's almost to full size."
    "But something has been eating the plants. I haven't seen anything, but when I checked the leaves, I could see bites taken out."
    $ spinach2_cameras = False
    menu spinach_3_menu:
        "Check the surveillance cameras" if (not spinach2_cameras):
            "I trained the farm's cameras on the spinach plot, but the next morning when I looked at the video, none of the motion sensors were triggered.  I scanned through the video but couldn't find anything out of the ordinary."
            $ spinach2_cameras = True
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
                                kid normal "There you go little buddies."
                                him happy "Bye bye, vicious spinach eaters!"
                            "Have [kid_name] help you kill them.":
                                $ confident += 1
                                him determined "I'm not going to kill them. You are."
                                kid angry "What?! No. No way!"
                                him annoyed "If we don't, they'll destroy our crops. Not just this year, but next year, too."
                                kid sad "They just want to eat a little spinach."
                                him concerned "They will eat all our spinach, and they won't stop there."
                                if (is_independent()):
                                    call spinach2_eat_snails
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
                                    "I dropped them in a bucket of water one by one and that seemed to kill them."
                            "Send her away and kill them yourself.":
                                him determined "I'll take care of it. You just run along, now."
                                if (is_independent()):
                                    call spinach2_eat_snails
                                else:
                                    hide kid with moveouleft
                                    "She left, and I carried out the death sentence on the turtle-snails."

                    "I made some more traps and repeated the process until no more turtle-snails appeared."
                    "And we harvested a lot of wonderful spinach."
                "Just pick the spinach early":
                    call spinach2_pick_early
        "Just pick the spinach early":
            call spinach2_pick_early
    return

label spinach2_eat_snails:
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
    "So I disposed of them."
    return

label spinach2_pick_early:
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
    "After we picked the spinach, they moved on to our [snail_crop]."
    him annoyed "This is something that I cannot forgive."
    him angry "This means war!"
    "My nights were filled with killing turtle-snails."
    "They appeared in my dreams, giant, house-sized turtle-snails with ever-chewing mouths, the entire earth disappearing beneath their slavering jaws until Talaam was just an empty spot in the vast blackness of space."
    "I started seeing them everywhere I looked -- in the fields, in the barn, in the outhouse."
    "Finally, their numbers were greatly reduced, and I could rest.  Until the next invasion..."
    return

# Strawberries 1 - grow more?
# TODO: Test this to see if it works with strawberries+
label strawberries1:
    scene fields with fade
    show him normal at midright
    show kid at midleft with dissolve
    him normal "These strawberries are the best!"
    kid "Mmmm!"
    "We didn't have a lot of extra strawberries for jam or anything, but they tasted so sweet and delicious."
    "There's nothing like a fresh, warmed-in-the-sun, juicy, sweet, home-grown strawberry."
    "The other nice thing about strawberry plants is that they made lots of runners. If I wanted to, I could pull them up and start another strawberry field."
    menu:
        "What should I do?"
        "Expand your strawberry empire." if (get_extra_work() >= 0):
            him happy "What could be better than more strawberries?!  Let's plant some more, [kid_name]!"
            kid "Yeah!"
            $ strawberries_index = get_crop_index("strawberries")
            $ crop_info[strawberries_index][MAXIMUM_INDEX] += 1
            $ enable_crop("strawberries")
        "Sell the extra plants.":
            "I didn't really need more strawberry plants.  But maybe someone else did."
            nvl clear
            him_c "I've got some extra strawberry plants I'm willing to sell. They grow fast and easy and taste delicious!"
            sara_c "😲 I want some!!!"
            ilian_c "We don't even have a farm."
            sara_c "We have some dirt! I need strawberries!!! 😍😋🍓"
            natalia_c "Oh, my grandkids would love those. I'll take a few."
            kevin_c "I would like to plant some for additional vitamin C."
            him_c "Okay, I should have enough to everyone to have a few."
            thuc_c "I have strawberry plants, too. I'll sell them for the same price as [his_name]."
            nvl clear
            # TODO: currency check, add some income.
            "I was able to make a little extra money selling strawberry plants."
        "Leave them alone.":
            "I was too busy this year. I decided to just leave them there and deal with them later."

    return

# Strawberries 2 - mutant cancerous strawberries from solar flare
label strawberries2:
    scene fields with fade
    show him normal at center with dissolve
    "There were two things I liked about strawberries."
    "Obviously, the first was the delicious sweet fruit."
    "The second was that they were pretty low maintenance. I fertilized them and weeded them a little and that was it."
    "So it wasn't unusual that I hadn't checked on them for a month or two."
    "And when I finally did, I couldn't believe what I saw..."
    him surprised "What the-- where's all my strawberries?!"
    "The strawberry field was covered with strawberry plants, but where there should have been flowers, instead the strawberry plants had made thousands and thousands of runners."
    "So they were still strawberry plants, but there were hardly any flowers."
    "I looked closer to see if something was eating the flowers, but most of the plants had never made flowers at all."
    him concerned "Did I add too much nitrogen or something?"
    "I tested the soil. It showed the perfect balance of nutrients for strawberry plants."
    "I was stumped. Was everyone having this problem with strawberries?"
    nvl clear
    him_c "Hey, anyone else's strawberry plants not flowering?"
    thuc_c "Did you add too much nitrogen?"
    him_c "No, I already tested that. It's all fine. It's like the plants went crazy producing runners instead of flowers."
    thuc_c "Weird. Mine are fine."
    sara_c "Mine, too!"
    zaina_c "We haven't experienced any problems."
    him_c "Really? It's just mine?"
    if (year <= 20):
        lily_c "It is possible the plants mutated."
        sara_c "Like, X-Men strawberries?!"
        lily_c "Our frequent solar flares bombard the plants with more radioactive particles than on Earth. With most plants, a mutation in one plant might just mean its seeds are sterile, or it doesn't grow fruit."
        him_c "This is almost my whole field!"
        lily_c "Strawberries reproduce partly by cloning, so if the original plant had a mutation that caused it to not make flowers, it would affect that plant and all of its runners."
        him_c "Oh... and maybe the mutation also made it produce more runners, so it took over my whole field!"
        lily_c "Yes. That is my theory."
    else:
        zaina_c "Is it possible they mutated?"
        her_c "The solar flares definitely cause cells to mutate faster than on Earth."
        zaina_c "You know, we think the solar flares are partly responsible for the reduced productivity of crops on Talaam."
        him_c "And strawberries reproduce partly by cloning, so if one plant mutated to produce runners instead of flowers, it would reproduce very quickly."
    sara_c "I can't decide if that's creepy or cool."
    him_c "Mostly it's annoying, because it means my strawberry plants are messed up."

    nvl clear
    menu:
        "What should I do?"
        "Rip out the mutated strawberries." if (get_extra_work() > 0):
            "It was a huge pain, but I decided to rip out all the mutated strawberries.  I destroyed every plant that didn't have any flowers on it."
            "And the few strawberries that I did get, I planted instead of eating."
            # TODO: currency check, decrease profit
        "Till over the whole field.":
            "It would take forever to figure out which strawberry plants had mutated and which hadn't. I picked the strawberries that were there, ran over the whole thing with the tiller, and I was done."
            "Maybe next year I could plant strawberries from the seeds that I salvaged."

            $ enable_crop("strawberries")
            $ strawberries_index = get_crop_index("strawberries")
            $ crop_info[strawberries_index][MAXIMUM_INDEX] = 1
            # TODO: Test this...
            $ farm.crops.delete_crop("strawberries+")

    return
