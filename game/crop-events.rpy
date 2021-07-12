# Crop-specific work events

# Default crop event, if no other crop event can be found
label default_crop_event:
    scene fields with fade
    "The year passed by in a blur: -- tilling, planting, weeding, harvesting the same crops over and over -- the endless cycle of life on the farm."
    return

# Events that can happen if you have Terra work more than 70%
# Too much homework!
label terra_overwork1:
    scene fields with fade
    show tractor at midleft
    show him determined at midleft
    show kid determined at midright
    with dissolve

    $ random_crop = farm.crops.random_crop(include_animals = False)
    him happy "Ready to get going on the [random_crop], [kid_name]?"
    kid concerned "I guess..."
    him surprised "What's wrong?"
    kid angry "How am I supposed to do my homework if I'm always out here working with you?!"
    him annoyed "What are you talking about? You have plenty of time to do your homework!"
    kid sad "I've got a big project due tomorrow and I started it but it's going to take me hours and hours and I just don't know if I can do it!"
    menu:
        "What should I say?"
        "You'll have plenty of time after we finish here.":
            him determined "We're going to finish this and then you can work on your project."
            kid annoyed "I doubt it. If I get a bad grade it will be your fault."
            him angry "No, it will be your fault for not starting your project earlier when you had more time! It's not my fault you saved it all until the last minute!"
            kid angry "I didn't think you'd ask me to work every single day after school this whole week!"
            him annoyed "Well, there's a lot of work to do."
            kid yell "Fine! Let's just get it over with!"
            $ demanding += 1
            $ confident += 1
        "Work with me for half an hour and then go do homework.":
            him determined "Work with me for thirty minutes, and then you can have the rest of the day to do your project."
            kid angry "Thirty minutes?!"
            him annoyed "There will be several hours left after that. That should be plenty of time."
            kid annoyed "Fine..."
        "Go do your project and then come help me.":
            him concerned "Go work on your project. If you have time left, come out and help me."
            kid normal "Okay, thanks, dad."
            $ responsive += 1
        "You sound pretty stressed out about it.":
            him concerned "You sound really stressed out."
            kid annoyed "Uh, yeah! It's worth so many points and I haven't had time to do much of anything on it!"
            him normal "What do you think you should do?"
            kid concerned "...work on my homework."
            him explaining "Then go do that. As soon as you're done, though, I need your help out here."
            kid sad "Okay..."
            $ confident += 1
    $ demanding += 1
    $ terra_overwork_count += 1
    return

label terra_overwork2:
    scene fields with fade
    show tractor at midleft
    show him determined at midleft
    show kid determined at midright
    with dissolve

    $ random_crop = farm.crops.random_crop(include_animals = False)
    him determined "Today we need to compost the goat droppings."
    kid concerned "With the tractor, right?"
    him concerned "Well, we'll till some in right where it is, but we need to spread it out and make sure there's plenty of straw mixed in to turn it into compost."
    kid normal "Because otherwise it could burn the plants, right?"
    him happy "Right!"
    "Apparently she did listen to me, sometimes."
    "We worked together for several hours, spreading out the droppings and straw over the field. But she started slowing down until finally she just plopped down on her back."
    show kid at sitting with move
    kid sad "Can I be done?"
    "We still had at least another hour to go before we'd be done with this field."
    him concerned "You okay?"
    kid nervous "I'm tired, and my back hurts..."
    menu:
        "What should I say?"
        "Help with something else instead.":
            him surprised "Why don't you work on something else and I'll finish this up?"
            kid concerned "Like what?"
            him normal "You can start making dinner."
            kid annoyed "Is it potatoes and beans again?"
            him annoyed "Yeah, but we can have pickles, too."
            kid normal "Okay."
            show kid at standing with move
            hide kid with moveoutright
            "She left to make dinner and I finished up the job."
            "Hopefully she wouldn't burn anything."
            $ confident += 1
            $ kid_work_slider -= 2
        "Go home and rest.":
            him concerned "You go home and rest; I can finish up here."
            kid concerned "Thanks, dad."
            "My back was hurting, too, but I kept at it until the job was done."
            $ responsive += 1
            $ kid_work_slider -= 5
        "Let's take a little break.":
            him happy "Me too! Let's take a break."
            kid normal "Okay."
            show him at sitting with move
            "We found a clear patch and lay down next to each other, gazing up at the sky."
            "There was a cool breeze and the clouds skated and shifted across the sky."
            kid happy "Ha ha... that cloud looks like a crabird doing ballet..."
            him surprised "Which one?"
            kid normal "That one!"
            him explaining "I think it looks more like a dragon flying."
            kid concerned "Hmmm... maybe."
            show him at standing
            show kid at standing
            with move
            "After a few minutes, we got back to work and finished the job."
            $ responsive += 1
        "We're going to keep at it until we're done.":
            him determined "That's too bad. We're going to keep working here until we're done."
            kid angry "Can't I at least take a little break?!"
            him annoyed "Five minutes."
            "After five minutes, she went back to work, but she moved as slowly as possible and raked with limp arms that reminded me of a jellyfish."
            "Still, we finished the job."
            $ demanding += 1
            $ confident += 1
            $ kid_work_slider -= 2
    $ demanding += 1
    $ terra_overwork_count += 1
    return

label terra_overwork3:
    scene fields with fade
    show tractor at midleft
    show him determined at midleft
    show kid determined at midright
    with dissolve

    $ random_crop = farm.crops.random_crop(include_animals = False)
    # Never get to hang out with friends!
    "[kid_name] and I worked hard harvesting the [random_crop]. On Earth, there were machines for harvesting them, but we prioritized variety and adaptability over efficiency."
    "So we were gathering them all by hand and putting them in containers in the trailer of the tractor."
    "Harvest was my favorite part of farming; the part that made all the hard work worth it."
    "But it was still hard work..."
    show him normal at quarterleft
    show kid concerned at center
    with move
    him happy "Wow, look how big this one got!"
    kid sad "..."
    show him at left
    show kid at midleft
    with move
    him surprised "[kid_name]?"
    kid nervous "..."
    him concerned "[kid_name], what's wrong?"
    kid sad "Oh. Well, Oleg invited me to come over but I told him I had to come help you."
    him surprised "Oh."
    "On the one hand, I was proud of her work ethic. On the other hand, I knew she didn't get to hang out with friends as often as she liked..."
    menu:
        "What should I say?"
        "Go hang out with him. I got this.":
            him happy "You should go hang out with him! I can finish this."
            kid surprised "Are you sure?"
            him normal "Yeah! It's not often you both have your schedule free."
            kid happy "Okay, thanks, dad!"
            "She skipped away and I sighed. It was good to see her so happy, but... there were a lot of [random_crop] left to harvest."
            $ responsive += 1
            $ kid_work_slider -= 10
        "Let's finish up quick and then you can hang out.":
            him happy "Let's work really fast and then you'll have time to hang out!"
            kid surprised "You think so?"
            him normal "Yeah! Let's just do two more rows."
            $ responsive += 1
            $ demanding += 1
            $ kid_work_slider -= 2
            "We finished up the two rows, working as fast as possible. By the time she got over there, it would be almost time to come home, but I still thought it was worth it."
        "You made the right choice.":
            him determined "You made the right choice, [kid_name]."
            kid annoyed "Hmph."
            $ demanding += 1
            "We worked in silence, trudging along and picking up every last one of the [random_crop]."
    $ demanding += 1
    $ terra_overwork_count += 1
    return

    # This is your job
label terra_overwork4:
    scene fields with fade
    show tractor at midleft
    show him determined at midleft
    show kid determined at midright
    with dissolve

    $ random_crop = farm.crops.random_crop(include_animals = False)

    "You don't always hear much about the work on a field after the harvest is done."
    "We had to till in the stubble, and then [kid_name] and I had a lot of maintenance to do on the equipment."
    "Every farm machine had to be cleaned and oiled; and in order to that we had to take a lot of pieces apart."
    "I was trying to teach [kid_name] about how to change the oil in the tiller."
    him explaining "Then we put the old oil in this container for recycling."
    kid angry "Why am I always doing your job?!"
    him surprised "What?"
    kid annoyed "Taking care of these vehicles is {b}your{/b} job, right? So why are you making {b}me{/b} do it?"
    him annoyed "It's not 'my' job, it's just a job that needs to get done. That's what we do."
    kid angry "I spend so much time helping with your work that I don't have any time to do my own!"
    him angry "What work?! You're a kid!"
    if ((year > 27) and (not family27_no_work)):
        kid annoyed "I have my delivery job. People depend on me."
    else:
        kid annoyed "I have work for school, and for mom, and there's things I want to do!"
    him annoyed "This is more important."
    kid nervous "More important to you..."
    "I felt like yelling, but I kept my mouth shut. It was true that I asked her to work a lot, but that's just part of being a farm kid."
    kid sad "I just feel like I never have time for anything."
    menu:
        "What should I say?"
        "That's how it is being a farm kid.":
            him doubt "Sorry, that's just how it is when you're a farm kid."
            kid angry "I didn't ask to be a farm kid!"
            him determined "But you are."
            $ demanding += 1
        "I need your help." if (get_extra_work() <= 1):
            him concerned "I'm sorry, [kid_name], but there's a lot of work that needs to be done and you're making it all possible."
            kid surprised "What do you mean?"
            him surprised "I couldn't do all this without you. We wouldn't have all this great food, all these credits, everything we enjoy... you make it all possible."
            kid concerned "You mean... you need me?"
            him normal "I sure do."
            kid annoyed "Well... I'd rather you didn't need me so much."
            him sad "I know... I know."
            $ demanding += 1
        "I'll try and let you have more time in the future.":
            him concerned "I'll see if I can schedule a bit more free time for you in the future."
            kid nervous "Yeah... sure."
            $ responsive += 1
        "Let's look at your schedule together and figure this out.":
            him concerned "Hmmm. Why don't you write out the things that you want to do and how much time they take, and we can make a schedule together?"
            kid nervous "I guess..."
            $ responsive += 1
    "I remember working really hard when I was a kid... but I also remember having time to ride my bike to the creek and splash around with friends or climb trees or work on our always in-progress treehouse..."
    "Being a teenager was pretty busy, though, since I had farm work and school work."
    if (get_extra_work() < 0):
        "This farm took so much work, I couldn't imagine how I could do it all without [kid_name]'s help."
    else:
        "Maybe I didn't need to make [kid_name] work quite so much."

    $ demanding += 1
    $ terra_overwork_count += 1
    return

# GARLIC1 Terra has no clue about its anti-vampiric properties.
label garlic1:
    scene farm_interior with fade
    show him normal at midright with dissolve
    him happy "Dinner's ready!"
    show her normal at center
    show kid normal at midleft
    show bro normal at quarterleft
    with moveinleft
    kid annoyed "Yuck, what is that smell?!"
    him surprised "Smell? I don't smell anything weird... I'm just making dinner."
    kid concerned "It smells like... rotten eggs or something! What are you cooking?!"
    him normal "Just some garlic mashed potatoes."
    her happy "Garlic mashed potatoes?! Wow!"
    if (bro_age > TODDLER_MAX):
        bro sad "Mashed potatoes are my favorite! But those smell bad..."
    kid angry "I'm not eating any!"
    him angry "Hey, you haven't even tried it yet."
    kid annoyed "I don't need to try it! It smells disgusting!"
    menu:
        "What should I do?"
        "Make her try a bite.":
            him annoyed "You need to try at least one bite. Then you can decide if you like it or not."
            kid determined "I already know I'll hate it."
            her concerned "At least try to have a good attitude!"
            "She wrinkled her nose and lifted a tiny spoonful to her mouth."
            "She gulped it down and followed it with a huge glass of water."
            kid annoyed "I don't like it."
            him determined "Surprise, surprise."
        "Don't make her.":
            him determined "You don't have to eat it. All the more for me."
            her determined "And me! Garlic mashed potatoes are my favorite!"
            bro surprised "Can I have some more?"
            him happy "You like them? Sure! I made lots!"
    kid surprised "Why would someone eat something that smells like that?"
    her concerned "Garlic actually tastes really good, and it's has a lot of health benefits."
    him normal "And it keeps vampires away."
    kid annoyed "Vampires?"
    him happy "That's what legends say, anyway!"
    kid determined "That makes absolutely no sense."
    her normal "Well, the legends might be based on a real disease, porphyria, that causes paleness, light sensitivity, erosion of lips and gums... and a sensitivity to garlic."
    kid normal "Earth sure has some weird ideas."
    him happy "You have some weird ideas, like 'garlic is yucky'."
    kid annoyed "Hmph."
    return


# WHEAT1: Wheat is yummy!
label wheat1:
    scene farm_interior with fade
    "Every time I paid for Brennan's wheat seeds it left a bad taste in my mouth."
    "I tried to counteract it by making plenty of bread, biscuits, dumplings, pizza, and noodles."
    "We didn't have a lot of sugar, so cakes and cookies were out, but whenever I got fresh fruit I would make a pie."
    show him normal at midright
    show her normal at midleft
    show kid normal at center
    show bro normal at quarterleft
    with dissolve
    if ("strawberries+" in farm.crops):
        her sleeping "Mmmmm. There's nothing better than strawberry pie!"
        him happy "What do you think of this recipe? Do you like the strawberries better cooked in like this?"
        her happy "I like them both!"
        kid surprised "Are you putting cheese on your pie?! Weird!"
        him determined "I'm pretending it's ice cream."
        kid nervous "You put ice cream on pie?! I thought it went in cones or something."
        her normal "There's no wrong way to eat ice cream."
        him flirting "Except for that weird bacon-garlic ice cream we had that one time."
        her annoyed "Ohhh, that was awful! I can't believe you tried that."
        him concerned "It turns out there's some things even bacon can't improve."
        kid annoyed "If bacon's so good, how come you never make it?"
        him sad "We didn't bring pigs to Talaam... I think if I had to do it over again, that would be the thing I would bring."
        her annoyed "We're probably healthier without it."

    elif ("plums+" in farm.crops):
        her surprised "Wow, you made plum pie again? Isn't that a lot of work?"
        him happy "Not really. I didn't peel the plums or anything; just took out the pits and tossed them in a crust."
        bro nervous "Do I have to eat the crust?"
        kid determined "If you don't eat it, I will!"

    elif (("squash" in farm.crops) and ("honey" in farm.crops)):
        "Since I didn't grow many fruits, I made a squash pie with some honey and whatever spices I could round up."
        her surprised "Pumpkin pie?! How in the world..."
        him happy "It's actually squash pie, but hopefully it tastes a little like pumpkin!"
        kid surprised "Squash and pumpkin both sound like weird pies."
        him normal "You can't decide if it's weird until you try it."
        her determined "Where'd you find the spices?"
        him concerned "Pavel's spice garden. He didn't have everything, but he at least had cinnamon and ginger."
        "I took a bite. If I used my imagination, it almost tasted like pumpkin pie..."
        bro concerned "This is weird."
        kid concerned "It's not bad... could be sweeter, though."
        her happy "If you don't want yours, I'll eat it! This is delicious!"
        him normal "I'm glad someone likes it."
    else:
        "And when I couldn't get fresh fruit I would make a savory pie."
        if ("tomatoes" in farm.crops):
            "Tomatoes and goat cheese was my favorite so far."
        else:
            "A little meat, lots of vegetables, and a savory, creamy gravy all baked inside a flaky pie crust."
        her sleeping "Mmmmm... great dinner, [his_name]."
        bro concerned "Do we have any bread?"
        him annoyed "No. Just this delicious pie."
        kid surprised "It's not bad."
    return


# CORN1: Corn was made sterile by solar flares
label corn1:
    scene fields with fade
    show him normal at center with dissolve
    "When I went to go check on the corn I planted, I noticed that only about a third of the stalks grew up."
    him surprised "Why didn't the others germinate?"
    "It was normal for a few seeds not to germinate, but not this many. I had to find out what the problem was."
    "I gathered some of the seeds that hadn't germinated, and some that had, and looked at them closely."
    him determined "The structure looks fine..."
    "The weather had been fine, the soil tested fine, and the seeds looked fine... I was stumped."
    "I decided to get a lab analysis."
    scene lab with fade
    show him normal at midleft with dissolve
    if (year < LILY_DIES_YEAR):
        show lily normal at midright with moveinright
        lily "After close analysis, I can tell you that these seeds are sterile."
        him annoyed "Obviously! But {b}why{/b} are they sterile?!"
        lily angry "Their DNA has mutated. Mutations happen naturally even on Earth. But the radiation from solar flares causes mutations much more frequently."
    else:
        "Miranda ran some tests on them, and concluded that the DNA had mutated to the point that the seeds were sterile."
        "We concluded it was probably the result of solar flares."

    $ modify_credits(-0.6 * farm.crops.count("corn") * get_credits_from_name("corn"))
    "There wasn't really anything I could do. I just would have to work with having less corn than I thought this year."
    return

# CORN2: How to process corn
label corn2:
    scene fields with fade
    "There are tons of different types of corn, but on Talaam we mostly grew a variety of hard heirloom corn."
    "It's not so good for eating fresh off the cob because it's not sweet at all."
    "But it grinds up into a nice flour, and you can even pop it a little bit."
    "It stores easily, too -- after harvesting the ears of corn, I pulled the silk and the husks back to expose the colorful kernels."
    "And then I hung them up to dry for a few months."
    "When they were all dry, I ran them through the corn sheller. Then the kernels were ready to pop, grind, or store for later."
    "It would take more work, but I could treat the corn with lime in a process called nixtamalization. This allows more B vitamins to be extracted from the corn, kills fungi, and makes it easier to grind."
    "It would be vital if corn were our main staple, but we have such a variety of foods here we probably don't need to."
    if (get_extra_work() <= 0):
        "Too bad I didn't have time for that this round. Maybe next time I would treat it."
    else:
        menu:
            "What should I do?"
            "Treat the corn with lime.":
                "I decided the extra nutrition was worth it. If I'm going to all the trouble of growing food, I want it to be as nutritious as possible."
                "I soaked the kernels in an alkaline solution and then let them dry again."
                "Now they could be used for some of my favorite foods - tortillas, pozole, and chips!"
                if ((farm.crops.count("tomatoes") > 0) and (farm.crops.count("peppers") > 0)):
                    if (farm.crops.count("onions") > 0):
                        "And with the peppers, onions, and tomatoes I grew, I could make salsa to go with them."
                    else:
                        "And with the peppers and tomatoes I grew, I could make salsa to go with them."
                    if (farm.crops.count("garlic") > 0):
                        "I added some garlic, too, for a nice zing."
                    scene farm_interior with fade
                    show him normal at midleft
                    show her normal at midright
                    show kid normal at center
                    if (bro_years > 0):
                        show bro normal at quarterright
                    her surprised "Chips and salsa?! Wonderful!"
                    kid happy "I like chips, too!"
                    him happy "Eat up!"

            "Don't treat it.":
                "I decided not to treat it. That meant there were some things I couldn't make very well, but it would make better popcorn."
                scene farm_interior with fade
                show him normal at midleft
                show her normal at midright
                show kid normal at center
                if (bro_years > 0):
                    show bro normal at quarterright
                kid surprised "What is this?"
                her happy "Popcorn!!"
                "The kernels were small and less airy than normal Earth popcorn, but [kid_name] wouldn't know the difference."
                him happy "Eat up!"
                kid surprised "It's... puffy? And salty!"
                her sleeping "Delicious..."
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
    $ carrots_fallow = False
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
            $ carrots_fallow = True
            $ crop_temporarily_disabled = "carrots"
        "Who cares, they taste the same.":
            "I didn't have time to worry about oddly-shaped carrots."
            "I just chopped them up and cooked them and then nobody even noticed."
    return

# CARROTS2 - great carrots if fallow, otherwise find pests.
label carrots2:
    play sound "sfx/rain.ogg" loop
    scene fields with fade
    show rain
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
            kid nervous "It looks like eyeballs."
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
        $ modify_credits(-farm.crops.count("carrots") * get_credits_from_name("carrots"))
        "I finally figured out there were some pests eating them. By that time, it was too late to fix the problem. So we wouldn't have any carrots this year."
        menu:
            "What should I do next year?"
            "Treat the carrots with pesticide" if (get_extra_work() >= 0):
                "I decided to treat next year's carrots with pesticide. It'd be more work, but I didn't want to give up carrots."
            "Don't plant carrots next year and let the pests die off.":
                "The easiest thing to do was just not plant carrots for a year. Then the pests would die."
                $ crop_temporarily_disabled = "carrots"
    stop sound fadeout 2.0
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
            show her normal coat at midright with dissolve
            show him normal at midleft with moveinleft
            him surprised "Hey, Dr. [her_name], is it possible to eat too many carrots?"
            her annoyed coat "Are you talking about [kid_name]'s orange hands?"
            him concerned "Yeah... is that bad?"
            her concerned coat "No, not on its own. It's only bad if she's not getting other nutrients she needs because she's just eating carrots."
            him normal "Okay, good to know."
            her annoyed coat "Don't you think I would have said something if there was something wrong?!"
            him surprised "Well, I wasn't sure you noticed."
            her determined coat "Of course I noticed. And if you're not careful, the same thing will happen to you."
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

    scene farm_interior with fade
    image him orange = im.MatrixColor("images/sprites/him/him happy.png",  im.matrix.tint(0.9, 0.7, 0.3))
    show him orange at center
    with dissolve

    him "I'm never going to stop eating these delicious carrots!!!"
    return

# POTATOES 1 - Solanine
label potatoes1:
    scene fields with fade
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
            sara_c "Hey, is it OK to eat green potatoes? Or is it just the sprouts you're not supposed to eat? {emoji=worried}"
            natalia_c "As long as they taste good they're OK."
            him_c "You can cut off the green parts if you're worried about it."
            sara_c "Okay, they just looked a little weird."
            nvl clear
        "Don't use any that have any green.":
            "I decided not to risk poisoning myself or others."
            $ modify_credits(-0.2 * farm.crops.count("potatoes") * get_credits_from_name("potatoes"))
            "But even though they weren't good to eat, they would be fine for planting."
            $ colonists += 1
        "Warn people about the risks of solanine.":
            nvl clear
            him_c "Just wanted to give everyone a heads up on potatoes."
            him_c "If they're green, you should peel them and get rid of any green parts."
            him_c "And don't eat them if they taste bad."
            him_c "Look up solanine poisoning if you want more information."
            sara_c "Why would we risk any sort of poisoning?! {emoji=scream} {emoji=yuck}"
            him_c "They're probably fine!"
            natalia_c "Even supermarket potatoes sometimes had some green on them. It's not a big deal."
            julia_c "Unless you're wrong and our insides twist in knots and we start hallucinating."
            natalia_c "Well, I'll eat them if you won't."
            ilian_c "I'll discount them, but anyone taking them from the storehouse does so at their own risk."
            nvl clear
            $ modify_credits(-0.1 * farm.crops.count("potatoes") * get_credits_from_name("potatoes"))
            "Wow, I didn't think that would be such a big deal."
            $ colonists -= 1
    return

# POTATOES2 - what to do with them
label potatoes2:
    scene fields with fade
    "I grew a lot of potatoes. In some ways, they were the perfect crop. They were protected from a lot of pests and weather since they were undeground."
    "They gave a high yield, and were a calorie- and nutrient-dense food."
    "But that also meant we ate them a lot."
    scene farm_interior with fade
    show him normal at center with dissolve
    "I wanted to do something different with them for dinner tonight..."

    menu:
        "What should I do with the potatoes?"
        "Put them in a chowder":
            "There's nothing like a nice, hearty chowder. Goat's milk, onions, some grass crab meat, herbs, and, of course, lots of potatoes."
            show her surprised at midleft with moveinleft
            her surprised "Mmmm, that smells so good! Like clam chowder!"
            him concerned "If only I had some bacon..."
            her flirting "How about some smoked crabird?"
            him normal "That's a start!"

        "Make potato chips":
            "I missed the satisfying crunch of potato chips. I really wanted to fry some up."
            "But first I'd need a lot of oil..."
            "More than the goat butter we had or the amount I pressed from squash seeds with our small oil press."
            scene storeroom with fade
            show ilian normal at midright with dissolve
            show him normal at midleft with moveinleft
            him surprised "How much for some oil?"
            ilian "How much do you need?"
            him determined "About a liter."
            "He told me and I cringed, but I felt I had to have potato chips!"
            "Then an idea struck me."
            him pout "How much would you pay me for potato chips?"
            ilian angry "The storehouse doesn't take luxury goods like that. You'll have to ask around."
            him concerned "Oh."
            ilian happy "But I, personally, would pay very well for such chips."
            "With the amounts he told me, I did some quick calculations in my head."
            him normal "Give me 10 liters of oil."
            ilian normal "Very well. Just make sure you bring some of those chips by here first, all right?"
            scene farm_interior with fade
            show him normal at midleft with moveinleft
            if (year >= 7):
                show kid normal at midright with moveinright
                kid surprised "Is dinner ready yet?"
                him normal "No, but I'm making a special treat. You make us a salad, and I'm going to make a wonderful thing called potato chips."
                kid concerned "What, like wood chips? That sounds gross."
                him happy "Oh no, much, much better."
                kid nervous "Okay..."
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
            her flirting "You're going to be in the kitchen for a long time."
            him flirting "I could use some help..."
            her determined "I'll take care of everything else around the house; you just keep cooking potato chips!"
            $ modify_credits(200)
            "In the end we managed to make a little extra with the chips, though it was so much work I wasn't sure I'd do it all the time."

        "Make potato salad":
            "Potato salad was one of my favorite summer dishes back on Earth. I'd made it before and it wasn't too hard."
            "But there were a lot of things the storehouse didn't have here."
            scene farm_interior with fade
            show him normal at center with dissolve
            him annoyed "Mayonnaise, mustard, pickles, celery -- if I leave all those things out is it even still potato salad?!"
            "I'd have to make my own recipe."
            him concerned "I could use goat milk for creaminess, a little vinegar for a nice tang, and I do have some other herbs and spices..."
            him surprised "I have some homemade pickles I could chop up and put in there, and I have one egg I could boil..."
            "The end result was sort of a potato salad, though it tasted nothing like the comfort food I remembered. I'd have to call it something else."
            show her normal at midleft with moveinleft
            show him normal at midright with move
            her surprised "Is that... dinner?"
            him normal "Yes, it's potato... uh, Cold Potato Mixup!"
            her flirting "You just made that up, didn't you?"
            him happy "Yeah! Want to try it with me?"
            her concerned "I am hungry..."
            him concerned "..."
            her surprised "..."
            him surprised "What do you think?"
            her concerned "It's... a different way to eat potatoes."
            him determined "It's not bad."
            her normal "No, it's kind of good... I think it needs some more salt, though."
            him flirting "More salt, coming right up!"
            her happy "It looks like a lot of work..."
            him concerned "Yeah, I kind of spent all afternoon on it."
            her concerned "It kind of reminds me of potato salad..."
            him surprised "Really?"
            her normal "Yeah... just a little."
            "That was good enough for me."

    return

# POTATOES3 - Rotten potatoes
label potatoes3:
    play sound "sfx/rain.ogg" loop
    scene fields with fade
    show rain
    "I'll never forget the time it rained..."
    "And rained."
    "And rained."
    "It rained nonstop for two whole weeks."
    "Some rain is good from crops. It meant I didn't have to manually irrigate them."
    "But this much was terrible for my potatoes."
    show him concerned at center behind rain with dissolve
    him "They've all rotted."
    "Instead of beautiful, firm, starchy potatoes, all I had were mushy brown foul-smelling lumps."
    "There was nothing I could do to save them."
    "But I had to dig them out so they wouldn't contaminate the field."
    "At least I could use them for compost for other plants."
    show him concerned at quarterleft with move
    "But every hour spent in the mud fishing them out felt oppresive and pointless."
    show him pout at center with move
    "I spent all season on them, and what did I have to show for it?"
    "Just foul-smelling mush."
    show him sad sweat at quarterright with move
    "I worked and worked all day, all afternoon, and into the evening."
    show night_overlay
    show him pout at midleft with move
    "I was so frustrated and mad that I just wanted to get it all done and forget about it."
    show him sad at midright with move
    "I couldn't see very well in the moonlight but I kept ripping up the plants and loading the rotten potatoes onto the trailer."
    show him annoyed sweat with dissolve
    "I slipped and fell in the mud right as [her_name] came walking up."
    show her concerned at midleft behind rain
    show kid normal at center behind rain
    if (bro_years > 0):
        show bro normal at midleft behind rain
    with moveinleft
    her "Hey, we missed you at dinner. Everything okay?"
    menu:
        "What should I say?"
        "Fine.":
            him pout "Fine."
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
            him annoyed "Nobody's eating them; they're all bad."

    her sad "Oh, honey, I'm sorry..."
    if (marriage_strength >= 2):
        her surprised "Want some help?"
        him concerned "No, no, you've been working all day, too, I can't ask you to do that."
        her sad "Are you sure?"
    him sad "Yeah, I should probably quit for today anyway."
    her normal "We saved you some dinner..."
    $ modify_credits(-farm.crops.count("potatoes") * get_credits_from_name("potatoes"))
    him determined "As long as it's not potatoes."

    stop sound fadeout 2.0
    if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        "There was one good thing that came out of all this, though."
        "Since I didn't have to harvest potatoes, I did have some time to prepare new fields for crops."
        $ modify_farm_size(2)
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
            "What should I do about the squash?"
            "Pollinate by hand" if (get_extra_work() >= 0):
                him determined "I guess I'm Cupid's little helper today..."
                "I took a paintbrush and dabbed the pollen from the male flowers and then brushed it on the female flowers."
                "Since there were several flowers on each plant, and a whole field full of plants, it took quite a while."
                $ modify_credits(0.5*get_credits_from_name("squash"))
                "But it wasn't difficult, and it did increase our squash yield dramatically."
            "Ask to borrow some bees" if (year > 10):
                "I thought I remembered someone saying something about bees, but I couldn't remember who."
                nvl clear
                him_c "Hey, anyone have extra bees? My squash needs pollination!"
                natalia_c "We got some from Kevin."
                julia_c "Send your kids to pollinate the plants by hand. The work will be good for them."
                kevin_c "I do have bees, but not extra."
                nvl clear
                "Maybe if I talked to Kevin in person we could work something out."
                scene farm_exterior flip with fade
                show kevin normal at midright with dissolve
                show him normal at midleft with moveinleft
                him happy "Hey, Kevin! How's it going?"
                kevin happy "Satisfactorily."
                him normal "Good, good...hey, about those bees..."
                kevin sad "I apologize, but I do not have extra bees at this time."
                him concerned "Could I maybe, like, borrow them, just for a few weeks?"
                kevin normal "I could rent them to you."
                menu:
                    "What should I say?"
                    "Could we trade?":
                        him surprised "Could we trade? Maybe for squash?"
                        kevin sad "Squash and goat's milk, in these quantities."
                        $ modify_credits(-50)
                        him normal "Looks reasonable. It's a deal."
                    "Okay, how about for 50?":
                        him normal "Okay, how about 50?"
                        kevin sad "That is insufficient. I propose 80."
                        him surprised "Maybe 60?"
                        kevin normal "75 is the lowest I will consider."
                        $ modify_credits(-75)
                        him normal "All right, 75 it is."
                    "I'll pay you 100.":
                        him normal "I'll pay you 100 for them."
                        kevin sad "That is acceptable."
                        $ modify_credits(-100)
                        him "It's a deal."
                    "Never mind, I don't need bees.":
                        kevin sad "Very well, the choice is yours."
                        jump squash1_forget_it
                kevin happy "Good. I will write up a contract."
                him annoyed "A contract, huh?"
                kevin normal "Yes. That way the terms are clear and unarguable by both sides."
                "I couldn't really argue with that."
                "I skimmed his legalese and it looked reasonable. For the consideration of the use of his bees, blah blah blah, the undersigned hereby agree to blah blah blah."
                "I transported his hive of bees at night, when most of them were sleeping, and in the morning they woke up to a new home."
                "They seemed to adjust pretty well, and went right for the squash blossoms."
                "I was kind of sad to give them back."
                $ modify_credits(0.3 * farm.crops.count("squash") * get_credits_from_name("squash"))
                "We harvested a lot of squash that season!"

            "Forget the squash for this season":
                label squash1_forget_it:
                    "I didn't have time to baby the plants. They'd have to survive on their own."
                    $ modify_credits(-0.4 * farm.crops.count("squash") * get_credits_from_name("squash"))
                    "Some of them produced fruit, but most didn't. What a waste..."
    return

# SQUASH2 - squash bugs
label squash2:
    play music problems
    play sound "sfx/rain.ogg" loop
    scene fields with fade
    show rain
    show him normal at center behind rain with dissolve
    "I went to weed the squash plants, but as I was weeding, I noticed something."
    him surprised "These plants are a bit smaller than they should be...and some of the leaves have yellow spots on them."
    him angry "What the- squash bugs! I thought we left all those behind on Earth!"
    "Squash bugs were probably my least favorite insect of all time. They reproduced like crazy and devoured entire squash plants, leaves, flowers, fruits, and all."
    "They must have been transported on one of the shuttles -- maybe in some wood or fruit."
    "But I didn't have time to waste on being furious. I had to get rid of them!"
    menu:
        "What should I do about squash bugs?"
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
            else:
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
            $ modify_credits(-0.75 * farm.crops.count("squash") * get_credits_from_name("squash"))
            "But that meant I only havested one fourth of the squash I had planned on."
        "Try and get the new folks to fix the problem. They started it, after all!":
            $ squash2_method = "passthebuck"
            nvl clear
            him_c "Alright, who brought squash bugs to Talaam?!"
            if (year < MARTIN_DIES_YEAR):
                martin_c "Not squash bugs!"
            else:
                natalia_c "Oh no, not squash bugs!"
            sara_c "What are squash bugs????? {emoji=surprised}"
            natalia_c "A squash farmer's worst nightmare. I haven't seen any here yet, but if they're anywhere on the planet I'm sure they'll find all the squash plants."
            him_c "They found all of mine. But whoever brought them should be responsible for getting rid of them!"
            if (year < NAOMI_DIES_YEAR):
                naomi_c "Do you think someone brought them here on purpose?"
            else:
                sara_c "You're not saying someone brought them here on purpose?! {emoji=shocked}"
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
            sara_c "Oleg and I can come help you on Monday morning. We don't know anything about squash but we can kill bugs! {emoji=mad} {emoji=bugs} {emoji=death}"
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
    stop sound fadeout 2.0
    return

# SQUASH 3 - consequences of squash bug method.
label squash3:
    scene fields with fade
    "I was curious to see how this next batch of squash would fare; given the trouble I had with squash bugs last time."
    if (squash2_method == "ignore"):
        $ modify_credits(-farm.crops.count("squash") * get_credits_from_name("squash"))
        "I didn't think it was possible, but there were even more squash bugs this year. The plants didn't even have a chance to set any fruit at all before they were completely devoured."
        "I couldn't plant squash again until at least a year had passed. Maybe if they didn't have any squash to eat, they'd all die out."
        $ crop_temporarily_disabled = "squash"
    else:
        "I checked the seedlings every day for signs of squash bugs. Nothing."
        "Was it possible I had exterminated all the squash bugs on the planet??"
        "No, I needed to stay vigilant!"
        "Sure enough, as the flowers bloomed and squash started to grow, I noticed one plant looking a little less healthy than the rest."
        "There were squash bugs on it!"
        "It was much easier to kill them all when they were all one plant. I scrutinized that section every day and got rid of all the bugs and eggs I saw."
        $ modify_credits(0.5 * farm.crops.count("squash") * get_credits_from_name("squash"))
        "The result was a bountiful squash harvest, even more than I had projected."
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
    scene barn with fade
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
    him angry "Hey!"
    "One of the male goats was peeing all over himself, and a bunch of it got on me."
    "That was where the bad smell was coming from."
    "Apparently that was how he was trying to attract a mate."
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
    him_c "..."
    thuc_c "...ha ha, sorry!"
    nvl clear

    "So it sounded like I needed to separate or neuter the bucks. Or butcher them."

    menu:
        "What should I do about the goats?"
        "Smuggle some to Pete" if (year >14): #only if Pete and his group have left
            "I felt bad for Pete. Maybe he would like some goats."
            "I couldn't send him a message; radio communications weren't private."
            "I'd have to just go over there."
            if (year >= PETE_LEAVES_CAVES_YEAR):
                scene shack with fade
            else:
                scene cave with fade
            show pete normal at midright with dissolve
            show him normal at midleft with moveinleft
            if mavericks_strong():
                pete happy "Hey there, [his_name]. Good to see ya."
            else:
                pete angry "What do {b}you{/b} want?"
            him normal "Hey, Pete! I just wondered if you wanted some goats. The bucks are getting ornery and I really don't want to have two herds."
            pete normal "I got plenty of cows to take care of."
            him surprised "Really? Goats aren't much trouble. They just need a fence and a place to sleep. Or you could just eat them."
            pete happy "Well... actually, it might be good project for Travis. But I'd need a doe, too."
            him "Sure, I can spare one. She's almost full grown."
            pete normal "Alrighty then. I'll have some beef to trade you for, alright?"
            him "Sounds good. Later, Pete."
            $ mavericks += 1
        "Send the meat to the storehouse":
            "I didn't want to have two goat herds. That would just be too much work."
            "So I slaughtered them, cut up the meat, and sent it to the storehouse."
            "While I was there, I was able to pickup a bunch of foods my family had been craving."
            scene farm_interior with fade
            show her normal at midright
            show kid normal at center
            with dissolve
            show him normal at midleft with moveinleft
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
            if (crop_enabled("wheat")):
                "With the wheat I grew I could make a crust for pizza."
            else:
                "I sold two links of it at the storehouse and had enough money to buy wheat so we could make pizza."
            scene farm_interior with fade
            show him happy at midright with dissolve
            show kid normal at center
            show her normal at midleft
            with moveinleft
            him happy "Dinner's ready!"
            her surprised "Is this a... pepperoni pizza?! Ohhh, [his_name]!"
            if (year >= 7):
                kid surprised "What's pepponi pitsa?"
                him determined "Only the best food ever invented."
                her concerned "It might taste weird to her, though."
                him happy "That's fine; I'll eat hers!"
                kid normal "I want to try it!"
            "We each took a slice. The goat cheese didn't really pull into long strings like mozzarella, but it had melted into nice medallions on the top."
            "The whole wheat crust was denser and less puffy than traditional pizza, too."
            "But after one bite, I was in heaven. The pizza was just slightly crunchy, with tangy tomato sauce, creamy cheese, and, best of all, big rounds of pepperoni that were just the slightest bit cripsy."
            kid surprised "Hot!"
            her sleeping "Mmmm."
            him sleeping "Mmmmmmm."
            her happy "Wow. I haven't had pizza in so long! I'm glad your pepperoni turned out."
            him sleeping "Ummm."
            "I couldn't even talk. I was too entranced by the flavors, the textures, the memories..."
            "Pizza after a soccer game, pizza at a video game party with friends, pizza with [her_name] on a rainy night in, feeding each other and laughing and cuddling on the couch..."
            her surprised "Are... are you crying?"
            him sad "This... is the best pizza I've ever had. It tastes like... Earth."
            if (year >= 7):
                kid normal "Earth is spicy?"
                her concerned "Spicy and sweet and creamy and saucy and complicated."
                him flirting "Sounds like someone else I know."
                her flirting "Shut up and eat your pizza."
                if (year >= 20):
                    kid annoyed "Dad, that was so bad."
                    him surprised "Was it so bad it's... cheesy?"
                    kid normal "Ohhh, dad!"

        "Allocate more land for goats" if (get_extra_work() >= 0):
            "If we needed two herds, then I'd make two herds. It wasn't too much work to make another goat pen and feeding area."
            "And it would be better to control the goats' mating, so we didn't have goats getting pregnant too young or goat pee smell getting on the milk or things like that."
            "I'm sure we'd eat some of these goats eventually, but for now I just wanted to grow the herd."
            $ goats_index = get_crop_index("goats")
            $ crop_info[goats_index][MAXIMUM_INDEX] += 1
            # goats take up another square now.
    return

# GOATS 3 - escaping goats
label goats3:
    scene barn with fade
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
    show julia normal at quarterright
    show goat at midright
    with dissolve
    show him determined at midleft behind goat with moveinleft
    if (year > 7):
        show kid concerned at quarterleft with moveinleft
    "Sure, enough, Julia was there scowling and flapping a dishtowel, trying to drive the goats away."
    show julia at midright with move
    show goat at center with move
    "They'd skitter a few steps away, then go right back to nibbling on some sweet potato vines."
    julia angry "There you are!"
    him concerned "Sorry about the goats. I just noticed they got out."
    julia normal "Well, they've been here all morning. I'm not sure my poor sweet potatoes will recover."
    him annoyed "I-"
    julia angry "I tried to reach you on the radio, but you didn't answer."
    "She looked pointedly at my radio on my belt -- it was turned off. I sometimes 'forgot' to turn on my radio -- the truth is, I liked the peace and quiet."
    him blush "Must have forgotten to turn it on. Well, I'll just get these goats out of your way."
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
            show julia normal at midright with dissolve
            show him determined at midleft with moveinleft
            him determined "I just wanted to apologize for my goats getting into your sweet potatoes. Here's some [random_crop] for you."
            julia angry "Hmph. It's a start, anyway."
            him surprised "A start?!"
            julia happy "I'll let you know in a week if the plants recover or not. If not, we'll need twice this amount to make up for it."
            "Sometimes, I couldn't believe this woman. How Thuc could stand being married to her, I had no idea."
            him annoyed "I guess we'll see then."
            julia normal "Yes, let's wait and see."
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
            show kid concerned at midright with moveinright
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
                    him annoyed "That's not possible. One of us must not have closed it all the way, and I know it wasn't me, so it had to be you. Time to get back to work."
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
    scene fields with fade
    $ tomatoes1_action = "none"
    "There's nothing like fresh, juicy tomatoes straight from the vine. The sweet juice, the way the seeds squirt all over when you bite into them, their perfect roundness..."
    "But the best thing about growing tomatoes on Talaam was that there were no hornworms!"
    "As a kid I spent hours hunting those giant green caterpillars. I earned a bounty for every hornworm I destroyed."
    "In fact, it was a little bit sad that [kid_name] wouldn't have that opportunity..."
    "...but not too sad."
    "This year, my tomatoes were doing pretty well, but a lot of them had a sunken, mushy area on the bottom."
    menu:
        "What should I do about the tomatoes?"
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
    scene fields with fade
    $ tomatoes2_action = "none"
    if (tomatoes1_action == "research"):
        "The tomatoes looked much better this year!"
        menu:
            "Now, I needed to choose which fruits to save seeds from for planting next year."
            "First tomatoes":
                $ tomatoes2_action = "early harvest"
                "I wanted the tomatoes to ripen as quickly as possible. Less time from seed to harvest is more efficient!"
            "Biggest tomatoes":
                $ tomatoes2_action = "size"
                "I wanted the biggest tomatoes. I remembered submitting my largest tomato to the county fair as a kid. It had seemed so enormous... but when I saw the tomato that beat it, I was blown away."
                "I wanted to see how big Talaam tomatoes could get."
            "Sweetest tomatoes":
                $ tomatoes2_action = "sweetness"
                "Sweet tomatoes were the best for eating. I can't stand mealy or bland tomatoes."

        if ((get_work_available() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
            "After harvesting tomatoes and their seeds, I had enough extra time to get another field ready for planting crops on next year."
            $ modify_farm_size(1)
    else:
        "The tomatoes had the same rotten bottom area as last time, only now it's even worse!"
        "I did some research and found out that usually means there's too much nitrogen in the soil and not enough calcium."
        if (tomatoes1_action == "fertilize"):
            "So adding more fertilizer just made it worse."
        $ modify_credits(-0.6 * farm.crops.count("tomatoes") * get_credits_from_name("tomatoes"))
        "Most of my tomatoes were useless..."
        "...but at least I knew what to do next year."
    return

# TOMATOES 3 - results of tomatoes 2
label tomatoes3:
    scene fields with fade
    $ idx = get_crop_index("tomatoes")
    if (tomatoes2_action  == "early harvest"):
        "Because I made sure to always save seeds from the earliest tomatoes, the genetics of the tomato plants every year tended towards a fast harvest."
        $ modify_credits(farm.crops.count("tomatoes") * get_credits_from_name("tomatoes"))
        "In fact, now I can squeeze in two plantings a year, effectively doubling my tomato harvest."
        $ crop_info[idx][CALORIES_INDEX] = roundint(crop_info[idx][CALORIES_INDEX] * 1.5)
        $ crop_info[idx][VITA_INDEX] = roundint(crop_info[idx][VITA_INDEX] * 1.5)
        $ crop_info[idx][VITC_INDEX] = roundint(crop_info[idx][VITC_INDEX] * 1.5)
        $ crop_info[idx][VITM_INDEX] = roundint(crop_info[idx][VITM_INDEX] * 1.5)
        $ crop_info[idx][VALUE_INDEX] = roundint(crop_info[idx][VALUE_INDEX] * 1.5)
        $ crop_info[idx][NITROGEN_INDEX] = roundint(crop_info[idx][NITROGEN_INDEX] * 1.5)
    elif (tomatoes2_action == "size"):
        "Since I only used seeds from the biggest tomatoes, the size of the tomatoes kept getting bigger and bigger."
        $ modify_credits(0.5 * farm.crops.count("tomatoes") * get_credits_from_name("tomatoes"))
        "Not only did they look impressive, but they were easier to process because I had less stems to cut off before canning them."
        $ crop_info[idx][WORK_INDEX] = roundint(crop_info[idx][WORK_INDEX] / 2)
        $ crop_info[idx][VALUE_INDEX] = roundint(crop_info[idx][VALUE_INDEX] * 1.25)

    elif (tomatoes2_action == "sweetness"):
        "As I selected for the sweetest tomatoes, my harvest got slowly sweeter and sweeter."
        "[her_name] will sometimes pack a lunch of just tomatoes and a little goat cheese."
        "And [kid_name] likes to eat them, too."
        $ modify_credits(0.25 * farm.crops.count("tomatoes") * get_credits_from_name("tomatoes"))
        "They were so sweet I used them like berries in dessert dishes."
        $ crop_info[idx][VALUE_INDEX] = roundint(crop_info[idx][VALUE_INDEX] * 1.75)
    else:
        "Finally, I had a good tomato harvest. The tomatoes were firm all over and there were plenty of them."
        "Time for salsa, spaghetti sauce, and maybe even some pizza!"

    if ((get_work_available() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        "Now that the tomato harvest was finally over, I could start thinking about next year... I wanted another field for crops, so I cleared and fenced another field."
        $ modify_farm_size(1)
    return

# PLUMS 1 - trees growing
label plums1:
    scene fields with fade
    "I was happy to see the plum trees getting larger and larger."
    "They didn't have any fruit now, so it felt like a lot of work for nothing."
    "But I knew if I kept taking care of them and fertilizing them, eventually they would bear fruit."
    "Kind of like raising kids, actually. All that work when they were babies, changing diapers, and holding them, and feeding them..."
    "But, unlike the plum tree, I didn't know for sure what kind of adult I would eventually get."
    return

# PLUMS 2 Several years later
# Prunes or jam?
label plums2:
    scene plum_blossoms with fade
    "I'll never forget the first time the plum trees really bloomed..."
    "Thousands of pink blossoms covered the trees this spring, and when they fell, their petals covered the ground in a soft pink carpet."
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
    "I saved a few pits in case I wanted to plant more later."
    $ plums_index = get_crop_index("plums")
    $ crop_info[plums_index][MAXIMUM_INDEX] += 1
    $ enable_crop("plums", False)
    "I could just bring them to the storehouse, but they'd be worth more if I made them into prunes or jam first."

    $ make_item = "plums"
    menu:
        "What should I do?"
        "Make prunes" if (get_extra_work() >= 0):
            $ make_item = "prunes"
            scene farm_interior with fade
            "I pitted them and put them on a rack to dry."
            "I had to put a screen over them to keep pests away, but after several days I had some delicious prunes."
            show her normal coat at midleft with moveinleft
            show him normal at midright with move
            her surprised coat "Prunes? That's wonderful! I don't have much constipation medicine so it'll be great to have a natural remedy instead."
            him annoyed "You don't have to be constipated to enjoy some good prunes."
            her normal coat "They'll be good for [kid_name], too. Thanks, [his_name]."
            "I dropped most of them off at the storehouse and didn't think much about it for several days, until I got a visitor."
            scene farm_exterior with fade
            show him normal at midright with dissolve
            show thuc normal at midleft with moveinleft
            thuc happy "Man, I'm so glad you made prunes. Can I just say, everything around here is going a lot more smoothly?"
            him surprised "You like prunes?"
            thuc normal "Well, one of my kids really needed them. I don't want to embarrass them, so that's all I'm going to say. But thank you!"
            him normal "You're welcome, I guess."
            thuc happy "In fact, I brought you a little something."
            "He handed me a basket full of heads of garlic."
            him surprised "Oh, thanks!"
            thuc normal "This is nice and fresh, so you can plant it or eat it."
            him happy "Mmmm, this'll be good! Thank you!"
            if (crop_enabled("garlic")):
                "I already could grow my own garlic, but I appreciated Thuc's gift."
            else:
                "I couldn't wait to eat some, but even better, now I could grow my own."
            $ enable_crop("garlic")
            return

        "Make jam" if (get_extra_work() >= 0):
            scene farm_interior with fade
            $ make_item = "jam"
            "I decided to make jam."
            "My mother always made jam with sugar and pectin."
            "It would kind of defeat the purpose of making jam if I had to buy expensive sugar and pectin to make it work."
            "After some research, I found plums already have a fair amount of sugar and pectin in them. So I decided to slow cook them until they made a thick jam."
            "It was a bit sour, but very flavorful. And the jars should last at least a year."

            scene storeroom with fade
            show ilian normal at midright with dissolve
            show him normal at midleft with moveinleft
            him normal "Hey there, Ilian."
            ilian normal "Oh. Hello."
            him happy "How much can you give me for all this plum jam?"
            ilian angry "I can only give you 50 credits."
            him surprised "What? Why is that?"
            ilian normal "I'm out of money. But if you'd like to exchange, I can give you seeds for onions, broccoli, or turnips."
            menu:
                "Which should I choose?"
                "Onions":
                    him normal "Give me the onions."
                    $ enable_crop("onions")
                "Broccoli":
                    him normal "Broccoli sounds good."
                    $ enable_crop("broccoli")                    
                "Turnips":
                    him normal "How about the turnips?"
                    $ enable_crop("turnips")
                "Credits":
                    $ modify_credits(50)
                    him normal "I'll just take the 50 credits"
            ilian normal "Fine. Here you go."
            "My plum jam didn't make me rich, but at least I got something for it."
            return

        "Just bring the plums to the storehouse.":
            "I decided to just bring the plums to the storehouse. I didn't have time for anything else."
            $ modify_credits(40)
            "I earned 40 credits for them."

    if not (renpy.showing("storeroom")):
        scene storeroom with fade
        show ilian normal at midright
        show him normal at midleft with dissolve

    "While I was at the storehouse, I saw that they had a ton of onions for just 15 credits."
    "If I bought them, I could plant some and grow my own..."
    if (credits >= 15):
        menu:
            "What should I do?"
            "Buy onions.":
                $ modify_credits(-15)
                "I decided to buy them. It's always good to have more crops to choose from, and onions go well with everything."
                $ enable_crop("onions")
            "Don't buy onions":
                "I decided not to buy them. I had enough crops to deal with."
    else:
        "Too bad I didn't have enough credits for them."
    return

# BEANS 1 - How to harvest beans
label beans1:
    scene fields with fade
    show tractor at midleft
    show him normal at midleft
    with dissolve
    him happy "Look at all these beans!"
    him normal "And they're finally dry enough to harvest."
    "I drove the tractor down the rows so the puller attachment could pluck up the plants from the ground."
    show tractor at midright
    show him determined at midright
    with move
    "Then I fed them into the sheller to separate the pods from the beans."
    scene farm_exterior with fade
    show him normal at center with dissolve
    if (year >= 7):
        show kid normal at midleft with moveinleft
        kid surprised "Can I turn the crank?"
        him happy "Of course!"
        if (year <= CHILD_MAX):
            "She only lasted for a few minutes, but it gave me a chance to move some things around so that the shelling would be more efficient."
        else:
            "She cranked and cranked... I wasn't sure she ever would have admitted she was tired, so I made her give me a turn."
        "When we got tired of turning the crank by hand I attached my drill to turn it for us. That went even faster."
        "We filled up barrels and barrels of dried beans."
    else:
        "When I got tired of turning the crank by hand I attached my drill to turn it for us. That went even faster."
        "I filled up barrels and barrels of dried beans."
    return

# BEANS 2 - Wet beans
label beans2:
    play sound "sfx/rain.ogg" loop
    scene fields with fade
    show rain
    show him concerned at center behind rain with dissolve
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
            "...and most of them were soggy and rotten."
            him annoyed "That was a lot of work for nothing."
            $ harvest_factor = 0.25
        "Hang them up somewhere dry.":
            "I needed them to dry, so I decided to hang them up."
            "I strung clothesline zig-zagging around the house and in the barn."
            "I hung them upside down in bunches everywhere."
            stop sound fadeout 2.0
            scene farm_interior with fade
            show him concerned at midright with dissolve
            show her normal at midleft with moveinleft
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
            "But it rained for over a week, and the rain seeped in under the tarp. The whole bottom layer was soggy and rotten."
            "At least the top layers dried out okay."
            $ harvest_factor = 0.65

    $ modify_credits(-(1-harvest_factor) * farm.crops.count("beans") * get_credits_from_name("beans"))
    "Hopefully the weather will be better for beans next year."
    stop sound fadeout 2.0
    return

# SPINACH 1 - heat wave kills spinach seeds
label spinach1:
    scene fields with fade
    "Even with all our technology -- our hybrid tractors, our careful genetic modifications, our surveillance cameras and timed sprinkler systems -- we were still at Mother Nature's mercy."
    "It usually didn't get very warm on Talaam. Most of the time our proximity to the ocean kept the temperatures moderate."
    "But one year we had heat combined with terrible solar flares..."
    "...and the spinach seeds never came up."
    "They needed cool temperatures to germinate. The weather was nice again -- for now."
    "I had enough seeds to plant one more batch of spinach. But if those also failed, then next year I wouldn't have any spinach seeds at all."
    menu:
        "What should I do with my spinach seeds?"
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
            $ modify_credits(-farm.crops.count("spinach") * get_credits_from_name("spinach"))
            him annoyed "Enjoy your spinach, goats."
            $ crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] = 1
        "Save the seeds.":
            "If we had one heat wave, we could have another. The safest bet was to just save the seeds for next year."
            scene farm_interior with fade
            show her normal at midright
            show kid normal at center
            show him normal at midleft
            her surprised "Is the spinach ready yet? I wanted to make a salad to go with dinner."
            him concerned "Sorry, no spinach this year. It got too hot."
            her concerned "Oh...that's too bad."
            $ modify_credits(-farm.crops.count("spinach") * get_credits_from_name("spinach"))
            him normal "Don't worry; we'll definitely have some next year."
            $ crop_info[get_crop_index("spinach")][MAXIMUM_INDEX] = 2
    return

# SPINACH2 - turtle slugs
label spinach2:
    play music problems
    scene fields with fade
    "I've been planting my spinach a little earlier to avoid any heat problems."
    "But this year, something has been eating the plants. I haven't seen anything, but when I checked the leaves, I could see bites taken out."
    show him determined at center with dissolve
    him "What could be eating the spinach?"
    $ spinach2_cameras = False
    menu spinach_3_menu:
        "What should I do?"
        "Check the surveillance cameras" if (not spinach2_cameras):
            "I trained the farm's cameras on the spinach plot, but the next morning when I looked at the video, none of the motion sensors were triggered.  I scanned through the video but couldn't find anything out of the ordinary."
            $ spinach2_cameras = True
            jump spinach_3_menu
        "Check on your spinach at night":
            show night_overlay with dissolve
            show him annoyed at center with moveinleft
            "After [kid_name] and [her_name] went to bed, I snuck out of the house to examine the spinach plants.  My flashlight caught something small and slimy -- it looked like a snail!"
            "It wasn't exactly like an Earth snail; its shell was hard, and shaped like a turtle's shell instead of in a spiral pattern. Its body was soft and squishy, but with little feet protuberances like a caterpillar."
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
                    scene fields with fade
                    show him normal at midright with dissolve
                    "In the morning, the hole was full of turtle-snails, just waiting for me."
                    if (get_work_kid() > 0):
                        show kid surprised at midleft with dissolve
                        kid "What are you doing out here?"
                        him angry "I am about to dispense justice onto these vicious turtle-snails that have been murdering our spinach."
                        "She peered inside the trap."
                        kid annoyed "How are you going to do that?"
                        him concerned "I haven't decided yet..."
                        kid nervous "Actually, they're kind of cute."
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
                                    call spinach2_eat_snails from _call_spinach2_eat_snails
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
                                    call spinach2_eat_snails from _call_spinach2_eat_snails_1
                                else:
                                    hide kid with moveoutleft
                                    "She left, and I carried out the death sentence on the turtle-snails."

                    "I made some more traps and repeated the process until no more turtle-snails appeared."
                    "And we harvested a lot of wonderful spinach."
                "Just pick the spinach early":
                    "It'd be too much work to kill all the snails. If I just harvested the spinach early then there wouldn't be anything for them to eat."
                    call spinach2_pick_early from _call_spinach2_pick_early
        "Just pick the spinach early":
            "I decided to just pick the spinach. It was still small, but edible. It would probably taste even better."
            "As I was picking it, I found one of the creatures responsible."
            "It was small, with a hard, domelike shell. Its body was soft and squishy, but it with little feet protuberances like a caterpillar."
            "We called them turtle snails. I hoped that after I finished picking the spinach, they wouldn't have anything else to eat and they would leave."
            call spinach2_pick_early from _call_spinach2_pick_early_1

    scene black with fade
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
    if (bro_years > 0):
        show bro surprised at quarterright
    show her surprised at midleft
    with dissolve
    $ achieved("Chez Dad")
    her concerned "It's...interesting."
    kid nervous "It's...not bad."
    him concerned "I suppose... I could eat this."
    if (bro_years > 4):
        bro annoyed "I'm not eating it."
    "It was an interesting experiment, but ultimately we did not want to eat that many turtle-snails."
    "So I disposed of them."
    return

label spinach2_pick_early:
    "But spinach isn't the only thing turtle-snails like..."
    if ("beans" in farm.crops):
        $ snail_crop = "beans"
    elif ("peppers" in farm.crops):
        $ snail_crop = "peppers"
    elif ("squash" in farm.crops):
        $ snail_crop = "squash"
    elif ("broccoli" in farm.crops):
        $ snail_crop = "broccoli"
    elif ("strawberries" in farm.crops):
        $ snail_crop = "strawberries"
    elif ("carrots" in farm.crops):
        $ snail_crop = "carrots"
    else:
        $ snail_crop = "other crops"
    "After we picked the spinach, they moved on to our [snail_crop]."
    him annoyed "This is something that I cannot forgive."
    him angry "This means war!"
    "My nights were filled with killing turtle-snails."
    "They appeared in my dreams, giant, house-sized turtle-snails with ever-chewing mouths, the entire earth disappearing beneath their slavering jaws until Talaam was just an empty spot in the vast blackness of space."
    "I started seeing them everywhere I looked -- in the fields, in the barn, in the outhouse."
    "I trapped and tossed and stamped and squished, but the next night there were still more. For a week I barely slept trying to kill them all."
    "Finally, their numbers were greatly reduced, and I could rest.  Until the next invasion..."
    return

# Strawberries 1 - grow more?
label strawberries1:
    scene fields with fade
    show him normal at midright
    show kid normal at midleft with dissolve
    him normal "These strawberries are the best!"
    kid happy "Mmmm!"
    "We didn't have a lot of extra strawberries for jam or anything, but they tasted so sweet and delicious."
    "There's nothing like a fresh, warmed-in-the-sun, juicy, sweet, home-grown strawberry."
    "The other nice thing about strawberry plants is that they made lots of runners. If I wanted to, I could pull them up and start another strawberry field."
    menu:
        "What should I do?"
        "Expand your strawberry empire." if (get_extra_work() >= 0):
            him happy "What could be better than more strawberries?!  Let's plant some more, [kid_name]!"
            kid normal "Yeah!"
            $ strawberries_index = get_crop_index("strawberries")
            $ crop_info[strawberries_index][MAXIMUM_INDEX] += 1
            $ enable_crop("strawberries", False)
            $ responsive += 1
        "Sell the extra plants.":
            "I didn't really need more strawberry plants.  But maybe someone else did."
            nvl clear
            him_c "I've got some extra strawberry plants I'm willing to sell. They grow fast and easy and taste delicious!"
            sara_c "{emoji=surprised} I want some!!!"
            ilian_c "We don't even have a farm."
            sara_c "We have some dirt! I need strawberries!!! {emoji=hearteyes} {emoji=yum} {emoji=strawberries}"
            natalia_c "Oh, my grandkids would love those. I'll take a few."
            kevin_c "I would like to plant some for additional vitamin C."
            him_c "Okay, I should have enough to everyone to have a few."
            thuc_c "I have strawberry plants, too. I'll sell them for the same price as [his_name]."
            nvl clear
            $ modify_credits(100)
            "I was able to make a little extra money selling strawberry plants."
        "Leave them alone.":
            "I was too busy this year. I decided to just leave them there and deal with them later."

    return

# Strawberries 2 - mutant cancerous strawberries from solar flare
label strawberries2:
    play sound "sfx/rain.ogg" loop
    scene fields with fade
    show rain
    "There were two things I liked about strawberries."
    "Obviously, the first was the delicious sweet fruit."
    "The second was that they were pretty low maintenance. I fertilized them and weeded them a little and that was it."
    "So it wasn't unusual that I hadn't checked on them for a month or two."
    show him normal at center behind rain with moveinleft
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
    if (year <= LILY_DIES_YEAR):
        lily_c "It is possible the plants mutated."
        sara_c "Like, X-Men strawberries?! {emoji=biohazard}"
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
        "Rip out only the mutated strawberries." if (get_extra_work() > 0):
            "It was a huge pain, but I decided to rip out all the mutated strawberries.  I destroyed every plant that didn't have any flowers on it."
            $ credits_lost = farm.crops.count("strawberries") * get_credits_from_name("strawberries")
            $ credits_lost += farm.crops.count("strawberries+") * get_credits_from_name("strawberries+")
            $ modify_credits(-credits_lost)
            "And the few strawberries that I did get, I planted instead of eating."
        "Till over the whole field.":
            "It would take forever to figure out which strawberry plants had mutated and which hadn't. I picked the strawberries that were there, ran over the whole thing with the tiller, and I was done."
            $ credits_lost = farm.crops.count("strawberries") * get_credits_from_name("strawberries")/2
            $ credits_lost += farm.crops.count("strawberries+") * get_credits_from_name("strawberries+")/2
            $ modify_credits(-credits_lost)
            $ enable_crop("strawberries", False)
            $ strawberries_index = get_crop_index("strawberries")
            $ crop_info[strawberries_index][MAXIMUM_INDEX] = 1
            $ farm.delete_crop("strawberries+")
            "Maybe next year I could plant strawberries from the seeds that I salvaged."
    stop sound fadeout 2.0
    $ achieved("Mutant Ninja Berries")
    return

label onions1:
    scene fields with fade
    show him normal at center with dissolve
    "One reason I liked onions is that their growing season was opposite many other plants."
    "We planted them right after harvesting most other vegetables."
    "They grew slowly during our cool, rainy months, and we harvested them when the weather got warm."
    "And I never would have predicted that onions would have been so popular!"
    zaina_c "[his_name], are your onions almost done?! Onions just make everything taste better!"
    if (year < PAVEL_DIES_YEAR):
        pavel_c "In a good curry they are essential!"
    if (year < LILY_DIES_YEAR):
        lily_c "Did you know onions were eaten in ancient Egypt, and China? They are one of the oldest cultivated foods."
    if (year < MARTIN_DIES_YEAR):
        martin_c "They grow wild all over Earth, on every continent."
    julia_c "Save onion skins for Gardenia, please! She wants to use them to make a yellow dye."
    $ modify_credits(farm.crops.count("onions") * get_credits_from_name("onions"))
    "Since not many people planted them this year, they were in really high demand."
    return

# Honey event
# Can only happen year 11+
label honey1:
    scene fields with fade
    show him normal at center with dissolve
    "Having bees wasn't just good for pollinating plants; I also really enjoyed when we got to harvest the honey."
    "But when I went to harvest the honey, I noticed something."
    him surprised "Some of the honey is missing!"
    "A whole frame was gone."
    "At first, I thought maybe I had made a mistake and just forgot to put it in or something. But when I looked around, I found it several meters away."
    "All the honey and the comb had been clumsily scraped off. I looked around for tracks but didn't see any."
    him angry "Who did this?!"
    "I went to my security cameras and looked at the footage. There was nothing during the past week... it must have been done a while ago."
    "But I finally found the thief. It was late at night, so the footage was black and white and a little blurry."
    him surprised "It looks like... a kid?!"
    "The kid looked about [kid_name]'s age. At first I thought maybe it was her... but then I noticed that the kid entered and left from the path that led to town."
    "I couldn't make out his features, but it looked like a boy wearing a wide-brimmed hat."
    "There couldn't be that many kids that age with that kind of hat on the planet."
    menu:
        "What should I do?"
        "Ask on the colony message area.":
            nvl clear
            him_c "Hey, I'm looking for a kid about [kid_name]'s age with a wide-brimmed hat. Anyone know who that could be?"
            natalia_c "I have a hat like that but my kids are all older. What happened?"
            if (year <= NAOMI_DIES_YEAR):
                naomi_c "Is something wrong?"
            menu:
                "What should I say?"
                "He stole some honey.":
                    him_c "He stole some of my honey."

                "Just looking for him.":
                    him_c "Nothing in particular. Just looking for him."
                    ilian_c "You wouldn't be looking without a reason. What'd he do?"
                    if (year <= NAOMI_DIES_YEAR):
                        naomi_c "Please be honest with us, [his_name]."
                    him_c "...he stole some honey from our farm."
            sara_c "That's awful! He's not one of the miner's kids, is he? {emoji=worried}"
            brennan_c "Nope, not one of ours."
            julia_c "Kids these days..."
            nvl clear
            "No one had any more information on the message board, but I got a private message later that day."
            if (year <= NAOMI_DIES_YEAR):
                naomi_c "The honey thief may be from Pete and Helen's family."
            else:
                sara_c "Hey, have you considered that the honey thief might be Pete and Helen's son?"
            him_c "You think it's Travis? It would explain why no one recognized him... Thanks, I'll look into it."
            nvl clear

        "Look for a kid with a wide-brimmed hat.":
            "I kept my eyes peeled in town, and even made an excuse to stop by the school, but I didn't see any kids that matched the video."
            "I finally asked [her_name] about it. She knows almost everyone because of her work, but I wasn't sure she'd want to tell me."
            scene hospital with fade
            show her normal coat at midright with dissolve
            show him normal at midleft with moveinleft
            him surprised "Hey do you recognize this kid?"
            "I showed her the footage."
            her surprised coat "A honey thief, huh?"
            him determined "Looks like it."
            her concerned coat "I can't say for sure... but it looks like Oleg or Travis."
            him concerned "That's what I thought..."
            her determined coat "No, it's definitely Travis. I recognize those clothes."

        "Ask [kid_name] if she recognizes him.":
            scene farm_interior with fade
            show kid normal at midright with dissolve
            show him normal at midleft with moveinleft
            him determined "Do you know who this is?"
            "I showed her the video footage."
            kid surprised "Wait... play it again?"
            "I could tell from the expression on her face that she knew who it was."
            kid nervous "Is he in trouble?"
            him annoyed "Well, he did steal honey from our farm."
            kid concerned "What are you going to do to him?"
            him surprised "I just want to talk to him."
            kid nervous "I... I think it's Travis."

    "It was time to pay Travis a visit."
    if (year <= PETE_LEAVES_YEAR):
        scene farm_exterior flip with fade
    elif (year <= PETE_LEAVES_CAVES_YEAR):
        scene cave with fade
    else:
        scene shack with fade

    if (not helen_dead):
        show helen normal at center

    show travis normal at midright
    with dissolve
    show him normal at quarterleft behind travis with moveinleft
    if (not helen_dead):
        helen happy "Oh. Hello, [his_name]."
        him normal "Hey there, Helen. How's it going?"
        helen normal "Okay, I guess. What brings you way out here?"
        menu:
            "What should I do?"
            "Talk to Helen about Travis":
                him determined "I'll get right to the point. Travis stole some of our honey."
                show travis angry at quarterright with move
                helen sad "Oh, really? Why do you think that?"
                show travis angry at right with move
                him concerned "I have video footage right here."
                "I showed her the security video."
                helen angry "Hmmm. Travis!"
                travis normal "I was just going to go, uh, do my chores!"
                show helen sad at quarterright with move
                helen sad "C'mere and talk with [his_name]. And--"
                "She whispered something in his ear that I didn't hear."
                hide helen with moveoutright
            "Talk to Travis directly.":
                $ travis_points += 1
                him determined "Travis, I need to talk to you."
                show helen sad at right with move

    show him at center with move
    show travis normal at midright with move
    travis happy "Uh, hi there Mr. [his_name]. It's, uh, been awhile. How's [kid_name]?"
    him annoyed "Don't change the subject. I caught you stealing my honey."
    travis normal "Oh, uh, what?"
    "I showed him the video. Standing here and comparing him to the video, it was easier to tell that it was him."
    "He fidgeted and looked around as if wondering if there was an escape route. Or if he could possibly lie his way out of it."
    him determined "I know it was you."
    travis angry "Oh. Uh. Yeah."
    menu:
        "What should I say?"
        "Why did you do it?":
            him concerned "Why did you steal from me?"
            travis angry "I don't know."
            him surprised "You don't have a good reason?"
            travis normal "Not really. I mean, honey tastes good. It's really sweet."
            him annoyed "That's the only reason?"
            travis angry "Pretty much."
        "I expect full compensation.":
            $ travis_points -= 1
            him determined "I expect you to compensate me for that honey. It's about 50 credits worth."
            travis angry "50 credits?!"
            him concerned "If you don't have the credits, you can work for me instead."
            travis angry "..."
            him surprised "What was that?"
            travis normal "...okay."
        "(Wait for him to say something)":
            "I just waited. He shifted his weight from one foot to the other. I waited some more. Finally, he said quietly,"
            travis angry "I'm sorry I stole your honey."
            him normal "Thank you, Travis. Please don't let it happen again."
            travis normal "I won't."
            "I waited some more. He cleared his throat and looked around."
            travis happy "So is that it?"
            him determined "Well, usually when someone steals something, they apologize and then give it back."
            travis normal "Oh. I can't give it back; we already ate it."
            him surprised "We?"
            travis happy "My brothers and sisters and I."
            "Well, at least he shared his ill-gotten goods."
            him determined "So what are you going to do instead?"
            travis angry "Oh. Ummm, I could probably give you some cheese. I helped make it."
            if (not helen_dead):
                him normal "That sounds good. Why don't you and your parents work out something and bring it by later?"
            else:
                him normal "That sounds good. Why don't you and your dad work out something and bring it by later?"
            travis normal "Okay."

        "I'm disappointed you would steal from me.":
            him sad "I'm disappointed you would steal from me."
            travis angry "It's nothing against you personally! We just really wanted something sweet."
            him surprised "We?"
            travis normal "My brothers and sisters and I. Sometimes we just get really hungry."
            him concerned "I see. Unfortunately, I can no longer trust you like I once did."
            travis angry "Oh."
            him sad "But if you're really hungry, come ask and I'll give you some food."
            travis normal "Oh. I mean, we don't need a handout or anything, we're doing just fine--"
            him normal "It's okay. I get it."
    him surprised "It's gotta be tough living out there by yourselves?"
    travis angry "My dad's always saying how we gotta live on our own, do everything ourselves, be independent."
    him concerned "Yeah..."
    travis normal "I guess I was just trying to do something on my own."

    menu:
        "What should I say?"
        "Quit stealing.":
            $ travis_points -= 1
            him determined "I understand what you're saying, but you can't steal from people."
            travis angry "Yeah."
        "Want to learn beekeeping?":
            $ travis_points += 2
            $ mavericks += 1
            him determined "You want to be independent? Why don't you come learn beekeeping? Eventually I'll need to split the hive and you can have your own bees."
            travis angry "I don't like bees..."
            him normal "You probably got stung a lot during your heist, huh?"
            travis normal "Yeah... but I wasn't going to walk away empty-handed!"
            him happy "Well, learning how to handle bees without getting stung is part of beekeeping!"
            travis happy "Well... that'd be stellar."
            him normal "Great! You can pay off the honey you stole by working with the bees."
        "Good luck.":
            him determined "Good luck living on your own."
            travis angry "Okay."

    return

# BROCCOLI 1 - grubs?!
label broccoli1:
    scene farm_interior with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center
    him happy "Man, I love broccoli! Especially with this goat cheese sauce..."
    kid annoyed "It's okay."
    her concerned "I usually like it, but there's something funny about it today..."
    him surprised "Really? I haven't tasted anything weird."
    her surprised "Did you wash the broccoli before you cooked it?"
    him determined "I rinsed it off, sure."
    "She poked around under the cheese sauce, and when her fork came out, it had a small blob on it that didn't look like broccoli or cheese."
    "It looked like..."
    her blush "A caterpillar?!"
    kid surprised "What?!"
    him doubt "Do they even have caterpillars here?"
    "She brought the fork closer to my face."
    her annoyed "You tell me!"
    "It wasn't a caterpillar - there were no nubby feet or sections. But it definitely looked like some kind of tiny grub."
    her sad "I'm pretty sure I ate one of those..."
    him surprised "Yeah, me too. Hopefully they're not poisonous."
    her angry "Well, they're definitely disgusting!"
    hide her with moveoutleft
    kid shifty "...I'm done."
    hide kid with moveoutleft
    him laugh "Looks like more food for me!"
    "I picked off the strange grubs and enjoyed my broccoli."

    "...but next time I made sure to wash it very thoroughly."

    return


###########################################################################################
#
# MONEY EVENTS - Events for if you have a lot of money.
#
###########################################################################################

# Donate to a sick single parent.
label money1:
    nvl clear
    "I was doing some financial calculations on the computer pad when I got a message from Sara."
    nvl clear
    sara_c "[his_name], we're looking for people to help out a family in need. There's a dad and three little kids and the dad has been sick for the past month."
    him_c "That's rough. What do they need?"
    sara_c "Well, he'd like to be able to hire someone to help out with the kids and around the house, but he can't really afford it."
    sara_c "A few people have been taking turns volunteering but they can't do it long term."
    him_c "So he needs money."
    sara_c "Basically, yes. We also have a few people looking for work, so it'll be good for everyone. 1000 credits would be enough for a few months."
    "I explained the situation to [her_name], who said she thought donating was a good idea but left the exact amount up to me."
    menu:
        "What should I do? I have [credits] credits."
        "Donate 1000 credits":
            him_c "I'll donate 1000 credits."
            $ modify_credits(-1000)
            sara_c "Wow, really?! Okay, I guess my work is done for the day!"
            $ colonists += 2
        "Donate 500 credits":
            him_c "I'll donate 500 credits."
            $ modify_credits(-500)
            sara_c "Thank you; that's very generous of you! I'm sure I can find some other people to chip in the rest."
            $ colonists += 2
        "Donate 100 credits":
            him_c "I can spare 100 credits."
            $ modify_credits(-100)
            sara_c "Okay, thanks, every little bit helps!"
            $ colonists += 1
        "Don't donate anything":
            him_c "Sorry, I can't donate anything."
            sara_c "Oh... okay."
            $ colonists -= 1
            return
    "About a month later I got a note from the dad and his kids."
    nvl clear
    note_c "Thanks so much for helping out when I was sick. It's been a long recovery but I am starting to work again. Your donation made a huge difference."
    nvl clear
    return

# Investment opportunity
label money2:
    scene community_center with fade
    show him normal at midleft with dissolve
    "One evening after a meeting, Zaina approached me."
    show zaina normal at midright with moveinright
    zaina normal "Hey, [his_name], I have a question for you."
    him happy "Okay, ask away!"
    zaina sad "You seem like you're good with money. I have a great invention, but I need some capital to get started."
    him surprised "What's your invention?"
    zaina normal "Well, you push it between the rows, and as you walk it spins blades. They can chop up weeds and stuff without using electricity."
    him concerned "Wait, so it's like a weed chopper?"
    zaina happy "That's a great name for it! Yeah, a weed chopper! I think everyone will want one!"
    him normal "Hmmm. I know pulling weeds is one of my least favorite parts of farming..."
    zaina normal "Right?! I talked to Ilian about the parts - we can print most of them, but some parts have to be metal, which is not cheap."
    him concerned "How much are we talking?"
    zaina sad "I could make them for about 45 credits each, but if I made 50 or more of them it would only cost 35 credits each. That makes 1750 credits total."
    him surprised "1750 credits?!"
    zaina normal "I have 750 I could spare, but that's it. Will you help with the other 1000? I'll pay you back with the profits!"
    menu:
        "What should I tell her?"
        "I can invest 1000 and help you sell them." if (get_extra_work() >= 1):
            $ modify_credits(-1000)
            him happy "This is a great idea! I can invest 1000 credits and you can pay me back with your profits. I'll help you sell them, too."
            zaina happy "Thank you! I'm like a fossil when it comes to business stuff, so I'm glad you can help."
            scene stars with fade
            "It was a good thing I helped out - her invention was great, but there were a lot of costs she had not factored into her price. I helped her estimate those and we set a higher price."
            "I also helped with advertising, and we managed to sell all 50 of the weed choppers."
            nvl clear
            $ modify_credits(1500)
            zaina_c "I couldn't have done it without you! Here's your share of the profits."
        "I can invest 1000.":
            $ modify_credits(-1000)
            him happy "This is a great idea! I can invest 1000 credits and you can pay me back with your profits."
            zaina happy "Great!"
            scene stars with fade
            "She made a whole bunch of weed choppers, but she underestimated some of the costs and she wasn't very good at explaining it. She ended up only selling half of them and giving the rest away."
            nvl clear
            $ modify_credits(800)
            zaina_c "[his_name], I didn't end up making any profits on this project at all... but I can pay you back 800 credits and a free weed chopper. I'm sorry."
        "I'll buy one, but I can't help you.":
            him concerned "Sorry, I can't help you with this. I would like to buy a weed chopper, though."
            zaina sad "Well, I don't think I'll make them if I can't get the capital to make at least 50. It wouldn't really be worth it."
        "I can't help you.":
            him determined "Sorry, I can't help you. Good luck, though!"
            zaina sad "Okay, I understand. Hopefully I can find another investor..."
            "She never found anyone, though, so she never made the weed choppers."

    nvl clear
    return
