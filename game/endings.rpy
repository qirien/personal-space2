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

    # TODO: community ending stuff
    # Talk about miners, colonists, mavericks, and jellies

    # TODO: work/farm ending stuff?

    # TODO: remove debug code
    "Reached ending. Attachment: [attachment], Competence: [competence], Independence: [independence]"
    # community ending
    # TODO: 10 is kinda high?
    if (colonists >= 10):
        if (miners >= 10):
            if (mavericks >= 10):
                call ending_CMiMa
            else:
                call ending_CMima
        else:
            if (mavericks >= 10):
                call ending_CmiMa
            else:
                call ending_Cmima
    else:
        if (miners >= 10):
            if (mavericks >= 10):
                call ending_cMiMa
            else:
                call ending_cMima
        else:
            if (mavericks >= 10):
                call ending_cmiMa
            else:
                call ending_cmima

    "For now, though, I was more concerned with [kid_name]."
    # TODO: some of this community stuff doesn't work with these endings.

    $ parenting_style = get_parenting_style()
    "Parenting style: [parenting_style]"
    if (attachment < ATTACHMENT_HIGH):
        if (competence < COMPETENCE_HIGH):
            # aci and acI
            if (independence < INDEPENDENCE_HIGH):
                call ending_aci
            else:
                call ending_acI
        else:
            # aCi and aCI
            if (independence < INDEPENDENCE_HIGH):
                call ending_aCi
            else:
                call ending_aCI
    else:
        if (competence < COMPETENCE_HIGH):
            # Aci and AcI
            if (independence < INDEPENDENCE_HIGH):
                call ending_Aci
            else:
                call ending_AcI
        else:
            # ACi and ACI
            if (independence < INDEPENDENCE_HIGH):
                call ending_ACi
            else:
                call ending_ACI

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
            # TODO: this doesn't show all poems because every time you make it a new Board, it deletes all the old poems. Might need to separate board from poems somehow or keep track of them with a separate global variable.
            # TODO: add 'Share my poems'! link here?
            call screen poetry_display(word_board)
        "No":
            $ pass
    call credits
    return

#1 aci - Blames you for everything. Clingy. Follows (miner?) boyfriend back to Earth but you know the relationship won't last.
label ending_aci:
    "Ending aci"
    scene plains with fade
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
    show kid at midleft with moveinleft
    show brennan at left with move
    her concerned "[kid_name]! You-- you're leaving?!"
    kid annoyed "Yeah."
    him angry "Like hell you are! You take that bag right back home right now!"
    brennan normal "Sorry, she's a legal adult and she signed a contract."
    her sad "Why would you do this?"
    kid angry "Lorant loves me. We're happy together. And I've always wanted to go to Earth."
    him determined "But we'll never see you again."
    kid shifty "You hardly ever saw me when I lived with you, so I don't see what the big difference will be."
    her sad "Isn't there some way I can change your mind?"
    brennan angry "It's too late for that. The contract is signed."
    kid cry "Mom, I... I'm sorry. I love you, but I want to go."
    "[her_name] embraced her tightly for several minutes, as if stamping in her mind every detail about our daughter."
    menu:
        "What should I say?"
        "Goodbye, sweetie.":
            him concerned "Goodbye, sweetie."
        "You're making a mistake.":
            him annoyed "You're making a mistake! When things go wrong and you realize how horribly you've screwed up, remember that I told you so!"
            kid "Wow, I really am going to miss you."
        "We'll miss you.":
            him concerned "We'll miss you..."

    kid sad "Goodbye, dad."
    "She hugged me briefly, and then turned around. She ran to catch up to Lorant, clinging to his arm as they boarded the shuttle."
    hide kid with moveoutright
    show brennan at midleft with move
    "Just like that, she was gone from my life."
    "I never saw her again."
    him yell "How could you let her sign a contract like that without even mentioning it to us?!"
    brennan normal "It's not my fault if you don't know what's going on in your own kid's life."
    her surprised "Brenann!"
    # TODO: adjust based on whether you are a good farmer/liaison or not
    brennan angry "Sorry, but it's true. You're a fine farmer, [his_name], and a decent liaison, but you're a terrible father."
    him angry "Since when do you know anything about being a father? Oh wait, you've probably got bastards on several planets by now. I'm sure you're a wondeful father to them."
    brennan normal "Before I came back I decided to make sure I'd never be a father. Seems like you should have done the same."
    her yell "Enough! This might be the last time you see each other. Do you really want the other person to remember you this way?"
    him annoyed "I'd be happy if he never thought of me again."
    brennan sad "I'm sorry, [her_name]. I wouldn't want your last memories of me to be sad ones."
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
    "[her_name] and I watched the shuttle lift off in silence. We ate a quiet dinner with [bro_name], and then [her_name] went to bed early."
    "I found her in our room, heaving great sobs."
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

    "Ending 1/8, Bring Back my Baby."
    $ achievement.grant("Bring Back my Baby")

    return

#2 acI - Rejects your life and joins mavericks, but fails. Moves from one job to the next, but drives away people around her and isn't good at anything.
label ending_acI:
    "Ending acI."
    "Even though [kid_name] still lives on Talaam, I worry a lot about her."
    "She's got more competition with deliveries and now it's harder for her to get business."
    "I worry that she moved in with Travis because she needed a job and a place to stay, not because she really loves him."
    "I worry that she'll be too prideful to ask for help when she needs it."
    "And I worry that I didn't teach her enough for her to be out on her own already."
    "And the worst part about these worries is that, for the most part, I can't do anything about them."
    "I try to talk to her, to be there for her..."
    "...but she doesn't want anything to do with me."

    scene restaurant with fade
    show travis at midright
    show kid at center
    with dissolve
    show him at midleft
    with moveinleft
    him concerned "Hey, [kid_name]."
    kid annoyed "Dad. What are you doing here?"
    him sad "I just had some extra pickles and thought you might like some."
    "I held them out like I used to hold carrots out for Lettie when I was training her."
    "She looked at Travis, who shrugged and walked off."
    hide travis with moveoutright
    "She took the pickles but didn't get too close."
    kid concerned "Thanks."
    him "If there's anything you need help with--"
    kid "Dad, I'm fine."
    him "How's Travis?"
    kid "Good."
    him "You still have lots of deliveries to make?"
    kid "Some. But the miners that left were my best customers."
    menu:
        "What should I say?"
        "What are you going to do?":
            him "So...what are you going to do?"
            kid "Something else, I guess. Don't worry about it, dad -- it's my life."
            him "I'm your dad; I can't not worry about you."
        "Come home.":
            him "Come home, [kid_name]. Your room is still there, waiting for you--"
            kid "So you can boss me around? No thanks, dad."
            him "I wouldn't--"
            kid "Yeah, you would. You don't know any other way to be."
            "That was unfair. But I couldn't think of a good retort."
            kid "And that's fine, but I can't live there anymore."
            him "You could."
        "Travis doesn't deserve you.":
            him "Travis doesn't deserve you. Why are you still hanging around him?"
            kid "You don't even know him! He works hard!"
            him "Doing what?"
            kid "Look, you had your chance to be my dad when I was little and I didn't have a choice. It's too late to start caring now."
            him "I've cared for you your whole life!"
    kid "Ugh, Dad, can we not?"
    him sad "..."
    kid "Just... just let me live my life, okay? I'm going to make mistakes."
    kid "Maybe I'll be unemployed, maybe I'll trust the wrong person and have my heart broken, maybe I'll go hungry and eat nothing but potatoes for a month, or maybe I'll hunt crabirds and die alone in the wilderness!"
    kid "But if I don't try, if I don't get a chance to make those mistakes for myself...what's the point of being alive?"
    "I wanted to embrace her, to give her a father's comfort. But I didn't think I could take it if she pushed me away."
    him concerned "I understand."
    "I turned to leave."
    kid "Dad?"
    him surprised "Yes?"
    kid "Thanks for the pickles."
    him normal "Anytime."

    "Ending 2/8 Mistakes to Call My Own."
    return

#3 aCi - She stays on Talaam, working with Kelly as a nurse
# because she's trying to please you, but even though she's pretty good at it
# she has no confidence or self-direction.
# always worried, aims to please people, scared of making mistakes
label ending_aCi:
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
    thuc "Yeah, maybe you should do it, [her_name]. I'm starting to feel a little nervous!"
    her annoyed coat "She needs the practice! I'll make sure she does it right. Try again, [kid_name]."
    kid concerned "Okay... right, um, here?"
    her concerned coat "Remember, find the triangle."
    thuc "This is the most painful shot I've ever had, and you haven't even pierced the skin yet!"
    kid surprised "Here?"
    her happy coat "Yes, that's right!"
    thuc "Ow!"
    kid concerned "Sorry!!"
    her determined coat "Slow down! Slow and steady... there."
    thuc "So, is that all I need?"
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
    him normal "I'm just glad she found something useful to do."
    her concerned coat "Yeah, maybe..."
    him surprised "What's wrong?"
    her determined coat "I'm not sure this is the right job for her."
    him determined "Well, if she's not going to help grow food, then helping people not die is a pretty good use of her talents."
    her concerned coat "She's not very good at it."
    him surprised "She's not?"
    her annoyed coat "No. She feels awkward touching people, and she's always second-guessing herself, and she has a hard time remembering what to do."
    him flirting "I'm sure she just needs more practice. I've heard from a {b}very{/b} reliable source that it takes a lot of time to become a competent medical professional."
    her concerned coat "Yeah...maybe."

    "Before I left, I peeked in the other room to check on [kid_name]. She was studying her anatomy book with a ferocious energy, as though it were her opponent in deadly combat."

    him happy "That's my girl! You'll make something of yourself yet!"
    "She didn't say anything, just nodded and continued reading, her forehead scrunched up in concentration."
    "She was trying so hard. I was proud of her. I almost said something, but then I stopped myself. I didn't want her to get sloppy."

    "Ending 3/8, Proving Herself."
    return

#4 aCI - Returns to Earth to study medicine, though you worry about her lack of friends/family
label ending_aCI:
    "Ending aCI."
    her "It's not too late to change your mind. You could complete your studies here..."
    kid "I know, mom, but I want to be a real doctor, not just your apprentice. I want to become the best, so Earth is where I need to go."
    him "Study hard, [kid_name]. Make us proud."
    kid sad "I'm trying, dad."
    her determined "We are proud. And you'll always have a home here, no matter what happens."
    him "Don't get caught up with stupid college stuff, all right? Stay away from the wild parties and the drugs and the cheating and all that."
    her "Oh, I'm so excited for you to experience Earth! You might even get to meet your cousins."
    kid "I'm excited to see a rain forest. Or any forest at all, actually."
    bro "Send us pictures!"
    him "Wow, my little daughter, on her way to med school..."
    kid nervous "Oh no...What if I can't do it? What if I really suck at taking care of myself? What am I thinking; I've never even been to a real school!"
    her normal "No backing out now! You'll be fine. I promise."
    him "Don't forget us."
    kid "I'll send you messages when I can."
    brennan "Careful, or you'll end up stuck here for another 12 years. The shuttle's leaving!"

    kid "But... I don't know if I can do this!"
    him "You can and you will! Now, get on that shuttle!"
    her "Goodbye, [kid_name]! We love you!"
    "She hoisted her duffle bag onto her shoulder and boarded the shuttle. I couldn't believe it was really happening. Our baby was leaving."
    bro "Goodbye!"
    "I didn't know what to say. All I could think about were the things I didn't have a chance to teach her, to tell her."
    "What if she started failing her classes? What if she didn't cook herself good enough food? What if she made huge mistakes and didn't apologize? What if her heart was broken?"
    "It was too late for me to teach her those things. She'd have to learn from her own mistakes, now."
    him "Goodbye!"

    "Ending 4/8, Down to Earth."
    return

#5 Aci - stays on your farm helping you, though she doesn't work hard enough to be of much help.
label ending_Aci:
    "Ending Aci"
    scene fields with fade
    "[kid_name] said she didn't want to work on our farm, but..."
    "That's what she ended up doing."
    "She also makes deliveries, but she always helps me with the harvest and other jobs around the farm that are a lot easier with a few people."
    "She still needs a lot of direction, but she's willing to do what I ask."
    "I was expecting [kid_name] to get married and leave us, or go off to pursue her own dreams, but so far she seems content to keep things as they are."
    "I remember when she was little, she wasn't afraid of anything, and she couldn't wait to do new things like go to school or go to the beach."
    "Now, when I ask her what she sees in her future, she just shrugs."
    "She's changed a lot...but in some ways, she's still a kid."
    "That's fine for now, but part of me wants more for her."
    "Should she want to leave home? Is it my fault that she doesn't? Should I have taught her more, somehow?"
    "I can't stop thinking these kinds of things."
    "I guess that's part of what it means to be a parent."

    # TODO: add a scene here, not just narration?
    "Ending 5/8, Forever My Little Girl"

    return

#6 AcI - like #5, but sets out on her own, but you worry she will not know enough or be able to work hard enough
label ending_AcI:
    "Ending AcI."
    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    with dissolve
    him determined "Whoa, your prices have gone up!"
    kid determined "I want to put a motor on this thing so I can make deliveries faster. It's going to take some money, though."
    him flirting "Well, you're still the best delivery girl on the entire planet, so I guess I have no choice!"
    kid happy "Da-ad..."
    him surprised "We going to see you at dinner tonight?"
    kid normal "Not tonight, I'm meeting some friends at Travis' place."
    him concerned "The bar?"
    kid annoyed "It's mostly a restaurant! Besides, nothing else is open late."
    him normal "Okay, well, come back tomorrow and I'll have another load for you."
    kid happy "I will!"
    hide kid with moveoutleft
    "I could have just brought my crops to the storehouse myself, of course."
    "But I wanted an excuse to see [kid_name]. Ever since she moved out I hardly ever see her."
    show her with moveinright
    him determined "You just missed her."
    her concerned "Is she doing okay?"
    him concerned "She's expanding her business, which is good... but she lives in a tiny shack and probably eats terrible restaurant food all the time, and..."
    her happy "If that's the worst we have to worry about, then we're doing pretty good."
    him concerned "I guess so. I just..."
    her surprised "What?"
    him determined "I want more for her. When she was little, I'd watch her sleeping and imagine all the amazing things she could do with her life, and now..."
    her normal "There's nothing wrong with living an ordinary life. She's a good person. She has her own life but she still visits us and she supports herself. What more could you want?"
    him surprised "Doesn't it feel like a waste to you?"
    her determined "No! Is your life a waste because you spent it growing food instead of inventing vaccines or leading a revolution or discovering new planets?"
    him annoyed "No, of course not."
    her normal "Then hers isn't either. Besides, she's still young -- who knows what else she might do?"
    him flirting "Too bad you can't say the same thing about us."
    her flirting "Speak for yourself! I've still got a long life ahead of me."
    him normal "It's never to late to keep living, right?"
    her surprised "You don't regret the life we made here... do you?"
    him concerned "Regret this life...? No. No, I don't. It's been full of work and learning things the hard way, but also full of love and fun times and my favorite people."
    her happy "Good! I don't regret it, either. It took me a long time to get used to this planet and everything that's different, but now I love it. And I love you."
    him happy "Love you too, [her_name]."
    # TODO: write something a bit better here.

    "Ending 6/8 Ordinary Extraterrestrial Life"
    return

#7 ACi - studies sociology/biology online but lives with you
label ending_ACi:
    "Ending ACi."
    scene farm_interior with fade
    show kid normal at midright
    show her normal at center
    show bro normal at midleft
    with dissolve
    show him normal at quarterleft with moveinleft
    kid happy "Welcome home, dad!"
    him determined "Hey."
    her surprised "Rough day?"
    him normal "Just tired. I'm glad it's your turn to make dinner, [kid_name]."
    kid normal "Yeah, just don't expect fine cuisine, I'm not that good of a cook."
    him happy "As long as it's not writhing or a blackened husk I will eat it!"
    bro normal "Ugh, not the potato squash thing..."
    kid annoyed "What's wrong with the potato squash thing??"
    bro annoyed "It looks like something that came out of a sulfur vent."
    her determined "[bro_name]!"
    him happy "Ha ha, it does kind of look like that..."
    kid concerned "Not you, too!"
    him normal "...but it tastes really good, so thank you [kid_name]!"
    kid annoyed "I think [bro_name] should have to take a turn cooking dinner, too. Isn't he old enough to do that?"
    bro normal "I'm happy to cook mashed potatoes."
    kid angry "Is that the only thing you eat?!"
    her annoyed "Hey, kids, settle down. [kid_name] makes a good point, but Dad and I will talk about it and decide as parents if [bro_name] should start making meals."
    him normal "For now, let's just appreciate [kid_name]'s meal without comparing it to anything inedible."

    "The meal was actually pretty tasty, even though [bro_name] mostly just picked out the potatoes and mashed them on his plate."
    him surprised "How are your studies coming, [kid_name]?"
    kid happy "Great! Zaina said she would help me with astronomy, Thuc is teaching me Earth biology, and Sara's helping me with sociology. Every book is so Earth-centric, though."
    her flirting "It's almost as if that was the only planet humans lived on for thousands of years."
    kid normal "Well, it's not now, so they need to update their materials!"
    bro "Are you still trying to talk to the jellysquids?"
    kid concerned "Yeah, that's sort of my independent research project. Along with comparing everything I learn about Earth science to what I can actually observe here on Talaam."
    him happy "Wow... my daughter is doing cutting edge alien research... this is so cool!"
    bro "Is the astronomy very different?"
    kid normal "Well, instead of looking for Jupiter and Saturn I look for Sol and the other planets in our system, but a lot of the constellations and galaxies are not too different."
    him surprised "Really? The stars seem completely foreign from what I remember from Earth..."
    kid "Well, the axis of rotation is a little different so the hemispheres don't exactly match up, but I can show you a really cool nebula."
    him "I'd like that."
    scene stars with fade
    "We ended up watching the stars together. [kid_name] had borrowed a telescope that she setup, and [her_name] brought out some blankets."
    "[bro_name] and [kid_name] argued about how solar flares affected Talaam's evolutionary past, and [her_name] snuggled up against my shoulder."
    "I was so proud of these kids... I didn't know exactly what they would accomplish, but for right now I was just enjoying being together."

    "Ending 7/8 The Stars are Right"
    return

#8 ACI - becomes an expert in her field, starts to form her own happy family on Talaam
label ending_ACI:
    "Ending ACI."
    "[her_name] moved out. We all pitched in to build a dorm-style apartment building for the growing number of non-farmers that didn't need a lot of space."
    "She seemed to like it; it was closer to town, where she spent most of her time in the library and at the science lab studying biology and sociology."
    # TODO: should your convo about marriage affect this?
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
    him surprised "A whole city? How come we never knew about it?"
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
    kid normal "Well, that's what I wanted to tell you! A non-profit group on Earth, the Extraterrestrial Allies Foundation, has approved a grant to pay us for our work, obtain equipment, and send more researchers here to Talaam."
    if (miners > 10):
        oleg "RET made a large donation, too, I think on Brennan's advice."
        him annoyed "They're probably hoping the jellysquids will lead them to more mineral deposits."
    kid normal "Anyway, enough about me. I want to know what you've been up to, [bro_name]."
    bro "Me?"
    kid happy "Yeah!"
    bro "Just...just regular stuff."
    her happy "He's actually been studying sunspots and solar flares lately."
    kid surprised "Really?"
    bro "Yeah... I've been trying to make a computer model so we can predict solar flares long-term more accurately, but the physics engines just aren't good enough to simulate the sunspots. But with enough data-"
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
    her flirting "I don't see any old people in here..."
    show him happy
    show her happy
    with dissolve
    "We laughed, and talked, and joked around while doing the dishes together. [bro_name] got out his source code to show Oleg, and [her_name] was asking [kid_name] about alien physiology, and I just felt happy to be in the middle of it all."

    "I want a lot of things for [kid_name], but most of all I want her to find some of this same happiness I've found. Happiness in love, in family, in community."
    "The kind of happiness you feel after working hard all day to accomplish something amazing and coming home to people who love you and forgive you and want you to be your best."

    "So I'm not just happy that she and Oleg are dating."
    "I'm not just happy that she's staying here, on Talaam."
    "I'm also happy she found a way to do something she loves that helps people."
    "She's working hard to understand the jellies in a way that no one else can."
    "With her research and mediation, I see a bright, peaceful future ahead for her."
    "And I'll get to see it all happen."

    "Ending 8/8, The Future is Bright"
    return

# COMMUNITY ENDINGS
# TODO: Add some dialogue/messages/interaction with others instead of just narration?
# TODO: Add some sprites/backgrounds to go with each thing?

label ending_CMiMa:
    "Over the next few years, our colony flourished."
    "We still had pests, and plants died or didn't grow quite as we thought they would sometimes."
    "But we had enough food that sharing wasn't a problem."
    "RET continued to support us with supplies, and eventually we became more self-sufficient."
    "The miners continued their jobs, and many stayed on Talaam after retiring."
    "Even though our colony was doing fine, every once in a while, a family would join Pete and the mavericks."
    "Their low-tech hacks inspired creativity and making do with less."
    # TODO: heavy rains in "good" endings, but they cope somehow?
    return

label ending_CMima:
    "Over the next few years, our colony flourished."
    "We still had pests, and plants died or didn't grow quite as we thought they would sometimes."
    "But we had enough food that sharing wasn't a problem."
    "RET continued to support us with supplies, and eventually we became more self-sufficient."
    "The miners continued their jobs, and many stayed on Talaam after retiring."
    "The mavericks, however, had a hard time surviving, and by the end of a few years, most had died or rejoined the colonists."
    "Pete insisted on living on his own even when everyone else had given up."
    return

label ending_CmiMa:
    "Over the next few years, our colony flourished."
    "We still had pests, and plants died or didn't grow quite as we thought they would sometimes."
    "But we had enough food that sharing wasn't a problem."
    "The miners weren't doing well though, and RET struggled to support them."
    "Another company bought out RET but they didn't improve things."
    "I was surprised to hear that Brennan joined the mavericks after declaring his disgust with the new management."
    "One day, all the miners quit their jobs. Some joined the colony."
    "Others tried living on their own and ended up stealing food from us, but eventually we worked things out."
    # TODO: More details?? Sounds interesting!
    return

label ending_Cmima:
    "Our colony kept on going like it always had."
    "We were focused on our own needs."
    "The miners didn't do well enough to support RET, and another company bought them out."
    "I was surprised when Brennan quit his job and took up farming after declaring his disguist with the new management."
    "One day, all the miners quit their jobs. Some joined the colony."
    "The mavericks weren't doing well either, and an outbreak of a foodborne illness left many of them sick or dead."
    "Many joined back with the colony if they were well enough."
    "Pete insisted on living on his own even when everyone else had given up."
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
