## Community Events
label community1:
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    # TODO: Introduce new colonist characters; establish old ones 
    menu:
        "Welcome them warmly! Introduce yourself to everyone."
            $ colonists += 1
        "Let them come to you."
    return


label community2:
    "New colonists interpret their contracts more literally. They want to put all their crops in the community center before taking some for themselves."
    # TODO: have the new colonist quote the contract so players know what the exact terms are.
    menu:
        "Agree with their more literal interpretation."
            $ colonists += 1 #would this also affect the miner's ease of transition later on?
        "Push to have each farmer store most of their own crops. It's more efficient, right?"
            $ luddites += 1
    return


label community3:
    "The old colonists sometimes accidentally leave the new colonists out of stuff, like women's bath night or goat meat distribution (aka BBQ)."
    menu:
        "We'll try to be better about inviting everyone next time."
        #TO DO: make option to ask someone to do it, or hope someone else does it. If you hope someone else does it, no one does it.
        "I'll personally make the calendar more accurate, and put a reminder on the village discussion forum."
            $ colonists += 1
            # TODO: what if he forgets?
        "I'll ask the mayor to write upcoming events on a white board outside the storeroom."
            $ luddites += 1
    return


label community4:
    "Indium is discovered. Rare Earth Tech warns them that 50 miners are on the way. They tell the colonists to start stockpiling preserves for the miners and to institute currency."
    "Since instantaneous communications to Earth are limited to a few hundred characters, it's not clear how exactly they are supposed to prepare."
    "Should we start rationing food?"
    menu:
        "Yes, ration food as much as possible. Otherwise we will have hungry miners."
            $ miners += 2
        "Ration a little. We don't want to starve ourselves."
            $ miners += 1
        "No, don't ration food. The miners can hunt and forage."
            $ luddites -= 1 # TODO: This might be better represented by another variable. If the player chooses this, the luddites will be in competition with the miners over hunting and foraging grounds.
    "How will we issue currency?"
    menu:
        "Use pieces of whittled wood."
            $ luddites += 1
        "Use an encrypted form of digital currency."
        "Use the one printer to print rudimentary banknotes."
            
        # TO DO: do more research and think through the consequences of these choices. Make a variable for each one.
    return


label community5:
    "Community 5 Event"
    return


label community6:
    "Community 6 Event"
    return


label community7:
    "Community 7 Event"
    return


label community8:
    "Community 8 Event"
    return


label community9:
    "Community 9 Event"
    return


label community10:
    "Community 10 Event"
    return


label community11:
    "Community 11 Event"
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
