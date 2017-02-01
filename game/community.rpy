## Community Events
label community1:
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    # TODO: Introduce new colonist characters; establish old ones 
    menu:
        "Welcome them warmly! Introduce yourself to everyone.":
            $ colonists += 1
        "Let them come to you.":
            $ pass
    return


label community2:
    "New colonists interpret their contracts more literally. They want to put all their crops in the community center before taking some for themselves."
    # TODO: have the new colonist quote the contract so players know what the exact terms are.
    menu:
        "Agree with their more literal interpretation.":
            $ colonists += 1 
            $ miners += 1 #would this also affect the miner's ease of transition later on? yes, so I should TODO: another variable for this event?
        "Push to have each farmer store most of their own crops. It's more efficient, right?":
            $ luddites += 1
    return


label community3:
    "The old colonists sometimes accidentally leave the new colonists out of stuff, like women's bath night or goat meat distribution (aka BBQ)."
    menu:
        "We'll try to be better about inviting everyone next time.":
            $ pass
        #TODO: make option to ask someone to do it, or hope someone else does it. If you hope someone else does it, no one does it.
        "I'll personally make the calendar more accurate, and put a reminder on the village discussion forum.":
            $ colonists += 1
            # TODO: what if he forgets?
        "I'll ask the mayor to write upcoming events on a white board outside the storeroom.":
            $ luddites += 1
    return


label community4:
    "Rare Earth Tech says that they need a liason from the colony."
    "The colony has a town meeting to determine how to deal with the situation."
    "Who will represent our colony's needs to Rare Earth Tech?"
    "We are accepting nominations."
    "Who will you nominate? You may not nominated yourself."
    menu:
        "Sister Naomi, our religious leader and childcare leader.":
            $ pass
        "My wife's friend Sara. She doesn't seem too busy.":
            $ pass
        "My friend Thuc. I think that would be funny.":
            $ pass
    "We listened to the results of the election."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "Your fellow colonists elected you to be the new representative."
        $ is_liason = True
        return
    elif(style == "authoritarian"):
        "You, Sarah, and Sister Naomi were nominated. You had the most votes, but not the majority."
        $ is_liason = True
        return
    elif(style == "permissive"):
        "You were nominated, but Sarah was elected as the new representative."
        return
    else:
        "Sarah is elected as the new representative."
        #TODO: does the order of these options matter for variable settings?


label community5:
    "Indium is discovered. Rare Earth Tech warns them that 50 miners are on the way. They tell the colonists to start stockpiling preserves for the miners and to institute currency."
    "Since instantaneous communications to Earth are limited to a few hundred characters, it's not clear how exactly they are supposed to prepare."
    # It will take 4 Earth years for the miners to arrive. About 8 Talaam years.
    if is_liason:
        "Should we start rationing food?"
        menu:
            "Yes, ration food as much as possible. Otherwise we will have hungry miners.":
                $ miners += 2
            "Ration a little--the stuff we don't like anyway. We don't want to starve ourselves.":
                $ miners += 1
            "No, don't ration food. The miners can hunt and forage. This taxation wasn't in our contract.":
                $ luddites -= 1 # TODO: This might be better represented by another variable. If the player chooses this, the luddites will be in competition with the miners over hunting and foraging grounds.
        "How will we issue currency?"
        menu:
            "Use pieces of whittled wood.":
                $ luddites += 1
            "Use Rare Earth's encrypted form of digital currency.":
                $ miners += 1
            "Use the one printer to print rudimentary banknotes.":
                $ colonists += 1
    # TODO: do more research and think through the consequences of these choices (replace with more reasonable ones?). Make a variable for each one.
    else:
        show sarah midright
        sarah "The miners won't arrive for another four Earth years."
        sarah "We will start rationing the food that keeps the longest. I've started construction of a few silos for dried grains and beans."
        sarah "Next harvest we'll start accepting canned goods as well."
        sarah "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sarah "I'll be grading your crops against the RET standards."
        
    return


label community6:
    show pete midright
    show julia midleft
    "Pete and Helen accidentally left a tablet outside during a solar flare."
    "The tablet was completely ruined. The same week, their other tablet was out for repairs."
    "They missed watching movies and reading books and keeping in touch with everyone. But they found that they were more creative about how to entertain themselves."
    # TODO: How does the player hear about this?  Maybe Pete asks to use his to submit his weekly report or make a request or something?
    # TODO: determine just how durable the tablets are. They could probably survive being submerged, stepped on, etc. Maybe run over by a tractor?  Poor Pete, he runs over everything!  :-(
    pete "It made me wonder if I would be happier living on my own, with no ties to any company or colony."
    pete "What would you think if someone left the colony?"
    menu:
        "I'd think they were very irresponsible.":
            $ colony += 1
        "I could understand that. Sometimes I feel the same way.":
            $ luddites += 1
        "I guess they would have to forfeit any help from Rare Earth Tech": 
            $ miners += 1
    return

label community7:
     "Some people were compensated more than others for their jobs as colonists."
     "At a farmer's meeting, you mention that the work is worth it to help your parents live comfortably."
     "Thuc says that he almost paid Rare Earth Tech for the chance to come, despite you feeling that he's more qualified because of his experience with sustainable farming techniques."
     "Rare Earth Tech paid off Ilian's considerable restaurant supply startup debts."
     "None of the new colonists were compensated."
     "Why didn't Rare Earth Tech deal more fairly with its employees?"
     if is_liason:
        menu:
            "I don't know. That seems pretty unfair. I'll ask them in my next letter."
                $ luddites += 1
            "From a business standpoint, it makes more sense to negotiate salary with each employee individually."
                $ miners += 1 
            "We're all here now, so let's help each other.":
                $ colony += 1
     else:
        "Sarah made some kind of excuse for Rare Earth Tech's econimizing."
     
     return


label community8:
    "You get to tell Rare Earth Tech what luxuries you want from Earth."
    "Besides a new battery for my tractor, I'd really like some good Earth toilet paper. her_name wants some Gouda cheese."
    if is_liason:
        "You need to find out what everyone else wants too, and send a brief message summarizing it."
        #talk to various villagers. include a bicycle?
        show natalia left
        with dissolve
        natalia "I don't care what else comes from Earth, but there had better be some medication for Martin in there. The longer he lives, the happier our family will be."
        "What will you write? You have a limited amount of characters." #plausible?
        menu:
            "Toilet paper, cheese, peanut butter, lemon juice, and medicine for Martin."
                $ pass
            "Cancer medicine for Martin." #this option will help Martin live another year, and Joanna and Tomas don't join the Luddites with this option. Change to a more specific, long name, to justify it having to take up a lot of characters.
                $ asked_only_medicine = True
                $ pass
        "I sent the message."
    else:
        "We told Sarah that we wanted toilet paper and Gouda cheese."
    
    return


label community9:
    "Pete wants to go camping."
    "He says that guys need more bonding time together, and they should all go hunting at the same time."
    menu:
        "Sounds fun! Go with him and invite your friends." #you learn the particulars of how to camp safe from radiation.
            $ luddites += 1
            $ colonists += 1
        "Sounds dangerous. I have to focus on farming right now anyway."
            $ miners += 1 #not sure which side colonists +1 should go on for this one. 
    return


label community10:
    "Martin Peron is dying of cancer. He wants your advice. Who do you think should take care of his farm?"
    menu:
        "Tomás, his oldest son, and Joanna Nguyen, his wife."
            $ colonists += 1 #more investment in older farms; Tomas and Joanna are less likely to join the luddites this way
        "Let Natalia, his wife, scale back how they'd like."
            $ luddites += 1
        #Possibly an option (would have work event ramifications): "I can help plan the crops, but I need help from Martin's children to execute the plans."
    return


label community11:
    "Miners arrive. You meet their leader and 'your' family's miner. You get to know your miner a bit better."
    "The luxuries from Earth arrive."
    if asked_only_medicine:
        "The exact medicine for Martin came! They included a bunch of other stuff, but not much of what other people asked for."
        "The Peron family is crying happily."
        her "Hey, where's the Gouda cheese? I was really looking forward to it."
        "Other people complain that they didn't get what they wanted. Some of it is humorous."
    else:
        "They sent medicine for Martin, but when I gave it to him, he and Natalie looked crestfallen."
        natalia "This isn't the kind of medicine we needed! This is useless!"
        natalia "Did you tell them what kind of medicine Martin needed?"
        him "I told them Martin needed medicine, and I assumed that they knew what kind from the doctor's reports."
        her "Oooh, Gouda cheese!"
        "Other people got what they wanted, but not the Perons."
     # I don't have an increase in stats for this one, because I'll use the asked_only_medicine variable later to determine some other things, the end of which can have the stat increase. 
     # This is about a third through the game, which should be about right. It gives the luddites some time to establish themselves. 
     # Does Brennan show up with the miners, or is that too fan-servicey?
    return


label community12:
    #I'm not sure if the timeline on this makes sense. Wouldn't you find out a little sooner than the next Talaam year?
    "You find out that your miner isn't good at cooking and has been living off emergency rations."
    "It's not just 'your' miner; many of the rations given to the miners have spoiled since they're too tired to cook and completely offput by the strange tastes."
    "When they do cook, they tend to favor familiar Earth foods, and they love meat. They burn through their meat ration very quickly."
    "How should the community react?" #TODO: depends on if you were elected earlier; otherwise you're limited to helping just your miner.
    menu:
        "Organize cooking lessons for the miners."
            $ colonists += 1
        "Suggest that each family share dinner with their miners in exchange for their rations." #or indulge them?
            $ miners += 1
        "Refuse to help them. They'll learn soon enough that the spice of hunger covers a variety of strange tastes."
            $ luddites += 1
    return


label community13:
    "Miners find a beautiful cave while digging."
    "Dr. Lily attends a brief expedition and discovers a vertabrate without an exoskeleton, which is very rare on Talaam because of the radiation."
    if is_liason: 
        "Dr. Lily asks you to tell Rare Earth Tech about the unusual creatures to get them to halt mining operations in the cave."
        "Rare Earth Tech says the miners are okay to continue their excavation however they see fit."
    else:
        "Sara asked Rare Earth Tech to halt the mining on Dr. Lily's behalf, but they didn't stop."
        "The miners end up exploding the cave to access more minerals deeper down. Dr. Lily is furious."
    #I'm not sure what the choice on this one should be. I want to build up some tensions between the colonists and the miners to give people a plausible reason to leave."
    #I also want some things to happen that the player can't affect to give them a sense of helplessness? Or is there enough of that? Should there be a way to stop the miners from excavating the cave, maybe if your relationship with them is high enough?
    return


label community14:
    "Pete and Helen, and their child, leave their home on the colony because they feel Rare Earth Tech is immoral."
    "They plan to leave almost everything provided by Rare Earth Tech, with the exception of some aluminum sheeting to protect from radiation. They're also taking about a third of their cattle."
    "They announce it on the community message board."
    "Dr. Lily joins them."
    if asked_only_medicine: 
        "No one else joined them."
    else:
        "Tomás Peron and Joanna Nguyen leave with them as well."
    $ luddites += 1
    "How do you react?"
    menu:
        "Warn them that they are doomed."
        "Tell them that you understand their decision but that you are sad to see them go."
            $ colonists += 1
        "Joke that you wish you could join them."
    if is_liason:
        "What do you do with Pete and Helen's remaining cattle?"
        menu:
            "Ask Thuc if any of his kids can look after them."
                $ colonists += 1
            #Thuc doesn't feel as loyal to Rare Earth Tech because they didn't compensate him fairly.
            "Take them for your own farm!"
            #not sure if I want this as a real option
                $ pass
            "Wait for a volunteer. Ilian volunteers."
                $ miners += 1
            #Ilian feels more loyal to Rare Earth Tech, despite his cynical personality?
    else:
        "Pete and Helen's cattle went to Ilian, who wanted to keep track of them."
    return


label community15:
    "Losing members of the community is difficult. Some of the younger memebers of the community step up."
    "Miranda Peron (now about age 26) steps up to take Dr. Lily's spot. She had been studying with Dr. Lily before."
    return


label community16:
    "Community 16 Event"
    return


label community17:
    "Community 17 Event"
    return


label community18:
    "Community 18 Event"
    return


label community19:
    "Community 19 Event"
    return


label community20:
    "Community 20 Event"
    return


label community21:
    "Community 21 Event"
    return


label community22:
    "Community 22 Event"
    return


label community23:
    "Community 23 Event"
    return


label community24:
    "Community 24 Event"
    return


label community25:
    "Community 25 Event"
    return


label community26:
    "Community 26 Event"
    return


label community27:
    "Community 27 Event"
    return


label community28:
    "Community 28 Event"
    return


label community29:
    "Community 29 Event"
    return


label community30:
    "Community 30 Event"
    return
