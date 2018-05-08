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
    if (attachment < ATTACHMENT_GOOD):
        if (competence < COMPETENCE_GOOD):
            # aci and acI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_aci
            else:
                jump ending_acI
        else:
            # aCi and aCI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_aCi
            else:
                jump ending_aCI
    else:
        if (competence < COMPETENCE_GOOD):
            # Aci and AcI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_Aci
            else:
                jump ending_AcI
        else:
            # ACi and ACI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_ACi
            else:
                jump ending_ACI

    call credits
    return

#1 aci - Blames you for everything. Clingy. Follows (miner?) boyfriend back to Earth but you know the relationship won't last.
label ending_aci:
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

#2 acI - Rejects your life and joins luddites/returns to Earth to fulfill her dream of becoming a ________, but fails. Moves from one job to the next, but drives away people around her and isn't good at anything.
label ending_acI:
    "Ending acI."
    return

#3 aCi - Gets sucked into a crappy marriage on Talaam with the first person who shows affection, but at least she won't die of starvation.
label ending_aCi:
    "Ending aCi."
    return

#4 aCI - Rejects your life and returns to Earth to fulfill her dreams and she succeeds, becoming an awesome __________ (or studies jellypeople?), though you worry about her lack of friends/family
label ending_aCI:
    "Ending aCI."
    return

#5 Aci - stays on your farm helping you, though she doesn't work hard enough to be of much help.
label ending_Aci:
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
    return
