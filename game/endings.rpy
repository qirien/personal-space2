##
# ENDINGS
#

# Determine which ending the user should receive, depending on Terra's stats.
label ending:
    "[kid_name]'s childhood was so different from my own. Instead of playgrounds and toys, she had alien creatures and mining conflicts."
    "I guess we both had parents, and friends, and problems."
    "Some things are always the same."

    # TODO: community ending stuff
    # Talk about miners, colonists, luddites, and jellies



    # TODO: work/farm ending stuff?

    # TODO: remove debug code
    "Reached ending. Attachment: [attachment], Competence: [competence], Independence: [independence]"
    $ parenting_style = get_parenting_style()
    "Parenting style: [parenting_style]"
    if (attachment < ATTACHMENT_HIGH):
        if (competence < COMPETENCE_HIGH):
            # aci and acI
            if (independence < INDEPENDENCE_HIGH):
                jump ending_aci
            else:
                jump ending_acI
        else:
            # aCi and aCI
            if (independence < INDEPENDENCE_HIGH):
                jump ending_aCi
            else:
                jump ending_aCI
    else:
        if (competence < COMPETENCE_HIGH):
            # Aci and AcI
            if (independence < INDEPENDENCE_HIGH):
                jump ending_Aci
            else:
                jump ending_AcI
        else:
            # ACi and ACI
            if (independence < INDEPENDENCE_HIGH):
                jump ending_ACi
            else:
                jump ending_ACI

    call credits
    return

#1 aci - Blames you for everything. Clingy. Follows (miner?) boyfriend back to Earth but you know the relationship won't last.
label ending_aci:
    "Ending aci"
    her surprised "Where's [kid_name]? I thought she'd want to say goodbye to Anya."
    him surprised "I thought Anya was staying here, with Travis."
    her concerned "I thought they broke up..."
    him normal "I can't keep track of who's with who anymore!"

    brennan "[her_name]. I just wanted to say I'm sorry."
    her surprised "Sorry for what?"
    brennan "That [kid_name]'s leaving. I tried to convince her to stay, but after everything she told me... well, I can't blame her."
    him annoyed "Leaving? Leaving for where?"
    brennan "Earth, of course. Where else would we be headed?"
    him angry "She's NOT going with YOU!"
    brennan "Of course not. She's traded places with Anya so she can be with Lorant. I thought you knew."
    her determined "No. We did not."
    him "There she is!"
    her concerned "[kid_name]! You-- you're leaving?!"
    kid "Yeah."
    him angry "Like hell you are! You take that bag right back home right now!"
    brennan "Sorry, she's a legal adult and she signed a contract."
    her sad "Why would you do this?"
    kid "Lorant loves me. We're happy together. And I've always wanted to go to Earth."
    him determined "But we'll never see you again."
    kid "You hardly ever saw me when I lived with you, so I don't see what the big difference will be."
    her sad "Isn't there some way I can change your mind?"
    brennan "It's too late for that. The contract is signed."
    kid "Mom, I... I'm sorry. I love you, but I want to go."
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

    kid "Goodbye, dad."
    "She hugged me briefly, and then turned around. She ran to catch up to Lorant, clinging to his arm as they boarded the shuttle."
    hide kid with moveoutright
    "Just like that, she was gone from my life."
    "I never saw her again."
    him angry "How could you let her sign a contract like that without even mentioning it to us?!"
    brennan "It's not my fault if you don't know what's going on in your own kid's life."
    her "Brenann!"
    # TODO: adjust based on whether you are a good farmer/liason or not
    brennan "Sorry, but it's true. You're a fine farmer, [his_name], and a decent liason, but you're a terrible father."
    him "Since when do you know anything about being a father? Oh wait, you've probably got bastards on several planets by now. I'm sure you're a wondeful father to them."
    brennan "Before I came back I decided to make sure I'd never be a father. Seems like you should have done the same."
    her "Enough! This might be the last time you see each other. Do you really want the other person to remember you this way?"
    him "I'd be happy if he never thought of me again."
    brennan "I'm sorry, [her_name]. I wouldn't want your last memories of me to be sad ones."
    her "Will you look out for [kid_name]? I know you said you never wanted to be a father..."
    brennan "I'm not her father. But... I am her manager. Yes, I'll watch out for her."
    "[her_name] glared at me. I wanted to get in one last barb at Brennan, to hurt him so he'd feel as awful as I did. But I didn't want to hurt [her_name]."
    # TODO: give the user a choice about what to say here
    him "I... I'd appreciate that."
    "He nodded and boarded the shuttle. I looked at all the windows for [kid_name] and her boyfriend, but I couldn't see them anywhere. She didn't even wave goodbye."
    "[her_name] and I watched the shuttle lift off in silence. We ate a quiet dinner with [bro_name], and then [her_name] went to bed early."
    "I found her in our room, heaving great sobs."
    her sad "She's gone. My little girl. She's really gone."
    him concerned "We knew it would happen someday..."
    her annoyed "But not like this! She left because we failed her. And now we'll probably never see her again."
    him "It's not our fault she chose to go back to Earth with some idiot!"
    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):
        her "Isn't it? We never gave her any space! We tried to control her life and never let her make her own decisions!"
    elif (parenting_style == "authoritative"):
        her "Isn't it? Were we too strict? Not strict enough? Maybe I didn't spend enough time with her..."
    elif (parenting_style == "permissive"):
        her "Isn't it? We just let her do whatever she wanted! Why are we surprised when she keeps doing exactly that?!"
    else:
        her "Isn't it? We just weren't there for her often enough. We were too absorbed in our own lives..."
    him angry "You can't think that way!"
    her surprised "What do you mean?"
    him annoyed "You can't second-guess every decision you ever made. What's done is done."
    her sad "Then what are we supposed to do now?"
    him determined "The only thing we can do is try and be better than we were. Maybe she's back on Earth, but we can still send her messages. We can try and do better with [bro_name]."
    her concerned "That's true, but..."
    her sad "None of that will bring my baby [kid_name] back."

    "Ending 1/8, Bring Back my Baby."

    return

#2 acI - Rejects your life and joins luddites, but fails. Moves from one job to the next, but drives away people around her and isn't good at anything.
label ending_acI:
    "Ending acI."
    "Even though [kid_name] still lives on Talaam, I worry a lot about her."
    "She's trying to support herself with her delivery business, but with just a bike, she can't carry very much cargo."
    "I worry that she moved in with Travis because she needed a place to stay, not because she loves him."
    "I worry that she'll be too prideful to ask for help when she needs it."
    "And I worry that I didn't teach her enough for her to be out on her own already."
    "And the worst part about these worries is that, for the most part, I can't do anything about them."
    "I try to talk to her, to be there for her..."
    "...but she doesn't want anything to do with me."

    scene farm_exterior with fade
    show travis at midright
    show kid at center
    with dissolve
    show him at midleft
    with moveinleft
    him concerned "Hey, [kid_name]."
    kid "Dad. What are you doing here?"
    him "I just had some extra pickles and thought you might like some."
    "I held them out like I used to hold carrots out for Lettie when I was training her."
    "She looked at Travis, who shrugged and walked off."
    hide travis with moveoutright
    "She took the pickles but didn't get too close."
    kid "Thanks."
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
            kid "It's none of your business. You had your chance to be my dad when I was little and didn't have a choice. It's too late to start caring now."
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
    show her normal at midright
    show thuc normal at center
    show kid normal at midleft
    with dissolve
    kid surprised "Is this the right spot for the injection?"
    her determined "Not quite. Feel the bone there? Now come about two finger's width down... into that muscle there."
    kid nervous "Right here?"
    her concerned "Almost... a little lower. See, when you pinch it, it looks like this."
    kid sad "Maybe you should do it."
    thuc "Yeah, maybe you should do it, [her_name]. I'm starting to feel a little nervous!"
    her annoyed "She needs the practice! I'll make sure she does it right. Try again, [kid_name]."
    kid determined "Okay... right, um, here?"
    her concerned "Remember, find the triangle."
    thuc "This is the most painful shot I've ever had, and you haven't even pierced the skin yet!"
    kid surprised "Here?"
    her happy "Yes, that's right!"
    thuc "Ow!"
    kid concerned "Sorry!!"
    her determined "Slow down! Slow and steady... there."
    thuc "So, is that all I need?"
    her normal "Yes, let me know if you don't start feeling better by tonight."
    hide thuc with moveoutleft
    show him at quarterleft with moveinright
    him happy "Hello, lovely ladies! I brought you some lunch!"
    kid annoyed "I'm not hungry."
    hide kid with moveoutright
    him surprised "What's with her?"
    her concerned "I tried starting her with some basic hands-on nursing duties today... she's having a hard time."
    him determined "Well, she's smart, so I'm sure she'll catch on quickly."
    her annoyed "I hope so."
    him normal "I'm just glad she found something useful to do."
    her concerned "Yeah, I guess so."
    him surprised "What's wrong?"
    her determined "I'm not sure this is the right job for her."
    him determined "Well, if she's not going to help grow food, then helping people not die is a pretty good use of her talents."
    her concerned "She's not very good at it."
    him surprised "She's not?"
    her annoyed "No. She feels awkward touching people, and she's always second-guessing herself, and she has a hard time remembering what to do."
    him determined "I'm sure she just needs more practice. It takes a long time to learn to be a good medical professional, as you know very well."
    her concerned "Yes... I suppose so."


    kid concerned "I'm never going to be good enough!"

    "Ending 3/8, Never Good Enough."
    return

#4 aCI - Returns to Earth to study medicine, though you worry about her lack of friends/family
label ending_aCI:
    "Ending aCI."
    her "It's not too late to change your mind. You could complete your studies here..."
    kid "I know, mom, but I want to be a real doctor, not just your apprentice. I want to become the best, so Earth is where I need to go."
    him "Study hard, [kid_name]. Make us proud."
    kid sad "I'm trying, dad."
    her determined "We are proud. And you'll always have a home here, no matter what happens."
    him "Don't get caught up with stupid college stuff, all right? Stay away from the wild parties and the drugs and all that."
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
    "I kept expecting [kid_name] to get married and leave us, or go off to pursue her own dreams, but so far she seems content to keep things as they are."
    "She helps around the farm sometimes, but I still feel like I have to tell her how to do things and keep a close eye on her."
    "I remember when she was little, she wasn't afraid of anything, and she couldn't wait to do new things like go to school or go to the beach."
    "Now, when I ask her what she sees in her future, she just shrugs."
    "She's changed a lot...but in some ways, she's still a kid."
    "That's fine for now, but part of me wants more for her."
    "Should she want to leave home? Is it my fault that she doesn't? Should I have taught her more, somehow?"
    "I can't stop thinking these kinds of things."
    "I guess that's part of what it means to be a parent."

    "Ending 5/8, Forever My Little Girl"

    return

#6 AcI - like #5, but sets out on her own, but you worry she will not know enough or be able to work hard enough
label ending_AcI:
    "Ending AcI."
    return

#7 ACi - studies sociology/biology online but lives with you
label ending_ACi:
    "Ending ACi."
    return

#8 ACI - becomes an expert in her field, starts to form her own happy family on Talaam
label ending_ACI:
    "Ending ACI."
    "[her_name] moved out. We all pitched in to build a dorm-style apartment building for the growing number of non-farmers that didn't need a lot of space."
    "She seemed to like it; it was closer to town, where she spent most of her time in the library and at the science lab studying biology and sociology."
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
    him flirt "We do prefer our daughter not to starve to death."
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
    "The food fell on her lap and she elbowed me gently."
    her flirt "Oh, now look one you've done. You've ruined my fanciest clothes."
    him flirt "Want me to help you clean that off?"
    her happy "Mom, Dad, can you not? Some of us are trying to eat here."
    oleg "I don't know; it's kind of sweet to see old people that are still so in love."
    him surprised "Old people?!"
    her surprised "I don't see any old people in here..."
    "We laughed, and talked, and joked around while doing the dishes together. [bro_name] got out his source code to show Oleg, and [her_name] was asking [kid_name] about alien physiology, and I just felt happy to be in the middle of it all."

    "I want a lot of things for [kid_name], but most of all I want her to find some of this same happiness I've found.  Happiness in love, in family, in community."
    "The kind of happiness you feel after working hard all day to accomplish something amazing and coming home to people who love you and forgive you and want you to be your best."

    "So I'm not just happy that she and Oleg are dating."
    "I'm not just happy that she's staying here, on Talaam."
    "I'm also happy she found a way to do something she loves that helps people."
    "She's working hard to understand the jellies in a way that no one else can."
    "With her research and mediation, I see a beautiful future of peace ahead for her."
    "And I'll get to see it all happen."

    "Ending 8/8, Happily Ever After Starts Here"

    return
