## Family Events
#
# Each family event has several parenting choices.  The decisions for the month
# will affect how much the child's stats increase that month.
#
# "demanding" and "responsive" are just for the current year and affect how much the child's stats increase that month.  They may increase
# (or in some cases, decrease) by 1-5 each month.
# "authoritative", "authoritarian", "permissive", and "neglectful" are cumulative and affect the community's direction and have some correlation to "demanding" and "responsive".  Only increase one per month.
# TODO: The only way to get the "authoritative" option is usually to learn more about the situation by choosing "patient" options, such as "Listen", "Ask why", "Wait", "Think about it", etc.

# Intro event
label family_intro:
    "All [kid_name] needed was a clean diaper, milk, and some love."
    "It didn't always feel simple, though. Sometimes it was all I could do just to stay awake."

    call bedroom_scene(True)
    show kid sad with dissolve
    her sleeping "[his_name]."
    him sleeping "Mrmph?"
    her concerned "[kid_name]'s crying."
    show kid cry with dissolve
    "Sometimes I still had to remind myself that we had a baby, even though it had been several weeks."
    "It was my turn to help her at night."
    him concerned "Okay..."
    show her sleeping
    show kid concerned
    with dissolve
    "I changed her diaper as quietly as I could. I tried not to disturb [her_name], but I could tell she was still awake."
    "I got out the bottle to feed [kid_name]. I was so tired, but I laid her down next to me and watched her in the shadowy moonlight, her tiny cheeks working to eat."
    show kid laugh with dissolve
    "She was too little to hold the bottle herself, but she lifted her hands in jerky movements that brushed against me."
    show kid concerned with dissolve
    "I dozed off and dropped the bottle."
    "Maybe I could prop it up somehow and sleep while she ate? I had a vague feeling that might not be a good idea."
    "I tried to see it as a special time to snuggle, but my brain kept yelling at me to go back to sleep."
    show kid normal with dissolve
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
    show kid cry at midleft, baby_pos

    her "I just wish I knew why she was still crying! We've tried everything -- food, diaper, snuggles, a warm bath, lying on her back, lying on her tummy...I don't know what else we can do."
    him sad "I know. It's been hours..."
    "I knew [her_name] was exhausted. She had been carrying [kid_name] around all day and feeding her every few hours."
    "I wanted to help, but I had spent the whole day cleaning out the barn and was spent.  All I could think about was sleeping."
    "Sleeping..."
    window hide
    show black with irisin
    hide black with irisout
    window show
    "No, I couldn't sleep while they both needed me. But what should I do?"
    menu:
        "Take [kid_name] for a walk.":
            $ responsive += 1
            $ marriage_strength += 1
            him concerned "Here, I'll take her for a walk. I know I could use some fresh air, and we've tried everything else."
            show him determined at center with move
            show kid cry at center, baby_pos with move
            her concerned "It's not too cold out, is it?"
            him normal "She'll be fine wrapped up in her blanket. See if you can get some sleep."
            her sad "Are you sure? I know you're tired, too..."
            him happy "If she's still crying in a few hours, it'll be your turn."
            her happy "Okay, good idea."
            "I snuggled her into her baby carrier and closed the door behind me."
            hide him
            hide kid
            with moveoutleft
            scene farm_exterior with fade
            show night_overlay with dissolve
            show him concerned at center behind night_overlay
            show kid cry at center, baby_pos behind night_overlay
            with moveinright
            him normal "There now, little [kid_name], how's that?"
            "..."
            "She's still crying. I better get further from the house so I don't keep up [her_name]."
            hide him
            hide kid
            with moveoutleft
            scene fields with fade
            show night_overlay with dissolve
            show him determined at center behind night_overlay
            show kid cry at center, baby_pos behind night_overlay
            with moveinright
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
            show him concerned at center with move
            show kid angry at center, baby_pos with move
            him normal "Come on, [kid_name]."
            show him concerned at midright
            show kid angry at midright, baby_pos with move
            "[her_name] went outside to do some reading while I held [kid_name]. I paced restlessly, holding the baby in different positions until [her_name] returned."
            show him at center
            show kid cry at center, baby_pos
            with move
            "She had a big list of things to try, and we tried them all.  I don't know if the white noise and the bath worked, or if she finally just wore herself out, but eventually she stopped crying and fell asleep."
            show kid normal
            $ authoritative += 1

        "Let [her_name] handle it.":
            $ marriage_strength -= 1
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
                    show her sad at midright, squatting
                    show kid sad at center, baby_pos, squatting
                    show bedroom_overlay
                    show night_overlay
                    with dissolve
                    show him concerned at quarterleft with moveinleft
                    "[her_name] was lying on the bed with her arm around [kid_name], her face streaked with red from crying."
                    "I was glad to see she'd stopped crying, but then she looked up at me with hollow eyes and a resigned expression."
                    "She didn't say anything, just lay her head back down and stared at [kid_name] blankly."
                    him sad "[her_name]... I'm sorry. I shouldn't have left. I'm here, now."
                    #show him normal at center behind kid with move
                    #show him normal at quarterleft behind kid
                    hide kid with dissolve
                    show kid sad at quarterleft, baby_pos, jumpinghigh
                    with dissolve
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
            $ confident += 1
            him normal "Sometimes babies cry. Since nothing we're doing is helping, let's just set her down and take a break."
            her concerned "We can't take a break. We're her parents!"
            him annoyed "It won't kill her to not be held for ten minutes.  Come here, [her_nickname]."
            show him normal at center with move
            show kid cry at center, baby_pos with move
            him determined "Come here, little siren."
            show him normal at quarterright
            show kid angry at quarterright, baby_pos
            with move
            show him normal at squatting
            show kid angry at sitting
            with move
            show him normal at standing with move
            "We set [kid_name] down and I set a timer for ten minutes."
            show him determined at midright with move
            "We listened to her scream while we did the dishes together silently."
            "[her_name] started crying, too."
            her sad "Why am I so bad at this?"
            show kid cry with dissolve
            him determined "You've been doing a perfect job all day! It's not your fault."
            her sad "Maybe if she had a different mom she wouldn't cry so much."
            him angry "No way!"
            show kid sad with dissolve
            show him normal at center with move
            him concerned "I've seen you with her; you give her everything she needs. You're patient, loving, and hard-working. She's our daughter, and we're the parents she needs!"
            him sad "We're the parents she's got, and we'll raise her, no matter what!"
            "I held [her_name] for a while and she seemed to calm down a little. When the timer went off, I dashed for the cradle before [her_name] could respond."
            show him normal at quarterright with move
            him happy "Now I'm going to try to be as awesome a parent as you've been all day. You just get some sleep or read a book or whatever you want to do! I got this!"
            # TODO: add dancing with baby animation here?
            show him happy at center, squatting
            show kid concerned at center, squatting
            with move
            "I danced around the room with [kid_name], who seemed slightly calmed by the swaying motions, though she still fussed and squirmed."
            show him happy at right, standing
            show kid concerned at right, baby_pos
            with move
            her normal "[his_name]... You don't have to try to impress me."
            show him happy at midright, squatting
            show kid cry at midright, squatting
            with move
            him happy "What's that? [kid_name] and I can't hear you; we're having too much fun."
            "[her_name] laughed, just for a second, and it was the most beautiful sound I'd heard all day. She put on some music with a good beat, and then came over and joined our dancing."
            "[kid_name] didn't know what to make of it, but we certainly felt better after our crazy midnight dancing."
            "I don't know if it was the music or dancing or if she just tired herself out, but eventually [kid_name] fell asleep and we followed suit."
            $ authoritative += 1
            $ authoritarian += 1

    call bedroom_scene(show_baby=True)
    show kid happy with dissolve
    "The next day, [kid_name] woke up with gurgles and smiles, as if the nightmare of the night before had never happened."
    "That laughter stirred in me so many emotions -- a primal love at her helplessness, frustration at the irony of it all, shame at how selfish I had felt, and underlying everything, a deep exhaustion that magnified every emotion."
    him determined "She really needs us, doesn't she?"
    her concerned "We both need you."

    return

# 10 Earth mos. old
# Get work done or play with kid?
label family2:
    $ family2_work_done = 0
    scene fields with fade
    "Farming's hard work, no doubt about it. No sick days or vacations, either."
    "But I don't mind it, most of the time. Planting season is my favorite, seeing the possibilities in huge swathes of empty soil"
    "Even knowing the seeds are hiding there, it still feels like a miracle whenever they pop out of the ground into young seedlings."
    "I had only a few rows to go when I got a transmission from [her_name] on the radio."

    her radio "[his_name]! I'm leaving right now! There's an emergency at the clinic."
    him surprised "Okay, I'll take care of things here."
    her radio "[kid_name]'s in her crib. Bye!"

    "We had worked out a pretty good schedule, where I would get up early and try to get my most intensive farm work done in the mornings."
    "Then I'd come home at lunchtime and [her_name] would head over to the clinic for appointments and drop-ins."
    "But this sounded like something that couldn't wait."
    "[her_name] didn't say if [kid_name] was asleep or not..."
    menu:
        "What should I do?"
        "Go straight home.":
            $ responsive += 1
            "I didn't want to leave [kid_name] alone. If she was asleep, I could setup the baby monitor and go back out to work."
            "I decided to head home. It bugged me to leave the planting unfinished but [kid_name] was more important."
            "It was a good thing, too. [kid_name] was kind of cry-shouting. If she could talk, it'd mean something like 'Mom! Dad! Where are you?'"

        "Ask [her_name] for more information.":
            $ responsive += 1
            him determined "Hey, is [kid_name] asleep? Did you setup the baby monitor?"
            "I waited for a few minutes, but [her_name] didn't respond. She was probably on the other channel talking to whoever had the emergency."
            "I decided to head home. It bugged me to leave the planting unfinished but [kid_name] was more important."
            "It was a good thing, too. [kid_name] was kind of cry-shouting. If she could talk, it'd mean something like 'Mom! Dad! Where are you?'"

        "Finish up the last few rows and then go home.":
            $ demanding += 1
            $ family2_work_done += 1
            "[kid_name] could wait a few minutes while I finished this up. I hated leaving things half-done."
            "It ended up taking almost an hour, but I sure felt satisfied to have finished the entire field."
            "But as I headed for home, I could hear [kid_name] crying urgently."
            "When I finally walked into her room, she looked at me with a hurt, betrayed expression. She couldn't really talk yet, but her eyes said it all."
            "All she needed was someone she could depend on, and I had failed at the most basic task: being there."

    scene farm_interior with fade
    show him normal at center
    show kid surprised at midright, baby_pos
    "I managed to calm [kid_name] down with some snuggles and a snack."
    "I built a house out of blocks with her, but then my mind started to wander."
    show kid happy
    show him annoyed
    with dissolve
    "I was hoping to get a lot more done today. I had to get these seeds in the ground right away, or my whole schedule would be off and our crop yield would suffer."
    "If there had been a big accident, [her_name] might be needed at the clinic tomorrow, too, so I couldn't just put everything off."
    show kid shifty
    show him concerned
    with dissolve
    "Maybe I could get some things done during [kid_name]'s nap? I checked the clock. No, she wouldn't be ready for that for a few more hours."
    show kid laugh
    show him surprised
    with dissolve
    "She brought me a picture book and I read it to her, but my mind was still racing for how I could get my work done."

    menu:
        "What should I do?"
        "Stay and play with her.":
            $ responsive += 1
            "[kid_name] clearly was enjoying our time together; I should try to do the same."
            "People kept telling me she'd grow up fast, but so far it felt very slow."
            "I tried to be in the moment with [kid_name] and do what she wanted to do as the hours stretched on."
            show him at midright with move
            show kid normal with dissolve
            "We had lunch together and went for a walk and started some beans cooking for dinner."
            scene farm_exterior with fade
            show him concerned
            show kid normal at right
            with dissolve
            "I tried to wear her out by crawling all around the yard with her."
            show him annoyed at left
            show kid laugh at left
            with move
            "I checked the time again and again until finally it was naptime."
            show him normal at center
            show kid annoyed at center
            with move
            show kid sad at center, baby_pos with move
            "[kid_name] seemed to sense my eagerness to leave, though, or maybe she just missed her routine with her mom, because she didn't want to go to sleep."
            scene black with fade
            "When she finally settled down, I rushed out and was able to at least start on another field before she woke up."
            # TODO: lower crop yield
            $ permissive += 1

        "Try and do some work at home.":
            $ responsive += 1
            "There were a few things I could do at home -- researching, planning, checking the surveillance cameras..."
            show him determined with dissolve
            show kid normal at midleft, baby_pos with move
            "So I worked on those while [kid_name] crawled around, took all the pots and pans out of the cupboards, and banged on them."
            show kid shifty at right, baby_pos with move
            "She pulled the blankets and sheets off all the beds trying to climb up and bounce on them."
            show him annoyed with dissolve
            show kid annoyed at midright, baby_pos with move
            "We played peek-a-boo for a bit, but then she kept trying to grab my computer pad."
            show kid nervous at center, baby_pos with move
            "Seems like she wanted a turn, but I couldn't do any of my work without the computer pad."
            menu:
                "What should I do?"
                "Let her watch a show.":
                    $ responsive += 1
                    "I turned on a show she liked. I started some beans cooking for dinner, but I really didn't have anything else I could do at home without my computer pad, so I ended up watching it with her until naptime."
                    $ permissive += 1
                "Take her outside to play while you work.":
                    $ family2_work_done += 1
                    scene farm_exterior with fade
                    show him determined at midright
                    show kid surprised at center, baby_pos
                    with dissolve
                    "She might have more fun outside. I dragged a chair out there where I could sit and work."
                    show kid normal at right, baby_pos with move
                    "She crawled around for a few minutes, but then she crawled back and pulled herself up to stand using my leg."
                    show kid annoyed at center, baby_pos with move
                    "She grabbed at my screen again. This was one stubborn child!"
                    menu:
                        "What should I do?"
                        "Let her watch a show.":
                            $ responsive += 1
                            show kid happy with dissolve
                            "I turned on a show she liked. I really didn't have anything else I could do at home without my computer pad, so I ended up just watching it with her until naptime."
                            $ permissive += 1
                        "Show her something fun to do.":
                            $ responsive += 1
                            $ demanding += 1
                            $ family2_work_done += 1
                            "Seems like she just needed an idea of something else to do."
                            show kid happy with dissolve
                            "I brought out a big bowl filled with water, and a funnel and a cup. I set them down on the dirt and showed her how to scoop up water with the cup and pour it in the funnel to make mud."
                            "She happily played in the water and mud until naptime, and I finished the research paper I was reading."
                            $ authoritative += 1
                        "Yell at her to stop.":
                            $ demanding += 1
                            $ family2_work_done += 1
                            him angry "[kid_name], stop it! I'm working! You go play."
                            "This just seemed to make her mad."
                            kid nervous "Aaa! Aaaa! Aaaaaaa!"
                            "I ignored her. I stood up and worked on my computer pad that way, trying to ignore her shouts and tugs on my pants."
                            show him annoyed
                            show kid angry
                            with dissolve
                            "It was pretty hard to concentrate, but I did manage to make my way through the research paper I was reading."
                            $ authoritarian += 1

        "Put her in the backpack and go back to work.":
            $ confident += 1
            him happy "Alright, [kid_name], want to go ride the tractor? Huh? Do you?"
            "I don't know how much of my words she understood, but she sensed my excitement and smiled up at me."
            him normal "Yeah! Let me just put you in the backpack..."
            him concerned "Both feet at the same time, now... Left, then right, no, hey, stop bending your legs!"
            him happy "There we go! We're going to go make plants grow!"
            kid happy "Daa!"
            scene tractor with fade
            "We got on the tractor and I drove back to the field that needed planting."
            "I had to kind of sit on the edge of the seat so that there was room behind me for the backpack. It wasn't the comfiest seat, but it worked."
            "Terra cooed and kicked and played with my hair and seemed to enjoy the ride..."
            "...for about ten minutes."
            kid normal "Aaaa!"
            him happy "I know! Isn't this fun?!"
            kid angry "Aaa! Aaaaaah!"
            him surprised "I guess it's probably pretty boring for you, huh?"
            kid normal "..."
            him concerned "Sorry, baby, but we have to get this work done, or we won't have food to eat."
            kid angry "Aaaa!"
            "She kicked her legs more, in frustration now. She pushed against me, trying to worm her way out of the backpack, but she was strapped in tight."
            "I tried to think about what would help her be happy while I worked on these fields for the next hour or two."
            $ family2_activity_count = 0
            $ family2_sung = False
            $ family2_eat = False
            $ family2_play = False
            $ family2_talk = False
            menu family2_baby_activities:
                "Sing a song." if not family2_sung:
                    $ family2_activity_count += 1
                    $ family2_sung = True
                    $ family2_work_done += 1
                    $ responsive += 1
                    "I tried to remember some songs she might like."
                    him surprised "Do you know 'Head, shoulders, knees, and toes?"
                    "She seemed to like that one.  I sang all the songs I knew, from 'Arroz con Leche' that I learned in elementary school Spanish class, to the pop hit 'Eclipsed by Your Love', to humming 'Beethoven's Fifth'."
                    him normal "You like that?"
                    kid normal "Aaa, baaa baa baa, daa."
                    him happy "Yeah!"
                    kid angry "..."
                    him concerned "I need to learn some more songs!"
                    jump family2_baby_activities

                "Give her something to eat." if not family2_eat:
                    $ family2_activity_count += 1
                    $ family2_eat = True
                    $ family2_work_done += 1
                    $ responsive += 1
                    him surprised "Are you hungry, [kid_name]? I didn't bring any food..."
                    him happy "What am I saying? I live on a farm; I'm surrounded by food!"
                    "I jumped down and ran over to a field I had planted several weeks earlier."
                    him normal "Looks like it's time to thin these out, anyway. Want some sprouts?"
                    "I started thinning the little sprouts, handing some up to her to munch on."
                    "She spit some of them out on the back of my neck, but she wasn't crying, so that was good."
                    "I thinned the whole row and turned back to sit down at the tractor."
                    kid angry "Aaaa!"
                    jump family2_baby_activities

                "Give her something to play with." if not family2_play:
                    $ family2_activity_count += 1
                    $ family2_play = True
                    $ family2_work_done += 1
                    $ responsive += 1
                    him surprised "You probably want something to play with, huh? I didn't bring any toys..."
                    him happy "But kids have been growing up since before toys were invented, so I think we'll be okay! Here, have a stick."
                    "She took the stick and stuck it in her mouth. Then she whacked my head with it."
                    him sad "Ouch."
                    "Then she dropped it."
                    him annoyed "I'm not going to get much done if I have to keep picking up your stick. Don't drop it, okay?"
                    "She held onto it for several minutes, whacking my head or chewing on it, or whatever she was doing. It was hard to see her while she was in the backpack."
                    "And then she dropped it."
                    kid angry "Aaaa!"
                    jump family2_baby_activities

                "Talk to her." if not family2_talk:
                    $ family2_activity_count += 1
                    $ family2_talk = True
                    $ family2_work_done += 1
                    $ responsive += 1
                    him surprised "You feeling lonely back there? Don't worry, we're together, [kid_name]!"
                    kid angry "Baa, baaaaaa!"
                    him surprised "Ooh, are you turning into a sheep? Your arm is so soft, it's like a little lamb. Baa, baa!"
                    kid happy "Baa, baa!"
                    him happy "Yeah, you're a little sheep! Or maybe you're a baby cow?"
                    kid normal "..."
                    him normal "You know, a cow. Moo, moo?"
                    kid normal "Maa, maaa."
                    him happy "Did you say 'mama'? Ha ha, don't let mom hear you comparing her to a cow. She wouldn't like that."
                    kid angry "Aaaa!"
                    him surprised "Hey, don't worry, I won't tell her. Ummm, hmmm, what else should we talk about?"
                    kid angry "Aaaa!"
                    him normal "Yeah, I don't want to talk about politics either. Why don't I tell you about plants?"
                    kid normal "Aaa?"
                    him normal "Plants need water, sunlight, and nutrients from the soil to survive. But if you want them to grow big and strong, you have to make sure they have the right amounts of all of these."
                    kid angry "Aaah! Aaa! Aaaaaaaa!"
                    him annoyed "Okay, you don't have to scream, we don't have to talk about plants if you don't want to."
                    jump family2_baby_activities

                "Yell at her.":
                    $ demanding += 1
                    $ responsive -= 2
                    $ family2_work_done += 5
                    him angry "Be quiet and let me work!"
                    kid angry "Waaah!"
                    him determined "Sorry, [kid_name], but the work has to be done. And I'm going to keep you safe while I do it."
                    $ authoritarian += 1

                "Give up and let her cry." if ((family2_activity_count >= 1) and (family2_activity_count < 4)):
                    $ demanding += 1
                    $ family2_work_done += 5
                    him concerned "I'm sorry, [kid_name], but I just need to get this work done. I know it's boring for you, but you'll survive, okay?"
                    $ authoritative += 1

                "Give up and go home." if ((family2_activity_count >= 1) and (family2_activity_count < 4)):
                    $ responsive += 1
                    him concerned "You're probably pretty uncomfortable and bored back there, huh? I guess I'll have to just do this another time."
                    $ permissive += 1

                "Finish up and go home." if (family2_activity_count >= 4):
                    $ demanding += 1
                    $ confident += 1
                    him happy "Guess what, [kid_name]?? We're all done!"
                    kid angry "Aaa!"
                    him normal "Yeah! We did it!"
                    "I was completely exhausted, mentally and physically and psychologically, but I finished the planting I needed to for today."
                    $ authoritarian += 1

        "Leave her in her crib.":
            "I put her in her crib. She wouldn't like it, but she'd be safe enough there for a few hours while I finished the planting."
            "Sure enough, she cried as soon as I set her down. I turned on the baby monitor, but turned the volume on my receiver down so I couldn't hear her screaming."
            "I closed the door, hopped on the tractor and sped away from the house."
            "Every once in awhile, I turned on the baby monitor. Sure enough, she was still screaming. At least that meant she was okay, right?"
            "After about an hour she finally stopped crying; maybe she had fallen asleep."
            "Or maybe she finally realized that I wasn't going to come back until I was done."
            $ family2_work_done += 5
            $ neglectful += 1

    scene farm_interior with fade
    show him determined at midright with dissolve
    show her concerned at midleft with moveinleft
    "Late that night, after I fed [kid_name] dinner and she had fallen asleep, [her_name] finally came home."
    "She trudged into the house, looking at least as tired as I felt."
    show him normal at midleft with move
    "I caught her up in a big hug and kissed her twice."
    show him surprised at midright with move
    him surprised "Rough day?"
    her concerned "Yeah. We had to operate... it wasn't pretty, but she survived."
    him concerned "Operate?! Sounds serious... who was it?"
    her sad "Helen. She had appendicitis."
    him surprised "Have you ever fixed one of those before?"
    her determined "No, but I did a surgical rotation where I helped perform one. But it's quite different to be the one in charge."
    him determined "It's a good thing you have a real nurse helping you out now."
    "[her_name] seemed to be thinking about something else, though."
    her concerned "Yeah...I hope Helen will be okay."
    "I made her up a plate of beans while we talked."
    "From the way she devoured them, I guess she hadn't eaten all day."
    him concerned "How'd Pete take it?"
    her flirt "He was kind of a wreck. I tried to keep him busy, so he didn't have time to get drunk or anything."
    him surprised "What about Travis? That kid is the cutest hurricane of destruction I've ever seen."
    her normal "I know. It's hard to believe he's just a year older than [kid_name]..."

    her concerned "How was [kid_name]? I guess she's asleep now?"
    him normal "Yeah, she's asleep. "


    if (family2_work_done <= 2):
        # TODO: lower crop yield
        extend "I didn't get much done, but she had a good time."
    else:
        extend "I managed to get all my work done, though she didn't like it very much."

    "[her_name] nodded, and ate another spoonful of beans. She seemed to be thinking about something."

    her determined "[his_name], we need help."
    him annoyed "With what?"
    her annoyed "With [kid_name]! I saw Pete and Helen at the clinic today, and you know where their son Travis was?"
    him surprised "Terrorizing the clinic's cotton ball supplies?"
    her determined "No! He was at Sister Naomi's."
    him normal "Oh, well, that was nice of her."
    her normal "She offered to let [kid_name] come, too."
    him happy "That sounds great!"
    her determined "Good, I'm glad you agree. Fridays are our days, so all the little kids will come over to our house on Fridays."
    him surprised "What? I thought you just said she'd be at Sister Naomi's!"
    her normal "It's a childcare co-op. Each of the families takes one day a week to have the kids over to their house. Sister Naomi doesn't have any kids, but she volunteered to be in the rotation anyway to help us out."
    him normal "So... [kid_name] will be at other houses four days a week, and we'll have all the kids over once a week?"
    her normal "That's how it works."
    him concerned "..."
    her concerned "I...thought it would be a good thing, for everyone."
    menu:
        "You should have asked me first.":
            $ marriage_strength -= 1
            him annoyed "You should have talked to me about it first. After all, I'll be watching them half the time."
            her annoyed "It's obviously more efficient and better for everyone. I thought you would see that."
            him angry "You can't just make these kinds of decisions without me! We're both her parents!"
            her angry "I'm going to have to be at the clinic a lot more in the next few weeks, so you'll need to watch her."
            him annoyed "You're doing it again! We need to decide these things together!"
            her annoyed "There's nothing to decide. There's only one real choice if both of us are going to continue to work full time."
            him concerned "We both have to work; it's in our contract."
            her "..."
            him "..."
            her surprised "So what do you think we should do?"
            him concerned "I think we should join the childcare co-op."
            her annoyed "I agree."
            him happy "Good! That wasn't so hard, was it?"
            her determined "So, you just want to make all the decisions?"
            him annoyed "I want us to make them together."
            her annoyed "Yeah. Together."

        "This'll be great!":
            $ marriage_strength += 1
            him happy "This will be great! I can concentrate on work during most of the week, and concentrate on [kid_name] on Fridays."
            her normal "[kid_name] and three other toddlers. Including Travis."
            him happy "Still, it'll be so much better than trying to work and keep her happy at the same time."
            her happy "I'm glad you agree."
            him flirt "And maybe we'll even have time to fit in a little you-and-me time on some of those days..."
            her flirt "I hope so."
        "I've never watched four toddlers before.":
            $ marriage_strength += 1
            him surprised "Four toddlers at once?! I can barely handle one!"
            her concerned "That's what I thought, too, but Sister Naomi says it's not much harder..."
            him determined "I guess we'll find out. Hopefully they're not all like Travis."
            her flirt "Well, I'm sure you'll do just fine, Mr. Superdad."
            him happy "Superdad? Have I earned that title?"
            her happy "I'm pretty sure you have."
            if (family2_work_done >= 5):
                "I felt a twinge of guilt as she said that. I hadn't been a super dad today at all; super farmer, maybe, but I'd let Terra cry in order to get my work done..."
                "[her_name] saw the look on my face and stroked my face."
                her surprised "What is it?"
                him sad "Today was... it was a long day."
                "She leaned her head on my shoulder and sighed."
                her concerned "Me too, [his_nickname]. But we're still here, together, all three of us."

    return

#####################################################
#
# TODDLER
#
#####################################################

# 18 Earth mos. old
# Camping trip, putting everything in her mouth
label family3:
    scene farm_interior with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center, baby_pos
    with dissolve
    $ random_crop = farm.crops.random_crop(include_animals = False)
    him concerned "Whew, I thought I'd never finish harvesting all those [random_crop]!"
    her surprised "You're all done?"
    kid laugh "All done!"
    him happy "Yeah!"
    her happy "Good job! I'm glad they're doing so well."
    him normal "I think I'm going to take it easy for a few days..."
    her concerned "Yeah..."
    show her happy with dissolve
    show kid shifty at left, baby_pos with move
    extend " Hey, you know what we've never done?"
    him flirt "I can think of a lot of things."
    her annoyed "As a family?"
    him surprised "Oh. No, what?"
    her happy "Gone on vacation!"
    show kid laugh at center, baby_pos with move
    him annoyed "You went to the ocean that one time..."
    her annoyed "Like I said, as a family."
    him surprised "Where do you want to go? There's no hotels or anything..."
    show kid surprised at center, baby_pos with dissolve
    her surprised "I thought maybe we could go camping?"
    him happy "That sounds great! I love camping!"
    show kid laugh at center, baby_pos with dissolve
    "Our excitement was contagious. [kid_name] stood up and clapped her hands. I picked her up and tossed her up into the air, catching her into a big hug." # TODO: animate this?
    show him at center with move
    show kid normal at jumpinghigh with move
    him "You want to go camping too, huh, [kid_name]? Sleep outside?"
    kid laugh "Ow sai!"
    show kid normal at midright, baby_pos with move
    "She squirmed to get down, then toddled over the door and banged on it with her hands."
    show kid shifty at right, baby_pos with move
    her concerned "We don't have to go far... just over the south ridge or something. Just take a break from everything for a few days."
    him normal "I know the perfect spot! Let's go tonight!"
    her flirt "I think we'll need a little time to get a few things together. How about tomorrow?"
    show kid annoyed at midright, baby_pos with move
    him happy "Okay, tomorrow! Right after you're done at the clinic!"
    him surprised "Oh...can you really leave? What if something happens while you're gone?"
    her determined "Everything will be fine. I'll take a radio so they can contact me if there's an emergency."

    scene path with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center, baby_pos
    with moveinleft
    "The next day, we packed up some food and makeshift bedrolls and some equipment for starting fires."
    "[her_name] and I took turns carrying the equipment and carrying [kid_name]. She liked to walk, but she walked so slowly because she wanted to stop and look at every rock, bug, and bush."

    hide him
    hide her
    hide kid
    with moveoutright

    # TODO: get background.
    # scene sunset with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center, baby_pos
    with moveinleft

    "Finally, we arrived."
    him flirt "Remember this spot?"
    her flirt "It seems kind of familiar... though I mostly remember the food."
    show kid shifty at quarterright, baby_pos with move
    him surprised "The food?"
    her happy "Yeah, you made such a delicious picnic dinner!"
    show kid annoyed at right, baby_pos with move
    show her flirt at center with dissolve
    extend " And then we stayed out here all night long..."
    hide kid with moveoutright
    him happy "Oh, so you do remember!"
    her normal "Of course I do. It's a beautiful place."
    show him sleeping
    show her sleeping
    with dissolve
    "I held [her_name] close for a minute, both of us savoring the memory."
    her surprised "Oh! Where's [kid_name]?!"
    show him surprised with dissolve
    "We had just set her down, and already she had wandered off. We both scanned the area. I tried not to be too worried... she couldn't have gone far, right?"
    her concerned "I don't see her! Where is she?!"
    him concerned "[kid_name]! [kid_name]!"
    "She was too young to respond or come running back. [her_name] was heading back the way we had come, calling out with increasing urgency."
    hide her with moveoutleft
    show him concerned at quarterright with move
    "It had been only about five minutes since we had seen her, but my mind started to fill with all the terrible things that could have happened to her."
    show him sad at quarterleft with move
    "But then I saw our daughter, sitting on the other side of a large rock."
    # TODO: bg
    #scene canyon with fade
    show kid surprised at quarterright, baby_pos with dissolve
    show him concerned at midright with moveinleft
    him determined "She's over here!"
    show her sad at quarterright behind kid with moveinleft
    "She was chewing on some sticks she found on the ground."
    her concerned "Oh no! Are these poisonous?! I can't remember..."
    show kid happy with dissolve
    "[her_name] got the sticks out of [kid_name]'s mouth while I checked Dr. Lily's  plants guide on my computer pad. [kid_name] just smiled and showed us her tiny teeth."
    show her concerned at midleft
    show kid normal at midleft, baby_pos
    with move
    him normal "Looks like that plant's harmless."
    show him concerned at center with move
    "[her_name] snuggled her close and I held them both, wishing my embrace could create a force field equipped with a homing beacon to protect my little [kid_name]. I felt like I had failed, somehow, like a real father would have done something differently."
    her concerned "I'm sorry, [his_name]. I should have been watching her closer."
    him surprised "That's just what I was going to say!"
    show kid annoyed with dissolve
    "[kid_name] strained against [her_name]'s arms and twisted and writhed, trying to get down."
    her sad "Oof! This girl is getting heavy!"
    show kid shifty at midleft, baby_pos with move
    "[her_name] set her down, but she went right back over to her sticks and began chewing on them again."
    show kid normal at quarterright with move
    "We gave each other exasperated looks and then laughed."
    show kid happy with dissolve
    him happy "Clearly, this girl needs something to gnaw on."
    her flirt "Got anything our little hamster can cut her teeth on?"
    him concerned "Maybe..."

    menu:
        "What should I do?"
        "Make her a chewing toy":
            $ responsive += 1
            $ permissive += 1
            him normal "I'm going to make her a chew toy!"
            her happy "I think she'd like that."
            "I got some of the sticks she loved so much and carved them smooth so they would be nice and clean and without splinters."
            show kid shifty at midright, baby_pos with move
            "I made sure there were no sharp ends and then gave them to her."
            show kid surprised with dissolve
            "She grabbed them from me, but then frowned and picked up some other sticks off the ground."
            show kid annoyed at quarterright, baby_pos with move
            her surprised "I guess she likes the bark?"
            "I kept giving her the ones I had made, but she didn't want them at all."
            show kid happy with dissolve
            him annoyed "Well that was a lot of work for nothing."
        "Give her something else she can chew on.":
            "I pulled open my pack and rifled through it. There must be something in here she can put in her mouth, right?"
            "I found a carrot."
            her surprised "Oh, I've never fed her carrots before. She's not going to choke on them, is she?"
            him normal "Well, I think she has enough teeth to give it a try."
            show him at midright with move
            "I cut into a long, thin strip and handed it to her."
            show kid surprised with dissolve
            "She gnawed on it thoughtfully for a few minutes."
            her normal "Hmm, looks like she likes it!"
            "...and then she spit out the chewed-up shreds."
            show kid annoyed with dissolve
            him normal "It's better than chewing on sticks, right?"
            her concerned "Probably?"
            $ responsive += 1
            $ demanding += 1
            $ confident += 1
            $ authoritative += 1
        "Don't let her put the sticks in her mouth.":
            show him determined at midright with move
            show kid annoyed at midright, baby_pos with dissolve
            him determined "No no, [kid_name]. Not in your mouth."
            show kid annoyed at quarterright, baby_pos with move
            show kid nervous at midright, baby_pos with move
            "She went for them again, but I held her back."
            him determined "You can't just put everything your mouth. No."
            show kid at center, baby_pos with move
            kid angry "No! No no no no no!"
            her annoyed "You can't just tell her 'no' about everything."
            him annoyed "She shouldn't be chewing on those."
            her normal "Then show her what she can chew on."
            "[her_name] handed her an apple."
            show her at center with move
            her "This is for chewing!"
            show her at midleft with move
            show kid surprised with dissolve
            "[kid_name] took the apple and put her mouth on it, but she couldn't figure out how to take a bite with her tiny mouth."
            show kid nervous with dissolve
            "She threw it in the dirt."
            him angry "Hey, stop that! Now no one wants to eat it."
            her annoyed "Relax, it's just a little dirt."
            "She rinsed the apple off with our water bottle and took a bite."
            her happy "Yum! See, [kid_name]? Yummy apple!"
            show kid surprised with dissolve
            "[kid_name] gnawed on it a little more. She could make better progress now that there were some uneven surfaces to work with, but eventually she threw it in the dirt again."
            $ demanding += 1
            $ authoritarian += 1
        "Let her chew on the sticks. It's good for her immune system, right?":
            him normal "Those sticks are fine. They're not poisonous."
            her concerned "But, they're really dirty! She's going to get sick. Animals have probably peed all over them."
            him annoyed "We're outside. That's a totally normal thing."
            her annoyed "That doesn't mean I want to feed it to my baby!"
            him determined "She's not a baby anymore. She's a nature explorer! Right, [kid_name]?"
            "[kid_name] sensed my enthusiasm and smiled widely, waving her sticks at us."
            show kid laugh with dissolve
            $ responsive += 1
            $ confident += 1
            $ neglectful += 1

    # TODO: bg
    scene black with fade
    "Camping was ten times harder with little [kid_name]. We had to make sure she didn't fall in the fire when we cooked our dinner, if we put her on our backs she got heavy fast, and it was tricky trying to keep an eye on her when we set her down."
    show him sleeping at midright
    show her sleeping at center
    show kid normal at center, baby_pos
    show night_overlay
    "When it started to get dark, we were both exhausted."
    him flirt "I was going to suggest some romantic star gazing, but..."
    her concerned "Yeah, the only thing I want to look at right now is the inside of my eyelids."
    him normal "Yeah, I'm exhausted. But wasn't this great?"
    her normal "It was a nice change of scenery. And that sunset was gorgeous."
    him flirt "Just like you."
    her happy "Good night, [his_nickname]."
    him normal "Good night, [her_nickname]."
    return


# 2 Earth years old
# Picky eater!
label family4:
    scene farm_interior with fade
    "Months passed by in a busy blur of planting and harvesting."
    "[kid_name] learned several new words every day, and her little fingers that used to be so clumsy were now holding crayons and picking up tiny grains of rice."
    "...and then throwing them on the floor."
    show him determined at midright
    show her determined at midleft
    show kid nervous at center, baby_pos
    with dissolve
    kid "No!"
    her annoyed "Rice is what's for dinner, sweetie."
    him normal "You know daddy's friend Mr. Thuc? He worked hard to grow that rice, so let's not waste it, okay?"
    kid annoyed "Yucky."
    "[her_name] took away [kid_name]'s plate before she could throw any more of it on the floor."
    her concerned "It is kind of plain."
    # TODO: Change based on recent plants grown? Or does that not make sense because everyone's giving them to the storehouse now?
    him surprised "I think it tastes better with the onions and beans."
    her surprised "Yeah, they're a little bland, too. Maybe it needs more salt?"
    him normal "Try the beans, [kid_name]. Yum!"
    "I put one on her plate and she pushed it right back at me."
    kid shifty "Yucky."
    her normal "Ooh, I know just what this needs. I'll be right back."
    hide her with moveoutleft
    "I tried not to feel offended that she didn't like the beans I had cooked. It wasn't gourmet cuisine, but I had added some herbs and cooked it to just the right consistency."
    "I thought it was pretty good. But maybe I just wasn't as picky."
    him concerned "You haven't eaten a thing all dinner!"
    kid annoyed "Ap'sos."
    him annoyed "We don't have applesauce. Right now we're having rice and beans."
    kid nervous "Ap'sos!"
    him determined "Where'd you even get applesauce from? I haven't seen it at the storehouse for a long time."
    kid shifty "Travis mommy."
    "Travis' mom - that would be Helen. [kid_name] had been over there for coop daycare today. Somehow she always had sweet things for the kids to eat."
    "...Sweet things to ruin their tastebuds for real food."
    menu:
        "What should I say?"
        "You must eat this dinner.":
            $ demanding += 1
            him angry "You're not leaving the table until you eat all of this food."
            kid annoyed "Yucky!"
            him determined "Then you'll stay here."
            "She picked up a grain of rice, looked me right in the eyes, and threw it on the floor."
            "I put it right back on her plate."
            him annoyed "You still have to eat it."
            show kid at midleft, baby_pos with move
            "She slid off her chair and made to run away, but I put her right back in it."
            show him at center with move
            show kid at center, baby_pos with move
            him determined "No. Eat your dinner."
            kid nervous "No! Yucky!"
            "She squirmed in my hands and started to slide out so I gripped her arms more tightly and held her in place on my lap."
            him annoyed "Eat. Your. Dinner."
            kid angry "No! No no no no no no!"
            "She was screaming now, and her screams turned into crying and thrashing. She kicked the table and my cup of water tipped over, splashing us both."
            show her surprised at midleft with moveinleft
            her surprised "What's going on out here?!"
            him angry "She's a disobedient, ungrateful brat!"
            kid cry "Wahhhhhhh!"
            her annoyed "[his_name], go outside and calm down. Let me deal with her."
            menu:
                "What should I do?"
                "Leave":
                    $ marriage_strength -= 1
                    him determined "..."
                    show kid at midleft, baby_pos with move
                    hide him with moveoutleft
                    "I handed [kid_name] to [her_name] and tried not to slam the door on my way out."
                    scene farm_exterior with fade
                    "I hated how spoiled [kid_name] was acting."
                    "I hated [her_name] telling me what to do."
                    "...I hated that she was right."
                    "How could I expect [kid_name] to control her actions if I was getting this angry over food?"
                    "On the other hand, we couldn't just let her eat whatever she wanted, even if we did happen to have it around."
                    "I didn't know what to do."
                    scene farm_interior with fade
                    show her normal at midright
                    show kid normal at midright, baby_pos
                    with dissolve
                    show him determined behind kid,her at midleft with moveinleft
                    "Finally I came back home. [her_name] and [kid_name] were snuggled up on the bed reading a book together."
                    "[kid_name]'s plate of food sat on the table, untouched."
                    show her angry with dissolve
                    "[her_name] looked at me like I was a naughty dog or something. I bristled."
                    show him annoyed with dissolve
                    menu:
                        "What should I do?"
                        "Give them a hug":
                            $ responsive += 1
                            $ marriage_strength += 1
                            show him normal at center with move
                            show her concerned with dissolve
                            "I pushed away my negative feelings, bent over and hugged them both."
                            "I just wanted to show them that I loved them. That was more important than anything else."
                            "I sat down next to [her_name] and she laid her head on my shoulder. [kid_name] slid off her lap, and I closed my eyes to rest for a moment."
                            show him sleeping
                            show her sleeping
                            with dissolve
                            show kid shifty at midleft with move
                            show him surprised with dissolve
                            "When I opened them, [kid_name] was sitting at the table, eating her food."
                            "I felt like a fool, but I decided to just leave it alone."
                        "Demand [kid_name] finish her food.":
                            $ demanding += 1
                            him determined "Feeling better? Okay, now it's time to finish your dinner."
                            her annoyed "[his_name]..."
                            kid nervous "No! Yucky!"
                            "And we started all over again..."
                        "Apologize":
                            $ responsive += 1
                            $ marriage_strength += 1
                            him sad "I... I'm sorry. I was out of control."
                            "[her_name] squeezed my hand and gave me a little smile."
                            her normal "It's okay."
                            show kid annoyed with dissolve
                            "[kid_name] gave me the stinkeye."
                            him determined "I'm sorry, [kid_name]. I was not trying to hurt you. I'm trying to help you eat healthy foods to grow big and strong."
                            show kid shifty at center, baby_pos with move
                            "[kid_name] seemed to think about this for a moment, then went to the table and carefully spooned up a bit of beans."
                            show kid laugh at midleft, baby_pos with move
                            "She brought it over near my mouth."
                            kid normal "Daddy eat."
                            "I opened my mouth and allowed her to feed me."
                            him normal "Mmmm! Yum!"
                            "She spooned some into her own mouth and copied me."
                            kid laugh "Mmmm! Yum!"
                            him happy "That's my girl!"

                        "Eat your dinner.":
                            "Maybe no one else was hungry, but I was."
                            "I sat down and started to eat."
                            "[her_name] soon joined me."
                            "I didn't say anything to [kid_name], just shoveled beans and rice into my mouth in silence."
                            "When I left the table to wash my plate, she walked over and ate her rice. She carefully pushed the beans to one side."
                            "I didn't have the energy to argue with her anymore."

                "Don't leave":
                    $ demanding += 1
                    him angry "No! Nobody's leaving this table until [kid_name] eats her dinner!"
                    her annoyed "[his_name]..."
                    show kid angry with dissolve
                    "That's when [kid_name] bit my wrist."
                    him surprised "Yeow!"
                    "I didn't think I'd be the kind of parent that spanked their kid."
                    him angry "You do NOT hurt your family!"
                    "But I did."
                    him determined "You show your parents respect!"
                    kid cry "Wahhhhhh!"
                    "Part of me still thinks she deserved it."
                    her angry "[his_name], stop! That's enough!"
                    "But I know when I was a kid, I hated being spanked."
                    "Maybe it changed my behavior for a short time, but mostly I just felt mad at my dad for being out of control."
                    "I have a lot more sympathy for him now."
                    "It was only later that I realized the irony of me demanding respect and nonviolence from [kid_name] while spanking her."

            $ authoritarian += 1

        "I'll see if I can get you some applesauce.":
            $ responsive += 1
            him determined "Okay, sweetie, I'll see if I can get you some applesauce."
            "We didn't have any applesauce, but we did have a few apples."
            "I cut them up and put them in a pot with a little water and turned on the stove."
            her surprised "Are you making something else? I thought you liked the beans."
            him determined "I like them, but [kid_name] really wants some applesauce."
            her annoyed "So you're just going to make her some?"
            him surprised "Well, yeah, we don't have any already made, right?"
            her angry "You worked hard to make dinner today! She shouldn't get some special thing just because she's being picky!"
            him annoyed "Well, I'm making applesauce. Maybe in the meantime you can get her to eat the rest of her food."
            her annoyed "Why do I always have to be the bad guy?"
            him "No one's making you."
            her angry "But if I don't, you'll spoil her!"
            "She left the room and I heard her coaxing [kid_name] to try to eat her beans. She was trying to be patient, but she sounded more and more frustrated the longer she tried."
            "Finally the apples were soft and I could mash them up."
            him normal "Here you go, [kid_name]!"
            "She gobbled up the applesauce, but didn't touch her rice or beans."
            her annoyed "That is not a healthy dinner."
            him determined "She won't get malnutrition from eating a bowl of applesauce, right?"
            her annoyed "Eventually, she might. If she doesn't eat anything else."
            him annoyed "You worry too much. She'll be fine."
            $ permissive += 1

        "(Say nothing.)":
            "I didn't really care what she ate. [her_name] could deal with [kid_name] when she got back."
            "I just wanted to eat my dinner in peace. I ate quickly."
            "Just as [her_name] came back, I stood up."
            him determined "Gotta go check on something."
            her annoyed "Right now? We were having family dinner together..."
            him normal "Sorry."
            her surprised "[kid_name], why aren't you eating your beans?!"
            kid angry "Ap'sos!"
            "I just barely escaped in time."
            $ neglectful += 1
        "You can eat it or not, but there won't be more dinner.":
            $ demanding += 1
            $ responsive += 1
            $ confident += 1
            him determined "This is what's for dinner. You can eat it or not."
            kid "Yucky."
            him normal "You don't have to like it. But I think it's pretty good."
            "I closed my eyes and savored the feel of the chunky beans and onions, each individual grain of rice, the melding of starch and protein and amino acids and whatever else is in food."
            "[kid_name] looked at me skeptically."
            him normal "Well, I guess if you're hungry then eventually you'll eat."
            "She slid down off her chair and toddled over to the pantry. She stood on her tiptoes to grab a jar of pickles and brought it to the table."
            kid "Want 'ickles."
            menu:
                "What should I say?"
                "No pickles.":
                    him "No pickles. Eat your rice and beans if you're hungry."
                "You can have some pickles after you eat your dinner.":
                    $ demanding += 1
                    $ responsive += 1
                    him "You can have some pickles after you eat your dinner."
                    "Was this bribery or positive reinforcement? I wasn't sure, and honestly, I was starting to not care. I just wanted dinner to be over."
                    kid "'ickles!"
                    him "After dinner."
                    kid "'ickles!"
                    him "..."
                    kid "..."
                    "I ate my food, pretending not to care about what [kid_name] did. When I was done, I opened the jar of pickles and put three on my plate."
                    him happy "Yay, I finished my dinner, I can eat pickles!"
                    "[kid_name] was not convinced. She reached for the pickle jar, but I pushed it away."
                    him normal "After dinner."

                "Whatever, eat pickles, I don't even care anymore.":
                    $ responsive += 1
                    him annoyed "Whatever, eat pickles! I don't even care anymore."
                    "She ate half the jar of pickles, and nothing else."

                    $ permissive += 1
                    return

            "She scowled at me and left the table. I guess she really hated rice and beans. Hopefully she'd learn to like them, though; we ate them a lot."
            "If she was really hungry, she'd eat anything... right?"
            "I was pretty sure she wasn't starving. I wasn't going to turn dinnertime into a theatrical power struggle."
            "And, sure enough, the next time we had rice and beans she just ate them without complaining."
            "Sometimes I just didn't understand [kid_name]."
            $ authoritative += 1
    return

# 2.7 Earth years old
# Toilet Training
label family5:
    scene black with fade
    "[kid_name] was learning so much every day. She could drink from a cup, sing little songs, run, and jump. She learned several new words every day."
    show baby with fade
    "When I thought back to the tiny helpless creature she was just two years ago, it was hard to even believe this was the same person."
    hide baby with fade
    show kid normal at center with fade
    "Learning some things was harder than others, though."
    hide kid with fade
    "Once she could pull her pants up and down by herself, we taught her how to use the toilet."
    "She understood what it was for, and did pretty well for the first few days."
    "Then we had several days where she hardly ever made it to the toilet on time."
    scene farm_interior with fade
    show him normal at midright
    show her normal at midleft
    with dissolve
    her annoyed "That is the third mess of pee I've cleaned up today!"
    him flirt "Ahh, you're ahead of me, I've only cleaned up two."
    her concerned "At least now she's finally asleep...I thought she was getting this!"
    him concerned "I thought so too..."
    her sad "I can't keep doing this much laundry. Something has to change."
    him flirt "We could keep her in the barn with Lettie!"
    her sad "I'm seriously considering it..."

    menu:
        "What should I say?"
        "We can't give up. We just have to get through this.":
            $ demanding += 1
            him determined "We can't give up. We just have to get through this."
            her annoyed "Okay, then you can do the laundry."
            him determined "I'll do [kid_name]'s laundry if you do the rest."
            her determined "That's a deal."
            him surprised "But maybe we also need a different strategy."
            her surprised "Like what?"
        "Maybe we should give up for now.":
            $ responsive += 1
            him sad "Maybe she's not ready..."
            her surprised "You want to go back to diapers?"
            him determined "It shouldn't be this hard!"
            her concerned "I think she can do it; she seems like she wants to use the toilet. But we need to change our approach."
            him concerned "I guess if she's cooperative we might just need to try something else..."
        "We need a different approach.":
            $ demanding += 1
            $ responsive += 1
            him surprised "Maybe we need a different approach."
            her surprised "Like what?"

    $ family5_punishment = ""
    $ family5_reward = ""
    $ family5_research = False
    $ family5_prepared = False
    $ family5_method = ""
    menu family5_strategy:
        "What should I say?"
        "She should have consequences for accidents." if ((family5_punishment == "") or (family5_punishment == "be spanked")):
            $ demanding += 1
            him determined "I think [kid_name] needs to have some consequences for having an accident."
            her concerned "What kind of consequences?"
            menu:
                "What should I say?"
                "She should help clean up her mess.":
                    him normal "She can help clean up her mess."
                    her annoyed "That'll be more work than if we just cleaned it up ourselves!"
                    him surprised "Yes, but maybe it'll help her learn from it?"
                    her concerned "I guess it might..."
                    $ family5_punishment = "clean up her mess"
                    jump family5_strategy
                "She should go to timeout.":
                    him determined "She should go to timeout for as long as it takes us to clean it up."
                    her annoyed "How are we going to enforce that while we're cleaning up the mess?"
                    him concerned "We'll make it work."
                    her concerned "I guess that might work."
                    $ family5_punishment = "go to timeout"
                    jump family5_strategy
                "She should not be able to use the computer pad.":
                    him determined "She should not be able to use the computer pad."
                    her surprised "How is that relevant?"
                    him concerned "I don't know; it's the only punishment I could think of."
                    $ family5_punishment = "not use the computer pad"
                    jump family5_strategy
                "We should spank her." if (family5_punishment != "be spanked"):
                    him annoyed "We should just spank her whenever she has an accident."
                    her angry "Are you serious?! I don't know much about parenting, but even I know that's a bad idea."
                    him surprised "Why is that?"
                    her determined "There's a famous study about this. When parents spanked their kids for accidents, the kids didn't do any better at using the bathroom -- they did worse!"
                    him surprised "So what does your study say worked with the kids?"
                    her concerned "I don't remember. I just remember spanking was the least effective strategy."
                    $ family5_punishment = "be spanked"
                    jump family5_strategy

        "She should have rewards for success." if (family5_reward == ""):
            $ responsive += 1
            him normal "We need some kind of reward."
            her concerned "What did you have in mind?"
            menu:
                "What reward should I suggest?"
                "A small reward just for sitting on the toilet.":
                    him determined "I think she needs to sit on the toilet more. Maybe we should reward her just for trying."
                    her determined "I thought we were past that stage, but maybe we could do that. It's not like we have tons of candy lying around, though..."
                    him concerned "It doesn't have to be candy... maybe five minutes of her favorite computer pad game? Or a spoonful of applesauce?"
                    her normal "She does love applesauce."
                    him normal "Okay, I'll make up a batch of applesauce."
                    $ family5_reward = "small"
                    jump family5_strategy
                "A big reward if she can stay dry all day.":
                    him determined "I think she should get a big reward if she can stay dry all day."
                    her annoyed "You really think she can do that?"
                    him normal "She did that one day last week!"
                    her normal "That's true...but what kind of reward should she get?"
                    him surprised "What about some new underwear?"
                    her normal "Yeah, she could use some more anyway. I could decorate them with her to make it more fun."
                    him "Maybe I could take her for a ride on Lettie with me sometime, too."
                    her happy "Oh yeah, she loves that!"
                    $ family5_reward = "big"
                    jump family5_strategy
        "We should research this first." if (not family5_research):
            him determined "Actually, I want to do some research first."
            her determined "Good idea. Let's both do some research and talk more in twenty minutes."
            "We snuggled up together on the couch, reading on our computer pads. It was not the most romantic topic, but I was glad we were working together."
            "I read about several scientific studies on toilet training. They all found that punishment was not as effective as rewards, and that praise and encouragement were important, too."
            "But no matter what strategy was used, accidents and regression were pretty normal for kids this age."
            "There were several different strategies people recommended, but they all agreed that parents should be positive and not make the child feel bad for accidents."
            "I shared what I found with [her_name]."
            her normal "I read about some different training methods. One idea is to have the kid drink a lot so she can practice more."
            him surprised "More pee? Is that really what we want?"
            her annoyed "Well, you do that at a time when you can pay attention to her and help her recognize the feeling of having to use the bathroom."
            him determined "Okay, that might help."
            her concerned "Another method recommended having the kid just be outside with no diaper so that if they made a mess it wasn't a big deal."
            him normal "Hmmm, any other methods?"
            her annoyed "Well, another one just said you should wait and let the kid decide when she's ready."
            him concerned "I am so ready to be done with diapers."
            her normal "I know; think how much less laundry we'd have!"
            him surprised "But which ideas should we use?"
            $ family5_research = True
            jump family5_strategy

        "We should be prepared for messes." if (not family5_prepared):
            him concerned "Maybe part of the problem is our attitude. This is a big step for her; we can't expect her to be perfect at it right away."
            her concerned "Maybe you're right..."
            him normal "I mean, think about how long it took her to learn to walk, and how many times she had to fall down."
            her normal "I guess using the toilet seems so easy to us because we don't remember learning it and we do it every day."
            him happy "Exactly! Let's make sure we have a positive attitude and don't get mad at her for making mistakes while she's learning."
            her concerned "Though that's hard to do when it seems like she's making mistakes on purpose..."
            him concerned "Yeah, she's been kind of ornery lately. Asserting her independence, I think they call it."
            her flirt "She's getting more like us every day."
            him surprised "Speak for yourself! I, personally, am the picture of humble cooperation!"
            her surprised "Really? So you'll scrub that mud off the floor like I asked you do to last week?"
            him flirt "Of course! I may be cooperative, but I never claimed to have a great memory."
            her flirt "Oh, I see."
            $ family5_prepared = True
            jump family5_strategy
        "We should train her differently." if ((family5_research) and (family5_method == "")):
            him concerned "I think we should train her differently."
            her surprised "Which method did you have in mind?"
            menu:
                "What should I say?"
                "We should remind her more often.":
                    him concerned "Maybe we just need to remind her more often?"
                    her concerned "I don't know; today I reminded her, but she didn't go, and five minutes later she had an accident."
                    $ family5_method = "remind her"
                "We should be outside as much as possible.":
                    him normal "I think we should be outside and with as few clothes on as possible so that there's less to cleanup. Maybe we can put a pot out there that she can use as a potty?"
                    her concerned "Anything that cuts down on dirty laundry sounds good to me!"
                    $ family5_method = "keep her outside"
                "We should have her drink lots of liquids.":
                    him determined "We should have her drink lots of liquids."
                    her surprised "Maybe we could do that on Saturday, when we're both home?"
                    him normal "Sure, we could take turns being her personal trainer."
                    her concerned "It sounds like a lot of work, but if it pays off it'll be worth it."
                    $ family5_method = "give her lots to drink"
            jump family5_strategy
        "I think that's a good plan.":
            him normal "Okay, sounds like we have a plan."
            scene black with fade
            "And the next day we began our plan."
            if (family5_method == "keep her outside"):
                scene farm_exterior with fade
            else:
                scene farm_interior with fade
            show her normal at midright
            show him normal at midleft
            show kid normal at center
            with dissolve
            if (family5_prepared):
                "We were prepared for her to have lots of messes, and we weren't going to let that bother us."
            if (family5_method == "remind her"):
                "I setup a program on my computer pad to beep every 30 minutes to remind me to remind her to try using the toilet."
            if (family5_method == "keep her outside"):
                "We got ready to spend the day outside. The weather was warm enough that we put [kid_name] in just some underwear, and we brought chairs outside to try to enjoy ourselves."
                "We brought a small bucket for her to use as a potty."
                kid surprised "I putting dirt in potty."
                her concerned "Dirt doesn't go in the potty, [kid_name]. Poop and pee go in the potty."
                him surprised "Here's another bucket. You can put dirt in here."
            if (family5_method == "give her lots to drink"):
                "I made up some fresh tomato juice; one of [kid_name]'s favorites. I gave her several cupfuls."
                him surprised "You sure you don't want more?"
                kid concerned "No. I full now."
                her concerned "Okay, do you remember what happens when you drink a lot?"
                kid "I not thirsty."
                him happy "That's right, but what else happens? What does your body make?"
                "She thought about this for a minute."
                kid laugh "If I not thirsty, I run like this!"
                show kid at right with move
                "She ran as fast as she could out the door and around the yard, pumping her little arms like a marathon runner."
                show kid normal at left with move
                her happy "Good running, [kid_name]!"
                show kid normal at center with move
                kid happy "I run so fast!"
                him happy "Yes, you did. And drinking does give your body energy. But it also makes your body have to pee."
                kid surprised "..."
                her surprised "And where does pee go?"
                "She looked down at her underwear with a familiar look of concentration."
                him surprised "Not here! In the potty, in the potty!"
                "She stopped and we led her to the potty. She had already peed a little in her underwear, but the rest went in the potty, so I decided to count it as a success despite the additional laundry."
                her concerned "I'll go get another pair from the clothesline."
                hide her with moveoutleft
                show her with moveinleft
                "I gave her more juice. She had to pee several times that morning, and it seemed to me that she improved at recognizing her body's signals."
            if (family5_reward == "big"):
                him surprised "If you keep your underwear dry all day, Mommy will get you some new underwear that you can decorate!"
                her flirt "And you can go riding with Daddy on the horse."
                kid happy "I ride on horsie!"
                him normal "Okay, what will you need to do?"
                kid normal "Have dry underwear."
                her surprised "And how will you do that?"
                "She was quiet for a minute. I realized that this concept, while so simple for us, was still fairly new to her."
                him surprised "Where does your pee go?"
                kid normal "In the potty."
                her normal "Right. So you pee in the potty, and your underwear stays dry. Got it?"
                kid "Okay."
            if (family5_reward == "small"):
                him surprised "Every time you sit on the potty, you can have a spoonful of applesauce!"
                kid shifty "I go sit on potty now!"
                "She sat on the potty for a minute, but nothing happened."
                kid happy "I go eat applesauce!"
                her annoyed "Did she actually even try to use it?"
                him determined "I don't know, but we promised she could have some..."
                kid normal "Applesauce!"
                him normal "Alright, here you go."
                kid happy "More applesauce!"
                him determined "You have to sit on the potty first."
                "She went back and forth between the potty and the applesauce a few times before she got tired of it. One of the times she even used it."
                "I realized it worked better if I reminded her about the applesauce when I thought she might actually have to use the bathroom."
                show black with fade
                hide black with fade
                him surprised "[kid_name], time to use the potty. Then you can have applesauce."
                kid "I go sit on potty!"
                "I figured that once she got used to sitting on the potty, we could cut down the reward to every time she actually used it."
            scene black with fade
            "I don't know if it was our new methods, or our heightened attention, or what, but she didn't have any other problems that day."
            "The next day, though, she had an accident."
            scene farm_interior with fade
            show him normal at midleft
            show kid normal at midright
            with dissolve
            if (family5_prepared or family5_research):
                him concerned "Uh-oh, you made a mess."
                kid sad "Uh-oh."
                him determined "Remember, pee goes in the potty. Go sit on the potty."
            else:
                him angry "[kid_name]! You peed on the floor!"
                kid sad "Uh-oh"
                him annoyed "Pee goes in the potty. Go sit on the potty."
            "While she sat on the potty, I got her some clean clothes and helped her wash off."
            kid normal "I not have any pee."
            if (family5_punishment == "clean up her mess"):
                him determined "Okay, next let's clean it up. First we get a bucket of water."
                kid happy "I get bucket!"
                him normal "Good! I'll get a rag."
                "Water from her small bucket sloshed all over the floor, so we had to wipe that up along with the floor."
                "I showed her how to put her dirty clothes in the washtub."
                "[her_name] was right; it was more work than just cleaning it up myself. But [kid_name] was willing to help, and it actually felt less annoying than doing it all by myself and feeling resentful."
                "Hopefully it helped her, too."
                him surprised "Next time you have a pee feeling, where do you need to go?"
                kid normal "I go potty."
                him determined "Right."
            if (family5_punishment == "go to timeout"):
                him determined "Okay, now you have to go to timeout while I clean it up."
                kid angry "No!!!"
                "We spent thirty minutes of her popping out of timeout and me putting her back in while also trying to clean up the mess."
                "I felt so frustrated at the end, I was ready to call the whole thing off."
                "Good thing it was the weekend, and I could take turns with [her_name]."
            if (family5_punishment == "not use the computer pad"):
                him determined "Now you can't use the computer pad until you pee in the potty."
                kid angry "No!"
                him annoyed "Pee goes in the potty, [kid_name]. Use the potty, and you can use the computer pad again."
                show kid yell with dissolve
                "She threw a huge tantrum, screaming and crying to use the computer pad. It took all my patience to remain calm, but somehow I did it until she calmed down thirty minutes later."
                show kid cry with dissolve
                "Good thing it was the weekend, and I could take turns with [her_name]."
            if (family5_method == "keep her outside"):
                "We decided to spend the day outside again, so that made subsequent messes easier to cleanup."

    scene black with fade
    "Toilet training was definitely not my favorite part of parenting so far, but I couldn't see any way around it. It was just something everyone had to learn to do."
    if (family5_prepared):
        "It helped that [her_name] and I decided to expect messes. They were still annoying, but they didn't make me quite so mad."
    "There were plenty more accidents, but over the next few months, [kid_name] slowly caught on."
    call bedroom_scene(False, False)
    her concerned "I think I can finally say [kid_name] is potty trained."
    him flirt "Don't say it out loud! You might jinx it!"
    her sad "In some ways, that was the hardest part of parenting yet."
    him surprised "Harder than all those sleepless nights when she was a baby?"
    her concerned "I don't know. Maybe it's just whatever thing you're doing at the moment that seems the hardest."
    him normal "Well, it was hard, but we did it! All three of us. And now we don't have to worry about our little [kid_name] heading off to college without being potty trained."
    her surprised "College?! I was just thinking about kindergarten!"
    him surprised "That's not that far off, is it?"
    her concerned "No..."
    him concerned "..."
    her normal "Hey, thanks for doing this parenting thing with me."
    him flirt "There's no one else I'd rather potty-train a two-year-old with!"
    her flirt "There better not be!"
    him normal "Just you. Always you."
    her sleeping "Mmmm...I love you, [his_name]."
    him sleeping "I love you..."

    if ((family5_punishment == "not use the computer pad") or (family5_punishment == "go to timeout") or (family5_punishment == "be spanked")):
        $ authoritarian += 1
    elif ((family5_method != "") and (family5_punishment == "clean up her mess")):
        $ authoritative += 1
        $ confident += 1
    elif ((family5_punishment == "") or (family5_reward != "")):
        $ permissive += 1
    else:
        $ neglectful += 1

    return

# 3.5 Earth years old
# Incessant questions
label family6:
    scene black with fade
    "I remember when [kid_name] was so small and crying incosolably; I couldn't wait for her to learn to talk."
    "Now she was like a perpetual motion machine of questions and opinions."

    scene farm_interior with fade
    show him normal at midleft
    show her normal at center
    show kid normal at right
    with dissolve
    him determined "I sure hope you have nothing planned for today."
    her surprised "Why, did you want to do something?"
    him normal "Nope! I want to do a whole lot of nothing today. It's been a crazy week."
    her concerned "Yeah, harvest time is always like that, isn't it?"
    him happy "But now I'm done! Just for this morning, I want to relax..."
    her happy "A relaxing weekend... sounds nice."
    him surprised "You don't have any appointments today?"
    her normal "No, after this crazy week I moved them all to next week. So unless someone gets injured I've got the whole weekend at home."
    him normal "One of us needs to help can food this afternoon at the storehouse."
    her "But not right now."
    "We sat next to each other, her head on my shoulder, just enjoying the peace and quiet and being together."
    show him sleeping
    show her sleeping
    with dissolve
    show kid normal at midright with move
    kid normal "Dad."
    him "..."
    show kid normal at quarterleft with move
    kid annoyed "Dad!"
    him "...Yeah?"
    kid angry "Listen to me!"
    him "I'm listening."
    kid annoyed "You can't be listening. You're sleeping. Wake up, daddy, wake up!"
    him "I'm awake, I'm just closing my eyes."
    show kid normal at midright with move
    kid angry "Wake up and listen!"
    him determined "All right, I'm listening. What?!"
    kid normal "What are we doing today? I want to go see grandma."
    him surprised "Grandma? Your grandparents all live on Earth..."
    her normal "That's Sister Naomi. She said the kids could call her grandma."
    her concerned "But she's probably busy today, [kid_name]. We're just going to stay at home and relax this morning."
    kid concerned "Why?"
    her normal "Daddy and I are a little tired. It's been a busy week!"
    kid annoyed "Why so busy?"
    her determined "It's harvest time, which means daddy has a lot to do, and people are more likely to get hurt because they push themselves too hard."
    kid surprised "Why?"
    her surprised "That's a good question! Why is that, [his_name]? Why are people so foolish and don't know their own limits?"
    him annoyed "I don't know what you're talking about."
    her flirt "Oh, so you don't need this painkiller prescription, then?"
    him determined "I didn't say that!"
    kid normal "Why you taking medicine, daddy?"
    him normal "Because I had to lift heavy things all week and my back's killing me."
    kid sad "Daddy, are you going to die?"
    him surprised "What? No, no! It just hurts a lot."
    kid happy "OK, good, because I wanna go swimming!"
    her sleeping "What do you think, [his_name]?"
    menu:
        "What should I say?"
        "Don't make me decide.":
            him angry "Don't put this all on me! You decide what to do; I'm just going to lie right here."
            her annoyed "So you don't want to do anything together."
            him annoyed "We're together right now, aren't we?"
            her determined "Not really."
            him determined "I'm not going anywhere."
            her annoyed "Fine. [kid_name], I'll take you swimming. Seems like daddy needs a little 'me time' so he can get back to his usual jolly self."
            hide her
            hide kid
            with moveoutleft
            "They left, but I couldn't relax even though the house was finally quiet."
            "I deserved a little time to myself now and then, right?!"
            $ neglectful += 1

        "[kid_name] can play on the computer pad so we can relax.":
            $ responsive += 1
            $ confident += 1
            him surprised "Here, [kid_name], why don't you play Bubble Bee while mom and dad chill out?"
            her annoyed "Really? We're going to spend our relaxing morning listening to that stupid game?"
            him annoyed "You wanted me to decide, so I decided."
            kid laugh "Bubble Bee!"
            "I turned the volume down low and [her_name] and I lay dozing on the couch together."
            "We even had time to play a round of the video game we liked to play together."
            her happy "It's been too long since we did something like this together!"
            him flirt "Yeah, we've gotten pretty bad at this game."
            her flirt "Good thing we've gotten better at some other things."
            him surprised "We have?"
            her normal "Yeah, like... cooking. I love your cooking."
            him normal "I've always been good at cooking."
            her flirt "That's what I thought, but however good you were before, you're even better now."
            him concerned "I should cook more often."
            her concerned "Yes, you should. Maybe tonight?"
            him surprised "I thought you were making...wait, are we talking about actual cooking, or, you know, 'cooking'?"
            her flirt "Both!"
            him flirt "Then let's cook together tonight, [her_nickname]!"

            $ marriage_strength += 1
            $ permissive += 1

        "Let's go swimming.":
            $ responsive += 1
            him normal "It is a nice day out; let's go swimming!"
            her concerned "But the water's so cold, and it's so stressful taking her there because we always have to be watching her so closely. She thinks she can swim, you know."
            him happy "She'll learn to swim faster with practice! C'mon, [kid_name], grab a towel!"
            her determined "I guess if we're going together..."
            menu:
                "You can stay here if you want.":
                    $ marriage_strength += 1
                    him surprised "Why don't you stay here and rest? I know you've had a tough week."
                    her surprised "Are you sure?"
                    him normal "Yeah! [kid_name] and I will have fun!"
                    her sad "Oh, thank you, [his_name]. I didn't know how to say it, but I'm just so exhausted."
                    "I was too, but not so exhausted I couldn't go swimming."
                    "Besides, it felt good to help out [her_name]."

                "Come on; it'll be fun!":
                    him happy "Come on, it'll be fun!"
                    her concerned "I suppose..."

            call family6_swimming
            $ permissive += 1

        "Let me think about it.":
            him concerned "Let me think about it for a minute."
            "I had really been looking forward to just lazing around, but I knew that was not what [kid_name] wanted to do."
            kid concerned "Are you done thinking yet, daddy?"
            him surprised "Maybe we can do both somehow?"
            her concerned "We only have a few hours... what did you have in mind?"
            menu:
                "Let's relax for an hour and then go swimming.":
                    $ responsive += 1
                    $ demanding += 1
                    $ confident += 1
                    him normal "[kid_name], we're going to relax here for one hour. Here, I'll set a timer so you can see."
                    kid angry "One hour?!"
                    him determined "Yes, you need to find something to do for one hour while mom and dad take a break. Then we'll all go swimming!"
                    her happy "Maybe you can take your animals swimming in the sink until it's time to go?"
                    show kid normal with dissolve
                    "I waited for her to throw a fit or refuse, but I guess she liked the idea of her little toy animals going swimming, because she ran off to get them."
                    hide kid with moveoutleft
                    him concerned "You know she's going to make a big mess over there, right?"
                    her normal "I am not even thinking about that right now. I'm thinking about how lovely it is to be snuggled up to you right here, right now."
                    him flirt "Mmmm, this is pretty nice..."
                    her determined "And it's just water, so don't worry."
                    him concerned "She's getting out the soap..."
                    her surprised "Then it's just soap and water... right?"
                    him normal "Right. How much of a mess can she make in an hour?"
                    "It turned out she could make quite a large mess of soap suds and water in fifteen minutes, but we all pitched in with towels and then hung them out and headed to the swimming hole together."
                    "We'd have to airdry after swimming, because we used every towel in the house cleaning her mess. But we managed."
                    call family6_swimming

                    $ authoritative += 1
                "Let's relax together.":
                    him happy "Why don't we watch a movie together or something?"
                    her concerned "I guess we could do that."
                    "It took us half an hour to find a movie that we thought we would all enjoy."
                    "[kid_name] settled in on my lap for the first part of the animated comedy. [her_name] and I laughed at the situational irony and witty comebacks, while [kid_name] mainly laughed at the silly faces and fart jokes."
                    "[kid_name] kept interrupting the movie with questions, and I wasn't sure whether I should teach her to be quiet during movies, or if I should answer her questions."
                    kid surprised "Why is the mommy mad?"
                    menu:
                        "What should I do?"
                        "Tell her to be quiet.":
                            him determined "Shhh, just watch."
                            kid annoyed "Maybe the mommy is just mean."
                            him annoyed "Shhhh!"
                            kid concerned "..."
                        "Give a quick explanation.":
                            $ responsive += 1
                            him normal "The kid was supposed to take out the trash, not play with the trash."
                            kid sad "But why doesn't she like the robot?"
                            him determined "Shhhh, we'll talk about it more later."
                            kid annoyed "Maybe she's just mean."
                            him annoyed "..."
                        "Pause the movie and talk about what happened.":
                            $ responsive += 1
                            $ demanding += 1
                            him normal "The kid was supposed to take out the trash, not play with the trash."
                            kid sad "But why doesn't she like the robot?"
                            him determined "Because the kid was building a robot when he was supposed to be doing chores. Like if we asked you to pick up your toys, and you built a big tower instead."
                            kid normal "I like big towers!"
                            him normal "I do, too, but it's more important to obey your mom and dad."
                            kid annoyed "No, it's not."
                            her surprised "Why don't we just continue the movie?"

                    $ authoritative += 1

        "No way. We're sitting right here while [kid_name] plays quietly.":
            $ demanding += 1
            him determined "No. Mom and dad are relaxing, and you, [kid_name] are going to go play quietly."
            kid angry "I want to go swimming!"
            him annoyed "You decided not to play quietly. Now go to your room."
            kid yell "No! I'm going swimming!"
            show kid yell at left with move
            "She ran for the front door. Part of me wondered how far she'd get if I just let her go, but another part of me knew I couldn't try it."
            show him at left behind kid with move
            "I caught her up and carried her to her room."
            show him at right
            show kid angry at right
            with move
            "As soon as I let her go, she threw herself against the door and tried to run back out."
            hide kid with moveoutright
            "So I locked her in."
            "We had installed a latch up high on the outside so that she would stay in her own room at night."
            "Sometimes, we just needed to be separate for a while to calm down. I knew she'd be safe in there."
            her concerned "..."
            him determined "..."
            "But it was kind of hard to relax when she was banging on the door and yelling at the top of her lungs."
            $ authoritarian += 1


    # TODO: change this to parenting class?
    scene black with fade
    "Later that night, after [kid_name] went to bed, [her_name] and I took a walk together."
    scene fields with fade
    show him normal at midright
    show her normal at center
    with moveinright
    #show overlay night
    him surprised "That's something I can't figure out -- how can I tell when doing things with [kid_name] is being a loving parent, and when I'm just spoiling her?"
    her concerned "I know what you mean... I guess it depends on your motivation."
    him determined "Should that matter?"
    her determined "Well, yeah... if you're just doing what [kid_name] wants because you're afraid she'll throw a fit, or you just want to do the easiest thing, then that's going to teach her the wrong thing."
    her normal "But if you think about it and decide that doing something with [kid_name] is what's best for the family, then I think it's the right thing to do."
    him concerned "Yeah... but it's not always that simple."
    her determined "No matter what, though, we need to do everything with love. I want her to always feel loved and accepted at home. When she has troubles, I want us to be the ones she trusts to listen and help with compassion."
    him normal "I can't imagine her growing up... it feels like she's been little forever."
    her normal "Yeah... I can hardly remember what life was like before we had [kid_name]... what did we even do all day?"
    him happy "Whatever we wanted!"
    her concerned "Yeah... but it was kind of empty, wasn't it? Incomplete?"
    him concerned "I don't know; do you feel that way?"
    her determined "A little. In fact, I kind of..."
    him surprised "What?"
    her surprised "Should we have another kid? I worry [kid_name] will be too spoiled by herself, and it will be nice to have someone here for her to play with."
    him concerned "I don't know... those baby years were rough. It's still rough!"
    her determined "I feel like I'm ready for it... if you are."

    menu:
        "What should I say?"
        "No way!":
            him annoyed "No way!"
            her surprised "Are you sure?"
            him determined "Yeah, I'm sure! It's crazy enough with one kid, there's no way I could handle two!"
            her concerned "Oh."
            him concerned "..."
            her sad "Like... never?"
            him sad "I don't know. Not now, that's for sure."
            her determined "Well, think about it. I would like to have at least one more kid sometime. And I think sooner is better than later."
            $ year6_have_baby = False
        "It would be efficient":
            him surprised "It's probably more efficient to have them closer together."
            her normal "Yeah, if we wait too long they won't really want to play together."
            him normal "And we'll forget all the tricks we learned!"
            $ year6_have_baby = True
        "If you're ready.":
            him surprised "We can if you want to -- you're the one that has to host them for nine months."
            $ year6_have_baby = True
        "Sure! Anytime!":
            him happy "Yeah! I love kids!"
            her happy "Oh, good! I'm so glad we feel the same way!"
            $ year6_have_baby = True
        "I'm not ready yet.":
            him concerned "I... I don't think I'm ready yet. I'm sorry, [her_name]. I just feel like one kid is already more than I can handle right now."
            her concerned "It's okay. I'm the one that gets pregnant, but I can't have another baby by myself... I need you to be ready, too."
            $ year6_have_baby = False


    if (year6_have_baby):
        "That's what we said, but [her_name] didn't get pregnant right away."

    return

# Helped function for event 6 if they go swimming
label family6_swimming:
    scene pond with fade
    # TODO: CG or interesting movement/sprites here?
    #scene stream with fade
    show him normal at midleft
    show kid normal at midright
    with dissolve
    "It was pretty fun to swim with [kid_name]; she tried to hard to swim but she kept doggy paddling instead."
    him "Big arms! Big arms!"
    kid surprised "My arms are big! So big!"
    him "Scoop the water! Come on!"
    kid happy "I scooping, I scooping!"
    "After an hour or so we lay in the sun to warm up, and then we went home."
    return


#####################################################
#
# SMALL CHILD
#
#####################################################

# 4 Earth years old
# Back-Talking
label family7:

    "I'd been working on a surprise for [kid_name] for several weeks. It was her fourth birthday (by the Earth calendar) and she was old enough that I thought she might actually appreciate what I'd made."

    scene farm_interior with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center
    with dissolve
    "[his_name] and [her_name]" "♫ ~ Happy Birthday to you! ~ ♫" # TODO: Use a different, unicode font for the musical notes so that they will show up.
    him happy "Make a wish!"
    "We didn't have a traditional birthday cake, but [her_name] had made some sweetbread and spread some precious melted chocolate on the top."
    "[kid_name] blew out the candle and we settled down to eat our treat."
    kid concerned "Blech, what's this brown stuff on top?"
    her flirt "It's called chocolate, and if you don't want it, daddy and I will fight over it."
    kid annoyed "It's kind of gross."
    "She wiped it off her sweetbread and onto her plate. [her_name] and I both looked at the chocolate, then at each other."
    show kid shifty with dissolve
    him concerned "Go ahead; you should take it. I know how much you like chocolate."
    her concerned "No, you should have it. You like it just as much."
    him determined "...Let's split it."
    "She took half and I took half. Ohhhh, chocolate. It'd been months since I last tasted any..."
    her surprised "Could you grow cocoa beans?"
    him concerned "I think it's too cold here. Plus, we don't have sugar crops to go with them."
    her determined "That's what this planet needs more of: sugar, chocolate, and coffee!"
    him surprised "You could grow them closer to the equator..."
    kid nervous "Did you get me anything for my birthday?"
    her surprised "[kid_name]! That's not polite to ask!"
    him happy "But, yes, I made you something."
    kid laugh "Yay, I love presents!"
    "I had put the present in an old wheat can and wrapped it in the prettiest towel we had. She wasn't disappointed about that, though -- she didn't even know what wrapping paper was."
    "Inside was doll-sized furniture that I had woven out of supple sticks -- two beds, a table and chairs, and a cradle."
    "I even made some blankets out of one of my old socks."
    "She didn't have a dollhouse, but she often made one out of blocks and pretended her toy animals were people."
    kid sad "I don't think this bed will fit me."
    him normal "It's for your little animals."
    kid concerned "But animals don't sleep in beds."
    him surprised "Don't you sometimes pretend they are people?"
    kid shifty "No, they are animals that can talk like people. But they are still animals."
    her concerned "Just say 'thank you', [kid_name]"
    kid normal "Thank you, daddy."
    her normal "Good, now open this one."
    "[her_name] had made a little doll family out of cotton balls and first aid tape. A mom, a dad, a girl, and a little baby. She had drawn cute faces on the tape."
    kid surprised "Oh! Is this me?"
    her happy "Yes, and mommy and daddy, too."
    "[kid_name] pointed to the baby."
    kid concerned "Who's this?"
    her normal "A baby."
    kid surprised "But we don't have a baby."
    her flirt "We might someday."
    him happy "He goes in the cradle, like this."
    "We played dollhouse together for awhile, until it started to get late."
    him normal "Now it's time to put everything away, okay?"
    kid annoyed "No. I'm not done."
    her concerned "Come on, [kid_name], it's bedtime."
    "I reached for the toy in her hand but she twisted away."
    kid angry "No! Go away!"
    show him annoyed with dissolve
    menu:
        "What should I do?"
        "Don't let her talk to you like that.":
            $ demanding += 1
            him angry "You do NOT talk to your parents like that!"
            kid yell "You don't talk to me like that!"
            "The way her eyes sparked with rebellion lit my anger like a barrel of gunpowder."
            menu family7_anger_menu:
                "What should I do?"
                "Yell at her.":
                    him annoyed "You are not the boss around here! Show some respect"
                    kid annoyed "You are not the boss of me!"
                    him angry "Oh yes I am!"
                    call family7_angry_ending
                "Spank her.":
                    "I had to show her. I had to make her realize that she was a tiny powerless child and she had to obey me!"
                    "I grabbed her and put her face down on my lap."
                    kid angry "No, no, daddy, no, don't spank me! I'll clean up! Stop! Just stop!"
                    her surprised "[his_name]!"
                    show kid cry with dissolve
                    him "You are"
                    "(whack)"
                    him "NOT the"
                    "(whack)"
                    him "boss!"
                    "(whack)"
                    call family7_angry_ending
                "Guilt trip her.":
                    him determined "Your mother and I worked hard to make your birthday awesome. And you won't even clean up your toys?!"
                    kid annoyed "No. I'm still playing."
                    "I wasn't getting through to her. I felt like I had to make her understand!"
                    him angry "You are not the boss! You do what your parents say, not the other way around!"
                    call family7_angry_ending
                "Take a deep breath.":
                    "I tried to breathe deeply and calm down. If I did something while I was angry, it might be something I'd regret."
                    "But that sick desire to prove I was the boss, to make her afraid of me, to force her to obey, was still there."
                    menu:
                        "What should I do?"
                        "Ask [her_name] for help.":
                            him concerned "[her_name], can you handle this? I just...can't, right now."
                            her determined "Good idea."
                            kid concerned "Yeah, good idea."
                            "I walked out of the house before I could explode. I didn't want to be a yelling-spanking-angry dad, but I didn't know how else to handle [kid_name] when she got this way."
                        "Walk away.":
                            "I walked out of the house before I could explode. I didn't want to be a yelling-spanking-angry dad, but I didn't know how else to handle [kid_name] when she got this way."
                        "Talk to [kid_name].":
                            him annoyed "You're being really rude. That's not how you talk to adults."
                            kid concerned "Yes it is!"
                            him angry "You are not the boss!"
                            call family7_angry_ending
            $ authoritarian += 1
        "Try to convince her.":
            $ responsive += 1
            him annoyed "Stop it, [kid_name]. We have to put the toys away or we might step on them and break them."
            kid angry "No! You're mean!"
            "I wasn't making very much progress... I needed to try something else."
            $ family7_logic = False
            menu family7_cleanup_convince_menu:
                "What should I do?"
                "Convince her with logic." if (not family7_logic):
                    him normal "If you like having toys, then you're responsible for taking care of those toys. Part of taking care of toys is putting them away."
                    kid yell "No! I'm still playing!"
                    him determined "Look at the clock. You can see it's bedtime."
                    kid annoyed "I'm not tired!"
                    "This wasn't working."
                    $ family7_logic = True
                    jump family7_cleanup_convince_menu

                "Bribe her.":
                    him normal "If you put your toys away now, I'll read you a story!"
                    kid concerned "Two stories!"
                    menu:
                        "What should I say?"
                        "One story. Come on, let's clean up!":
                            $ demanding += 1
                            him "One story. Come on, let's clean up together!"
                        "Sure, two stories.":
                            him determined "Okay, fine, two stories."
                            kid shifty "How about three stories?"
                            him annoyed "How about we clean up right now or we won't have time for any stories?"
                    "I put a piece of furniture in the box and waited."
                    "She put one in, too."
                    "[her_name] helped, and together we cleaned up the mess."
                    $ permissive += 1
                    call family7_bedtime
                "Set consequences.":
                    $ demanding += 1
                    him angry "You clean these up right now or...."
                    menu:
                        "What should I say?"
                        "...or I'll throw them away!":
                            him angry "You clean these up right now or I'll throw them all away!"
                            kid sad "No! Don't throw away my toys!"
                            him annoyed "Then clean them up!"
                            kid angry "No!"
                            "She's not cleaning them up..."
                            menu:
                                "What should I do?"
                                "Throw the toys away.":
                                    "I had spent hours making those stupid pieces of tiny furniture. Could I really throw them all away?"
                                    "Did I have a choice? I said that I would, so that's what I was going to do."
                                    "I gathered them up in the box and marched out the door."
                                    her concerned "[his_name]?!"
                                    kid sad "Daddy?!"
                                    her angry "You can't just throw those away! I worked hard on them!"
                                    kid cry "No!!!"
                                    him annoyed "We have to be consistent! If I said I would do something, then I'll do it!"
                                    her annoyed "That would be wasteful. Let me put them away and we can think about it later when we're not so upset."
                                    "The way she said 'we' left no doubt that she meant me."
                                    him angry "Fine. But don't give them back to her until we talk about it together."
                                    "I didn't even think about whether [her_name] was willing to carry out my threat or not. We were in this together; we had to be unified."
                                    "But I probably shouldn't have made such a drastic threat in the first place."
                                    "I couldn't just let [kid_name] get away with stuff, either."
                                    "Sometimes, I just didn't know what to do."
                                    # TODO: Do we need a "trust" variable that keeps track of whether the parents keep their word?
                                "Put them away.":
                                    "I wasn't going to throw away something I had worked so hard on. I gathered up all the toys in the box and hid them away. Maybe I'd get them out when she'd forgotten about it."
                                    call family7_bedtime
                                "Give her another chance.":
                                    "I picked up the box and started putting pieces into it in slow motion."
                                    kid cry "No, stop, daddy, I'll clean up!"
                                    "She helped put all the pieces away so fast we were done in under a minute. I couldn't believe she had thrown a fit about such a simple thing."
                                    call family7_she_cleaned_up
                            $ authoritarian += 1
                        "...or you won't be able to play with them tomorrow.":
                            him determined "Clean these up now or you won't be able to play with them tomorrow."
                            kid concerned "No!"
                            "She's not cleaning them up..."
                            "I put the pieces in the box and hid them away."
                            kid angry "Give me my toys!"
                            him annoyed "No!"
                            show him determined with dissolve
                            extend " I mean, you decided not to clean them up, so now you may not play with them."
                            kid annoyed "You're mean!"
                            him annoyed "You decided not to clean up; that's what happens."
                            her normal "Anyway, now it's bedtime! As soon as you brush your teeth, I'll read you a story."
                            $ authoritative += 1
                            call family7_bedtime
                        "...or you'll get a spanking!":
                            him annoyed "You clean these up right now or you'll get a spanking!"
                            her concerned "[his_name]..."
                            "[kid_name] looked at me, as if trying to gauge how serious I was."
                            "I put on my meanest face. It wasn't hard; I felt like a rattlesnake, shaking my warning rattle, daring her to make one wrong step..."
                            "She folded her arms and looked up at me defiantly."
                            kid angry "No."
                            "Now I had to decide if I was bluffing or not. Was it really worth making such a threat over cleaning up toys?"
                            "But it wasn't just about cleaning up toys; it was about her challenging my authority and teaching her that she really did have to do what mom and dad said."
                            "I didn't know any other way to show her that."
                            show him angry with dissolve
                            "So I spanked her."
                            show her concerned
                            show kid cry
                            with dissolve
                            "She cried."
                            $ responsive -= 2
                            show him annoyed with dissolve
                            "[her_name] put her to bed, glaring at me whenever I tried to help."
                            show him concerned with dissolve
                            "Finally I gave up trying to help and just sat down on the couch and tried to catch up on my email."
                            her annoyed "Really? Spanking? That's the best you could do?"
                            him annoyed "I didn't see you jumping in with any bright ideas!"
                            her angry "I didn't think you were serious!"
                            him angry "There's no point in making a threat if you're not willing to carry it out!"
                            her concerned "Then maybe you shouldn't make threats like that."
                            him annoyed "Fine. Next time you can handle it; show me what a 'good' parent does."
                            her annoyed "Fine. I will."
                            $ authoritarian += 1

        "Don't make her clean up.":
            $ responsive += 1
            him surprised "Okay, if it means that much to you I guess you can leave them out."
            her determined "It is time for bed, though. Come on, [kid_name]."
            kid yell "I'm not going to bed! I'm not tired!"
            "The last thing I wanted was to get stuck arguing with a four year old for hours."
            him sad "I, uh, I need to go check on the goats."
            "I fled out the front door just as the wailing started."
            "I felt a twinge of guilt, but shoved it aside. [her_name] was much better at this sort of thing; I'd just be in the way."
            $ permissive += 1

        "Take a deep breath.":
            "I took a deep  breath. I don't know why she was so upset all of a sudden, but me yelling at her wouldn't help the situation any."
            "I realized I had some other options."
            menu:
                "What should I say?"
                "Why are you so mad?":
                    him surprised "Why are you so mad?"
                    kid yell "You won't let me play with my toys!"
                    him normal "You can play with them more tomorrow. But right now we need to clean them up because it's bedtime."
                    kid angry "I'm not tired!"
                    jump family7_patience_menu
                "Clean this up or you won't be able to play with them tomorrow.":
                    him determined "You need to clean these up or you won't be able to play with your new toys tomorrow."
                    kid yell "No! I'm not done playing!"
                    jump family7_patience_menu
                "You wish you could play more.":
                    him concerned "You wish you could play with your toys more."
                    kid concerned "Yeah! I'm having too much fun."
                    "I gave her a hug and stroked her hair."
                    him normal "It has been fun to play together. I hope we can play more tomorrow."
                    kid angry "I'm not tired!"
                    menu family7_patience_menu:
                        "What should I say?"
                        "Too bad! It's time for bed!":
                            him angry "Too bad! It's time to clean up and go to bed!"
                            kid yell "No! You can't make me!"
                            "Some part of me took that as a challenge. I {b}would{/b} make her clean up and go to bed!"
                            jump family7_anger_menu

                        "You may not feel tired, but it's bedtime.":
                            him surprised "You probably don't feel tired right now, huh?"
                            kid shifty "Nope!"
                            him normal "But it's bedtime, so we're going to clean up. As soon as all the toys are in the box, we will read a story."
                            kid annoyed "I don't want a story! I want to play!"
                            menu:
                                "What should I do?"
                                "Set a consequence and a time limit.":
                                    him determined "I know you wish you could play, but it's time to clean up. If you decide not to clean up, you will not be able to play with these toys tomorrow. You have five minutes."
                                    show kid annoyed at right
                                    show him at left
                                    with move
                                    "I left the room and started a timer on my computer pad. I did some deep breathing."
                                    show him concerned with dissolve
                                    "I had kept my cool so far, but, man, this kid really knew how to rile me up."
                                    "I had to remind myself that she wasn't doing it on purpose; she was just testing her limits. This was a totally normal four-year-old thing to do."
                                    "I just had to stay calm and be clear and firm."
                                    show him sad with dissolve
                                    "...Why was that so hard?!"
                                    show her at quarterleft with move
                                    "[her_name] followed me and gave my shoulders a squeeze."
                                    her surprised "You are being so patient with her!"
                                    him annoyed "Maybe too patient. Why is she acting so bratty, anyway?"
                                    her concerned "She might just be tired. She woke up pretty early this morning."
                                    "I heard clanking coming from the other room. Peeking around the corner, I saw that she had started putting the toys in the box."
                                    call family7_she_cleaned_up
                                    $ authoritative += 1
                                    call family7_bedtime
                                "Give up.":
                                    jump family7_give_up
                                "Demand she clean up now.":
                                    him angry "You clean these up right now!"
                                    kid yell "No!"
                                    jump family7_anger_menu
                        "Fine; don't go to bed. I'm done.":
                            label family7_give_up:
                                $ responsive -= 1
                                him angry "Fine! Don't go to bed and don't clean up! Grow up to be a lazy moron for all I care!"
                                "I left the house in a flash of anger."
                                hide him with moveoutleft
                                "I just didn't have enough patience. Or maybe I was doing this all wrong."
                                "Or maybe [kid_name] was just a bratty kid."
                                "Either way, I couldn't take it anymore."
                                $ neglectful += 1

                "Make cleaning up a game.":
                    $ responsive += 1
                    $ demanding += 1
                    him surprised "Uh-oh! Do you hear that?!"
                    kid concerned "Hear what?"
                    him normal "It's the [kid_name] Crane! It's here to cleanup the toys for us!"
                    kid shifty "Where?"
                    show him at center with move
                    show kid surprised at upside_down
                    "I grabbed her by the ankles so she dangled upside down." # TODO: add animation here
                    show kid surprised at up_and_down
                    him happy "Right here! Look at those powerful hands!"
                    "She hesitated. I think she could sense it was kind of a trick."
                    him normal "I wonder how many toys the crane can hold at one time?!"
                    "She grabbed a handful of toys, spreading her fingers wide to catch as many as she could."
                    kid "This many!"
                    him "Wow! That's so many! Now the crane drops them in the box!"
                    show him at quarterright
                    show kid at quarterright, up_and_down
                    with move
                    "I maneuvered her over the box and she let go of the toys and squealed with delight."

                    kid "Again!"
                    show him at center
                    show kid at center, up_and_down
                    with move
                    "I repeated the process several times. [her_name] took pity on me and helped cleanup a few stragglers."
                    "I helped [kid_name] down."
                    hide kid
                    show kid normal at center
                    kid happy "That was fun, daddy! [kid_name] Crane should come every night!"
                    "Uh-oh... what had I started?!"
                    her flirt "And now it's time for bed!"
                    hide her with moveoutleft
                    $ authoritative += 1
                    call family7_bedtime

    if (year6_have_baby):
        scene black with fade
        "The next day, we found out [her_name] was pregnant."
        "I felt overwhelmed. I could barely function as a dad of one kid, much less two!"
        "Sometimes, I was amazed that humanity had ever managed to survive past childhood."
        "There was no choice but to keep trying. Maybe in nine months I'd be a better dad than I was now?"
        "I had the feeling it would take more than the passage of time to make a better parent out of me."
    else:
        scene black with fade

    "I wanted to be a better parent."
    "But I had so much on my plate already -- serving as community liaison, farming, and taking care of everyday life."
    "Did I really have time for one more thing?"
    menu:
        "What should I do?"
        "Take a parenting class":
            "I asked around to see if anyone was willing to teach a parenting class."
            "Sister Naomi thought that was a great idea. Soon me and a few other moms and dads were gathered at the community center. There were even some parents that I thought already knew everything."
            call parenting_class1
        "Do some reading":
            "I tried to read some parenting books, but they all seemed to conflict with each other."
            "One book said to love your kids no matter what; another said to make sure not to spoil your child by doing whatever they said. One said to never let a baby cry; another said that it's okay for babies to cry sometimes."
            "The few things they agreed on were things I already knew: being a parent is hard, and kids need parents."
        "Do nothing":
            "I didn't have time for this. And, really, our ancestors didn't have time to read parenting books and humans turned out okay, so why should I have to turn it into some huge complicated thing?"
        "Discuss it with [her_name]":
            "I decided to talk to [her_name] about it. We were both [kid_name]'s parents, after all!"
            scene bedroom with fade
            show him sleeping at midleft, squatting
            show her sleeping at midright, squatting
            show bedroom_overlay
            show night_overlay
            with dissolve

            him determined "Hey, [her_name]?"
            her surprised "What?"
            him surprised "Do you think we should be doing something differently? As parents, I mean?"
            her concerned "Maybe...I don't have any experience here, so it's hard to know if we're doing the right thing."
            him concerned "Yeah...  I wish I could talk to my parents about it."
            her flirt "I have the feeling that 140 characters isn't going to be enough space for much useful parenting advice."
            him "Well, there's some good parents here, right?"
            her determined "Yeah... maybe? I've never really thought about the other adults as parents, mostly just as people."
            him "Sister Naomi seems like she would be a good mom. I mean, I guess she was. Or is. Well, now she's a grandma or maybe even a great-grandma but everyone's back on Earth."
            her normal "Yeah, I'll ask her!"
            scene black with fade
            "After [her_name] talked to her, Sister Naomi agreed to host a parenting workshop one night a week. Her husband, Mayor Grayson, offered to watch the kids so anyone who wanted to could attend."
            call parenting_class1
    return

label family7_bedtime:
    "I read her a story and kissed her good night."
    "She grabbed my neck and kissed me back."
    kid nervous "I love you, daddy."
    him normal "I love you, [kid_name]. Happy birthday."
    "I turned out the light and stepped out of the room."
    show night_overlay with dissolve
    kid sad "Wait, wait!"
    him normal "What is it?"
    kid concerned "I need a drink of water."
    him annoyed "Okay, go get some water if you want."
    kid sad "I want you to bring it to me."
    "Oh boy. I wasn't sure I had enough patience for this."
    menu:
        "What should I do?"
        "Bring her the water.":
            $ responsive += 1
            "I could bring her one cup of water, right?"
            him normal "Here you go."
            "I set down the cup and turned to leave."
            kid concerned "Daddy?"
            him annoyed "What?"
            kid sad "I need a hug."
            "I could do one hug, right?"
            "She wrapped her arms around my neck and didn't want to let go. She was still so small; she'd learned a lot in her short little life, but she still had a long way to go."
            "After a minute I extricated myself and patted her hand."
            him "Good night, [kid_name]."
            kid normal "Goodnight."

        "Politely refuse.":
            $ demanding += 1
            him determined "You can do that. Good night, sweetie."
            kid cry "Daddy!"
            him annoyed "It's time to go to sleep. I love you, good night."
            kid sad "...good night."

        "Tell her how you feel.":
            him annoyed "[kid_name], I just used up all my patience trying to get you to clean up your toys and I am about to explode!"
            kid cry "Daddy..."
            him determined "So, good night!"
            kid sad "...good night."
    return

label family7_she_cleaned_up:
    $ confident += 1
    menu:
        "What should I say?"
        "I'm glad you decided to clean up.":
            $ responsive += 1
            him normal "I'm glad you decided to clean up. Now you can play with your toys tomorrow."
            kid angry "..."
        "See? That wasn't so hard.":
            him determined "See? That wasn't so hard. Next time just clean up when I ask."
            kid angry "..."
        "I hope you learned your lesson.":
            him determined "I hope you learned your lesson, [kid_name]."
            kid angry "I learned you are mean."
    return

label family7_angry_ending:
    $ responsive -= 5
    hide her with moveoutright
    "I picked her up and put her in her room. She pounded her tiny fists on my back but I was so filled with rage and adrenaline that I barely felt them."
    him determined "Stay in your room until you can talk with respect!"
    kid "No I won't!"
    "She tried to make a run for it but I caught her arm and pushed her back in. She landed with a thump on the hard floor."
    "I closed the door before she could make another attempt to escape."
    him angry "You are not the boss! You are a spoiled, whiny, powerless child and {b}I{/b} am the boss of {b}you{/b}!"
    "She started crying. I locked the door from the outside."
    "She threw herself against it, the wood creaking, and started pounding on the door."
    kid "Let me out!"
    "She still didn't understand why she was so wrong."
    him annoyed "You stay in there until you're ready to quit being such a brat!"
    her angry "..."
    "The house was suddenly quiet. The only sound was [kid_name]'s sobs, muffled only slightly by the door."
    "[kid_name] cried herself to sleep, and I tried to read through my emails, but it was hard to concentrate."
    "[her_name] didn't talk to me either; she wouldn't even look at me. I think she was disappointed in me. That brought all my anger back to the surface again."
    him annoyed "You were a lot of help back there."
    her concerned "You scared me."
    him surprised "I scared {b}you{/b}?"
    her sad "I didn't think you were that kind of person. The kind of person that has to make others feel bad so he can make himself feel better."
    him angry "I'm not! You think I should just let her get away with that kind of disrespect?!"
    her determined "I think there's better ways than intimidation, yes. Do you really want [kid_name] to be afraid of you?"
    him annoyed "Maybe she should be afraid enough to show some manners."
    her annoyed "Respect doesn't come from fear. It comes from trust. And you just destroyed hers."
    kid "Mommy?"
    her concerned "What is it, dear?"
    "[kid_name] ran in and hid her face in [her_name]'s lap. The she spoke, so quietly that I could barely hear."
    kid "I peed in my bed."
    "[her_name] shot me a glare, as if [kid_name]'s bladder problems were my fault. She was probably peeing in the bed on purpose to try to get even with us!"
    "I started to stand up, but [her_name] beat me to it."
    her determined "I'll handle this. I don't trust you right now."
    "A sour mix of resentment and anger bubbled through my thoughts. I wanted to lash out, get even, show everyone that I was in charge..."
    "But I didn't want to be that kind of dad."
    "The kind of dad whose own kids were afraid of him."
    "I remember being afraid of my dad, sometimes. That's why whenever I had problems, I always went to my mom."
    "I didn't want [kid_name] to feel like that."
    $ marriage_strength -= 1
    return

# 5 Earth years old
# Play group, First Day of School
label family8:
    "It was my turn to host playgroup. It always felt a little frustrating not to be able to go out in the fields and get my work done, but I could also see that it was good for [kid_name]."
    "I'll admit I looked forward to school starting next week. We had just had a preview day where these kids got to see the school and meet the teacher."
    "[kid_name] was really excited -- she loved new things, and the school had some pretty fun learning toys. I wasn't worried about her at all."
    "But I wondered how the other kids in her playgroup would handle the transition to school..."
    scene fields with fade
    show him normal at quarterright
    show kid normal at center
    show travis at midleft
    show oleg at quarterleft
    travis "Mud fight!"
    him annoyed "Hey! Quit throwing mud! Not everyone wants to play that."
    kid laugh "I do!"
    show kid normal at squatting with move
    "Travis threw his mudball at her and she dodged it, giggling."
    show kid normal at center with move
    "She scooped up some mud of her own and flung it his way, but it hit Oleg instead, who was busy drawing in the dirt with a stick."
    show travis at squatting with move
    show oleg sad with dissolve
    show travis at midleft with move
    "He started crying."
    "[kid_name] didn't seem to notice; she was still chasing down Travis."
    menu:
        "What should I do?"
        "Run after [kid_name].":
            $ demanding += 1
            him angry "[kid_name]!"
            kid happy "What?"
            "She yelled back without stopping her chase."
            him annoyed "Come here. I need to talk to you."
            kid concerned "Why?"
            him angry "Come here now!"
            "She finally stopped chasing Travis and came over to me."
            kid annoyed "What?"
            him concerned "You just hit Oleg in the face with your mudball."
            kid nervous "Oh. Whoops."
            him annoyed "You need to go apologize to him."
            "She yelled over at Oleg, who was still wiping his face off onto his shirt."
            kid surprised "Sorry, Oleg!"
            oleg "..."
            menu:
                "What should I do?"
                "Insist on a better apology.":
                    $ demanding += 1
                    him determined "What kind of apology was that? You need to walk over to him and tell him sincerely to his face."
                    kid annoyed "I already said sorry!"
                    him annoyed "You need to say it for real."
                    kid angry "Fine."
                    "She ran over to Oleg."
                    kid shifty "I'm sorry."
                    oleg "It's okay."
                    kid angry "There; are you happy now?!"
                    "I sighed. It was so much work to keep up with that child..."
                "Teach her about apologies later.":
                    $ demanding += 1
                    $ responsive += 1
                    "I decided we needed to have a talk about the right way to apologize later."
                    scene farm_interior with fade
                    show him normal at midleft
                    show kid normal at midright
                    him concerned "[kid_name], why do you think we say sorry when we hurt someone?"
                    kid shifty "I don't know."
                    him surprised "How do you feel when someone hurts you?"
                    kid angry "Mad. And sad."
                    him determined "What about when they say they're sorry?"
                    kid concerned "Not so mad."
                    him normal "Exactly. Saying sorry helps us both feel better. So when you say sorry, make sure you say it in a way that communicates that."
                    kid annoyed "I do!"
                    him "Let's practice. Pretend I took your toy tractor."
                    kid angry "Hey, give me back my tractor!"
                    him "Oh, I'm sorry. Here, you can have it back."
                    "I exaggerated the emotion to show her how to apologize."
                    kid concerned "Okay..."
                    him "Now you pretend you've taken my tractor."
                    kid happy "Ha ha, it's mine, now!"
                    him sad "Hey, give me back my tractor!"
                    kid sad "I'm sorry. Here, you can have it back."
                    him happy "Good job! Apologize just like that next time, okay?"
                    kid normal "Okay..."
                    "She wasn't perfect at it, but I think I taught her pretty well."
                    "At any rate, I knew we'd have plenty of opportunities to practice apologies in the future."
                "Let it go.":
                    "That was good enough, I guess."
        "Comfort Oleg.":
            $ responsive += 1
            him concerned "Sorry about that, Oleg. Here, you can wipe the mud off with this."
            oleg "Okay. I hate being dirty."
            "Once Oleg got cleaned up, he didn't seem too upset, but went back to his drawing. I was a little jealous of Ilian and Sara sometimes -- how come they got such an easygoing kid?"
            "[kid_name] ran back toward us, racing Travis, and I had to smile."
            "She wasn't an easy kid -- but I loved her vibrant energy and insatiable curiosity...even when it sometimes exhausted me."
            menu:
                "Have her apologize to Oleg.":
                    $ demanding += 1
                    him concerned "[kid_name], you hit Oleg in the face with a mudball and then ran away."
                    kid shifty "Oh. Sorry, Oleg!"
                    oleg "It's okay."
                "Let it go.":
                    "Oleg was fine; no need to bring that up again."

    scene black with fade
    "Soon school started, and [her_name] and I walked [kid_name] to the school for her first day."
    scene path with fade #TODO: school house background?
    show him normal at midleft
    show her normal at midright
    show kid normal at center
    with dissolve

    kid happy "And then I'm going to make breakfast for Oleg with the toy kitchen set, and then at recess I'm going to go down the slide really fast and I hope we get to draw and I hope my teacher knows I already know all my colors..."
    kid laugh "...and the letters of the alphabet and my numbers up to fifty except Travis says I always mess up around forty-seven and skip right to forty-nine but I don't, right, daddy?"
    him surprised "Um, what was the question?"
    kid normal "I'm so excited to eat lunch there, too! I have my very own lunch box and I'm going to show it to Travis and he'll think it's so cool how we made it together, daddy."
    her concerned "[kid_name]."
    kid concerned "What?"
    her normal "We're almost there. Come get a goodbye hug."
    kid normal "Bye, mommy!"
    "She turned to me, and I felt like I should say something, but I wasn't sure what."
    menu:
        "What should I do?"
        "Say nothing.":
            "I didn't need to say anything. I just gave her a little wave and turned to walk away."
            $ neglectful += 1
        "Cheerfully give her a goodbye hug.":
            him happy "Goodbye, sweetie! Do your best!"
            kid happy "I always do my best!"
            "I hugged her tight and she ran off to the schoolhouse."
            $ demanding += 1
            $ responsive += 1
            $ confident += 1
            $ authoritative += 1
        "Admonish her to behave.":
            him determined "You make sure you behave yourself in there, [kid_name]. Do everything your teacher says."
            kid shifty "Uh-huh."
            $ demanding += 1
            $ authoritarian += 1
        "Tell her it's okay to be nervous":
            him concerned "It's okay to be nervous, [kid_name]; this is a big step! You've never been to school; it's going to be very different for you."
            kid shifty "Uh-huh."
            "I hugged her tight and didn't want to let go. I couldn't believe my little baby was going off to school..."
            $ responsive += 1
            $ permissive += 1

    "[her_name] moved to follow her, but I held her hand."
    him normal "Didn't her teacher ask us not to come in with her, so she could get used to coming in on her own?"
    her concerned "I guess so... Is she really going to be okay?"
    "We heard a wail and saw Oleg arriving with Ilian and Sara. His hand was clenched tightly around Sara's. Ilian was carrying their second child on his shoulders. The whole family looked stressed out."
    "Sara gave little Oleg a hug and gestured toward the school, but he shook his head. Tears streamed down his face. Their baby sensed the mood and started fussing also."
    him surprised "I guess we have it pretty easy, huh?"
    her normal "For once. I'm going to help them out; want to come?"
    menu:
        "What should I do?"
        "Go to work":
            him concerned "Sorry, I have too much work to do."
            her concerned "Okay, don't forget to pick up [kid_name] today. Eventually she can walk home on her own, but I told her you'd walk with her today."
            him determined "Okay."
            "[her_name] went and took the baby from Ilian so they could both concentrate on helping Oleg. I turned away and jogged back to the farm. I had a lot of work to do."
        "Go with [her_name]":
            $ marriage_strength += 1
            # TODO: crop consequences?
            him normal "Sure, I have a few minutes."
            "[her_name] went and took the baby from Ilian so they could both concentrate on helping Oleg."
            "[her_name] cuddled the baby and I distracted her with peek-a-boo until Ilian and Sara finally got Oleg to go inside the school."
            sara sad "Thanks, guys. I really hope Oleg will be okay..."
            ilian "Now that he's away from us, he'll be fine. He was the same way when we first started playgroup, remember?"
            him normal "He'd cry and cry until you left, and then he'd be completely happy the whole time."
            her normal "Except as soon as you came to pick him up, he'd cry again."
            sara normal "You're probably right."
            sara sad "But maybe we should peek in him, just in case."
            her surprised "I'll admit, I'm a little curious about what they're doing..."
            "The four of us crept over to the schoolhouse."
            ilian "Sara, if he sees you or me, he'll start crying. Someone else had better look."
            her normal "I'm holding the baby; [his_name] should do it."
            him happy "Okay! I got this!"
            "I sidled up to the side of the window and slowly peered inside."
            scene classroom with fade
            show kid normal at midright
            show oleg at midleft
            with dissolve
            show frame_overlay
            # TODO: is this frame ok?
            kid normal "Here's your cornmeal mush, Oleg. Isn't it delicious?"
            "She handed him a small empty bowl with a little spoon. He pretended to take a bite."
            oleg "That's delicious! I like the raisins."
            kid shifty "Travis grew them for me. He's the dad, and I'm the mom, and you can be the baby."
            oleg "Wahhh, wahhhh!"
            kid concerned "There, there, baby, have some more cornmeal mush."
            oleg "Ptooey!"
            "He pretended to spit it out. He did a pretty good impression of his baby sister."
            show travis at center with moveinright
            travis "Dinosaurs with bazookas are coming! Fight them off!"
            show kid angry at pace_back_and_forth
            show oleg at pace_back_and_forth
            show travis at pace_back_and_forth
            "[kid_name] swatted the air with her frying pan while Travis used a rolling pin as a gun and Oleg made some swatting motions in the air."
            "Teacher" "Come over here, it's circle time!"
            hide travis
            hide kid
            hide oleg
            with moveoutleft
            scene path with fade
            sara "Well?"
            him "They were all playing happily. They even obeyed the teacher when she called them. I think they'll be fine."
            ilian "Good. Now I've got to run; I've had three people message me wondering why the storehouse isn't open yet."

    if (year6_have_baby):
        scene black with fade
        "[her_name]'s second pregnancy seemed to go by so much faster than the first one."
        "A few weeks after school started, [her_name] went into labor in the middle of the night."
        # TODO: Depending on faction, contact someone different to watch Terra?
        call baby_delivery

    else:
        scene black with fade
        "The next day, we walked [kid_name] to school again. After we dropped her off, [her_name] wanted to talk to me about something."
        $ year8_have_baby = True
        scene path with fade
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
                    her serious "Yes. But it'll be okay."
                    him serious "We'll figure it out."
            "We can do this!":
                $ marriage_strength += 1
                him determined "This is...this is..."
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
                $ marriage_strength += 1
                him surprised "How do you feel about it?"
                her concerned "I don't know. Worried, I guess."
                him concerned "Yeah, how will this even work?"
                her sad "I don't know if I can do this..."
                him determined "Hey, don't cry, it'll be okay."
                jump pregnancy_alone

    return

label baby_delivery:
    scene hospital with fade
    show him normal at midleft
    show her normal at center
    with dissolve
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
    her pregnant concerned "You forgot the 'shut up' part."
    him normal "..."
    show julia at midright with moveinright
    scene black with fade
    scene hospital with fade
    show him normal at midleft
    show her pregnant concerned at center
    show julia at midright
    with dissolve
    "Finally, the baby was born. A boy!"
    $ bro_birth_year = year

    "...but he didn't look like [kid_name] did when she was born."
    him surprised "Is... is he missing some of his lip?"
    julia "Looks like a cleft lip. Somehow we missed that on the ultrasound."
    her surprised "Oh my..."
    menu:
        "What should I say?"
        "We'll get through this.":
            him concerned "[her_name]... it's okay. We'll get through this."
            her sad "I know, it's just... he looks so different than I was expecting..."
        "What an ugly child.":
            him determined "That is the ugliest child I have ever seen."
            julia "[his_name]!"
            her sad "[his_name]...I'm sorry."
            him surprised "It's not your fault! I'm just saying whatever pops into my head."
        "He's my son!":
            him happy "Wow, this kid looks so goofy, he's definitely my son."
            her concerned "[his_name]..."
            "I bundled him up and held him close."

    julia "Repairing a cleft lip is a fairly simple surgery. But don't worry about that right now. Just hold that precious baby!"
    "I snuggled him close while Julia finished helping [her_name] with the afterbirth. He opened his eyes and looked right at me. His serious expression pierced my heart."
    him normal "Awww, don't worry little guy! We'll take care of you, no matter what."
    her normal "We can't call him 'little guy'. What's his name?"
    him determined "We talked about lots of names..."
    her determined "You let me choose [kid_name]'s name. Now you pick this baby's name."
    him surprised "Really? You trust me to name him?"
    her flirt "As long as it's one of the names we both agreed on."
    him happy "Okay! Let's see... you look like a..."
    $bro_name = renpy.input("Baby's Name", default=bro_name)

    her surprised "You picked [bro_name]? Hmmm. I guess he does kind of look like a '[bro_name]'."
    scene farm_interior with fade
    "It took me a long time to get used to [bro_name]'s cleft lip. But the look wasn't the hardest part of it -- it was how hard it was to feed him."
    "It took half an hour just to feed him one bottle, and I had to help squeeze the bottle for him. His cleft lip made it harder for him to get the suction he needed to get the milk out of the bottle."
    "And he couldn't really breastfeed well at all."
    "[kid_name] kind of understood that [bro_name] needed a lot of attention, and we tried to include her in taking care of him and everything else we did."
    "Still, she probably ended up resenting him a little. And I could understand why. Sometimes I felt frustrated that he needed so much from us."
    "But, when I forgot myself and just loved him, all that time spent together strengthened our whole family."

    return

# 5.5 Earth years old
# Getting along with friends, being bossy
label family9:
    "Now that [kid_name] was in school, our family dynamics had changed."
    "Instead of yearning for a few minutes of uninterrupted time and slogging through our weekly turn in the kids' coop, I found myself looking forward to her coming home from school."
    "She seemed to appreciate me more, too."
    scene fields with fade
    show him normal at midright
    if (year6_have_baby):
        show bro at midright, baby_pos
    with dissolve
    show kid normal at midleft
    show oleg at quarterleft
    with moveinleft
    kid happy "Daddy!"
    show kid normal at midright with move
    if (year6_have_baby):
        "I set [bro_name] down so I could give [kid_name] my full attention for a minute."
        show bro at baby_pos
        show kid at midright, baby_pos with move
    "She tackled me with a big hug and I swung her around in a circle."
    show kid happy at quarterright, standing with move
    him happy "Welcome home! Oh, I see you brought Oleg with you. Hi, there!"
    show oleg at center with move
    oleg "Hello, Mr. [his_name]."
    kid shifty "Is it okay if Oleg comes over to play?"
    him normal "Of course!"
    "Oleg was so polite and obedient; he hardly ever got into trouble. [kid_name] actually behaved better when he was around."
    $ random_crop = farm.crops.random_crop()
    "The two of them ran off to play and I continued working with the [random_crop]."
    hide kid
    hide oleg
    with moveoutleft

    "After a while, I figured I should check on them."
    scene barn with fade
    show kid normal at midright
    show oleg at quarterright
    with dissolve
    "I found them in the barn, where [kid_name] had put one of Lettie's saddle blankets on Oleg and a rope loosely around his neck."
    kid happy "Giddyup, horsie!"
    show him normal at midleft
    if (year6_have_baby):
        show bro at midleft, baby_pos
    with moveinleft
    oleg "[kid_name]..."
    kid normal "Now go around in a circle. We have to patrol the whole farm for crabirds."
    oleg "{b}Then{/b} can we play something else?"
    kid shifty "Maybe."
    "Poor Oleg. He was perhaps a little too nice..."
    him "[kid_name], you can't have a rope around someone's neck. That's too dangerous."
    kid annoyed "Awww, dad!"
    "She took the rope off, and Oleg looked a little relieved."
    menu:
        "What else should I say?"
        "Maybe you should play something else.":
            $ responsive += 1
            him happy "[kid_name], I think you should play something else."
            kid sad "But daaad!"
            him surprised "Oleg, what do you want to play?"
            $ permissive += 1
        "Stop bossing Oleg around.":
            $ demanding += 1
            him annoyed "Quit bossing Oleg around. He's not going to want to play with you anymore."
            kid angry "Oleg likes playing with me! Don't you, Oleg?"
            oleg "I do... but {size=-10}I want to play something else{/size}."
            him surprised "What do you want to play, Oleg?"
            $ authoritarian += 1
        "Come here so I can talk to you privately.":
            $ demanding += 1
            $ responsive += 1
            $ confident += 1
            him determined "Come here, [kid_name]. I have something to tell you."
            show kid normal at center with move
            kid concerned "What?"
            "I leaned down a whispered into her ear."
            him concerned "Oleg's been trying to tell you that he wants to play something else. He's our guest, so can you make sure he's having fun, too?"
            kid annoyed "He is having fun!"
            him determined "I don't think so. Ask him what he would like to do, and then do that."
            kid concerned "Fine."
            show kid normal at midright with move
            kid surprised "What do you want to play, Oleg?"
            $ authoritative += 1
        "Never mind.":
            "They didn't need me to tell them what to do. If Oleg didn't like playing horsie, he could just say so."
            $ neglectful += 1
            jump family9_sara
    oleg "Umm, I don't know..."
    kid yell "See? If we don't do what I want to do, then we just end up doing nothing!"
    him normal "Figure out something to do together. Maybe that game where you pretend to be on a spaceship visiting different planets?"
    oleg happy "Yeah! We can go to pillow planet that's full of pillows!"
    kid happy "And applesauce planet!"
    label family9_sara:
        "I was about to leave when Sara walked in."
        show sara sad at left with moveinleft
        sara "Oleg! Where have you been?!"
        oleg "Just playing."
        sara "When you didn't come home from school I was so worried!"
        "Our eyes met, and I knew were were both thinking of Josephina, the Peron's little girl who had gone missing seven years ago."
        "Anytime a kid was missing, we all remembered searching for her all night long, her dead body washing ashore, her funeral..."
        him concerned "I'm sorry; I thought you knew he was here."
        oleg "[kid_name] wanted me to come play..."
        sara normal "Well, you can't just do whatever [kid_name] says. You have to do what your momma says."
        show oleg at quarterleft with move
        oleg "I'm sorry, momma."
        "The poor kid looked about to cry."
        sara "It's okay, baby. It's okay."
        "We setup a schedule where Oleg could come play on certain days, and [kid_name] would play at his house on other days."
        "I hoped they would continue to be good friends."
        return
    return

# 6.2 Earth years old
# Fighting with brother OR playing games when she's not supposed to
label family10:
    "Sometimes I had to make sure to stop and enjoy the good times. It always felt like such a relief when no one was crying or needed anything, but I didn't want to take such times for granted."
    "[kid_name] came home from school and I gave her a snack."
    scene farm_interior with fade
    show him normal at midright
    if (year6_have_baby):
        show bro at center, baby_pos
        "[bro_name] wanted a snack, too, so I sliced up some tomatoes."
    show kid shifty at midleft with moveinleft
    menu:
        "What should I say?"
        "How was school today?":
            him normal "How was school today?"
            kid concerned "Okay."
            him concerned "..."
            kid annoyed "..."
            if (year6_have_baby):
                him normal "[bro_name] and I rode the tractor all over today plowing the fields and mixing in the compost."
            else:
                him normal "I plowed the fields today. Gotta mix in all that fertilizer."
            kid concerned "Okay."
        "What was the funniest thing that happened today?":
            $ responsive += 1
            him happy "What was the funniest thing that happened today?"
            kid surprised "The funniest?"
            him surprised "Or just one funny thing. Maybe there were a lot."
            kid shifty "Hmmm.... Well, we talked about what we wanted to be when we grew up."
            him normal "Oh yeah?"
            kid normal "The teacher asked Oleg first, and he said he wanted to be a crabird."
            him happy "Ha ha, wow, that'd be weird."
            kid happy "Yeah! And then I thought, if I could be anything, I'd like to be a spaceship so I could take people anywhere they wanted to go."
            him surprised "A spaceship, huh?"
            kid nervous "Yeah, we could go to Earth whenever we wanted, and I could meet my grandparents, and get stuff people wanted."
            him normal "Who knows, maybe you'll be a pilot or something?"
            kid laugh "Or I might invent teleporters."
            him happy "I would love that."
        "What did you learn today?":
            $ demanding += 1
            him determined "So, what did you learn today?"
            kid annoyed "Nothing."
            him annoyed "Right, because you already know everything."
            kid shifty "Yup."
            him surprised "So what did you discuss today?"
            kid concerned "Stuff."
            him annoyed "Such as?"
            kid surprised "Dad, why does it take so long for ships to get here from Earth?"
            him surprised "Oh, is that what you talked about at school?"
            kid annoyed "No, I just want to know."
            him normal "Well, I guess it's hard to make something go that fast. And it's really far."
            kid concerned "Does Earth really exist?"
            him happy "It definitely does. I was born there."
            kid shifty "It's just so hard to imagine."
            him surprised "Yeah, I bet it seems so foreign..."
            kid concerned "It is. All those cities, so many people... it's just weird."
        "(Don't say anything)":
            him concerned "..."
            kid concerned "..."
            "She ate her snack in silence."

    if (year6_have_baby):
        "She finished her snack and got out the blocks. I cleaned up the kitchen a bit and [bro_name] wandered over to play with her."
        show bro at quarterleft, baby_pos with move
        show him normal with dissolve
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
                him normal "I'm glad to see you playing happily together."
                "I tousled their hair. I know I'm probably biased, but they seemed like the cutest kids in the universe to me."
                "They didn't seem to even notice I was there, and just kept playing."
            "Just keep watching.":
                "I didn't want to ruin the moment, so I just watched them."
        kid shifty "[bro_name]! Look what I built! Here's the volcano. And here's us."
        "She walked the figurines up the mountain until they reached the top. [bro_name] made to touch the blocks, but she stopped him."
        kid concerned "No no, it's hot."
        bro "Hot?"
        "She had the parent figurines give warnings."
        kid angry "\"It's so hot!\" \"Don't fall in!\""
        kid concerned "Here's [bro_name]. Uh-oh, he's getting close to the edge!"
        "She dropped one of the figurines into the \"volcano\" while making a disturbingly accurate crying sound. [bro_name] just watched. He was probably happy to get any attention from her at all, but..."
        menu:
            "Should I say something?"
            "Wait and see.":
                "I waited to see what [kid_name] would do."
                kid angry "\"I'll save you!\""
                "She had the family hold hands and lower her figurine into the volcano, and she fished her brother out."
                kid normal "Gotcha! Whew, that was close!"
                bro surprised "I in there?"
                kid happy "Yeah, you were in the lava! But we got you out."
                bro concerned "Hot?"
                kid normal "No, it's not hot anymore."
                "He pushed the side of the volcano, and the blocks tumbled down."
                "She looked furious."
                kid yell "[bro_name]! No, no, NO!!!"
                menu:
                    "What should I say?"
                    "Stop yelling at him!":
                        $ demanding += 1
                        him angry "Stop yelling at your brother!"
                        kid angry "He wrecked my volcano!"
                        him annoyed "They're his blocks, too. You need to share!"
                        kid annoyed "I was sharing!"
                        him angry "Well, it's his turn, now!"
                        kid yell "No! I'm in the middle of a game!"
                        him annoyed "Go to your room!"
                        kid cry "You ruined everything!"
                        "She stomped off, and [bro_name] started crying. I tried to comfort him, but it was difficult when I was so angry."
                        him "(How does a little six-year-old know how to make me so mad?!)"
                        $ authoritarian += 1
                    "Hey, it's an earthquake!":
                        $ responsive += 1
                        him surprised "Ahhh, earthquake! Can the family survive?"
                        "I pulled my figurine out of the pile of blocks."
                        him determined "\"Don't worry, I'll save you!\""
                        "I dug around, trying to get the other figurines out. I got [kid_name]'s and handed it to her."
                        him surprised "Quick, we've got to get [bro_name] and mom!"
                        "We rummaged through the blocks until we pulled out their two figurines. I handed [bro_name] his."
                        kid happy "Now run away from the lava!"
                        him happy "Ahhhh, lava!"
                        "We made our guys run down the pile of blocks."
                        menu:
                            "Keep playing with them.":
                                "The three of us played natural disaster-escaping family until dinner time."
                                # TODO: have some farming consequences?
                                $ permissive += 1
                            "Compliment them on getting along.":
                                $ demanding += 1
                                $ confident += 1
                                him normal "Good job getting along."
                                "I'm pretty sure [kid_name] heard me, but she was already on to the next thing and didn't respond."
                                "I left them to it while I went to change the oil in my tractor. Hopefully they'd get along for awhile."
                                $ authoritative += 1
            "Leave them alone.":
                "Nobody was sad; they didn't need me to interfere."
                "Besides, the tractor needed an oil change."
                $ confident += 1
                $ neglectful += 1
            "Scold [kid_name].":
                $ demanding += 1
                him annoyed "[kid_name]! Don't drop your brother in the volcano!"
                "She looked at me defiantly, then shoved the blocks, burying all the figurines. One tipped and fell on [bro_name], who started crying."
                kid yell "Earthquake! The volcano's erupting! There's lava everywhere! Ahhhhhh!"
                bro cry "Wahhhhh!"
                show him surprised with dissolve
                kid concerned "We all died."
                bro sad "All died."
                kid shifty "Except me. I ran away."
                him annoyed "Terra..."
                kid concerned "And now I live by myself in the jungle."
                "[bro_name] reached for his figurine, but she pulled it out first and put it up high where he couldn't reach."
                kid annoyed "You can't play with him. He's dead."
                bro annoyed "I want it!"
                kid angry "Nope. Dead is forever. All gone."
                bro cry "Not all gone!"
                him annoyed "[kid_name], that's enough. If you can't get along with [bro_name], then you'll need to go to your room."
                show bro surprised
                show him determined
                show kid annoyed
                with dissolve
                "I gave [bro_name] his figure. He looked at it suspiciously, as if trying to tell from its appearance whether it was still okay to play with after being \"dead\"."
                kid angry "Dad, you're ruining the game!"
                menu:
                    "Scold her some more.":
                        him angry "No, {b}you{/b} are ruining the game! How does it make [bro_name] feel to have you killing off his guy?"
                        kid annoyed "It's just a game!"
                        him annoyed "Even in a game you can't be a jerk to everyone!"
                        kid yell "You're a jerk!"
                        him angry "That's enough! Go to your room!"
                        kid annoyed "You go to your room!"
                        "I picked her up. She'd gotten heavier, but my adrenaline was up now and I lifted her easily and dropped her into her room."
                        "I meant to set her down, but she struggled right as we reached the doorway and she kicked my wrist."
                        "I tried to set her down gently but I kind of dropped her and her head hit her bed post."
                        kid cry "Wahhhhhhhhh!"
                        menu:
                            "What should I say?"
                            "That's what you get for disobeying.":
                                him annoyed "That's what you get for disobeying your father!"
                                kid angry "You hurt me!"
                                him "..."
                                kid sad "You're so mean..."
                                "I turned away. She was trying to make me feel guilty, but none of this would have happened if she had just done what I asked!"
                                $ responsive -= 1
                                $ authoritarian += 1
                            "I'm sorry.":
                                him concerned "I'm sorry, [kid_name]. I didn't mean for you to hit your head."
                                kid sad "Yes, you did. You're always mean to me."
                                "I tried to hug her but she turned away. I couldn't make her accept my apology. But hopefully she'd remember what I'd said."
                                $ authoritarian += 1

                    "Suggest they play something else.":
                        him surprised "Why don't we make a road for the guys instead?"
                        "I started laying out some blocks in a path. [kid_name] just watched me for a minute, but [bro_name] brought his figure over and banged it on the block path happily."
                        "I made a building out of blocks."
                        him normal "Here's the school."
                        "[kid_name] made a path going off a different way."
                        kid normal "And here's the storehouse. I'm going to get all the applesauce."
                        him surprised "Here, [bro_name], why don't you use these blocks here?"
                        "I cleared out a little space for him and stacked some blocks up in a way that would be hard to knock down."
                        "He knocked it down anyway, banging his figurine on the blocks as if it was jumping."
                        him happy "Ha ha, maybe that's the junk pile."
                        "They played together for a while and I snuck off. Hopefully I still had time to change the oil in the tractor."
                        $ responsive += 1
                        $ authoritative += 1

    # She doesn't have a little brother, so instead she's playing on the tablet
    else:
        kid surprised "Can I use the computer pad?"
        him surprised "What are you going to do on it?"
        kid shifty "Can I play Goose Life?"
        him annoyed "Goose Life?"
        "It was a pretty stupid game, mostly just tapping moving things on the screen. But it was addictive, so she liked it."
        menu:
            "What should I say?"
            "Fine, whatever.":
                $ responsive += 1
                $ confident += 1
                him annoyed "Fine, whatever."
                kid happy "Yay!"
                $ neglectful += 1
                jump family10_ending
            "No, something else.":
                $ demanding += 1
                him determined "No, choose something else."
                kid concerned "Science Kids is pretty fun, I guess."
                him normal "That sounds better."
            "You can play it for fifteen minutes and then you need to choose something else.":
                $ responsive += 1
                $ demanding += 1
                $ confident += 1
                him normal "You can play it for fifteen minutes and then you need to do something else. Here, I'll set a timer."
                kid happy "Okay."

        "She sat on the floor and was soon engrossed, and I went to go change the oil in the tractor."
        "It was probably an hour or so later that I went back in to check on her."
        "I opened the door, and she looked up guiltily. She quickly swiped her app away and tried to smile at me."
        kid shifty "Hi, dad."
        menu:
            "What should I do?"
            "Ask her about it":
                $ responsive += 1
                him surprised "Were you playing Goose Life?"
                kid sad "No..."
            "Accuse her":
                $ demanding += 1
                him angry "You were playing Goose Life! When I told you not to!"
                kid annoyed "No I wasn't!"
            "Do nothing":
                "I didn't have time for this. She wasn't in any danger, and I needed to get back to work."
                $ neglectful += 1
                jump family10_ending

        menu:
            "What should I do?"
            "Investigate the computer pad.":
                "I grabbed the computer pad, but I couldn't tell what she had been doing."
                "I had no proof...but her expression told me she was hiding something."
            "Ask for the truth.":
                him determined "Tell me the truth."
                kid angry "I did!"
                him angry "I know you're lying!"
                kid sad "I'm not!"
            "Go back to work.":
                "She might have been lying, but I didn't have time to figure it out. I had to get back to work."
                $ neglectful += 1
                jump family10_ending

        menu:
            "What should I do?"
            "Talk about why lying is bad.":
                $ responsive += 1
                him concerned "When you lie, I can't trust what you say. I want to be able to trust you."
                kid concerned "I know."
                him "I don't want you to ever lie to me, okay?"
                kid sad "Okay."
                $ permissive += 1
            "Punish her.":
                $ demanding += 1
                him angry "I can't believe you lied to me! You're grounded for a month!"
                kid angry "You're so mean!"
                him annoyed "I wouldn't have to get mean if you would just do what you're told."
                $ authoritarian += 1
            "Take away the computer pad.":
                $ demanding += 1
                $ responsive += 1
                "I took the computer pad and put it up high."
                him determined "You weren't following our rules, so now you cannot play with the computer pad."
                kid angry "What! But I didn't do anything!"
                him concerned "I'm disappointed that I can't trust you to follow our rules or tell the truth. You will not be able to use the computer pad for two weeks."
                kid yell "Two weeks?!"
                him annoyed "One for disobeying the rules, and one for lying about it."
                kid angry "That's not fair!"
                him determined "That's the consequence for breaking that rule."
                kid cry "I'm sorry! I did play Goose Life. But I just really want to see the ending!"
                him normal "I understand. But you still broke the rules."
                kid shifty "So... since I told the truth, can you reduce the time to just one week?"
                menu:
                    "What should I say?"
                    "No, it's too late for that.":
                        him determined "Sorry, it's too late for that. You needed to tell the truth in the first place."
                        $ demanding += 1
                    "Yeah, I guess.":
                        him concerned "Yeah, I guess."
                        $ responsive += 1
                    "I'll reduce it by two days.":
                        him determined "I appreciate that you finally told the truth, so I will reduce the time by two days. Next time I hope you'll tell me the truth right away."
                        $ demanding += 1
                        $ responsive += 1
                kid annoyed "...you're mean."
                him normal "Sometimes."
                $ authoritative += 1

    label family10_ending:
        if (year8_have_baby):
            "[her_name]'s second pregnancy seemed to go by so much faster than the first one."
            "[kid_name] was really looking forward to having a little brother or sister; she was all excited to help with everything."
            "A few weeks after school started, [her_name] went into labor in the middle of the night."
            # TODO: Depending on faction, contact someone different to watch Terra?
            call baby_delivery
    return

# 6.8 Earth years old
# Dinner Table Manners
# TODO: Continue writing blocking from here
label family11:
    scene farm_interior with fade
    show him normal at midleft
    show her normal at midright
    show kid normal at center
    "Meal times at our house were never boring. [kid_name] would tell us about what happened at school, [her_name] would talk about the patients she saw, and I would update everyone on how the crops were doing."
    "Even [bro_name] usually had something to say."
    "They weren't always peaceful, though..."
    kid "Beans again? Ugh."
    him "You can put Special Sauce on them if you want."
    "We called it \"Special Sauce\", but it was really just homemade ketchup. With fruit instead of sugar."
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
            him determined "Here you go."
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
            $ demanding += 1
            him "Where are your manners? I raised you to speak better than that!"
            kid "C'mon, pass me the sauce!"
        "I'm eating outside.":
            him "I'm eating outside."
            "Maybe that would get the message across. I just couldn't deal with that kind of garbage right now."
            "I took the special sauce with me."
            $ confident += 1
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
            $ confident += 1
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
            kid "You're starving your child here!"
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

        "If you keep talking rudely, you'll be grounded!" if (manners_grounded_days < 7):
            $ demanding += 1
            him annoyed "If you keep talking rudely, you'll be grounded!"
            kid "Gimme the sauce!"
            him angry "Okay, you're grounded for another day."
            $ manners_grounded_days += 1
            if (manners_grounded_days > 1):
                him "That makes [manners_grounded_days] days, now. Is this really worth it?"
            jump manners_patience

        "As soon as you ask politely, I will pass them to you." if (manners_patience_count < 2):
            $ demanding += 1
            $ responsive += 1
            him determined "As soon as you ask politely, I will pass them to you."
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
# Growing Independence, miner friend, lice
label family12:
    scene farm_interior with fade
    show him normal at midright
    show kid normal at midleft with moveinleft
    him happy "Welcome home, [kid_name]! How was school?"
    kid "Pretty good. Hey, can I go over to Anya's house tomorrow? I can walk home with her."
    him surprised "Tomorrow? Who's Anya?"
    kid "One of my friends from school."
    him concerned "Really? I don't know of any farmers who have a kid named Anya..."
    kid "Her parents are miners."
    him determined "Oh."
    "I wasn't sure what to think about that. On the one hand, I was glad she had a new friend; she'd never had a girl her own age to be friends with before."
    "On the other hand, I didn't know much about the miners. Should I really let her go to someone's house I didn't know?"
    "I couldn't help but think of Josefina, the Peron's daughter that accidentally got run over by Pete's tractor when she was about this age."
    kid "Please, dad? We're like best friends."
    him surprised "Who are her parents?"
    kid "I don't know; just...parents, I guess."
    menu:
        "What should I say?"
        "Sure, you can go.":
            $ responsive += 1
            $ confident += 1
            him normal "Sure, you can go."
            kid "Yay! I'm going to message her right now, she'll be so excited!"
            $ permissive += 1
            call family12_anyas_house
        "Are her parents going to be home?":
            $ demanding += 1
            $ confident += 1
            him concerned "Are her parents going to be home?"
            kid "Um, yeah, I guess, probably?"
            him determined "You don't know."
            kid "We don't talk about our parents!"
            him surprised "Why don't I message her parents and get some more information?"
            kid "Okay. Her last name's Lewis."
            call family12_contact_parents
        "I don't want you going over to some random miner's house.":
            $ demanding += 1
            him annoyed "I don't want you going over to some random miner's house. I don't know anything about them!"
            kid "They're not random! Anya's my best friend!"
            menu:
                "What should I say?"
                "Sorry, I don't have time.":
                    him determined "I don't know them, and I don't have time to get to know them. Sorry, [kid_name]."
                    kid "You're so mean!"
                    $ neglectful += 1
                    call family12_disobey
                "You can't go over to someone's house unless I know them.":
                    $ demanding += 1
                    him determined "Sorry, [kid_name]. You can't go over to someone's house unless I know their parents."
                    kid "Well, then you need to get to know Anya's parents!"
                    him "Picking my friends is not your job."
                    kid "But your job is to pick my friends?!"
                    him "Yes, it is."
                    $ authoritarian += 1
                    call family12_disobey
                "Maybe I could send them a message.":
                    him concerned "I guess I could send a message or something..."
                    call family12_contact_parents

        "Why don't you invite her to come over here?":
            $ demanding += 1
            him concerned "Why don't you invite her to come over here? That'd be easier."
            kid "I do want to to that, but tomorrow she's going to show me some cool stuff she brought from Earth!"
            menu:
                "What should I say?"
                "You can't go.":
                    him determined "Sorry, [kid_name]. You can't go over to someone's house unless I know their parents."
                    kid "What?! Dad, that's so mean."
                    $ authoritarian += 1
                    call family12_disobey
                "Let me talk to her parents first.":
                    him concerned "I guess I could send her parents a message..."
                    call family12_contact_parents



    scene black with fade
    "Anya was a good enough kid; she and [kid_name] certainly seemed to have fun together. They giggled and made mud pies and bracelets and played space explorers."
    "Several days later, though, I noticed something."
    scene farm_interior with fade
    show him normal at midright
    show kid normal at midleft
    kid "I'm just so itchy! All the time!"
    him surprised "Did you touch a weird plant or something? Where do you itch?"
    kid "On my head!"
    "I was ready for some bizarre alien tick or something (though since most of the animals here were cold blooded, it seemed unlikely), but I wasn't ready for what I found."
    him concerned "You have something in your hair... is this dandruff?"
    kid "What's dandruff?"
    him surprised "There's these tiny white things on your hair. Man, they're really stuck on there good."
    kid "What? What are they?!"
    him "I don't know; here, go wash your hair in the sink and we'll see if that helps it go away."
    "She washed her hair, but the little white things were still there."
    him concerned "They look like little sesame seeds, or..."
    kid "Or what?!"
    him surprised "Eggs?"
    kid "Eggs?! From what?!"
    show her normal at quarterleft with moveinleft
    her concerned "Lice. We are currently experiencing an outbreak of lice."
    him annoyed "I thought we left all those horrible parasites back on Earth!"
    her annoyed "Yes, {b}we{/b} did. The miners, however, did not observe quite as strict decontamination protocols, and a few lice eggs made it through."
    him angry "How could that even happen?!"
    her concerned "My guess is that they didn't decontaminate clothing or toys thoroughly enough to kill lice. They are pretty resistant little bugs."
    kid "I have lice?!"
    her determined "Yes. I'm going to send out a community alert right now. [his_name], can you get started treating [kid_name]? I sent you a message with some instructions."
    menu:
        "What should I say?"
        "I'm not doing that.":
            $ marriage_strength -= 1
            him annoyed "No way. I'm not doing that."
            her angry "[his_name], I really need your cooperation. I need to concentrate on educating the community so we can kill all the lice on the entire planet."
            him "..."
            her flirt "Besides, you probably have them, too, and you'll need my help to get rid of them. I'm not sleeping in the same bed with you until you've been treated, too."
            him surprised "That's low."
            her determined "That's life."

        "Sure, I'll get started.":
            $ marriage_strength += 1
            him concerned "Okay, I'll get started."

    "I had never got rid of lice before. I got them once in school, but all I remember is my mom combing my hair a lot. I'd better read up on it."
    "But [her_name]'s instructions were pretty thorough."
    # TODO: include these?

    "First we queued up a lice comb to be 3D printed at the library."
    scene library with fade
    show pete at midright with dissolve
    show him normal at center
    show kid normal at midleft
    with moveinleft

    pete "Hey there, [his_name]. Hey, Travis, wanna say hi? [kid_name]'s here."
    travis "No!"
    pete "Think he's embarrassed about his new haircut."
    travis "Dad!"
    pete "Anyway, here's your comb."
    him concerned "Thanks for printing it for us."
    pete "Not a problem, I've got a batch of six more going right now. Got a feeling they'll be a hot item."

    scene farm_interior with fade
    show him determined at midright
    show kid sad at center
    with dissolve
    "We didn't have anti-lice shampoo or anything, so we just used some vinegar to help the eggs detach from the hair better."
    "Then I started to comb."
    "And comb."
    "...and comb."
    scene black with fade
    scene farm_interior with fade
    show him determined at midright
    show kid normal at center
    with dissolve
    kid "How much longer is this going to take?!"
    him "We have to be thorough! Otherwise we won't be able to get rid of them."
    kid "Can I play on the computer pad?"
    menu:
        "What should I say"
        "No, you'll move around too much.":
            him "No, you'll move around too much."
            kid "I won't!"
            him "Yes, you will. Now hold still!"
        "No, but why don't we put on a movie?":
            him happy "No, but why don't we put on a movie? I'm getting kind of bored, too."
            kid "Okay. Can I pick?"
            him determined "Just as long as it's not Zuppo."
            kid "Aw, man."
        "I guess.":
            him "I guess..."
            kid "Yay!"
            "It was hard to comb her hair properly when she was playing her game. I did my best, though."

    "Now that I knew about lice, my head kept itching. I wasn't sure if it was real or if I was just creeped out."
    him determined "I think that's it."
    show her normal at midleft with moveinleft
    her surprised "You got them all?"
    him concerned "I went through her whole head... that's all I can do for today."
    her determined "Good, now I'll take a look at your hair."
    "I sat on the stool and waited for the verdict. My scalp itched like crazy."
    her determined "Yup, you have them, too. Where's that comb?"
    "I sat down and she started combing my hair efficiently, dipping the comb in water to rinse off eggs and lice. It was pretty creepy seeing what had been living on my head."
    him concerned "What about you?"
    her surprised "Me? Oh, I'm just going to shave my head."
    him surprised "What?!"
    her laughing "Ha ha ha! You should see the look on your face!"
    him concerned "You're not going to shave your head, right?!"
    her determined "I don't think it'll come to that. You'll have to help me comb my hair, though. I can do some of it myself but I need your help to be thorough."
    him flirt "I can be thorough."
    her determined "Good, because all of us will need to be 100\% thorough if we want to rid our planet of these lice."
    him concerned "Maybe I should just shave my hair. I don't want to make more work for you."
    her surprised "Well, it's up to you. At least your hair would grow back pretty fast."
    menu:
        "What should I do?"
        "Shave your head.":
            him happy "You know what, I need a change anyway!  Let's shave it all off!"
            "I wasn't the only one -- at least half the men and boys shaved their heads. A few women did, too; can't say I blamed them."
        "Don't shave it.":
            him concerned "I just don't want to shave it. Sorry, [her_name]."
            her concerned "It's okay; I'll comb it for you. It'll still be easier to go through than mine."

    scene stars with fade
    "We repeated the combing process every day for a week. Even after that, we still combed each other's hair looking for any survivors every few days."
    "[her_name] said we needed to keep looking out for them for a few months."
    "It was amazing how these tiny insects took over our lives for a while. The whole community was pretty upset about it."
    nvl clear
    julia_c "I can't believe someone was so incompetent as to allow lice from Earth to contaminate our entire colony!"
    brennan_c "RET has discovered a mistake was made in the decontamination of personal items. Our procedures have been modified and we regret any inconvenience this mistake may have caused you."
    julia_c "{b}May{/b} have caused?!"
    martin_c "This isn't just an inconvenience; we lost a lot of valuable time during planting to these bugs. I had to plant tomatoes later than I wanted to; hopefully it won't get too cold before they're ripe."
    menu:
        "What should I say?"
        "I lost time, too. The miners should be held responsible for these damages!":
            him_c "I lost time, too. The miners should be held responsible for these damages!"
            julia_c "Exactly! They expect us to feed them, and then make us waste our precious time with these vermin! I have ten children to decontaminate!"
            $ miners -= 1

        "I know the lice are really annoying, but it's no one's fault.":
            him_c "I know the lice are really annoying, but we can't blame the miners. It was an accident."
            julia_c "A preventable accident! They expect us to feed them, and then make us waste our precious time with these vermin! I have ten children to decontaminate!"
            $ miners += 1

    miranda_c "Most of us aren't children anymore, Mom."
    julia_c "Do you have someone else who's willing to check your hair for lice?"
    miranda_c "..."
    julia_c "There's plenty of reasons to find a husband, and this is just one of them!"
    lily_c "Miranda and I can assist each other with this task so as not to overburden you."
    julia_c "Well, that's... that's very nice of you, Lily. Thank you. Though I still blame RET for this."
    brennan_c "For what it's worth, so do I. Despite the official statement they made me post up there, I'm spitting mad, too. I've got a lot of hair to comb through, here."
    pete_c "I'll take care of it."
    sara_c "You're offering to comb through Brennan's hair?! 😳"
    pete_c "Nah, I'll just shave it off. Give you a nice rugged look."
    brennan_c "Pete, if you really want to help a fellow out, make me another couple liters of that brew of yours."
    pete_c "If you've got the credits, I've got the brew."
    sara_c "Please don't let Pete cut your hair. I can give you a nice, short style that'll be easier to comb through. 🧑"
    brennan_c "I'm not cutting my hair. I just can't part with these luscious locks."
    nvl hide

    scene farm_interior with fade
    show him normal at midright
    show kid normal at midleft
    with dissolve
    kid "Can I invite Anya over to play next week?"
    "I was pretty sure the lice originally came from Anya. I wondered if they had brought any other parasites with them -- bed bugs, for instance."
    "But it wasn't the kid's fault. Probably."
    "And they would play together at school no matter what."
    him concerned "I suppose so."
    kid "Yay!"
    him annoyed "Now let me check your hair again."

    return

label family12_contact_parents:
    nvl clear
    him_c "Hey, is this Anya's parents? I'm Terra's dad, and she says Anya invited her over for tomorrow after school?"
    "Several hours later, I got a response."
    lewis_c "Yeah, that's okay."
    menu:
        "What should I write?"
        "Is an adult going to be there?":
            him_c "Is an adult going to be there?"
            lewis_c "Yeah."
        "Can Anya come over here instead?":
            him_c "Can Anya come over here instead?"
            lewis_c "Sure."
            call family12_anya_come_over
            return
        "When should I pick her up?":
            him_c "When should I pick her up?"
            lewis_c "Before dinner."

    nvl hide
    "I didn't have as many details as I wanted, but I told [kid_name] that she could go."
    call family12_anyas_house
    return

label family12_anyas_house:
    scene farm_exterior flip with fade
    "I decided to go over a little early to pickup [kid_name]. Maybe I could meet her parents."
    "But when I got there and knocked on the door, a teenager answered the door."
    "Anya and [kid_name] had been playing in the mud in the backyard, which was fine, but I wasn't sure if the teenager counted as a 'responsible adult' or not."
    "Besides, maybe [kid_name] was getting old enough that she didn't need adult supervision all the time?"
    menu:
        "What do I think?"
        "She still needs adult supervision.":
            $ demanding += 1
            "I decided she still needed adult supervision, especially when playing with friends. On her own, she'd probably be fine, but you get more than one kid together and they tended to get in trouble."
            "Maybe Anya could come play at our house in the future."
        "She'll be fine on her own.":
            $ responsive += 1
            $ confident += 1
            "I couldn't be there for [kid_name] forever. She needed to be ready to be without me or another adult, and she couldn't learn those skills without practicising them."

    "The whole walk home [kid_name] talked and talked about everything she and Anya did. It was pretty cute, actually."
    return

label family12_disobey:
    "The next day, [kid_name] was late coming home from school."
    him surprised "Where is that girl?"
    "After an hour, I started to get worried. Then I remembered what she had asked yesterday, and I started to get mad."
    "I called up Mr. Lewis on the radio."
    # TODO: radio interface
    him "Mr. Lewis? Is [kid_name] there?"
    "Mr. Lewis" "I just got home, but no, she's not here."
    him "Are you sure? She hasn't come home yet..."
    "Anya" "She just left to go home, dad!"
    "Mr. Lewis" "Oh. Apparently she just left."
    him "Thank you; that's good to know."
    "The sun was starting to go down, but by my calculations, [kid_name] still had at about an hour's walk ahead of her."
    "As long as she could find her way from the miner's camp to the town, she'd be able to find her way home pretty easily. It's not like there were a ton of other places to go or confusing roads."
    "But it was getting dark, and I kept picturing young Josephina's corpse from her funeral eight years ago..."
    menu:
        "What should I do?"
        "Go and meet [kid_name].":
            $ responsive += 1
            "I couldn't let her walk all that way alone in the dusk. She was only 7 years old."
            "I saddled Lettie and set out towards town."
            "I found her sitting on the community center steps, looking exhausted, and like maybe she had been crying."
            # TODO: setup this scene and blocking
            naomi "There he his now. See? Look how much he missed you."
            "[kid_name] looked up at me with worry in her eyes. Seeing that face, my anger ebbed away like a sand castle before the tide."
            him "Thanks for looking out for her."
            naomi "Oh, I think she's looking out for me. She stopped by just in time to help me carry a few things from the storehouse."
            kid "Sorry, dad."
            "She looked so sad, and a little afraid. Naomi leaned on my arm to whisper into my ear."
            naomi "Have a nice ride home and then decide what to do about her disobedience, won't you?"
            hide naomi with moveoutright
            him "Come on, [kid_name]. Let's go home."
            "[kid_name] sat behind me on Lettie, on a special pad we attached there for double riding. Her little arms wrapped around my waist and her face was pressed against my back."
            him "I guess you went to Anya's house?"
            kid "Yes."
            him "How was it?"
            kid "It was fun. But it was taking forever to walk home. My feet were hurting."
            him "Hmmm."
            "The rest of the ride home was quiet, as I thought about what I should do about [kid_name]."
            "Sister Naomi was right; when I took time to think about it, I had a lot more options than just yelling at her, which is what I had originally planned to do."
            "So, when we got home, I had decided what to say."

        "Wait here.":
            $ demanding += 1
            "She'd be fine. And the long walk might teach her a better lesson than my scolding ever could."
            "Though maybe I should scold her, too."
            "I got a message on my computer pad."
            naomi_c "I just sent [kid_name] on home; she stopped at my house to help me carry some things. Please don't be too mad at her."
            him_c "Thanks, Sister Naomi."
            "I tried to get some things done, but I kept checking down the road, looking for [kid_name]. Finally I saw her, walking wearily down the dirt path as the sun's last rays faded into night."
            "She trudged into the house and flopped down on the floor. I could tell she had been crying from the dusty tear tracks running down her face."
            kid "Sorry, dad."
            "I remembered what Sister Naomi said and bit back the angry rant I had started planning."
            him "Welcome home, [kid_name]."
            "I pulled her into a hug and just held her for a few minutes. She wasn't normally the snuggly type, but she stayed in my arms for several minutes."
            "Finally, I figured I'd better tell her what was going to happen."

    him "You disobeyed me and went to Anya's house anyway. Here's the consequences."
    menu:
        "What should I say?"
        "No playing with friends.":
            $ demanding += 1
            him annoyed "You can't play with friends until you've proven that you can be obedient. I expect you to come straight home from school and not have any friends over."
            kid "For how long?!"
            him determined "Until you've proven that you can be obedient, and I can trust you."
            kid "Hmph."
            "She wasn't happy about it, but she didn't argue, either."
        "You'll help me with my chores.":
            $ demanding += 1
            him annoyed "You'll need to do extra work with me on the farm until you've proven that you can be obedient. I expect you to do everything exactly as I've asked you. And if something's not clear, you need to ask"
            kid "For how long?!"
            him determined "Until you've proven that you can be obedient, and I can trust you."
            kid "You'll probably make me do super hard stuff like 'Hey [kid_name], weed this whole field.'"
            him normal "I won't ask you to do anything you can't do. But I do expect you to work hard."
            "She wasn't happy about it, but she didn't argue, either."
        "You need to apologize.":
            him annoyed "You need to apologize for what you did."
            kid "I did apologize!"
            "I just looked at her. She sighed."
            kid "Fine. Dad, I'm sorry I disobeyed and went to Anya's house when you said not to."
            him normal "Thank you. I forgive you. Please don't do that ever again."
        "All of the above.":
            $ demanding += 2
            him "You need to apologize, and instead of playing with friends you'll need to help out extra on the farm and do everything I ask."
            kid "For how long?!"
            him determined "Until you've proven that you can be obedient and that I can trust you."
            kid "You'll probably make me do super hard stuff like 'Hey [kid_name], go weed this whole field.'"
            him normal "I won't ask you to do anything you can't do. But I do expect you to work hard."
            "She wasn't happy about it, but she didn't argue, either."
    "After a week, she had worked pretty hard to obey everything I asked, so I started restoring priveleges."
    "I let her have Anya over after school one time."
    return

label family12_anya_come_over:
    scene farm_interior with fade
    show him normal at center
    show kid normal at midleft with moveinleft
    "[kid_name] was so excited to show Anya around our little house."
    kid "Here's the kitchen, and this is [bro_name]'s room, and the outhouse is out there and here's my room! Want to come in!"
    hide kid with moveoutright
    "[kid_name] didn't wait for a response, pulling Anya into her room where they sat down to make something out of yarn."
    him annoyed "Welcome home."
    "I guess they didn't need me, which was probably for the best."
    return




#####################################################
#
# BIG KID
#
#####################################################

# 8 Earth years old
# Sex Education
label family13:

    "Several months ago, we found out [her_name] was expecting again. We hadn't really planned for another baby... but we hadn't actively prevented it, either."
    "I guess I was getting used to having kids. When I looked back at the time before I was a father, it seemed so long ago."
    "It was hard to even remember when it was just [her_name] and me..."
    "We brought the kids to the clinic so that they could see their new sibling via ultrasound."
    scene clinic with fade
    show him normal at midright
    show her normal at center
    show kid normal at midleft
    show bro at quarterleft
    with dissolve

    her normal "So, if you look on the screen there, hopefully I can get a good angle so you can see the baby's face."
    # TODO: add ultrasound pic?
    him surprised "Was that it?"
    her concerned "Maybe? I don't think I'll ever get used to performing an ultrasound on myself..."
    him normal "You could have asked the nurse to help, right?"
    her normal "Yeah, but I wanted it to be just our family."
    kid "Is that a hand?"
    her happy "Yes! There's the baby - you can see the little mouth, and the hand."
    him "Wow, that really makes it seem real."
    her flirt "That's because it is real."
    bro "That's in your tummy?"
    kid "It's not her tummy, it's her uterus. Only girls have them."
    "[bro_name] looked disappointed."
    bro "Why?"
    him "Men and women have mostly the same parts, but a few different parts so they can come together and make babies."
    her "We still have a long time before this baby is born, but that's good. We need time to get ready!"
    bro "Babies cry a lot."
    him "Yeah, they don't know all sorts of awesome words like you do. But babies grow and learn, and when they know words they don't cry as much."
    kid "So how come [bro_name] still cries all the time?"
    bro "I do not!"
    her "I cry sometimes, too. Sometimes words just aren't enough."
    "I helped [her_name] put away the ultrasound machine, and we started to walk back home."
    scene path with fade
    "[bro_name] wanted to walk really slowly and look at all the flowers, but [kid_name] wanted to run, so [her_name] sent [kid_name] and I on ahead."

    scene fields with fade
    show him normal at midright
    show kid normal at midleft
    with dissolve
    kid "Dad, I have a question."
    him "What is it?"

    # TODO: Is this different based on earlier decisions?
    kid "So, you need a man and a woman to make a baby, right?"
    him "Right..."
    kid "Well, how, exactly, does that work? I mean, they come together, but... how?"
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
            him "Nothing. Ah, um, I'll race you home!"
            kid "Okay!"
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
                        kid "Grandma Grayson said that if we get some more sugar on the next shuttle we can make cookies."
                        him "You'll let me have one, right?"
                        kid "Sure, dad."
                        $ authoritative += 1
                        jump family13_end
            menu:
                "What should I tell her about sex?"
                "Tell her the physical mechanics." if not sex_ed_biology:
                    $ confident += 1
                    him "A man's penis can go inside the woman's vagina and the sperm comes out of it when they have sex."
                    kid "Oh."
                    "She thought about it for a minute."
                    kid "And that's how you and Mom made me?"
                    him "That's how."
                    "She looked away for a minute, and I could almost see her brain processing this new information."
                    kid "Are you sure?"
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
                    him "Sex is how babies are made, so it's kind of a big deal. You need parents who are going to stay together and work together to take care of the baby."
                    if (not sex_ed_biology):
                        kid "Okay, but what is it?!"
                    else:
                        kid "So it always makes a baby?"
                        him "No, not always. But that's how babies start. Not just humans, but animals, too."
                        kid "Like our baby goat? His parents had sex?!"
                        him "Well, with animals we usually call it 'mating', but, yeah."
                    $ sex_ed_babycreation = True
                    $ sex_ed_counter += 1
                    jump sex_ed
                "Explain how good it feels." if not sex_ed_goodfeeling:
                    him "It feels really good to have sex together."
                    if (not sex_ed_biology):
                        kid "Okay, but what is it?!"
                    else:
                        kid "Like... a hug?"
                        him "Kind of. But special. It makes you feel closer to the person you're with, so you want to make sure it's someone you love enough to be with forever."
                        kid "Forever?"
                        him "Well, that's how I feel. Some people don't look at it as that special, I guess. But your mom and I only share it with each other, so it helps us feel closer together."
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
                        kid "Like you and mom?"
                        him "Yeah! Like me and mom."
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
            kid "Will you take me hunting sometime soon? I looooove crabird meat. It's so good. I could eat it every day."
            # TODO: Make this a choice or dependent on choices?
            him "Yeah, let's go tomorrow morning before school. We'll get up early and catch them before they get warmed up."
            $ permissive += 1

label family13_end:
    scene black with fade
    "We were all excited for a new brother or sister in the family..."
    "...but [her_name] lost the baby."
    "I shouldn't put it that way; that makes it sound like she did it on purpose. Like she misplaced it, or left it outside too long."
    "It wasn't anything she did; sometimes these things just happen."
    scene farm_interior with fade
    show him concerned at midright
    show kid surprised at midleft
    with dissolve
    kid surprised "So mommy's not pregnant anymore?"
    menu:
        "What should I say?"
        "No.":
            him sad "No."
            kid sad "Oh."
            "She didn't ask me anything else, which was fine with me because I didn't want to talk about it, either."
            "I felt like maybe it was partly my fault; I should have let [her_name] rest more, or grown better food, or... something."
            "And if I felt that way, how did [her_name] feel?"
        "No, the baby died.":
            him sad "No, the baby died for some reason while it was inside Mom."
            kid "You don't know why?"
            him concerned "No. Sometimes these things just happen."
            "[kid_name] started crying."
            kid cry "I wanted a baby sister!"
            him sad "I know, sweetie. We all did."
            show kid at midright with move
            "She climbed up onto my lap. It was a tight fit now that she was getting bigger, but I held her close and we cried together."
            show bro at midleft with moveinleft
            bro sad "I'm sad, too."
            him determined "Come here. It's okay to cry."
            show bro sad at center with move
            "I tried to be strong for them, but I ended up sniffling too. [her_name] came out of the bedroom and sat next to us."
            show her sad at center behind bro,him with moveinleft
            "I put my arm around her and we all cried together."
            "I didn't know how to comfort them, or if I even should. There would be something wrong with us if we weren't sad about losing a baby."
            "Maybe the best thing to do was just mourn together."
        "No. It's hard for mom.":
            $ marriage_strength += 1
            him determined "No, she's not. And Mom is pretty sad and hurting a lot right now so let's do what we can to help her, okay?"
            kid "Okay..."
            him surprised "What can we do right now to help mom?"
            "She looked around. [her_name] was in our bedroom with the door closed. Hopefully she was taking a nap."
            kid sad "I can be quiet while she takes a nap."
            him normal "That's good. Do you think we can make dinner so quietly that we can surprise her when she wakes up?"
            show bro normal at midleft with moveinleft
            show kid normal at center with move
            kid normal "Yeah! Let's make something she likes!"
            bro normal "I can help!"
            him happy "Okay, but we gotta be real quiet, okay? Like ninja chefs!"
            "I cringed every time [kid_name] banged a pot or when [bro_name] dropped the silverware while trying to set the table."
            "[her_name] probably didn't have the best nap, but when she got up..."
            her surprised "What's all this?"
            kid happy "We made you dinner!"
            bro normal "We're ninja chefs!"
            him sad "We wanted to try to cheer you up."
            her sad "Oh, you guys..."
            "She burst into tears, but they weren't all sad tears."
            him concerned "Hey, hey."
            her concerned "I don't deserve you guys."
            him normal "I know; you deserve way better! But it's not about deserving. We're a team, right? So we help each other!"
            bro happy "Team Ninja Chefs!"
            kid annoyed "No, that's dumb. We should be team Foodalicious!"
            him happy "How about Team Let's Eat This Food Before It Gets Cold?"
            kid normal "Da-ad."

    call bedroom_scene
    her concerned "I'm sorry..."
    him concerned "Hey, hey, it's not your fault."
    her sad "Maybe if I hadn't worked so hard, or eaten better food, or..."
    him determined "You're a doctor; you know sometimes these things just happen."
    her serious "Just because we don't know the cause doesn't mean there isn't one!"
    menu:
        "What should I say?"
        "You did your best.":
            $ marriage_strength += 1
            him sad "You did your best -- that's what matters."
            her surprised "But what if 'my best' just isn't good enough?"
            him normal "It's good enough for me."
        "You can't think that way.":
            $ marriage_strength += 1
            him angry "You can't think that way! You'd have to be a god to know enough to be able to prevent everything bad from happening."
            her sad "But I should at least be able to keep my kids alive."
            him determined "Not everything is under your control. Or mine, either."
            her concerned "I know. But sometimes I feel like it should be."
        "I love you.":
            $ marriage_strength += 1
            him determined "I love you. I've seen you working hard for everyone, seen the love you pour into our family, and I'm amazed. You give so much."
            her sad "But it's not enough!"
            him normal "It's enough. You did all you could."
        "It's my fault, too!":
            him annoyed "Then maybe it's my fault! I should have let you rest more, taken care of the kids more, and then you wouldn't have had to!"
            her sad "No, of course not!"
            him concerned "Then it's not your fault, either."
            her "..."
            him "..."
        "(Don't say anything)":
            "I didn't know how to respond. I worried that anything I would say would just make things worse."
            "I listened to her sob quietly into her pillow. I reached over to give her a hug, but she got out of bed and went outside."
            "Maybe she just needed to grieve by herself."
            return
    "I gave her a tissue for her nose, and then held her close. We both grieved, but at least we could share our grief with each other."

    return

# 8.7 Earth years old
# Teacher Troubles
label family14:
    scene farm_interior with fade
    show kid angry at midleft
    #show bro crying at quarterleft with dissolve
    show him normal at midright with moveinright

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
            him determined "..."
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
            him "Everyone?"
            kid "Especially teachers!"
        "(Say nothing)":
            him determined "..."
            "I put my arm around her, trying to show her that I was there for her. Words just weren't good enough."
            "She didn't lean into me, but she didn't push me away, either."
            kid "I just wish everyone would stop telling me what to do!"
            him surprised "Is there someone in particular?"
            kid "My teacher is so mean."

    him surprised "Isn't telling you what to do kind of your teacher's job?"
    kid "No! She's supposed to be teaching me useful things like math and reading, not making me do busy work all day!"
    menu:
        "What should I say?"
        "You need to listen to your teacher.":
            $ demanding += 1
            him determined "She's your teacher. She knows what she's doing, and you need to respect her and obey her."
            kid "Even if she's wrong?"
            him angry "Yes! You're the kid; your job is to obey! She's the adult; her job is to teach."
            kid "Why am I even talking to you about this?!"
            him annoyed "I'm trying to help you."
            kid "No, you just want to make me do what you want!"
            him angry "The only things I want you to do are things that are good for you!"
            kid "It feels like everyone's just being mean. Everyone hates me."
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
                    "I got right up in her face and gripped her arms, tightly so she couldn't wriggle away."
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
            him determined "Tell me about it."
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
                    him determined "You need to listen to your teacher."
                    kid "But she's wrong!"
                    him concerned "Maybe so, but she deserves a certain amount of respect."
                    him determined "And so does your brother."
                    kid "And so do I!"
                    him annoyed "You'll need to apologize to your teacher and your brother, and you won't be able to use the computer pad for games or play with friends this week."
                    $ authoritarian += 1
                    "She didn't like it, but she did what her teacher asked. She still had problems with hitting her brother, so she wasn't able to play with friends or use the computer pad for a long time."
                    "How long would it take for her to get the message?!"
                    return
                "What did you want to do instead?":
                    him surprised "What did you want to do instead?"
                    kid "Read my book."
                    him determined "Well, spelling is still something you should study. Does this happen all the time?"
                    kid "Yes."
                    him concerned "Maybe we could ask if you could do a higher level of spelling words?"
                    kid "Ugh, that'd be even more work!"
                    him normal "It'd be less boring."
                    kid "I guess. I still don't want to write them ten times. My hand gets sore. And what's the point of writing by hand, anyway? You and mom never write by hand. It's a waste of paper."
                    him happy "One problem at a time, [kid_name]. Let's send your teacher a note. Do you want to type it, or write it."
                    kid "Type it!"
                    "We wrote to her teacher, and Terra asked if she could have harder spelling words and type them instead of handwrite them."
                    "I wasn't sure what her teacher would say, but at least I helped Terra with her problem at school."
                    him determined "Now, there's one more thing."
                    kid "What's that?"
                    him annoyed "You hit your brother. How can you make it up to him?"
                    kid "How is he going to make it up to ME for annoying me?!"
                    him concerned "Don't worry about what he will do; you just decide what you will do."
                    kid "I'm supposed to do something nice for him when he's been annoying me all afternoon?!"
                    him annoyed "I expect you to apologize to him and do something kind for him."
                    kid "I can't do that!"
                    him normal "I'll ask you later tonight and you can tell me what you chose."
                    kid "Ugh. Fine. But you should also ask {b}him{/b} to stop annoying {b}me{/b}!"
                    "That's what she said, but at dinner she set the table for [bro_name], and I heard her mutter 'sorry' to him, too."
                    "It's not the shiny happy ending  I wanted, but maybe she learned something?"
                    "At least we worked things out with her teacher."
                    $ confident += 1
                    $ authoritative += 1
                    return
        "You're just whining.":
            him "Quit whining and don't hit your brother."
            kid "But...!"
            "I left before she could complain more. What more needed to be said?"
            $ neglectful += 1
            $ confident += 1
            return

    return

# 9.4 Earth years old
# Allowance?
label family15:
    scene farm_interior with fade
    show him normal at midright
    show kid normal at midleft
    # TODO: Modify allowance_amount based on this event and do something with it.
    kid "Dad, I need some money. Can I have an allowance?"
    him happy "[kid_name], I have no problem with ants. I already 'allow ants.'  Get it??"
    kid "Ha ha. That doesn't even make sense. So can I?"
    menu:
        "What should I say?"
        "Why do you want an allowance?":
            $ responsive += 1
            him surprised "Why do you want an allowance?"
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
                    kid "No, but I really really really really really really want them! Do I need to say 'really' more times? Maybe a googol times?"
                    kid "Really really really really really really..."
                    him annoyed "I think I get the picture."
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
            kid "You should go to your room. Dad, you just hate me!"
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
            her annoyed "Why not? You do."
            him "...Fine, whatever, as long as you handle it."
            # TODO: should this end differently?

            return
        "No.":
            $ responsive -= 1
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
    $ confident += 1
    "(This is tricky... what kind of allowance should I give her?)"
    menu:
        "What should I say?"
        "Make a proposal.":
            $ demanding += 1
            him "You'll need to write up a budget proposal."
            kid "A budget proposal? I don't know how to do that!"
            him "Yup. List your expenses, why you think you should have them, and then list possible sources of income."
            kid "That'll be a lot of work!"
            him "Getting money always takes work."
            kid "Can't you just give me some money?!"
            him "Nope. If you really think you should have an allowance, convince me with a written proposal."
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
            kid "But you never think I'm 'good'! Even when I try really hard and do nice things for everyone and don't hit [bro_name] and do extra chores you never even notice!"
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
    "The way my kids grew up was pretty different from how [her_name] and I grew up on Earth. They never experienced things like grocery stores, school fundraisers, football games, or trains."
    "But some things were pretty similar to my own childhood."
    him annoyed "Yes, you need to clean your room today."
    kid "But I like it messy! It feels comfortable and I know where everything is!"
    him determined "Really? Where's your hairbrush?"
    kid "I... I could find it if I had to!"
    him annoyed "You have to. Right now."
    kid "Ugh, I know where everything {b}else{/b} is!"
    him surprised "How can you even have this much stuff? Where did this all come from?"
    kid "I like to collect things."
    him annoyed "Can't you just pick one thing? I mean, you have shells, rocks, and bottlecaps. And that's not even counting every school art project you've ever made, old plastic containers from rations, and -- what {b}are{/b} these?"
    kid "It's my origami zoo!"
    him surprised "Didn't you make that like five years ago?"
    kid "Yes, and I still love it!"
    kid "Besides, it's not like we can get new things all the time. Every thing is precious."
    menu:
        "What should I say?"
        "Clean it up or be grounded.":
            $ demanding += 1
            $ confident += 1
            him determined "You need to clean it up right now or you'll be grounded."
            kid "Right now?!"
            him annoyed "Yes, right now."
            "I left her to clean it up. She's a big girl now; she doesn't need my help to clean her room."
            "When I came back, it was pretty clean..."
            "...until I looked under her bed."
            "She had just shoved everything under there."
            him angry "[kid_name]!"
            kid "What?"
            menu:
                "What should I do?"
                "Tell her to clean it up and she's grounded.":
                    him angry "That's it, you're grounded. Also, clean this up right now!"
                    kid "I don't know how!"
                    him annoyed "Well, you better figure it out quick. You have one hour."
                    kid "Or what?!"
                    him determined "Do you want to find out?"
                    "Tears sprang to her eyes, but I had no pity. It's not like I was asking her to do something hard; just make her room neat. She had to learn."
                    $ authoritarian += 1
                "Ask her to fix the problem":
                    him determined "What do you need to do here?"
                    kid "What? The room is clean."
                    him determined "When I say 'clean', I don't mean 'everything under the bed'. I expect every item to be in a container that is meant for that specific type of item."
                    kid "That'll take forever!"
                    him "It might take a while, but I know you can do it."
                    kid "I just... I don't know where everything goes!"
                    him "Let me help you. Let's break it down one thing at a time."
                    "I spent several hours helping her organize her room. Hopefully she could do it better on her own next time."
                    $ authoritative += 1
                "Just throw it all away.":
                    $ responsive -= 2
                    "I didn't say anything. I just took it all out back and dumped it in a pile."
                    "Some of it could probably be recycled, but why should that be my job?"
                    "Then I lit it on fire."
                    "[kid_name] came running out and screamed when she saw the blaze."
                    kid "No! Stop! I'll clean it up!"
                    him determined "If you won't take care of your things, then you don't get to have things."
                    kid "You are the worst dad ever!"
                    him annoyed "Also, you're grounded. You didn't do what I asked and you spoke to me rudely."
                    "She burst into tears."
                    "When [her_name] came home, [kid_name] sobbed out the entire story to her. [her_name] didn't say anything, but she shot me an angry look over the top of [kid_name]'s head."
                    "After [kid_name] cried herself to sleep, [her_name] turned to me."
                    her annoyed "You burned all her things?"
                    him determined "She wouldn't clean her room. It was just a bunch of junk, anyway."
                    her angry "It wasn't junk to her!"
                    him angry "Well, she should've taken better care of it!"
                    her annoyed "Well, it'll be hard for her to learn how now that she doesn't have anything to take care of."
                    him annoyed "I think she learned her lesson."
                    her angry "She learned that she can't trust you! She learned that you don't care about her at all! Just about satisfying your own ego."
                    him angry "This isn't about me!"
                    her concerned "You can't even see it, can you?"
                    him determined "All I see is a spoiled little girl who maybe finally learned a lesson."
                    her serious "I wish we could've talked about it together before you did that."
                    him annoyed "Yeah, well, you weren't here."
                    her sad "..."
                    him annoyed "..."
                    $ authoritarian += 1

        "I won't make you clean it.":
            $ responsive += 1
            him concerned "I guess it's not hurting anyone for you to keep this stuff around..."
            kid "Yeah, it'd be a waste of time to clean it up. It'd just get messy again, right?"
            him determined "Yeah..."
            "Mostly I just didn't have the energy to make her do anything about it. And, it wasn't that important, right?"
            $ permissive += 1
        "I'll help you organize them.":
            $ responsive += 1
            him determined "It sounds like you don't know where to start. I'll help you organize this stuff."
            kid "I guess, if you really want to."
            "I spent about two hours sorting through little bags and boxes and bins full of random items that I didn't even know we had."
            "We used the old food containers to organize it into some kind of order."
            him "Now it's your job to make sure it stays organized."
            kid "Why? It'll just get messy again."
            him "Not if you maintain it!"
            kid "I don't think that's going to happen."
            menu:
                "What should I do?"
                "Hold her accountable.":
                    $ demanding += 1
                    $ confident += 1
                    him determined "Well, every week we'll check on your room. If you've kept it organized, you won't have any work to do. If it's gotten messy, you'll need to clean it by yourself."
                    kid "All by myself!"
                    him normal "If you're going to keep all these things, then you're responsible for keeping them organized. I'll help you by checking on it each week."
                    kid "Ugh, what a pain."
                    him determined "If you need help figuring something out, I'll help you. But if you don't keep things organized, then I will give them away."
                    kid "You're so mean!"
                    him normal "Let me know if you need any help, okay?"
                    $ authoritative += 1
                "Do this again next time.":
                    him normal "Then I'll help you clean it again."
                    kid "Okay, if you really want to."
                    $ permissive += 1
        "Maybe you could share some of it?":
            $ demanding += 1
            him surprised "Maybe you could give some of it away?"
            kid "Give away my precious things?!"
            # TODO: change depending on favorite faction?
            him determined "Not all of them, but I know Travis and his family don't have access to all the stuff at the storehouse or the printers anymore."
            kid "Give away my precious things to {b}Travis{/b}?!"
            him normal "Maybe his little sister."
            kid "She does like animals..."
            him concerned "She would probably play with it more than you do..."
            kid "Well, maybe I can give a few things away, but not everything!"
            him "Okay, let's make some piles. We'll give some things away, and the stuff you want to keep we can organize so you can find things better."
            kid "I don't need to be able to find things better."
            "I ignored her and just got started."
            $ authoritative += 1
        "I don't care.":
            $ confident += 1
            him annoyed "I don't actually care. It's your room, whatever."
            kid "Yeah, exactly."
            $ neglectful += 1

    "That night after dinner, [bro_name] was quiet."
    him surprised "What are you thinking about, [bro_name]?"
    bro "I miss Sister Naomi."
    him surprised "You do?"
    "The whole community was saddened by her death, though none of us were really surprised."
    bro "Yeah...We used to always stop by her house after school and she'd have an apple or piece of bread for us. Sometimes she even had candy."
    kid "I miss her, too."
    bro "Where'd she go?"
    menu:
        "What should I say?"
        "She's in heaven.":
            him "She's in heaven."
            kid "Where's that?"
            him "I don't know. But it's where you go when you die, if you lived a good life."
            bro "What if you didn't live a good life?"
            menu:
                "What should I say?"
                "Then you go to hell.":
                    him "I guess then you go to hell."
                "I don't know.":
                    him "I don't know; don't worry about all that stuff."
                "Then you keep learning until you can go to heaven.":
                    him "I don't know how it all works, but what I'd do is make it so people could keep trying, learning all they needed to, until they were good enough to go to heaven."
                    her "If you were God?"
                    him "Well, God's at least as smart as me, so I'm sure He's come up with something good."

        "She's in our hearts.":
            him "She's in our hearts."
            kid "Her body's turning into the tree we planted, and trees give off oxygen. So when we breathe in the oxygen, our lungs take it to the heart and it goes in our blood."
            bro "Wow, she really is in our hearts!"
            menu:
                "What should I say?"
                "I didn't mean it like that.":
                    him "I meant that our memories of her and the things she taught us live on."
                    her "Oh. Well that's boring."
                "True enough.":
                    him "I guess that's true, too."
                "Good metaphor.":
                    him "That's a good metaphor, [kid_name]. Even though she's gone, her influence lives on."
                    kid "In our blood!"

        "She's gone.":
            him "She's gone. Every part of her is in the ground under that tree."
            "[her_name], who had been pretty quiet, spoke up."
            her "I don't know about that. It's possible her consciousness is separate from her body and still lives on."
            him "I doubt it."
        "I don't know.":
            him "I don't know."
            her "I believe some part of her, the part of her that thinks and feels and loves, lives on separate from her body."
            kid "But we can't see it?"
            her "Right. Just like love, or hope, or even radiation, we can't see it but that doesn't mean it's not there."
            bro "Do you think she's watching us now?"
            her "Maybe. But knowing her, she's probably busy helping someone and doesn't have time to spy on us all day."
            kid "Ha ha, that'd be funny if she was spying on us. Hi, Sister Naomi, I'm being good, you can stop spying on me now!"
            bro "Maybe she's helping our baby that died."
            her normal "What a nice thought. Maybe she is."

    return


# 10.5 Earth years old
# Sibling fighting; Unexplained crying
label family17:
    "I know parents aren't supposed to have favorite kids, but..."
    menu:
        "[kid_name] was my favorite.":
            "[kid_name] was my favorite. She was so expressive and dramatic and full of life. She always wanted to talk to me."
            "Sure, when she was angry, she was a volcano! But she'd also still snuggle up to me and tell me she loved me."
            "I also loved [bro_name], of course. But he was content to do things quietly, by himself, so I didn't spend as much time with him."
        "[bro_name] was my favorite.":
            "[bro_name] was my favorite. He was so much easier and was content to do his own thing, instead of bugging me and getting in trouble all the time."
        "I refused to even think about having a favorite kid.":
            "No. I wasn't going to allow myself to have a favorite kid. I loved them both, even though they were very different."
            "[kid_name] was always expressive and loved to talk and have people pay attention to her."
            "[bro_name] was a lot quieter. He was happy just doing his own thing most of the time."

    "But even he had problems sometimes."
    scene farm_exterior with fade
    show him normal at center with moveinright

    "I came back from working one day to hear loud wails emanating from the house."
    him surprised "Is that... [bro_name]?"
    "I also heard some shouting."
    kid angry "Stop crying! Be quiet! You're giving me a headache!"
    "The weeping just got louder."
    kid sad "Stop, you're going to get snot all over my bed! What's your problem, anyway?!"
    menu:
        "What should I do?"
        "Hurry and go help.":
            $ responsive += 1
            "I quickened my pace and, just before I entered the house, overheard [kid_name] yelling."
            kid angry "Get- Off- My- BED!"
            "There was a loud THUMP - probably the sound of [kid_name] pushing [bro_name] off her bed and onto the floor."
            bro "Owwwww! Wahhhhhhh!"
            him determined "Stop!"
        "Leave them alone.":
            $ responsive -= 1
            $ demanding -= 1
            $ confident += 1
            "I didn't want to get in the middle of that mess. I decided I had some more work I really should get done before I went home."
            kid angry "Get- Off- My- BED!"
            "There was a loud THUMP - probably the sound of [kid_name] pushing [bro_name] off her bed and onto the floor."
            bro "Owwwww! Wahhhhhhh!"
            "The wailing increased in volume and I decided this was not a problem that was going to solve itself."
        "Listen some more.":
            $ demanding += 1
            "I decided to eavesdrop a bit to find out what was going on."
            kid angry "Get- Off- My- BED!"
            "There was a loud THUMP - probably the sound of [kid_name] pushing [bro_name] off her bed and onto the floor."
            bro "Owwwww! Wahhhhhhh!"
            "The wailing increased in volume and I decided I'd better go in."

    scene farm_interior with fade
    show bro sad at midright, squatting
    show kid angry at center
    with dissolve
    show him normal at midleft with moveinleft

    him surprised "What's going on here?"
    kid sad "[bro_name] keeps crying and he won't stop or even tell me what's going on and he's making a huge mess!"
    "[kid_name] was almost as upset as [bro_name], who was still crying uncontrollably. His face was red and snot streamed down from his nose."
    menu:
        "What should I do?"
        "Get [bro_name] a handkerchief.":
            $ responsive += 1
            "I didn't say anything, just got a handkerchief for [bro_name] and handed it to him. He wiped his nose, and soon the handkerchief was completely saturated."
            "I got a few more, and sat by him as he continued to cry."
            kid "What's wrong with him?! We just came home from school and when he saw the bread was gone he freaked out!"
        "Ask [kid_name] for more details":
            him concerned "How did this start?"
            kid cry "I don't know! We just came home from school and we were going to have a snack but there wasn't any bread and he started freaking out."
        "Tell [bro_name] to be quiet.":
            $ demanding += 1
            him determined "[bro_name], you need to stop crying."
            "He just wailed even louder."
            kid annoyed "What's wrong with him?! We just came home from school and when he saw the bread was gone he freaked out!"
        "Ask [bro_name] what's wrong.":
            $ responsive += 1
            him concerned "What's wrong, [bro_name]?"
            bro "There's (sniff) no (sniff) bread!"
            kid annoyed "He's been like that since we got home from school."
        "Chastise [kid_name] for pushing [bro_name].":
            $ demanding += 1
            him determined "[kid_name], you shouldn't have pushed [bro_name] off your bed."
            kid angry "I already asked politely like a hundred times! He shouldn't be on my bed, anyway!"
            "It was true -- her pillow was all wet."
            him annoyed "What started all of this?"
            kid annoyed "We just came home from school and he saw the bread was all gone and he completely freaked out."

    him determined "[her_name], let me help [bro_name] on my own. You just go and do your homework. He'll be okay."
    kid annoyed "I don't know how I'm supposed to get any homework done with that racket."
    him annoyed "Then go to the library, or the clinic, or wherever you need to, okay?"
    "She sighed. I wasn't sure if she was just annoyed at the inconvenience, or if she was really worried about [bro_name], but she took the computer pad and left."
    hide kid with moveoutleft
    "I turned my attention to [bro_name], who was working his way through handkerchief number three."

    $ cry_duration = 0
    $ family17_think = False
    $ family17_ask = False
    $ family17_yell = False
    $ family17_sit = False
    menu family17_cry_loop:
        "What should I do?"
        "Think about it from [bro_name]'s point of view." if (not family17_think):
            $ responsive += 1
            "It wasn't that unusual for us to be out of bread; we didn't have it all the time. But [bro_name] did really like it."
            "I had eaten the last two pieces with my lunch. Maybe he had been looking forward to eating them?"
            "That didn't seem worth throwing a fit about, though... maybe something happened at school?"
            $ family17_think = True
            $ cry_duration += 1
            if (cry_duration >= 2):
                jump family17_after_cry
            else:
                jump family17_cry_loop
        "Ask him what happened at school." if (not family17_ask):
            him surprised "Did something happen at school?"
            "It was like he didn't even hear me. He just kept crying."
            $ family17_ask = True
            $ cry_duration += 1
            if (cry_duration >= 2):
                jump family17_after_cry
            else:
                jump family17_cry_loop
        "Yell at him." if (not family17_yell):
            $ responsive -= 1
            $ demanding += 1
            him angry "Quit crying and tell me what's wrong! I can't help you if you won't talk about it!"
            "He just cried even louder."
            $ family17_yell = True
            $ cry_duration += 1
            jump family17_angry
        "Just sit quietly with him." if (not family17_sit):
            $ responsive += 1
            "I didn't know what to do, so I just sat down next to him."
            "I patted his back. That's supposed to be reassuring, right?"
            "..."
            "After a few minutes, he was still crying."
            $ family17_sit = True
            $ cry_duration += 1
            if (cry_duration >= 2):
                jump family17_after_cry
            else:
                jump family17_cry_loop

    label family17_after_cry:
        him concerned "Hey, I want to help you. Whatever the problem is, we can fix it."
        bro "I want (sniff) bread!"
        "At least he was talking now. Maybe we were making some progress?"
        him surprised "Bread? Really? This whole thing is just about bread?"
        bro "I really like it! I wanted to have it when I got home! But it was all gone.  Wahhhhhhhh!"
        $ family17_apologize = False
        $ family17_acknowledge = False
        $ family17_tell = False
        $ family17_ask = False
        $ sniffle_duration = 0
        menu family17_sniffle_loop:
            "What should I do?"
            "Apologize for eating it." if (not family17_apologize):
                $ responsive += 1
                him sad "I'm sorry -- I ate it for lunch. I didn't know you wanted it."
                bro "I want bread!"
                $ family17_apologize = True
                $ sniffle_duration += 1
                if (sniffle_duration >= 2):
                    jump family17_after_sniffle
                jump family17_sniffle_loop
            "Acknowledge his feelings." if (not family17_acknowledge):
                $ responsive += 1
                him sad "You were pretty disappointed when you came home and the bread was gone, huh?"
                "He nodded."
                $ family17_acknowledge = True
                $ sniffle_duration += 1
                if (sniffle_duration >= 2):
                    jump family17_after_sniffle
                jump family17_sniffle_loop
            "Tell him to accept facts."  if (not family17_tell):
                $ demanding += 1
                him determined "Well, the bread's gone, and that's all there is to it. Crying won't bring it back."
                bro "But I want bread!"
                $ family17_tell = True
                $ sniffle_duration += 1
                if (sniffle_duration >= 2):
                    jump family17_after_sniffle
                jump family17_sniffle_loop
            "Ask what this is really about."  if (not family17_ask):
                $ demanding += 1
                him annoyed "[bro_name], you can't be this upset about bread. That's just not that important. What's really going on here?"
                bro "It's important to me!"
                $ family17_ask = True
                $ sniffle_duration += 1
                if (sniffle_duration >= 2):
                    jump family17_after_sniffle
                jump family17_sniffle_loop

    label family17_after_sniffle:
        "He was finally starting to calm down a bit. I guess maybe he just needed someone to listen to him? Or maybe he just had to let it all out." # TODO: some way to ask about this in parenting class? or research it in a parenting manual (tantrums vs meltdowns)?  Some options only available if you've read the right database entry?
        him concerned "I'm glad you're calming down; now we can work on solving the problem."
        bro "I can have some bread?"
        menu:
            "What should I say?"
            "I will find you some!":
                $ responsive += 1
                him determined "[bro_name], I can tell this is super important to you. So I'm going to go out there and find you some bread, no matter what it takes!"
                bro "Really?"
                $ permissive += 1
                jump family17_quest

            "Let's work something else out.":
                him normal "Well, we're all out. But we have plenty of other food."
                bro "But I really want bread!"
                him surprised "We have applesauce and potatoes and even some crabird jerky - don't you want some of those?"
                bro "No. They aren't bread."
                him annoyed "We don't have bread all the time. Sometimes you just have to eat other things."
                "He started crying again."
                bro "I want bread!"
                menu:
                    "What should I say?"
                    "No bread. Eat something else.":
                        him determined "We have no bread. Eat something else."
                        bro "Wahhhhhhhh!"
                        "He was getting way too upset about this. Maybe he just needed some time alone."
                        $ neglectful += 1
                    "You're so spoiled!":
                        him angry "You're so spoiled! You can't just expect to eat whatever you like every day!"
                        bro "Wahhhhhhhh!"
                        "His wailing was so obnoxious, I now understood how [kid_name] had felt. It made me furious."
                        jump family17_angry
                    "If you want it so badly, you can go find some.":
                        him angry "If you want bread so badly, you can go and find some! I don't have time to coddle you."
                        bro "Wahhhhhhhh!"
                        $ authoritarian += 1
                    "If it's that important to you, then let's go find some.":
                        him concerned "I guess if it's that important to you, we can try and find some."
                        bro "Really?"
                        jump family17_quest
                $ confident += 1
                "I left him alone and went back to work. His wails followed me to the fields. Even when I was out of hearing range, they pounded in my head like a hammer of guilt."
                "When I checked on him an hour later, he was asleep."
                him surprised "What was that all about?"
                "Kids were impossible to understand, sometimes."
                return

            "I'll help you get some.":
                $ responsive += 1
                $ demanding += 1
                $ confident += 1
                him determined "I'm not going to do it for you. But if you really want bread, I can help you figure out a way to get some."
                bro "How?"
                him "An adventure!"
                bro "Really?"
                $ authoritative += 1


    label family17_quest:
        # TODO: crop consequences
        him determined "Yup. QUEST ACCEPTED!"
        $ renpy.notify("Quest Accepted: Find [bro_name] some bread!")
        bro "Can I come?"
        him normal "Of course! If we're going on a quest, we need a party of adventurers! And perhaps a noble steed!"
        "I threw a water bottle and some crabird jerky in my pack and we set off."
        scene barn with fade
        show lettie at midright with dissolve
        show him normal at midleft
        show bro at quarterleft
        with moveinleft
        him determined "Come, noble steed! We embark on a quest to satiate the hunger of this innocent boy!"
        bro "With bread!"
        "We saddled her up with a pad behind the saddle for [bro_name] to sit on. He held on tight to my waist and we set off for town."
        bro "Where are we going to find bread?"
        him surprised "Someone in town probably has some... but who?"
        menu:
            "Who should I ask about bread?"
            "Ilian, the storehouse manager":
                "I cringed, but I thought grumpy old Ilian would probably be the most likely to have bread."
                scene storehouse with fade
                show ilian at midright with dissolve
                show him normal at midleft
                show bro at quarterleft
                with moveinleft
                him normal "Ilian! How are you?"
                "He sighed, got up from the cans he was organizing, and came over to the counter."
                ilian "What do you want?"
                him surprised "Doesn't anyone ever come here just to hang out with you?"
                ilian "No."
                him normal "Huh. We should fix that sometime."
                ilian "Please don't. Just tell me what you want so I can get back to work."
                him determined "We need some bread!"
                "I patted [bro_name] on the head, but he clung to my leg timidly. I could see why; Ilian was scowling at us like we were a couple of weevils."
                ilian "Bread, huh? Not wheat?"
                him normal "Nope. It's gotta be bread."
                ilian "Don't have any."
                him surprised "You don't have any bread?"
                ilian "Of course not. Bread doesn't keep more than a few days. I could sell you some wheat if you want to make your own."
                "I checked the time. It was getting late. We didn't have time to look anywhere else, especially since the farms were so spread out."
                him determined "Guess we'll be making our own bread, then."
                "I paid Ilian for the wheat, and also some yeast. We only had one farm growing wheat and it was in high demand, so it was pretty expensive. The bread from this morning was a gift from one of [her_name]'s patients."

            "Pavel Grayson, the mayor":
                "Mayor Grayson knew everyone. He would probably have some idea."
                scene community_center with fade
                show pavel sad at midright with dissolve
                show him normal at midleft
                show bro normal at quarterleft
                with moveinleft
                "When I went to see him, though, he looked so haggard and forlorn that I almost turned right around."
                "Ever since his wife died about two years ago, he hadn't been the same."
                him surprised "Mayor Grayson! Hey, how are you doing?"
                pavel normal "Oh, it's [his_name]. Yes, I'm fine. And you? I see you brought young, ah, your young son along with you."
                "I didn't blame him for not remembering [bro_name]'s name. The community was growing while the mayor's memory was weakening."
                bro "Dad and I are on a quest!"
                pavel sad "Are you, young fellow? Isn't that wonderful, to spend that time with your father..."
                "He trailed off, a faraway look in his eyes."
                bro "Do you miss Sister Naomi?"
                pavel "Sorry, what's that?"
                menu:
                    "What should I do?"
                    "Shush [bro_name]":
                        him annoyed "[bro_name]! Don't ask him that!"
                        pavel "Now now, [his_name]. I like to run a transparent government! You can ask me anything, [bro_name]."
                        bro "I just wondered if you were thinking about Sister Naomi."
                    "Let [bro_name] talk.":
                        bro "I just wondered if you were thinking about Sister Naomi."

                pavel normal "Oh yes, very much. I can almost feel her right next to me, though, sometimes..."
                bro "Like a ghost?"
                pavel "Perhaps a bit like a ghost. Or a powerful memory."
                bro "She made the best candy."
                pavel "She did, didn't she! I couldn't eat any of it, of course, with my diabetes, but when she'd make it I'd just inhale the scent and that was almost as good."
                bro "She even smelled like candy."
                pavel sad "Yes, now that you mention it, that's exactly what she smelled like. So sweet..."
                "I was worried we were bothering the Mayor by talking about his dead wife so much, but he didn't seem upset. Even as tears glistened in the corners of his eyes, he had a fond smile on his face."
                him concerned "..."
                pavel normal "But, you didn't come here to reminisce with me! What brings you to my office?"
                "I had almost forgotten about the bread. It seemed a little silly, now."
                menu:
                    "What should I say?"
                    "Nothing, just wanted to say hi.":
                        him normal "No reason. We just wanted to see you and say hi."
                    "We're searching for some bread.":
                        him determined "[bro_name] really wants some bread to eat, but his selfish dad ate it all for lunch."
                        pavel "Some bread, eh?  I see..."
                        bro "Do you have any?"
                        pavel "No, I don't. You could check with the wheat farmers, but they'd probably charge a high price for it."
                        him normal "Okay, thanks Mayor."
                pavel "You should come by more often - maybe on your way home from school, [bro_name]?"
                bro "You don't have candy, do you?"
                pavel "Ha ha ha, no, I don't have candy. But I'll see if I can find something good for you. And we can remember Naomi, together."
                bro "Okay."
                "As we left, the sun was setting. It was too late to go anywhere else, so we headed home."

            "Pete, leader of the luddites":
                him determined "Let's go ask Pete."
                bro "Mister Pete is scary."
                him surprised "What, really? Pete?"
                bro "Yeah. He yelled at me one time when I was walking too close to his cows."
                him concerned "Yeah, he... Pete doesn't like people interfering with him."
                bro "Is he going to yell at us if we ask for bread?"
                him normal "No way; he's a friend of mine. Come on; there's no need to be scared of him."
                "It was a long ride over to Pete's ranch, but it felt good to spend time with [bro_name]. He was so quiet that he didn't always get much attention, but his little arms held me tight as we rode and I got the feeling he was feeling better."
                scene farm_exterior flip with fade
                show pete at midright with dissolve
                show him normal at midleft
                show bro normal at quarterleft
                with moveinleft
                him surprised "Hey, Pete. How's it going?"
                pete "[his_name]. Whoa, is this your little [bro_name]? He's gotten big."
                him normal "He's doing pretty good. Hope he hasn't been bothering you or your herd."
                pete "Nah, some of the other kids try and scare the cows, playing some kinda game where they try and make 'em run. But I don't think [bro_name]'s one of them."
                "I waited for [bro_name] to say something, but he seemed pretty scared of Pete. He just held my hand tight and looked down at the ground."
                menu:
                    "What should I do?"
                    "Mention him yelling at [bro_name].":
                        him surprised "Really? He says you yelled at him the other day."
                        pete "Did I? Maybe I thought he was one of the other kids. Getting to be a lot of them, I can't keep them all straight."
                        him normal "Yeah, me neither! They should all wear nametags or something."
                        pete "Heh. We could brand 'em. Right on the forehead."
                        him happy "Ha ha, yeah, really."
                        "I laughed, but then looked down at [bro_name], who was clutching my hand even harder and had his face pressed against my leg."
                        pete "Kid, I'm joking! Man, where'd you get such a serious kid?"
                        him normal "I guess someone in our family should be serious."
                        pete "Ain't going to be you, that's for sure. Anyway, what brings you all the way out here? Don't have cheese to trade, if that's what your after."
                        him determined "No, we're actually looking for some bread."
                    "Ask about bread.":
                        him determined "So, we're actually here because we're looking for some bread."
                pete "You think I got bread?"
                him concerned "I thought I'd check."
                pete "Nah, wheat's too much of a pain. Got corn and cows and that's about it."
                him surprised "Want to trade a bit of cornmeal for this crabird jerky?"
                pete "All I got are kernels. You gotta grind 'em yourself."
                him normal "Sure, I can do that."
                "Maybe we could make some cornbread. It wasn't what [bro_name] had in mind, but we didn't have time to look anywhere else, and it was the best I could do."
                him "Thanks, Pete. See you around."
                pete "See you. Take it easy, kid."

        scene path with fade
        show lettie at center
        show him normal at center
        show bro normal at center
        with dissolve
        show night_overlay
        "[bro_name] and I were both engrossed in our own thoughts on the ride back home."
        "But as we approached home, [bro_name] broke the silence."
        bro "I like riding with you, dad."
        him "I like riding with you, [bro_name]."
        "We didn't find any bread, but [bro_name] seemed to be feeling better. Maybe hanging out with dad was what he really needed."
    return

label family17_angry:
    him annoyed "You're too old to be throwing tantrums like this! You're blubbering like a baby!"
    bro "I... can't help it (sniff)"
    him determined "You can help it, and you will. This is no way for a kid your age to behave."
    "If anything, his crying got worse. I started to feel really frustrated. I wanted to help [bro_name], but nothing I was doing was helping!"
    menu:
        "What should I do?"
        "Threaten him.":
            $ responsive -= 5
            him annoyed "Stop crying or you'll get a spanking!"
            "He continued crying as if I hadn't said anything."
            "His disobedience was really infuriating!"
            him angry "You want to cry?! Fine, I'll give you something to REALLY cry about!"
            "(whack)"
            "(whack)"
            "(whack)"
            "His crying increased, but I was done. I couldn't help him; nobody could. He was just impossible!"
            "I stomped out of the room, out of the house, but I could still hear him."
            "How could a child make me feel so helpless?!"
            $ authoritarian += 1
        "Leave him alone.":
            him annoyed "Cry here all afternoon if you want to; I'm not going to wait around for you."
            $ neglectful += 1
    return


# 11.1 Earth years old
# Bathing is still a necessity
label family18:
    "I still couldn't get used to how tall [kid_name] was all of a sudden. It was like my little girl had spent a few years in a portal world and come back to us completely different."
    "Well, not completely different."
    "Sometimes she still acted like a little kid."
    him annoyed "Yes, I'm serious. You need to take a bath!"
    kid "Can't I just wash off here at the sink?"
    him determined "No. You need a real bath, all over."
    kid "Ugh, why?! I just had a bath two days ago!"
    menu:
        "What should I say?"
        "Because I said so.":
            him annoyed "Because I said so. I'm the dad; you're the kid. When I say 'Take a bath', you take a bath!"
            $ demanding += 1
        "Because you stink.":
            him surprised "Want me to tell you the truth?"
            kid "Yeah, I guess?"
            him determined "You're getting kind of stinky."
        "Because it's healthy.":
            him normal "I want you to be healthy. Right now there is a seriously out of control bacteria party going on in your armpits and who knows where else, and party time is over."
    kid "Dad!"
    him normal "Don't you want the truth?"
    kid sad "You don't have to say it like that."
    him "Well, you need to take a bath."
    kid "I really hate taking baths!"

    menu:
        "What should I say?"
        "(Say nothing)":
            $ responsive += 1
            $ confident += 1
            "I just walked away. It wasn't worth fighting over. If she really wanted to walk around stinky and dirty, I guess that was her problem."
            # TODO: [her_name] notices and says something?
            $ neglectful += 1
            return
        "You'll take a bath, or else!":
            $ demanding += 1
            him angry "You'll take a bath, or else!"
            kid annoyed "Or else what?!"
            menu:
                "What should I say?"
                "I'll throw you in the river!":
                    him annoyed "I'll throw you in the river."
                    kid "I'm eleven years old. You can't just carry me around like a baby."
                    him angry "You don't think I could?!"
                    "I lifted her up. It had been a long time since I carried her anywhere. Her arms and legs were so long, now. And she was much heavier."
                    kid "Stop it! Dad, put me down! I'll take a bath, I will, just put me down!"
                    "I could probably make it all the way to the river. But maybe I shouldn't. I felt suddenly guilty. How would I like it if someone threw me in the river? Then again, I didn't want to let her think she could get away with this kind of disobedience."
                    menu:
                        "What should I do?"
                        "Set her down.":
                            him "Fine."
                            kid "Wow. I can't believe you were seriously going to throw me in the river."
                            him "I can't believe you were seriously going to make me throw you in the river instead of just taking a bath."
                            kid "I didn't make you do anything. You always tell me that [bro_name] doesn't make me do stuff, that I have a choice when he makes me mad. Well, so do you."
                            him "..."
                            "Maybe she was right..."
                        "Keep going.":
                            him "You had your chance."
                            kid "Dad, seriously, let go, now!"
                            "She started prying at my hands, but I kept holding on to her the entire walk to the river. It took about twenty minutes, her protesting and crying the whole way."
                            # TODO: scene change
                            "The air was cool, but not cold. It would be an uncomfortable bath for her, but she wasn't in any danger. The leeches all lived in the warm ponds, not the cold river, so she couldn't even complain about those."
                            "When we arrived, I didn't pause at all. I walked right into the water, boots and all, and dropped her in the middle of it with her clothes still on."
                            "Then I turned around to start walking back home."
                            "A huge wave of water splashed my back. [kid_name], drenched and furious as a cat, was using all her might to send water my direction."
                            "I felt kind of mad, but I couldn't blame her. I had humiliated her and made her feel like a little kid again. I thought that was what she needed. But what did she need now?"
                            menu:
                                "What should I do?"
                                "Try to cheer her up with a water fight.":
                                    $ responsive += 1
                                    "I send a wave of water back, and soon we were splashing and yelling and hollering."
                                    "Our anger turned into laughter as we aimed water splashes at each other."
                                    him happy "Dodge this!"
                                    kid "Ha ha, you missed! Besides, I'm already soaked so I don't even notice any more water!"
                                    him normal "You couldn't hit me if I was the-- blruggleegrlgle."
                                    kid "What's that? I couldn't hear you; seems like your mouth's full of water!"
                                    him "Here, come closer so you can hear better."
                                    # TODO: animate this
                                    kid "What? What were you going to say?"
                                    him "I don't know WATER you going to say?!"
                                    kid "No fair! You tricked me!"
                                    "Finally, both of us sopping wet and shivering, we headed for home."
                                    scene farm_interior with fade
                                    show her normal at midright with dissolve
                                    show kid normal at center
                                    show him normal at midleft
                                    with moveinleft
                                    her surprised "There you are! Where have you-- um, why are you soaking wet?"
                                    "[kid_name] and I looked at each other, then burst out laughing."
                                    him happy "[kid_name] took a bath."
                                    kid happy "Dad needed one, too."
                                    her normal "Hmmm. Looks like... fun?"
                                    kid normal "Yeah, it was pretty fun. Too bad you missed it."
                                    her happy "Too bad."
                                    $ authoritarian += 1
                                    return
                                "Just walk home.":
                                    $ demanding += 1
                                    "What she needed was a serious dad who would make sure she did what she needed to do, and never backed down."
                                    "I would be that dad, even if she hated me for it."
                                    $ authoritarian += 1
                                    return

                "No food until you take a bath.":
                    him annoyed "No food until you take a bath."
                    kid "What?? You'd starve your own kid? Over a bath?!"
                    him determined "It'd be you starving yourself because you're too lazy to take a bath!"
                    kid "Ugh! You treat me like such a baby sometimes!"
                    him angry "You're acting like a baby! Adults don't walk around assaulting each other's nostrils with their stench! When they're dirty, they just go take a bath!"
                    $ authoritative += 1

                "No computer pad until you take a bath.":
                    him annoyed "No computer pad until you take a bath."
                    kid "Fine. I don't have time for that today, anyway; I have too much homework."
                    "Uh-oh. I really wanted her to take a bath today; I was hoping that my threat would do the trick."
                    menu:
                        "What should I say?"
                        "Fine; go do your homework.":
                            him determined "Fine. Go do your homework."
                            kid "I'm already doing it! You don't have to tell me!"
                            "She really didn't like me telling her what to do."
                            "Too bad; I was her dad. It was my job to tell her what to do."
                            "She finished her homework right after dinner, and reached for the computer pad."
                            him "Take your bath first."
                            kid "Daaad! I've been working hard on homework this whole time and now I just want to take a break!"
                            him "As soon as you've finished your bath, you may use the computer pad."
                            $ authoritative += 1
                        "I changed my mind.":
                            $ demanding += 1
                            him annoyed "I changed my mind. You have to take a bath right now."
                            kid "What?! I'm trying to do my homework!"
                            him angry "Right. NOW!"
                            $ authoritarian += 1
                        "(Say nothing.)":
                            "I didn't say anything. Sooner or later she'd want to use the computer pad, and then she'd have to take a bath."
                            "Sure enough, right after dinner, she finished her homework and reached for the computer pad."
                            him "Take your bath first."
                            kid "Daaad! I've been working hard on homework this whole time and now I just want to take a break!"
                            him "As soon as you've finished your bath, you may use the computer pad."
                            $ authoritative += 1
        "If you decide not to take a bath, you'll need to stay outside with the other stinky things.":
            $ demanding += 1
            $ responsive += 1
            $ confident += 1
            him surprised "If you decide not to take a bath, you'll need to stay outside with the other stinky things. I don't allow Lettie or the goats in the house, so if you're stinky like them, you'll need to stay outside, too."
            kid "But... I have to do my homework!"
            him normal "I guess you can decide if you want to do your homework outside or take a bath first."
            kid "It's cold outside!"
            "It wasn't that cold. But I wasn't going to be sidetracked into an argument about that."
            him normal "You can wear a jacket if you want. Or go in the barn."
            kid "But, but..."
            him happy "It's up to you."
            "I felt so free. It wasn't up to me to figure out how to make her take a bath; I just needed to set some reasonable conditions and let her decide."
            kid "Ugh, fine, I'll take a bath!"
            $ authoritative += 1
        "I hate bathing, too. Maybe if we all stink we won't notice it so much?":
            $ responsive += 1
            him happy "I hate bathing, too. Maybe if we all stink we won't notice it so much?"
            kid "You stink. You should take a bath."
            him "Nope. [kid_name] hates baths, so none of us are going to take a bath ever again."
            kid "How about you take a bath, and then I'll take one?"
            him "I thought we weren't doing the bath thing anymore?"
            kid "You first."
            him "Okay. I love baths."
            hide him with moveoutleft
            scene black with fade
            "I went off to the bath. I was going to have the best bath ever."
            him happy "Wow, this warm water feels so good!"
            him surprised "Why didn't I do this earlier?! This is so fun!"
            him normal "Mmmm, this soap smells nice!"
            him surprised "I feel good, na-na na-na na-na na." # TODO: Singing notes in here?
            scene farm_interior with fade
            show kid normal at midright with dissolve
            show him normal at midleft with moveinleft
            him happy "Wow, that was great! That was so fun; I might have to go take another bath in a few hours!"
            "[kid_name] just rolled her eyes and sighed."
            $ permissive += 1
        "Why don't you want to take a bath?":
            $ responsive += 1
            him surprised "Why don't you want to take a bath?"
            kid "I just took one! Besides, I don't stink."
            him surprised "Did you know that after prolonged exposure to your own smell, your nose's smell receptors stop responding to it?"
            kid "What do you mean?"
            him normal "Your nose gets used to your own smell, and you can't smell yourself."
            kid "You just made that up."
            him "No, it's called olfactory fatigue. Here, let's look it up."
            "I showed her an article on the subject."
            kid "Hmmm."
            him "In fact, people didn't used to take so many baths, and they probably didn't really notice the unwashed body scent so much. But in our culture, we really notice it."
            kid "Did people on Earth take baths more than we do here on Talaam?"
            him "Yeah, I used to take a shower every day."
            kid "Every day?!"
            him "Yup. I'd come in from the farm and first thing I'd do was take a shower. If I didn't, my mom wouldn't feed me anything."
            kid "Well, a shower sounds better than a bath."
            him "Yeah, I kind of miss showers. Maybe we can figure out how to put one in sometime."
            him "But for now, we have the washtub."
            kid "Do I really have to take a bath?"
            him "I'm not going to make you do it. But when I say 'You stink,' know that I'm saying that as someone who genuinely loves you and doesn't want other people to judge you by your scent."
            kid "I still don't think I stink."
            him "You do. But it's okay; I love you anyway."
            kid "Fine. I'll take a bath."
            $ authoritative += 1

    "She stomped off. A few minutes later, I heard the pipes running. Hopefully that meant she was filling up the washtub."
    "She came out a while later, dressed in clean clothes, her skin damp, but she still smelled bad. If anything, now it was worse, like a locker room for pit bulls."
    him surprised "Did you use soap?"
    kid angry "You didn't say anything about soap!"
    him determined "I thought it was obvious."
    kid "No!"
    menu:
        "What should I say?"
        "Go back and wash with soap.":
            him determined "It's not a bath unless you use soap. Go try again."
            kid "Daaad! You're wasting my whole afternoon!"
            "She tried to get away without using soap the next few times, also, but each time I sent her back to the tub."
            "Soon she didn't forget, but she still didn't like baths."
        "Use soap next time.":
            him concerned "You know what... just, use soap next time."
            kid happy "Okay."
            "She forgot to use soap about half the time, but I just couldn't muster up the energy to make her go back and do it all again."
            "Hopefully eventually she would learn how to clean herself properly..."

    return

# 11.8 Earth years old
# Pornography...
label family19:
    $ family19_notlikethat = False
    $ family19_questions = False
    "You're sending an e-mail to the farming committee and looking for a photo you took of some crops when you find a pornographic video stored on the computer pad."
    "Looking at the time and date, it must be from when [kid_name] was using the tablet yesterday..."
    menu:
        "What should I do?"
        "Punish Terra.":
           $ demanding += 1
           him annoyed "[kid_name]!"
           kid "What?"
           him "I found your pornography on the computer pad."
           kid "Dad, I can explain--"
           him "I don't want to hear it. I can't believe you would watch that filth."
           kid "I just--"
           him annoyed "No. You are grounded -- from using the computer pad, from hanging out with friends, everything!"
           kid "Dad, you won't even let me talk!"
           him angry "There's nothing to discuss! I don't ever want to find you doing something like that again!"
           kid angry "Ugh, you don't even listen!"
           $ authoritarian += 1
        "Watch the video.":
           $ demanding -= 1
           "You start watching it and immediately cringe."
           "There's nothing romantic or loving about it -- it's designed solely to ramp up hormones and get to a climax as fast as possible."
           "And the rough foreplay seems uncomfortably like rape -- not something you'd want [kid_name] to think was normal."
           kid surprised "Dad, what are you watching?"
           him "I found this video on here when I was looking at your history."
           kid blushing "Oh. That."
           jump family19_porn_chat
        "It's not a big deal. Do nothing.":
            "Teenagers are going to watch porn. That's just a fact of life."
            $ confident += 1
            $ demanding -= 1
            $ neglectful += 1
        "Ask her about it.":
            $ responsive += 1
            him concerned "[kid_name], come sit with me for a minute."
            kid surprised "What is it, dad?"
            him determined "What can you tell me about this pornography on the computer pad?"
            kid "I don't know."
            him surprised "I know that it's from when you were using it."
            kid "Yeah..."
            "She falls silent. You sense that she wants to leave, but she might also have questions that she doesn't know how to ask."

            menu family19_porn_chat:
               "What should I say?"
               "Tell me about what happened." if (sex_ed_biology):
                   $ demanding += 1
                   $ responsive += 1
                   him "Tell me about what happened."
                   kid "It was an accident."
                   him "I know sometimes pornography can come up when you're not even looking for it."
                   kid "Yeah, I wasn't! I was just looking up something about a book I was reading."
                   him "I know. I probably should have talked to you about it before. But it's kind of hard for me to talk about sometimes, since sex is such a private thing."
                   kid "Then why do people make videos like that?"
                   him "That's a good question. I know a lot of them are trying to make money. Some are trying to express themselves."
                   kid "I just... I just couldn't stop watching it."
                   him "I know -- our brains are wired to respond to sex very strongly. And at your age, it's probably something you're curious about."
                   kid "..."
                   him "That's why you need to have a plan ahead of time, so the thinking part of your brain can be more in control."
                   kid "A plan?"
                   him "Yeah. If you see pornography, turn off the screen and bring the computer pad to me. I won't be mad; I'll just help you decide what to do."
                   kid "..."
                   him "Will you do that?"
                   kid "..."
                   "She didn't say anything, just pulled at a strand of her hair and twisted it."
                   him "Can you please do that?"
                   kid "...okay."
                   him "And if you have questions about sex, I hope you'll ask me or mom."
                   kid "..."
                   him "..."
                   $ parenting_style = get_parenting_style()
                   if ((parenting_style == "permissive") or
                       (parenting_style == "authoritative")):
                       kid "Does it hurt?"
                       him "Not if you're doing it right. Good sex is when both people are trying to help the other person feel good and show their love for each other."
                   "She didn't look at me, and I could tell she had a lot on her mind. But it was hard for her to say what she was thinking."
                   "I reached over and hugged her."
                   him "I hope you know that I love you."
                   kid "Yeah."
                   "She hugged me back, only briefly, but it reminded me that she was in some ways still a kid, and she still depended on me for love and truth and guidance."
                   "Hopefully I was doing okay."
                   $ confident += 1
                   $ authoritative += 1
               "This is not acceptable computer use.":
                   $ demanding += 1
                   him determined "Pornography is not acceptable computer use."
                   kid "Oh. Uh, okay."
                   "I was kind of surprised she didn't argue with me. She probably just didn't want to talk about it."
                   him surprised "..."
                   kid "...Can I go now?"
                   him concerned "Uh, yeah."
                   $ authoritarian += 1
               "Never look at this kind of garbage again!":
                   him annoyed "You must never look at this kind of thing again."
                   kid "..."
                   him angry "Did you hear me?!"
                   kid "I heard you!"
                   "She stomped off. She was so temperamental these days, it was hard to get through to her. But I wouldn't stop trying."
                   $ demanding += 1
                   $ authoritarian += 1
               "You're old enough to be responsible for you watch.":
                   him "Well, you're old enough to be responsible for what you watch."
                   kid sad "Okay..."
                   $ permissive += 1
               "You know that real sex isn't like that, right?" if (not family19_notlikethat):
                   $ responsive += 1
                   him "You know that real sex isn't like that, right?"
                   kid "Oh, uh, yeah."
                   "She tried to sound confident in her answer but failed."
                   "I felt like I had something more I needed to teach her, but I wasn't sure how to say it..."
                   $ family19_notlikethat = True
                   jump family19_porn_chat
               "Pornography is addictive.":
                   $ demanding += 1
                   him determined "Pornography is addictive."
                   kid "What do you mean?"
                   "I had to remember that [kid_name] had grown up much more sheltered than I had... This was a small town with a small school."
                   "All the analogies I thought of were things she had no experience with -- drugs, smoking, even sugar was something she had very little knowledge of."
                   him concerned "Well...it tries to make you feel a certain way. Your body is programmed to want to do things that make it feel that way."
                   kid "So I'm a robot now?"
                   him "Not at all. You also have a brain and free will, so you can decide if the things your body wants are good for you."
                   kid "How do you know?"
                   him "Well, how did the video make you feel?"
                   kid "..."
                   "I let her think about that for a minute."
                   him "Well?"
                   kid "Tickly and kind of yucky. But I couldn't stop watching it..."
                   him "Sounds like you understand the addictiveness I'm talking about."
                   kid "..."
                   him "That's why you need to decide with your brain ahead of time what to do if you see something that's not good for you."
                   "She looked pensive, and I wished I could have read her thoughts to know what she was thinking."
                   kid "Can I go now?"
                   him "Um, yeah."
                   $ authoritative += 1
               "Do you have any questions about sex?" if (not family19_questions):
                   $ responsive += 1
                   him "Do you have any questions about sex?"
                   kid "What? No!"
                   if (not sex_ed_biology):
                       "She probably had a lot of questions; I certainly hadn't explained much to her."
                       "But if she wasn't willing to ask them..."
                   else:
                       "I could tell she did have questions; she just didn't know how to ask them. Or maybe she didn't know what to ask."
                   $ family19_questions = True
                   jump family19_porn_chat
    return

# 12.4 Earth years old
# Musical Instrument
label family20:

    kid "Dad, listen to this song."
    him "Okay..."
    "She played me a song where a girl about her age was playing a soulful song on the saxophone."
    him "That's a good song."
    kid "I wish I could do that."
    menu:
        "What should I say?"
        "You can do anything.":
            $ responsive += 1
            him "You can do anything if you put your mind to it!"
            kid "Yeah? Where am I going to get a saxophone?"
        "You can sing, can't you?":
            $ demanding += 1
            him "You can sing, right? Maybe you could sing kind of like that?"
            kid "It's not the same. And I'm not that good at singing, either."
        "Yeah, that's too bad.":
            him "Yeah, that's too bad."
            kid "Saxophones are just so cool."
        "What exactly are you talking about?":
            him "What exactly are you talking about?"
            kid "I want to play the saxophone!"

    "I hadn't seen a real saxophone in years."
    him "We don't have any saxophones here, do we? Guess it wasn't considered important for a beginning colony."
    kid "I {b}really{/b} want to play one!"
    "I wanted to support her desires... but I also wasn't sure how serious she was about this. It would take a lot of work to figure out some way to get a saxophone, and then what if she changed her mind later?"
    "And would she really be able to learn how to play on her own?"

    him "Let me think about it."
    kid "You mean it might be possible?! That would be so cool!"
    him "I don't know if it's possible! I'm going to find out, though."

    scene black with fade

    nvl clear
    him_c "Anyone have a saxophone? [kid_name] wants to play..."
    ilian_c "Saxophone! Oh man, I haven't played in so long... wish I'd brought mine with me."
    sara_c "There's no way your bari sax would've fit the weight {b}or{/b} size limit! 😬"
    kevin_c "There's a design you could print, but you'd need a bunch of tiny screws, springs, and pins for all the valves."
    ilian_c "You'd need to make pads out of fabric, and reeds out of wood. They'd have to be really precise."
    ilian_c "Honestly, almost any other instrument would be easier to make."
    him_c "Okay, thanks. Do you think RET would send one from Earth?"
    brennan_c "Musical instruments aren't on the schedule."

    scene farm_interior with fade
    kid "So? What did you find?"
    him "Well..."
    menu:
        "What should I say?"
        "If you really want one, here's where to start.":
            $ responsive += 1
            $ demanding += 1
            $ confident += 1
            him "If you really want one, here's where to start."
            "I showed her what Kevin and Ilian had said."
            kid "I can make one! I'm going to see if we can print one right now!"
            him determined "Hold on a minute. Before you print anything, you need a detailed plan. We only want to print it if you're actually going to make it."
            kid "Of course I'm going to make it."
            him "Well, then you'll need a plan anyway."
            "She got started, but after a few days of working on it, the true scope of the project dawned on her."
            kid "I can't do this! I don't even know what a saxophone is supposed to be like!"
            him "Did you ask Ilian to see if he'd help you?"
            kid "I don't want to ask Ilian."
            him surprised "Why not?"
            kid "I just don't! He's always yelling at Oleg; he'd probably just yell at me."
            "That was actually a possibility."
            him determined "Well, he's the only person on the entire planet that we know can play the saxophone. Didn't you want to ask if he'd teach you?"
            kid "Can't you do it?"
            him "This is your reponsibility. But if you need my help with something specific, you can ask."
            kid "That sounds like your way of saying you aren't going to help."
            him "I'll help -- but you're in charge."
            kid "I don't want to talk to Ilian!"
            him "Do you want to ask me for help?"
            kid "Yes, help!"
            him "What do you want me to do?"
            kid "Talk to him for me!"
            him "I already said I'm not doing that."
            kid "Then what am I supposed to do?!"
            him "Try asking me to go with you."
            kid "Hmph. Fine. Will you come with me to talk to him?"
            him "Sure!"
            scene black with fade
            "Ilian agreed to help her make a saxophone. He wanted to make one for himself, too, so they worked on it together every afternoon for a few months."
        "One way or another, I will find you a saxophone!":
            $ responsive += 1
            him "One way or another, I will find you a saxophone!"
            kid "Okay, cool."
            him "'Cool'? No, 'thank you' or anything?"
            kid "Yeah, uh, thanks, dad."
            him "I don't think you realize how much work this is going to be."
            kid "Yeah I do!"
            "She had no clue."
            scene black with fade
            "Ilian and I worked for months getting everything just right. It seemed like such an inefficient machine, but [kid_name] really wanted one."
            "Ilian wanted one, too, so we worked on the pair of saxophones for weeks."
            "I just hoped [kid_name] would appreciate all our hard work."
            $ permissive += 1
        "That's not something you can do right now.":
            $ neglectful += 1
            him "That's not something you can do right now."
            kid "It's impossible?"
            menu:
                "What should I say?"
                "Yes, it's impossible.":
                    him "Yes, it's impossible."
                    kid "Figures. Why'd you and Mom ever leave Earth, anyway? They have so much cool stuff there. All we have is dirt and crabirds."
                    "I was about to answer her, but then she left the room. I guess it was a rhetorical question."
                    scene black with fade
                    "Several weeks later, [kid_name] came home and slammed the door behind her."
                    him "Hey, watch it!"
                    kid "You lied to me!"
                    him "What are you talking about?"
                    kid "You said it was impossible to get a saxophone, but Ilian built one!"
                    him "I meant it was impossible for you."
                    kid "You should have told me. I would have talked to him!"
                    him "I didn't want you to get your hopes up on something that wouldn't even work."
                    kid "Well it does work!"
                    him "For Ilian. He knows what he's doing."
                    kid "You were just being lazy."
                    him "I have better things to do than fool around with music all day! You can't make food with a saxophone! It's not going to keep you alive!"
                    kid "It would make me feel like I have a life!"
                    "She stormed off."
                    "A part of me felt guilty for quashing her dream, but it was probably for the best."
                    "This wasn't Earth; we didn't have time to waste on useless things."
                    # TODO: trust variable
                    $ responsive -= 1
                    return
                "It might be possible.":
                    $ confident += 1
                    him "It might be possible, but so difficult as to be practically impossible."
                    kid "You're not making any sense."
                    him "Look, I've done what I can do, okay? You want to look into it more, you can ask Ilian about it; he used to play saxophone."
                    kid "Fine, maybe I will."
                    scene black with fade
                    "It turned out Ilian wanted to make a saxophone for himself, and after she begged and begged so he let [kid_name] make one with him in exchange for her minding the storehouse for him sometimes."
                    "It took them several weeks, but [kid_name] was really into it. I guess she was serious about wanting to play the saxophone!"
        "Focus on what you can do.":
            $ demanding += 1
            him "We're not going to be able to get a saxophone. Focus on what you can do."
            kid "I can watch videos and dream in my heart. Not helping, dad!!"
            him "That's not all; you can focus on your singing. I've scheduled individual voice lessons for you with Julia."
            kid "Julia?! Aw man, not her! She's so mean!"
            him "She just expects a lot from people. As long as you work hard and don't give her a reason to be disappointed you'll be fine."
            kid "Do I have to?"
            him "Yes. I think musical training would help you a lot."
            kid "How is that going to help?"
            him "You'll learn music theory and how to read music, which will help with any instrument you play in the future."
            kid "So it would help me learn saxophone?"
            "Honestly, I didn't know. I'd never learned to play a musical instrument. But Julia said it would, and I believed her."
            him "Yes."
            kid "...Okay."
            scene black with fade
            "Julia expected a lot from [kid_name], but she was quick to praise when [kid_name] improved."
            scene farm_interior with fade
            show him normal at midright
            show kid normal at midleft with dissolve
            kid surprised "{font=fonts/OpenSansEmoji.otf}🎶{/font}You are my sunshine, my only sunshine-{font=fonts/OpenSansEmoji.otf}🎶{/font}"
            "It amazed me how much her voice improved, and though I soon got tired of her practicing the same songs over and over, it was nice to hear music around the house."
            him happy "You sound good, [kid_name]. Keep practicing."
            "She didn't say anything, just blushed and kept singing."
            kid "{font=fonts/OpenSansEmoji.otf}🎶{/font}Please don't take my sunshine away.{font=fonts/OpenSansEmoji.otf}🎶{/font}"
            $ authoritarian += 1
            return

    scene storeroom with fade
    "Finally they were finished. I came over to see what they had made."
    ilian "These are really terrible quality; they're going to need constant maintenance, and all the keys take a different amount of pressure, and there's leaks everywhere..."
    kid "But they work!"
    him "Yeah? Let's hear it!"
    kid "I don't know much yet; just this one note."
    # TODO: add SFX here
    him "Yep, that's a note all right."
    ilian "I suppose now you'll want lessons."
    kid "Yeah!"
    ilian "Let me talk to your father."
    "Ilian had a gleam in his eye. I could tell these lessons weren't going to come cheap."
    him "I can pay you in produce."
    ilian "No, you can't. Everything you grow is supposed to come to the storehouse; it's not even yours."
    him "What were you thinking, then?"
    ilian "25 credits per lesson. Once a week." # TODO: currency check
    him "I don't know; she could probably teach herself. There's plenty of instructional videos. And I found a music computer program that looks pretty good."
    ilian "All of which are a poor substitute for a living, breathing, personal instructor."
    "I didn't know much about music, but he was probably right."
    menu:
        "What should I say?"
        "15 credits.":
            him "15 credits."
            "I figured I could probably bargain him down. He looked like he wanted to teach [kid_name] almost as much as she wanted to learn."
            ilian "15 credits? That's not even minimum wage."
            him "There's no such thing as minimum wage."
            ilian "20 credits for a half hour lesson combined with Oleg."
            him "What happened to a 'personal instructor'?"
            ilian "If you're paying less, you get less. That's how the world works."
            him "All right, fine."
        "You have a deal.":
            him "You have a deal. It's not like you have any competition in the saxophone teaching business."
            ilian "I'm glad you realize the value of the musical arts."
        "Isn't there something else we could exchange?":
            him "Isn't there something else we could exchange?"
            ilian "You don't have anything I want."
            him "Like, horseback riding lessons for Oleg, or something?"
            ilian "Oleg hates horses."
            him "I could come help you process food while she's in her lesson. Canning, dehydrating, whatever."
            ilian "That could work. Fine; you have a deal."
        # TODO: make you now have less work available. Also subtract the money.
    "I was worried that the saxophone would just be a fad [kid_name] went through, but she really got into it."
    "I wasn't a musician, so I didn't even understand what she was talking about half the time she tried to tell me about her music."
    "But when she played, I could hear her expressing emotions even she didn't know she had."
    $ plays_saxophone = True
    return

#####################################################
#
# TEENAGER
#
#####################################################

# 13 Earth years old
# Sarcastic Humor
label family21:
    scene farm_interior with fade
    show him normal at midleft
    show kid normal at center
    show bro at midright
    with dissolve

    "Lately, [kid_name] and [bro_name] had been playing a video game together. I thought it would be good for them, to help them bond and learn to cooperate, but sometimes it just made them both frustrated..."
    bro "Aliens on the left! I'll get the laser sword."
    kid "Oh yeah, that's real smart. The laser sword? That's the weakest weapon in the game against those guys!"
    bro "I like the laser sword..."
    "She used a whiny kid voice to mock him."
    kid "'I like the laser sword. Stand still so I can hit you with my super wimpy weapon.' They're going to crush you if you try that."
    bro "Well, what do you think I should use?"
    kid "Duh! The sniper blaster! They're weak against blast damage and you can keep your distance so you don't die in like five seconds like you do every time!"
    bro "I hate the scope; it's too hard."
    kid "It's only hard if you're a total n00b." # TODO: make up some Talaam slang here?
    "[bro_name] was almost in tears. [kid_name] was focused on the game and didn't seem to notice."
    menu:
        "What should I do?"
        "Say something.":
            $ demanding += 1
            him determined "[kid_name], that's not nice."
            "She didn't look up, just shrugged as they continued their battle."
            kid "Sorry."
            "They kept playing, but soon [bro_name] made a mistake."
            kid "Really? You didn't see that guy whose been slobbering over your shoulder for the last ten minutes?"
            bro "I did, but I couldn't move in time!"
            him annoyed "Pause your game and listen to me!"
            kid "I can't pause it; it's online. We still have a chance to beat Travis if [bro_name] would stop rolling on the ground like a baby."
            bro "I'm hiding!"
            menu:
                "What should I say?"
                "Turn it off now.":
                    $ demanding += 1
                    him angry "Turn it off now!"
                    kid "Seriously, dad?"
                    him annoyed "Yes. Right now."
                    kid "Ugh! Fine. There. What's so important you couldn't wait for five minutes?"
                "Turn it off as soon as the round is over.":
                    $ responsive += 1
                    him determined "Turn it off as soon as the round is over."
                    kid "Okay, fine."
                    "They finished the round, and lost. Travis's avatar did a triple backflip over their motionless avatars and grinned mockingly. I could see why [kid_name] wanted to beat him."
                    "She quit the game and turned to me."
                    kid "What is it?"

            menu:
                "What should I say?"
                "No more video games.":
                    $ demanding += 1
                    him angry "No more video games."
                    "That got their attention."
                    kid "WHAT?! No more video games? Why?"
                    him annoyed "You're being rude to your brother. That's not allowed."
                    kid "For how long?"
                    bro "For me, too?"
                    menu:
                        "What should I say?"
                        "Just do something else for awhile.":
                            him normal "Just go and do something else for awhile."
                            kid "For how long?!"
                            him "At least for today. We'll see if you can be polite and earn your video game priveleges back."
                            kid "That's mean."
                            $ authoritative += 1
                        "You're both done for a week!":
                            him annoyed "No video games for either of you for a week!"
                            bro "But I didn't do anything!"
                            kid "I didn't do anything either! I was just trying to help him get better at this game!"
                            him "You heard me."
                            kid "But... but that's not fair!"
                            him "Sometimes life isn't fair. Guess you'll learn to deal with it."
                            bro "You're a mean dad!"
                            kid "Yeah!"
                            him normal "Yup, sometimes I have to be Mean Dad."
                            kid "Come on, [bro_name], let's go play outside."
                            bro "Yeah."
                            "Hmmm. Somehow I had turned [kid_name]'s animosity towards [bro_name] into animosity towards me. I guess that was better?"
                            $ authoritarian += 1
                        "[bro_name] can still play.":
                            him determined "[bro_name], you were talking politely; you may still play."
                            bro "I don't want to play without [kid_name]! I'd just lose..."
                            kid "Yeah, you would."
                            him normal "Then maybe it's time to do something else."
                            $ authoritarian += 1
                    "I felt kind of bad taking away their video games, but it was the simplest solution I could see to the problem."
                    "But soon enough, they were fighting again..."
                    kid "Can you just run like a normal person without swinging your arms around like a jellyfish?!"
                    bro "I'm not trying to!"
                    "Maybe siblings just always fought, and there was nothing I could do about it..."
                    return
                "You're hurting [bro_name]'s feelings.":
                    $ responsive += 1
                    him concerned "You're hurting [bro_name]'s feelings."
                    kid "I'm not trying to be rude or anything, I'm trying to help him get better at this game."
                    bro "No, you're just being mean!"
                    him determined "What you're doing isn't helping him at all. If you want to help him, you need to be more positive and don't get mad about mistakes."
                    kid "Well, he also needs to stop making stupid mistakes!"
                    him concerned "Do you remember when you first started playing? Wasn't it pretty hard?"
                    kid "Yeah, but I wasn't {b}that{/b} bad."
                    him surprised "Didn't you make a lot of mistakes, too?"
                    kid "Yeah, but not like that! I mean, seriously, who picks the laser sword?!"
                    bro "I just want to play it my way."
                    menu:
                        "What should I say?"
                        "Maybe you shouldn't play together.":
                            him concerned "Maybe you shouldn't play this game together."
                            bro "No! I want to play with [kid_name]!"
                            kid "Yeah, we do want to play together."
                            him determined "Then act like it."
                            $ permissive += 1
                        "You can play together if you are polite.":
                            $ confident += 1
                            $ demanding += 1
                            him determined "You can play together as long as you are being polite. You're on the same team, remember?"
                            kid "Okay, but, [bro_name] can you pick a different weapon next time?"
                            bro "Yeah, I guess."
                            him normal "Okay! That's more like it!"
                            $ authoritarian += 1
                        "Just do better next time.":
                            him annoyed "Just do better next time."
                            $ permissive += 1
                "I expect kind language.":
                    $ confident += 1
                    $ responsive += 1
                    him concerned "I expect kind language from everyone in our house."
                    kid "I'm just trying to help him!"
                    him determined "Then you can help him politely."
                    kid "Okay, can you PLEASE not use the laser sword?"
                    bro "But I like it!"
                    kid "See?! Being polite didn't work!"
                    him concerned "Being polite isn't just about the words you say; it's your attitude and how you say them. Would you want someone to tell you how to play?"
                    kid "I don't need anyone to tell me how to play."
                    him annoyed "Well, [bro_name] feels the same way. Let him play his way."
                    kid "Or else what?"
                    menu:
                        "What should I say?"
                        "Or you won't be able to play video games.":
                            $ demanding += 1
                            him determined "If you can't be polite, you won't be able to play video games."
                            kid "What?! That's so unfair!"
                            him annoyed "That's the rule."
                            kid "Ugh, fine. Can we get back to our game now?"
                            him "Yes."
                            $ authoritative += 1
                        "Or you will have to muck out the barn instead.":
                            $ demanding += 1
                            him determined "If you can't talk politely, you can go muck out the barn instead."
                            kid "What?! That doesn't even make sense!"
                            him annoyed "That's the rule."
                            kid "That's a dumb rule."
                            him "..."
                            bro "Can we play now?"
                            him "Yes."
                            $ authoritarian += 1
                        "I don't know; just be polite!":
                            him angry "I don't know! Why don't you just be polite; then you won't have to find out!"
                            bro "Can we play now?"
                            him "Yes."
                            $ permissive += 1
                "Quit being so rude!":
                    him angry "Quit being so rude!"
                    her "Alright! Fine! You don't have to yell."
                    $ authoritarian += 1
        "Say nothing.":
            $ demanding -= 1
            $ neglectful += 1
            $ confident += 1
            "I didn't say anything; just kept on walking. They could learn how to get along on their own."
            return

    "They went back to playing. Hopefully they'd get along better now."
    menu:
        "What should I do?"
        "Stay and watch.":
            # TODO: productivity penalty?
            "I stayed and watched for a little while. [bro_name]'s avatar got killed, and [kid_name] grunted in frustration."
            kid "[bro_name]!"
            bro "Sorry!"
            "[kid_name] glanced over at me and sighed."
            kid "It's okay."
            bro "Watch out for the mines; that's what killed me."
            kid "Where is their flag?"
            bro "I can climb the tower and find it!"
            kid "Try it."
            bro "Ohhh! Travis got me! But I saw the flag; it's right behind you, under that bench!"
            kid "Yeah! Got it!"
            bro "Now get back! Stay away from the tower!"
            kid "Almost there..."
            bro "He's chasing you... but he's too slow! Yeah! We did it!"
            kid "Yeah!"
            "[bro_name]'s avatar lifted [kid_name]'s up to stand on his hands, and she somersaulted off and they gave synchronized thumbs-ups."
            "I guess they could get along, when they wanted to."
        "Get back to work.":
            "Hopefully they would get along; I didn't have time to stick around and find out."
    return

# 13.6 Earth years old
# You falsely accused Terra! Apologize?
label family22:

    scene farm_interior with fade
    show him determined at midright
    show kid normal at center
    with dissolve
    "After a boring dinner, I was still hungry.  I went to the pantry to get out a jar of applesauce to share with everyone, but then I noticed a jar was missing."
    "[kid_name] loved applesauce. She was always begging me for more, but she knew she was only allowed to have some when [her_name] or I dished it out."
    him angry "[kid_name]!"
    kid "What?"
    him annoyed "Did you steal the applesauce?"
    kid "No! Is it gone?"
    him determined "One of them is missing, and I'm pretty sure it was you!"
    kid "It wasn't! I didn't do it, I swear!"
    "Her mouth twitched as she said it, and I had a feeling she was lying."
    him annoyed "And now you're lying about it?!"
    kid angry "I'm not lying!!"
    him angry "Go to your room! You can come out when you're ready to tell the truth!"
    kid "I am telling the truth! Why won't you believe me?!"
    "She stomped off to her room."
    "I was furious. It was bad enough to break a rule, but then to lie about it?"
    show her surprised at midleft with moveinleft
    her "What's going on?"
    him annoyed "[kid_name] stole the applesauce and won't admit it."
    her concerned "Are you sure it was [kid_name]?"
    him concerned "She acted really guilty."
    her determined "I found an empty jar in [bro_name]'s room, behind his clothes."
    show him surprised with dissolve
    "I was shocked. It had never occured to me that obedient, quiet [bro_name] had stolen the applesauce."
    her serious "[bro_name], please come here."
    show bro at left with moveinleft
    bro "Yeah?"
    her concerned "Come closer; I need you to tell me about something."
    show bro at center with move
    bro "What is it?"
    her serious "I found this applesauce jar in your room."
    bro "..."
    her determined "You know that you're not allowed to take applesauce from the pantry."
    bro "..."
    "I started to say something, but [her_name] but a hand on my arm. It was hard for me to be patient with [bro_name] sometimes, but he liked to do things at his own pace."
    her concerned "Tell me about what happened."
    bro "I...was hungry."
    her surprised "And so you took the applesauce?"
    bro "...Yes."
    her "I see. Thank you for telling the truth, [bro_name]. I'm disappointed you broke our rule and took something that wasn't yours. How are you going to fix this?"
    bro "...I don't know."
    her "I'll let you think about it for a while. I'll ask you again at bedtime, okay?"
    bro "Okay."
    him annoyed "..."
    bro "...can I go now?"
    her "Yes. I love you, [bro_name]."
    bro "I love you too, mommy."
    hide bro with moveoutleft
    menu:
        "What should I do?"
        "Apologize to [kid_name]":
            $ responsive += 1
            $ confident += 1
            "I owed [kid_name] an apology. I had accused her of stealing and lying, when she was innocent."
            # TODO: have a Terra's room bg?
            "I knocked on her door."
            kid "What?"
            show kid normal at midleft
            show him normal at midright
            with dissolve
            him "I'm sorry, [kid_name]. I got mad at you and thought you were lying but I was wrong."
            kid "See?! You never trust me!"
            him determined "You have lied to me in the past, which makes it hard for me to know when you're telling the truth."
            kid "Well I was telling the truth!"
            him angry "I know that now!"
            kid "You should just always believe me."
            him annoyed "Maybe I will once you always tell the truth."
            "I had come in here to apologize; how had this turned sour so quickly?"
            him concerned "Anyway, I didn't come in here to argue with you; I just wanted to apologize."
            kid "Okay."
            "I gave her a quick hug. She didn't quite push me away, but she didn't hug me back, either."

        "Talk with [her_name]":
            "I wanted to talk about this with [her_name]."
            menu:
                "What should I say?"
                "You let [bro_name] off too easy.":
                    him annoyed "You sure let [bro_name] off easy."
                    her surprised "What do you think I should have done?"
                    him concerned "I don't know; I was going to yell at him so he'd know this kind of thing was unacceptable."
                    her concerned "He's a sensitive kid. He already knows what he did was wrong."
                    him determined "Still, shouldn't we punish him or something?"
                    her determined "He will choose an appropriate consequence for himself. If he tries to get away with something easy, then I'll pick the consequences for him."
                    him surprised "Like earning money for some more applesauce?"
                    her normal "Yeah, something like that. He won't always have us around to help him fix his mistakes; he needs to learn to do it on his own."
                    him concerned "I guess that's true..."
                "How do you stay so calm?":
                    him concerned "How do you stay so calm?"
                    her flirt "I've had lots of practice dealing with troublesome rascals."
                    him annoyed "I hope you're not talking about Brennan."
                    her annoyed "No, silly! I'm talking about you... and a lot of my patients, to be honest."
                    him happy "Ooh, sounds like a good story!"
                    her normal "Nope, you know I don't talk about my patients."
                    him flirt "What about your patience?"
                    her flirt "I think we've talked about that enough."
                    $ marriage_strength += 1
                "I love you.":
                    him determined "I love you, [her_name]."
                    her surprised "I love you too, but what made you say that now?"
                    him normal "I'm just so glad we're parents together. Our kids are lucky to have a mom like you."
                    her normal "And a dad like you."
                    $ marriage_strength += 1

        "Talk to [bro_name]":
            "That wasn't enough. [bro_name] needed a serious talking-to! I followed him back to his room."
            # TODO: room bg here?
            hide her with dissolve
            show bro at midleft with dissolve
            show him normal at midright with move
            him determined "[bro_name], I can't believe you stole the applesauce! Don't you know how hard we work to have treats like that?"
            bro "I was just hungry."
            him angry "Yeah, but you can't just eat whatever you want! We have carrots you can eat anytime for snacks if you're hungry."
            bro "I don't like carrots. I like applesauce."
            him annoyed "It doesn't matter; the appleasauce is not yours."
            bro "I know."
            him determined "Okay, well, you just remember that!"
            "He wouldn't meet my eyes, instead watching as he fingered the ties of his quilt."
            bro "Yes."
            menu:
                "What should I do?"
                "Leave him alone":
                    "I left the room. Sometimes I felt so disconnected from [bro_name]; his thoughts were a mystery to me. But I think he understood what I said."
                "Give him a hug":
                    $ responsive += 1
                    "I hugged him. He hugged me back, tight. I was surprised at the strength of his little kid hands."
                    him normal "I'll always love you, [bro_name], even if you make mistakes."
                    "He didn't say anything, but we hugged for a long time."
                "Demand that he look at you.":
                    $ demanding += 1
                    him angry "Look at me when I'm talking to you!"
                    "He turned his head slowly, focusing on my lips."
                    him determined "I don't want you stealing ever again. Do you understand?"
                    "He nodded."
                    him concerned "Good."

    "The next day we had a quiet and uneventful dinner. I tried to start a conversation."
    him "How was school?"
    "[bro_name] shrugged."
    kid "Fine."
    "After an awkward silence, [her_name] tried again."
    her "How's Anya doing?"
    kid "Okay. She bombed our last math test but she doesn't really care."
    her surprised "Really?"
    kid "Math's not her thing. She's working on some really cool art, though."
    him surprised "What does she draw?"
    kid "Animals, mostly. She's got this beautiful jellysquid one that she's going to color, and maybe even print out if she can get the money."

    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):
        him "How come you never draw anymore?"
        kid "Because I suck at it."
        him "You just need more practice. If you work hard, you can get good at anything."
        "[kid_name] didn't say anything but I could tell from her face that she didn't believe that."
        her "Anyway, I've got some charts I really should look through this evening."
        "[bro_name] and [kid_name] did the dishes while [her_name] and I worked side by side on our different jobs."
        "I remembered the days when [her_name] and I used to come home and play video games together; now it seemed like there was always too much work to do."
        "We were so busy, we didn't have much time to just hang out."
        "But at least we were together."
    elif (parenting_style == "authoritative"):
        him determined "I thought the miners had plenty of money."
        kid "Her parents do. Anya doesn't."
        him surprised "Not even enough to print out art?"
        kid "No. They don't buy her anything. I don't think they buy much for themselves, either, except firegrass."
        her concerned "Maybe they're saving up for something for when they go back to Earth."
        him determined "I still think it's weird that some people don't want to stay here."
        her flirt "Not everyone is in love with alien farms like you."
        him flirt "I don't know what you're talking about! I'm only in love with you."
        kid "Anyway, I'm done with my homework. It was pretty easy."
        bro "I'm done, too."
        him happy "We should do something together!"
        her concerned "I was going to go over some patients' charts..."
        extend "but that can wait. What should we do?"
        menu:
            "We should play a game together.":
                him "We should play a game together!"
                kid "As long as it's not something stupid."
                bro "Chess!"
                kid "Not chess!"
                her "Chess is fun, but it's a two player game."
                bro "We can play four player!"
                him "We only have one chess set..."
                kid "I hate chess!"
                her "Pictionary?"
                him "You always win!"
                her "Then let's do kids against adults."
                kid "Oh yeah!"
                bro "I'm not that good at drawing..."
                kid "You don't have to be good, just fast! C'mon, [bro_name], we can totally beat them!"
                bro "Okay..."
                "We played a few rounds of pictionary. The kids did surprisingly well, and I liked the game a lot better when [her_name] was on my team."
            "We should go for a walk.":
                him "The weather's nice; let's go for a walk."
                kid "But I'm tired!"
                bro "I'm not swimming!"
                her "The river's not that far. And you don't have to swim. Bring a book if you're worried you'll get bored, [her_name]."
                him "I'll bring my net; maybe I can catch something!"
                her "We just had dinner..."
                him "Then this'll be dessert!"
                "We walked down to the river. I caught a tiny lobster-looking creature, but it was so small, I just threw it back."
                bro "Stop splashing me!"
                kid "Ha ha ha, it looks like you peed your pants."
                bro "Moooom!"
                her "[kid_name], trade pants with [bro_name]. You know he doesn't like to be splashed."
                kid "What? No way! His pants won't fit me! I'm not walking back to the house naked!"
                her "We'll untie the waistband and you can wear them."
                bro "Ha ha, that looks really funny."
                kid "Stop making fun of me!"
                him "It does look pretty funny. But you'll be okay; we'll be home soon."
                her "Here, you can wrap my jacket around your waist if you want."
                kid "Fine. Ugh, nobody here can take a joke!"
                him "Next time you should splash me instead."
                kid "You'd probably throw me in the river."
                him "Yeah... doesn't that sound fun?"
                kid "No!"
            "We should watch a movie.":
                him "We should watch a movie."
                kid "Can we please watch 'Catacombs'? I love that show!"
                "[bro_name] shook his head. I remember last time we watched it, he woke up in the middle of the night screaming from a bad dream."
                her "I'll pick something everyone will like."
                him "Good luck!"
                her "With our huge database I'm sure I can find something!"
                "She somehow managed to find a movie that had teen protagonists for [kid_name], wasn't too scary for [bro_name], and had deep ideas for [her_name] and I."
                "I popped some popcorn I had been saving and we snuggled up to watch the movie together."
    elif (parenting_style == "permissive"):
        him "Oh, that's cool."
        "We finished eating, and [her_name] and I did the dishes while the kids played on their computer pads."
        bro "This level is too hard!"
        him "Too hard?"
        bro "I've tried it like fifty times!"
        him "Let me see if I can help you."
        "It was a hard level, especially for Talaam kids who weren't used to hard video games. But I beat it for him after a few tries."
        him "Here you go."
        bro "Thanks, dad."
        kid "Can you help me with my math?"
        him surprised "You're not done with your homework yet?"
        kid "No, I was waiting for you to be able to help me with it."
        him "Oh, well, okay."
        "Somehow helping [kid_name] with her math homework was even more exhausting than farming. When I started falling asleep at the desk, [her_name] took over for me."
        her "Go on to bed; I'll help her finish her homework."
        "She didn't have to tell me twice."
    else: # neglectful or inconsistent
        him "Oh, okay."
        "I left right after I finished eating."
        "Sometimes I liked to go for a walk in the evening, just by myself. Or sometimes I'd see if Thuc or Pete wanted to hang out."
        "Today, though, I just admired the sunset."

    return

# 14.2 Earth years old
# Chatting with friends on family tablet
# Address several statistics: teens that spend more time on screens and less doing actual stuff
# are more depressed, get less sleep, and feel more lonely and left out.
# Solutions include: screen-free time, a new hobby, helping her setup a hangout space/time
# with friends, etc.
label family23:
    "It hadn't really been a big deal to share our computer pad with the kids when they were small."
    "On Earth we had been used to everyone having their own, but lots of things were different here on Talaam."
    "We didn't have an electronics store where you could just go pick up another computer pad whenever you wanted."
    "Lately, [kid_name] was on there all the time..."
    scene farm_interior with fade
    show kid normal at midright with dissolve
    show him normal at midleft with moveinleft
    him surprised "Hey, [kid_name], I need to use the computer pad. Can you finish up, please?"
    kid "Dad, I'm doing my homework!"
    him annoyed "With headphones on?"
    kid "Listening to music helps me concentrate!"
    show him surprised at center with move
    "I looked over her shoulder to see what she was doing. She did have her homework up on one part of the screen... and a long conversation with Oleg on the other."
    him annoyed "Does texting help you concentrate, too?"
    kid "Yes!"
    him angry "You shouldn't text during homework! It's distracting!"
    kid "What?!"
    him annoyed "You heard what I said."
    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):
        $ demanding += 1
        kid "Whatever."
        him angry "Don't take that attitude with me!"
        kid "Sorry! Fine!"
        $ authoritarian += 1

    elif (parenting_style == "authoritative"):
        kid "That's really unfair, dad. Can you please just trust me to get my homework done in my own way?"
        him surprised "What are you suggesting?"
        kid "Can you give me thirty minutes? If I'm not done by then, I'll let you use the computer pad, and I won't text until my homework is done."
        him determined "You think you can be done in thirty minutes."
        kid "I know I can!"
        menu:
            "What should I say?"
            "No. No texting during homework.":
                $ demanding += 1
                him angry "No. You may not text during homework!"
                kid "Ugh! Dad, there's this thing called 'friends'. Maybe you've heard of it."
                him annoyed "You can have friends."
                kid "But if I can't be there for them when they need me, am I really being a good friend?"
                him normal "I think they can last for an hour or two without you while you finish your homework."
                kid "No, dad, sometimes they really need me. We're not just gossiping or fooling around; we're helping each other deal with life!"
                him surprised "Are your lives that difficult?"
                kid "Sometimes! We help each other through stuff."
                him determined "Like what?"
                kid "Like... I'm telling Oleg some ways he can help his mom, who's feeling stressed out about their new baby."
                him surprised "Really?"
                kid "Yeah, see?"
                "She showed me her text conversation. She was telling the truth."
                menu:
                    "What should I say?"
                    "Those conversations can wait.":
                        $ demanding += 1
                        him determined "Those conversations, as important as they are, don't have to happen during homework. You can chat when you're done."
                        kid "Dad, you're making me choose between being a good student and being a good friend! I can do both, if you'll let me!"
                        him annoyed "Don't try to make me the bad guy. You'll be better at both if you just do one at a time."
                        kid "Fine."
                    "You can ask for a special exception.":
                        $ responsive += 1
                        him determined "If there's a social emergency, you can ask for an exception to the rule. But otherwise I expect you to finish your homework before chatting with friends."
                        kid "Okay, fine."
                    "I trust you to use your own judgment.":
                        $ responsive += 1
                        him normal "I'm glad you're being a good friend. And so far you've been a good student, too. As long as you are completing your schoolwork with high quality, I'll let you decide when you need to text and when you need to concentrate."
                        kid "Thanks, dad. I can do this."
            "Yes, that sounds reasonable.":
                $ responsive += 1
                him "Yes... that sounds pretty reasonable."
                kid "Thanks, dad. I know what I'm doing."
    elif (parenting_style == "permissive"):
        kid "Daaaad, that's just not fair! You've always let me do that before!"
        him angry "I didn't know you were doing it!"
        kid "Everyone texts each other while they do homework. It's the only time we have to hang out!"
        him annoyed "Okay, okay, I get it. But I really need to use the computer pad. So you have thirty minutes, okay?"
        kid "Fine."
    else:
        kid "Oh, now suddenly you care about my homework?!"
        him surprised "Of course I care about your homework!"
        kid "You don't know anything about me!"
        him annoyed "I'm your dad. I think I know a thing or two about you."
        kid "Oh yeah? Like what?"
        menu:
            "What should I say?"
            "I know that you'll finish your homework faster without texting!":
                $ demanding += 1
                him angry "I don't know everything, but I know that you'll finish your homework faster if you're not wasting time texting!"
                kid "Because homework is the most important thing in the universe."
                him determined "It's in the top ten."
                kid "No, it's not! Helping friends is more important."
                him annoyed "And that's what you're doing. Helping friends."
                kid "Yes! Not that I expect you to understand."
                him concerned "..."
            "I know you're talking with Oleg.":
                him determined "I know you're talking with Oleg."
                kid "Yeah? About what?"
                him "Probably stupid stuff!"
                kid "No! We're talking about how he can help his mom with the new baby!"
                him surprised "Really?"
                kid "Yeah, look for yourself."
                "She showed me the computer pad. It looked like Oleg was pretty upset that his mom was feeling overwhelmed, and [kid_name] was giving him some ideas of ways to help."
                # TODO: show her actual screen of messages?
                him concerned "..."
                kid "You think I'm just another stupid teenager, but that's just because you don't know me."
            "You're right; tell me what I should know.":
                $ responsive += 1
                him concerned "You're right. I don't know much about what's going on in your life. What should I know about?"
                kid "There's- it's- you can't just ask that now!"
                him "So you won't tell me anything."
                kid "No! It would take too long and you don't really care anyway."
                him "..."
                "She turned back to her homework."

            "Just finish up and let me use the computer pad.":
                him annoyed "Just finish up and let me use the computer pad."

    "Finally, [kid_name] was done with the computer pad. She handed it to me."
    menu:
        "What should I say?"
        "You should hang out with friends in person.":
            $ responsive += 1
            him determined "You should hang out with your friends in person. It'll mean more that way."
            kid "We don't have time! We have so much homework, and Oleg has to work in the storehouse, and I help you on the farm..." # TODO: change based on how much she is helping you on the farm?
            him normal "If you have time to chat on the tablet, then I think you have time to hang out!"
            kid "Well, he chats with me when there's no one at the storehouse and he's just sitting around."
            him happy "He could come over here after work!"
            kid "Yeah? That might be fun..."
            him normal "You can invite some other friends, too. You guys need to talk more in person. Talking online just isn't the same."
            kid "Really? Then how come you and Mom are always sending each other messages?"
            him happy "That's in addition to good, quality meatspace time."
            kid "Meatspace! Ugh, dad, that's such a gross expression. It makes me think of Travis's dad butchering cows."
            him normal "That's just one of the many exciting things happening in the real world."
            kid "That's exactly why I worry about inviting my friends over."
            him surprised "You're worried they'll find out you got your sense of humor from me?"
            kid "No! I'm worried they'll think I'm crazy like you!"
            him normal "Okay, I'll try not say anything embarassing like 'meatspace' while your friends are here."
            kid "Maybe that would be okay, then."
            menu:
                "What should I say?"
                "Make sure homework and chores are done first.":
                    $ demanding += 1
                    $ confident += 1
                    him determined "Just make sure your homework and chores are done first."
                    kid "I know, dad, I know!"
                    $ authoritative += 1
                "It'll be cool to get to know your friends.":
                    him happy "It'll be cool to get to know your friends more!"
                    kid "Dad, no, just, can you just like disappear or something while they're here?"
                    him normal "I'll try not to bug you guys too much."
                    $ permissive += 1
        "You need to concentrate more on your schoolwork.":
            $ demanding += 1
            him concerned "You need to concentrate more on your schoolwork, and less on music and talking with friends."
            kid "I thought we went over this!"
            him determined "Your schoolwork is more important. Now, don't you have a test you need to study for?"
            kid "No."
            him normal "Then study anyway, because I know you will have a test, and I expect you to get 100\%."
            kid "I'll never be perfect!"
            him determined "But if you don't try, you'll never know how good you could get. This guy on Earth named Peale said, 'Shoot for the moon. Even if you miss, you'll land among the stars.'"
            kid annoyed "We're already among the stars."
            him normal "Then maybe you need an even higher goal."
            $ authoritarian += 1
        "Thanks.":
            $ confident += 1
            him determined "Thanks, [kid_name]."
            $ neglectful += 1

    # Afterwards, depending on your attitude, she may come and ask
    # your opinion of some new music she found.
    if (responsive >= 1):
        scene black with fade
        scene farm_interior with fade
        show him normal at midright
        show kid normal at center with moveinleft
        kid "Hey dad, check out this music video I found."
        # TODO: play weird music?
        "It was a surreal video about a boy from a world of robots encountering a girl from a world of vines and flowers. They struggled to understand each other, but eventually they made a sculpture of a metal flowers together."
        "The music was repetitive and kind of grated on my ears, and the video was pretty cheesy, but [kid_name] obviously liked it."
        menu:
            "What should I say?"
            "What do you like about this video?":
                $ responsive += 1
                him surprised "What do you like about this video?"
                kid "It's a beautiful story. They're so different, but they learn from each other and work together."
                him determined "Hmmm, that's a good message."
                kid "It's not a 'message', dad, it's a story!"
                him normal "Oh yes, of course."
            "That was weird.":
                him surprised "That was weird. Do you actually like that music?"
                kid "Ugh, just never mind. I should have known you wouldn't get it."
            "Do you feel like the girl in the video?":
                $ responsive += 1
                him surprised "Do you feel like the girl in the video?"
                kid "No, I feel more like...both of them. Like they're two sides of me."
                him normal "Oh, I see. So the boy's not Oleg?"
                kid "No! Dad, we're just friends!"
                him determined "Okay, good."

        him normal "That reminds me of this other video your mom sent me when we were dating! I wonder if we brought it from Earth?"
        kid "Oh no, not one your weird old videos!"
        him surprised "It's not weird! It's romantic!"
        kid "Okay, I'll watch it, but just one!"
        # TODO: play OPS1 music?
        show her normal at midleft with moveinleft
        her surprised "Is that the video I think it is?"
        him happy "Yeah! I wanted to show [kid_name]."
        her happy "Ohh, I remember when it first came out, it was like it was made for us."
        him flirt "Like you were made for me."
    return

# 14.8 Earth years old
# Hanging out with Anya and her older brother
# Lettie dies.
label family24:
    "My horse, Lettie, was almost a member of the family. But she was over twenty-five years old, now, and it was starting to show."
    "She was the only horse on the colony; at one point there were plans for horse breeding, but when RET found precious ores they sent mining equipment instead."
    "I know [her_name] didn't really get it, but Lettie's been one of my best friends. No matter what's going on, I can always depend on her to be there when I need her."
    "And she always accepts me just the way I am."
    scene barn with fade
    show lettie at midright
    show him normal at midleft with moveinleft
    him "Hello, old girl."
    "She nickered softly in return and stepped up to me. I patted her neck and talked to her as I got her ready to ride."
    him "We're going to go pickup [kid_name] from Anya's house."
    "Lettie shook her head."
    him "I know, she's old enough to come home on her own, but it'll be dark, and sometimes it's the only chance I get to talk to her."
    him "Besides, you want a walk, right?"
    scene path with fade
    show lettie at center
    show him normal at center
    with dissolve
    "Lettie seemed to enjoy the walk. Even though she was getting older, it was good for her get out and exercise often."
    menu:
        "On the ride up to the miner's house, I told Lettie all about..."
        "[her_name].":
            him "[her_name]'s been really busy lately... there's a lot more people to take care of, and she has a hard time telling people to wait, even if their needs aren't really that urgent."
            him "I love how dedicated she is, even if it frustrates me sometimes."
            him "I guess all I can do is support her and try and make things relaxing for her at home."
        "[kid_name].":
            him "[kid_name]'s not a kid anymore . . . I wonder what she'll end up doing? Raising a bunch of kids, or researching crazy alien creatures, or farming like me?"
            him "I'm sure not ready to be a grandpa. Let's hope that doesn't happen for a long time yet."
            him "It would serve her right to have kids as stubborn as she is someday."
        "[bro_name].":
            him "I still don't get [bro_name]. He doesn't talk much, and when he does it's about things I don't get, like factories or far-off galaxies or jellysquids."
            him "But I love him all the same."
            him "Do you have to understand someone to love them? Or if I don't understand him, does it mean I don't love him enough?"
            "Lettie snorted."
            him "Sorry; I wasn't talking about you. Good point, though."
        "myself.":
            him "I remember when I used to be able to haul and lift and weed and plow all day long and not hurt at all. Sure, I'd be tired, but the next day I felt as good as new."
            him "Nowadays, after a hard day in the fields, I feel it in my back, my knees, my neck -- everywhere."
            "Lettie tossed her head."
            him "I guess you probably know what I mean, since you're getting a bit older, too."

    #scene bg miners
    "After we arrived at Anya's house, I secured Lettie's tether to the gate."
    "Lettie was breathing a little harder than usual, so I thought I'd let her take a break while I looked for [kid_name]."
    "She seemed happy to be resting, and started grazing on some small nearby shrubs."
    "Anya's father told me they had gone for a walk by the canyon."
    scene bg canyon
    show him normal at midleft with moveinleft
    "The canyon was full of interesting rocks and crags and had great views. I couldn't enjoy them, though, because it was starting to get dark. Even though [kid_name] was almost 15 in Earth years, I still worried about her after dark."
    "...Maybe especially because she was almost 15."
    him surprised "[kid_name]!"
    "My call echoed up and down the canyon. I listened carefully, but there was no response, so I walked further along."
    hide him with moveoutright
    scene bg sunset
    show him normal at midleft with moveinleft
    him concerned "[kid_name]!"
    show kid normal at midright with moveinright
    kid "Dad! I'm right here; no need to yell. What are you doing here, anyways? I was just about to start walking home."
    him "I wanted to walk home with you. Where's Anya?"
    kid "Oh... yeah, I should tell her bye. Bye, Anya!"
    "Anya yelled back through the trees."
    "Anya" "Bye!"
    "???" "Bye, [kid_name]!"
    "I heard giggling and several voices, some of which were fairly deep. [kid_name] and I started walking back together."
    him surprised "Who were you with?"
    kid "Just Anya and a few other friends."
    menu:
        "What should I say?"
        # TODO: should her response depend on your parenting style?
        "Which friends?":
            him "Other friends? Which other friends?"
            kid "No one you know! Just some people we hang out with."
            him "I know almost everyone."
            kid "Just Anya's brother and his friend. They're miners; you probably don't know them."
        "What were you doing?":
            him "What were you doing?"
            kid "Just hanging out."
            him "With boys."
            kid "It's just Anya's brother and his friend! What's the big deal?"
        "I never said you could do this!":
            him "I said you could hang out with Anya; I didn't say you could go off in the canyon with boys."
            kid "We didn't plan it like that! Anya's brother and his friend just kind of showed up and so we hiked around together."
        "How'd it go?":
            him "How'd it go?"
            kid "Fine. Anya's brother is pretty funny. He had some great snacks, too. We hiked around, took some funny pictures. You know, just stupid teenager stuff."
        "(Don't say anything.)":
            "I didn't say anything. She was allowed to hang out with friends without getting grilled by her dad, right?"
            "Besides, I didn't know what to say."
            "We walked in silence for several minutes."
            $ neglectful += 1
            jump lettie_dies

    "Anya's brother Lorant was about twenty. I didn't know much about him except that he worked in the mine and was planning on returning to Earth with his parents when their contract was up."
    "I felt wary. I could think of only one reason two twenty-something boys would hang out with young teenage girls."
    "There was a big difference between fourteen - okay, almost fifteen - and twenty."
    "I'm not sure why it was a much creepier age difference than, say, a 20-year-old and a 25-year-old. But I was definitely creeped out."
    "Then again, the dating pool was a lot smaller here. I had to remember that this wasn't Earth. There weren't a lot of teenagers or young adults to choose from."
    "But it wasn't the middle ages, either."
    menu:
        "What should I say?"
        "I'm worried you don't have any adult supervision.":
            $ demanding += 1
            him concerned "I'm worried that there's no adult supervision when you're at Anya's."
            kid "What are you talking about? Her brother's old enough to work in the mines, so how is he not an adult?"
            him annoyed "I meant {b}responsible{/b} adult."
            kid "Dad! You don't even know him!"
            him angry "I don't have to know him!"
            kid "What are you so worried about?"
        "Sometimes older teenagers get younger teenagers into trouble.":
            $ responsive += 1
            him concerned "[kid_name], I don't know if it's the case here, but sometimes older teenagers or young adults can get younger teenagers into trouble."
            kid "What are you talking about? We were just hiking around."
            him "I'm not worried about what happened today; I'm worried about what might happen next time."
            kid "We're just hanging out."
            him "It's natural to think that older kids are cool, and to be flattered if they like you or pay attention to you. But don't let them pressure you into doing something you don't want to do."
            kid "He's not pressuring me into doing anything!"
            him "I'm not saying he is. But it's something I want you to be aware of for the future."
            kid "You're not making any sense."
        "I don't want you hanging out with Anya's brother.":
            $ demanding += 1
            him annoyed "I don't want you hanging around with Anya's brother."
            kid "What?! Why not?"
            him determined "He's bad news. I can feel it."
            kid "Bad news? You can 'feel' it? What are you, a fortune teller?"
            him annoyed "Look, I know this isn't obvious to you because you're young. That's not your fault, but as your dad it's my duty to protect you."
            kid "Protect me from what? My friends?"
            him determined "This scenario has happened thousands of times. Older boy meets girl. Boy flatters girl. Girl thinks boy loves her. Boy pressures girl to do stupid things. Girl does stupid things so boy will like her. Boy leaves. Girl cries."
            kid "This is nothing like that! What are you even talking about?"
        "Just be careful.":
            him concerned "Just... be careful, [kid_name]."
            kid "Careful of what? What does that even mean?"

    him angry "I'm worried that he's going to influence you to do stupid things! Stupid things that could ruin the rest of your life."
    kid "Like what?!"
    him annoyed "A hundred things! Smoking too much fireweed, or having sex and getting pregnant or heartbroken or both, or getting drunk, or driving tractors too fast, or exploring dangerous caves, or... I don't know!"
    kid "We were JUST. HIKING."
    him angry "Yes, this time! What about next time?"
    kid "He doesn't do any of that stuff! You don't even know him!"
    him "I know what guys that age are like."
    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):
        kid "You don't know what you're talking about."
    elif (parenting_style == "authoritative"):
        kid "I get what you're saying, but that's just not what's going on here."
    elif (parenting_style == "permissive"):
        kid "Not all guys that age. C'mon, dad, you're just being overprotective."
    else:
        kid "Now you suddenly care about what I do?"

label lettie_dies:
    scene miner_camp with fade
    show him normal at left
    show kid normal at midleft
    show lettie at right
    with dissolve
    "I was about to say something when I noticed a strange smell. We were almost to where I had tied up Lettie, but something was wrong."
    "The smell was horse diarrhea, and when I ran up Lettie was trembling and shaking."
    show him normal at midright with move
    him surprised "Lettie!"
    "I knelt next to her. She was barely breathing."
    kid "Is she okay?"
    him "I don't think so. Her heartbeat's irregular and weak."
    "She had been fine on the ride up! What could have happened to make her so ill so quickly?"
    "I looked around. In Lettie's mouth I found some short, flat needles from an evergreen bush nearby."
    "The bush was not a plant native to Talaam. In fact, it looked like."
    him determined "Yew."
    kid "Me? I didn't do anything!"
    him concerned "No, a yew tree. Or bush, looks like. Who plants yew where there's horses around?!"
    "My mind raced. Yew poisoning was well-known, but there was no antidote. There were some treatments we could try...if we could get them in time."
    "I pulled out my radio. My hand was trembling and I was a lot less coherent than I wanted to be."
    him angry "[her_name]! At the miner's village... Lettie's sick. I need your help!"
    her "What's wrong with her?"
    him concerned "Yew. There was a yew bush, and she ate it... maybe a lot of it."
    "I knew I should give her more information, but my brain felt stuck, as if mired in glue."
    her "I'll bring activated charcoal and the stomach pump right away."
    "Lettie convulsed, and I patted her on the side of her neck."
    him "Okay, okay old girl. [her_name]'s coming."
    "But by the time [her_name] arrived, it was too late."
    "Lettie's heart had stopped."
    show her normal at center with moveinright
    her sad "I'm so sorry, [his_name]."
    "I sensed sort of distantly that [her_name] and [kid_name] were saying comforting things and had their arms around me."
    "Lettie had been with me even longer than [her_name]. We'd grown up together."
    "And now she was gone."
    scene black with fade

    "That whole evening was kind of a blur. Thuc arrived with his tractor and a big trailer. Anya and Lorant and Oleg showed up and together we all managed to get Lettie's body into the back of the tractor."
    "[her_name] must have called them. She probably knew we'd end up having to move Lettie, one way or another."
    "I didn't cry, but I didn't say much, either. I just concentrated on the next thing to do."
    # TODO: change who helps based on community scores?

    "We buried her near the garden. I planted a tree on top of her grave -- an apple tree. She sure loved apples. It doesn't get cold enough here to set fruit most years, but that didn't matter."

    "I missed her. But more than that, I felt like she shouldn't have died -- her death never would have happened if Anya's family hadn't put that yew bush right by their front gate."
    "Or if I had noticed it when I tethered her to it."

    "I couldn't stop thinking about it when [her_name] invited Anya and her brother over to hang out."
    "Their family never even apologized to me for Lettie's death from their yew bush."
    "I didn't say anything when they were here, but afterwards I felt like I would explode if I didn't talk about it."
    "So I posted on the farmer's community board."

    him_c "You probably heard Lettie died. She died of yew poisoning from a bush planted by some miners."
    him_c "I hope everyone knows this plant is poisonous to livestock and humans."
    him_c "I don't know why anyone would even bring it to Talaam; it's deadly and doesn't provide food. I think I'm even allergic to it."
    him_c "I hope the owners will rip that plant out and destroy it so no one else gets hurt."
    sara_c "I'm sorry for your loss, [his_name]. I'm sure whoever planted it wasn't thinking anyone would eat it. 🙁"
    julia_c "Lettie was a good horse."
    brennan_c "Yew's a tough plant that can grow almost anywhere and is symbolic of death and rebirth."
    brennan_c "The Lewis' were thinking of these qualities and not its horse-murdering tendencies."
    her_c "I'm sorry about Lettie, too, but yew is also useful for treating some types of cancer. We shouldn't just destroy it."
    him_c "But why do we need it here, on Talaam?! We have a chance to start from scratch, to only bring the best things from Earth!"
    him_c "Instead we contaminate our planet with poisonous weeds and people that don't even give a damn."
    her_c "[his_name]!"
    sara_c "😢"
    him_c "If you don't pull out weeds, they'll suck the life out of all the good plants you're trying to grow."
    if (is_liason):
        brennan_c "I'm going to pretend I didn't hear the RET liason comparing our entire mining operation to poisonous weeds."
        brennan_c "If anything, you guys are the parasites. Where do you think all your technology and supplies come from?"
    else:
        brennan_c "I'm sure you'd be ecstatic if RET's entire operation just keeled over tomorrow."
        brennan_c "Maybe you'll be joining Pete next, living on your own far away from all us poisonous weeds."

    "Ugh. I hated hearing that from Brennan."
    "But the yew tree was just a symptom of a much larger problem."
    # TODO: make sure it's OK to change these community variables here.
    menu:
        "That problem was..."
        "The miners and RET were ruining our planet.":
            $ luddites += 1
            "The miners and RET were ruining our planet."
            "I mean, I guess it was only because of RET that we had the funding to come here in the first place."
            "But I wished they'd just leave us alone. I wished they would leave [kid_name] alone."
            "It was a futile wish, though, and one I couldn't afford to indulge."
        "Strife and division threatened to destroy our community.":
            "We were always fighting. I thought that away from Earth's politics and territorial squabbles, we'd be able to find true peace."
            "Away from Earth's materialism and fads, I thought my kids and farm would be safe."
            "But we were still human. And apparently 'human' means 'conflict'."
        "All these problems were distracting me from my farming.":
            $ colonists += 1
            "I didn't have time for all this crap. All I wanted to do was grow my crops and herds and raise my family in peace."
            "But even when I was light years from home, there were still other people to deal with."
            "People harming me, my horse, [kid_name]."
            "And I had to deal with that."
        "I was a jerk.":
            $ miners += 1
            "I was the problem."
            "I was a selfish, whiny jerk who just wanted someone to blame."
            "I knew I needed to forgive, but I couldn't just yet."
            "And even if I forgave them, I'm not sure I could ever trust that family."

    "[her_name] interrupted my musings."
    her "Hey, sweetie."
    him "Hey."
    "She sat next to me and held my hand."
    her "You weren't just talking about yew plants."
    "I shook my head."
    her "You think Lorant is a bad friend for [kid_name]?"
    "I shrugged. I felt like a fool. I shouldn't have posted about Lettie's death online, and I didn't know what to do about the creeping weeds of my life."
    her "Well, I agree with you. He's too old for her, and he gives me the creeps. I'm all for giving people a fair chance, but I'm not trusting him alone with my daughter."
    him "You don't think I'm just crazy with grief?"
    her "I think posting on the message board like that was a stupid and tactless thing to do, but you make a fair point. We can be good neighbors and support the miners without trusting Anya's brother with our daughter."
    him "She's not going to like it."
    her "I'm a doctor; I'm used to people not liking their treatments, whether its pills or cryotherapy or an IV or whatever. But, like at the clinic, perhaps if we approach this the right way we can minimize her discomfort."
    menu:
        "What should we do?"
        "Forbid her from hanging out at Anya's house.":
            him "She just can't hang out at their house!"
            her "I agree. They're unsupervised, far from any public areas, and there's too many creeps in that area."
            him "There's more than one?"
            her "I'll just say that my supply of morning-after pills is starting to run a little low."
            him "...wow."
            him "Shouldn't people know about stuff like this?"
            her "You know I don't reveal things about my patients. And there's no laws being broken. Everything was consensual, or so they tell me, but there's a big difference between 'consensual' and 'a well-thought out plan'."
            him "So I'm probably not the only one that feels this way."
            her "Definitely not."
            him "Okay, good. [kid_name]'s not going to like it, though."
            her "Too bad. It's what she needs."
            $ authoritarian += 1
        "Encourage her to have her friends over to our house more.":
            him "Maybe we could just encourage her to have friends over to our house more often?"
            her "That's a start..."
            him "I mean, nothing's serious yet... right?"
            her "She claims he's just a friend."
            him "Then there's no need to get all dystopian on her. We'll just make our house a fun hangout place."
            her "Okay, I hope that works."
            $ permissive += 1
        "Get [kid_name] to help solve the problem.":
            $ confident += 1
            him "Why don't we ask [kid_name] to help us with this problem?"
            her "Won't she be a bit biased?"
            him "We don't have to do what she says, but if she's invested in the solution she'll be more likely to follow it without complaining."
            her "We could try..."
            "We went to [kid_name]'s room."
            him "[kid_name], we would like your help with a problem."
            kid "What's that?"
            him "We are a bit worried about you hanging out at Anya's house where it's so far and there's not a lot of adults around. We want you and Anya to still be able to hang out, though."
            kid "You could just get over it."
            her "Look, we didn't have to ask your opinion--!"
            him "Hey, calm down. [kid_name], we thought you might have an idea about where you and Anya could hang out that is in a safer place with more people around."
            kid "There's nothing wrong with her house."
            him "As your parents, we're not comfortable with that. What other options are there?"
            kid "You want something with more people around? No one wants to do that."
            him "How about something a bit more centralized; closer to town. So if there's an emergency you'd have plenty of people close by."
            "[kid_name] thought about it for a minute. That was progress; she finally wasn't just trying to shut me down."
            kid "Actually, it'd be cool if we had our own hangout place. Like, in books I always read about teenagers hanging out at malls or cafes or parks or places like that. We don't really have that here."
            her "We haven't had that many teenagers before."
            him "That's a great idea, [kid_name]!"
            kid "But you guys can't come there! That would defeat the whole purpose."
            him "Let's see what we can work out."
            "We worked with the community, and some groups agreed to meet in the school instead of the community center so that the teenagers could have the community center to themselves several evenings a week."
            "[kid_name] worked with Anya and some other friends to make a ping pong table and some soft rugs. They talked about future plans, too, like a mini-kitchen and some big speakers for music."
            her "This is a great project for [kid_name] and her friends. And people are around the community center all the time, so it'll be easy for us all to keep an eye on them without being too intrusive."
            him "Like with the surveillance cameras you installed?"
            her "You noticed that, huh? Well, they don't need to know about those."
            $ authoritative += 1

        "Let [kid_name] make her own decisions.":
            $ confident += 1
            him "It's her life; if she wants to ruin it why should we get in her way?"
            her angry "Because she's our daughter! Because she doesn't even know what she's doing!"
            him "Are you sure about that? Maybe she does know what she's doing!"
            her "Are you serious? How much of life did you understand at fourteen years old?!"
            him "Enough to know that I wanted to make my own mistakes and for my parents to leave me alone!"
            her "That's what you wanted then, but looking back, aren't you glad they didn't?"
            him "..."
            her "Fine. I guess this is something I'll handle on my own."
            him "Good."
            $ neglectful += 1
            $ marriage_strength -= 1

    return

# 15.5 Earth years old
# Thinking about the future
# foreshadowing ending
label family25:
    scene black with fade
    "[her_name] was busier than ever. Not only did she have to treat the miners from RET and deal with all their extra paperwork, but she also did routine checkups for the colony."
    "Her duties only increased as the number of babies increased and as people got older."
    scene farm_interior with fade
    show him normal at midright
    show kid normal at midleft
    with dissolve

    him concerned "Mom won't be home until later, and [bro_name]'s helping her out, so it's just you and me again."
    if (is_attached()):
        kid "Okay. Want me to fix something?"
        him "Sure, I started these potatoes earlier but let's make some squash to go with them."
    else: # not attached
        kid "Okay."
        him "Let's make some dinner. I already have potatoes; we just need some squash."
        "She rolled her eyes and sighed, but washed her hands and got ready to help."

    if (is_independent()):
        kid "I can handle it by myself dad."
        him "Are you sure?"
        kid "Yes! I know you're trying to finish harvesting, so come back in an hour and I'll have it all ready for you."
        him "Thanks, [kid_name], that'd be great."
        scene black with fade

        if (is_competent()):
            "When I came back an hour later, she had the table set, the potatoes were smothered in a creamy goat cheese sauce, and the squash was roasted with a bit of a caramel edge to it."
            him "Wow, this is delicious!"
            kid "It's just dinner..."
            him "You're a great cook. I'm glad I don't have to worry about you starving to death when you're living on your own someday."
        else: # independent but not competent
            "When I came back an hour later, there was some weird kind of creamy potato squash soup thing on the table."
            "There was a faint bitterness in the air, like something had been burning recently."
            kid "...Dinner's ready."
            "The gloppy soup had bits of squash that were somehow both burned and undercooked at the same time."
            "I ate it, though, and so did she."
            him "Thanks for, ah, making dinner."
            kid "It's kind of gross."
            him "...yeah."
            kid "You're not supposed to say 'yeah'!"
            him surprised "What am I supposed to say?"
            kid "You're supposed to lie and tell me it's good!"
            him "Sorry, [kid_name]. I wasn't going to complain, but you brought it up."
            kid "I'm just a terrible cook."
            him "You just need more practice. It's okay, though, you still have some time before you'll be living on your own."
    else: # is attached but not independent
        "I peeled and chopped the squash, and she got some goat cheese to make a creamy sauce for the potatoes."
        him "Use low heat for the cream sauce."
        kid "I know! Dad, I'm not a little kid, I can cook."
        "I kept my mouth shut but kept an eye on her as we prepared the food together."
        if (is_competent()):
            "And you know what? She was right. She did know what she was doing."
            "She skimmed a little cream from the top of the goat's milk and mixed it with potato starch to make a roux."
            "She added some more milk and goat cheese, and a delicate sprinkling of spices that smelled heavenly."
            "The cream sauce melded with the soft potatoes to make the perfect comfort food."
            him happy "You're a great cook. I'm glad I don't have to worry about you starving to death when you're living on your own someday."
        else:
            "She dumped the cheese in the pan and heated it up. Maybe I had never taught her how to make a cream sauce..."
            "Then she added a bunch of salt."
            "The result was really salty goat cheese potatoes."
            him "Thanks for cooking with me. Hard to believe you might be cooking for yourself in just a few years, huh?"

    kid "Yeah... you and mom went to college after high school, right?"
    him "Your mom did -- for a long time. I went part-time for a while, but I had to quit to help my parents on the farm."
    kid "Can I go to college?"
    "That was a good question. Teenagers on the colony usually ended up mostly doing what their parents did, though some like Miranda also earned degrees via independent study."
    him "Miranda earned a biology degree studying with Dr. Lily. I think anyone who wants to could do that, too."
    kid "But you don't need a college degree to do most stuff here."
    him "No, but learning is always good. What do you want to study?"
    kid "I don't know! I like a lot of things. Music, jellies, fossils, reading, the stars..."
    him "And farming?"
    kid "Maybe. I like to eat, anyway!"
    him "Hunger is a powerful motivator."
    kid "Anya says she's going to be a miner. Her brother just started and he already earns a lot of money."
    him "But aren't they leaving in a few years?"
    kid "Yeah, but she can at least work until then...It just seems like there's not many choices here on Talaam. If you're not a farmer or a miner, why are you even here?"
    menu:
        "What should I say?"
        "We need other people, too.":
            $ responsive += 1
            him "We need people to do other things, too. Sara, and Ilian aren't farmers, but imagine how disorganized we'd be without them!"
            him "Or how much less we'd know without Zaina's studies, or how many people would have died without your mom there to fix them up."
            him "I love farming, but if you don't want to do that, there's plenty of other great things you can do to help the colony."
            kid "Thanks for the speech, dad."
        "Miners and farmers can do other things, too.":
            $ responsive += 1
            $ demanding += 1
            him "Just because you're a miner or farmer doesn't mean that's your whole life. Pete still reads lots of books, and Joanna paints, and Thuc juggles..."
            kid "What about you?"
            him "Well... when I have free time, I want to spend it with my wife and kids. And, well, uh..."
            kid "What?"
            him "And sometimes I write bad poetry."
            kid "Ha ha, that's true. So you're saying I could be a farmer and still be into music?"
            him "Yeah, you don't need a college degree for that. And you don't need a college degree to read books and learn stuff, either."
        "Earth has a lot more opportunities.":
            $ demanding += 1
            him "Honestly, Earth has way more opportunities for things to study."
            kid "Yeah! I'd love to see it someday."
            him "I'd like you to see it, except... I don't know if you could come back."
            kid "Yeah..."
        "Good question.":
            him "Good question. I wonder the same thing sometimes."
            kid "So... if I don't want to be a farmer or a miner, why would I stay?"
            him "Maybe you don't want to leave your family?"
            if (is_independent()):
                "She looked at me like I was crazy. If she left, she probably wouldn't miss us at all."
            else:
                "She looked at me appraisingly, like she was trying to decide how much my friendship was worth. It made me want to impress her, to show her how awesome our family was so she would stay."
                "But that was silly. I was her dad."

    #TODO: foreshadow ending here
    if (is_attached()):
        if (is_competent()):
            if (is_independent()):
                "ACI"
            else:
                "ACi"
        else:
            if (is_independent()):
                "AcI"
            else:
                "Aci"
    else:
        if (is_competent()):
            if (is_independent()):
                "aCI"
            else:
                "aCi"
        else:
            if (is_independent()):
                "acI"
            else:
                "aci"

    kid "What do you think I should do?"
    menu:
        "What should I say?"
        "Follow your heart!":
            him "You should follow your heart. If you can't do what you love, there's no point in being alive."
            kid "But what if following my heart doesn't make any money? I'm going to need to eat."
            him "Yeah, you might need to work at a job you don't like very much to support your passion. Or find someone else who will support your passion."
            kid "Like marry a rich guy?"
            him "Uh, that's one way, I guess..."
            kid "Ha ha, I'm just kidding, dad!" # is she really?
            $ permissive += 1
        "You need to be able to support your family and community.":
            $ confident += 1
            him "You have a duty to help support your family and community. That needs to come before your personal desires."
            kid "So you think I should be a farmer."
            him "I think that instead of asking 'What do I want to do?' you should ask 'What does the colony need me to do?'."
            kid "Which is farming."
            him "Maybe! There's other important things, too. It's like John F. Kennedy said -- 'Ask not what your country can do for you – ask what you can do for your country.'"
            kid "Even if I don't want to?"
            him "It's not a matter of wanting; it's a matter of duty. Your family and community have supported you and raised you. It's your duty to support them."
            $ authoritarian += 1
        "Be the best at whatever you choose.":
            $ confident += 1
            him "You have a lot of choices here, but whatever you choose, do your best in a way that helps people."
            if (plays_saxophone):
                kid "But some things don't really help people all that much. Like, how does it help the community if I practice my saxophone or play with jellies?"
            else:
                kid "But some things don't really help people all that much. Like, how does it help the community if I play with jellies?"
            him "I bet you can find a way to share your passion with the community."
            kid "Huh, maybe. I never really thought about it before..."
            $ authoritative += 1
        "I don't care.":
            him "I don't really care what you choose. That's totally up to you."
            kid "You don't care at all?"
            him "Nope."
            "I was her dad, not her career counselor. It was none of my business and she probably wouldn't listen to me anyway."
            "Though she did look a little disappointed."
            $ neglectful += 1
    return

# 16.1 Earth years old
# Do you invite her to join you for chores so she can learn, or let her have time with friends?
# She thinks eating jellies is wrong! Maybe eating all animals is wrong?
# She calls you names. Do you argue, or discuss what makes something sentient?
label family26:
    # TODO: join these two things together somehow
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

# 16.7 Earth years old
# Financial Responsibility & Bikes
label family27:

    scene farm_interior with fade
    show him normal at midright with dissolve
    show kid normal at midleft with moveinleft
    "I was about to go to bed when [kid_name] came into the room."
    kid "Dad, I need a bike."
    him surprised "A bike?"
    kid "Yes! I'm so sick of walking to school and back every day!"
    him "It's not that far."
    kid "And, not just school, but going to town, too. Every time I want to go it takes me half an hour just to walk there."
    him surprised "Is that really why you want a bike?"

    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritative"):
        kid "I would be a lot more useful to this family with a bike. I could go shopping for you and even ride it around the farm when we work together."
    elif (parenting_style == "authoritarian"):
        kid "It would let me be more independent. Like, if I wanted to get a job somewhere, I would have a way to get there quickly on my own."
    elif (parenting_style == "permissive"):
        kid "I've read about bikes in so many books - they're like a totally normal kid thing, and I've never even ridden on one! Oleg's mom has one I've seen her riding around, so I know it's possible!"
    else:
        kid "I just really want one."


    him "Do we even have any bikes?"
    # TODO: currency check
    $ bike_cost = 300
    kid "I asked Oleg's mom, and she said she made it. It cost her about [bike_cost] credits worth of materials, plus finding the right kind of plant for the frame."
    him surprised "She uses a plant for the frame?"
    kid "It's a sturdy, hollow plant with lightweight wood."
    him determined "Huh. Seems like you've looked into this a bit."
    kid "Yeah, all I need are the [bike_cost] credits! I can find the plants myself!"
    him concerned "[bike_cost] credits is a lot!"
    kid "Please, dad?"

    menu:
        "What should I do?"
        "Buy her a bike":
            $ responsive += 1
            him surprised "I remember when I first got a bike with gears... it was red, and I attached a playing card to the spokes so it would sound like a motorcycle."
            kid "A motorcycle is like a motorbike, right?"
            him normal "Kind of... Anyway, I agree that you should have a bike. I'll transfer you the credits."
            kid "Okay, good."
            $ permissive += 1

        "Have her use her own money.":
            $ demanding += 1
            $ confident += 1
            if (allowance_amount > 0):
                # TODO: make sure this makes sense with the numbers
                him "You have an allowance, you know. You could save up for it yourself."
                $ saving_weeks = int(round(float(bike_cost) / float(allowance_amount)))
                kid "What?! That would take me like..."
                "She did some calculations in her head."
                $ saving_months = saving_weeks / 4.0
                kid "...[saving_weeks] weeks! That's [saving_months] months, which is way too long for me to wait."
            him "You could earn your own money."
            kid "Doing what?"
            him "Whatever people need."
            if (parenting_style == "permissive"):
                kid "I'm not going to do whatever people want!"
            else:
                kid "That's not very helpful."

            him "Well, if you want a bike that badly, I bet you'll be able to find something you can do to earn money. Remember when you sold those jellyfish shells?"
            kid "Maybe... But who would I even ask?"
            # TODO: have these based on stats? or increase stats?
            menu:
                "What should I tell her?"
                "Ask in town.":
                    $ responsive += 1
                    him "You could ask around in town, see what people need."
                    kid "Okay..."
                "Find a need and offer to help.":
                    $ responsive += 1
                    him "Look around and see what people need help with. Then find a way to help them and offer to help for a fair price."
                    kid "How do I know what people need?"
                    him "Look on the message board, or ask someone who's connected to the community."
                    kid "Too bad Sister Naomi's not here anymore..."
                    him "Yeah, she'd probably have some great ideas. But Pavel or Ilian might know something, too. Or you could ask mom."
                    kid "Okay."
                "Ask the miners.":
                    $ responsive += 1
                    him "Ask the miners. They work pretty hard all day, and they usually have a lot of credits, so maybe there's things you could do that they would pay for."
                    kid "Okay, I'll ask next time I go see Anya."
                "Ask Pete.":
                    $ responsive += 1
                    him "Ask Pete. He might not be able to pay in credits, but he has stuff you can't get anywhere else that other people might pay well for."
                    kid "He lives so far away. If I had a bike, maybe that would work. I'm going to ask the miners."
                "Figure it out yourself.":
                    $ demanding += 1
                    him "I'm sure you'll figure something out."
                    kid "Thanks for nothing."

            "[kid_name] found a job tutoring some kids in one of the miner families."
            "It paid pretty well, but she often didn't get home until after dark."
            $ authoritative += 1
            # TODO: decrease her amount of available work?
        "Don't buy her a bike.":
            him annoyed "Sorry, I don't have 300 credits lying around. Your feet will work just fine."
            kid surprised "That's it? Just 'No'?!"
            him angry "I don't have time to discuss it! Go figure it out yourself if you want a bike so bad!"
            kid angry "Maybe I will!"
            $ neglectful += 1
        "Offer to buy her one in exchange for more work.":
            $ demanding += 1
            $ confident += 1
            him "I can understand why you'd want a bike. If I didn't have Lettie, I'd probably want one, too."
            kid "Yeah! So you'll get me one?"
            him "Well, not for free."
            kid "Oh no. What do I have to do?"
            him "If I'm going to be paying for your bike, then you'll need to do work for me on the bike."
            kid "Okay, like what?"
            him "Anything I ask."
            kid "But... what if I have homework, or I'm tired, or I don't want to do it right then?"
            him "Those are my terms. If I buy the bike, then I get a say in how the bike is used."
            kid "That's not fair! You're going to make me waste all my time doing your work!"
            him "C'mon, I'm not that mean. It'll probably just be a trip to the storehouse once in a while or something."
            if (is_competent() and is_independent()):
                kid "Then I want that in writing. I don't want to be your bike slave."
                him "I'm not sure whether to be impressed or exasperated."
                kid "Both?"
                "We laughed together, and drew up a short contract specifying what exactly I expected from her in return for buying her the bike."
                $ demanding += 1
                $ authoritative += 1
            elif (is_attached()):
                kid "C'mon, dad. Please just let me have a bike? I promise I'll help out sometimes."
                him "I'll hold you to that."
                $ authoritarian += 1
            else:
                kid "That's not fair!"
                him "I'm the parent; those are the rules."
                $ authoritarian += 1


    # TODO: fit this in somehow?
    # TODO: different job depending on personality/ending?
    "[kid_name] finally got her bike, which was good, but it also meant we didn't see her as much."
    "She attached a little cart to the back and started delivering things for people all over the colony."
    "She'd deliver fresh groceries to the miners, supplies to Pete, and even started taking some little kids home from school."
    her concerned "I'm worried about [kid_name]'s job..."
    him surprised "What? Why?"
    her determined "It takes up a lot of time; she's exhausted by the time she gets home but she still has to do homework."
    him concerned "Yeah, she hasn't had much time to help on the farm lately, either."
    her surprised "Maybe she should quit and concentrate on her schooling..."
    him determined "No way. It's good for her to do something real and useful. She'll use that way more in life than whatever random stuff they're teaching her in school."
    her annoyed "It's not 'random stuff', it's math, literature, science, social studies -- you know, the stuff that makes us human."
    him annoyed "Yeah, but she's almost 18. She needs to start exploring what she's going to be doing here as a contributing adult."
    her angry "What about college?"
    him normal "All they have here is independent study. I think she'd be better off starting to work and then studying more what she actually needs."
    her annoyed "A college education is important."
    him annoyed "When was the last time you used calculus? History? And you don't need a class to enjoy a good book or think about philosophy or whatever."
    her determined "I use math all the time at work."
    him determined "But not calculus."
    her concerned "...No, but I use the same kind of thinking and complex problem-solving and abstraction that calculus trains you to do."
    him determined "Okay, what about history?"
    her determined "History is all about finding the common threads among humanity. Since we moved here, it's become even more important to me."
    him surprised "How?"
    her concerned "The parallels help me understand our situation better."
    him annoyed "Like what?"
    her determined "In some ways we like the settlers on the Oregon Trail -- forging a new path, exploring, and trying to make a wild, lonely place a home."
    her concerned "Understanding the grievances of populists and revolutionaries throughout history helps me undestand why Pete left -- and to be wary of what RET could become."
    him determined "Okay, but [kid_name] could still work and study at the same time."
    her determined "She still has a lot to learn. I don't want her to miss out on important parts of her education."
    $ parenting_style = get_parenting_style()

    # TODO: Make this affect available work or something.
    menu:
        "What should I say?"
        "We should encourage her work.":
            him concerned "The reality is, everyone needs a job here. She might not do this job forever, but I think this type of practical education is just as important as more abstract studies."
            her concerned "It is good to see her excited about doing real work."
            him determined "It might be a good opportunity for [bro_name] to step up and do more on the farm, too."

        "We should make her quit.":
            him concerned "Maybe you're right..."
            her concerned "We should let her be a kid as long as possible, and get as much schooling as she can."
            him determined "And I still need her help on the farm. Even with her and [bro_name] both helping me, it's tough to keep up with the demand for crops."

            scene black with fade
            "But [kid_name] did not take the news well."
            kid "What do you mean, I can't work? Aren't you always the ones telling me I should work hard, be responsible, figure out what I'm going to do when I grow up??"
            her concerned "There's still a lot you need to learn. Right now your schooling is more important."
            if (parenting_style == "authoritative"):
                kid "Maybe you're right..."
                $ family27_no_work = True
            elif (parenting_style == "authoritarian"):
                kid "You want me to be a productive and useful adult, right?"
                him determined "Yes, but we also want to you to get a good education and help out at home."
                kid "How about if I can keep my job as long as I also do my chores and do my schoolwork?"
                "She had a point. But we were the parents, and it was our job to do what was best for her. Hopefully we knew what that was."
                "I looked at [her_name]. She shrugged. I guess this decision was up to me."
                menu:
                    "What should I say?"
                    "You have a deal.":
                        $ responsive += 1
                        him normal "We can try it. But I expect you to get good grades and do your chores. Whatever work you can fit in around that is fine."
                        kid "Thank you, dad! I'm glad you listened to me."
                        "Hopefully I wouldn't regret this..."
                    "No deal. You may not work.":
                        him annoyed "[kid_name], I said no. Stop arguing!"
                        kid "You never listen to me! Whose life is this anyway?!"
                        her concerned "Sweetie..."
                        kid "Sorry, mom, I don't have time. I have to go cram my head full of useless facts instead of doing real work."
                        "She left to her room."
                        "Hopefully we were doing the right thing..."
                        $ family27_no_work = True

            elif (parenting_style == "permissive"):
                kid "No! You guys can't be serious?! I always get good grades and do everything you ask, why can't you just let me do what I want?!"
                him "Sorry, [kid_name]. We just want what's best for you."
                kid "Well maybe next time you could bother to figure that out! Hint: it's not quitting my job!"
                her "[kid_name]..."
                "She left to her room."
                "Hopefully we were doing the right thing..."
                $ family27_no_work = True
            else:
                kid "I'm sick of working on this farm! Why can't you let me choose my own life?!"
                him "Sorry, [kid_name]. We just want what's best for you."
                kid "No, you just want what's best for {b}you{/b}."
                "She left to her room."
                "Hopefully we were doing the right thing..."
                $ family27_no_work = True

        "We should let her decide.":
            him determined "This should be her decision. We should make sure she knows what she's choosing between, and encourage her education, but it's her life."
            her concerned "She's still a kid, though..."
            him annoyed "Not for long. If she doesn't make big decisions now, how is she going to learn how to make them when she's not a kid?"
            her flirt "Our little baby is growing up..."

        "We should only let her work if she keeps her grades up.":
            him concerned "Her studies are important, but so is her work. So I think she should only be able to keep working if she can also make sure to do all her schoolwork."
            her concerned "That sounds like a lot of stress."
            him determined "If she's busy, she's not getting in trouble, right?"
            her normal "Let's hope so."

    if (not family27_no_work):
        $ confident += 1
    return

# 17.3 Earth years old
# Terra's job, plans for future
# TODO: make sure this is consistent with community events
label family28:
    scene farm_interior with fade
    show him normal at midleft
    show her normal at midright
    show kid normal at center
    with dissolve

    kid "I'm heading out. Bye."
    her concerned "Okay, be home for dinner."
    him "She sure has been gone a lot lately."
    her "Do you think she's okay?"
    him "I don't know..."
    if (family27_no_work):
        "We had told [kid_name] she couldn't work, but she still left on her bike a lot."
        "She said she was hanging out with friends, but I was a little suspicious."
    else:
        her "Her job sure keeps her busy."
        him "If that's really what she's doing."

    menu:
        "What should I do?"
        "Investigate.":
            $ demanding += 1
            him "I'm going to investigate."
            her "I'll help."
            him "You follow her; I'll ask around."
            her "You want me to follow her? How, fly?"
            him "You're still a decent runner, aren't you?"
            her "You just want to see me get hot and sweaty."
            him "Wish I could!"
            "She left, and I turned to my computer pad. There were several ways I could go about this..."
            nvl clear
            menu:
                "Ask around.":
                    "I decided to ask around. Maybe someone else had seen her."
                    if (luddites > 10):
                        him_c "Hey, Pete, I'm looking for [kid_name]. Any idea where she's at?"
                        pete_c "She usually comes over here around this time. Want me to tell her something?"
                        him_c "Oh, is she hanging out with Travis?"
                        pete_c "No, making deliveries. I thought you knew that."
                        if (family27_no_work):
                            him_c "Yeah, well, she said she wasn't doing that anymore."
                            pete_c "Huh. Well, she is."
                            him_c "Thanks, Pete."
                            "So she usually rode all the way to Pete's house, but not to hang out with Travis..."
                        else:
                            him_c "Yeah, I do. Just checking up on her."
                            pete_c "Ha! You're about as sly as a hippo, you know that?"
                            him_c "Yeah, yeah."

                    if (miners > 10):
                        him_c "Brennan, have you seen [kid_name]?"
                        brenann_c "Not today."
                        him_c "You don't happen to know where she's at?"
                        brennan_c "No. Sorry."
                        "It was hard to tell online, but it seemed like he was hiding something."

                    if (colonists > 10):
                        him_c "Hey, Sara, any idea where [her_name] is? I'm looking for her..."
                        sara_c "Oh, she was just here, buying some stuff from Ilian. 😃"
                        him_c "What kind of stuff?"
                        sara_c "Ilian says... oil and salt? Like, a lot of it."
                        him_c "Really..."
                        sara_c "I think she's running errands for Pete or something because she rode off in that direction."
                        if (family27_no_work):
                            "Sounds like she was still doing her delivery job."
                        else:
                            "It sounded like just a delivery business..."
                "Check the security cameras.":
                    "I still had access to the community center surveillance cameras."
                    "She wasn't in the teen hangout area, but when I checked the external camera, I saw her exit the storehouse and load up her bike with supplies."
                    "Looks like she was still doing her delivery job..."

                "Send her a message.":
                    him_c "Hey, where are you?"
                    kid_c "I'm just out, biking around. Why? I already finished my homework!"
                    him_c "Are you near the storehouse? I could use some more rice."
                    if (family27_no_work):
                        kid_c "Okay, dad."
                    else:
                        kid_c "That's too heavy, dad! I'm already taking a bunch of oil and salt to Pete."
                "Ask her friends.":
                    "I sent a message to all her friends, asking if they knew where she was."
                    oleg_c "She was just here, but she left with a bunch of oil and salt."
                    travis_c "Why are you looking for her?"
                    him_c "I'm her dad. It's my job to know where she is."
                    travis_c "She's fine. Don't worry about her."
                    him_c "...so where is she?"
                    "I didn't get any further response."
            if (family27_no_work):
                "So. She was delivering goods, even after we had told her not to."
                "That's what she was hiding."
            else:
                "She didn't seem to be hiding anything, but I still felt uneasy."
            nvl clear
            "I told [her_name] what I found out."
            her_c "Okay, I don't think I can make it to Pete's before she leaves. I'll head over to the miner's camp and see if she comes there."
            "I waited. I didn't hear anything from [her_name] for a long time, until..."
            her_c "Found her. Coming home. Talk more when we get there."

        "Leave her alone.":
            him "She's probably fine."
            her "I'm not so sure. I'm going to investigate."
            him "Really?"
            her "Yes. I just have a feeling that something's off here."
            him "Well, let me know what you find out."
            scene black with fade

    scene farm_interior with fade
    show him normal at midright with dissolve
    show her normal at center
    show kid normal at midleft
    with move

    her concerned "She was delivering firegrass and alcohol to Brennan, for the miners."
    kid "I wasn't using any of it! I just deliver it!"
    her determined "Pete sells the stuff to her and she sells it to the miners for a profit."
    menu:
        "What should I say?"
        "Good job!" if (not family27_no_work):
            $ responsive += 1
            $ confident += 1
            him happy "Wow, that's great! I bet you're earning a ton!"
            her "[his_name]!"
            kid "Not too much. I just deliver it."
            him "How much do you make?"
            kid "About 10 an hour." # TODO: currency check
            him "Not bad, but you could probably charge a bit more. It's not like you have competition."
            kid "If I charge too much, Pete will just deliver it himself."
            him "True, true."
            her "You're really okay with your daughter making money off these dangerous substances?"
            him "People are going to use them whether she brings them or not. She's just delivering whatever people need."

        "What are you, a drug dealer?":
            $ demanding += 1
            him angry "What are you, a drug dealer?!"
            kid "Dad, it's just some cider and some fire grass. Fire grass is not that different from the coffee you're always wishing you had."
            him "You're enabling people to keep using the stuff!"
            kid "People are going to use it whether I deliver it or not! I'm making good money with this."
            him "Money's not the only issue!"

        "Tell me more, [kid_name].":
            $ responsive += 1
            $ confident += 1
            him surprised "Tell me more about this."
            kid "It's not a big deal. I just take some supplies to Pete and the miners and they pay me. It's not like I'm getting drunk or stoned or anything."
            her annoyed "Not yet."

        "You were supposed to stop this job!" if family27_no_work:
            $ demanding += 1
            him angry "You were supposed to stop this job! You need to concentrate on your studies, not be running around the colony delivering drugs!"
            kid "I'm almost an adult now! I'm not going to be living on your farm and going to school forever!"
            her "That is true, but while you live at our house, we expect you to follow our rules."
            kid "Even if they're stupid."
            her "Yes, even if they're stupid."
            kid "Then maybe I shouldn't live at this house."
            menu:
                "What should I say?"
                "Fine! Leave!":
                    him angry "Fine! Leave, then! Try living on your own and see how you like it!"
                    kid "I will. I'm sick of your arbitrary rules and you making decisions for me."
                    her "[kid_name]..."
                    kid "No, I should have done this months ago. I'm done with this house, with your stupid rules, with... you!"
                    # TODO: does she actually leave?
                    $ neglectful += 1
                    jump family28_run_away
                "Think about it and decide for yourself.":
                    him determined "If you think that's best. But before you decide, will you think about it and make a plan?"
                    kid "A plan?"
                    him "Yeah. You know, where you're going to stay, how you'll earn money, what you'll eat. Stuff like that."
                    her "Don't leave just because you're angry. Leave because you're really ready to live on your own."
                    kid "I... I'm not ready to leave yet. But I'm not quitting this job, either."
                    him normal "I can see that this job is very important to you."
                    her "But it's probably not what you want to do for the rest of your life."
                    kid "I love it, mom! People need me, I'm useful, and I get paid."
                    her "I know. I'm willing to let you work at this job if you will also start making some long-term plans."
                    kid "Like what?"
                    her "Like studying or apprenticing. A delivery service is a great job for you now, but does it pay enough for you to live on your own? To support a family?"
                    kid "Probably not. But I don't have a family right now!"
                    her "I know. But someday you might want one. So how about if you keep working at your job, but you also make some goals for what you want to do in the future."
                    him "If you will do that, we'll let you keep your job."
                    kid "You'll {b}let{/b} me?! Ugh!"
                    "[her_name] shot me a glare. I was just trying to help, but maybe I'd let her handle this one."
                    her "Is that acceptable to you?"
                    kid "Fine."
                    her "Good! I'm glad we could work something out. You can do better than delivering fire grass and alcohol."
                    $ authoritative += 1
                "You can keep your job":
                    $ responsive += 1
                    him annoyed "I guess you can keep your job. Does it really make you happy?"
                    kid "Yes! I love it!"
                    him normal "That's what matters most, I guess..."
                    $ permissive += 1
                    her "Just... be smart, okay?"
                "You wouldn't survive without us!":
                    him angry "You wouldn't last a week without us!"
                    kid "Oh yeah? Watch me!"
                    her annoyed "[his_name]..."
                    him annoyed "Just you wait, she'll come crawling back here in a day or two begging our forgiveness."
                    her concerned "I hope you're right..."
                    $ authoritarian += 1
                    jump family28_run_away

    kid "Anyway, would it be so bad if I did use them? I'm practically an adult now, anyway."
    her concerned "As your family doctor, I'd advise against it. Both are habit-forming and cause permanent damage to various parts of your body."

    her annoyed "And as your mom, I'd tell you that you're smarter than that."
    menu:
        "What should I say?"
        "Life's too short not to enjoy everything!":
            him happy "Life's too short to worry so much about stuff like that! If you get the chance, enjoy yourself!"
            kid "Yeah, that's what Brennan said..."
            her "Brennan said that, huh?"
            kid "Yeah, and he handed me a cup to try."
            him surprised "Brennan offered you alcohol?"
            $ neglectful += 1
        "A little bit's fine now and then.":
            him normal "Oh, a little bit now and then won't hurt you. But you don't want it to become something that runs your life."
            kid "Yeah yeah, I know all about alcoholism."
            her "No, you really don't. I know we talked about it in health class, but if you haven't seen it for yourself..."
            kid "Look, I'll be careful, okay! I only had one sip!"
            her "One sip... Brennan offered you alcohol?"
            $ permissive += 1
        "Listen to your mom.":
            him "Your mom's right. Stay away from that stuff!"
            her "If you never have any, you never have to worry about if you're damaging your body, or getting addicted, or anything like that."
            kid "Well it was just the one time, so it's not a big deal."
            her "Just the one time...?  Wait, did Brennan give you alcohol?"
            $ authoritarian += 1
        "You need to decide for yourself. But decide now.":
            $ confident += 1
            him "This is something you have to decide for yourself. So do some objective research, get some opinions, and then figure out what you want to do."
            her "But don't wait until you're in that situation to decide, because then you may not make a good decision."
            kid "Yeah, maybe I wouldn't have tried it if I had thought about it beforehand..."
            her "Tried it? Wait, did Brennan give you alcohol?"
            $ authoritative += 1

    kid "Well, yeah. Just a bit of the cider I delivered. I said it tasted weird, but he said it was an adult thing and maybe that meant I was still a kid. Do I look like a kid to you?!"
    her determined "I'm going to have to talk to him about that."
    him determined "Or maybe I should."
    kid "What? What's the big deal?"
    him "In our culture, a guy like Brennan giving alcohol to a teenage girl is like..."
    her "It's like..."
    kid "What? What is it like?"
    him "Like giving fire grass to a two year old, just to watch them act all crazy."
    her concerned "Some people think it's fun to get other people drunk."
    him annoyed "When people are drunk, their inhibitions are down. They are more willing to do things they might not otherwise do."
    kid "You mean like... Brennan wouldn't do that!"
    her sad "..."
    him sad "..."
    kid "...would he?"
    her concerned "Not on purpose, but..."
    him annoyed "But he doesn't always think about the consequences of his actions. Especially where women are concerned."
    her normal "Anyway, decide ahead of time if or how much you want to drink, and make sure you're around people you can trust."
    him determined "And you can't trust Brennan."
    return

label family28_runaway:
    scene black with fade
    "[kid_name] took a bag with her stuff and rode off on her bike. I did some asking around and it turned out there was a shack halfway to the mining camp that was used as a drop point."
    "She stayed there for a week, and then came back."
    scene farm_interior with fade
    show him determined at midright
    show her concerned at center
    show oleg normal at midleft
    with dissolve
    show kid annoyed at quarterleft with moveinleft

    kid "I lasted a week without you just fine."
    him annoyed "Oh yeah? Then why'd you come back?"
    her annoyed "[his_name]! We're glad you came back, [kid_name]. Obviously you could live on your own, and you will someday, but not yet."
    oleg "What did you eat?"
    kid "I ate whatever I wanted from the storehouse. Bread, fruit, cheese-- I'm telling you, I make good money."
    her happy "I'm glad you're okay. I missed you, though!"
    "[her_name] gave [kid_name] a big hug. [kid_name] glared at me over [her_name]'s shoulder when I didn't join in."
    return

# 18 Earth years old
# Graduation! Terra is stressed out about tests and a big social problem (Oleg? Travis? Anya?)
# What kind of guy should she look for as a husband?
label family29:
# idea: if she is on the path to end up with Oleg, is he not attracted to her but they are great friends and they have to decide if they want to get married anyway?  Or they have some reason why they wouldn't get married...
    "Graduation!"
    return

# 18.6 Earth years old (ENDING)
label family30:
    "[kid_name] has finally graduated from Talaam's little school. And, now that she didn't have school every day, she had moved on to other things."
    $ parenting_style = get_parenting_style()
    if (parenting_style == "authoritarian"):    # aCi or aCI
        # Medicine, either at home or on Earth, trying to make her parents happy
        "She had been spending all her time at the clinic with [her_name], learning and assisting."
        "[her_name] found some online classes for her to take in anatomy and physiology and said [kid_name] was a diligent student."
    elif (parenting_style == "authoritative"):  # ACi or ACI
        # Studies jellypeople and sociology-biology, living with you or married
        "Ever since that trip to the ocean where we communicated with the jelly people, [kid_name] had been obssessed with them."
        "Miranda had been meeting with them and studying them, and so [kid_name] joined her. She was also taking online classes in biology and sociology."

    elif (parenting_style == "permissive"):     # Aci or AcI
        # Farming, either living in her parents' basement or on her own
        "[kid_name] didn't seem to have a specific passion -- she split her time between helping me farm and running her delivery service."

    else: #neglectful or inconsistent,          # aci or acI
        # She's still running her delivery service and dating Travis/Lorant
        "I hardly ever saw her -- it seemed like she was always out delivering things."
        if is_independent():
            boyfriend_name = "Travis"
        else:
            boyfriend_name = "Lorant"
        "Or with her boyfriend, [boyfriend_name]. I'm not sure how that happened, but apparently they're a thing."

    # A spot opens up on the shuttle, and [her_name] is considering taking it.
    "One night I came home and [kid_name] and [her_name] were talking."
    scene farm_interior with fade
    show her concerned at midright
    show kid nervous at center
    with dissolve
    show him normal at midleft with moveinleft

    her concerned "I love Earth, but it's not a decision to make lightly. You might not ever be able to come back."
    kid annoyed "Well, you and dad left your parents to come here. How would this be any different?"
    him surprised "Wait, you're thinking of going back to Earth?!"
    kid nervous "Maybe! I never even thought of it as a possibility, but then Anya said she wanted to stay here with Travis and asked if I wanted her spot!"
    if (boyfriend_name == "Travis"):
        him concerned "I thought you were dating Travis."
        kid angry "Ugh! Dad, we broke up so long ago! He's been with Anya for a few months, even though I think they're totally toxic to each other, but that's not what we're talking about right now."
    him annoyed "You'd have to be an idiot to go back to Earth. Talaam is so much better; that's why we came here."
    her annoyed "There are some great things about Earth."
    him determined "Like what? Traffic? Urban sprawl? Corrupt governments? Terrorists?"
    her angry "How about universities, live music, rain forests, grocery stores, and indoor plumbing?"
    him annoyed "What would you even do on Earth?"
    if (parenting_style == "authoritarian"):
        kid "I want to study medicine and become a doctor, like Mom."
    elif (parenting_style == "authoritative"):
        kid "The best biologists are on Earth. How can I compare Talaam and Earth biology if I've never even been to Earth?"
    else:
        kid "Earth is this incredible, amazing place that almost every book or movie or game is based on, and I've never even been there. If I did, maybe things would make more sense to me."
        kid normal "Plus there's probably better guys there. My dating pool is so small it's more like a wading pool."
        her concerned "Well, there's definitely more guys there..."
        him annoyed "...but I don't know about better ones."

    kid annoyed "Anyway, I'm just thinking about it, so don't make it into this big deal, okay?"
    her concerned "I'm glad you're talking to us about it. There's a lot of things to consider."
    menu:
        "What should I say?"
        "Going to Earth would be good for you." if ((parenting_style == "authoritative") or (parenting_style == "authoritarian")):
            $ demanding +=1
            $ confident += 2
            him determined "There is a lot you can learn on Earth that you can't learn here. I think it would be good for you."
            kid surprised "You think I should go?!"
            if (parenting_style == "authoritative"):
                him normal "This is a rare opportunity. I love Talaam, but if you want to become a doctor you really should study there."
            else:
                him normal "This is a rare opportunity. I love Talaam, but you can learn so much more about biology from experts there."
            her surprised "Wow, I never thought I'd hear you say that."
            him annoyed "It doesn't mean she has to stay there forever. Hopefully she'll learn everything she can and bring it back here to make Talaam even better."
            kid concerned "I'll think about it..."
            $ authoritarian += 1
        "We need you here.":
            $ demanding += 1
            $ confident -= 2
            him concerned "[kid_name], we still need you here."
            her annoyed "We can't keep her with us forever."
            him annoyed "There's few enough people on Talaam as it is. We can't afford to lose a single one, especially not our own daughter!"
            kid concerned "I'll think about it..."
            $ authoritarian += 1
        "Think about it carefully.":
            $ responsive += 1
            $ demanding += 1
            him normal "It's your choice, but please think carefully about the consequences either way."
            kid surprised "What consequences?"
            him concerned "For example, if you went to Earth, it might be difficult to come back here. We might never see you again."
            her concerned "On the other side, if you decide not to go, you might never get that chance again, either."
            him determined "If you went to Earth, you'd be completely alone. No family, no friends, no community supporting you."
            her determined "But you'd have a chance to meet so many more new people and friends that you would never meet here."
            him normal "On Earth, you could get a traditional college degree in anything you wanted."
            her concerned "But you might be in debt when it's over, and unless you have a very well-paying job, that debt could last a long time."
            him annoyed "If you go to college on Earth, they'll tell you all the classes you need to take and you'll have to write papers that say what your teachers want and do exactly what they say."
            her normal "But here, you're in charge of your education, and while that gives you a lot of freedom to study what you want, it might be hard to stay motivated and learn efficiently without as much structure."
            kid surprised "That's... a lot to think about!"
            him normal "Good! If you're not thinking about it a lot, you'll probably make the wrong decision."
            her concerned "I don't think there is a 'wrong' decision here. But please gain as much information as you can and think hard before you make a decision."
            kid concerned "Okay... yeah. I guess I have a lot to think about."

            $ authoritative += 1
        "You should do what makes you happy.":
            $ responsive += 1
            him normal "It's your choice. Just do whatever makes you happy."
            kid annoyed "I don't know if going to Earth will make me happy! I don't even know what it's like!"
            her concerned "Going to Earth or not going to Earth is not going to make you happy."
            kid sad "Then what will?"
            her normal "Loving people and doing good will make you happy. You can do that anywhere."
            kid annoyed "So you're saying it doesn't matter where I go?"
            her concerned "You can be happy anywhere. But if you really want to go to Earth, then maybe you should."
            him concerned "It's your choice, sweetie."

            $ permissive += 1
        "Don't ask me what to do.":
            $ responsive -= 1
            him annoyed "Why did you even bring it up? You're just going to do whatever you want anyway."
            kid annoyed "Well maybe I wanted some advice before I made up my mind! If I did, though, I definitely wouldn't ask you!"
            "She stormed away to her room."
            her annoyed "That was a stupid thing to say."
            him angry "What? It's not like she listens to us."
            her angry "You don't know your own daughter at all, do you? She acts like she's not listening and she doesn't care what we think, but later when she's thinking she'll hear our words and they will influence her."
            him determined "Well I've never seen that."
            her determined "I have. Now if you'll excuse me, I need to try and undo all the damage you just did."
            $ neglectful += 1

    return
