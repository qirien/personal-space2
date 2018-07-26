##
# ENDINGS
#

# Determine which ending the user should receive, depending on Terra's stats.
# TODO: Add community ending
label ending:
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
    "She hugged me briefly, and then walked away."
    hide kid with moveoutright
    "Just like that, she was gone from my life."
    "I never saw her again."
    him angry "How could you let her sign a contract like that without even mentioning it to us?!"
    brennan "It's not my fault if you don't know what's going on in your own kid's life."
    her "Brenann!"
    brennan "Sorry, but it's true. You're a fine farmer, [his_name], and a decent liason, but you're a terrible father."
    him "Since when do you know anything about being a father? Oh wait, you've probably got bastards on several planets by now. I'm sure you're a wondeful father to them."
    brennan "Before I came back I decided to make sure I'd never be a father. Seems like you should have done the same."
    her "Enough! This might be the last time you see each other. Do you really want the other person to remember you this way?"
    him "I'd be happy if he never thought of me again."
    brennan "I'm sorry, [her_name]. I wouldn't want your last memories of me to be sad ones."
    her "Will you look out for [kid_name]? I know you said you never wanted to be a father..."
    brennan "I'm now her manager. Yes, I'll watch out for her."
    "[her_name] glared at me. I wanted to get in one last barb at Brennan, to hurt him so he'd feel as awful as I did. But I didn't want to hurt [her_name]."
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
    "She's trying to support herself with her delivery business, but with the miners gone, I can't imagine she's very successful."
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
    kid "Not anymore. The miners were my best customers, but they're gone now."
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

    "Ending 2/8 My Very Own Mistakes."
    return

#3 aCi - Gets sucked into a crappy marriage on Talaam with the first person who shows affection, but at least she won't die of starvation.
label ending_aCi:
    "Ending aCi."
    return

#4 aCI - Rejects your life and returns to Earth to fulfill her dreams and she succeeds, becoming an awesome __________ (or studies jellypeople?), though you worry about her lack of friends/family
label ending_aCI:
    "Ending aCI."
    her "It's not too late to change your mind. You could complete your studies here..."
    kid "I know, mom, but all the good astronomers and equipment are on Earth. I want to become the best, so that's where I need to go."
    him "Study hard, [kid_name]. Make us proud."
    kid sad "I'm trying, dad."
    her "We are proud. And you'll always have a home here, no matter what happens."
    kid "Maybe I can convince someone to setup some real telescopes here. We could study the solar flares, the local solar system..."
    her "If you want to. But, oh, I'm so excited for you to experience Earth! You might even get to meet your cousins."
    kid "I'm excited to see a rain forest. Or any forest at all, actually."
    bro "Send us pictures!"
    him "Don't forget us."
    kid "I'll send you messages when I can."
    brennan "Careful, or you'll end up stuck here for another 12 years. The shuttle's leaving!"
    kid "Okay! Bye mom! Bye dad!"
    her "Goodbye, [kid_name]! We love you!"
    "She hoisted her duffle bag onto her shoulder and boarded the shuttle. I couldn't believe it was really happening. Our baby was leaving."
    bro "Goodbye!"
    "I didn't know what to say. All I could think about were the things I didn't have a chance to teach her, to tell her."
    him "Goodbye!"
    
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

#6 AcI - like #8, sets out on her own, but you worry she will not know enough or be able to work hard enough
label ending_AcI:
    "Ending AcI."
    return

#7 ACi - starts a farm nearby, asks you for help all the time, second-guesses herself
label ending_ACi:
    "Ending ACi."
    return

#8 ACI - becomes an expert in her field, starts to form her own happy family on Talaam
label ending_ACI:
    "Ending ACI."
    "I want a lot of things for [kid_name], but most of all I want her to find some of the same happiness I've found.  Happiness in love, in family, in community."
    "The kind of happiness you feel after working hard all day to accomplish something amazing and coming home to people who love you and forgive you and want you to be your best."

    "So I'm not just happy that she's dating the nicest young man on the entire planet."
    "I'm not just happy that she's staying here, on Talaam."
    "I'm also happy she found a way to do something she loves that helps people."
    "She worked hard to earn a dual degree in sociology and biology, and she has learned to understand the jellies in a way that no one else can."
    "With her mediating between the colony and the jellies, I see a beautiful future of peace ahead."
    "And I'll get to see it all happen."

    "Ending 8/8, Happily Ever After Starts Here"

    return
