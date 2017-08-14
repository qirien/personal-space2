## Family Events
# 
# Each family event has several parenting choices.  The decisions for the month
# will affect how much the child's stats increase that month.
#
# "demanding" and "responsive" are just for the current year and affect how much the child's stats increase that month.
# "authoritative", "authoritarian", "permissive", and "neglectful" are cumulative and affect the community's direction and have some correlation to "demanding" and "responsive".  Only increase one per month (?).
# TODO: The only way to get the "authoritative" option is usually to learn more about the situation by choosing "patient" options, such as "Listen", "Ask why", "Wait", "Think about it", etc.
# TODO: Use something that will randomize choice order after we've done a lot of testing

# Intro event
label family_intro:
    "Things used to be so simple. All you needed was a clean diaper, milk, and some love."
    "Now... I don't even know what you need from me."
    "It didn't always feel simple, though. Sometimes it was all I could do just to stay awake."

    #scene bedroom with fade         
    her "[his_name]."
    him "Mrmph?"
    her "[kid_name]'s crying."
    "Sometimes I still had to remind myself that we had a baby, even though it had been several weeks."
    "It was my turn to help her at night."
    him "Okay..."
    "I changed her diaper as quietly as I could. I tried not to disturb [her_name], but I could tell she was still awake." 
    "I got out the bottle to feed [kid_name]. I was so tired, but I laid her down next to me and watched her in the shadowy moonlight, her tiny cheeks working to eat."
    "She was too little to hold the bottle herself, but she lifted her hands in jerky movements that brushed against me."
    "I dozed off and dropped the bottle."
    "Maybe I could prop it up somehow and sleep while she ate? I had a vague feeling that might not be a good idea."
    "I tried to see it as a special time to snuggle, but my brain kept yelling at me to go back to sleep."
    "She finally finished the bottle, dozing off right away for once."
    "[her_name] reached across the baby and squeezed my hand before we both fell back asleep."
    "I guess it felt a little bit pointless to take care of [kid_name] in the middle of the night if [her_name] couldn't sleep through it, but she seemed to appreciate it."
    "And it did make me feel like more of a \"dad\", instead of just \"the husband of a mother\", if that makes any sense." 
    return

# 3 Earth mos. old
# CAN'T STOP CRYING!!
label family1:
    # TODO: check expressions, positions
    scene farm_interior with fade
    show him concerned at midright
    show her concerned at midleft

    her "I just wish I knew why she was still crying! Even if I couldn't help her, at least I'd know I wasn't overlooking something."
    him sad "I know. It's been hours..."
    "I knew she was exhausted. She had been carrying [kid_name] around all day and feeding her every few hours."
    "I wanted to help, but I had spent the whole day cleaning out the barn and was spent.  All I could think about was sleeping."
    "Sleeping..."
    show black with dissolve
    hide black with dissolve
    "No, I couldn't sleep while they both needed me. But what should I do?"
    menu:
        "Take [kid_name] for a walk.":
            $ responsive += 1
            him concerned "Here, I'll take her for a walk. I know I could use some fresh air, and we've tried everything else."
            her concerned "It's not too cold out, is it?"
            him normal "She'll be fine wrapped up in her blanket. See if you can get some sleep."
            her sad "Are you sure? I know you're tired, too..."
            him happy "If she's still crying in a few hours, it'll be your turn."
            her happy "Okay, good idea."
            "I snuggled her into her baby carrier and closed the door behind me."
            # TODO night overlay
            scene farm_exterior with fade
            show him normal at center with dissolve
            him normal "There now, little [kid_name], how's that?"
            "..."
            "She's still crying. I better get further from the house so I don't keep up [her_name]."
            scene fields with fade
            "The winters on Talaam were mild, but it was cold enough that I snuggled [kid_name] close to my chest as I walked, feeling her tiny warmth through my jacket."
            "I reminded myself that she wouldn't cry forever, that this was just one night, even as I felt like sobbing alongside her with exhaustion."
            "I hated feeling so helpless."
            scene moon with fade
            "I wonder if [kid_name] felt the same way?"
            "I looked down at her tiny squalling face and stroked her cheek. She was so upset, and had no other way to tell us about it. She certainly couldn't do anything to help herself."
            "We walked the fields for at least an hour; maybe more."
            "I don't know if she wore herself out or started feeling better, but she finally stopped crying and fell asleep. I was too tired to even be happy about it."
            scene farm_interior with fade
            "I tiptoed back into the house and struggled to take her out of the carrier without waking her up."
            "Finally, she was sleeping in bed, and I fell into bed next to her and [her_name]."
            $ authoritative += 1
            $ permissive += 1
            
        "Ask someone else for help.":
            $ responsive += 1
            "I wish I could ask my parents, but they're light years away. I'm not sure who else we could ask, though."
            him concerned "Maybe we should ask someone else for help. Someone who knows more about babies."
            her annoyed "Who's going to know more about [kid_name] than us?!"
            him annoyed "Everyone! Anyone! All I know is animals; calves and colts don't cry like this!"
            her sad "I'm a doctor; I should be able to figure something out. But I can't even think when [kid_name]'s crying."
            him concerned "Here, I'll hold her, and you go do some research or ask around or whatever."
            "[her_name] went outside to do some reading while I held [kid_name]. I paced restlessly, holding the baby in different positions until [her_name] returned."
            "She had a big list of things to try, and we tried them all.  I don't know if the white noise and the bath worked, or if she finally just wore herself out, but eventually she stopped crying and fell asleep."
            $ authoritative += 1
            
        "Let [her_name] handle it.":
            $ responsive -= 1
            "[her_name] knows more about this kind of thing than I do. I pushed open the door of our tiny house."
            her annoyed "Where are you going?!"
            him annoyed "You figure it out. I'm going for a walk."
            "Or maybe I'd try to get some sleep in the barn."
            her angry "You can't just leave me here with a screaming baby!"
            "[kid_name] and [her_name] wailed in unison, and their tears wrenched at my heart, but I just couldn't take it anymore."
            scene farm_exterior with fade
            "I stepped out into the night, closing the door gently with what little control I had left. I started to run."
            scene fields with fade
            "The crying faded from my ears the further I got from the house, but I could still hear the cries echoing in my head. I ran faster."
            scene moon with fade
            "I reached the end of our fields, out of breath, legs and chest aching. The pain felt good; I deserved it."
            "Maybe I wasn't cut out to be a dad. What kind of dad leaves when there's trouble?"
            "But this was trouble I couldn't fix. What was the point in sticking around, when everything I did just seemed to make it worse?"
            "That's what I told myself, but I still felt like a traitor."
            "..."
            "I {b}was{/b} a traitor."
            menu:
                "Go back and apologize.":
                    $ responsive += 1
                    "I had to make things right."
                    "I ran back to the house. I could still hear [kid_name]'s crying even from outside."
                    scene bedroom with fade
                    "[her_name] was lying on the bed with her arm around [kid_name], her face streaked with red from crying."
                    "I was glad to see she'd stopped crying, but then she looked up at me with hollow eyes and a resigned expression."
                    "She didn't say anything, just lay her head back down and stared at [kid_name] blankly."
                    him sad "[her_name]... I'm sorry. I shouldn't have left. I'm here, now."
                    "She still didn't respond, even when I picked up squalling [kid_name] and bounced her gently, trying for the hundredth time to help her calm down."
                    "As I left the room, [her_name] said something I've never forgotten."
                    her annoyed "Don't ever leave us again."
                    $ neglectful += 1
                "Spend the night in the barn":
                    "I couldn't go back there. I was already frayed and broken and ready to snap. My brain felt like a sparking circuit, and I worried that if I stayed, I might hurt someone or make a big mistake."
                    scene barn with fade
                    "I lay down on the hay in the barn and closed my eyes. [kid_name]'s screams echoed in my head so loudly I sat up and looked around. But there was no one there."
                    "Sleep was a long time in coming."
                    $ neglectful += 1                    
            
        "Let [kid_name] cry.":
            $ demanding += 1
            him normal "Sometimes babies cry. Since nothing we're doing is helping, let's just set her down and take a break."
            her concerned "We can't take a break. We're her parents!"
            him annoyed "It won't kill her to not be held for ten minutes.  Come here, [her_nickname]."
            "We set [kid_name] down and I set a timer for ten minutes."
            "We listened to her scream while we did the dishes together silently."
            "[her_name] started crying, too."
            her sad "Why am I so bad at this?"
            him serious "You've been doing a perfect job all day! It's not your fault."
            her sad "Maybe if she had a different mom she wouldn't cry so much."
            him angry "No way!"
            him concerned "I've seen you with her; you give her everything she needs. You're patient, loving, and hard-working. She's our daughter, and we're the parents she needs!"
            him sad "We're the parents she's got, and we'll raise her, no matter what!"
            "I held [her_name] for a while and she seemed to calm down a little. When the timer went off, I dashed for the cradle before [her_name] could respond."
            him happy "Now I'm going to try to be as awesome a parent as you've been all day. You just get some sleep or read a book or whatever you want to do! I got this!"
            "I danced around the room with [kid_name], who seemed slightly calmed by the swaying motions, though she still fussed and squirmed."
            her normal "[his_name]... You don't have to try to impress me."
            him happy "What's that? [kid_name] and I can't hear you; we're having too much fun."
            "[her_name] laughed, just for a second, and it was the most beautiful sound I'd heard all day. She put on some music with a good beat, and then came over and joined our dancing."
            "[kid_name] didn't know what to make of it, but we certainly felt better after our crazy midnight dancing."
            "I don't know if it was the music or dancing or if she just tired herself out, but eventually [kid_name] fell asleep and we followed suit."
            $ authoritative += 1
            $ authoritarian += 1
    

    "The next day, [kid_name] woke up with gurgles and smiles, as if the nightmare of the night before had never happened."
    "That laughter stirred in me so many emotions -- a primal love at her helplessness, frustration at the irony of it all, shame at how selfish I had felt, and underlying everything, a deep exhaustion that magnified every emotion."
    him serious "She really needs us, doesn't she?"
    her sleeping "Zzzzzz..."
    
    return
    
# 10 Earth mos. old
label family2:
    "Terra is getting into everything and Kelly's got a surgery and Jack's in charge at home of ten month old Terra."
    menu:
        "Make a play pen for her":
            $ demanding += 1
            $ authoritarian += 1            
        "Strap her on and try to get some work done":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Just let her play. She probably won't die.":
            $ neglectful += 1
        "Play with her":
            $ responsive += 1
            $ permissive += 1
 
    # Sister Naomi volunteers to watch Terra at her house while Jack and 
    # Kelly have a date. After a quiet evening, they finally get around to
    # talking about childraising plans
    # TODO: Perhaps they join the daycare coop at the end of this scene?
    return

#####################################################
#
# TODDLER
#
#####################################################

# 18 Earth mos. old
label family3:
    "Terra keeps putting sticks and rocks in her mouth on a family camping trip!"
    menu:
        "Make her a chewing toy":
            $ responsive += 1
            $ permissive += 1            
        "Give her something she can chew on.": #like a woodenspoon
            $ responsive += 1
            $ demanding += 1
            $ authoritative += 1            
        "Slap her hand away every time she reaches for them.":
            $ demanding += 1
            $ authoritarian += 1
        "Let her mouth them. It's good for her immune system, right?":
            $ responsive += 1
            $ neglectful += 1
    return
    
    scene farm_interior with fade
    show him at midright
    show her at midleft
    show kid at center
    him concerned "Whew, I thought I'd never finish harvesting all those potatoes!" # TODO: Change to some crop he's actually growing this year.
    her surprised "You're all done?"
    kid "All done!"
    him happy "Yeah!"
    her happy "Good job! I'm glad they're doing so well."
    him normal "I think I'm going to take it easy for a few days..."
    her concerned "Yeah..."
    show her happy with dissolve
    exted " Hey, you know what we've never done?"
    him flirting "I can think of a lot of things."
    her annoyed "As a family?"
    him surprised "Oh. No, what?"
    her happy "Gone on vacation!"
    him annoyed "You went to the ocean that one time..."
    her annoyed "Like I said, as a family."
    him surprised "Where do you want to go? There's no hotels or anything..."
    her surprised "I thought maybe we could go camping?"
    him happy "That sounds great! I love camping!"
    "Our excitement was contagious. [kid_name] stood up and clapped her hands. I picked her up and tossed her up into the air, catching her into a big hug." # TODO: animate this?
    him "You want to go camping too, huh, [kid_name]? Sleep outside?"
    kid "Outside!"
    "She squirmed to get down, then toddled over the door and banged on it with her hands."
    her normal "We don't have to go far... just over the south ridge or something. Just take a break from everything for a few days."
    him normal "I know the perfect spot! Let's go tonight!"
    her flirting "I think we'll need a little time to get a few things together. How about tomorrow?"
    him happy "Okay, tomorrow! Right after you're done at the clinic!"
    him surprised "Oh...can you really leave? What if something happens while you're gone?"
    her determined "Everything will be fine. I'll take a radio so they can contact me if there's an emergency."
    
    scene path with fade
    "The next day, we packed up some food and makeshift bedrolls and some equipment for starting fires."
    "[her_name] and I took turns carrying the equipment and carrying [kid_name]. She liked to walk, but she walked so slowly because she wanted to stop and look at every rock, bug, and bush."
    
    scene sunset with fade
    "Finally, we arrived."
    him flirting "Remember this spot?"
    her flirting "It seems kind of familiar... though I mostly remember the food."
    him surprised "The food?"
    her happy "Yeah, you made such a delicious picnic dinner!"
    show her flirting with dissolve
    extend " And then we stayed out here all night long..."
    him happy "Oh, so you do remember!"
    her normal "Of course I do. It's a beautiful place."
    "I held [her_name] close for a minute, both of us savoring the memory."
    her surprised "Oh! Where's [kid_name]?!"
    "We had just set her down, and already she had wandered off. We both scanned the area. No point in worrying yet, right?"
    him normal "She's just behind that bush."
    "She was chewing on some of the leaves."
    her concerned "Oh no! Are these poisonous?! I can't remember..."
    "[her_name] got the leaves out of [kid_name]'s mouth. Hopefully she hadn't eaten too many..."
    
    # TODO: Finish this.
    
    menu:
        "Make her a chewing toy":
            $ responsive += 1
            $ permissive += 1            
        "Give her something she can chew on.": #like a woodenspoon
            $ responsive += 1
            $ demanding += 1
            $ authoritative += 1            
        "Slap her hand away every time she reaches for them.":
            $ demanding += 1
            $ authoritarian += 1
        "Let her mouth them. It's good for her immune system, right?":
            $ responsive += 1
            $ neglectful += 1

# 2 Earth years old
label family4:
    "Terra won't eat what you want her to eat. We're having jerky, rice, and potatoes for dinner, but all she wants to eat is something we don't have right now."
    menu:
        "Make her stay at the table until she eats everything on her plate.": 
            $ demanding += 1
            $ authoritarian += 1
        "Tell her we don't have that food right now and keep the food out longer.":
            $ demanding += 1
            $ authoritative += 1
        "Ask a neighbor for the food she wants.":
            $ responsive += 1
            $ permissive += 1
        "Let [her_name] deal with it.":
            $ neglectful += 1
                        
    return

# 2.7 Earth years old
label family5:
    "Toilet training! She's learning it, but she has an accident."
    menu:
        "Just clean it up. She'll learn eventually.":
            $ responsive += 1
            $ neglectful += 1
        "Have her help you clean it up, then reward her later for just trying to go to the bathroom.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Punish her every time she has an accident":
            $ demanding += 1
            $ authoritarian += 1
        "Promise her a big reward if she can stay dry all day":
            $ responsive += 1
            $ permissive += 1
            
            
        # perhaps also a discussion about is she too young, should they give up, everyone's tired of washing diapers.  Maybe she should just LIVE OUTSIDE?!
    return

# 3.5 Earth years old
label family6:
    "Terra wants your attention while you're trying to relax on a lazy Sunday afternoon"
    menu:
        "Play with her just enough for her to get less bored and play a little more on her own.":
            $ responsive += 1
            $ demanding += 1
            $ authoritative += 1
        "Give her your complete attention.":
            $ responsive += 1
            $ permissive += 1
        "Tell her to stop bothering you.":
            $ demanding += 1
            $ responsive -= 1
            $ authoritarian += 1
        "Go into your room and lock the door.":
            $ responsive -= 1
            $ neglectful += 1
            
    "Sometimes you despair of ever having a minute to yourself."
    # TODO: Discussion of whether or not to have another child, as they feel Terra would benefit from a playmate. Or maybe just more time with friends?
    her "Hey, want to have another kid?"
    menu:
        "What should I say?"
        "Are you kidding?!":
            him "No way!"
            $ year6_have_baby = False
        "It would be efficient":
            him "It's probably more efficient to have them closer together."
            $ year6_have_baby = True            
        "If you're ready.":
            him "We can if you want to -- you're the one that has to host them for nine months." 
            $ year6_have_baby = True
        "Sure! Anytime!":
            him "Yeah! I love kids!"
            $ year6_have_baby = True            
    return

#####################################################
#
# SMALL CHILD
#
#####################################################

# 4 Earth years old
# Back-Talking
label family7:
    "Terra gets a new toy: some blocks! But later she talks back when asked to pick up her toys, saying \"I hate you!\""
    menu:
        "What do you say?"
        "There's consequences for such disrespect!":
            $ demanding += 1
            $ authoritarian += 1
        "How can you say that after all I do for you?":
            $ responsive += 1
            $ permissive += 1
        "You don't really mean that!":
            $ responsive += 1
        "I can see you're upset. When you're ready to talk respectfully, we can try to solve the problem.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Just ignore her. Maybe next time you will not bother making her clean up her toys.":
            $ neglectful += 1
            
            # TODO: She continues to talk rudely, has to go to timeout, user has to be patient through a zillion menus until she finally calms down
    return

# 5 Earth years old
# First Day of School
label family8:
    "First day of school! She's a little nervous, but not screaming and crying."
    # TODO: how would the first day be different in a 1 room schoolhouse? Maybe she'll see a familiar face in a babysitter there?
    menu:
        "Leave when she's not looking.":
            $ neglectful += 1
        "Cheerfully give her a goodbye hug.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Admonish her to behave.":
            $ demanding += 1
            $ authoritarian += 1            
        "Talk about how nervous she is.":
            $ responsive += 1
            $ permissive += 1
            
    if (year6_have_baby):
        "[her_name]'s second pregnancy seemed to go by so much faster than the first one."
        "A few weeks after school started, [her_name] went into labor in the middle of the night."
        # TODO: Depending on faction, contact someone different to watch Terra?
        call baby_delivery
        
    else:
        $ year8_have_baby = True
        scene farm_interior with fade
        show her normal at midleft
        show him normal at midright
        with dissolve        
        her concerned "It's a good thing [kid_name]'s in school... since I think I'm pregnant."
        him surprised "What, really? I thought we decided to wait!"
        her annoyed "Well, sometimes these things happen anyway."
        him concerned "Are you sure?"
        her surprised "Yes, I ran the test myself."
        menu:
            "What should I say?"
            "How are we going to do this?":
                him annoyed "Well, this is just great."
                her annoyed "What do you care? It's not like you have to be pregnant for nine months!"
                him angry "We don't have enough food for another baby! Where will they sleep? We don't even know what we're doing with [kid_name]!"
                her sad "I know it's hard, but..."
                him concerned "I'm sorry. Hey. Don't cry."
                her angry "I'll cry if I want to! Especially if my husband is yelling at me!"
                him angry "Fine, I'm sorry! I just..."
                show him concerned with dissolve
                extend "It's a lot to take in."
                label pregnancy_alone:                
                    her concerned "I need us to be on the same side.  "
                    show her sad with dissolve
                    extend "I can't do this alone."
                    him determined "You're not alone. I'll always be on your side."
                    him happy "I'll be by your side, at your side, sideways, right-side-up and upside-down!"
                    her normal "Then I don't have anything to worry about."
                    him normal "Nope."
                    "I held her close, stroking her hair, and she embraced me with a need I hadn't felt from her in a long time."
                    "Not the hunger of desire, or companionship, but of needing someone to share her burdens."
                    "How long had she known and worried by herself?"
                    "But I still had a lot of questions. I relived those sleepless, stressful months of when [kid_name] was a baby and wondered how we could do that again."
                    her concerned "You're still worried."
                    him normal "So are you."
                    her serious "Yes. But not as much."
                    him serious "We'll figure it out."
            "We can do this!":
                him serious "This is...this is..."
                her surprised "What?"
                him happy "This is awesome!"
                her annoyed "I don't feel awesome, I'll tell you that much."
                him surprised "Hey, is that why you've been so tired lately?"
                her serious "Probably so."
                him normal "Any morning sickness? I haven't noticed you eating differently."
                her normal "Not yet. "
                show her concerned with dissolve
                extend "I can't believe we're doing this again..."
                him normal "We're pros, now! It'll be so much easier!"
                her annoyed "What part of this is easy?!"
                him flirt "Well, conceiving the baby was pretty easy..."
                her flirt "If it was as hard to conceive a baby as it is to give birth, there'd be a lot less people in the world."                
                him surprised "How would that even work? Like, the baby would start large and shrink as they got older?"
                her normal "Yeah, that doesn't make much sense, I guess."                
                him happy "I love you even when you don't make sense."
                her concerned "Oh, [his_name]. I love you too. I'm so glad you're with me."
                him concerned "Hey, are you crying?"
                her normal "Just a little. Stupid pregnancy hormones."
                him happy "Here, you can wipe your tears on my shirt."
                her flirt "Now that's true love."                
            "How do you feel about it?":
                him surprised "How do you feel about it?"
                her concerned "I don't know. Worried, I guess."
                him concerned "Yeah, how will this even work?"
                her sad "I don't know if I can do this..."
                him serious "Hey, don't cry, it'll be okay."
                jump pregnancy_alone   
  
    return

label baby_delivery:
    #scene clinic with fade
    her pregnant concerned "Oh no, I remember this part. This is awful!"
    him determined "You did it once, you can do it again! Just a little bit more and then you'll be done!"
    her pregnant angry "You say 'a little bit', but I know it's going to be a few hours!"
    him normal "What's a few hours in the grand scheme of things? Hang in there!"
    her pregnant annoyed "You're fired as my cheerleader."
    him happy "I'm fired? You're the one that's on fire! Look at you, awesome momma!"
    her pregnant angry "I am literally in as much pain as if I were on fire!"
    him concerned "I know; I'm just trying to help you stay positive."
    her pregnant annoyed "Just shut up and rub my back."
    him happy "OK! One back rub, coming right up!"
    her pregnant normal "You forgot the 'shut up' part."
    him normal "..."
    "Finally, the baby was born. A boy!"
    $ bro_birth_year = year
    #TODO: Finish delivery. Baby has some birth defect - cleft lip, club foot? Let the player choose bro_name    
    
    return
    
# 5.5 Earth years old
# Holiday Traditions (or maybe honesty?)
label family9:
    "It's some holiday that we can decide on later! Terra doesn't want to do some tradition."
    menu:
        "Traditions are pointless. Why celebrate at all?":
            $ neglectful += 1
        "Keep the tradition.":
            $ demanding += 1
            $ authoritarian += 1            
        "Make a new tradition":
            $ responsive += 1
            $ permissive += 1
        "Keep the tradition and make a new tradition":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1            
        
    return

# 6.2 Earth years old
# Damages Tablet
label family10:
    "Sometimes I had to make sure to stop and enjoy the good times. It always felt like such a relief when no one was crying or needed anything, but I didn't want to take such times for granted."
    "[kid_name] came home from school and I gave her a snack."
    if (year6_have_baby):
        "[bro_name] wanted a snack, too, so I sliced up some tomatoes." # TODO: or whatever crop we planted?
    menu:
        "What should I say?"
        "How was school today?":
            him "How was school today?"
            kid "Okay."
            him "..."
            kid "..."
            if (year6_have_baby):
                him "[bro_name] and I rode the tractor all over today plowing the fields and mixing in the compost."
            else:
                him "I plowed the fields today. Gotta mix in all that fertilzer."
            kid "Okay."
        "What was the funniest thing that happened today?":
            $ responsive += 1
            him "What was the funniest thing that happened today?"
            kid "The funniest?"
            him "Or just a funny thing. Maybe there were a lot."
            kid "Hmmm.... Well, we talked about what we wanted to be when we grew up."
            him "Oh yeah?"
            kid "The teacher asked #TODO:friend_name first, and she said she wanted to be a crabird."
            him "Ha ha, wow, that'd be weird."
            kid "Yeah! And then I thought, if I could be anything, I'd like to be a spaceship so I could take people anywhere they wanted to go."
            him "A spaceship, huh?"
            kid "Yeah, we could go to Earth whenever we wanted, and I could meet my grandparents, and get stuff people wanted."
            him "Who knows, maybe you'll be a pilot or something?"
            kid "Or I might invent teleporters."
            him "I would love that."            
        "What did you learn today?":
            $ demanding += 1
            him "So, what did you learn today?"
            kid "Nothing."
            him "Right, because you already know everything."
            kid "Yup."
            him "So what did you discuss today?"
            kid "Stuff."
            him "Such as?"
            kid "Dad, why does it take so long for ships to get here from Earth?"
            him "Oh, is that what you talked about at school?"
            kid "No, I just want to know."
            him "Well, I guess it's hard to make something go that fast. And it's really far."
            kid "Sometimes I wonder if Earth really exists."
            him "It definitely does. I was born there."
            kid "It's just so hard to imagine."
            him "Yeah, I bet it seems so foreign..."
            kid "It is. All those cities, so many people... it's just weird."
        "(Don't say anything)":
            him "..."
            kid "..."
            "She ate her snack in silence."
        
    if (year6_have_baby):
        "She finished her snack and got out the blocks. I cleaned up the kitchen a bit and [bro_name] wandered over to play with her."
        "It still amazed me to see the two of them playing together. Two tiny people, that hadn't even existed several years ago..."
        "They were quite different, though. When [kid_name] was his age, she was climbing on everything and pulling down everything she could reach."
        "[bro_name] was a more easygoing kid."
        "I love [kid_name], but it would've been a challenge to have two kids like that..."
        "He was finally getting old enough to play with [kid_name], though he was still learning how."
        "She had stacked up the blocks into a mountain, and had setup some little figurines at the base."
        menu:
            "What should I say?"
            "Compliment them on playing well.":
                $ demanding += 1
                $ responsive += 1
                him "I'm glad to see you playing happily together."
                "I tousled their hair. I know I'm probably biased, but they seemed like the cutest kids in the universe to me."
                "They didn't seem to even notice I was there, and just kept playing."
            "Just keep watching.":
                "I didn't want to ruin the moment, so I just watched them."
        kid "[bro_name]! Look what I built! Here's the volcano. And here's us."
        "She walked the figurines up the mountain until they reached the top. [bro_name] made to touch the blocks, but she stopped him."
        kid "No no, it's hot."
        bro "Hot?"
        "She had the parent figurines give warnings."
        kid "\"It's so hot!\" \"Don't fall in!\""
        kid "Here's [bro_name]. Uh-oh, he's getting close to the edge!"        
        "She dropped one of the figurines into the \"volcano\" while making a disturbingly accurate crying sound. [bro_name] just watched. He was probably happy to get any attention from her at all, but..."
        menu:
            "Should I say something?"
            "Wait and see.":
                "I waited to see what [kid_name] would do."
                kid "\"I'll save you!\""
                "She had the family hold hands and lower her figurine into the volcano, and she fished her brother out."
                kid "Gotcha! Whew, that was close!"
                bro "I in there?"
                kid "Yeah, you were in the lava! But we got you out."
                bro "Hot?"
                kid "No, it's not hot anymore."
                "He pushed the side of the volcano, and the blocks tumbled down."
                "She looked furious."
                kid "[bro_name]! No, no, NO!!!"
                menu:
                    "What should I say?"
                    "Stop yelling at him!":
                        $ demanding += 1
                        him "Stop yelling at your brother!"
                        kid "He wrecked my volcano!"
                        him "They're his blocks, too. You need to share!"
                        kid "I was sharing!"
                        him "Well, it's his turn, now!"
                        kid "No! I'm in the middle of a game!"
                        him "Go to your room!"
                        kid "You ruined everything!"
                        "She stomped off, and [bro_name] started crying. I tried to comfort him, but it was difficult when I was so angry."
                        him "(How does a little six-year-old know how to make me so mad?!)"
                        $ authoritarian += 1
                    "Hey, it's an earthquake!":
                        $ responsive += 1
                        him "Ahhh, earthquake! Can the family survive?"
                        "I pulled my figurine out of the pile of blocks."
                        him "\"Don't worry, I'll save you!\""
                        "I dug around, trying to get the other figurines out. I got [kid_name]'s and handed it to her."
                        him "Quick, we've got to get [bro_name] and mom!"
                        "We rummaged through the blocks until we pulled out their two figurines. I handed [bro_name] his."
                        kid "Now run away from the lava!"
                        him "Ahhhh, lava!"
                        "We made our guys run down the pile of blocks."
                        menu:
                            "Keep playing with them.":
                                "The three of us played natural disaster-escaping family until dinner time."
                                # TODO: have some farming consequences?
                                $ permissive += 1
                            "Compliment them on getting along.":
                                $ demanding += 1
                                him "Good job getting along."
                                "I'm pretty sure [kid_name] heard me, but she was already on to the next thing and didn't respond."
                                "I left them to it while I went to change the oil in my tractor. Hopefully they'd get along for awhile."
                                $ authoritative += 1
            "Leave them alone.":
                "Nobody was sad; they didn't need me to interfere."
                "Besides, the tractor needed an oil change."
                $ neglectful += 1
            "Scold [kid_name].":
                $ demanding += 1
                him "[kid_name]! Don't drop your brother in the volcano!"
                "She looked at me defiantly, then shoved the blocks, burying all the figurines. One tipped and fell on [bro_name], who started crying."
                kid "Earthquake! The volcano's erupting! There's lava everywhere! Ahhhhhh!"
                bro "Wahhhhh!"
                kid "We all died."
                bro "All died."
                kid "Except me. I ran away."
                him "Terra..."
                kid "And now I live by myself in the jungle."
                "[bro_name] reached for his figurine, but she pulled it out first and put it up high where he couldn't reach."
                kid "You can't play with him. He's dead."
                bro "I want it!"
                kid "Nope. Dead means dead forever. All gone."
                bro "Not all gone!"
                him "[kid_name], that's enough. If you can't get along with [bro_name], then you'll need to go to your room."
                "I gave [bro_name] his figure. He looked at it suspiciously, as if trying to tell from its appearance whether it was still okay to play with after being \"dead\"."
                kid "Dad, you're ruining the game!"
                menu:
                    "Scold her some more.":
                        him "No, {b}you{/b} are ruining the game! How does it make [bro_name] feel to have you killing off his guy?"
                        kid "It's just a game!"
                        him "Even in a game you can't be a jerk to everyone!"
                        kid "You're a jerk!"
                        him "That's enough! Go to your room!"
                        kid "You go to your room!"
                        "I picked her up. She'd gotten heavier, but my adrenaline was up now and I lifted her easily and dropped her into her room."
                        "I meant to set her down, but she struggled right as we reached the doorway and she kicked my wrist."
                        "She dropped to the floor and her head hit her bed post."
                        kid "Wahhhhhhhhh!"
                        menu:
                            "What should I say?"
                            "That's what you get for disobeying.":
                                him "That's what you get for disobeying your father!"
                                kid "You hurt me!"
                                him "..."
                                kid "You're so mean..."
                                "I turned away. She was trying to make me feel guilty, but none of this would have happened if she had just done what I asked!"
                                $ responsive -= 1
                                $ authoritarian += 1
                            "I'm sorry.":
                                him "I'm sorry, [kid_name]. I didn't mean for you to hit your head."
                                kid "Yes, you did. You're always mean to me."
                                "I turned away. I couldn't make her accept my apology. But hopefully she'd remember what I'd said."
                                $ authoritarian += 1

                    "Suggest they play something else.":
                        him "Why don't we make a road for the guys instead?"
                        "I started laying out some blocks in a path. [kid_name] just watched me for a minute, but [bro_name] brought his figure over and banged it on the block path happily."
                        "I made a building out of blocks."
                        him "Here's the school."
                        "[kid_name] made a path going off a different way."
                        kid "And here's the storehouse. I'm going to get all the chocolate."
                        him "Here, [bro_name], why don't you use these blocks here?"
                        "I cleared out a little space for him and stacked some blocks up in a way that would be hard to knock down."
                        "He knocked it down anyway, banging his figurine on the blocks as if it was jumping."
                        him "Ha ha, maybe that's the junk pile."
                        "They played together for a while and I snuck off. Hopefully I still had time to change the oil in the tractor."
                        $ responsive += 1
                        $ authoritative += 1                

    # She doesn't have a little brother, so instead she's playing on the tablet              
    else:
        kid "Can I use the computer pad?"
        him "Sure, here you go. Be careful, okay?"
        kid "I will."
        "She loaded up the kid's science app that she liked, and I went to go change the oil in the tractor."
        "It was probably an hour or so later that I went back in to check on her."
        # TODO: Finish this
            
        "Terra drops the family tablet and a crack forms.  It's still usable, but annoying"
        menu:
            "Do nothing. She'll learn eventually on her own.":
                $ neglectful += 1
            "Yell at her to be more careful":
                $ demanding +=1 
                $ authoritarian += 1
            "Ask how it happened and require her to do extra chores to make up for it.":
                $ demanding += 1
                $ responsive += 1          
                $ authoritative += 1
            "Tell her it's all right, she can't be expected to take care of things at her age.":
                $ responsive += 1
                $ permissive += 1
                
    if (year8_have_baby):
        "[her_name]'s second pregnancy seemed to go by so much faster than the first one."
        "[kid_name] was really looking forward to having a little brother or sister; she was all excited to help with everything."
        "A few weeks after school started, [her_name] went into labor in the middle of the night."
        # TODO: Depending on faction, contact someone different to watch Terra?
        call baby_delivery            
    return

# 6.8 Earth years old
# Dinner Table Manners
label family11:
    "Manners at the dinner table!  Terra used to know how to say Please and Thank You, but lately she's forgotten or is testing the limits."
    menu:
        "I raised you to talk better than that!":
            $ demanding += 1
            $ authoritarian += 1
        "I expect you to say 'please' when you ask for something, and 'thank you' when someone helps you. Try again.":
            # she keeps asking rudely a billion times, do you give up and give her what she wants, get mad, set a consequence, or simply ignore her until she talks politely?
            $ demanding += 1
            $ responsive += 1            
            $ authoritative += 1
        "Give her what she wants.":
            $ responsive += 1
            $ permissive += 1
        "Maybe next time you'll eat by yourself.":
            $ neglectful += 1
            
    return
    
    "Meal times at our house were never boring. [kid_name] would tell us about what happened at school, [her_name] would talk about the patients she saw, and I would update everyone on how the crops were doing."
    "Even [bro_name] usually had something to say."
    "They weren't always peaceful, though..."
    kid "Beans again? Ugh."
    him "You can put Special Sauce on them if you want."
    "We called it \"Special Sauce\", but it was really just homemade ketchup. With a few other secret ingredients to make it healthier."
    kid "Yeah, gimme the sauce."
    if (year6_have_baby):
        bro "Gimme sauce!"
    else:
        bro "Ya ya ya ya."
    her "Say \"please\" when you ask for something."
    "[kid_name] knew this; she used to say \"please\" and \"thank you\" all the time. But not today."
    menu:
        "What should I say?"
        "Here you go.":
            $ responsive += 1
            him serious "Here you go."
            "It wasn't worth making a big deal over."
            "Maybe it was just a one-time thing."
            kid "Gimme the potatoes."
            "Or maybe not."
            menu:
                "What should I do?"
                "Just pass her the potatoes.":
                    "I just passed them to her. I mean, they were just words, right? She'd learn eventually..."
                    $ permissive += 1
                    return                                                            
                "Say something about it.":
                    "[her_name] was about to pass the potatoes, but I stopped her. I took the sauce back."
            
        "Say \"please\"":
            $ demanding += 1
            $ responsive += 1
            him "We say \"please\" when we ask for something, and \"thank you\" when someone does something for us."
            kid "C'mon, pass me the sauce!"
        "Where are your manners?!":
            him "Where are your manners? I raised you to speak better than that!"
            kid "C'mon, pass me the sauce!"
        "I'm eating outside.":
            him "I'm eating outside."
            "Maybe that would get the message across. I just couldn't deal with that kind of garbage right now."
            "I took the special sauce with me."
            $ neglectful += 1
            return
            
    "She was not going to talk to me like that!"
    $ manners_grounded_days = 0
    $ manners_patience_count = 0
    menu manners_patience:
        "What should I say?"
        "(Send her to her room with no dinner)" if (manners_grounded_days >= 2):
            him angry "Go to your room!"
            her surprised "[his_name], calm down. It's not that big of a deal."
            him annoyed "It is a big deal! I will not have a rude daughter like that in our house!"
            her annoyed "Well we sure aren't kicking her out just because she didn't say \"please\"!"
            him determined "She can come out whenever she's ready to say \"please\"."
            kid "That'll be NEVER!"
            her angry "Oh, sure, we'll just starve our kids until they do what we want! Is your ego that important to you!?"
            him angry "It's not my ego! It's basic human decency!"
            her annoyed "Sure, you just keep telling yourself that."
            "[kid_name] didn't come out of her room at all that evening. What a stubborn kid..."
            "Hopefully she learned her lesson."
            $ authoritarian += 1
            
        "(Ignore her until she asks politely)" if (manners_patience_count >= 4):
            him happy "So, [her_name], what did you work on today?"
            her concerned "I've been researching--" 
            kid "Pass the sauce!"
            him normal "Go on."
            her concerned "I've been researching the nutritional properties of crabird eggs."
            him surprised "I didn't know you could eat the eggs!"
            kid "I JUST WANT SOME FOOD!"
            if (year6_have_baby):
                bro "Me, me me!"
            else:
                bro "Wahhhhh!"
            her normal "They're hard to find, as crabirds tend to bury them in the mud near a stream, but they have high levels of-"
            kid "You guys are so mean! I just want some food!"
            her concerned "-high levels of certain amino acids."
            kid "Ugh! Fine! PLEASE pass the sauce!"
            if (year6_have_baby):
                bro "Peas!"
            else:
                bro "Wahhhhh!"
        
            him happy "Here you go, [kid_name]. Thanks for asking politely."
            kid "You're mean."
            her "I think the word you're looking for is \"thank you\"."
            "She just glared at us and then dug in to her beans and sauce."
            "I decided to save that one for another time."
            if (manners_grounded_days >= 1):
                "She was already grounded."
            $ authoritative += 1
            return
        "I will wait as long as I need to." if (manners_patience_count >= 2):
            him determined "I will wait as long as I need to."
            kid "Can I have the sauce?"
            him "I expect you to use the word \"please\"."
            $ manners_patience_count += 1
            jump manners_patience 
            
        "If you keep talking rudely, you'll be grounded!":
            $ demanding += 1
            kid "Gimme the sauce!"
            him angry "Okay, you're grounded for another day."
            $ manners_grounded_days += 1
            if (manners_grounded_days > 1):
                him "That makes [grounded_days] days, now. Is this really worth it?"
            jump manners_patience
            
        "As soon as you ask politely, I will pass them to you.":
            $ demanding += 1
            $ responsive += 1
            kid "What? I just want some sauce and beans!"
            him annoyed "Then ask politely."
            kid "Gimme the sauce!"
            $ manners_patience_count += 1            
            jump manners_patience
            
        "(Just pass them to her)" if ((manners_patience_count + manners_grounded_days) >= 1):
            $ responsive += 1
            "I gave up. I didn't have the time or patience to wait for her to decide to use a stupid word like \"please\"."
            if (manners_grounded_days > 0):
                "And now she was grounded as well."
            else:
                "What a pointless battle."
            $ permissive += 1
            return
    

# 7.4 Earth years old
# Growing Independence
label family12:
    "[kid_name] wants to walk to a friends' house after school and walk home. It's pretty far, but she's been there before."
    "Still, you can't help but think of Josefina, the Peron's daughter that accidentally got run over by Pete's tractor when she was about this age."
    menu:
        "No way. You'll go with her.":
            $ demanding += 1
            $ authoritarian += 1
        "Talk to the friends' parents.":
            # It turns out an older sibling will accompany them.
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Sure, she's a big girl now.":
            $ responsive += 1
            $ permissive += 1
        "Sounds like a pain. Just say she can't go.":
            $ neglectful += 1
            
    return
    
#####################################################
#
# BIG KID
#
#####################################################    

# 8 Earth years old
# Sex Education
label family13:
    "Terra wonders where babies come from."
    menu:
        "She's not ready.":
            $ demanding += 1
            $ authoritarian += 1
        "Give a vague metaphor.":
            $ responsive += 1
            $ neglectful += 1
        "Keep it simple":
            $ responsive += 1
            $ demanding += 1          
            $ authoritative += 1
        "Give a detailed explanation.":
            $ responsive += 1
            $ permissive += 1
        
    return
    
    # TODO: uncomment above when ready for prose, and make sure variables are changing properly
    # TODO: Is this because Mom is pregnant again?  Miscarriage -> hysterectomy?
    scene fields with fade
    show him at midright
    show kid at midleft
    with dissolve
    kid "Dad, I have a question."
    him "What is it?"
    
    # TODO: Is this different based on earlier decisions?
    kid "So, you need a man and a woman to make a baby, right?"
    him "Right..."
    kid "Well, how, exactly, does that work? I mean, I know they come together, but . . . how?"
    him "Let me think about the best way to explain that to you..."
    menu:
        "She's not ready for this":
            $ demanding += 1
            him "Maybe when you're older. That's not something you need to worry about right now."
            kid "But I am worried about it right now!"
            him "Ask your mom, then."
            kid "Why can't you just tell me?"
            him "I just... I just can't! So quit asking!"
            "I felt a little bad, but really, she's asking the wrong person!  That's [her_name]'s job!"
            $ authoritarian += 1
        "Give a vague metaphor":
            him "Well, you know, it's like, uh, like bees carry pollen?  And they fertilize the flowers so fruits can grow? It's . . . kind of like that."
            kid "I know that! But how does it work? Where's the pollen, and what's the flower?"
            him "Well, males and females have different parts, so the male part is like the pollen, and the female part is like the flower."
            kid "I don't get it."
            him "Ah, yeah, well . . . hey, look, that crabird landed on top of one of the goats!"
            kid "What does that have to do with it?"
            him "Nothing. Time to collect fertilizer! Here's your shovel."
            "Whew, that was a close one!  I'd better figure out what to say next time. Or maybe [her_name] could talk to her about it."
            $ neglectful += 1
        "Keep it simple":
            $ responsive += 1            
            him "The man has sperm and when one of them comes together with the woman's egg, it can make a baby."
            kid "Where does he get the sperm?"
            him "His body can make them."
            kid "Okay, but the egg is inside the woman, right? So how does the sperm get there?"
            him "That happens during sex."
            kid "But... what is sex, exactly?"
            "She's not giving up, is she?! I don't want her to imagine something wrong."
            $ sex_ed_counter = 0
            label sex_ed:
                if (sex_ed_counter >= 3): #short attention span!
                        kid "I like playing with babies. But I don't want to have to take care of one all the time."
                        him "Not now. Maybe someday. Then I can be a grandpa."
                        kid "Ha ha, then I'll call you Grandpa Dad."
                        him "I wish you could meet your real grandparents."
                        kid "Your parents? What would we do?"
                        him "Maybe you'd ride horses together, or bake cookies, or play with the dogs."
                        kid "Grandma Grayson said that if we get some more sugar on the next shuttle we can make cookies." # TODO: Make sure she's not dead
                        him "You'll let me have one, right?"
                        kid "Sure, dad."
                        $ authoritative += 1                                                                                
                        return #done with event
            menu:
                "What should I tell her about sex?"
                "Tell her the biology facts." if not sex_ed_biology:
                    him "A man's penis can go inside the woman's vagina and put the sperm there when they have sex."
                    kid "Oh."
                    "She thought about it for a minute."
                    kid "And that's how you and Mom made me?"
                    him "That's how."
                    "She looked away for a minute, and I could almost see her processing this new information."
                    kid "Huh. Are you sure?"
                    him "Sure as you're sitting here asking me if I'm sure."
                    $ sex_ed_biology = True
                    $ sex_ed_counter += 1
                    jump sex_ed
                "Emphasize committment and marriage." if not sex_ed_commitment:
                    $ demanding += 1
                    him "Sex is an important part of marriage. It makes you feel closer together, and you show your love for your spouse in a special way."
                    if (not sex_ed_biology):
                        kid "Okay, but what is it?!"
                    else:
                       kid "So you have to be married to have sex?"
                       him "Well, it's special enough you don't do it with just anyone. You want to be sure they're someone you want to give your whole heart to, someone you can really trust in the long run."                    
                    $ sex_ed_commitment = True
                    $ sex_ed_counter += 1
                    jump sex_ed
                "Tell her the baby-creation part." if not sex_ed_babycreation:
                    him "Sex is how babies are made, so it's kind of a big deal. You  need a mom and a dad who are going to stay together and be good parents for the baby."
                    if (not sex_ed_biology):
                        kid "Okay, but what is it?!"
                    else:
                        kid "So it always makes a baby?"
                        him "No, not always. But that's how babies start. Not just humans, but animals, too."
                        kid "Like our baby goat? His parents had sex?"
                        him "Well, with animals we usually call it 'mating', but, yeah."
                    $ sex_ed_babycreation = True
                    $ sex_ed_counter += 1
                    jump sex_ed
                "Explain how good it feels." if not sex_ed_goodfeeling:                    
                    him "It feels really good to have sex together."
                    if (not sex_ed_biology):
                        kid "Okay, but what is it?!"
                    else:
                        kid "Okay, can I try it?"
                        him "No! I mean, not yet. Someday. When you're much older."
                        kid "Why not?"
                    $ sex_ed_counter += 1                        
                    $ sex_ed_goodfeeling
                    jump sex_ed                    
                "Talk about birth control." if not sex_ed_birthcontrol:
                    him "If the man and woman aren't ready for a baby, there's ways to have sex without making a baby."
                    if (not sex_ed_biology):
                        kid "Okay, but what is sex?!"
                    else:
                        kid "Oh. How do you know if you're ready for a baby?"
                        him "Well, both people need to be ready to take care of it, and to know that they're going to stay together and give the baby good parents."
                        kid "Are you going to have another baby?"
                        # TODO: change this based on number of kids, etc?
                        him "Maybe. That's up to me and your mom."
                    $ sex_ed_counter += 1
                    $ sex_ed_birthcontrol
                    jump sex_ed
                "That's enough details for now.":
                    him "Anyway, that's all you need to know for now."
                    $ sex_ed_counter = 3 # this will cut out to baby discussion
                    jump sex_ed                   
            
        "Tell her all the details":
            $ responsive += 1
            "I told her everything I knew about sex - biology, emotional effects, irresponsible sex, birth control, hormones..."
            kid "Ha ha, look, there's a crabird sitting on that goat's head."
            him ". . . have you been listening at all?"
            kid "Not really. It was kind of boring."
            him "Huh. Sorry."
            kid "I'm going to go chase it off. Ooh, or maybe we should shoot it and eat it for dinner."
            him "No way, you might shoot the goat!"
            kid "Will you take me hunting sometime soon? I looooove crabird meat. It's so good. I could eat every day."
            # TODO: Make this a choice or dependent on choices?
            him "Yeah, let's go tomorrow morning before school. We'll get up early and catch them before they get warmed up."
            $ permissive += 1
    return

# 8.7 Earth years old
# Teacher Troubles
label family14:
    "Terra is having problems at school and taking it out on her little sibling."
    menu:
        "Demand that her teacher fix the problem":
            $ responsive += 1
            $ permissive += 1            
        "Brainstorm ways Terra could work it out":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Terra should quit asking you and stop bothering her brother.":
            $ demanding += 1
            $ authoritarian += 1
        
    return
     
    scene farm_interior with fade
    #show kid at midleft
    #show brother crying at quarterleft with dissolve
    show him at midright with moveinright
    
    him surprised "Whoa, what's going on?"
    kid "He's annoying me!"
    bro "She hit me!"
    kid "You wouldn't shut up! I asked you to quit humming but you're doing it just to annoy me!"
    him "Hey, hey, both of you go sit on your beds and cool off."
    her "They've been like that ever since I got home. Something's bothering [kid_name], but she won't tell me what it is."
    him "I'll talk to her."
    her "Good, I'll talk to [bro_name]."
    
    menu:
        "What should I say?"
        "You know better than to hit your brother!":
            $ demanding += 1
            him angry "You know better than to hit your brother! That violence is unacceptable!"
            kid "Oh, of course you take his side!"
            him annoyed "Well, yeah, you were the one hitting."
            kid "He was trying to get me in trouble! I'm always in trouble."                     
        "You seem really upset.":
            $ responsive += 1
            him concerned "You seem really upset. What's going on?"
            kid "Of course I'm upset! [bro_name]'s always getting me in trouble!"
        "I'm disappointed you and your brother weren't getting along.":
            $ demanding += 1            
            him concerned "I'm disappointed you and your brother weren't getting along."
            kid "Do you know how hard it is to be nice when someone is humming the same annoying song in your ear over and over?!"
        "(Say nothing)":
            $ responsive += 1
            him serious "..."
            "I sat down next to her, ready to listen."            
            kid "..."
            him concerned "..."
            "It took a few moments, but she finally said,"
            kid "He's always trying to get me in trouble!"            
    
    him sad "That sounds tough. But it seems like there's something else bothering you."
    kid "Not really."
    him concerned "Maybe something at school?"
    kid "..."
    menu:
        "What should I say?"
        "How's your teacher?":
            him surprised "Everything okay with your teacher?"
            kid "She's so mean! She's always telling me what to do!"
        "How are your friends?":
            him surprised "Everything okay with your friends?"
            kid "Yeah, they're okay. We're all mad about our teacher, though. She's always telling us what to do!"            
        "How are you feeling?":
            him surprised "Are you feeling okay?"
            kid "I'm not sick or anything. Just tired of everyone telling me what to do!"
        "(Say nothing)":            
            him serious "..."
            "I put my arm around her, trying to show her that I was there for her. Words just weren't good enough."
            "She didn't lean into me, but she didn't push me away, either."
            kid "I just wish everyone would stop telling me what to do!"
            
    him surprised "Isn't that your teacher's job?"
    kid "No! She's supposed to be teaching me useful things like math and reading, not making me do busy work all day!"
    menu:
        "What should I say?"
        "You need to listen to your teacher.":
            $ demanding += 1
            him serious "She's your teacher. She knows what she's doing, and you need to respect her and obey her."
            kid "Even if she's wrong?"
            him angry "Yes! You're the kid; your job is to obey! She's the adult; her job is to teach."
            kid "Why am I even talking to you about this?!"
            him annoyed "I'm trying to help you."
            kid "No, you just want to make me do what you want!"
            him angry "The only things I want you to do are things that are good for you!"
            kid "It feels like everyone's just being mean."
            "I could feel I was getting angry. She wasn't listening at all!"
            menu:
                "(Leave the room)":
                    him annoyed "We'll talk more about it later."
                    "I couldn't think straight when I was so angry. I didn't want to end up saying or doing something I'd regret."
                    "But I couldn't just let her get away with hitting her brother, either."
                    "In the end, we took away her computer pad time for a week. I don't know if it helped; we had to do that several times. She didn't use the computer pad for several months because she kept hitting her brother."
                    "Was this normal? I don't think my brother and sister and I fought like that."
                    "Or maybe we did, but we outgrew it? Was this just a phase?"
                    "I felt like I was trying to harvest tomatoes in the dark."
                    $ authoritarian += 1
                    return
                "(Make her understand)":
                    $ responsive -= 5
                    "I got right up in her face and gripped her arms, tighter than I meant to."
                    him angry "We are not being mean! We are trying to teach you how to be a decent human being! But it's really hard when you keep hitting people and disobeying us!"
                    kid "Ow, dad, that hurts!"
                    him angry "Did you hear what I said?!"
                    kid "Yeah, just let go! Let go!"
                    her concerned "Why don't you let me talk to her for awhile, [his_name]?"
                    him annoyed "Go for it. Not that it'll do any good."
                    her angry "[his_name]!"
                    him angry "She's so selfish! She never listens! She just thinks everything is about her all the time!"
                    her angry "I wonder where she could have learned that?!"
                    him annoyed "Oh, so it's my fault [kid_name]'s a selfish brat? You had nothing to do with it?"
                    her annoyed "Where is she going to learn how to be calm when she's angry if we don't show her how?"
                    him angry "!"
                    her concerned "..."
                    him sad "..."
                    kid "..."
                    "I left. Maybe I shouldn't have said all those things. But [kid_name]'s rebellious attitude got to me every time."
                    "She made me so mad..."
                    "I guess, in that way, I understood a little bit of how [bro_name] made her mad."
                    "What a hypocrite... I expected her to be a paragon of calmness when someone was annoying her, but when she annoyed me, I flipped out just like she did."
                    "I almost... I could have hit her."
                    "Half of me wondered if it would have helped, while the other half was horrified I'd even considered it."
                    "What kind of father am I?"
                    $ authoritarian += 1                    
                    return
                
        "Tell me about it.":
            $ responsive += 1
            him serious "Tell me about it."
            kid "We have to write our spelling words ten times each! Ten times! And I don't need to study them at all because I already know them!"
            him concerned "That does sound frustrating."
            kid "Yeah, and when I asked her if I could do something else, she didn't even listen; she just said no!"
            menu:
                "What should I say?"
                "That was really mean!":
                    $ responsive += 1
                    him surprised "That was really mean!"
                    kid "Yeah! School is so boring!"
                    him concerned "Yeah, you shouldn't have to do boring work! I'll go talk to your teacher."
                    kid "Yeah. She shouldn't make us do stuff like that."
                    "I talked to the teacher and managed to cajole her into letting [kid_name] write her words only five times each."
                    "[kid_name] seemed pretty happy about it, so I guess I did the right thing?"
                    $ permissive += 1
                    return 
                "You need to listen to your teacher.":
                    $ demanding += 1
                    him serious "You need to listen to your teacher."
                    kid "But she's wrong!"
                    him concerned "Maybe so, but she deserves a certain amount of respect."
                    him serious "And so does your brother."
                    kid "And so do I!"
                    him annoyed "You'll need to apologize to your teacher and your brother, and you won't be able to use the computer pad for games or play with friends this week." 
                    $ authoritarian += 1
                    "She didn't like it, but she did what her teacher asked. She still had problems with hitting her brother, so she wasn't able to play with friends or use the computer pad for a long time."
                    "How long would it take for her to get the message?!"
                    return
                "What did you want to do instead?":
                    him surprised "What did you want to do instead?"
                    kid "Read my book."
                    him serious "Well, spelling is still something you should study. Does this happen all the time?"
                    kid "Yes."
                    him concerned "Maybe we could ask if you could do a higher level of spelling words?"
                    kid "Ugh, that'd be even more work!"
                    him normal "It'd be less boring."
                    kid "I guess. I still don't want to write them ten times. My hand gets sore. And what's the point of writing by hand, anyway? You and mom never write by hand. It's a waste of paper."
                    him happy "One problem at a time, [kid_name]. Let's send your teacher a note. Do you want to type it, or write it."
                    kid "Type it!"
                    "We wrote to her teacher, and Terra asked if she could have harder spelling words and type them instead of handwrite them."
                    "I wasn't sure what her teacher would say, but at least I helped Terra with her problem at school."
                    him serious "Now, there's one more thing."
                    kid "What's that?"
                    him annoyed "You hit your brother. How can you make it up to him?"
                    kid "How is he going to make it up to ME for annoying me?!"
                    him concerned "Don't worry about what he will do; you just decide what you will do."
                    kid "I don't know. Not him anymore, I guess."
                    him annoyed "I expect you to apologize to him and do something kind for him."
                    kid "I can't do that!"
                    him normal "I'll ask you later tonight and you can tell me what you chose."
                    kid "Ugh. Fine. But you should also ask {b}him{/b} to stop annoying {b}me{/b}!"
                    "That's what she said, but at dinner she set the table for [bro_name], and I heard her mutter 'sorry' to him, too."
                    "It's not shiny happy ending I wanted, but maybe she learned something?"
                    "At least we worked things out with her teacher."
                    $ authoritative += 1
                    return
        "You're just whining.":
            him "Quit whining and don't hit your brother."
            kid "But...!"
            "I left before she could complain more. What more needed to be said?"
            $ neglectful += 1
            return    
    
    return

# 9.4 Earth years old
# Allowance?
label family15:
    "Terra wants some money. She read about something called 'an allowance' in a book and wants to buy foods/clothes/toys? that she wants!"
    menu:
        "No.":
            $ neglectful += 1
        "Start an allowance based on completing chores and being good.":
            $ demanding += 1
            $ authoritarian += 1
        "Require her to write up her projected expenses to help determine the amount of the allowance.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        # Also probably something about she is now responsible for certain expenditures
        "Sure, here you go.":
            $ responsive += 1
            $ permissive += 1
            
    return

    # TODO: Modify allowance_amount based on this event and do something with it.
    kid "Dad, I need some money. Can I have an allowance?"
    him "[kid_name], I have no problem with ants. I already allow ants."
    kid "Ha ha. That doesn't even make sense. So can I?"
    menu:
        "What should I say?"
        "Why do you want an allowance?":
            $ responsive += 1
            him "Why do you want an allowance?"
            kid "Sometimes there's things I want to buy!"
            him "Like what?"
            kid "Like fruit, or cool socks, or my friend is selling these jumpropes that she made, or sometimes I want to print things."
            menu:
                "What should I say?"
                "I can understand that.":
                    $ responsive += 1
                    him "I can understand that. Sounds like you want to be responsible for your own money, instead of asking us about everything?"
                    kid "Yeah! I just want to do it myself."
                    jump allowance_how
                "You don't need those things!":
                    $ demanding += 1
                    him "Those aren't things you even need!"
                    kid "No, but I really really really really really really want them! Do I need to say 'really' more times?"
                    jump allowance_how
                "If there's something you want, I'll buy it for you.":
                    $ demanding -= 1
                    him "If you want something, I can buy it for you."
                    kid "Daaad, I want to buy it myself!"
                    jump allowance_how
                "We don't have the money for that":
                    $ demanding += 1
                    him "We don't have any extra money for things like that."
                    kid "Really? Not even five cents?" # TODO: currency check?
                    jump allowance_how
        "An allowance?! You already have everything you need!":
            $ demanding += 1
            him "You already have everything you need. Isn't that enough?"
            kid "But I really really want a jumprope!"
            him "You have plenty of toys to play with! Stop complaining! You're so spoiled!"
            kid "I'm not spoiled! Everyone else plays jump rope and I'm the only one that doesn't have one. You're just being mean!"
            him "You need to learn that you can't always have everything you want!"
            kid "{b}You{/b} need to learn to share!"
            him "You can't speak that way to me! Go to your room!"
            kid "Dad, you're not being fair, you just hate me!"
            him "I SAID GO TO YOUR ROOM!"
            $ authoritarian += 1
            
            # Kelly comes home and chides you for yelling.
            her "Hey, [his_name]."
            him "Welcome home."
            her "Where's [kid_name]?"
            him "In her room. She wants an allowance."
            her "Oh, that's a good idea."
            him "Not you too!"
            her "What, you never had an allowance?"
            him "No. My parents handled the money. If I wanted money, I had to work for someone else."
            her "So you don't want to pay her anything."
            him "No! That's not how the world works."
            her "But she wants to earn some money."
            him "She wants to {b}have{/b} money, anyway."
            her "I'm sure there's some way she can make money. Maybe she could do some work for me at the clinic."
            him "She shouldn't get paid to help out her family."
            her "Why not? You do."
            him "...Fine, whatever, as long as you handle it."
            
            return
        "No.":
            $ responsive -= 1
            $ demanding -= 1
            him "No."
            kid "Why not?"
            him "You don't need one."
            kid "I do need one!"
            him "I said no! Quit bothering me about it!"
            kid "You're so mean!"
            $ neglectful += 1
            return
            
    return
    
label allowance_how:
    "(This is tricky... what kind of allowance should I give her?)"
    menu:
        "What should I say?"
        "Make a proposal.":
            $ demanding += 1
            him "You'll need to write up a budget proposal."
            kid "A budget proposal? Seriously?"
            him "Yup. List your expenses, why you think you should have them, and then list possible sources of income."
            kid "That'll be a lot of work!"
            him "Getting money always takes work."
            kid "I guess I could do that."
            $ authoritative += 1
        "You can have a small amount.":
            $ responsive += 1
            him "You can have 25 cents a week." # TODO: currency check?
            kid "25 cents?! That's almost nothing! It'll take me months to save up enough for a jumprope!"
            him "You can earn more doing extra chores if you want."
            kid "Like when I do the dishes and stuff?"
            him "Not your regular chores, extra chores."
            kid "That's mean."
            him "It's up to you. If you want to start right now, you can muck out the barn for a dollar."
            kid "It's so stinky! I hate mucking out the barn!"
            him "Your choice. Better decide soon, though, because I'm about to go do it."
            kid "Okay! Okay! I'll go muck out the barn!"
            him "Great!"
            $ authoritative += 1
        "You can have a large amount.":
            $ responsive += 1
            him "You can have five dollars a week."
            kid "Really? Starting when?"
            him "Right now! Here you go."
            kid "Awesome! I'll be able to buy all sorts of stuff!"
            $ permissive += 1
        "You can have a large amount, but only if you are good and do your chores.":
            $ demanding += 1
            him "You can have five dollars a week if you do all your chores and are good." # TODO: currency check?
            kid "Oh. So basically I'll never get an allowance?"
            him "That's up to you."
            kid "But you never think I'm 'good'! Even when I try really hard and do nice things for everyone and don't hit [baby_name] and do extra chores you never even notice!"
            menu:
                "What should I say?"
                "You'll just have to try harder.":
                    him "I guess you'll just have to try harder."
                    kid "There's no point. Forget it."
                    $ authoritarian += 1
                "I'll make a list of specific things.":
                    him "'Being good' is kind of vague. I'll make a list of specific things, and you can earn a certain amount for each thing you do right that week."
                    kid "So even if I make a mistake I can still have some allowance?"
                    him "Yeah, I don't expect you to be perfect, but I do expect you to try to improve, OK?"
                    kid "Okay, I guess."
                    $ authoritative += 1
                    
    return
        

# 10 Earth years old
# Cleaning her room
label family16:
    "You ask Terra to clean up her stuff (school supplies, rock collection, 'precious things', etc). She says it is clean and she likes it that way."
    menu:
        "Help her make a box for her most special things and choose some things to give away.":
            # charity for Luddites? # it would be in the right timeframe
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Throw her stuff away when she's at school.": # Hmmm, do we need a passive-aggressive variable?!
            $ responsive -= 1
            $ permissive += 1
        "Demand she clean it up now or be grounded.":
            $ demanding += 1
            $ authoritarian += 1
        "Let her keep it. If a little mess makes her happy, what's the big deal?":
            $ responsive += 1
            $ neglectful += 1
    return
   

# 10.5 Earth years old
# Unexplained crying
label family17:
    "She won't stop crying. She won't even explain what the problem is. She's making the other kid(s) cry and the entire house is filled with her wails."
    menu:
        "Leave. You can't handle all the noise!":
            $ neglectful += 1
        "Shut up or I'll give you something to REALLY cry about!":
            $ demanding += 1
            $ authoritarian += 1
        "Go for a walk and let her calm down.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Bring her some tissues and rub her back.":
            $ responsive += 1
            $ permissive += 1
            
        # TODO: Finally it comes out that one of her friends doesn't want to be her friend anymore. May have something to do with community tensions.  You can help her work out a plan of action, sympathize, or tell her that's how life is.
    return

# 11.1 Earth years old
# Wants a bike!
label family18:
    "Terra wants a bike!  There are no bikes.  Or maybe there are, but only for people whose jobs require them?"
    menu:
        "Find a way to get her a bike":
            "A bike is an essential part of childhood!  How will you do it?"
            menu:
                    "Ask if she can help out someone who has a bike and then get to use it.":
                            $ responsive += 1
                            $ demanding += 1
                            $ authoritative += 1
                    "Make a bike out of spare parts.":
                            $ responsive += 1
                            $ permissive += 1
                    "Ask [her_name] to help you make a bike out of spare parts.":
                            $ responsive += 1
                            $ permissive += 1
                            #maybe also relationship with wife improves?
        "There's just no bikes. Deal with it.":
            $ neglectful += 1
        "If she wants a bike, she'll have to be old enough to do the bike job.":
            $ demanding += 1
            $ authoritarian += 1
        "Sympathize, and suggest some alternatives.":
            "Maybe you can teach her to drive a tractor (but not on her own), or to ride a horse (if Lettie's still alive), or make a go cart or something?"
            $ responsive += 1
            $ authoritative += 1                
    return

# 11.8 Earth years old
# Pornography...
label family19:
    "You're sending an e-mail to the farming committee and looking for a photo you took of some crops when you find a pornographic video stored on the tablet."
    "Looking at the time and date, it must be from when [kid_name] was using the tablet yesterday..."
    menu:
       "I can't believe you would do such a thing! You're grounded from using the tablet for a month!":
           $ demanding += 1
           $ authoritarian += 1
       "Watch it. Maybe it's a good one.":
            "It's not. The acting is bad and it's not romantic at all."
            "It's not bad enough to be funny, though -- just bad."
            $ demanding -= 1
            $ permissive += 1
           # Terra catches you and you have to try to justify yourself?           
       "It's not a big deal. Do nothing.":
           $ demanding -= 1
           $ neglectful += 1
       "Ask her about how this got here.":
           "She found it accidentally but was fascinated so she watched it."
           menu:
               "Make a plan for how to avoid pornography in the future.":
                   $ demanding += 1
                   $ responsive += 1
                   $ authoritative += 1
               "Tell her to never do that again.":
                   $ demanding += 1
                   $ authoritarian += 1
               "She's old enough to be responsible for her own viewing habits.":
                   $ responsive += 1
                   $ permissive += 1
           
           return
    return

# 12.4 Earth years old
# Musical Instrument
label family20:
    "Terra wants to learn a musical instrument.  The colony doesn't have any or anyone who plays that instrument."
    menu:
        "FInd a way to make one and find a teacher who at least knows something about music.":
            $ responsive += 1
            $ permissive += 1
        "Encourage her to pick a different instrument.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Playing music is pointless; why don't you learn something useful?":
            $ responsive -= 1
            $ demanding += 1
            $ authoritarian += 1
        "Too bad.":
            $ responsive -= 1
            $ neglectful += 1
    return
    
#####################################################
#
# TEENAGER
#
#####################################################

# 13 Earth years old
# Sarcastic Humor
label family21:
    "Terra's sarcastic humor is hurting people's feelings."
    menu:
        "Punish her.":
            $ demanding += 1
            $ authoritarian += 1
        "Explain the language you expect around your house.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Explain how it makes people feel and beg her to be more considerate.":
            $ responsive += 1
            $ permissive += 1
        "Say nothing.":
            $ neglectful += 1
    return

# 13.6 Earth years old
# Bathing is still a necessity
label family22:
    "Terra refuses to bathe, even though she's getting stinky."
    menu:
        "Just avoid her. She'll get the message eventually.":
            $ neglectful += 1
        "You'll take a bath, or I'll throw you in the river!":
            $ demanding += 1
            $ authoritarian += 1
        "If you decide not to take a bath, you'll need to sleep in the barn with the other stinky things.":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "I hate bathing, too. Maybe if we all stink we won't notice it so much?":
            $ responsive += 1
            $ permissive += 1
        "Why don't you want to take a bath?":
            $ responsive += 1
            # TODO: work something out
        
return
# 14.2 Earth years old
# Chatting with friends on family tablet
label family23:
    "You're waiting for Terra to finish with the family tablet.  She was doing her homework on it while listening to music through headphones, but after a while you check and see she is chatting with her friend."
    menu:
        "Ask her to set herself a deadline to finish her homework":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Tell her if she's not done in ten minutes then she'll lose all tablet time this week.":
            # And no listening to music while doing homework!  How can you concentrate like that?!
            $ demanding += 1
            $ authoritarian += 1
        "Let her talk. It's good for her.":
            $ permissive += 1
        "Take the tablet. You should have priority.":
            $ neglectful += 1
    return

# 14.8 Earth years old
# Alcohol, drugs
label family24:
    "[her_name] asks you about fire grass. Seems like a lot of people have been talking about it lately."
    menu:
        "You're never to go near it, do you hear me?":
            $ demanding += 1
            $ authoritarian += 1
        "Explain what it is and why people are concerned.":
            # Conversation also turns to Pete's distillery and alcohol
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "Give her some of your stash.":
            $ responsive += 1
            $ permissive += 1
        "Give her a vague answer and get back to work.":
            $ neglectful += 1
    return

# 15.5 Earth years old
# A boy...friend?
label family25:
    "Terra sure has been spending a lot of time with some boy. They were holding hands... does she have a boyfriend?"
    menu:
        "Talk to her about it":
            him "Are you guys pretty serious?"
            kid "Yeah, for like the past month!"
            
            # TODO: Make this a loop where you choose lots of things to say
            # but only increase one parenting variable somehow
            menu:
                "You're too young for a boyfriend!":
                    $ demanding += 1
                    $ authoritarian += 1
                "Are you thinking about marriage?":
                    $ demanding += 1
                    $ authoritative += 1
                "What are your plans?":
                    $ responsive += 1
                    $ authoritative += 1
                "Tell me about him":
                    $ responsive += 1
                    $ permissive += 1
                "Have you thought about birth control?":
                    $ demanding += 1
                    $ permissive += 1
        "It's none of your business.":
            $ responsive -= 1
            $ neglectful += 1
        
    return

# 16.1 Earth years old
# Talking Politics
label family26:
    "She disagrees with your recent community decision! She calls you a fascist/spineless worm/panderer."
    menu:
        "Listen to her.":
            "You agree with some of her points, and explain some things she didn't know about."
            "She still disagrees with you, but you can tell she's thinking about it."
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "You don't know what you're talking about!":
            $ demanding += 1
            $ authoritarian += 1
        "Promise to make a better decision next time":
            $ responsive += 1
            $ permissive += 1
        "Laugh it off.":
            $ neglectful += 1
    return

# 16.7 Earth years old
# Fire grass
label family27:
    "[kid_name] comes home smelling like fire grass."
    "You knew that the miners smoked it, but it hasn't been popular among the colonists... until now."
    # TODO: change this based on choices in community events.
    # TODO: give a chance to talk about fire grass earlier
    menu:
        "What's that smell? What have you been up to?":
            $ demanding += 1
            $ authoritarian += 1
        "Hmm, seems like you've been smoking fire grass.  Tell me about it.":
            $ responsive += 1
            menu:
                "Tell her your concerns.":
                    $ demanding += 1
                    $ authoritative += 1
                "Tell her to invite you next time":
                    $ responsive += 1
                    $ permissive += 1
                "Tell her she better not smoke it again, it's not good for her!":
                    $ responsive -= 1
                    $ demanding += 1
                    $ authoritarian += 1
        "Say nothing. It's just a plant, right?":
            $ neglectful += 1
              
    return

# 17.3 Earth years old
# Terra's plans for future
label family28:
    "[kid_name] tells you her plans for the future." # TODO: make these based on your parenting style and choices
    "Some of it seems plausible, but for some of it you can tell she has no idea what she's talking about (expensive colleges, returning to Earth, getting her PhD in astrophysics online, etc)."
    menu:
        "Listen, then make suggestions":
            $ demanding += 1
            $ responsive += 1
            $ authoritative += 1
        "You don't know what you're talking about!":
            $ demanding += 1
            $ authoritarian += 1
        "Support her somewhat-crazy idea.":
            $ responsive += 1
            $ permissive += 1
        "She'll do what she wants. No point in talking to her about it.":
            $ neglectful += 1
    return

# 18 Earth years old
# Terra blames you for some big crisis!
label family29:
    "Big crisis! Foreshadows ending! She says she hates you for some reason and never wants to see you again!"
    menu:
        "Threaten to disown her":
            $ demanding += 1
            $ authoritarian += 1
        "Make sure she knows you love her":
            $ responsive += 1
            $ authoritative += 1
        "Argue with her":
            $ permissive += 1
        "Let her go.":
            $ neglectful += 1
    return

# 18.6 Earth years old (ENDING)
label family30:
    "Family 30 Event"
    return

    