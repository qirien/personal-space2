## Community Events
label community1:
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    "After the introductions, you get in line with your friend Thuc to have some soup."
    thuc "It's pretty exciting to have some new faces around!"
    him "How's it going? Julia couldn't make it?"
    thuc "No, she was too worn out."
    ilian "I wish I could have stayed home. After talking to people all day the last thing I want to see is more people."
    him "At least there's free soup."
    ilian "It's not free, it came from all those crops you paid to the storehouse! So if any of you gave subpar stuff, we're going to taste it."
    "You get your soup and sit with some of the new colonists."
    him "Hi, I'm [his_name]."
    zaina "I'm Zaina, and this is my husband Kevin. I'd let him speak for himself but his mouth is full, so I'm socially obligated to be polite in his place."
    him "Nice to meet you, Zaina and Kevin. Where will you be living?"
    zaina "We've set up a house out by the radio tower. It's closer to the mountains where I'll be working."
    kevin "And after Zaina figures out where the goods are, I'm in charge of figuring out if it's even possible for us to mine."
    him "Oh, right, that's Rare Earth Tech's plan to pay for this whole expedition."
    kevin "Yes. Usually when a company invests a bunch of money into a research project they would expect to make a profit."
    "What do you think the colony's purpose is?"
    menu:
        "Yep, making money is our goal.":
            $ miners += 1
        "I came to this colony for the excitement of exploration and to live a simpler life, not to worry about profit margins.":
            $ luddites += 1
        "Profits are important to RET, but at the end of the day, working together to do things we couldn't do alone is what keeps me going.":
            $ colonists += 1
    "You continue talking and then head home."
    #TODO: make longer discussion based on menu choice (this is the beginning of the game; we want some really dynamic choices at the start, even if they don't affect a lot)
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
        "How do you help them?"
        
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
    # explanation of why this is separate from the mayor
    "We are accepting nominations."
    menu:
        "Who will you nominate? You may not nominate yourself."
        
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
        "You, Sara, and Sister Naomi were nominated. You had the most votes, but not the majority."
        $ is_liason = True
        return
    elif(style == "permissive"):
        "You were nominated, but Sara was elected as the new representative."
        return
    else:
        "Sara is elected as the new representative."
        #TODO: does the order of these options matter for variable settings?
        #should a leader of the militia be elected here as well?
        
    return


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
    else:
        show sara at midright
        sara "The miners won't arrive for another four Earth years."
        sara "We will start rationing the food that keeps the longest. I've started construction of a few silos for dried grains and beans."
        sara "Next harvest we'll start accepting canned goods as well."
        sara "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sara "I'll be grading your crops against the RET standards."
        # TODO: when/where are crops preserved?  Does Ilian have machines/employees that do this? Or are farmers supposed to do this before taking to the storehouse?
    return


label community6:
    show pete at midright
    show helen at midleft
    "Pete and Helen accidentally left a tablet outside during a solar flare."
    "The tablet was completely ruined. The same week, their other tablet was out for repairs."
    "They missed watching movies and reading books and keeping in touch with everyone. But they found that they were more creative about how to entertain themselves."
    # TODO: How does the player hear about this?  Maybe Pete asks to use his to submit his weekly report or make a request or something?
    # TODO: determine just how durable the tablets are. They could probably survive being submerged, stepped on, etc. Maybe run over by a tractor?  Poor Pete, he runs over everything!  :-(
    pete "It made me wonder if I would be happier living on my own, with no ties to any company or colony."
    pete "What would you think if someone left the colony?"
    menu:
        "I'd think they were very irresponsible.":
            $ colonists += 1
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
            "I don't know. That seems pretty unfair. I'll ask them in my next letter.":
                $ luddites += 1
            "From a business standpoint, it makes more sense to negotiate salary with each employee individually.":
                $ miners += 1 
            "We're all here now, so let's help each other.":
                $ colonists += 1
     else:
        "Sara made some kind of excuse for Rare Earth Tech's econimizing."
     
     return


label community8:
    "Rare Earth Tech has some extra space on the shuttle for Earth luxuries"
    "Besides a new battery for my tractor, I'd really like some good Earth toilet paper. [her_name] wants some Gouda cheese culture."
    if is_liason:
        "You need to find out what everyone else wants too, and send a brief message summarizing it. TODAY."
        $ talked_about_luxuries_counter = 0
        label talk_about_luxuries:
            if (talked_about_luxuries_counter >= 4):
                    him "Oh, it's already the afternoon! I need to send in my report right away."
                    jump write_report
        menu:
            "Who will you talk to about what Earth luxuries they want?"
            "Natalia" if not talked_to_Natalia:
                show natalia at left
                with dissolve
                natalia "I don't care what else comes from Earth, but there had better be some medication for Martin in there. The longer he lives, the happier our family will be. [her_name] said he needed Vemurafenib." #TODO:if you want to make this harder, have the player go ask her what the medication is.
                $ talked_about_luxuries_counter += 1
                $ talked_to_Natalia = True
                jump talk_about_luxuries
            "Thuc Nguyen" if not talked_to_Thuc:
                show thuc at left
                with dissolve
                thuc "I'd like to grow peanuts. Regular, unroasted peanuts will work fine for cultivation purposes."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Thuc = True
                jump talk_about_luxuries
            "Sara" if not talked_to_Sara:
                show sara at right with dissolve
                sara "Oh, I don't know if this is possible, but I would really, really love a bicycle."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Sara = True
                jump talk_about_luxuries
            "Kevin" if not talked_to_Kevin:
                show Kevin at left with dissolve
                kevin "This is an extremely inefficient way to gather information. Could you not have contacted me electronically?"
                him "Yes, but you might not have responded in time. I need to tell them by the end of the day!"
                kevin "Very well. Are they sending new tablet batteries like I requested?"
                him "Yes, yes, don't worry about that. Ask for something that will boost your morale."
                kevin "Wouldn't being reminded of the Earth I'll never return to lower my morale?"
                him "It sounds like you don't want anything."
                kevin "I would like a bagel."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Kevin = True
                jump talk_about_luxuries
            #TODO: Add more people
        label write_report:
            "What will you write? You have a limited amount of characters." #plausible?
            menu:
                "Toilet paper, cheese, peanut butter, lemon juice, and medicine for Martin.":
                    $ pass
                "Vemurafenib for Martin.": #this option will help Martin live another year, and Joanna and Tomas don't join the Luddites with this option. Change to a more specific, long name, to justify it having to take up a lot of characters.
                    $ asked_only_medicine = True
                    $ pass
            "I sent the message."
    else:
        "We told Sara that we wanted toilet paper and Gouda cheese."
        #TODO: Maybe Sara asks you to go ask everyone? better alt
    return


label community9:
    "Pete wants to go camping."
    "He says that guys need more bonding time together, and they should all go hunting at the same time."
    menu:
        "Sounds fun! Go with him and invite your friends.": #you learn the particulars of how to camp safe from radiation.
            $ luddites += 1
            $ colonists += 1
        "Sounds dangerous. I have to focus on farming right now anyway.":
            $ miners += 1 #not sure which side colonists +1 should go on for this one. 
    return


label community10:
    "Martin Peron is dying of cancer. He wants your advice. Who do you think should take care of his farm?"
    menu:
        "Tomás, his oldest son, and Joanna Nguyen, his wife.":
            $ colonists += 1
            $ miners += 1
            #more investment in older farms; Tomas and Joanna are less likely to join the luddites this way
        "Let Natalia, his wife, scale back how they'd like.":
            $ luddites += 1
        #Possibly an option (would have work event ramifications): "I can help plan the crops, but I need help from Martin's children to execute the plans."
        # Perhaps a miner wants to switch jobs and be a farmer?  I guess that require this event to be later?
    return


label community11:
    "Miners arrive. You meet their leader, Bandile, who introduces the miner welcome program."
    "Your family will get to know one miner through weekly dinners."
    "The miner you've been assigned is Chaco."
    him "Nice to meet you Chaco. How was the trip over?"
    chaco "Fine."
    him "Did it take a while to adjust to living in such a small space?"
    chaco "No."
    him "What do you like to do in your free time?"
    chaco "Look at the stars."
    "I feel like we're playing 20 questions here! He's probably overhwelmed from the arrival."
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
     # This is about a third through the game, which should be about right. It gives the luddites some time to establish themselves. 
     # Does Brennan show up with the miners as their RET liason?
    if asked_only_medicine:
        "Thanks to the cancer medicine, Martin is able to work on the farm for six more months before dying a peaceful death."
        $ miners += 1
        $ colonists += 1
    else:
        "Without the medication, Martin's condition swiftly deteriorates, and he dies later that week."
        $ luddites += 1
    return


label community12:
    #I'm not sure if the timeline on this makes sense. Wouldn't you find out a little sooner than the next Talaam year?
    "You find out that Chaco isn't good at cooking and has been living off emergency rations."
    "It's not just Chaco; many of the rations given to the miners have spoiled since they're too tired to cook and completely offput by the strange tastes."
    "When they do cook, they tend to favor familiar Earth foods, and they love meat. They burn through their meat ration very quickly."
    "How should the community react?" #TODO: depends on if you were elected earlier; otherwise you're limited to helping just your miner.
    if is_liason:
        menu:
            "Suggest that each family share dinner with their miners in exchange for their rations.":
                $ miners += 1
                #you find out that they don't have very many spices at all, and share recipes.
            "Refuse to help them. They'll learn soon enough that the spice of hunger covers a variety of strange tastes.":
                $ pass
                #some miners steal food from farms, including one of Pete's cows, and he gets very angry, as it affects future calving.
                #you ask Bandile about what happened to the cows, but he just gives a cryptic answer.
                #you form a militia and hand out guns to the colonist volunteers, who take turns guarding the border between miners and luddites.
            "Allow them to buy extra meat, but at a high price.":
                $ pass #choosing this can contribute to a food shortage later on? or would the crabird plague do that?
    else:
        menu:
            "Ask Chaco about his favorite foods and recipes.":
                $ miners += 1
            "Not your problem": #jump to the same event as "refuse to help them" (above)
                $ pass
    #Do the miners resort to stealing? Elect a sherriff?
    #Is there a skewed male:female ratio now that the miners have arrived?  That could cause people to be more suspicious of them.
    return


label community13:
    "Chaco tells you that the miners found a beautiful cave while digging."
    "Dr. Lily attends a brief expedition and discovers a vertebrate without an exoskeleton, which is very rare on Talaam because of the radiation."
    if is_liason: 
        "Dr. Lily asks you to tell Rare Earth Tech about the unusual creatures to get them to halt mining operations in the cave."
        "Rare Earth Tech says the miners are okay to continue their excavation however they see fit."
        "You talk to Bandile about what it would take to halt the mining. He says the colony would have to compensate him for the time they can't work."
        if (colonists >= 10):
            "You convince the other colonists to compensate the miners to halt mining for two days."
            "Lily and her research assistant, Miranda Peron, gather more samples and photographs of the cave before it is destroyed."
            jump cave_explored
        else:
            "You ask the other colonists if they'd be willing to compensate the miners to stop the mining, but they aren't willing."
            jump cave_unexplored
        #if your relationship with colonists is high enough, you can collect enough money for them to halt mining for two days while Lily does research, and she won't leave?? with the luddites.
    else:
        "Sara asked Rare Earth Tech to halt the mining on Dr. Lily's behalf, but they didn't stop."
        jump cave_unexplored
            
    label cave_unexplored: 
        m "The miners end up exploding the cave to access more minerals deeper down. Dr. Lily is furious."
    return
    
    label cave_explored:
        m "The miners explode the cave to access more minerals deeper down. At least Dr. Lily got to document the life forms there."
        m "Next weekend, some miners are gambling away their new fortunes."
    #I'm not sure what the choice on this one should be. I want to build up some tensions between the colonists and the miners to give people a plausible reason to leave."
    #I also want some things to happen that the player can't affect to give them a sense of helplessness? Or is there enough of that? Should there be a way to stop the miners from excavating the cave, maybe if your relationship with them is high enough?
    #Perhaps you could get everyone on the colony to pitch in some currency to pay the miners NOT to mine temporarily while Lily takes lots of data.  So at least she gets to study the fossils and take lots of scans.  But perhaps the miners are rowdy and spend their currency on stuff other people wanted or cause trouble when not working, and you are also now low on money.
    # Pete should be a vocal opponent of the mining to foreshadow next month.
    # Perhaps something tragic, like someone decides to do a sit-in to protest the mining, but the miners don't know about it, and they get blown up as the excavation continues?
    return


label community14:
    "Pete and Helen, and their child, leave their home on the colony because they feel Rare Earth Tech is immoral and they don't like being controlled and pushed around."
    "They plan to leave almost everything provided by Rare Earth Tech, with the exception of some metal foam sheeting to protect from radiation. They're also taking about a third of their cattle."
    "They announce it on the community message board."
    "Dr. Lily joins them."
    if asked_only_medicine: 
        "No one else joined them."
    else:
        "Tomás Peron and Joanna Nguyen leave with them as well."
    $ luddites += 1
    "How do you react?"
    menu:
        "Warn them that they are doomed.":
            $ pass
        "Tell them that you understand their decision but that you are sad to see them go.":
            $ colonists += 1
        "Joke that you wish you could join them.":
            $ pass
    if is_liason:
        "What do you do with Pete and Helen's remaining cattle?"
        menu:
            "Ask Thuc if any of his kids can look after them.":
                $ colonists += 1
            #Thuc doesn't feel as loyal to Rare Earth Tech because they didn't compensate him fairly.
            "Take them for your own farm!":
            #not sure if I want this as a real option.
            # Maybe offer them to the miners?
                $ pass
            "Wait for a volunteer. Ilian volunteers.":
                $ miners += 1
            #Ilian feels more loyal to Rare Earth Tech, despite his cynical personality?
    else:
        "Pete and Helen's cattle went to Ilian, who wanted to keep track of them."
    return


label community15:
    "Losing members of the community is difficult. Some of the younger memebers of the community step up." # Sister Naomi dies?  Or has another stroke, this time so bad that she is essentially a vegetable.  Who should care for her?  Pavel can't do it alone
    "Miranda Peron (now about age 26) steps up to take Dr. Lily's spot. She had been studying with Dr. Lily before."
    return


label community16:
    "Trade with luddites: is it permitted in the contract?"
    "Luddites want to trade a few calves for medical supplies." # [her_name] is not supposed to treat them at the clinic, but she does anyway?
    "Also, you chat about the hardships of living without tech."
    #if the mode of currency stays a choice, how does it play in here?
    "Do you trade with the luddites?"
    menu:
        "yes.":
            $ luddites += 1
            $ trade_with_luddites = True
        "no.":
            $ pass
    return


label community17:
    "It's time for the harvest festival! Usually you eat a big meal and the kids go around begging desserts off everyone."
    "This year you're in charge. Who will you invite?"
    menu:
        "The miners and the luddites." if ((luddites >= 10) and (miners >=10)):
            $ invited_luddites = True
            $ invited_miners = True
        "The luddites." if (luddites >= 10): 
            $ invited_luddites = True
        "The miners." if (miners >= 10): 
            $ invited_miners = True
        "The usual--all the other colonists.":
            $ pass
    #TODO: depending on your levels with the miners and luddites, you can invite them. If you invite the luddites, they decide to host, and if you eat the jellyfish they serve, you become obsessed with jellyfish for a while.
    #TODO: find a real way to do if AND?
    # the obsession causes you to.... ??? throw crops into the sea?
    # also if you meet with the luddites, Pete can answer questions about cattle health.
    # if BOTH luddites and miners are there, they start trade negotiations? affects the fire grass event later.
    return


label community18:
    "The miners complain that a herd of cattle ran through their camp, making a huge mess and eating their scant herb gardens."
    "Then a farmer complains that a similar thing happened, only the cows ate some young crops."
    "How do you approach the problem? You know it was probably the luddites."
    menu:
        "Track down Pete and ask him what happened.":
        #if you talk to Pete, he explains that they were herding the cattle from their winter caves to summer camps and they couldn't keep up with them, because a large animal scared them into stampeding, basically.
        #THEN, if your relationship with the miners and colonists is good enough, they accept your explanation and
            $ luddites += 1
        #but if your relationship isn't good enough, they demand compensation.
        "Compensate the offended parties with currency.":
            $ miners += 1
        "Apologize, but don't compensate them. The luddites are a force of nature now.":
            $ pass
    return


label community19:
    "The luddites have been eating a lot of the crabbirds' natural predators, the wolf slugs." 
    "As a result, crabirds devestate this season's harvest."
    "There is enough stored food for everyone to live off of for the winter, but not for all the livestock."
    "How do you deal with this problem?"
    menu:
        "Give extra cattle to the luddites, where some might survive by grazing.":
            #The miners are desperate for beef later and might even trade guns with the luddites??
            $ luddites += 1
        "Make a lot of preserved meat jerky.":
            $ colonists += 1
        "Invite the miners for an epic barbeque.":
            $ miners += 1
    #one of the newer farming families wants to join the luddites?
    #TODO: finish this
    return


label community20:
    "Dr. Lily tells you her findings living with the luddites."
    "She tells you more about the vertebrates living in the caves, and the parasite in the thready jellyfish."
    "She feels like she's going to die soon, so she has moved in with Miranda Peron." #is Miranda married to a miner by now? might make a good event for a bit earlier.
    "Should she be allowed to move back to the colony?"
    menu:
        "No.":
            $ pass
        "Yes.":
            $ luddites += 1
    "Dr. Lily dies in a few months." #TODO: her burial spot depends on your decision earlier.
    # Or perhaps she simply walks into the ocean one day and never returns #oOooooOoo
    return


label community21:
    "Miners are using fire grass a lot. It helps them mine more for longer, which gives them more pay."
    "They are getting it from the luddites, who have been farming it." #TODO: does your decision to trade (or not) with luddites affect the miners?
    "RET doesn't have an official stance on fire weed. The long-term side effects aren't well known."  
    "What do you do about it?"
    menu:
        "Have miners receive a recommended daily allowance of fire weed at their next checkup":
            $ miners += 1 
        "Don't allow colonists to buy it.": # if you're trading with the luddites.
            $ pass
        "Nothing.":
            $ luddites += 1 #there are some bad side effects which affect their mining if they continue. Maybe in the next event?
    return


label community22:
    "Miners moving on to start mining the next mountain, which is near the luddites's winter quarters by the sea."
    "The luddites refuse to move, even though they know that their caves are in danger of collapsing with the mining."
    "What do you do?"
    menu:
        #this feels like it escalated really quickly. Talk with both parties before the menu?
        "Form a militia with the miners to force the luddites out of the cave.":
            $ miners += 1
        "Not your problem. Do nothing.":
            $ luddites -= 2 #TODO: minuses a problem? this seems like kind of a boring option?
        "Petition RET and the miners to choose a different location for now.":
            $ luddites += 1
        "Form a militia with the luddites to force the miners to a different site.":
            # Organize a passive resistance, strike, etc.  A petition from lots of farmers saying they will leave the colony if the luddites are not protected?  Only works if you have really high scores with everyone.
            # if you form a militia, someone gets injured or maimed
            $ pass
    return


label community23:
    "RET wants to switch to artificial meat."  #I like the idea of doing something with artificial meat, but let's keep thinking about this.  Maybe RET announces they will not send anymore live animals, but instead an artificial meat lab, and you can decide to phase out your animals or breed them more? 
    "You hate how it tastes."
    "Make the switch?"
    menu:
        "Yes.":
            $ miners += 1 #miners equal the interests of RET here
        "No.":
            $ luddites += 1
        "Make a convincing case for meat.": #provides fertilizer, hair for wool, milk, leather
            $ colonists += 1
    return


label community24:
    #Terra comments on how having kids is dangerous and thinks about her own future.
    
    #at a town meeting
    show him at midright
    show her concerned at midleft
    
    her "One of the mining women almost died having a stillborn baby."
    her "She had been mining right until the day before she went into labor. Overwork was definitely a factor."
    her "Will RET compensate her for her loss? She's still working even though she ought to rest."
    him "Good question. I'll ask them."
    "How will you word the query?"
    menu:
        "A miner overworked while pregnant and the fetus died before birth; will she receive compensation?":
            $ miners += 1
        "Please compensate the miner who lost her baby due to overwork.":
            $ miners += 2
        "We're experiencing health setbacks due to overwork. May colonists and miners take paid vacation days?":
            $ colonists += 1
    
    him "That reminds me, RET told me that due to the cost of shipping, they will no longer provide temporary birth control."
    him "RET recommends using the rhythm method."
    her "Are they serious? Does that include the miner's families?"
    him "Yes, although children born on Terra must stay here."
    julia "Luckily my time of fertility is ending, but for some of you this will be most inconvenient."
    ilian "No kidding. I've got enough mouths to feed at the moment."
    sara "[her_name], do you have any advice for us?"
    her "For women with regular cycles, tracking the time of ovulation works fairly well."
    her "Couples may wish to exercise their creativity if they wish to avoid conception yet remain intimate during the woman's fertile time."
    her "So, [his_name], is RET trying to grow the colony?"
    him "I honestly think it's just economic. Miranda, do you know if any of the local plants could be used as birth control?"
    #todo: set up Miranda as a character
    #miranda I'm not sure about preventing birth, but I know that fire grass can abort pregnancies in the early stages.
    #consequences if you said not to trade for it in community 21
    
    return

label community25:
    "Miners have a lot more money than farmers. They start employing young people as servants to do their household chores and look after their children."
    return


# Miranda predicts increased solar flare activity this year; how do you prepare?  Do you believe her?  Do you warn miners/luddites/everyone?
label community26:
    "Miranda predicts increased solar flare activity this year."
    "How do you prepare?"
    menu:
        "Plant more beets.":
            $ colonists += 1
        "Ask Pete for some brewer's yeast" if (luddites >= 10):
            $ colonists += 2
        "Ask Zaina if the miners have found any calcium or magnesium" if (miners >= 10):
            $ colonists += 2
        #these are all "natural" ways to help the body get rid of toxins
    "Will you warn people outside the colony about the solar flares?"
    menu:
        "Warn the luddites and the miners" if ((luddites >= 12) and (miners >=12)):
            #TODO: test these numbers
            $ miners += 1 
            $ luddites += 1
            "You warn both the luddites and the miners."
        "Warn the luddites." if (luddites >= 12): 
            $ luddites += 1
            "You warn the luddites."
            "The luddites are starting work on building water barriers around their winter homes. They've planted lots of guords so they can fill them with water when they're dry."
        "Warn the miners." if (miners >= 12): 
            $ miners += 1 
            "You warn the miners."
        "I won't warn anyone.":
            $ pass
    return


label community27:
    "Fire grass has some long-term side effects. Insomnia is a big problem."
    #depending on your relationship levels, different people ask you for help.
    "What do you advise? They aren't even using it anymore."
    menu:
        "Read a book.":
            $ pass
        "Work through it.":
            $ pass
        "Ask a doctor.":
            $ miners += 1
            #the doctor might suggest biofeedback exercises
    return

# Perhaps Mayor Grayson dies somewhere in here, leading to a power vaccuum and increased internal tensions as well.  
label community28:
    "Everyone around Mayor Grayson has noticed that his mental state has been declining."
    "When he is in one of his lucid moments, he decides to step down from his position as mayor."
    "He asked you to not let him be a burden on the colony."
    "You schedule a town meeting with the other colonists to decide who the new mayor should be."
    "Also... who is going to take care of Mayor Grayson?"
    #TODO:Go to past if_liason events and have some consultation with the mayor so that it's more clear what the mayor actually does. He makes decisions that will help the colonists the most in the long run.
    "Colonists are divided about if the new mayor should be a farmer with firsthand experience of growing food, or someone more detached from farming."
    "They decide on some basic qualifications and reconvene the next night to decide."
    "The next evening, some miners arrive and ask why they weren't invited?"
    "Their logic is that since they're also RET employees, they should be allowed to nominate a candidate for mayor."
    "There are more miners than colonists; if the miners act together they could control who becomes the mayor."
    "Will you let them join the election?"
    menu:
        "Let them vote, but not nominate.":
            $ pass
        "Let them nominate a candidate for mayor.":
            $ miners += 3
        "Don't let them vote or nominate a candidate for mayor.":
            $ colonists += 1
            $ miners -= 1
            #resulting unrest? would the luddites get involved too?
    "Mayor Grayson doesn't have any family to take care of him. How should the colony help him?"
    #I'm not sure if this is really the player's decision; it might play out more like a community discussion. 
    menu:
        "Assign him to a family and let him 'help' with the community daycare.":
             $ pass
             #is there a family that wants to take him in?
        "The colony doesn't have the resources to look after him. Give him a humane death." if (colonists <= 8):
             $ colonists -= 1
        "Ask Mayor Graysen what he wants.":
             $ pass
    return


label community29:
    "RET reports that they've heard from a miner that the luddites are hurting RET business interests." 
    #it's an account from about 7 years ago? about the cattle thing, but indignently whiney and kind of overblown.
    "They give permission to use force against the luddites if they are hindering mining operations."
    #it goes to both the liason and the head miner. If you're not the liason, Sara calls a town meeting to discuss it.
    if ((luddites >= 12) and (miners >=12)): 
        "Are the luddites getting out of hand?" #this is wrong, but I don't know what is right! do I use a jump command? I think there is a way to display text based on stats, but I can't remember.
    "You explain to RET that force isn't necessary" 
    if ((luddites <= 5) and (miners <=5)): 
        "You hear gunshots. The miners are attacking the luddites!?"
    #Lm - you can warn the luddites and some of them take shelter with you
    #lM - you can join the miners in driving away the luddites (do you actually kill them?)
    return

# Rebuilding, aftermath of big fight.
# many of the endings have Terra going back to Earth. Does a shuttle arrive at the last event? Is it taking some of the miners back at the end of their contracts?  
# I think that sounds good.  It's kind of a nice circle and parallel to the first game.  That would make the miners have ~12 year contracts in Earth time.
label community30:
    "The latest shuttles from RET have arrived."
    if ((luddites >= 12) and (miners >=12)): 
        "New miners are arriving to replace the ones who are leaving. You're kind of sad to see some of them go."
    #TODO: fill in the various endings, figure out what the threshold numbers should be
    return
