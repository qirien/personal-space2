## Family Events
# 
# Each family event has several parenting choices.  The decisions for the month
# will affect how much the child's stats increase that month.
#
# "demanding" and "responsive" are just for the current year and affect how much the child's stats increase that month.
# "authoritative", "authoritarian", "permissive", and "neglectful" are cumulative and affect the community's direction and have some correlation to "demanding" and "responsive".  Only increase one per month (?).
# TODO: The only way to get the "authoritative" option is usually to learn more about the situation by choosing "patient" options, such as "Listen", "Ask why", "Wait", "Think about it", etc.

# 3 Earth mos. old
# CAN'T STOP CRYING!!
label family1:
    "Terra's been crying for hours, no one knows why.  Everyone's tired and spent."
    menu:
        "Take her for a walk":
            $ responsive += 1 
            $ permissive += 1
        "Ask someone else for help":
            $ responsive += 1
            $ demanding += 1
            $ authoritative += 1                        
        "Let Kelly handle it":
            $ responsive += 0 # TODO: Do we ever subtract points?
            $ neglectful += 1
        "Let Terra cry":            
            $ demanding += 1
            $ authoritarian += 1
            
    return
    
    # Actual scene
    # TODO: delete above when ready for prose
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
            "Finally, she was sleeping in her crib, and I fell into bed."
            
        "Ask someone else for help.":
            "I wish I could ask my parents, but they're light years away. I'm not sure who else we could ask, though."
            him concerned "Maybe we should ask someone else for help. Someone who knows more about babies."
            her annoyed "Who's going to know more about [kid_name] than us?!"
            him annoyed "Everyone! Anyone! All I know is animals; calves and colts don't cry like this!"
            her sad "I'm a doctor; I should be able to figure something out. But I can't even think when [kid_name]'s crying."
            him concerned "Here, I'll hold her, and you go do some research or ask around or whatever."
            "[her_name] went outside to do some reading while I held [kid_name]. I paced restlessly, holding the baby in different positions until [her_name] returned."
            "She had a big list of things to try, and we tried them all.  I don't know if the white noise and the bath worked, or if she finally just wore herself out, but eventually she stopped crying and fell asleep."
            
        "Let [her_name] handle it.":
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
            "But this was a trouble I couldn't fix. What was the point in sticking around, when everything I did just seemed to make it worse?"
            "That's what I told myself, but I still felt like a traitor."
            "..."
            "I was a traitor."
            menu:
                "Go back and apologize.":
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
                "Spend the night in the barn":
                    "I couldn't go back there. I was already frayed and broken and ready to snap. My brain felt like a sparking circuit, and I worried that if I stayed, I might hurt someone or make a big mistake."
                    scene barn with fade
                    "I lay down on the hay in the barn and closed my eyes. [kid_name]'s screams echoed in my head so loudly I sat up and looked around. But there was no one there."
                    "Sleep was a long time in coming."
                    
            
        "Let [kid_name] cry.":
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
 
    # TODO: Perhaps they join the daycare coop at the end of this scene?
    return

#####################################################
#
# TODDLER
#
#####################################################

# 18 Earth mos. old
label family3:
    "Terra keeps putting sticks and rocks in her mouth."
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
                        
        # TODO: I don't completely understand when to call the function to increase it rather than the variable. How would you do this one, Andrea?
        # Still working with the best way to use these.  Basically, the child variables depend on the parenting variables, so I wrote a function to increase them so we can easily change the formula we use.
        # Currently, the child variables are increased each year automatically based on that year's decisions, so all we have to do in this file is worry about demanding and responsive.  
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
    "Terra wants your attention while you're trying to relax"
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
    "Terra talks back when asked to pick up her toys, saying \"I hate you!\""
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
        her "Now that [kid_name]'s in school, maybe it's time for us to have another baby?"
        menu:
            "What should I say?"
            "Are you kidding?!":
                him "No way!"
                $ year8_have_baby = False
            "It would be efficient":
                him "It's probably more efficient to have them closer together."
                $ year8_have_baby = True            
            "If you're ready.":
                him "We can if you want to -- you're the one that has to host them for nine months." 
                $ year8_have_baby = True
            "Sure! Anytime!":
                him "Yeah! I love kids!"
                $ year8_have_baby = True
    # TODO: Have a baby here if you decided to.
    return

label baby_delivery:
    scene clinic with fade
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
    #TODO: Finish delivery. Baby has some birth defect - cleft lip, club foot?     
    
# 5.5 Earth years old
# Holiday Traditions
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
            him "Maybe when your'e older. That's not something you need to worry about right now."
            kid "But I am worried about it right now!"
            him "Ask your mom, then."
            kid "Why can't you just tell me?"
            him "I just... I just can't! So quit asking!"
            "I felt a little bad, but really, she's asking the wrong person!  That's [her_name]'s job!"
        "Give a vague metaphor":
            him "Well, you know, it's like, uh, like bees carry pollen?  And they fertilize the flowers so fruits can grow? It's . . . kind of like that."
            kid "I know that! But how does it work? Where's the pollen, and what's the flower?"
            him "Well, males and females have different parts, so the male part is like the pollen, and the female part is like the flower."
            kid "I don't get it."
            him "Ah, yeah, well . . . hey, look, that crabird landed on top of one of the goats!"
            kid "What does that have to do with it?"
            him "Nothing. Time to collect fertilizer! Here's your shovel."
            "Whew, that was a close one!  I'd better figure out what to say next time. Or maybe [her_name] could talk to her about it."
        "Keep it simple":
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
            
        "Tell her all the details":
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
     
    # TODO: Finish this
    scene farm_interior with fade
    #show kid at midleft
    #show brother crying at quarterleft with dissolve
    show him at midright with moveinright
    
    him surprised "Whoa, what's going on?"
    kid "He's annoying me!"
    bro "She hit me!"
    kid "You should stop being so annoying!"
    him "Hey, hey, both of you go sit on your beds and cool off."
    her "They've been like that ever since I got home. Something's bothering [kid_name], but she won't tell me what it is."
    
    
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

    