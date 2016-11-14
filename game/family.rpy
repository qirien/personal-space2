## Family Events

# 3 Earth mos. old
label family1:
    # TODO: check expressions, positions
    scene bg farm_interior with fade
    show him concerned at midright
    show her concerned at midleft

    her "I just wish I knew why she was still crying! Even if I couldn't help her, at least I'd know I wasn't overlooking something."
    him sad "I know. It's been hours..."
    "I knew she was exhausted. She had been carrying [kid_name] around all day and feeding her every few hours."
    "I wanted to help, but I had spent the whole day cleaning out the barn and was spent.  All I could think about was sleeping."
    "Sleeping..."
    show black with dissolve
    hide black with dissolve
    him serious "(I can't sleep now. They both need me. But what should I do?)"
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
            scene bg farm_exterior with fade
            show him normal at center with dissolve
            him normal "There now, little [kid_name], how's that?"
            "..."
            "She's still crying. I better get further from the house so I don't keep up [her_name]."
            scene bg fields with fade
            "The winters on Talaam were mild, but it was cold enough that I snuggled [kid_name] close to my chest as I walked, feeling her tiny warmth through my jacket."
            "I reminded myself that she wouldn't cry forever, that this was just one night, even as I felt like sobbing alongside her with exhaustion."
            "I hated feeling so helpless."
            scene bg moon with fade
            "I wonder if [kid_name] felt the same way?"
            "I looked down at her tiny squalling face and stroked her cheek. She was so upset, and had no other way to tell us about it. She certainly couldn't do anything to help herself."
            "We walked the fields for at least an hour; maybe more."
            "I don't know if she wore herself out or started feeling better, but she finally stopped crying and fell asleep. I was too tired to even be happy about it."
            scene bg farm_interior with fade
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
            scene bg farm_exterior with fade
            "I stepped out into the night, closing the door gently with what little control I had left. I started to run."
            scene bg fields with fade
            "The crying faded from my ears the further I got from the house, but I could still hear the cries echoing in my head. I ran faster."
            scene bg moon with fade
            "I reached the end of our fields, out of breath, legs and chest aching. The pain felt good; I deserved it."
            "Maybe I wasn't cut out to be a dad. What kind of dad leaves when there's trouble?"
            "But this was a trouble I couldn't fix. What was the point in sticking around, when everything I did just seemed to make it worse?"
            "That's what I told myself, but I still felt like a traitor."
            "I was a traitor."
            menu:
                "Go back and apologize.":
                    "I had to make things right."
                    "I ran back to the house. I could still hear [kid_name]'s crying even from outside."
                    scene bg bedroom with fade
                    "[her_name] was lying on the bed with her arm around [kid_name], her face streaked with red from crying."
                    "I was glad to see she'd stopped crying, but then she looked up at me with hollow eyes and a resigned expression."
                    "She didn't say anything, just lay her head back down and stared at [kid_name] blankly."
                    him sad "[her_name]... I'm sorry. I shouldn't have left. I'm here, now."
                    "She still didn't respond, even when I picked up the squalling [kid_name] and bounced her gently, trying for the hundredth time to help her calm down."
                    "As I left the room, [her_name] said something I've never forgotten."
                    her annoyed "Don't ever leave us again."
                "Spend the night in the barn":
                    "I couldn't go back there. I was already frayed and broken and ready to snap. My brain felt like a sparking circuit, and I worried I might hurt someone or make a mistake."
                    scene bg barn with fade
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
    

#####################################################
#
# TODDLER
#
#####################################################
# 10 Earth mos. old
label family2:
    "Family 2 Event"
    return

# 18 Earth mos. old
label family3:
    "Family 3 Event"
    return

# 2 Earth years old
label family4:
    "Family 4 Event"
    return

# 2.7 Earth years old
label family5:
    "Family 5 Event"
    return

# 3.5 Earth years old
label family6:
    "Family 6 Event"
    return

#####################################################
#
# SMALL CHILD
#
#####################################################

# 4 Earth years old
label family7:
    "Family 7 Event"
    return

# 5 Earth years old
label family8:
    "Family 8 Event"
    return

# 5.5 Earth years old
label family9:
    "Family 9 Event"
    return

# 6.2 Earth years old
label family10:
    "Family 10 Event"
    return

# 6.8 Earth years old
label family11:
    "Family 11 Event"
    return

# 7.4 Earth years old
label family12:
    "Family 12 Event"
    return
    
#####################################################
#
# BIG KID
#
#####################################################    

# 8 Earth years old
label family13:
    "Family 13 Event"
    return

# 8.7 Earth years old
label family14:
    "Family 14 Event"
    return

# 9.4 Earth years old
label family15:
    "Family 15 Event"
    return

# 10 Earth years old
label family16:
    "Family 16 Event"
    return

# 10.5 Earth years old
label family17:
    "Family 17 Event"
    return

# 11.1 Earth years old
label family18:
    "Family 18 Event"
    return

# 11.8 Earth years old
label family19:
    "Family 19 Event"
    return

# 12.4 Earth years old
label family20:
    "Family 20 Event"
    return
    
#####################################################
#
# TEENAGER
#
#####################################################

# 13 Earth years old
label family21:
    "Family 21 Event"
    return

# 13.6 Earth years old
label family22:
    "Family 22 Event"
    return

# 14.2 Earth years old
label family23:
    "Family 23 Event"
    return

# 14.8 Earth years old
label family24:
    "Family 24 Event"
    return

# 15.5 Earth years old
label family25:
    "Family 25 Event"
    return

# 16.1 Earth years old
label family26:
    "Family 26 Event"
    return

# 16.7 Earth years old
label family27:
    "Family 27 Event"
    return

# 17.3 Earth years old
label family28:
    "Family 28 Event"
    return

# 18 Earth years old
label family29:
    "Family 29 Event"
    return

# 18.6 Earth years old (ENDING)
label family30:
    "Family 30 Event"
    return

    