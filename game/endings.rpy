##
# ENDINGS
#

# Determine which ending the user should receive, depending on Terra's stats.
label ending:
    scene stars with fade
    play music thoughtful
    "[kid_name]'s childhood was so different from my own. Instead of playgrounds and ready-made toys, she had alien creatures and mining conflicts."
    "I guess we both had parents, friends, and problems."
    "And we both grew up as farmers, too."
    "When she was a baby, I never would have guessed she'd grow up like she did."

    # TODO: work/farm ending stuff?
    # TODO: remove debug code
    "Reached ending. Attachment: [total_attachment], Competence: [total_competence], Independence: [total_independence]"
    # community ending
    # TODO: 10 is kinda high?
    if (colonists >= FACTION_HIGH):
        $ achieved("It Takes This Village")
        if (miners >= FACTION_HIGH):
            $ achieved("Miner Details")
            if (mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_CMiMa
            else:
                call ending_CMima
        else:
            if (mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_CmiMa
            else:
                call ending_Cmima
    else:
        if (miners >= FACTION_HIGH):
            $ achieved("Miner Details")
            if (mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_cMiMa
            else:
                call ending_cMima
        else:
            if (mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_cmiMa
            else:
                call ending_cmima

    if (has_strong_marriage()):
        "I don't know if I would have made it through it all without [her_name]."
        "She listens to me, she helps me with kids and on the farm, and when she disagrees she tells me straight up but with love."
        "After all that we've been through, our relationship is stronger than ever."
        $ achieved("Blackberry & Asparagus")
    else:
        "But even after everything we've been through, [her_name] and I are still together."
        "Is it because of love, or are we just so used to each other we can't imagine living any other way?"
        "I'm glad she's with me, anyway."

    "We didn't always agree on what [kid_name] should do, but in the end, [kid_name] made her own choices."
    "I'm sure I played a part in those, but I can't put my finger on any one thing that made her turn out the way she did."

    # TODO: some of this community stuff doesn't work with these endings. Make them more personal and less far-seeing.
    # TODO: mention jellies in endings?

    $ parenting_style = get_parenting_style()
    "Parenting style: [parenting_style]"

    if (total_attachment < ATTACHMENT_HIGH):
        if (total_competence < COMPETENCE_HIGH):
            call ending_ac
        else:
            call ending_aC
    else:
        if (total_competence < COMPETENCE_HIGH):
            call ending_Ac
        else:
            call ending_AC

    menu:
        "Would you like to make one last poem?"
        "Yes":
            menu:
                "What should it be about?"
                "My family":
                    $ word_board.set_wordpack(basic_words, family_words, baby_words, separation_words)
                "Talaam":
                    $ word_board.set_wordpack(basic_words, talaam_words, farm_words)
                "[her_name]":
                    $ word_board.set_wordpack(basic_words, family_words, romance_words)

            call make_poem
        "No":
            $ pass
    menu:
        "Would you like to see your poems?"
        "Yes":
            call screen poetry_display(word_board, True)
        "No":
            $ pass
    call credits
    return

#1 aci - Blames you for everything. Clingy. Returns to Earth (with Lorant?) but you know the relationship won't last.
label ending_ac:
    "Ending aci"
    play music tense
    scene plain with fade
    show him determined at center
    show her normal at midright
    with dissolve
    her surprised "Where's [kid_name]? I thought she'd want to say goodbye to Anya."
    him surprised "I thought Anya was staying here, with Travis."
    her concerned "I thought they broke up..."
    him normal "I can't keep track of who's with who anymore!"

    show brennan normal at midleft with moveinleft
    brennan normal "[her_name]. I just wanted to say I'm sorry."
    her surprised "Sorry for what?"
    brennan angry "That [kid_name]'s leaving. I tried to convince her to stay, but after everything she told me... well, I can't blame her."
    him annoyed "Leaving? Leaving for where?"
    brennan normal "Earth, of course. Where else would we be headed?"
    him angry "She's NOT going with YOU!"
    brennan angry "Of course not. She's traded places with Anya so she can be with Lorant. I thought you knew."
    her determined "No. We did not."
    him surprised "There she is!"
    show kid determined at midleft with moveinleft
    show brennan at left with move
    her concerned "[kid_name]! You-- you're leaving?!"
    kid annoyed "Yeah."
    him angry "Like hell you are! You take that bag right back home right now!"
    brennan normal "Sorry, she's a legal adult and she signed a contract."
    her sad "Why would you do this?"
    kid angry "Lorant loves me. We're happy together. And I've always wanted to go to Earth."
    him determined "But we'll never see you again."
    kid nervous "You hardly ever saw me when I lived with you, so I don't see what the big difference will be."
    her sad "Isn't there some way I can change your mind?"
    brennan angry "It's too late for that. The contract is signed."
    kid cry "Mom, I... I'm sorry. I love you, but I want to go."
    show her cry at center
    show him pout at midright
    with move
    "[her_name] embraced her tightly for several minutes, as if stamping in her mind every detail about our daughter."
    menu:
        "What should I say?"
        "Goodbye, sweetie.":
            him concerned "Goodbye, sweetie."
        "You're making a mistake.":
            him annoyed "You're making a mistake! When things go wrong and you realize how horribly you've screwed up, remember that I told you so!"
            kid annoyed "Wow, I really am going to miss you."
        "We'll miss you.":
            him concerned "We'll miss you..."

    kid sad "Goodbye, dad."
    show kid at center
    show her at quarterright
    with move
    "She hugged me briefly, and then turned around. She ran to catch up to Lorant, clinging to his arm as they boarded the shuttle."
    hide kid with moveoutright
    show brennan at midleft with move
    "Just like that, she was gone from my life."
    "I never saw her again."
    him yell "How could you let her sign a contract like that without even mentioning it to us?!"
    brennan normal "It's not my fault if you don't know what's going on in your own kid's life."
    her surprised "Brenann!"
    # TODO: adjust based on whether you are a good farmer/liaison or not
    if (miners_strong()):
        brennan angry "Sorry, but it's true. You're a fine farmer, [his_name], and a decent liaison, but you're a terrible father."
    else:
        brennan angry "Sorry, but it's true. You may be a decent farmer, but you're a terrible father."
    him angry "Since when do you know anything about being a father? Oh wait, you've probably got bastards on several planets by now. I'm sure you're a wondeful father to them."
    brennan normal "Before I came back I decided to make sure I'd never be a father. Seems like you should have done the same."
    her angry "Enough! This might be the last time you see each other. Do you really want the other person to remember you this way?"
    him annoyed "I'd be happy if he never thought of me again."
    brennan angry "I'm sorry, [her_name]. I wouldn't want your last memories of me to be sad ones."
    her concerned "Will you look out for [kid_name]? I know you said you never wanted to be a father..."
    brennan normal "I'm not her father. But... I am her manager. Yes, I'll watch out for her."
    "[her_name] glared at me. I wanted to get in one last barb at Brennan, to hurt him so he'd feel as awful as I did. But I didn't want to hurt [her_name]."
    menu:
        "What should I say."
        "...thanks.":
            him concerned "I... I'd appreciate that."
        "(Don't say anything)":
            "I didn't say anything. I couldn't say anything nice, and I thought I might regret all the not-so-nice retorts running through my brain."
        "If anything happens to her...!":
            him angry "If anything happens to her...!"
            brennan angry "Anything? All sorts of things will happen to her! But you don't get a say in that anymore. You gave that up when you shut her out of your life."
            her concerned "Let it go, [his_name]. This isn't helping anything."

    hide brennan with moveoutright
    show him concerned at midleft with move
    show her concerned at midright with move
    with dissolve
    "Brennan nodded and boarded the shuttle. I looked at all the windows for [kid_name] and her boyfriend, but I couldn't see them anywhere. She didn't even wave goodbye."
    scene farm_interior with fade
    show him concerned at center
    show her concerned at midright
    show bro concerned at midleft
    with dissolve
    "[her_name] and I watched the shuttle lift off in silence. We ate a quiet dinner with [bro_name], and then [her_name] went to bed early."
    hide her with moveoutright
    "I found her in our room, heaving great sobs."

    play music sad
    scene bedroom with fade
    show him surprised at midleft, squatting
    show her cry at midright, squatting
    show bedroom_overlay
    show night_overlay
    with dissolve

    her cry "She's gone. My little girl. She's really gone."
    him concerned "We knew she would leave someday..."
    her annoyed "But not like this! She left because we failed her. And now we'll probably never see her again."
    him angry "It's not our fault she chose to go back to Earth with some idiot!"
    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):
        her sad "Isn't it? We never gave her any space! We tried to control her life and never let her make her own decisions!"
    elif (parenting_style == "authoritative"):
        her sad "Isn't it? Were we too strict? Not strict enough? Maybe I didn't spend enough time with her..."
    elif (parenting_style == "permissive"):
        her sad "Isn't it? We just let her do whatever she wanted! Why are we surprised when she keeps doing exactly that?!"
    else:
        her sad "Isn't it? We just weren't there for her often enough. We were too absorbed in our own lives..."
    him angry "You can't think that way!"
    her surprised "What do you mean?"
    him annoyed "You can't second-guess every decision you ever made. What's done is done."
    her sad "Then what are we supposed to do now?"
    him determined "The only thing we can do is try and be better than we were. Maybe she's back on Earth, but we can still send her messages. We can try and do better with [bro_name]."
    her concerned "That's true, but..."
    her sad "None of that will bring my baby back."

    "Ending 1/4, Bring Back My Baby."
    $ achieved("Bring Back My Baby")

    return

# Ending #2 aC - She stays on Talaam, working with Kelly as a nurse
# because she's trying to please you, but even though she's pretty good at it
# she has no confidence or self-direction.
# always worried, aims to please people, scared of making mistakes
label ending_aC:
    "Ending aCi."
    scene hospital with fade
    show her normal coat at midright
    show thuc normal at center
    show kid normal at midleft
    with dissolve
    kid surprised "Is this the right spot for the injection?"
    her determined coat "Not quite. Feel the bone there? Now come about two finger's width down... into that muscle there."
    kid nervous "Right here?"
    her concerned coat "Almost... a little lower. See, when you pinch it, it looks like this."
    kid sad "Maybe you should do it."
    thuc "Yeah, this is the most painful shot I've ever had, and you haven't even pierced the skin yet!"
    her annoyed coat "She needs the practice! I'll make sure she does it right. Try again, [kid_name]."
    kid concerned "Okay... right, um, here?"
    her normal coat "Yes, that's right!"
    thuc sad "Ow!"
    kid concerned "Sorry!!"
    thuc happy "Just kidding, [kid_name]."
    her determined coat "Slow down! Slow and steady... there."
    thuc normal "So, is that all I need?"
    her normal coat "Yes, let me know if you don't start feeling better by tonight."
    hide thuc with moveoutleft
    show him normal at quarterleft with moveinright
    him happy "Hello, lovely ladies! I brought you some lunch!"
    kid annoyed "I'm not hungry."
    hide kid with moveoutright
    him surprised "What's with her?"
    her concerned coat "I tried starting her with some basic hands-on nursing duties today but... she's having a hard time."
    him determined "Well, she's smart, so I'm sure she'll catch on quickly."
    her annoyed coat "I hope so."
    show him at midleft with move
    him surprised "What's wrong?"
    her determined coat "I'm not sure this is the right job for her."
    him determined "Well, if she's not going to help grow food, then helping people not die is a pretty good use of her talents."
    her annoyed coat "She feels awkward touching people, and she's always second-guessing herself, and she needs my reassurance even about easy little things."
    him flirting "I'm sure she just needs more practice. I've heard from a {b}very{/b} reliable source that it takes a lot of time to become a competent medical professional."
    if (total_independence >= INDEPENDENCE_HIGH):
        her concerned coat "She's thinking about going back to Earth to study."
        him surprised "Why would she do that? She can learn everything she needs right here!"
        show kid determined at quarterleft with moveinleft
        kid determined "If I'm going to be a doctor, then I want to be a real doctor, not just mom's apprentice. I want to become the best, and Earth is the only place I can do that."
        him pout "The best, huh?"
        her normal coat "There have been so many new advances since we left -- you can learn them all and come back and teach me."
        kid normal "I've put my name on the list for the next shuttle. It'll be a few years, but if I can get my pre-med done here, then I can go straight to med school on Earth."
        him determined "You could help make Talaam even better... Good thinking, [kid_name]."
        kid normal "Thanks, dad."

    else:
        her concerned coat "Yeah...maybe."

        scene hospital with fade
        show kid determined at midright with dissolve
        show him surprised at midleft with moveinleft
        "Before I left, I peeked in the other room to check on [kid_name]. She was studying her anatomy book with a ferocious energy, as though it were her opponent in deadly combat."
        "I smiled at her, proud of her hard work. I almost told her so, but I stopped myself just in time. I didn't want her to get sloppy."
        show kid angry with dissolve
        "She saw my smile, but didn't say anything, just nodded and continued reading, her forehead scrunched up in concentration."

    "Ending 2/4, Proving Herself."
    $ achieved("Proving Herself")
    return


#3 Ac - sets out on her own, with delivery service, but you worry she will not know enough or be able to work hard enough
label ending_Ac:
    "Ending AcI."
    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    with dissolve
    him surprised "Whoa, your prices have gone up!"
    kid determined "I want to put a motor on this thing so I can make deliveries faster. It's going to take some money, though."
    him flirting "Well, you're still the best delivery girl on the entire planet, so I guess I have no choice!"
    kid happy "Da-ad..."
    him surprised "We going to see you at dinner tonight?"

    # TODO: have this depend on boy stats/independence
    kid normal "Not tonight, I'm meeting some friends at Travis' place."
    him concerned "The bar?"
    kid annoyed "It's mostly a restaurant! Besides, nothing else is open late."
    him normal "Okay, well, come back tomorrow and I'll have another load for you."
    kid happy "I will!"
    hide kid with moveoutleft
    "I could have just brought my crops to the storehouse myself, of course."
    "But I wanted an excuse to see [kid_name]. Ever since she moved out I hardly ever see her."
    show her determined with moveinright
    him determined "You just missed her."
    her concerned "Is she doing okay?"
    him concerned "She's expanding her business, which is good... but she lives in a tiny shack and probably eats terrible restaurant food all the time, and..."
    her happy "If that's the worst we have to worry about, then we're doing pretty good."
    him sad "I guess so. I just..."
    her surprised "What?"
    him determined "I want more for her. When she was little, I'd watch her sleeping and imagine all the amazing things she could do with her life, and now..."
    her normal "There's nothing wrong with living an ordinary life. She's a good person. She has her own life but she still visits us and she supports herself. What more could you want?"
    him surprised "Doesn't it feel like a waste to you?"
    her annoyed "No! Is your life a waste because you spent it growing food instead of inventing vaccines or leading a revolution or discovering new planets?"
    him annoyed "No, of course not."
    her determined "Then hers isn't either. Besides, she's still young -- who knows what else she might do?"
    him flirting "Too bad you can't say the same thing about us."
    her flirting "Speak for yourself! I've still got a long life ahead of me."
    him normal "It's never too late to keep living, right?"
    her surprised "You don't regret the life we made here... do you?"
    him concerned "Regret this life...?"
    "I stopped and thought about it for a moment."
    him normal "No. No, I don't. It's been full of work and learning things the hard way, but also full of love and fun times and my favorite people."
    if (has_strong_marriage()):
        her happy "Good! I don't regret it, either. It took me a long time to get used to this planet, but I'm glad I followed you way out here, across the universe."
        him happy "I'm glad you did, too! You make all the good things in my life possible."
    else:
        her normal "I don't regret it either. It took me a long time to get used to this crazy plent, but I'm doing good work out here, work that no one else can do."
        him determined "We all need you out here."

    hide her with moveoutleft
    "[her_name] went inside to make dinner, but I stayed outside for a few minutes, taking care of a few loose ends and thinking about [kid_name]."

    scene classroom with fade
    show toddler at center with dissolve
    "I remember when she was little, she wasn't afraid of anything, and she couldn't wait to do new things like go to school or go to the beach."
    scene ocean with fade
    show child at center with dissolve
    "Now, when I ask her what she sees in her future, she just shrugs."
    scene sunset with fade
    show kid nervous at center with dissolve
    "She's changed a lot...but in some ways, she's still a kid."
    "That's fine for now, but part of me wants more for her."
    "Should she want to leave home? Is it my fault that she doesn't? Should I have taught her more, somehow?"
    "I can't stop thinking these kinds of things."
    "I guess that's part of what it means to be a parent."

    "Ending 3/4, Forever My Little Girl"
    $ achieved("Forever My Little Girl")
    return

#4 AC - becomes an expert on the jellies, starts to form her own
#       happy web of relationships on Talaam
label ending_AC:
    "Ending AC"
    scene stars with fade
    "[kid_name] moved out. We all pitched in to build a dorm-style apartment building for the growing number of non-farmers that didn't need a lot of space."
    "She seemed to like it; it was closer to town, where she spent most of her time in the library and at the science lab studying biology, astronomy, and sociology."
    # TODO: should your convo about marriage affect this? YES (chooses whether they are best friends or boyfriend/girlfriend)
    "And she was closer to her boyfriend, Oleg."
    "We invited them over for dinner about once a week, where she'd catch us up on all the latest developments."
    scene farm_interior with fade
    show her normal at right
    show him normal at midright
    show kid normal at center
    show oleg normal at midleft
    show bro normal at left
    kid "...so it turns out that the jellysquids cultivate the cucumber kelp on purpose, and use both it and the fish that feed on it for food and tools."
    her surprised "The jellysquids use tools?"
    kid happy "Yeah! I've asked for some scuba gear on the next shuttle, but in the meantime I've been snorkeling down there and it's really amazing the city they've built!"
    bro determined "Can you pass the mashed potatoes?"
    kid annoyed "Aren't you eating anything else?! You're still as picky as ever..."
    him surprised "How come we never knew about the jellysquid city?"
    oleg "It never showed up on our scans because one, it's underwater, and two, it's completely made out of living, organic materials, so it just looked like a coral reef or something."
    kid normal "Oleg's made an app to help us map their city, and another to help us communicate better with them."
    him determined "Better communication would definitely be a good thing."
    if jellypeople_happy:
        kid happy "I'm just glad you didn't mess up our first contact with them... they're still recovering from all the shells they lost, but since they moved to another area and merged with another colony they've been growing much better."
    else:
        kid concerned "I'm just glad we were able to recover from that terrible first contact..."
        him surprised "Did they ever find shells for their babies?"
        kid determined "No, but they merged with another colony and have been able to grow more since then."

    him concerned "This sounds like great research..."
    kid annoyed "...but you wonder how I'm going to make a living, right?"
    him flirting "We do prefer our daughter not to starve to death."
    if (independence >= INDEPENDENCE_HIGH):
        kid normal "Well, that's what I wanted to tell you! A non-profit group on Earth, the Extraterrestrial Allies Foundation, has approved a grant to pay us for our work, obtain equipment, and send more researchers here to Talaam."
        if (miners > 10):
            oleg "RET made a large donation, too, I think on Brennan's advice."
            him annoyed "They're probably hoping the jellysquids will lead them to more mineral deposits."
    else:
        kid nervous "Yeah, I'm still working on that part..."
    kid normal "Anyway, enough about me. I want to know what you've been up to, [bro_name]."
    bro surprised "Me?"
    kid happy "Yeah!"
    bro sad "Just...just regular stuff."
    her happy "He's actually been studying sunspots and solar flares lately."
    kid surprised "Really?"
    bro determined "Yeah... I've been trying to make a computer model so we can predict solar flares long-term more accurately, but the physics engines just aren't good enough to simulate the sunspots. But with enough data-"
    oleg "-you'll be able to improve the model, and also improve predictions! That's great! Which physics engine are you using as a base?"

    "I listened to my family talk. I didn't understand half of what Oleg and [bro_name] were talking about, but I loved to see [bro_name] excited about something."
    "[kid_name] reached over and held Oleg's hand, and he squeezed it back as he extolled the virtues of his favorite physics engine."
    "I put my arm around [her_name] and pulled her close just as she was about to put a forkful of food in her mouth."
    "The food fell on her lap and she elbowed me in mock indignation."
    her flirting "Oh, now look one you've done. You've ruined my fanciest clothes."
    him flirting "Want me to help you clean that off?"
    her happy "Mom, Dad, can you not? Some of us are trying to eat here."
    oleg "I don't know; it's kind of sweet to see old people that are still so in love."
    him surprised "Old people?!"
    her surprised "I don't see any old people in here..."
    show him happy
    show her happy
    with dissolve

    him surprised "Anyway... how are your studies coming, [kid_name]?"
    kid happy "Great! Zaina is answering my questions about astronomy, Thuc is teaching me Earth biology, and Sara's helping me with sociology. Every book is so Earth-centric, though."
    her flirting "It's almost as if that was the only planet humans lived on for thousands of years."
    kid nervous "Well, it's not now, so they need to update their materials!"
    oleg normal "At least the star charts aren't completely worthless."
    him surprised "Really? The stars seem completely foreign from what I remember from Earth..."
    kid normal "Well, there's different planets obviously, and since Talaam's axis of rotation is different the hemispheres don't exactly match up. But I bet I can find some constellations you'd recognize!"
    bro happy "And I'll show you a cool nebula!"
    him happy "I'd like that."
    scene stars with fade
    show him normal at quarterleft, sitting
    show oleg normal at quarterright, sitting
    show her normal at midleft, sitting
    show bro normal at midright, sitting
    show kid normal at center, sitting
    with dissolve
    "We did the dishes and then went outside to watch the stars together. [kid_name] had borrowed a telescope that she setup, and [her_name] brought out some blankets."
    "[bro_name] and [kid_name] argued about how solar flares affected Talaam's evolutionary past, and [her_name] snuggled up against my shoulder."
    "I was so proud of these kids... I didn't know exactly what they would accomplish, but for right now I was just enjoying being together."

    "I want a lot of things for [kid_name], but most of all I want her to find some of this same happiness I've found. Happiness in love, in family, in community."
    "The kind of happiness you feel after working hard all day to accomplish something amazing and coming home to people who love you and forgive you and want you to be your best."

    "So I'm not just happy that she and Oleg are dating."
    "I'm not just happy that she's staying here, on Talaam."
    "I'm also happy she found a way to do something she loves that helps people"
    "She's working hard to understand the jellies in a way that no one else can."
    "With her research and mediation, I see a bright, peaceful future ahead for her."
    "And I'll get to see it all happen."

    "Ending 4/4 The Stars are Bright"
    $ achieved("The Stars are Bright")
    return

#############################################################################
# COMMUNITY ENDINGS
#############################################################################


# TODO: Add some dialogue/messages/interaction with others instead of just narration?
# TODO: Add some sprites/backgrounds to go with each thing?

label ending_CMiMa:
    scene bonfire with fade
    show him blush at midleft
    show brennan happy at midright
    show pete happy at center
    brennan "You've really never heard of quince? It's a common Earth fruit."
    pete "Even I've heard of it, and I grew up in the middle of nowhere."
    him "Well, I was kind of a picky eater growing up, so we didn't eat weird things like that."
    brennan flirting "It's a good thing you grew out of that, since we eat weird things all the time now!"
    pete normal "They're not even weird anymore. I've gotten to craving these wolfslug curry kebabs year-round."
    him excited "They are definitely delicious. Thanks for sharing."
    pete happy "I'm happy to make them for you as long as you bring the flatbread. I have a major brown thumb when it comes to growing wheat."
    him pout "If I drink the wine Brennan made while I eat the curry kebabs, I can remember what real wine tastes like!"
    brennan happy "It may be a long time before we can enjoy a mature vintage. I hope in ten years we can enjoy a good bottle together."
    pete normal "Or a bad bottle. I'm not picky."
    him content "Speaking of long-term projects, how are your interns from the high school working out?"
    brennan normal "Oh, I have one intern who has a knack for assembling good mining teams."
    brennan "He made friends with everyone and figured out their compatibilities quickly."
    pete happy "One of my interns has an amazing spatial memory. She can go foraging with me and then come back and draw a map."
    pete normal "Of course, with satellite imagery, we have the big things covered."
    pete "Her maps take out all the excess noise and make it easier to find things."
    him determined "Sounds like it's going well. My intern seems kind of depressed sometimes. I think she likes handicrafts though. I should have her spend some time with you, Pete."
    him "She might like leatherworking better than farming."
    pete happy "If she likes working with her hands, maybe she could make you a saddle for one of those grass crabs!"
    him sad "I do miss Lettie."
    brennan surprised "Why did they send just one horse?"
    him smirk "RET promised me I could bring any one thing to help me with farming. So I chose Lettie."
    pete normal "I'm surprised they let you do that, and even more surprised she survived the journey."
    him normal "It was in the contract!"
    him sad "They would never let more horses come here now though. Not with all the extra-planetary environmental sanctions."
    pete angry "Hey, no horse could replace Lettie. And who knows, maybe one of these alien quadrapeds can be domesticated."
    brennan normal "I'm happy to let Zaina find some likely candidates for domestication this rainy season."

    scene ocean_sunset
    "There were times when I wasn't sure we would all survive, let alone get along together."
    "To think that I would voluntarily spend time with Brennan..."
    "I was worried that Pete wouldn't be my friend after leaving the colony, but we adjusted over time."

    # TODO: heavy rains in "good" endings, but they cope somehow?
    return

label ending_CMima:
    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout behind rain at midleft
    show ilian angry at midright behind rain
    with dissolve
    him "After this next load, will we be done moving supplies?"
    ilian "No, we need to get at least two more loads to the old mining camp."
    him doubt "I wish I had harnasses for the cows. This is their kind of work."
    ilian normal "Our cattle would make lousy cart-pullers. Cattle wouldn't be able to handle the slippery stairs very well either."
    him sad "I still have to move our supplies to higher ground. How much flooding is expected in the next four hours?"
    ilian angry "Zaina calculated a good four inches, possibly more if the river floods its banks."
    ilian normal "Just ask Brennan or Chaco for help. Brennan volunteered the off-duty miners."
    him content "I hate asking other people for help, but it sure beats losing all my canned carrots."
    ilian happy "Hey, I know that feeling. We can do this if we work together."
    "After two more loads, I went home to do some more pushing and pulling."

    scene farm_exterior with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him surprised behind rain at midleft
    show brennan normal behind rain at midright
    show chaco normal behind rain at center
    with dissolve
    brennan "Hey, we were just finishing your last load of essentials! [her_name] asked us to come help. I think you just need to pack your personal items."
    him content "Thank you so much! I wasn't sure how I was going to get everything up the mountain."
    "I packed a few last things and headed up the mountain to a temporary shelter."

    scene yurt_interior with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show rain
    show him normal at midleft with moveinleft
    show her normal at midright
    her "You made it! Welcome to our temporary home."
    him content "Brennan and Chaco were a real help. It looks like a lot of other families that were close to the river have made it up here too."
    her sad "I hope Pete and the others are okay..."
    him determined "I think they've shown us that they want us to leave them alone."
    her nervous "Well, since we never talk to them, I guess we wouldn't know even if they did need help."

    "It's hard to believe that I would call Brennan a friend now, but he is actually kind of nice sometimes."
    "I think he warmed up to us original colonists after we helped the miners through a few tough times."
    "Pete and the others, though, have drifted apart from us."
    "If they had been more reasonable, things wouldn't be like this."
    "At least, I'd rather believe that than think it could be my problem."

    #several ways this could go. They could discover later that the mavericks were flooded out. A more immediate resolution would be interesting.
    #maybe Helen shows up with a backpack, explaining that they lost some food storage in the flood, and starts living in the old mining camp
    #"Pete insisted on living on his own even when everyone else had given up."

    return

label ending_CmiMa:
    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout behind rain at midleft
    show ilian angry at midright behind rain
    with dissolve
    him "After this next load, will we be done moving supplies?"
    ilian "No, we need to get at least two more loads to the old mining camp."
    him doubt "It's times like this that I really miss Lettie."
    ilian normal "Well, I miss your tractor. Since it's been cloudy for that last two weeks I'm guessing the charge is pretty low?"
    him sad "Yeah, it had only enough charge to move itself, but not an additional load."
    him sad "I still have to move our supplies to higher ground. How much flooding is expected in the next four hours?"
    ilian angry "Pete was saying that the rainfall hasn't been this heavy since we arrived. The river might even flood its banks in the next few hours."
    ilian normal "Pete and some of the others have been helping to move stuff, since their camp is already on high ground."
    him content "I hate asking other people for help, but it sure beats losing all my stored grain."
    ilian happy "Hey, I know that feeling. We can do this if we work together."
    "After two more loads, I went home to do some more pushing and pulling."

    scene farm_exterior with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him surprised behind rain at midleft
    show pete normal behind rain at midright
    show travis teen happy behind rain at center
    with dissolve
    pete "Hi [his_name]! [her_name] asked us to come help. We got your last grain barrel onto our wagon. I think you just need to pack your personal items."
    him content "Thank you so much! I wasn't sure how I was going to get everything up to higher ground."
    pete normal "After you've got everything, we're going to try to take as much of your yurt with us."
    him determined "Let's save as much as we can."
    "I packed a few last things and headed up to a temporary shelter which Pete and the others helped to build."

    scene shack with fade
    with dissolve
    play sound "sfx/rain.ogg" volume 0.6 loop
    show rain
    show him normal at midleft with moveinleft
    show her normal at midright
    her "You made it! Welcome to our temporary home."
    him content "Phew! I'm glad we have a place to sleep."
    her sad "I hope Brennan and the others are okay..."
    him determined "They're already in the mountains, so I doubt a flood will affect them very much."
    her nervous "Yes, but their mines could fill up with water faster than they expected."
    him sad "Even if I wanted to help, I don't think they would trust me."
    her sad "Why would they? It's not like we've been all that trusting of them."
    him determined "It's too late to change that now."

    scene black with fade
    "I've grown a lot closer to Pete and Travis over the past 18 years."
    "Even after they left the colony, I still wanted what was best for them and the others living with them."
    "I don't think I could bring myself to like the miners though."
    "Everything they stood for was against my principles. If they didn't want my help, then I didn't want to help them."

    return

label ending_Cmima:
    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout behind rain at midleft
    show ilian angry at midright behind rain
    with dissolve
    him "After this next load, will we be done moving supplies?"
    ilian "No, we need to get at least two more loads to the old mining camp."
    him doubt "I wish I had harnasses for the cows. This is their kind of work."
    ilian normal "Our cattle would make lousy cart-pullers. Cattle wouldn't be able to handle the slippery stairs very well either."
    him sad "I still have to move our supplies to higher ground. How much flooding is expected in the next four hours?"
    ilian angry "Zaina calculated a good four inches, possibly more if the river floods its banks."
    ilian normal "I would help you, but I've got my own stuff to move after this."
    him cry "I won't be able to bring up everything. Guess I'll say goodbye to my barrels of apples."
    ilian angry "Ask around. Maybe Thuc and Julia can help you, since their kids already moved their storage this morning."
    "After two more loads, I went home to do some more pushing and pulling."

    scene farm_exterior with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him surprised behind rain at midleft
    show thuc happy behind rain at midright
    show julia normal behind rain at center
    with dissolve
    thuc happy "I didn't want all your canned food to go to waste, so we took it up the mountain!"
    thuc sad "We can bring it back though, if you really wanted to feed the fishes."
    him content "Thank you so much! Maybe you can have some of my dried fish as thanks."
    "I packed a few last things and headed up the mountain to a temporary shelter."

    scene shack with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show rain
    show him normal at midleft with moveinleft
    show her normal at midright
    her "You made it! Welcome to our temporary home."
    him pout "Yes, ours along with a bunch of other people..."
    her nervous "At least it's out of the rain."
    him sad "Why didn't Brennan let us use the old mining camp as temporary shelter?"
    her concerned "I think the current rumor is that he didn't want people taking any of the equipment they left there."
    him normal "Like we would want any of that mining crap anyway."
    her surprised "Right? What would we do with it?"
    him pout "Maybe we could strip some solar cells from the solar panels though..."
    her laugh "I guess he wasn't far off."
    her sad "I hope Pete and the others are okay..."
    him determined "I think they've shown us that they want us to leave them alone."
    her nervous "Well, since we never talk to them, I guess we wouldn't know even if they did need help."
    "We focused on our own needs in our little community."
    "How could we help the others when it was a struggle to survive just with our own neighbors?"
    return

label ending_cMiMa:
    "Over the next few years, the colony had difficulty making enough food to survive."
    "People started hoarding food. Some continued to work through solar flares, only to die from the following radiation poisoning in a few years."
    "We became less like a colony and more like a few loosely-connected settlers."
    "Did some families join the mavericks? Or did they just leave in search of food one day, never to return?"
    "The miners bought their food from the mavericks, and the mavericks in turn used their credits to access the colony's technology."
    "Pete would sometimes take over the library for a day, lamenting how the databases these days were only used for entertainment and not for education."
    "He and Brennan developed a business relationship."
    return

label ending_cMima:
    "RET gave permission to the miners to use violent force on anyone who sabotagued or otherwise hindered the miners's operations."
    "A year of violent rains upset crops and native wildlife."
    "Floods destroyed our food storage of dried goods, and some people had to move to higher ground permanently."
    "The mavericks, also suffering from the weather, started stealing food from wherever they could find it."
    "A few were caught by the miners and beaten."
    "Eventually, the Brennan sent some of his miners to help hunt and forage in areas that weren't flooded."
    "Part of the colony ended up moving to a drier part of the continent."
    return

label ending_cmiMa:
    "We received sudden news that RET had gone out of business. Another company would accept the return of the latest shuttle, but there would be no more support shipments from Earth."
    "The remaining miners were very unhappy, but most learned how to hunt or farm to survive."
    "The colony wasn't doing well either, with our farms yielding less and less food each year."
    "Luckily, the mavericks had long ago learned how to survive without external help."
    "They shared their food with us and helped us build up our farms, but it was at a price."
    "In return for their food and labor, the mavericks required some of the colonists to join them."
    "People still died more often since we didn't have access to medical equipment from Earth, but we didn't all die out."
    return

label ending_cmima: #is this ending even possible?
    "We received sudden news that RET had gone out of business. Another company would accept the return of the latest shuttle, but there would be no more support shipments from Earth."
    "The remaining miners were very unhappy, but most learned how to hunt or farm to survive."
    "We barely grew enough food for ourselves. We felt like we were constantly on the brink of total collapse."
    "The mavericks weren't doing any better."
    "A year of heavy rains made problems for everyone."
    "Floods destroyed our food storage, contaminated our water, and completely killed off some of our crops."
    "After moving to higher ground, we tried again with the seeds we managed to save."
    "Some of us died of malnutrition and exhaustion."
    "It felt like soon our bones and possessions would be the only evidence of our existence here."
    return


# acI - Rejects your life and joins mavericks, but fails. Moves from one job to the next, but drives away people around her and isn't good at anything.
# TODO: Delete or use or have as an unlockable?
label ending_extra:
    "This ending was deleted due to changes in what variables were used to compute the ending. You would originally get this ending if you were a neglectful parent but [kid_name] was very independent."
    scene stars with fade
    "Even though [kid_name] still lives on Talaam, I worry a lot about her."
    "She's got more competition with deliveries and now it's harder for her to get business."
    "I worry that she moved in with Travis because she needed a job and a place to stay, not because she really loves him."
    "I worry that she'll be too prideful to ask for help when she needs it."
    "And I worry that I didn't teach her enough for her to be out on her own already."
    "And the worst part about these worries is that, for the most part, I can't do anything about them."
    "I try to talk to her, to be there for her..."
    "...but she doesn't want anything to do with me."

    scene restaurant with fade
    show travis normal at quarterright
    show kid determined at midright
    with dissolve
    show him at midleft
    with moveinleft
    him concerned "Hey, [kid_name]."
    kid annoyed "Dad. What are you doing here?"
    him sad "I just had some extra pickles and thought you might like some."
    "I held them out like I used to hold carrots out for Lettie when I was training her."
    "She looked at Travis, who shrugged and walked off."
    hide travis with moveoutright
    show kid at center with move
    "She took the pickles but didn't get too close."
    show kid at midright with move
    kid concerned "Thanks."
    him determined "If there's anything you need help with--"
    kid annoyed "Dad, I'm fine."
    him surprised "How's Travis?"
    kid nervous "Good."
    him normal "You still have lots of deliveries to make?"
    kid determined "Some. But the miners that left were my best customers."
    menu:
        "What should I say?"
        "What are you going to do?":
            him surprised "So...what are you going to do?"
            kid annoyed "Something else, I guess. Don't worry about it, dad -- it's my life."
            him sad "I'm your dad; I can't not worry about you."
        "Come home.":
            him sad "Come home, [kid_name]. Your room is still there, waiting for you--"
            kid angry "So you can boss me around? No thanks, dad."
            him annoyed "I wouldn't--"
            kid annoyed "Yeah, you would. You don't know any other way to be."
            "That was unfair. But I couldn't think of a good retort."
            kid determined "And that's fine, but I can't live there anymore."
            him determined "You could."
        "Travis doesn't deserve you.":
            him annoyed "Travis doesn't deserve you. Why are you still hanging around him?"
            kid annoyed "You don't even know him! He works hard!"
            him surprised "Doing what?"
            kid nervous "Look, you had your chance to be my dad when I was little and I didn't have a choice. It's too late to start caring now."
            him angry "I've cared for you your whole life!"
    kid sad "Ugh, Dad, can we not?"
    him sad "..."
    kid determined "Just... just let me live my life, okay? I'm going to make mistakes."
    kid surprised "Maybe I'll be unemployed, maybe I'll trust the wrong person and have my heart broken, maybe I'll go hungry and eat nothing but potatoes for a month, or maybe I'll hunt crabirds and die alone in the wilderness!"
    kid normal "But if I don't try, if I don't get a chance to make those mistakes for myself...what's the point of being alive?"
    show him surprised with dissolve
    "I wanted to embrace her, to give her a father's comfort. But I didn't think I could take it if she pushed me away."
    him concerned "I understand."
    "I turned to leave."
    kid surprised "Dad?"
    him surprised "Yes?"
    kid normal "Thanks for the pickles."
    him normal "Anytime."

    "Ending, Mistakes to Call My Own."
    return
