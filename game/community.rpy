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
    "Indium is discovered. Rare Earth Tech warns them that 50 miners are on the way. They tell the colonists to start stockpiling preserves for the miners and to institute currency."
    "Since instantaneous communications to Earth are limited to a few hundred characters, it's not clear how exactly they are supposed to prepare."
    "The colony has a town meeting to determine how to deal with the situation."
    # It will take 4 Earth years for the miners to arrive.
    "Who will represent our colony's needs to Rare Earth Tech?"
        #Authoritative parenting-style=voted by a majority
        #Autoritarian=voted by a plurality
        #Permissive=nominated, but didn't win
        #Passive=you are not nominated
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
            
        # TODO: do more research and think through the consequences of these choices. Make a variable for each one.
        # TODO: Why is your vote the deciding one? Are you on some kind of colonist preservation committee?
    return


label community5:
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
        "I would remind them of the contract they signed and ask them to obey it to the letter.": 
            # TODO: this option doesn't seem very natural?
            $ miners += 1
    return


label community6:
    "A new colonist is afraid to go out walking past the colony."
    menu:
        "Tell them they're right to be afraid":
            $ miners += 1 
            # increases their dependence on the corporation
        "Encourage them to explore.":
            $ luddites += 1
            $ colony += 1
    return


label community7:
    "Community 7 Event"
    return


label community8:
    "Your child is going to kindergarten. Parent-teacher conference."
    #Feedback on parenting style from teacher. You talk to some other parents while you're there. 
    return


label community9:
    "Community 9 Event"
    return


label community10:
    "Community 10 Event"
    return


label community11:
    "Miners arrive. You meet their leader and 'your' family's miner. You get to know your miner a bit better."
    menu:
        "Reassure and accept":
            $ miners += 1
            $ colonists += 1 
        "Remind them that farming is the really vital work.":
            $ pass
     # This is about a third through the game, which should be about right. It gives the luddites some time to establish themselves. 
    return


label community12:
    "Community 12 Event"
    return


label community13:
    "Community 13 Event"
    return


label community14:
    "Community 14 Event"
    return


label community15:
    "Community 15 Event"
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
