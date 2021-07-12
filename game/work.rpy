## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting."
    return

# Event for if you overwork yourself.
label overwork:
    $ overwork_count += 1
    $ random_crop = farm.crops.random_crop(True, False)

    if (overwork_count <= 1):
        "I like a challenge."
        "I push myself to work hard, be productive, and get things done."
        "But this year, I took on too much."
        "I was already exhausted from working dawn-to-dusk on weeding and maintaining the fields, and my list of to-dos was getting longer and longer."
        "Harvest loomed ever closer, like a meteor hovering overhead."
    else:
        "I should have known better, but I could tell that I was trying to take on too much (again)."
    # The first time you ask for help from a group, it's a bonding experience. After that, they get annoyed.
    nvl clear
    menu:
        "I have too much work... what should I do?"
        "Ask other farmers for help." if ((overwork_colonists < 2) and colonists_strong("moderate")):
            $ overwork_colonists += 1
            if (overwork_colonists <= 1):
                $ colonists += 1
                him_c "Hey, anyone want some free [random_crop]? I could use a hand harvesting them."
                thuc_c "Are you kidding? I love [random_crop]."
                julia_c "Got more than you can handle, eh?"
                zaina_c "If there's free fresh food, I'm there."
                him_c "Thanks, everyone..."
                scene fields with fade
                show him normal at center
                show thuc normal at midright
                show julia normal at quarterright
                show zaina normal at midleft
                show kevin normal at quarterleft
                with dissolve
                "With everyone's help, we were able to harvest all the [random_crop]. Everyone took home a bunch, too, so I had less to process."
            else:
                $ colonists -= 1
                him_c "Hey, I have extra [random_crop] for anyone that wants to help with the harvest."
                thuc_c "Now?? Sorry, no time. I could use a hand myself, actually."
                zaina_c "I could probably stop by in a few days..."
                scene fields with fade
                show him determined at midright
                show zaina normal at midleft
                "Not many people showed up, but we were able to harvest most of the [random_crop]."
                $ modify_credits(farm.income_loss(98))

        "Ask miners for help." if ((year > MINERS_ARRIVE_YEAR) and (overwork_miners < 2) and miners_strong("moderate")):
            $ overwork_miners += 1
            if (overwork_miners <= 1):
                $ miners += 1
                "Ugh. Asking for help was hard enough... but asking for help from Brennan? Maybe I could just post something on the miner's message area."
                "But unfortunately, I didn't have access to it."
                him_c "Brennan, can you post a notice that if any miners are looking for free food, they can come help harvest [random_crop]?"
                brennan_c "Why would any of them want to do that?"
                him_c "It's fresher and tastier if you pick it yourself."
                brennan_c "Hmmm. Not sure you'll get many takers, but if you send it to me, I'll post it."
                scene fields with fade
                show him normal at midright
                show miners at quarterleft
                with dissolve
                "It turned out a couple of miner families thought it would be fun to harvest food for a day."
                "They only stayed for a few hours, but at least they made a dent in the plentiful [random_crop]."
            else:
                $ miners -= 1
                him_c "Brennan, can you post a message asking if any miners want to help with the [random_crop] harvest?"
                brennan_c "Again? This seems like poor planning on your part."
                him_c "Can you just send the message?"
                brennan_c "Surely you don't expect us to come running every time you have a problem."
                him_c "CAN YOU PLEASE JUST ASK??!"
                brennan_c "Of course. Don't get so cheesed off."
                scene fields with fade
                "A few miners sent some of their kids that were too young for the mines, so I kind of ended up babysitting them all trying to make sure they did it right and didn't trample everything."
                "They picked a few [random_crop], but a lot of them just went to waste."
                $ modify_credits(farm.income_loss(75))
        "Ask your family for help." if (overwork_family < 2) :
            $ overwork_family += 1
            if (overwork_family <= 1):
                $ marriage_strength += 1
                $ responsive += 1
                $ demanding += 1
                call bedroom_scene(False, False) from _call_bedroom_scene
                show him determined with dissolve
                show her surprised with dissolve
                show him concerned with dissolve
                show her annoyed with dissolve
                her annoyed "All right. Out with it. Why can't you sleep?"
                him concerned "I need to harvest the [random_crop]..."
                her surprised "And... why is that a problem?"
                him sad "There's... a lot. Maybe too much, with all the other crops I have to worry about, too."
                her determined "Do you need some help?"
                him concerned "No, I could probably do it on my own..."
                her annoyed "Let me rephrase that. Do you want some help?"
                him sad "I know you're busy, but..."
                her determined "Nope, I'll help you out."
                if (year >= TODDLER_MAX):
                    her normal "[kid_name] can help, too."
                if (year >= CHILD_MAX):
                    him determined "And [bro_name]."
                her concerned "I don't have any appointments in the mornings this week, so I'll work here with you and then go in late. Okay?"
                him concerned "Thanks, [her_name]..."
                her annoyed "Now will you please go to sleep?"
                scene fields with fade
                "[her_name] wasn't an expert or anything, but with her help we were able to harvest all the [random_crop]."

            else:
                $ marriage_strength -= 1
                $ responsive -= 1
                $ demanding -= 1
                scene farm_interior with fade
                show him normal at midright
                show her normal at midleft
                show kid normal at quarterleft
                him surprised "Hey, I'm kind of worried about the [random_crop]..."
                her surprised "What's wrong?"
                him concerned "I don't know if I have time to harvest them all..."
                her annoyed "You knew this would happen."
                him surprised "What do you mean?"
                her angry "You planted all those [random_crop] knowing full well that you wouldn't have time to harvest them all yourself."
                him concerned "Well, I wasn't completely sure..."
                her annoyed "You can't just overplant your farm and expect me to help you out every time! I have a job already!"
                him angry "Fine! Don't help me, then."
                her concerned "I'll help you out this time. But this is the last time."
                him concerned "Thank you, [her_name]."

        "Ask Pete's group for help." if ((year > PETE_LEAVES_YEAR) and (overwork_mavericks < 2) and mavericks_strong("moderate") and not helen_dead):
            $ overwork_mavericks += 1
            if (overwork_mavericks <= 1):
                $ mavericks += 1
                if (year >= PETE_LEAVES_CAVES_YEAR):
                    scene shack with fade
                else:
                    scene cave with fade
                show pete normal at midleft with dissolve
                show him normal at midright with moveinright
                him happy "Pete! I feel like I never see you anymore!"
                pete happy "That's because you don't."
                him normal "Well, yeah, but it's not like you live on a different planet or anything."
                pete normal "Nope."
                him concerned "Hey, want to come help harvest [random_crop]? You can take some home with you."
                pete happy "I could probably find a few hours this week. Mind if I bring the whole family?"
                him happy "Bring anyone you like! Honestly, I could really use your help."
                scene fields with fade
                show him normal at midleft
                show pete normal at center
                show helen normal at midright
                show travis normal at quarterright
                if (year < LILY_DIES_YEAR):
                    show lily normal at quarterleft
                "With so many people, it didn't take us very long to harvest all the [random_crop]."
                him happy "Thanks, guys!"
            else:
                $ mavericks -= 1
                $ travis_points += 1
                scene shack with fade
                show pete normal at midright
                show him normal at midleft
                with dissolve
                him happy "Hey, Pete! Want to come help harvest [random_crop]?"
                pete normal "Not really. I got a bunch of other stuff going on right now."
                him sad "Oh..."
                pete angry "Don't look like that..."
                him concerned "I'll find some other way..."
                pete normal "I'll send Travis over. That's all the help I can spare at the moment, though."
                him normal "Thanks, I think that'll be good enough."
                "Travis worked hard, but it wasn't nearly enough help."
                $ modify_credits(farm.income_loss(90))

        "Don't ask for help.":
            $ overwork_self += 1
            "Everyone else had their own problems. I got myself into this mess; now I would get myself out of it."
            if (overwork_self <= 1):
                "I stayed up late; I woke up early. I didn't do anything else for weeks except take care of the farm."
                play sound "sfx/rain.ogg" loop
                scene fields with fade
                show tractor at center
                show him concerned at center
                with dissolve
                him concerned "I can do this... just one more week."
                scene black with fade
                scene fields with fade
                show rain
                show tractor behind rain at center
                show him sad behind rain at center
                with dissolve

                him sad "Just one more day..."
                window hide
                show black with irisin
                hide black with irisout
                window show
                show him sleeping with dissolve
                "It was when I fell asleep at the wheel of my tractor that I realized I was pushing myself too hard."
                show him sad with dissolve
                "I had to get some rest..."
                "And my harvest suffered."
                stop sound fadeout 2.0
                $ modify_credits(farm.income_loss(90))
            else:
                "But there was a limit to how much I could physically do, and my harvest suffered."
                $ modify_credits(farm.income_loss(80))
        "Hire some help." if ((year > MONEY_YEAR) and (credits >= 200)):
            "I had plenty of money. I'd just hire someone to help me."
            cycle work_hire:
                block:
                    "A few of the miners' kids were willing to help out on the farm -- but for a steep price. They didn't know much about farming, but they learned quickly!"
                    $ lorant_points += 1
                    $ modify_credits(-200)
                block:
                    "[kid_name] asked around, and some of her friends came and helped out. They didn't do the best job, but they didn't want much pay, either."
                    $ modify_credits(-100)
                block:
                    "Sara and Oleg answered my job offer -- it sounded like Sara and Ilian were going through a rough patch and she wanted to be financially independent."
                    $ oleg_points += 1
                    $ modify_credits(-150)
                block:
                    "I looked and looked but no one had the time to help me for any price that I could afford."
                    "So my crop yield was not what it could have been."
                    $ modify_credits(farm.income_loss(85))
    return

# If you don't make enough money...
label debt_event:
    $ random_crop = farm.crops.random_crop(True, False)
    scene farm_interior with fade
    show her determined at midright
    show him concerned at midleft
    with dissolve

    if (debt_event_count == 0):
        her concerned "[his_name]... I went to buy some things at the storehouse, but Ilian said we were out of credits."
        him sad "Oh. Yeah."
        her annoyed "He let me have the things anyway, just giving me a warning and subtracting the credits further into the negative... But that has happened the last three times I was there."
        menu:
            "What should I say?"
            "I'll try harder.":
                $ marriage_strength += 1
                him concerned "I'm sorry, [her_name] -- it's hard to balance everything, but I can do better."
                her sad "I know you're trying hard, but we can't be in debt."
                him sad "I just don't know how I can do things any more cheaply."
                her determined "Let's write it down. Maybe we'll see something."
            "This is impossible!":
                him angry "That's because it's impossible! They don't pay us enough for all the hard work we do on these crops!"
                her surprised "Is that why we keep running out of credits?"
                if (year > MINERS_ARRIVE_YEAR):
                    him annoyed "Yes. The miners get paid like kings and us farmers barely have enough to scrape by."
                else:
                    him annoyed "Yes. This whole 'credits' thing was a stupid idea."
                her determined "There's got to be some way we can make things work."
                him determined "Maybe. Let's write down everything..."
            "What are they going to do, kick us out?":
                him doubt "I'm not worried. What are they going to do, kick us off the planet?"
                her angry "No, but they might say we can't buy anything at the storehouse!"
                him concerned "That wouldn't be good..."
                her determined "Let's write some things down."
            "Let's make a budget.":
                $ marriage_strength += 1
                him concerned "Let's make a budget together. Maybe if we write everything down we can figure something out."

        "We analyzed our income and expenditures, searching for ways we could do things more cheaply."
        "We cut out some luxuries and managed to reduce our annual expenses by 100 credits."
        $ annual_expenses_base -= 100
        if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
            $ modify_farm_size(1)
            "I also decided to prepare another field. That way I could plant more crops."
    else:
        "Even after we tightened our belts and reduced unnecessary expenses, we were still in the red."
        "Ilian stopped selling us everything except the barest necessities."
        "I had to do something."
        if (get_extra_work() > 0):
            "I had some extra time after my farm chores were complete, so I asked around to see if there was another way to earn money."
            cycle work_debt:
                block:
                    "I asked the miners, and they gave me a job hauling rocks with my tractor for a few days."
                    $ modify_credits(300)
                block:
                    if (year < NAOMI_DIES_YEAR):
                        "Sister Naomi had some odd jobs she needed help with around the house."
                    elif (year < PAVEL_DIES_YEAR):
                        "Pavel paid me for helping him move some furniture and carry some heavy things for him."
                    else:
                        "I knew Sara didn't have much, but she paid me to help fix up some things at her house."
                    $ modify_credits(100)
                block:
                    "Ilian let me work in the storehouse organizing and preserving food."
                    $ modify_credits(50)
                block:
                    if (year < LILY_DIES_YEAR):
                        "Dr. Lily needed some help cataloguing samples of local plants and animals. It was monotonous work, but she paid well."
                    else:
                        "I helped Miranda classify some new plants that she found. It was pretty boring, but she paid well."
                    $ modify_credits(100)
        else:
            "But I already had too much on my plate just with my own farm."
            "Word must have gotten out about our financial plight..."
            if ((miners_strong()) and (year > MINERS_ARRIVE_YEAR) and not seen_miners_debt):
                "One of the miners paid me a little extra, saying that the [random_crop] were especially good."
                $ modify_credits(20)
                $ seen_miners_debt = True
            elif ((mavericks_strong()) and (not seen_mavericks_debt)):
                "Pete dropped off some strange meat. He said it was from a recent hunting trip."
                $ modify_credits(25)
                $ seen_mavericks_debt = True
            elif ((colonists_strong()) and (not seen_colonists_debt)):
                "Thuc took pity on me and gave me some extra food."
                $ modify_credits(30)
                $ seen_colonists_debt = True
            else:
                "I came home from the fields to find a bunch of dried corn on our front doorstep."
                "There was no note or anything..."
                if (year < NAOMI_DIES_YEAR):
                    "It was probably from Sister Naomi."
                elif (year < PAVEL_DIES_YEAR):
                    "Maybe it was from Pavel? He always tries to look out for people who need help."
                else:
                    "It must have been from Natalia -- she grew a lot of corn."
                $ modify_credits(35)
                "I was really fortunate to have such caring neighbors..."

    $ debt_consecutive_years = 0
    $ debt_event_count += 1
    return


# Year 1, 3 mo. old
label work_intro:
    play music farming
    scene fields with fade
    "The area of Talaam we had settled on didn't have seasons like temperate zones on Earth; the temperature stayed mild all year and it rained a lot."
    "This meant that we could grow crops year round, but some crops didn't grow as well."
    scene aurora_animated with fade
    "Talaam's frequent solar flares meant we always had to check the forecast and be ready to take shelter in case strong flares were predicted."
    "The flares' radiation was dangerous to humans, but so far hadn't had much effect on plants."
    "On this new planet, though, everything was an experiment."
    call farm_tutorial from _call_farm_tutorial
    return

label farm_tutorial:
    menu:
        "Would you like to see the Farming Tutorial?"
        "Yes.":
                scene tutorial-left with fade
                "The left part of the screen shows information about my family and colony."
                scene tutorial-mid with dissolve
                "The middle of the screen shows the current year and the farm layout. I have a lot of land but it's not all cleared for farming yet."
                scene tutorial-right with dissolve
                "On the right is how much energy the current farm will provide, and how much work it will take."
                "I can also clear the whole farm if I want to start from scratch."
                scene tutorial-crop-select with dissolve
                "When I select a farm space, I can choose what crop should go there and see information about each crop."
                "I always have to allocate space for my goats, but which other crops I plant is up to me."
                scene tutorial-red with dissolve
                "The background color of each space shows how much nitrogen is in this field."
                "A red color means there's not enough nitrogen for that crop and I need to pick something else."
                "If it's dark brown, there's plenty of nitrogen for crops."
                scene tutorial-mid with dissolve
                "The lighter the brown color, the lower the nitrogen in that field. I should put something there that will add nitrogen, like goats or beans, or I can leave the field fallow to rest."
                scene tutorial-right with dissolve
                "I need a certain amount of energy, and I only have a certain amount of work I can do. Other than that, I can choose whatever crops I want."
                if (year > MONEY_YEAR):
                    "Some crops are worth more money than others. If I don't choose crops well, I could end up losing credits."
                "Sometimes there's extra options I can only choose if I have extra work, so I don't want to try to do too much."
        "No.":
            $ pass
    return

# Year 2, 9 months old
# Help Kevin and Zaina and get a plum tree
label work2:
    scene farm_interior with fade
    show him normal at midleft
    show her baby happy at midright
    with dissolve
    play sound "sfx/baby-gurgle.ogg" fadein 5.0
    her "Are you going somewhere?"
    him determined "Yeah, I said I'd help Kevin and Zaina with their garden."
    her baby sad "It wasn't as easy as the video games made it seem, huh?"
    him happy "Yeah, turns out there's actually a lot of things that you can't learn just from simulations!"
    her baby happy "All right, good luck."
    stop sound fadeout 2.0
    show path with fade
    "I headed off towards the mountains. I could just barely see their house from our land, but it took me a while to walk there."
    scene fields flip with fade
    show kevin normal at midright
    show zaina normal at center
    with dissolve
    show him normal at midleft with moveinleft

    zaina happy "Thanks for coming, [his_name]. I can't believe I ever thought growing my own food would be easy!"
    him concerned "Well, some parts aren't too hard. But it helps if you know what you're doing."
    "I walked through their fields with them, pointing out plants that needed different location, or different irrigation, or different nutrients in the soil. Some were more sensitive to solar flares than others, too."
    kevin sad "This information was not in the farming guide I was given."
    him normal "Yeah, you can't learn everything about alien farming from a book."
    kevin normal "That is unfortunate. Perhaps such a book should be made."
    him annoyed "If you want to write it, go right ahead."
    zaina normal "I think we'll be too busy taking care of these plants to write much about it right now!"
    kevin happy "Perhaps at a future time."
    zaina happy "Anyway, thanks for helping us out. Our trees didn't bear many plums, but here's a few of the ones we got. Maybe you can plant the seeds after you eat them?"
    him surprised "Plums? That'll be delicious; thank you!"
    zaina normal "Thank you, [his_name]!"

    $ enable_crop("plums")
    tutorial "Place perennials like plums carefully when planning the farm. They can't be moved once they're planted without killing them."

    kevin sad "I do not want to pester you continually with farming questions. Is there someone else whom I could also ask for assistance?"
    menu:
        "Who should they go to for farming questions??"
        "Natalia, a sassy farmer growing beans and corn." if (not met_peron):
            $ bios.activate("Natalia")
            $ bios.activate("Martín")
            him determined "Natalia is a really good farmer."
            zaina sad "I don't think we've met her yet... is she the one with all the chickens?"
            him happy "Yeah! They also grow beans and a few different types of corn."
            kevin normal "Corn is a versatile plant. Culinarily, it can be a vegetable or a grain."
            zaina normal "Does she have popcorn?"
            him surprised "Yeah, I think some popcorn seeds came on the shuttle with you guys and she's been trying them out. I bet her kids love that."
            kevin sad "Her kids?"
            him determined "She and Martín have five kids. Or, four now, I guess."
            zaina sad "Now?"
            him concerned "There was an accident... and their daughter Josephina died when she was four years old."
            zaina sad "What a shame. What happened?"
            menu:
                "What should I tell them?"
                "Pete ran over her with his tractor.":
                    him sad "Pete was driving his tractor and didn't see her in time..."
                    zaina sad "How awful. I bet he still feels bad about it."
                    him concerned "The Peróns have a vigil every year to remember her."
                    kevin sad "Are accidents like that common?"
                    him determined "No, I mean, usually accidents aren't so bad that someone dies. Natalia has mostly forgiven Pete... but it's hard."
                "She got run over by a tractor.":
                    him sad "She wasn't looking where she was going, and a tractor ran over her."
                    kevin sad "Was it a self-driving tractor or something?"
                    him concerned "No, one of my friends was driving it."
                    zaina normal "Oh, I see. You don't want to tell me who it was before I get to know them."
                    him determined "Yeah. The Peróns are still pretty sad about it and hold a vigil every year where it happened."
                    $ mavericks += 1
            him normal "Anyway, their other kids are old enough to help around the colony. Well, maybe not Mateo. But their oldest son Tomás just got married."
            $ met_peron = True

        "Mayor Grayson. He's not a farmer but he knows everyone!" if (not met_grayson):
            $ bios.activate("Pavel")
            $ bios.activate("Naomi")
            him determined "Honestly, I'd ask Mayor Grayson."
            kevin sad "Is the mayor a farmer, too?"
            him normal "No, but he knows everyone and how they're doing and who's an expert on what. So he could direct you to the right person. Or if he can't, Naomi could."
            zaina normal "That's his wife, right? What is her job exactly?"
            him concerned "She helps people who are having a hard time. She can't prescribe medicine, but she's very reassuring and can encourage you to get more help."
            zaina sad "Reassuring? So she basically tells you to 'hang in there.'"
            him pout "Somehow when she says it, it feels like she understands what you're going through. She has some training in cognitive behavioral techniques, too, as a therapist, so it's not just random talk."
            zaina happy "Oh, she's the one who sent out the announcement about church! Do you go to her services?"
            him normal "No, but [her_name] does."
            $ met_grayson = True

        "Julia, a bossy farmer who's an expert on fertilizer." if (not met_nguyen):
            $ bios.activate("Julia")
            him normal "Julia's probably the best person to ask if you want an expert opinion."
            zaina sad "That's Thuc's wife, right? Wasn't she sick last time?"
            him concerned "Yeah, she has some kind of chronic pain issue. Whenever she's stuck inside, she reads up on research instead. Lately she's been reading a lot."
            kevin normal "So her knowledge is mostly theoretical?"
            him normal "Not at all; she and Thuc have a thriving farm. They are experts in fertilizer and waste reclamation, which is more interesting than you might think once you get past the 'yuck' factor."
            zaina normal "Okay, good to know."
            $ met_nguyen = True
        "Pete, the cattle rancher librarian." if (not met_jennings):
            $ mavericks += 1
            $ bios.activate("Travis")
            $ bios.activate("Pete")
            $ bios.activate("Helen")
            him normal "You should ask Pete! He and Helen are always trying new things with their cattle herds."
            kevin normal "Has he published his research?"
            him surprised "Uh, no, not really, but he'll tell you all about it if you let him."
            kevin sad "If knowledge is not written and catalogued, it will be lost."
            him normal "Yeah, that's kinda true, but who has time for that? Speaking of writing, though, he also runs the library, so if you're looking for a tool or research or need to fabricate something, he can help you out there."
            zaina happy "That would be great! I've been trying to fix this oven door handle but I really think I just need a new part."
            $ met_jennings = True

    him normal "If you want, I'll introduce you next time we get together."
    zaina normal "You know, I would really appreciate that. Everyone's so spread out, and we don't get together very often -- I feel like it's taking forever to get to know everyone."
    kevin happy "Thank you, [his_name]."
    return


# Year 4, 2 years old
# Show off at the Fall Festival or increase the size of your farm?
label work4:
    nvl clear
    pavel_c "The Fall Festival will be next weekend! Show off your best crops and animals. There will be games and music, too!"
    sara_c "I hope everyone can come! {emoji=happy}"
    nvl clear
    him "Hmmm... I was going to get a new field ready to expand the size of my farm, but I always like to go to the Fall Festival..."
    $ random_crop = farm.crops.random_crop(include_animals = False)
    $ work4_showoff = False
    menu:
        "What should I do?"
        "Show off my [random_crop] at the festival.":
            $ work4_showoff = True
            "It would be fun to show off my hard work. And it was a good chance to hang out with the other farmers and see what they were doing."

        "Prepare one field and then go without bringing anything.":
            "I didn't want to miss the Fall Festival. I worked hard to prepare and plow one new field, and then I headed over."
            $ modify_farm_size(1)

        "Don't go. Expand fields instead." if (farm_size < FARM_SIZE_MAXIMUM):
            "The festival was fun, but my farm was more important. Maybe I'd go next year..."
            "I worked hard to rip out the native vegetation and plow the new fields."
            $ modify_farm_size(2)
            return

    scene community_center with fade
    show natalia normal at quarterleft
    show pete normal at center
    show thuc normal at quarterright
    show goat at right
    with dissolve
    show him normal at left with moveinleft
    "Everyone brought their best crops to display."
    "Natalia had beautiful ears of corn, and even some samples of popcorn."
    show him surprised at midleft with move
    "Pete brought several kinds of cheeses and cider."
    show him normal at midright with move
    "Thuc brought the cutest baby goat I've ever seen. His daughter had taught it to stand on its hind legs, bleat, and jump through a hoop."
    thuc "This goat is almost as smart as [kid_name]!"
    him happy "And probably more obedient!"

    if (work4_showoff):
        thuc happy "Hey, are those your [random_crop] on display over there?"
        him normal "Yeah!"
        thuc normal "They turned out really well. How often do you fertilize them?"
        "We talked about [random_crop] for a while, and then I had an idea."
        him surprised "Hey, do you want to grow your own [random_crop]?"
        thuc normal "You'd help me get started?"
        him normal "Yeah!"
        thuc happy "Sure, that would be great. Do you want a strawberry plant?"
        him surprised "Strawberries?"
        thuc normal "Yeah, they're pretty easy and they come back every year so they don't take much work. We don't usually get a lot of them but the kids love them."
        him happy "Sure, thanks!"
        $ enable_crop("strawberries")
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
    him normal "Here, I'll carry the bucket. You carry the seeds."
    kid annoyed "No! I want to carry the bucket!"
    "She staggered a few steps with the bucket and it dropped, spilling half the water onto the ground."
    him annoyed "Let's try that again..."
    kid sad "Okay..."
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
    $ competence += 2
    $ achieved("Carbon Copy")
    "You can now choose how much [kid_name] helps on the farm. Her effectiveness depends on her {color=#ff0}competence{/color}."
    "Her competence increases as she learns and helps."
    window hide
    scene black with fade
    return

# Year 8, 4.8 years old
# The outhouse is full...
label work8:
    play music working
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
            "I'd spread this on my depleted fields so they would have more nitrogen each year." # this leads to +5 nitrogen in every square that lost it each year

    scene farm_interior with fade
    show her normal at midright
    show kid normal at center
    with dissolve
    show him concerned sweat at midleft with moveinleft
    her concerned "You look beat. And you smell like..."
    kid surprised "Like poop!"
    him determined "Yeah... the outhouse was full."
    her surprised "Oh! I guess that would happen eventually..."
    if (work8_choice == "clean"):
        him concerned sweat "I mucked the whole thing out."
        kid angry "Gross!"
        her concerned "Wow... that sounds awful."
    else:
        him concerned sweat "I had to build a new one."
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

    if ((work8_choice != "improve") and (get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        "Since I only spent one day on the outhouse, I had enough time to prepare some more space for future crops."
        $ modify_farm_size(2)
    return

# Year 10, 6.2 years old
# Bees?!
label work10:
    scene community_center with fade
    show kevin normal at midright
    show him normal at midleft
    with dissolve
    if (crop_enabled("plums") or crop_enabled("plums+")):
        kevin normal "[his_name]. How are your plum trees?"
        if "plums+" not in farm.crops:
            if "plums" in farm.crops: # we just barely planted plums, but it didn't work.
                him concerned "I tried to plant them a couple weeks ago, but they didn't germinate. It had probably been too long."
                kevin sad "Yes, that is possible."
            else:
                him concerned "I, uh, I'm afraid it didn't work out."
                kevin sad "I see."
            $ disable_crop("plums")
            $ disable_crop("plums+", False)
        else:
            him happy "Pretty good! We're even starting to get a few plums on them."
            kevin happy "That is good."

    him surprised "How's your garden coming, Kevin?"
    kevin normal "It does provide some food, but I have noticed that plants here have an average of a 25\% smaller yield than plants on Earth."
    him concerned "There could be several reasons for that..."
    kevin sad "After factoring out other issues such as soil quality, solar flares, and unreported crops, I have come to a conclusion."
    him surprised "What's that?"
    kevin normal "We need more pollinating insects. The native fauna of Talaam have not evolved to pollinate our plants."
    him normal "Like bees?"
    kevin happy "Precisely. Several colonies of bees are arriving on the next shuttle. I fear it is too many for my small garden. Would you be willing to reserve some land for them on your farm for 100 credits?"
    him surprised "Why wouldn't I want bees?"
    kevin sad "They do take a certain amount of upkeep and space every year."

    menu:
        "What should I say?"
        "Sure, I'd love bees!":
            $ modify_credits(-100)
            him happy "I'd love bees! Better pollination, honey, that sleepy buzzing sound on summer afternoons..."
            kevin normal "Very well. I shall mark you down for bees."
            $ enable_crop("honey")
            tutorial "Bees will boost production of neighboring squares and require just a little work."
            tutorial "However, you have to allocate a space for them every year."
            $ achieved("Family Beeswax")
        "No thanks.":
            him concerned "No thanks; I already have enough to worry about."
            kevin normal "Very well. I shall ask someone else."
    him surprised "Is that everything?"
    kevin sad "What about other garden helpers? Worms, ladybugs, pill bugs..."
    "I remembered George, the giant millipede thing that loved feeding on our compost pile, and how surprised [her_name] and I were to find him in the house."
    him normal "Well, Talaam already has giant millipede creatures - if you have a compost pile you'll see them eventually. Worms came with us from Earth in our compost -- we figured we'd need them and the bacteria."
    kevin normal "I see."
    him concerned "As for ladybugs -- that might be worth looking into. I wonder if they'd eat those corn pests we had a few years back. Though probably wasps would be better, since they had pretty tough armor."
    kevin sad "It might be difficult to convince others to bring wasps here."
    him happy "True; ladybugs have a much better reputation!"
    return

# Year 12, 7.4 years old
# Brennan's GMO sterile wheat
label work12:
    scene farm_interior with fade
    show him determined at center with dissolve
    nvl clear
    brennan_c "I have a special offer for all you farmers out there."
    julia_c "Oh, this'll be good."
    sara_c "{emoji=surprised}"
    pete_c "Let the man talk."
    brennan_c "I have the newest pest-resistant, high-yield, nutrient-packed wheat seeds from Earth. They grow fast, they don't need much water, and they can thrive in almost any climate."
    thuc_c "That sounds good, but..."
    julia_c "What's the catch?"
    brennan_c "Well, the seeds are patented. We put a lot of work into creating this variety and we can't have everyone distributing them."
    julia_c "Meaning we couldn't save seeds to plant next year."
    brennan_c "Right; they're sterile. You'd need to buy seeds each year from me. Well, from RET, really."
    if (community11_kidsonfarm):
        natalia_c "Hmm, I might get some for Joanna to try. If they're as good as you say..."
    else:
        natalia_c "Hmm, I might have to try those, if they're really as easy to grow as you say..."
    brennan_c "They are! You'll need to sign a 20 year contract. We have a set amount and we need reliable buyers."
    natalia_c "Twenty years? Some of us might not even be alive then."
    brennan_c "Twenty Talaam years. More like 12 Earth years. You'd agree to pay us [WHEAT_COST] credits every year and we'll provide you with two fields' worth of seeds."
    julia_c "That's ridiculous. Who would want to rely on you for their seeds?"
    brennan_c "You're a tough customer, Julia; I love that about you! But let's let everyone decide for themselves. Come see me if you want in on this great deal."
    nvl clear
    "I could almost smell fresh-baked bread. I knew the wheat would sell well... but I didn't like the idea of relying on Brennan for seeds."
    menu:
        "What should I do?"
        "Sign a wheat contract.":
            $ miners += 1
            scene mine with fade
            show brennan normal at midright with dissolve
            show him determined at midleft with moveinleft
            him determined "I'm interested in the wheat."
            brennan flirting "Good, good. Seems like you're smarter than you look."
            him annoyed "Don't make me change my mind."
            brennan normal "Ah, can't you take a joke?"
            him determined "..."
            brennan concerned "...Right. Here's your wheat seeds."
            $ enable_crop("wheat")
            # you sold your soul but can now grow wheat.
        "Don't sign a wheat contract":
            $ mavericks += 1
            him_c "No thanks, Brennan."
            "Later, Natalia came over for a visit."
            scene farm_interior with fade
            show him normal at midright
            show natalia normal at midleft
            with dissolve
            natalia angry "What do you think of the wheat?"
            him determined "I don't like the idea of Brennan controlling anything more than he has to."
            natalia happy "Ha! True enough. I need {b}something{/b} for my farm that's easier to grow. Do you have any suggestions?"
            him surprised "You've been growing corn, right?"
            natalia angry "Yes, and it's quite time-intensive."
            him normal "Have you tried potatoes?"
            natalia normal "No, do they do well here?"
            him determined "As long as you keep them dry, they're great! Do you want some seed potatoes to get started?"
            natalia happy "Yeah, it's something different, anyway! I have seed corn, if you want to exchange."
            him normal "It's a deal."
            $ enable_crop("corn")

    "I was looking forward to growing something new."
    if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        "I had a little extra time on my hands and decided to prepare some more land for crops."
        "Both my family and the colony were growing larger and demanding more food than ever."
        $ modify_farm_size(1)
    return

# Year 14, 8.7 years old
# Milking Goats
label work14:
    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    "I never realized how much I knew about farming until I had to teach someone else."
    "Even though she grew up on our farm, there was still so much [kid_name] didn't know."
    $ parenting_style = get_parenting_style()
    if (parenting_style== "authoritative"):
        "...but she's learning fast!"
        "I love seeing her grow more independent. When she's done feeding the goats, she doesn't sit around waiting for me to tell her what to do."
        "She looks around and starts doing whatever is needed, whether it's a fence that needs repairing, weeds that need to be pulled, or produce that needs to be harvested."
        "Sometimes she's a little too independent."
        kid happy "I want to milk the goats!"
        him surprised "You do?"
        kid normal "Yeah! I bet I can do it all by myself!"
        "She'd watched me many times, but the technique is a little tricky."

    elif (parenting_style == "authoritarian"):
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
    show him normal behind goat at midleft
    show kid normal at midright
    with moveinleft
    "I showed her how to lead the goat to the milking stand, wash off her udder, and set up some food for her."
    show kid surprised with dissolve
    "I helped her practice the finger motions needed to squirt the milk into the bucket."
    "She was tentative at first, but she seemed to be figuring it out."
    scene fields with fade
    "I left for a minute to check on something, but I wasn't gone for more than five minutes when I heard a scream."
    scene barn with fade
    show goat at center
    show kid cry at midright with dissolve
    show him concerned at midleft behind goat with moveinleft
    "I dashed back into the barn and saw [kid_name] crying, the bucket tipped over, and the goat lying down, looking quite satisfied."

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
            "I showed her how to put an upside-down bucket under the front of the goat so she couldn't just lie down."
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
            "We lost a little milk, but it was worth it to have [kid_name] be able to help with milking the goats."

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
                    him determined "It's your job to milk this goat."
                    hide him with moveoutright
                    "I left to finish up my work. Her sobs followed me around the farm everywhere I went."
                    "I wanted to teach her to be independent, to do things for herself. I guess I needed to push her a bit to get her to learn that..."
                    scene barn with fade
                    show him pout at center with moveinright
                    "When I came back after a half hour, the goat was put away and there was about a cup of milk in the pail. The goat looked happy, so she must have been milked enough."
                    "But [kid_name] was going to need a lot more practice..."
                    $ authoritarian += 1
                "Leave if you're not going to help.":
                    him annoyed "If you're not going to help, then get out of my way."
                    kid cry "Fine, I will!"
                    hide kid with moveoutleft
                    "I ended up just doing it myself. It wasn't that hard; maybe [kid_name] just wasn't old enough..."
                    $ neglectful += 1
    "Maybe I'd wait awhile before teaching her how to trim the goats' hooves..."
    return

# Year 16, 10 years old
# Seed exchange or increase size of farm
label work16:
    nvl clear
    sara_c "There will be a seed exchange this weekend! Bring some seeds to trade! {emoji=yum}"
    natalia_c "I'm bringing chile seeds - they're a little bit sweet and a little bit spicy!"
    kevin_c "I plan on bringing some plum pits."
    pavel_c "Wonderful! I hope everyone will participate."

    $ random_crop = "wheat"
    while (random_crop == "wheat"): #this won't go forever because you can only grow 2 fields of wheat
        $ random_crop = farm.crops.random_crop(include_animals = False)
    "A seed exchange could be good; I could share my great [random_crop] and get something new to plant in the future."
    "But Pete was already planning to come over and fence a new section of land for farming."
    "Last week I helped him expand his cattle paddock with a bigger fence and he was planning to return the favor."
    menu:
        "What should I do?"
        "Go to the seed exchange.":
            him_c "I'll be there, too!  I'm bringing [random_crop]!"
            sara_c "Oooh, great! {emoji=happy}"
            nvl clear
            scene community_center with fade
            show pavel normal at quarterleft
            show sara normal at midleft
            show natalia normal at center
            show kevin normal at quarterright
            show zaina normal at right
            with dissolve
            show him normal at left with moveinleft
            "There were a lot of people at the seed exchange!"
            pavel "Welcome, [his_name]! Good to see you!"
            him normal "Thanks. Where should I put these?"
            sara "There's an empty spot on the table there. Oh, you brought a sign. Perfect."
            $ colonists += 1
            hide sara
            hide pavel
            with moveoutleft
            show him at midleft with move
            him surprised "You said your chile peppers are spicy and sweet?"
            natalia happy "Oh yes. If you pick them green, they're a little bitter and more savory. If you wait until they turn red, they're sweeter. But the spiciness is the same either way."
            him normal "Sounds very flavorful!"
            kevin sad "[his_name], I was thinking about growing [random_crop]? Would you recommend it to me?"
            menu:
                "Would I recommend [random_crop]?"
                "Yeah, you'll like them!":
                    him happy "Yeah! You'll love them."
                    kevin happy "Then perhaps I shall try planting some."
                "No, you should try something else.":
                    him concerned "I'm not sure they're the best crop for you..."
                    kevin normal "Really? Why do you say that?"
                    menu:
                        "What should I say?"
                        "They're too much work.":
                            him annoyed "They're too much work, especially for the yield you get."
                            kevin happy "Nevertheless, I would like to try it."
                        "They don't really taste good.":
                            him concerned "Well, they don't really taste very good, so no one wants to eat them."
                            kevin happy "I like [random_crop]."
                            him surprised "Well, maybe they'd be good for you."
                        "They're not worth very much.":
                            him concerned "They don't sell for very much, so unless you love eating them yourself it's probably not worth it."
                            kevin happy "I like [random_crop]."
                            him surprised "Well, maybe they'd be good for you."
                        "They're not very nutritious.":
                            him annoyed "They just aren't that nutritious. Not many vitamins and minerals."
                            kevin sad "Oh. I had not considered that."

            if (not ((crop_enabled("plums") or crop_enabled("plums+")))):
                him surprised "You don't mind if I take a few plum pits, do you?"
                kevin normal "Please do. They are hardy and productive plants."
                $ enable_crop("plums")
                him happy "Great! I love fruit."
            else:
                "Kevin took some of my seeds, and I decided to take some of the chile pepper seeds."
                natalia normal "You won't be disappointed!"
                $ enable_crop("peppers")

        "Expand your farmland." if (farm_size < FARM_SIZE_MAXIMUM):
            $ mavericks += 1
            "I had already worked everything out with Pete. I'd have to miss this seed exchange. Hopefully they'd have more in the future."
            scene fields with fade
            show him normal at midleft with dissolve
            show pete normal at midright with moveinright
            pete happy "You ready to make this fence?"
            him determined "You bet!"
            "It took us all day, but now I had several more fields for planting!"
            $ modify_farm_size(3)
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
    if (year <= LILY_DIES_YEAR):
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
    him annoyed "I really wish you could see the solar flares during the day..."
    her normal "They're beautiful at night..."
    kid normal "Hey, what if there's not actually any solar flares, but they're actually doing top secret stuff and don't want anyone messing with it?"
    him surprised "What kind of top secret stuff would that be?"
    kid happy "I don't know; maybe aliens?? Or maybe they found some super valuable ore right under the school and they're blasting it away with dynamite right now!"
    her flirting "I don't think that is going to happen."
    bro concerned "There could be aliens though, right?"
    him determined "I think if there were aliens on Talaam they would have said hi by now. We've been here for years."
    kid shifty "Unless they're just watching us. To see if we're worth enslaving. And any day now, they'll come and attack us in our sleep!"
    show bro annoyed with dissolve
    "She tickled [bro_name] excitedly. He flinched and tried to push her hands away."
    bro sad "Stop!"
    her annoyed "[kid_name]..."
    kid annoyed "What?! I'm just trying to play with him!"
    bro sad "I don't like that!"
    kid sad "Ugh, why do you hate me so much?!"
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
            "[kid_name] tried the whole time to convince me that her only work should be school work and it was unfair of me to make the kids do all the work, so I didn't get to concentrate much on my own work."
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
            kid annoyed "I hope I don't 'win'."
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

    if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
        "I finished faster than I thought, and I had time to prepare another field for planting."
        $ modify_farm_size(1)
    return

# Year 20, 12 years old
# Irrigation Trouble
label work20:
    play music problems
    scene fields with fade
    "With Talaam's frequent rains, we didn't need to irrigate the fields very often."
    "But we had a system of gates and canals we could open up to get extra water from the river when it didn't rain enough."
    "After a week with no rain, and no rain in the forecast, I decided to open up the gates and let in some mountain river water."
    scene irrigation with fade
    show him normal at center with moveinleft
    "But when I got there, the river was so low that barely any water came into the canal."
    him surprised "Where'd all the water go?"
    "I followed the river upstream to Thuc's farm."
    scene irrigation flip with fade
    show thuc sad at midright with dissolve
    show him determined at midleft with moveinleft
    him surprised "The river is low here, too."
    thuc sad "Yeah, I went to flood the fields and there was nothing left."
    $ work20_thuc_present = False
    menu:
        "What should I say?"
        "Let's check it out.":
            him determined "I'm going to check it out. Come with me if you want."
            thuc normal "I was just going to tell you the same thing."
            $ work20_thuc_present = True
        "Did you use all the water?":
            "Thuc's irrigation techniques are a bit different from mine, since he grows different crops. His require a lot more water because they need to be flooded."
            him annoyed "Did you use all the water?"
            thuc sad "No more than usual."
            him determined "Huh. Well, I'm going to go check it out."

    "I headed farther upstream, past the town, and up into the hills. While passing the dam that Kevin had fixed a few years ago, I saw it seemed to be holding up."
    scene canyon with fade
    show him determined at midleft
    if (work20_thuc_present):
        show thuc normal at left
    with moveinleft
    "Further upstream I arrived at the diversion for farming water. There wasn't much water there, either. Finally, I reached the miner's camp."
    scene mine with fade
    show brennan normal at midright with dissolve
    show him determined at midleft
    if (work20_thuc_present):
        show thuc sad at quarterleft
    with moveinleft
    "At the camp, it was obvious what had happened. Much of the river had been diverted to give water for the mining machinery."

    him annoyed "First you contaminate our water, now you're stealing it?! There's none left for our crops downstream!"
    brennan concerned "Our refining processes use a lot of water. The new site needed water, so the river flows over here now. Sorry."
    him angry "Sorry? SORRY?! \"Sorry\" isn't going to make food grow out of the ground!"
    if work20_thuc_present:
        thuc sad "Well, who knows? Maybe we can eat what they're making up here?"
    brennan surprised "You'll have to get your water from somewhere else."

    menu:
        "What should I say?"
        "YOU need to get YOUR water elsewhere.":
            him annoyed "No, YOU need to get YOUR water from somewhere else! This is farming water!"
            if work20_thuc_present:
                thuc normal "We depend on having easy access to water to grow all our crops."
            brennan angry "Sorry, I have my orders."
        "(Say nothing)":
            show him pout with dissolve
            "I took a deep breath and just looked at him. He looked back into my eyes with a stubborn expression on his face, and an uncomfortable silence stretched between us like a yawn."
            "I realized I had some other options here."
            menu:
                "What should I say?"
                "Let's work something out.":
                    him concerned "We don't have to fight about this."
                    brennan angry "Good. Then leave us alone."
                    him determined "I know you all want to eat, and I don't want to interfere with your mining--"
                    if (miners >= 10):
                        brennan sad "[his_name]..."
                        if (work20_thuc_present):
                            him determined "It's not just about me and Thuc right now. It's about our whole community."
                        else:
                            him determined "It's not just about me. It's about our whole community."
                        brennan concerned "Look, I understand what you're saying, [his_name]. Obviously you need water. But my hands are tied."
                    else:
                        brennan angry "Yeah, right. You've done nothing but work against me since I got here."
                        him angry "It's not about you!"
                        brennan sad "I know you hate what RET's doing here, and you're just looking for excuses to stop us. Go complain somewhere else."

                "Can you please just wait until it rains?":
                    him concerned "If you can hold off on your operations just until it rains, then I think we can manage."
                    brennan angry "Sorry, [his_name], but I have my own deadlines."

        "Food is more important than mining!":
            him annoyed "Food is more important than mining!"
            brennan angry "Without this mining, you wouldn't be here at all."
            him concerned "Without food, none of us will be here very long."
            brennan sad "Then we'll all have to box the devil."
            him surprised "What?"
            brennan angry "We'll all just have to make do, won't we?"
    hide brennan with moveoutright
    "I left when it was clear nothing would be accomplished."
    if (work20_thuc_present):
        thuc normal "Sorry, [his_name]. We tried..."
        him determined "I'm not done yet."
    scene farm_interior with fade

    if (miners_strong()):
        nvl clear
        him_c "Brennan, if we both explain to RET why the farmers need that water, I'm sure they'll understand."
        brennan_c "...If you can get them to authorize a deadline extension, then I can help you."
        "Together, we composed a careful message to RET with our limited characters."
        nvl clear
        him_c "The water miners are using is needed to ensure crops survive. Brennan and I plan to treat and redirect water post-mining back to farm. Please authorize deadline extension."
        ret_c "Extension authorized. Proceed with plan."
        nvl clear
        "Thuc and I helped Brennan redirect the water back to the original river route after going through water treatment."
        "I breathed a sigh of relief as water flooded through the gates to my crops again."
        return

    else:
        "There was nothing I could say to change Brennan's mind."
        "But there had to be something I could do besides watch my crops dry up..."
        menu:
            "What should I do?"
            "Search RET's legal documents":
                "It sounded about as fun as giving myself a root canal with a backhoe."
                "But if I could find some legal description of how the water was supposed to be shared, Brennan would probably honor it."
                "And I knew just the person to ask for help."
                scene storeroom with fade
                show ilian normal at midright with dissolve
                show him determined at midleft with moveinleft
                him determined "Hey there, Ilian!"
                ilian angry "Hi. What do you need? Oil? Salt? Sugar?"
                him annoyed "I'm not here for supplies. I need help with legalese."
                ilian normal "So... why are you here?"
                him normal "You read up on the contract we signed with RET and you didn't even have to. I'm looking for some legal protection for water rights, and I hope there's something in a legal document about it."
                ilian happy "We're fighting over water rights now? Isn't that just like an old Western..."
                him determined "This is serious! My crops are dying! I won't have anything left for the storehouse if this keeps up!"
                ilian angry "Fine, we can take a look."
                "Ilian knew right where to find the documents, so we were already ahead of what I knew."
                ilian normal "Hmmm, water protection, water wildlife, water treatment..."
                ilian happy "Aha! Water diversion...water may be diverted no more than two kilometers... water must be treated after mining use... farmers may be required to modify water distribution to accomodate..."
                him concerned "That doesn't sound good."
                ilian normal "If you can prove he diverted the water more than two kilometers, you have a chance. Otherwise, you're supposed to modify your systems to accomodate for his water diversion."
                him sad "I don't think it's more than two kilometers..."
                ilian angry "Why am I not surprised?"
                him determined "Thanks anyway."
            "Ask RET for help":
                "This was exactly the kind of thing we needed a liaison for."
                if (is_liaison):
                    "And I guess that meant it was up to me to talk to RET about it."
                    "I'd better think carefully about what message to send to Earth. I had 140 characters to use on the quantum entanglement device."

                    $ work20_message = ""
                    $ work20_message_score = 0
                    $ work20_menuset = set()
                    menu work20_message_menu:
                        set work20_menuset
                        "RET Message:\n[work20_message]"
                        "River diverted for mining":
                            $ work20_message += "River diverted for mining "
                            jump work20_message_check
                        "No notice was given":
                            $ work20_message += "No notice was given "
                            $ work20_message_score += 1
                            jump work20_message_check
                        "Brennan refused to help":
                            $ work20_message += "Brennan refuses to help "
                            jump work20_message_check
                        "No water for crops":
                            $ work20_message += "No water for crops "
                            $ work20_message_score += 1
                            jump work20_message_check
                        "Brennan stole our water for mining":
                            $ work20_message += "Brennan stole our water for mining "
                            jump work20_message_check
                        "Tried to negotiate with Brennan":
                            $ work20_message += "Tried to negotiate with Brennan "
                            $ work20_message_score += 1
                            jump work20_message_check
                        "Water is vital for growing food":
                            $ work20_message += "Water is vital for growing food "
                            jump work20_message_check
                        "Please help":
                            $ work20_message += "Please help "
                            jump work20_message_check
                        "Mining water needs to return":
                            $ work20_message += "Mining water needs to return "
                            $ work20_message_score += 2
                            jump work20_message_check
                        "I noticed there was no water":
                            $ work20_message += "I noticed there was no water "
                            jump work20_message_check
                        "I followed the river upstream":
                            $ work20_message += "I followed the river upstream "
                            jump work20_message_check
                        "I talked with Brennan":
                            $ work20_message += "I talked with Brennan"
                            jump work20_message_check
                        "(Finish)":
                            jump work20_message_done

                    label work20_message_check:
                        if (len(work20_message) >= 100):
                            menu:
                                "It's getting pretty long... Is this message good?\n[work20_message]"
                                "Yes, send it.":
                                    jump work20_message_done
                                "No, start over.":
                                    $ work20_message = ""
                                    $ work20_message_score = 0
                                    $ work20_menuset = set()
                                    jump work20_message_menu
                        else:
                            jump work20_message_menu

                    label work20_message_done:
                        him_c "[work20_message]"
                        "After several hours, I still had no response. I finally looked up the Earth timetable and realized it was the middle of the night there."
                        "Finally, a response came back."
                        if (work20_message_score >= 3):
                            ret_c "If Mr. Callahan did not give prior notice to redirection, he must ensure outflow goes back to river. Otherwise, you must work out alternative water source."
                            "That was exactly what I was hoping for."
                            "Brennan griped and complained, but once he put some miners working on it, the water came back quickly."
                            "I breathed a sigh of relief as water flooded through the gates to my crops again."
                            return
                        else:
                            ret_c "Mr. Callahan justified. You must work out alternative water source."
                            "I tried to explain how important it was, but they wouldn't budge."
                            jump work20_other_water

                else:
                    "So I asked Sara to send RET a message about it."
                    sara_c "No water for your crops?! That's awful! {emoji=sad} I'll ask."
                    him_c "Did you hear back from RET yet?"
                    sara_c "They said you need to work out an alternative water source."
                    him_c "What?!"
                    sara_c "I'm sorry, [his_name]; apparently Brennan is allowed to divert the river for mining. {emoji=grimace}"

            "Get more farmers involved":
                "This wasn't just my problem. We needed all the farmers to be united in this."
                "But it was harder than I thought."
                "Some had more drought-tolerant plants and weren't worried. Others sourced their water from underground instead of the river."
                "At least Thuc was on my side."
                jump work20_other_water

        "Since RET wouldn't help, I'd just have to find some other way of getting the water I needed."
        label work20_other_water:
            scene farm_interior with fade
            show him determined at midright
            show thuc sad at midleft
            with dissolve
            thuc "So, our only options are to either build wells and pumps, or build a canal from where Brennan diverted the water to?"
            him sad "That's the way I see it."
            thuc normal "The water table is high enough here that we could probably just build a well."
            him concerned "Yeah, with a windmill pump, and a pond for storage. Just like the one on my grandpa's farm..."
            thuc happy "Sounds like a plan!"
            scene irrigation with fade
            show him determined at midright
            show thuc sad at midleft
            with dissolve
            "We got approval for the materials and started construction."
            "It was tough work digging the well, even with the auger tractor attachment. The auger was only meant for post holes, but we made some extensions so it would be long enough to drill a well."
            "Our first windmill wasn't centered or level, so we ended up having to take it apart and put it back together again."
            "Digging the pond wasn't tricky, just a lot of hard work."
            if colonists_strong():
                "When the other farmers heard about what we were doing, some of them came by to lend a hand."
            elif mavericks_strong():
                show pete normal at quarterleft with moveinleft
                "When Pete heard about what we were doing, he came by to lend a hand."
                pete "See, that's why you should quit working for the Man and come live out on your own, like me!"
                hide pete with moveoutleft
            show him sleeping with dissolve
            "When the water came rushing out onto my fields again, my shoulders finally relaxed for the first time in days."
            him happy "Yeah!"
            thuc happy "Nice!"
            him normal "This would have been ten times harder to do on my own... thanks for working with me, Thuc."
            thuc normal "Anytime. I think we work pretty... WELL together."
            him happy "Yeah, once we got started, things really FLOWED smoothly."
            thuc sad "Without all this, our crops would have suffered a lot of DAMage."
            him determined "I could sit here and PONDer this all day..."
            thuc normal "So WATER you going to do now?"
            him normal "WATER get back to work, I guess."
            thuc sad "That one's a bit of a stretch."
            him surprised "WATER, as in 'We oughtta'? W'otta? You don't think it works?"
            thuc normal "Nope, sorry. It... SINKS."
            show him laugh with dissolve
            "We managed to keep most of our crops from dying, but they probably wouldn't yield as much this year."
            $ modify_credits(-100)
    return

# Year 22, 13.6 years old
# A surprise 40th birthday party
label work22:
    play music problems
    scene community_center
    show night_overlay
    with fade
    show him determined at left behind night_overlay with moveinleft
    him determined "Why did [her_name] want to meet me here? It makes no sense..."
    him annoyed "And the lights are off, which means she's not even here...?"
    hide night_overlay with dissolve
    show her laugh at quarterleft
    show pete happy at midright
    show thuc happy at center
    show sara happy at quarterright
    show ilian happy at right
    show oleg normal at right
    show bro happy at center
    show kid happy at midleft
    with moveinbottom
    play music exciting
    "Everybody" "Happy Birthday, [his_name]!"
    him surprised "Whoa! What are you guys all doing here in the dark??"
    her happy "Waiting for you, silly! You were supposed to be here fifteen minutes ago!"
    him normal "Sorry, I didn't know this was a time-limited event. Is it really my birthday?"
    her normal "It is on Earth. You'd be--"
    him flirting "--old enough that my age is boring. I can't believe you got all the awesome people in one place at the same time for my birthday."
    her concerned "Well, Brennan and Julia couldn't make it."
    him happy "Like I said, all the awesome people are here!"
    kid laugh "You looked so surprised."
    bro normal "Did you even know we were here?"
    him normal "Nope! You were like stealthy birthday ninjas!"
    "The kids ran off to the a table covered with a variety of foods -- looks like [her_name] organized a potluck. I made a mental note to visit it very soon."
    hide bro
    hide kid
    hide oleg
    with moveoutleft
    show him at midleft with move
    him happy "Thanks for coming, Thuc!"
    thuc normal "I'll come to a party anytime. So is it true? Is this the big Four Oh?"
    him surprised "Um, maybe? I don't really keep track of my age, plus we spent that year on the shuttle that only felt like several months, so..."
    sara normal "Well, the colony database says you're 40, so I think it counts!"
    thuc sad "Don't worry; being 40 isn't so bad."
    him normal "You would know, huh?"
    thuc normal "It's 50 you have to worry about!"
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
            show oleg normal at right with moveinright
            her surprised "Oleg, I heard you're getting to be quite the programmer! What's your latest project?"
            oleg "Uh, not much."
            sara normal "It's okay; tell everyone about your game."
            thuc happy "You made a game?"
            oleg "Not really. I mean, kind of. It's not very good."
            sara happy "It's pretty fun! It's like a farming game, except that everything's underground and you have to protect crops from monsters and craft UV lights and sprinkler systems and stuff."
            oleg "It's not finished yet..."
            him happy "That sounds awesome. I'd like to play it when you're done."
            oleg "O-okay."
            $ oleg_points += 1
        "A midlife crisis sounds funny.":
            him happy "No, it's funny! Go ahead, tell me what you think I'll do."
            pete angry "You don't strike me as a flashy car kind of guy..."
            ilian angry "Anyway, those are currently in dismally short supply."
            if (is_liaison):
                sara normal "You're already the RET liaison, so you don't need to seek a position of power."
            else:
                sara normal "Maybe he'll seek a position of power in the community? Run for mayor?"
                pete happy "Pavel'd better watch out."
            if (get_extra_work() <= 0):
                thuc happy "He is kind of a workaholic..."
            else:
                thuc happy "Maybe he'll become a workaholic and we'll never see him around."
                ilian angry "We already don't see him around."

            pete normal "Maybe he'll run off and have a wild fling with a hot alien chick."
            sara sad "Uh, wow, where did that come from?"
            him surprised "Wait, there's hot alien chicks here? Where?"
            if has_strong_marriage():
                thuc normal "No way. You're so obssessed with [her_name], even if there were I don't think you'd notice."
                him flirting "I already have all the hot alien chicks I need."
                her surprised "You do?"
                him happy "Oh yeah. You're on a planet that's not Earth, so you're an alien. And all I need is you."
                show him at quarterleft with move
                show her sleeping with dissolve
                "I kissed her, right in front of everybody."
                show him at midleft with move
                sara normal "Awwwww! Sweet cheese!"
                her flirting "It's not cheesy if it's true, right?"
                pete happy "Nope. It's still cheesy."
            else:
                her concerned "I guess I'm lucky we haven't encountered aliens yet."
            sara normal "What about music? Maybe he'll start a punk metal band."
            her normal "He does write some pretty hardcore poetry..."
            him happy "Nah, I'm a terrible singer."
            sara happy "You might not have a midlife crisis."
            him normal "I'm not planning on it!"

    hide thuc
    hide sara
    hide pete
    hide oleg
    hide ilian
    with dissolve
    "I finally got to make my way over to the snacks. Pete had brought two kinds of cheeses, and Ilian had dug a few tiny pieces of chocolate out of the storehouse."
    "There were fresh fruits and vegetables and even some soft, homemade, whole wheat bread with jam and butter."
    "I savored every bite."

    show him normal at center
    show her normal at midleft
    with move
    him surprised "Did you plan all this?"
    her surprised "Well, I had the initial idea, but I had a lot of help from your friends."
    $ helping_faction = strongest_faction()
    if (helping_faction == "colonists"):
        show thuc normal at quarterright with moveinright
        her happy "Especially Thuc!"
        thuc happy "If I don't embarrass you for turning 40, who else will?"
        her flirting "I don't know; he's pretty good at embarrassing himself."
        him flirting "Hey, shouldn't you be a little nicer to me on my birthday?"
        show her normal with dissolve
        thuc normal "Which reminds me... I brought you a little something."
        him surprised "You did?"
        if crop_enabled("onions"):
            thuc happy "Yeah, I brought you some turnip seeds. They're not worth much because nobody likes them, but maybe you'd have a use for them?"
            him concerned "Ummm... maybe?"
            thuc sad "Sorry; it's the only thing I could think of that you didn't already have."
            him happy "No, this is great! I love more variety. Thanks, Thuc."
            $ enable_crop("turnips")
        else:
            thuc sad "Try not to tear up... I brought you this bag of onions."
            him sad "Oh, Thuc. They're so beautiful. I just can't help crying!"
            her concerned "..."
            thuc normal "You can plant them if you want."
            him cry "I will; thank you! Thank you so much!"
            $ enable_crop("onions")
    elif (helping_faction == "mavericks"):
        show pete normal at quarterright with moveinright
        her happy "Especially Pete!"
        pete happy "I thought you'd get a kick outta a surprise party."
        him happy "Yeah, it's awesome!!!"
        pete normal "I also wanted to give you these."
        him surprised "What kind of seeds are these?"
        pete happy "Broccoli."
        her surprised "Do you like broccoli a lot?"
        pete normal "How're we gonna raise decent kids if they don't learn to eat their broccoli?"
        her laugh "So true! And it has a lot of vitamin C, too."
        him happy "Great, thank you Pete! It's always good to have some more variety."
        $ enable_crop("broccoli")
    else:
        show chaco normal at quarterright with moveinright
        her happy "Especially Chaco!"
        "He didn't say anything, but a slight smile tugged at the corner of his mouth."
        "Coming from Chaco, that was like a big bear hug."
        chaco sad "Here."
        "He handed me some credits."
        him happy "Oh! Wow. Thank you, Chaco; this is a very generous gift!"
        chaco "Wanted to thank you."
        $ modify_credits(50)
    $ achieved("Over the Hill")
    return

# Year 24, 14.8 years old
# Tractor accident
label work24:
    "[kid_name] was big enough to do real work on the farm, now. She could help a mama goat give birth, knew which plants were weeds, and could build a fence out of almost anything."
    "But her favorite way to help was driving the tractor."
    scene fields with fade
    show tractor at midleft
    show him normal at midleft
    show kid normal at midright
    with dissolve
    "We were using the front loader attachment to add manure and to the fields."
    kid nervous "Please let me do the driving, dad! I know how to do it!"
    him annoyed "You haven't driven with the front loader attachment. The feel is totally different."
    kid annoyed "Well, how am I going to learn about it if you don't let me try it?!"
    "She had a good point. It wasn't really something you could learn just by watching."
    "But I wanted to keep her safe, too."
    him determined "I'll do the first run while you rake the manure into a pile. Then I'll decide if you can drive."
    kid concerned "Ugh. Fine."
    show kid at left with move
    show tractor at quarterright
    show him determined at quarterright
    with slowmove

    "I filled the front loader full of manure and drove down to the field we were preparing. I slowed down to turn to the side, and dumped the load on top of the dirt."
    "Then I drove back."
    show tractor at quarterleft
    show him at quarterleft
    with move
    him normal "Your turn. Watch out for the ditch on the side."
    show him at left with move
    show kid annoyed at quarterleft with move
    kid annoyed "Of course, dad, it's only been there my whole life."
    "She got a load of manure into the bucket and headed down towards the field. The bucket was a lot higher than I usually put it."
    play music tense
    show tractor at center
    show kid shifty at center
    with move
    him annoyed "Lower the bucket!"
    kid surprised "What?"
    "She couldn't hear me. I started running, following the tractor."
    show tractor at midright
    show kid concerned at midright
    show him surprised at midleft
    with move
    him angry "The bucket's too high! Lower the bucket!"
    "I was too late. She turned the corner, going a little too fast. I felt like time slowed down as I started running. I could see the tractor starting to tip."
    show tractor at quarterright
    show kid at quarterright
    show him at center
    with slowmove
    "I reached out, but I was helpless to stop it. The high, heavy bucket dragged the whole tractor over onto its side."
    hide tractor with moveoutright
    show kid at right, sitting with move
    kid determined "Ahhhhhhh!"
    him surprised "[kid_name]! Dammit!"
    show kid nervous with dissolve
    show him determined at midright, squatting with move
    "I ran as fast as I could. [kid_name] was quiet, which worried me even more than if she had been screaming."
    "When I finally reached her, she was unconscious and her leg was pinned under the tractor. I bent over her face and felt her breath."
    him determined "[kid_name]! [kid_name], wake up!"
    "I could probably lift the tractor off her, but if she couldn't scoot herself out it was pointless."
    him angry "[kid_name]!"
    "She stirred."
    him determined "Come on, [kid_name]. You're going to be okay."
    "She tried to get up, but could only sit. Good, at least her spine was okay."
    kid sad "Wha-what? I can't - I can't move my leg!"
    him concerned "I know. It'll be okay. Now, on the count of three, I'm going to lift the tractor, and you need to get out of there, okay?"
    kid nervous "It hurts!"
    him sad "I know it hurts, but we gotta get you out of there. I don't know if your leg will move, so you might have to use your arms."
    kid nervous "Okay. Ow. Okay. I think I can do that."
    him angry "1...2...3!"
    "I heaved up and tilted the tractor. I couldn't tip it all the way back to standing, but hopefully it was enough..."
    him annoyed "Now, now, now! Out now!"
    show kid nervous at right, squatting with move
    kid angry "Okay! I'm doing it...I'm clear!"
    "I set the tractor back down as gently as possible, my arms shaking and aching."
    show him concerned at midright, standing
    show kid annoyed with dissolve
    with move
    "I looked down at my daughter. Her lower leg was bloody and her pants were ripped. She had a bump on her head from where she had hit the ground."
    kid nervous "Ohhh. Oh, that hurts!"
    "She continued with a colorful curse that shocked me. Looking at her leg, though, I couldn't really blame her."
    $ work24_stopped_bleeding = False
    default work24_menuset = set()
    menu work24_first_aid:
        set work24_menuset
        "What should I do?"
        "Stop the bleeding.":
            him determined "First we better stop the bleeding."
            "I took off my shirt and wrapped it tightly around her leg."
            him concerned "Hold this on there, okay?"
            kid sad "Okay..."
            $ work24_stopped_bleeding = True
            jump work24_first_aid
        "Carry her to the clinic.":
            him determined "Let's get you to mom."
            "I couldn't take the tractor since it had tipped over. I'd get Thuc or someone to help me set it back up later."
            show him at right with move
            "I lifted her up in my arms, something I hadn't done for years and years."
            show him concerned at midright
            show kid sad at midright, squatting
            with slowmove
            "She was a lot heavier now."
            show him concerned at center
            show kid sad at center, squatting
            with move
            kid sad "Ow! My leg!"
            him concerned "Sorry...I'll try not to move it."
            "She rested her head on my chest, and I started on the long walk into town."
            hide him
            hide kid
            with moveoutleft
            scene path with fade
            "My arms, already strained from lifting the tractor, felt heavy and numb, but I walked on."
            "Finally we arrived at the clinic."
            scene hospital with fade
            show her surprised coat at midright with dissolve
            show him determined at midleft
            show kid nervous at center
            with moveinleft
            her surprised coat "[his_name]? What's wrong?"

        "See if she can walk.":
            him surprised "Can you stand up?"
            show kid determined at right, standing with move
            kid determined "Maybe... ugh. No, not really."
            show kid sad at right, squatting with move
            "As she tried to stand up, more blood trickled down her leg."
            jump work24_first_aid
        "Get some help.":
            him determined "I'm going to see if I can get some help, okay?"
            kid sad "Okay..."
            "I switched on my radio."
            play sound "sfx/radio.mp3"
            him concerned "Attention, this is [his_name]. [kid_name] is injured and needs transport to the clinic."
            "No one answered. I tried again."
            him determined "I need transport into town for [kid_name] who is injured. She might have broken her leg. Can anyone help?"
            play sound "sfx/radio.mp3"
            her "{i}[his_name]?! Is she okay?{/i}"
            him determined "She's conscious, but bleeding and her leg's hurt."
            her "{i}Can't you take the tractor?{/i}"
            him concerned "Nope. That's how she got hurt; tractor tipped over."
            natalia "{i}I'm on my way.{/i}"
            her "{i}Thank you, Natalia!{/i}"
            show tractor at center
            show natalia normal at center
            with moveinleft
            "Natalia arrived on her tractor with the trailer attachment. I nestled in the back with [kid_name] while she drove."
            scene path with fade
            kid concerned "Ow!"
            "Every bump made her leg hurt more. I tried to protect her from the worst bumps but it was a long, rough ride."
            "When we arrived, [her_name] was ready for us."
            scene hospital with fade
            show her surprised coat at midright with dissolve
            show him determined at midleft
            show kid nervous at center
            with moveinleft

    "[her_name] ran over, taking in [kid_name]'s injuries."
    her concerned coat "Okay. Not life-threatening. Set her on the bed here."
    show kid cry with dissolve
    "I told her the whole story while she and the nurse cleaned and examined the wound. She felt [kid_name]'s leg carefully, noting every wince. She examined the rest of her, too."
    "[kid_name] was clearly in pain, but also fascinated by what [her_name] was doing."
    her determined coat "Broken tibia. Transverse. Fibula seems to be okay. Concussion."
    "She looked me in the eyes for the first time since I arrived."
    her angry coat "We'll talk about why in the world she was the one driving the tractor later."
    him sad "Is it bad?"
    her concerned coat "She'll be okay, [his_name]. But I need to put her under to put in some pins, so why don't you head on home. [bro_name]'s probably wondering where you are."
    show kid nervous with dissolve
    "He had been working on homework when I left, but that was hours ago..."
    him determined "Okay. Keep me posted."
    hide him with moveoutleft
    scene farm_interior with fade
    play music problems
    "The next day, when they came home, [her_name] wanted to talk."
    show her annoyed coat at midright
    show him concerned at midleft
    with dissolve
    her angry coat "Why was [kid_name] driving that tractor? She's just a kid!"
    him annoyed "She's not just a kid! She's almost an adult and very capable!"
    her annoyed coat "Not capable enough, apparently."
    him determined "Does she still have some things to learn? Of course she does. But she drives the tractor all the time just fine."
    her concerned coat "I know, it's just... I want more for [kid_name]."
    him annoyed "Farming isn't good enough?"
    her sad coat "It's not that!  Well... maybe it is."
    him angry "We've been through this before. People will always need to eat! Growing food is one of the most important jobs people do!"
    her concerned coat "I know but... it's so dangerous. And she could do so much more."
    him annoyed "What could be more important than not starving to death??"
    her annoyed coat "How about not bleeding to death?"
    him concerned "Look, I don't want to have a whose-job-is-more-important argument with you. We need both jobs. What's this really about?"
    her concerned coat "I don't want her to spend the rest of her life digging in the dirt on this alien planet in the middle of nowhere."
    him annoyed "Isn't that what {b}we{/b} are doing?"
    her determined coat "Yes, but we chose this. She didn't."
    menu:
        "What should I say?"
        "You miss Earth.":
            $ marriage_strength += 1
            him concerned "You miss Earth still, don't you."
            her sad coat "Sometimes..."
            him sad "Sorry I dragged you way out here."
            her concerned coat "No, no, it's good. I like the life we have here."
            her surprised coat "I just like Earth, too, and I'd love for her to be able to experience that part of humanity."
            him determined "If she wants to."
        "She might not have a choice.":
            him determined "Well, she's here, and it's not like you can just buy a bus ticket back to Earth. She may be stuck here."
        "There's nothing good on Earth.":
            $ marriage_strength -= 1
            him annoyed "I don't see any reason why she would want to go back to Earth. Good riddance to that crowded, noisy, frivolous, self-absorbed planet!"
            her annoyed coat "Some of us liked it."
            him determined "I still can't see why."

    her concerned coat "Look if she really wants to be a farmer here, and that's her passion, then great, teach her to be the best farmer ever."
    him annoyed "I'm trying to--"
    her annoyed coat "I know, that's what you are trying to do already. Just, let me finish. But we shouldn't expect her to do what we do. She needs to decide for herself."
    him determined "I know that."
    her concerned coat "And she needs to stay alive and whole long enough to find that out."
    him sad "I'm sorry she got hurt, [her_name]."
    her determined coat "It was an accident..."
    menu:
        "What should I say?"
        "I need to teach her better.":
            him concerned "I should have taught her better. Then maybe she wouldn't have gotten hurt."
            her sad coat "..."
            "I heard a faint voice from the other room."
            kid "Dad, it's not your fault. I was driving too fast. You tried to warn me."
            him concerned "Thanks, [kid_name]."
            "I hadn't meant for [kid_name] to overhear us, but maybe it was a good thing. Maybe it would help her understand what we were trying to do."

        "Sometimes you have to learn things the hard way.":
            him annoyed "You have to understand, this world is just dangerous. She needs to learn how to be careful; maybe this is the only way she could learn that."
            her annoyed coat "Maybe you could help her learn in some way that preserves all her limbs."
            him determined "I wouldn't be doing her any favors if I made everything safe. Then she would never learn how to be careful and solve her own problems."
            her angry coat "Well you won't be doing her any favors if she doesn't survive until adulthood, either!"
            him angry "She survived! She'll be just fine!"
            her annoyed coat "Oh, so it's normal to just break your leg once in a while working on the farm?"
            "I thought I heard [kid_name] trying to say something, but I wasn't sure."
            kid "Mom?"
            him annoyed "Yes. Yes, it's totally normal for stuff like this to happen when you're doing real work."
            her angry coat "Real work?! You think you're the only one doing real work?"
            kid "Mom!"
            "[kid_name] was calling from her room."
            her concerned coat "Yes, [kid_name]?"
            kid "Can you guys keep it down? I'm trying to go to sleep."
            her annoyed coat "Sorry, [kid_name]."
            kid "Also, it's not dad's fault. I drove too fast around the corner."
            her concerned coat "Don't worry about that."
            him determined "See? She learned something from this."
            her annoyed coat "I just wish I could say the same thing about you."

        "Maybe she shouldn't work on the farm.":
            him concerned "Maybe she shouldn't work on the farm. I don't want to mess up the rest of her life."
            her concerned coat "I think usually it's good for her. Just... can you just be a little more careful?"
            him concerned "Yeah..."
            her determined coat "I know she looks like an adult, but inside she still has a lot of learning to do."
            him determined "Don't we all..."

    return

# Year 26, 16.1 years old
label work26:
    "Everyone knows about harvesting on the farm."
    "And everyone knows about planting."
    "But there's another step that is just as important that doesn't get a lot of credit."
    "Preparing."
    "After every harvest, I try to take a short break and then get ready for the next crops."
    "I test the soil to determine how much and what kinds of fertilizer to use."
    "I oil tools and machines and try to repair any that have broken."
    "I do an inventory of what seeds we have and try to decide how much we need to grow for each crop."
    "I didn't really need help, but I kind of wanted [kid_name] to learn that there was more to farming than just physical labor."
    "But it would probably take longer if I had to explain it all to her..."
    menu:
        "What should I do?"
        "Have [kid_name] help":
            "It might be more work, but it'd be worth it for how much [kid_name] would learn."
            scene farm_interior with fade
            show him determined at midleft
            show kid normal at midright
            with dissolve
            him normal "Hey, [kid_name]..."
            kid annoyed "Don't tell me there's more work to do!  I thought we just finished the harvest!"
            him annoyed "No more harvesting for now. This is fun. C'mon, I'll show you."
            kid surprised "Really? What are you doing?"
            scene fields with fade
            show him normal at midright
            show kid normal at midleft
            with moveinleft
            him determined "We need to go to these exact GPS coordinates..."
            kid happy "Ooh, is there treasure buried underground?!"
            him happy "If the raw materials for life-sustaining food counts as treasure, then YES!"
            kid annoyed "Not really what I mean..."
            him normal "Anyway, take this soil probe, and get a good sample... yes. Let's get a bunch of those from this list of coordinates."
            kid angry "So... basically we're collecting dirt?"
            him happy "Yes, but in a systematic way. Since we collect from the same spots every year, we can more accurately compare data."
            kid surprised "What kind of data?"
            him determined "Water retention, pH, and nutrient levels for potassium, phosphorus, and nitrogen."
            kid concerned "Why do you care?"
            him normal "These things determine what kind of fertilizer we add."
            kid surprised "Don't we just always add goat manure?"
            him determined "Well, yeah, but how much? And do you need anything else, like bone meal or sand or ashes?"
            kid concerned "I guess... you could just add them all?"
            him concerned "Too much of certain nutrients isn't good for the crops, either. So instead of guessing, we can run some tests and do some math."
            kid flirting "Wow, you're so scientific."
            him happy "I know!"
            "I showed her how to collect the samples, test them, and enter in the results."
            "Then we made a plan."
            "It made me happy to share my plans with someone... [her_name] never really cared about them. Maybe [kid_name] didn't care that much, either, but she had time to listen to me."
            if ((get_extra_work() > 0) and (farm_size < FARM_SIZE_MAXIMUM)):
                "I even decided to show her how to prepare a new field for crops. She helped with the tilling and fencing and everything."
                $ modify_farm_size(1)
            $ independence += 1
        "Do it myself.":
            "I kind of liked planning and preparing and doing the whole farm myself. Why should I share the easiest part with [kid_name]?"
            "Well, it wasn't always easy. But it wasn't physically taxing and it was kind of fun."
            scene fields with fade
            "I spent a few days taking soil samples, analyzing them, and making up a plan for the next year."
            "I felt a sense of satisfaction at coming up with a plan completely on my own, with no one to answer to but myself (unless Ilian decided to complain that we weren't growing enough potatoes again)."
    return

# Year 28, 17.3 years old
# Deal with restaurant?
label work28:
    "Talaam changed a lot while [kid_name] was growing up. When we started, it was just a bunch of farms and a community center."
    "Now we had two doctors, a dedicated fabricator shop, a dentist, a butcher, and a baker."
    "And, soon, our very first restaurant."
    $ bios.addToBio("Travis", "He doesn't seem to have the same issues with our community that Pete does. He hangs out here a lot and even opened up our colony's first restaurant.")

    nvl clear
    travis_c "You are all invited to the Grand Opening of the DinerMight, Talaam's first restaurant, next weekend! The first 10 customers get free pancakes!"
    julia_c "A restaurant?! Who has enough credits to go there?"
    zaina_c "It might be nice for special occasions."
    brennan_c "Might you be serving your dad's special cider?"
    travis_c "We've got several types of cider."
    natalia_c "Wait, is this a bar?"
    travis_c "It's a family-friendly restaurant."
    ilian_c "Finally, Talaam has developed into a truly cultured society."
    nvl clear

    scene farm_interior with fade
    show her concerned at midright
    show kid normal at center
    show bro normal at quarterright
    with dissolve
    show him normal at quarterleft with moveinleft
    him happy "Hey guys, who wants to go out to eat?"
    show her surprised with dissolve
    kid surprised "Like, outside?"
    him normal "No, like to a restaurant!"
    kid happy "Ooh, I've heard of those! Is Travis finally opening a place?"
    him surprised "Yeah, you've heard of it?"
    kid normal "Of course. He was trying to get me to work there but I wanted to wait to see if he was actually going to make it happen first."
    her happy "I haven't been out to eat in... years!"
    "I thought since we were several minutes early we'd definitely be one of the first 10 customers..."
    play music upbeat
    scene restaurant with fade
    show miners at center
    show travis normal at right with dissolve
    "...but I had underestimated the appeal of Talaam's first restaurant. We probably weren't even in the first 30 customers."
    "Miners, colonists, Travis' parents -- it was the largest gathering I'd seen on this planet."
    "Plus, the place wasn't that big."
    "Basically, he had hooked up a fridge to his tractor's power, setup a little griddle, and put out some benches and tables."
    "There was no menu, just lots and lots of pancakes, along with all sorts of toppings: plum syrup, sausage gravy, and honey butter."
    hide miners with moveoutright
    show him normal at center
    show her normal at midleft
    show kid normal at quarterleft
    show bro normal at left
    with moveinleft
    "We waited in line for thirty minutes while he and his sister cooked pancakes."
    if community_22_mined_anyway:
        "He had adapted quite well to his prosthetic leg; he didn't even limp anymore."
    show him at midright
    show her at center
    show kid at midleft
    show bro at quarterleft
    with move
    travis excited "Welcome! It's ten credits each! Apple cider's an additional five; all we have left is soft cider."
    kid determined "Are your parents okay with you running a restaurant?"
    travis normal "Sure. As long as I earn enough to pay them back for all the supplies I had to buy."
    menu:
        "What should I say?"
        "Forget it!":
            "That was way too expensive."
            him concerned "Uh, sorry, I changed my mind."
            her annoyed "You can't change your mind now!"
            him annoyed "But that price is ridiculous!"
            her normal "Then I'm buying."
            "Before I could protest she paid for pancakes and cider for the whole family."
            $ modify_credits(-60)
        "Just pancakes.":
            him normal "Just pancakes for four."
            travis happy "Pancakes for four, got it!"
            her concerned "Oh, I wanted to try the cider..."
            travis normal "Plus one cider!"
            $ modify_credits(-45)
            $ travis_points += 1
        "Pancakes and cider for the whole family!":
            him happy "Pancakes and cider for everyone!"
            kid laugh "Nice!"
            $ travis_points += 2
            $ modify_credits(-60)

    scene restaurant with fade
    show him happy at midright
    show her normal at midleft
    show kid normal at center
    show bro normal at quarterleft
    with dissolve
    "We smothered our pancakes in various toppings and sat down to eat."
    her sleeping "Oh yeah..."
    him sleeping "Mmmm, pancakes..."
    "He had cut the wheat with cornmeal, which was probably cheaper, and there was definitely a lot of buttermilk in them from his parents' cows."
    "But they were light and fluffy and hot and delicious."
    kid surprised "This is so good! How come we never eat pancakes?"
    if ("wheat" in farm.crops):
        him concerned "I usually sell the wheat because it brings in a lot of money."
    elif ("corn" in farm.crops):
        him concerned "You need wheat and cornmeal to make these, and wheat is pretty expensive here still."
    else:
        him concerned "Wheat is pretty expensive..."
    her determined "Plus, you need eggs. We don't usually have all those ingredients around all the time."
    kid flirting "Maybe Travis would teach me how to make them..."
    him annoyed "Or your parents could teach you. It's not hard."
    her flirting "Oh, but I'm sure it'd be so much more fun to learn from Travis~"
    kid annoyed "Mom! He just makes good pancakes, that's all!"

    scene restaurant with fade
    show him normal at center with dissolve
    "We stayed for a while after we ate, talking to friends and neighbors and enjoying being together."
    "After Travis finished cooking, he came up to me."
    show him at midleft with move
    show travis normal at midright with moveinright

    travis normal "Hey, I wanted to talk to you."
    him surprised "To me?"
    travis happy "Yeah, you grow potatoes, right?"
    him normal "Sometimes..."
    travis normal "I want to add potato dishes to the menu. They're cheap, filling, and easy. Can I get your promise that you'll grow at least three fields of potatoes next year and sell them to me?"

    menu:
        "What should I say?"
        "As long as your price is reasonable.":
            travis excited "Oh, it'll be very reasonable. In fact, I'm willing to pay you a lot more than the storehouse for your very best potatoes."
            him happy "Then we have a deal!"
            $ year28_promised_potatoes = True

        "I can't promise that.":
            him concerned "There's a lot of factors that come into play while planning my farm... I can't promise you that."
            travis angry "I see. Well, I'm sure someone else grows potatoes."
    hide travis with moveoutright
    show him at midright with move
    show pete normal at quarterleft with moveinleft
    him normal "Hey, Pete. How do you feel about all this? It's not exactly independent living away from everyone else."
    pete "Well, Travis is old enough to decide for himself, I reckon. But he's not depending on RET for anything, so I'm proud of that."
    him determined "Yeah, but he's depending on everyone else -- you can't have a restaurant without any customers. You always said you wanted to be self-sufficient, not depend on anyone for anything."
    pete "The main thing is, {b}he{/b} decided to open a restaurant. Not a committee, not some pasty-faced government dandy, not even his dad. So I'm okay with that."
    him normal "Good! I gotta say, I'm okay with it, too -- especially if he keeps making those great pancakes."
    pete happy "And it's a great market for my cider."

    play music thoughtful
    scene path with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center
    show bro normal at quarterleft
    "We walked home with full bellies and high spirits."
    kid happy "Thanks for buying us pancakes!"
    bro happy "Yeah, they were really good."
    show him sad with dissolve
    "A melancholy feeling sprouted in my chest as we walked. My tiny remote town had grown large enough for a restaurant."
    "Was it really still the wild frontier if I could just go into town and get pancakes whenever I wanted?"
    hide kid
    hide bro
    with dissolve
    show her at center with move
    her concerned "What is it, [his_name]?"
    him concerned "Our town sure is changing..."
    her determined "And it's about time."
    him surprised "You don't miss the days when there weren't so many people here? When you knew every single person on the planet?"
    her concerned "Not really..."
    him concerned "When there gets to be so many people... it's easier to justify just doing whatever you want."
    her surprised "What are you worried about?"
    him sad "What if Talaam becomes just like Earth? Where you just worry about pleasing your boss, and your boss just worries about making money, and that sense of community is lost?"
    her concerned "It might..."
    him concerned "Sometimes it feels like all my hard work is for nothing."
    her sad "Oh, [his_name]..."
    him normal "Sorry, I must be getting old to be whining like that."
    her flirting "Getting old, huh? You better find happiness where you can, then."
    him flirting "I think I found some, right here."

    return

# You only get this event if you promised potatoes to Travis
label work29_potatoes:
    scene fields with fade
    show him determined at midright
    with dissolve
    show travis normal at midleft with moveinleft

    him normal "Hey there, Travis!"
    if (farm.crops.count("potatoes") >= 3):
        travis excited "Hey, thanks for growing all those potatoes like I asked. The fries are one of my most popular items."
        $ modify_credits(1000)
        $ travis_points += 1
        "He had paid me 1000 credits more than the storehouse would have, so I was pretty happy with the arrangement."
        him happy "No problem. You need anything else?"
        travis happy "Yeah, actually. I was hoping to buy some honey from you so I can sell ice cream."
        if ("honey" in farm.crops):
            him concerned "I am going to have some honey this year..."
            travis normal "Great, will you sell it to me? I can pay in advance."
            him determined "Hmmm. Let me think about that."
            "There was something about the idea that bothered me... I stood in silence for a moment, trying to figure out what it was."
            "Then I figured it out. There was not that much honey on Talaam. If he bought all of mine, his ice cream would be one of the few sweet things on the whole planet."
            "If I sold to him, would I be creating a monopoly? He already had the only restaurant..."
            "Though I guess there was nothing stopping someone else from creating a restaurant if they really wanted to."
            menu:
                "What should I say?"
                "Sure.":
                    him normal "Sure, I'll save some honey for you."
                    "We worked out the specifics, and he paid me 500 credits."
                    $ modify_credits(500)
                    $ mavericks += 1
                    $ travis_points += 1
                "I don't want to do that.":
                    him concerned "Sorry, I don't want to sell all my honey to you. You can buy it from the storehouse like everyone else."
                    travis angry "If that's what you want."
                    $ colonists += 1
        else:
            him concerned "Sorry, I don't have any honey this year."
            travis normal "Okay, well, think about it for next year!"
            $ mavericks += 1

    else:
        travis angry "Hey... I thought you agreed to grow three fields of potatoes for me."
        "I thought back to the pancake breakfast at the restaurant... I had agreed to do that."
        menu:
            "What should I say?"
            "Sorry.":
                $ travis_points -= 1
                "I shrugged."
                him determined "Sorry."
                travis excited "'Sorry'? That's it? I thought I could trust you."
                him annoyed "Hey, we didn't have a contract or anything. I was going to be doing you a favor."
                travis angry "I didn't think two honest people needed a contract to keep their word. I guess I was wrong."
                $ mavericks -= 1
            "I can sell you something else.":
                him concerned "Hey, I'm really sorry about that... can I sell you something else?"
                travis normal "Hmmm... I'm looking at buying honey to make ice cream, if you have any of that."
                if (farm.crops.count("honey") > 0):
                    him normal "I do have honey."
                    travis angry "I guess that'll work."
                    "We worked out the specifics, and he paid me 500 credits."
                    $ modify_credits(500)
                else:
                    him sad "Sorry, I don't have honey, either."
                    travis excited "Forget it, then!"
                    $ mavericks -= 1
            "I can sell you the potatoes I have." if (farm.crops.count("potatoes") > 0):
                $ potato_count = farm.crops.count("potatoes")
                him concerned "I can sell you the potatoes I do have."
                travis normal "I guess that'll work."
                $ modify_credits(300 * potato_count)
                "He paid me for the potatoes and left."
    return

# Year 30, 18 years old
# Terra doesn't want to help! Pay rent?
label work30:
    play music problems
    scene farm_interior with fade
    show kid normal at midright
    show him normal at center
    show her normal at midleft
    "[kid_name] took a deep breath. I braced myself, sensing I was about to hear something I wouldn't like."
    kid determined "I don't want to work on this farm."
    him annoyed "What?!"
    her concerned "You don't have to..."
    kid concerned "I mean, I don't want the crops to fail or anything, but there's so many other things I want to do, too. And I need to know that you'll be okay without my help."
    him angry "Well, we won't be okay! Without your help, there's no way we could grow enough food!"
    her annoyed "[his_name], [kid_name] is almost an adult. She might choose a different job than you."
    show him sad with dissolve
    "I took a deep breath and thought about that for a bit. I suppose I had started taking [kid_name] for granted, assuming she'd just always be there."
    "Part of me wanted to make her stay -- we're farmers! Farming is what we do!"
    "...but another part of me knew that I couldn't force her to stay. Besides, [her_name] wasn't a farmer, either, so why should I expect [kid_name] to be one?"
    $ work28_rent = 0
    $ factor = 0.75
    menu:
        "What should I say?"
        "If you don't work, you need to pay rent.":
            him determined "I'm not going to force you to work on the farm, but if you're not, then you'll need to pay rent."
            her annoyed "Really? You want to charge our own daughter {b}rent{/b}?"
            him annoyed "Like it or not, that's how the real world works. Everybody needs to do something useful."
            her surprised "What if she's taking classes?"
            him pout "Everybody should work. Even people taking classes."
            her angry "So are you going to charge me rent, too?!"
            him annoyed "That's different! You get paid, and we use the money together. Is [kid_name] going to turn over everything she makes to us?"
            kid annoyed "No!"
            him determined "Everyone in this family helps out. If you're not helping around the house or the farm, then you can help out with money."
            her annoyed "But--"
            kid determined "I can pay 150 per month."
            her concerned "No, [kid_name], you might need that money..."
            menu:
                "Is 150 credits good for rent?"
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
                    her determined "[his_name], be reasonable. She's just getting started on her own."
                    kid determined "I can pay 200, but not 250."
                    him determined "Then I guess that will have to do."
                    $ work28_rent = 200
            her surprised "If you can't make it some month, come by the clinic and I can find some work for you."
            kid annoyed "I'll be fine, Mom."
            $ factor = 0.5

        "If you want to live here, you'll need to help.":
            him determined "Everyone that lives here needs to help out in some way."
            her surprised "Maybe not on the farm, but in other ways?"
            kid annoyed "Sure, I can do chores and stuff. I just don't want to be your fieldhand."
            "We worked out some things that [kid_name] could do that weren't farming -- making meals and running errands for [her_name] and I."
            him concerned "Hopefully I can still count on your help during harvest time."
            kid nervous "Yeah, for now."
            $ factor = 0.8
        "We can cut back gradually.":
            him determined "I need you until the harvest. After that, we can slowly cut things down."
            kid concerned "Okay..."
        "You don't have to work here.":
            him concerned "You don't have to work on the farm. But I could definitely use your help."
            if (is_attached()):
               kid concerned "Maybe just when you really need me."
               him determined "Okay. Thanks, [kid_name]."
            else:
                kid concerned "Uh, yeah, we'll see."
            $ factor = 0.5

    show bro concerned at quarterleft with moveinleft
    bro concerned "I don't want to work on the farm, either."
    "I already didn't have [bro_name] doing much on the farm. He was a good kid, but he was gentle and sensitive and I could tell he would never be the kind that enjoyed the rough hard work of farm life."
    "But the work needed to get done, somehow, and without [kid_name] it would be too much just for me."
    menu:
        "What should I do?"
        "Reduce the size of my farm."  if (farm_size > FARM_SIZE_MINIMUM):
            "The best thing to do was just to not plant as many crops. Then I wouldn't need as much help. Hopefully it would still be enough."
            $ modify_farm_size(-2)
        "Hire some help.":
            if (work28_rent > 0):
                "With the extra money [kid_name] would be paying in rent, I could afford to hire some help. Surely there'd be someone who'd be willing to do some hard work in exchange for a little extra money."
            else:
                "It would cost me, but I thought the cost of hiring another worker would be less than the cost of reducing the field."
            $ work28_rent -= 125
            $ factor += 0.2
        "Have [bro_name] help more.":
            him concerned "Sorry, [bro_name]. With [kid_name] leaving, I need your help more than ever."
            bro sad "I don't want to..."
            him explaining "I know. But sometimes we all gotta do things we don't want to do."
            $ factor += 0.2
    "I guess it was [kid_name]'s job to grow up and eventually leave us."
    "I wasn't quite ready for it to start, though."

    $ modify_credits(work28_rent)
    # She and Bro only can help a little now.
    $ kid_other_work = roundint(total_competence * factor)
    return
