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

    # TODO: remove debug code
    $ parenting_style = get_parenting_style()
    "Reached ending. Attachment: [total_attachment], Competence: [total_competence], Independence: [total_independence]. Marriage: [marriage_strength], Style: [parenting_style], Trust: [trust].  Colonists: [total_colonists], Miners: [total_miners], Mavericks: [total_mavericks]. Please screenshot this ('s') and send it with your feedback."
    # community ending
    # TODO: is this too high? too low?
    if (total_colonists >= FACTION_HIGH):
        $ achieved("It Takes This Village")
        if (total_miners >= FACTION_HIGH):
            $ achieved("Miner Details")
            if (total_mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")                
                call ending_CMiMa
            else:
                call ending_CMima
        else:
            if (total_mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_CmiMa
            else:
                call ending_Cmima
    else:
        if (total_miners >= FACTION_HIGH):
            $ achieved("Miner Details")
            if (mavericks >= FACTION_HIGH):
                $ achieved("Don't Tread on Me")
                call ending_cMiMa
            else:
                call ending_cMima
        else:
            if (total_mavericks >= FACTION_HIGH):
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

    # Set multi-persistent variables about this playthrough
    if not persistent.times_beaten:
        $ persistent.times_beaten = 1
    else:
        $ persistent.times_beaten += 1

    if renpy.variant('pc'):
        $ mp.jack_name = his_name
        $ mp.kelly_name = her_name
        $ mp.baby_name = kid_name
        $ mp.bro_name = bro_name
        $ mp.save()
    
    if persistent.crops_unlocked is None:
        $ persistent.crops_unlocked = set()
    $ i = 0
    while (i < len(crop_info)):
        if crop_info[i][ENABLED_INDEX]:
            $ persistent.crops_unlocked.add(crop_info[i][NAME_INDEX])
        $ i += 1
    $ renpy.save_persistent()

    scene stars with fade
    show text "{size=140}{font=fonts/SP-Marker Font.otf}The End{/font}{/size}" with dissolve
    stop music fadeout 3.0
    $ renpy.pause(3.0, hard=skippable)

    "Thank you for playing Our Personal Space 2: Space to Grow!"
    "New Game+ unlocked! Bonus section unlocked!"

    $ renpy.full_restart()
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
    brennan sad "[her_name]. I just wanted to say I'm sorry."
    her surprised "Sorry for what?"
    brennan concerned "That [kid_name]'s leaving. I tried to convince her to stay, but after everything she told me... well, I can't blame her."
    him annoyed "Leaving? Leaving for where?"
    brennan flirting "Earth, of course. Where else would we be headed?"
    him angry "She's NOT going with YOU!"
    brennan angry "Of course not. She's traded places with Anya so she can be with Lorant. I thought you knew."
    her determined "No. We did not."
    him surprised "There she is!"
    show kid determined at midleft with moveinleft
    show brennan at left with move
    her concerned "[kid_name]! You-- you're leaving?!"
    kid annoyed "Yeah."
    him angry "Like hell you are! You take that bag right back home right now!"
    brennan explaining "Sorry, she's a legal adult and she signed a contract."
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
    brennan concerned "It's not my fault if you don't know what's going on in your own kid's life."
    her surprised "Brenann!"
    if (miners_strong()):
        brennan angry "Sorry, but it's true. You're a fine farmer, [his_name], and a decent liaison, but you're a terrible father."
    else:
        brennan angry "Sorry, but it's true. You may be a decent farmer, but you're a terrible father."
    him angry "Since when do you know anything about being a father? Oh wait, you've probably got bastards on several planets by now. I'm sure you're a {b}wonderful{/b} father to them."
    brennan flirting "Before I came back I decided to make sure I'd never be a father. Seems like you should have done the same."
    her angry "Enough! This might be the last time you see each other. Do you really want the other person to remember you this way?"
    him annoyed "I'd be happy if he never thought of me again."
    brennan sad "I'm sorry, [her_name]. I wouldn't want your last memories of me to be sad ones."
    her concerned "Will you look out for [kid_name]? I know you said you never wanted to be a father..."
    brennan explaining "I'm not her father. But... I am her manager. Yes, I'll watch out for her."
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
    her cry "None of that will bring my baby back."

    $ achieved("Bring Back My Baby")
    "Ending 1/4: Bring Back My Baby."
    window auto hide
    show ending1_cg
    $ renpy.pause()    

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
    thuc happy "Yeah, this is the most painful shot I've ever had, and you haven't even pierced the skin yet!"
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
    if family30_leaving:
        her concerned coat "It's just... after tomorrow, she'll be gone, and I won't be able to help her anymore."
        him content "We've been helping her for her whole life... it's time for her to move on. There will be people on Earth who can help her out."
        her sad coat "But no one knows what's best for her as well as we do!"
        him surprised "That's true. I wish we could go with her..."
        her concerned coat "But we can't."

        scene plain with fade
        show kid normal at quarterright
        show her concerned at center
        show him concerned at midleft
        show bro concerned at quarterleft, flip
        with dissolve
        her sad "It's not too late to change your mind. You could complete your studies here..."
        kid concerned "I know, mom, but I want to be a real doctor, not just your apprentice. I want to become the best, so Earth is where I need to go."
        him determined "Study hard, [kid_name]. Make us proud."
        kid sad "I'm trying, dad."
        her determined "We are proud. And you'll always have a home here, no matter what happens."
        him annoyed "Don't get caught up with stupid college stuff, all right? Stay away from cheating and drugs and wild parties and boys and... pretty much just stay in your room the whole time."
        her normal "Not the whole time! Oh, I'm so excited for you to experience Earth! You might even get to meet your cousins."
        kid normal "I'm excited to see a rain forest. Or any forest at all, actually."
        bro normal "Send us pictures!"
        him excited "Wow, my little daughter, on her way to med school..."
        kid sad "Oh no...What if I can't do it? What if I really suck at taking care of myself? What am I thinking; I've never even been to a real school!"
        her normal "No backing out now! You'll be fine. I promise."
        him normal "Don't forget us."
        kid concerned "I'll send you messages when I can."
        show brennan flirting at right with moveinright
        brennan flirting "Careful, or you'll end up stuck here for another 12 years. The shuttle's leaving!"

        kid blush "But... I don't know if I can do this!"
        him determined "You can and you will! Now, get on that shuttle!"
        her surprised "Goodbye, [kid_name]! We love you!"
        "She hoisted her duffle bag onto her shoulder and boarded the shuttle. I couldn't believe it was really happening. Our baby was leaving."
        bro sad "Goodbye!"
        "I didn't know what to say. All I could think about were the things I didn't have a chance to teach her, to tell her."
        "What if she started failing her classes? What if she didn't cook herself good enough food? What if she made huge mistakes and didn't apologize? What if her heart was broken?"
        "It was too late for me to teach her those things. She'd have to learn from her own mistakes, now."
        hide kid
        hide brennan
        with moveoutright
        him surprised "Goodbye!"

    else:
        her concerned coat "Yeah...maybe."

        scene hospital with fade
        show kid determined at midright with dissolve
        show him surprised at midleft with moveinleft
        "Before I left, I peeked in the other room to check on [kid_name]. She was studying her anatomy book with a ferocious energy, as though it were her opponent in deadly combat."
        "I smiled at her, proud of her hard work. I almost told her so, but I stopped myself just in time. I didn't want her to get overconfident."
        show kid angry with dissolve
        "She saw my smile, but didn't say anything, just nodded and continued reading, her forehead scrunched up in concentration."

    $ achieved("Proving Herself")
    "Ending 2/4: Proving Herself."
    window auto hide
    show ending2_cg
    $ renpy.pause()    
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

    if (boyfriend_name == "Oleg"):
        kid normal "Not tonight, I'm going to Oleg's."
    elif (boyfriend_name == "Travis"):
        kid normal "Not tonight. I'm helping Travis at DinerMight."
        him concerned "Is he going to pay you for all the free waitressing you do?"
        kid normal "He pays me in meals! His pancakes are the best. Besides, it's the only chance we have to be together."
    else:
        kid normal "Not tonight, I'm meeting some friends at DinerMight."
        him concerned "Travis' bar?"
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
    "I remember when she was little, she wasn't afraid of anything."
    scene ocean with fade
    show child at center with dissolve
    "She couldn't wait to do new things like go to school or go to the beach."
    scene sunset with fade
    show kid nervous at center with dissolve
    "Now, when I ask her what she sees in her future, she just shrugs."
    "She's changed a lot...but in some ways, she's still a kid."
    "That's fine for now, but part of me wants more for her."
    "Should I have taught her more, made her work harder?"
    "I can't stop thinking these kinds of things..."
    "I guess that's part of what it means to be a parent."

    $ achieved("Forever My Little Girl")
    "Ending 3/4: Forever My Little Girl"
    window auto hide
    show ending3_cg
    $ renpy.pause()
    return

#4 AC - becomes an expert on the jellies, starts to form her own
#       happy web of relationships on Talaam
label ending_AC:
    "Ending AC"
    scene stars with fade
    "[kid_name] moved out. We all pitched in to build a dorm-style apartment building for the growing number of non-farmers that didn't need a lot of space."
    "She seemed to like it; it was closer to town, where she spent most of her time in the library and at the science lab studying biology, astronomy, and sociology."
    if (boyfriend_name == "Oleg"):
        "And she was closer to her boyfriend, Oleg."
    elif (boyfriend_name == "Travis"):
        "And she was closer to her boyfriend, Travis, and her other friends, like Oleg."
    else:
        "And she was closer to her friends, especially Oleg."
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
    oleg angry "It never showed up on our scans because one, it's underwater, and two, it's completely made out of living, organic materials, so it just looked like a coral reef or something."
    kid normal "Oleg's made an app to help us map their city, and another to help us communicate better with them."
    him determined "Better communication would definitely be a good thing."
    if jellypeople_happy:
        kid happy "I'm just glad you didn't mess up our first contact with them... they're still recovering from all the shells they lost, but since they moved and merged with another colony they've been doing much better."
    else:
        kid concerned "I'm just glad we were able to recover from that terrible first contact..."
        him surprised "Did they ever find shells for their babies?"
        kid determined "No, but they merged with another colony and have been able to grow more since then."

    him concerned "This sounds like great research..."
    kid annoyed "...but you wonder how I'm going to make a living, right?"
    him flirting "We do prefer our daughter not to starve to death."
    if (independence >= INDEPENDENCE_HIGH):
        kid normal "Well, that's what I wanted to tell you! A non-profit group on Earth, the Extraterrestrial Allies Foundation, has approved a grant to pay us for our work, obtain equipment, and send more researchers here to Talaam."
        if (miners_strong()):
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
    oleg happy "-you'll be able to improve the model, and also improve predictions! That's great! Which physics engine are you using as a base?"
    show kid happy with dissolve
    "I listened to my family talk. I didn't understand half of what Oleg and [bro_name] were talking about, but I loved to see [bro_name] excited about something."
    if (boyfriend_name == "Oleg"):
        "[kid_name] reached over and held Oleg's hand, and he squeezed it back as he extolled the virtues of his favorite physics engine."
    else:
        "[kid_name] listened as Oleg extolled the virtues of his favorite physics engine."
    "I put my arm around [her_name] and pulled her close just as she was about to put a forkful of food in her mouth."
    "The food fell on her lap and she elbowed me in mock indignation."
    her flirting "Oh, now look one you've done. You've ruined my fanciest clothes."
    him flirting "Want me to help you clean that off?"
    her happy "Mom, Dad, can you not? Some of us are trying to eat here."
    oleg normal "I don't know; it's kind of sweet to see old people that are still so in love."
    him surprised "Old people?!"
    her surprised "I don't see any old people in here..."
    show him happy
    show her normal
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

    if (boyfriend_name == "Oleg"):
        "So I'm not just happy that she and Oleg are dating."
    else:
        "So I'm not just happy that she found such a good friend in Oleg."
    "I'm not just happy that she's staying here, on Talaam."
    "I'm also happy she found a way to do something she loves that helps people."
    "She's working hard to understand the jellies in a way that no one else can."
    "With her research and mediation, I see a bright, peaceful future ahead for her."
    "And I'll get to see it all happen."

    $ achieved("The Stars are Bright")
    "Ending 4/4: The Stars are Bright"    
    window auto hide
    show ending4_cg
    $ renpy.pause()

    return

#############################################################################
# COMMUNITY ENDINGS
#############################################################################

label ending_CMiMa:
    $ c_end = "CMiMa"
    "Community Ending CMiMa"
    scene bonfire with fade
    show pete normal at center
    show him normal at midleft
    show brennan normal at midright
    brennan happy "You've really never heard of quince? It's a common Earth fruit."
    pete happy "Even I've heard of it, and I grew up in the middle of nowhere."
    him blush "Well, I was kind of a picky eater growing up, so we didn't eat weird things like that."
    brennan flirting "It's a good thing you grew out of that, since weird things are {i}de rigueur{/i} these days."
    pete normal "They're not even weird anymore. I've gotten to craving these wolfslug curry kebabs year-round."
    him pout "If I drink the wine Brennan made while I eat the curry kebabs, I almost feel like I'm in a fancy restaurant. All we need is a French waiter in a tuxedo."
    "Brennan stood and bowed, imitating a waiter with a terrible French accent."
    brennan normal "Mais oui! Please accept our apologies for the very limited wine menu. I'm afraid nonvintage is all we have at the moment."
    pete happy "It beats a nonexistent wine menu every time."

    "I enjoyed another bite of wolfslug kebab, the tangy, spicy curry sauce dripping down my chin. I wiped it off with a piece of the flatbread I had brought and ate that, too."

    him happy "Thanks for saving my wheat from that flood. I still can't believe we got everyone and their food stores out so quickly."    
    brennan explaining "You act like it was an act of altruism, but really, I'd do almost anything not to have to grow my own food."

    him normal "Speaking of people who hate growing their own food, how are your interns from the high school working out?"
    him pout "I know some of them are hoping to learn a trade other than farming."
    brennan normal "Oh, I have one intern who has a knack for assembling good mining teams."
    brennan "He made friends with everyone and figured out their compatibilities quickly."
    pete normal "One of my interns has an amazing spatial memory. She can go foraging with me and then come back and draw a map."
    pete happy "With satellite imagery, we have the big things covered, but her maps take out all the extra noise and make it easier to find things."
    him determined "Huh, good for you. My intern seems kind of depressed sometimes. I think she likes handicrafts though. I should have her spend some time with you, Pete."
    him surprised "She might like leatherworking better than farming."
    pete happy "If she likes working with her hands, maybe she could make you a saddle for one of those grass crabs!"
    him sad "I do miss Lettie."
    brennan surprised "Why did they send just one horse?"
    him smirk "RET promised me I could bring any one thing to help me with farming. So I chose Lettie."
    pete normal "I'm surprised they let you do that, and even more surprised she survived the journey."
    him normal "It was in the contract!"
    him sad "They would never let more horses come here now though. Not with all the extra-planetary environmental sanctions."
    pete angry "Hey, no horse could replace Lettie. But who knows, maybe one of these huge alien critters can be domesticated."
    brennan normal "I'm happy to let Zaina find some likely candidates for domestication this rainy season."

    scene ocean_sunset
    "There were times when I wasn't sure we would all survive, let alone get along together."
    "To think that I would voluntarily spend time with Brennan..."
    "And even though Pete left the colony, we still make time to see each other and help each other out."
    "I'm glad I have so many people I can rely on."

    return

label ending_CMima:
    $ c_end = "CMima"
    "Community Ending CMima"
    jump flood_ending_C

label ending_CmiMa:
    $ c_end = "CmiMa"
    "Community Ending CmiMa"
    jump flood_ending_C

label ending_Cmima:
    $ c_end = "Cmima"
    "Community Ending Cmima"
    jump flood_ending_C

label ending_cMiMa:
    $ c_end = "cMima"
    "Community Ending cMiMa"
    jump flood_ending_c

label ending_cMima:
    $ c_end = "cMima"
    "Community Ending cMima"
    jump flood_ending_c

label ending_cmiMa:
    $ c_end = "cmiMa"
    "Community Ending cmiMa"
    jump flood_ending_c

label ending_cmima: #is this ending even possible?
    $ c_end = "cmima"
    "Community Ending cmima"
    scene farm_exterior with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout at midleft
    him "It sure is raining a lot this week. The river's waters have been rising and the rain shows no sign of stopping."
    nvl clear
    him_c "Hey, is there a flood warning or anything? It looks like the river could bust its banks any minute."
    thuc_c "Didn't you hear? Zaina told everyone within a kilometer of the river to evacuate today."
    him_c "Um, no, I didn't see anything like that."
    thuc_c "Huh. One of my kids told me about it. Maybe she only sent it out to the miners?"
    him_c "Where should we evacuate?"
    thuc_c "I dunno. I'd offer my place but we have to evacuate too."

    him sad "I guess we could go to the community center? That's almost a kilometer away from the river."
    scene farm_interior with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show her normal at midright
    show him determined at midleft with moveinleft
    with fade
    him "Hey, I heard that it's supposed to flood! We need to load up the wagon and move stuff."
    her surprised "Why didn't we hear about this sooner?"
    him sad "I don't know, maybe Zaina sent an e-mail to the miners but forgot about us colonists?"
    her nervous "How much is it supposed to flood? Do we need to take everything?"
    him determined "It looks like that's what Thuc's family did."
    her_c "How much is it supposed to flood? Can just empty our cellar and be okay?"
    thuc_c "I don't know, but it's supposed to keep raining for another week or two!"
    him pout "Let's take as much as we can. Unfortunately none of the solar batteries are fully charged right now though..."
    her determined "We'll have to pull the wagon ourselves. Got it."

    scene farm_exterior with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout at midleft behind rain with dissolve
    show her nervous at midright behind rain with dissolve
    her "If we load the wagon up too high, we'll never get it through the mud."
    him "I know. I just hate to waste any food."
    her determined "Let's prioritize the dried meats and fruit, which will be the lightest and most calorie dense."
    him determined "Right."
    "We managed to get a load to the community center."

    scene community_center with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show him determined at midleft with dissolve
    show her determined at left with dissolve
    show ilian angry at midright with dissolve
    ilian "Why are you bringing that here?"
    him doubt "I figured it would be less susceptible to flooding here?"
    ilian normal "No, you need to take it to higher ground. It's likely to flood in the night here."
    him pout "Okay, then... where?"
    ilian angry "Like I know. No one tells me anything!"
    him doubt "I guess we'll look around and see what everyone else is doing..."

    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout at midleft behind rain with dissolve
    show her nervous at midright behind rain with dissolve
    "We took our wagon up the foothill towards the miner's camp. Other colonists had found places to stay here, with tents popping up every now and then."
    "We set up a temporary shelter, but it was still very wet. We were able to get another light load up, but most of our food storage was ruined by the flood."
    stop sound fadeout 1.0
    
    return

label flood_ending_C:
    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout behind rain at midleft
    show ilian angry at midright behind rain
    with dissolve
    him "After this next load, will we be done moving supplies?"
    ilian "No, we need to get at least two more loads to the old mining camp."
    him doubt "I wish I had harnesses for the cows. This is their kind of work."
    ilian normal "Our cattle would make lousy cart-pullers. Cattle wouldn't be able to handle the slippery stairs very well either."
    him sad "I still have to move our supplies to higher ground. How much flooding is expected in the next four hours?"

    if (c_end == "CMima"):
        ilian angry "Zaina calculated a good four inches, possibly more if the river floods its banks."
        ilian normal "Just ask Brennan or Chaco for help. Brennan volunteered the off-duty miners."
    if (c_end == "CmiMa"):
        ilian angry "Pete was saying that the rainfall hasn't been this heavy since we arrived. The river might even flood its banks in the next few hours."
        ilian normal "Pete and some of the others have been helping to move stuff, since their camp is already on high ground."
    if (c_end == "CMima" or c_end == "CmiMa"):
        him content "I hate asking other people for help, but it sure beats losing all my stored grain."
        ilian happy "Hey, I know that feeling. We can do this if we work together."
    if (c_end == "Cmima"):
        ilian angry "Zaina calculated a good four inches, possibly more if the river floods its banks."
        ilian normal "I would help you, but I've got my own stuff to move after this."
        him cry "I won't be able to bring up everything. Guess I'll say goodbye to my barrels of apples."
        ilian angry "Ask around. Maybe Thuc and Julia can help you, since their kids already moved their storage this morning."

    "After two more loads, I went home to do some more pushing and pulling."

    if (c_end == "CMima"):
        scene farm_exterior with fade
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

    if (c_end == "CmiMa"):
        scene farm_exterior with fade
        show rain
        show him surprised behind rain at midleft
        show pete normal behind rain at midright
        show travis normal behind rain at center
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
        show him normal at midleft behind rain with moveinleft
        show her normal at midright behind rain
        with dissolve
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

    if (c_end == "Cmima"):
        scene farm_exterior with fade
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

    stop sound fadeout 1.0
    return

label flood_ending_c: #for cMiMa, cmiMa, and cMima, but not cmima
    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him pout behind rain at midleft
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        show pete angry at midright behind rain
        with dissolve
    if (c_end == "cMima" or c_end == "cMiMa"):
        show brennan concerned at right behind rain
        with dissolve
    him "Thanks for warning me about the flood and for helping us evacuate."
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        pete happy "You might be working for an evil corporation, but you don't deserve to die of starvation after a flood ruins your food storage."
        him pout "Wait, are you saying the other colonists do deserve that?"
        pete normal "I don't know them personally like I do you."
    if (c_end == "cMima" or c_end == "cMiMa"):
        brennan explaining "You know, it's in our best interest to keep at least one farmer happy."
        him pout "Aren't you helping the others?"
        brennan flirting "We don't have time to move everyone, so I chose the farmer I hate the least."
        him smirk "Ha. That makes sense."
    him surprised "Do the other colonists even know about the flood?"
    if (c_end == "cMiMa"):
        pete happy "Not my circus..."
        brennan explaining "Not my monkeys!"
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        pete happy "If they haven't figured out there's a flood at this point, I'm not sure that a message would help."
    if (c_end == "cMima" or c_end == "cMiMa"):
        brennan surprised "I think it would be obvious by now."
    him determined "We should at least check the storehouse. The food stored there can help feed everyone."
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        pete normal "Fine with me."
    if (c_end == "cMima" or c_end == "cMiMa"):
        brennan normal "You make a good point. Let's see how they're doing."
    "We finished taking the last of my food storage to the evacuation camp in the foothills and headed to the storehouse."

    scene storeroom with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show him determined at center with dissolve
    show ilian angry at midright with dissolve
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        show pete normal at midleft with dissolve
    if (c_end == "cMima" or c_end == "cMiMa"):
        show brennan concerned at left with dissolve
    ilian "What do you guys want?"
    him normal "Do you need any help moving the storehouse goods before the flood comes in?"
    ilian normal "Pshh. I'm not going to fall for that kind of trap. You just want all our food for yourselves."
    ilian angry "According to the RET contracts, food not in the storehouse doesn't belong to RET anymore."
    him doubt "But if we don't move it, it will be ruined and no one will be able to eat it."
    ilian "Only if the flooding is as bad as Zaina says, but wouldn't she be motivated to get the food out of our dirty colonists' hands?"
    him pout "I don't think she feels that way about colonists..."
    him "How much food is back there, anyway?"
    ilian normal "None of your business."
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        show pete normal at right with move
        pete "There's scarcely enough to feed one family back here."
    if (c_end == "cMima"):
        show brennan sad at right with move
        brennan "There's only three barrels back here. I thought there would be more."
    ilian angry "Hey, authorized personnel only!"
    ilian "People haven't been bringing in their crops to the storehouse. They said it was too much trouble."
    him sad "I see. I hope they're able to save their food storage from the flood."

    scene path with fade
    play sound "sfx/rain.ogg" loop
    show rain
    show him sad behind rain at midleft
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        show pete normal at midright behind rain
        with dissolve
    if (c_end == "cMima" or c_end == "cMiMa"):
        show brennan concerned at right behind rain
        with dissolve
    him "That went worse than I expected."
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        pete "You colonists need to get organized or something worse than a flood is going to wipe you out."
    if (c_end == "cMima" or c_end == "cMiMa"):
        brennan "I had no idea things were this bad. Someone needs to come in and cut the crap."
    him "I guess no one wants to take responsibility."
    if (c_end == "cmiMa" or c_end == "cMiMa"):
        pete "I can see that. Run along now; [her_name]'s waiting for you in the temporary shelter."
    if (c_end == "cMima"):
        brennan "No kidding. You better see how [her_name] is doing. She's probably worried about you."

    scene shack with fade
    play sound "sfx/rain.ogg" volume 0.6 loop
    show rain
    show him normal at midleft with moveinleft
    show her normal at midright
    her "You made it! Welcome to our temporary home."
    him "I'm relieved, but somehow I'm not feeling glad."
    her annoyed "Yeah, this was so disorganized. I'm sure in a few weeks I'm going to be hearing about how so-and-so didn't get any help and nearly died."
    him sad "It's a shame. I feel like we could have done better."
    her concerned "At least we have friends who can help us when we need it."
    him normal "Yeah."
    if (c_end == "cmiMa"):
        "Had I focused too much on helping Pete's group, to the detriment of my other relationships?"
        "I can't be everything to everyone. At least Pete's still a good friend."
    if (c_end == "cMima"):
        "Did I focus too much on pleasing the miners, when I should have tried to balance things out a little more?"
        "At least RET's interests are secured, and they can continue supporting us."
    if (c_end == "cMiMa"):
        "Had I focused too much on trying to make sure the miners and Pete's group were happy, neglecting the issues in my own community?"
        "I feel like I could only do so much. There's always going to be something left undone."

    stop sound fadeout 1.0
    return