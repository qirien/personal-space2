## Community Events

# A short event that plays to introduce the community
# Feel free to change this if you want. It should be fairly short and remind
# everyone of the characters and situation.
label community_intro:
    "Luckily, we weren't alone on Talaam. There were several hundred other colonists here, now. Enough to feel like a real community, and not just  a few struggling pioneers."
    # show Julia and Ilian?
    "There were some I got along with..."
    # show Thuc and Natalia and Pete?
    "...and some I didn't. But we all had one thing in common -- we worked hard to grow the food we all needed to survive on this planet, light years away from Earth."
    return
    

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
    kevin "Yes. Usually when a company invests money into a research project they would do so with the expectation of making a profit."
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
    # Maybe something about building a park/playground for everyone? 
    return


label community2:
    "You've run out of storage space in your cellar, so you take the extras over to the storehouse."
    kevin "I'm aware that it's less efficient. But if I don't bring you my whole harvest, you won't know how much food I'm making. It's also part of our contract."
    ilian "I trust you to not hoard food, but I do appreciate your thoroughness. As long as you can manage bringing it all over."
    ilian "Hi [his_name]. Maybe your surplus can make it worth Kevin's while to come out here and they can have more variety in their diet."
    him "Sure, do you like spinach?" #to do:is there a way to call a vegetable that has been planted?
    kevin "A variety of foodstuffs is beneficial to anyone's diet."
    ilian "You know, Kevin and Zaina brought me everything that they harvested. Apparently that's the way we've supposed to have been doing it all along."
    him "Huh, really? How in the world do you have time to farm?"
    kevin "I can't start my engineering calculations until Zaina finishes her assessment, so farming is a useful pastime."
    him "'It's so much more than a pastime for us!'"#to himself
    kevin "I must depart, but I will take some of what [his_name] brought, if that's permissible."
    ilian "That's what I'm here for."
    #kevin leaves
    ilian "We probably should start doing things the way it is in the contract."
    ilian "I know it seems less efficient, but it gives us more control in the case of a famine."
    him "What if the storehouse burns down? Then we'll all have nothing."
    ilian "Or some alien varmint could eat it all no matter where it is."
    ilian "Look, I'm just telling you what our contract says. Do you want to read the fine print? I have it here on my tablet."
    menu:
        "Actually, yes.":
            jump contract
        "No, I believe you.":
             $ pass
    label after_contract:
    ilian "Will you start bringing your whole harvest in or not?"
    menu:
        "Should I bring my whole harvest in to the storehouse?"
        "I can bring in the whole harvest.":
            $ colonists += 1 
            $ miners += 1 #TODO: another variable for this event?
            $ whole_harvest_to_storehouse = True
        "Push to have each farmer store most of their own crops. It's more efficient, right?":
            $ luddites += 1
    return
    
    label contract: #to do: make this a different font with a white paper fade-in so it looks all businessy
        "In return for your individually contracted compensation, Rare Earth Tech, hereafter referred to as 'RET', will provide supplies, technology, and infrastructure to RET Colonists. Farmers will farm 3 acres to the best of their ability as weather permits."   
        "All food farmed by RET Colonists and all livestock raised by RET Colonists is property of RET, to be rationed out by the Storehouse Manager to all RET Employees according to the chart in Appendix C based on family size and estimated caloric consumption."  
        "Any Colonist not in accordance with this agreement will not be accorded Storehouse rations and will be expected to return all RET property, including but not limited to technology, vehicles, furniture, tools, etc."
        "Colonist couples of childbearing age must attempt to replace themselves through reproduction. Children of RET employees are also RET employees with regards to the legal status of their surplus goods."
        "RET reserves the right to amend this document as it sees fit."
    jump after_contract


label community3:
    thuc "What the heck. Did you just do that?" #is heck too Mormon
    him "Yes, I did. With the bonuses from my cavalry, my legendary general, and my superior navy from starting on an island, I can conquer Russia in one turn!"
    pete "That's the last time I let you start as Tonga!"
    thuc "I think you just won the game."
    him "I don't know, there might be a way for you to make a religious conquest!"
    thuc "Nope. I resign."
    pete "Well, that was a good game. I should have situated myself better from the beginning. I got caught up in collecting gold instead of buildin' an army."
    him "Same time next month?"
    pete "Yes, I reckon so. I'll remind you on the community bulletin."
    him "Can we call it something other than game night? All the new colonists will think we're a bunch of nerds."
    pete "Well, we are a bunch of nerds."
    him "Fine, then they'll believe me when I tell everyone I'm going to an intensive research session with you!"
    pete "Ha! Fine by me. As long as everyone else calls it that they'll be none the wiser."
    "A few months later, Kevin asks about it." #why are you talking to Kevin
    kevin "I keep seeing people attending 'intensive research sessions' on the colony calendar. What are they?"
    him "Oh, those. It's just people talking to Pete about stuff."
    kevin "How does he assist in research? Pete isn't equipped to help with fieldwork."
    him "I happen to have some research interests outside of fieldwork."
    kevin "He's a librarian, right? Is your hobby art history or something similar?"
    him "No, it's far more mundane. That's just what we call our monthly game night."
    kevin "I would love to play games with others. Why was this information hidden?"
    him "I didn't want the new colonists to think I was being frivolous with my time."
    kevin "Face-to-face socialization is highly recommended by RET's psychologists."
    kevin "It may feel frivolous, but it can actually increase your productivity."
    him "But farmers a long time ago didn't have time to play cards. They worked from sunup to sundown without complaining."
    kevin "That's simply what they told their grandchildren. Let me come to your game night!"
    him "Okay, come then! We need someone to shake things up."
    kevin "Shall I invite the other new colonists as well?"
    menu:
        "Sure, invite them all! We can reserve the town hall.":
            $ colonists += 1
            $ town_hall_games = True
            jump invite_all
        "They can make their own game night if they want.":
            $ luddites += 1 #rationale: the luddites are a product of the colonists becoming more fractured
            jump no_invite
        "I'll ask Pavel, the mayor, to remind them to make socialization a priority.":
            $ pass
            jump ask_pavel
        
    label invite_all:
        "Next month, we invited everyone to town hall to game night."
        "Only three or four people showed up, including Kevin, but they were happy to play games with us."
        return
        
    label no_invite:
        "I told Kevin that I liked the intimate atmosphere of playing games in someone's house, and we couldn't simply invite everyone."
        "He came to a few game nights but I think he ended up hosting his own with some of the other new colonists."
        return
         
    label ask_pavel:
        "I asked Pavel to remind everyone to remember to get to know the new colonists."
        "He sent an annoucement to the community bulletin."
        "I don't know if anyone actually did anything about it, but the thought was there."
        return

label community4:
    "Pavel, our mayor, called a town meeting."
    pavel "Rare Earth Tech sent us an instantaneous message, which was limited to 250 characters because of the limitations of the technology."
    pavel "This is what it said:"
    #TODO: separate style for RET messages?
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "Please elect a liason to help RET and colonists communicate and resolve conflicts of interest."
    elif(style == "authoritarian"):
        "We need a designated contact with the colony that you trust. Send your decision."
    elif(style == "permissive"):
        "You should probably choose someone to represent the colonist's interests to us."
    else:
        "Please elect a liason to help RET and colonists communicate and resolve conflicts of interest."
        
    pavel "It's my job to encourage whatever is best for the colony."
    pavel "I don't want you to ever question my loyalty. We need someone else for this job."
    pavel "The liason will have to understand what RET will want and tell them what's possible and what's not."
    pavel "They'll have to tell us what RET wants and convince us to change if necessary."
    pavel "There may be times when you have to make unpopular decisions, or take the blame for mistakes that weren't yours."
    pavel "I doubt anyone will volunteer for extra work, so we'd like everyone to nominate someone tonight."
    pavel "Then we'll vote on the nominations."
    #TODO: chatter between colonists would make this scene more lively and/or amusing
    menu:
        "Who will you nominate? You may not nominate yourself."
        
        "Sister Naomi, our religious leader and childcare leader.":
            $ pass
        "My wife's friend Sara. She's familiar with colony politics since she assists the mayor.":
            $ pass
        "My friend Thuc. I think that would be funny.":
            $ pass
    "After the nominations, we voted for our favorite candidate."
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
    "Zaina and Kevin discovered Indium nearby and have a plan for how to mine it."
    # It will take 4 Earth years for the miners to arrive. About 8 Talaam years.
    if is_liason:
        "RET sent me an instantaneous communication with advice on how to proceed."
        "It said:"
        $ style = get_parenting_style()
        if (style== "authoritative"):
            "50 new miner neighbors are coming in 4 Earth years. Please figure out the most efficient way to feed them."
        elif(style == "authoritarian"):
            "50 miners are arriving in 4 Earth years. Prepare to feed them, and institute currency so that they can pay you for what they eat."
        elif(style == "permissive"):
            "We're sending fifty miners your way, so if you could feed them, that would be great. They'll have money to pay for it."
        else:
            "50 new miner neighbors are coming in 4 Earth years. Please figure out the most efficient way to feed them."
            
        if (whole_harvest_to_storehouse == True):
            ilian "Well, in what I thought was a colossal waste of resources, a few farmers are already bringing their whole harvest to the storehouse."
            ilian "Based on the harvests of those farmers, we can probably grow and store enough food for the miners, but they will have to eat a lot of bread and beans."
            ilian "Assuming our chickens are still around in four Earth years, we could have hens ready for them to have eggs as well."
        else: 
            ilian "I don't know how much food you guys are storing, so I have no idea if we'll have enough food for them or not."
            ilian "If worst comes to worst, they could farm instead of mining, which I'm sure RET would be THRILLED with."
            
        "How should we prepare?"
        menu:
            "Have all the farmers bring their whole harvest to Ilian instead of storing it individually, and encourage them to grow extra grain and beans.":
                $ miners += 2
                jump whole_harvest_required
            "Have farmers bring in a certain amount of surplus each harvest.":
                $ miners += 1
                jump ration_harvest
            "Don't set aside food for the miners. They can hunt and forage. Feeding miners wasn't in our contract.":
                $ pass #rationale: this has pros and cons for luddites, so I don't actually want to subtract from their score. It's easier to simply not add to the miner variable.
                jump no_formal_rationing
    else:
        show sara at midright
        "Sara called you in to discuss the latest news from RET."
        sara "RET is sending miners to start mining the Indium that Zaina and Kevin found."
        sara "The miners won't arrive for another four Earth years."
        if (whole_harvest_to_storehouse == True):
            sara "Ilian tells me that we'll have enough food for them if we start storing a little now."
        else:
            sara "We're not sure if we'll have enough food for them or not."
        sara "We will start storing the surplus of food that keeps the longest. I've started construction of a few silos for dried grains and beans."
        sara "Next harvest we'll start accepting canned goods as well."
        sara "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sara "I'll be grading your crops against the RET standards."
        sara "There's something I need your help with though. Some of the other farmers aren't excited about storing their surplus in the storehouse."
        him "Really? Like who?"
        sara "Pete and Martin are the ones you know the best."
        him "I'll talk to them." #this could also be a choice... how neglectful do you want to be
        jump talk_about_food_storage
        # TODO: when/where are crops preserved?  Does Ilian have machines/employees that do this? Or are farmers supposed to do this before taking to the storehouse?
    return
    
    label whole_harvest_required:
    ilian "I'll need some help to build silos for the wheat."
    him "Wait, you mean it's not going into vacuum-sealed cans?"
    ilian "We don't have enough metal for that. But we can build big covered containers."
    him "This way we'll definitely have enough for the miners, right?"
    ilian "Yes. They won't even need to forage, unless they want some extra meat."
    jump ration_harvest
    
    label ration_harvest:
    ilian "I support your plan, but I'm worried about how we'll enforce it."
    ilian "Some of the other farmers are reluctant to centrally locate food."
    him "Oh? Like who?"
    ilian "Like Pete and Martin."
    ilian "I think they'd listen to you if you tried to persuade them though."
    ilian "We'll pay credits for their surplus, which they can use to buy other crops."
    him "I'll talk to them."
    jump talk_about_food_storage
    
    label talk_about_food_storage:
    him "Hey Pete. How are your cattle doing?"
    pete "Surprisingly hale for living on an alien planet."
    him "Great. There's something I want to ask you about."
    menu:
        "How do you approach the subject?"
        "I heard that you're not storing much surplus in the storehouse.":
            $ pass
            jump pete_no_storehouse
        "Could you start storing more surplus in the storehouse?":
            $ pass
            jump pete_no_storehouse #this choice has no impact on the story
            
    label pete_no_storehouse:
    pete "This climate is so wet that no amount of salting and drying will make jerky last four Earth years."
    pete "I have yet to successfully make a hard cheese that doesn't mold right away."
    pete "The best way to store my surplus is to keep growing this herd."
    #could have a choice here about how to respond, but you can't really change his mind. or try to bring up the credits thing, and he insists that the colony wouldn't let him starve.
    him "Yeah, you're right. Sorry, I didn't really think about how difficult it would be to store beef and dairy that long."
    pete "Don't mention it." #more pete-style way to say this?
    #change scene
    him "So Martin, how's your farm doing?"
    martin "Pretty good considering that we're on an alien planet!"
    martin "But recently some of our turkeys got sick and we couldn't even eat their meat after they died."
    him "How about your beans, are they doing well?"
    martin "Yes! We eat them about as fast as we can grow them."
    him "I was thinking if you had some extras, you could store them in the storehouse."
    martin "I would if I thought we would have extras. But we're usually trading them to other people for their crops."
    martin "You should know that. [her_name] usually trades vegetables for our eggs and corn."
    him "It works well now, but soon I'll be trading credits instead of food." #player decision instead of the non-decision above?
    martin "Well if anyone wants our food they can come here for it."
    #TODO: choice in conversation with Martin?
    return
    


label community6:
    #if town_hall_games = True, make the background the town hall. else it's at Pete's house.
    show pete at midright
    thuc "I brought 'Maximal Conquest' tonight, are you guys up for it?"
    him "Yes, and I promise to start in the Northern Hemisphere this time."
    pete "Your Antarctica strategy had no sense whatsoever."
    him "Trying the same losing strategy every time and hoping it will win has no sense."
    pete "I'll make you eat your words. Can we keep track of score on your tablet? Ours is out for repairs."
    him "What do you mean? Don't you both have one?"
    show helen at midleft
    helen "No, because SOMEONE left it out during a solar flare."
    pete "And SOMEONE left their tablet in spittin' distance of a cow."
    him "That must be rough."
    pete "Actually I've found it liberating. I used to perpetually check my tablet for new messages. Now I know how useless most of them were."
    pete "I can completely think about what I'm doing."
    pete "I do my feed calculations for the cattle by hand."
    helen "I miss watching TV. But at least one of the tablets is repairable, so we should be back to our normal selves soon."
    pete "I don't know about me. I kind of like feeling like I'm completely on my own."
    thuc "But you still are having game night, and you have your family too, so it's not like you're completely isolated."
    menu:
        "What do you think?"
        "We need each other to survive.":
            $ colonists += 1
            him "We need each other to survive. There's no way one person could survive on their own out here."
            pete "Is that really true? I've been out there on my own before--there's good foraging and hunting."
            him "Maybe you could survive on your own, but what about your family?"
            pete "They can help forage too!"
            pete "The most dangerous thing is the solar radiation. Without a radio, we wouldn't know when a solar flare was coming."
            pete "It's definitely more reliable to live in a community where we can help each other."
        "I understand wanting to be away from it all.":
            $ luddites += 1
            him "I understand wanting to be away from it all. It's part of the reason I came here."
            pete "We don't have to deal with inane government interference or rules made for the sake of havin' 'em."
            him "Although some of RETs demands have felt that way..."
            pete "True. But you can see where they're coming from for the most part."
            pete "And they're not in our face about it. I could go camping tonight and they'd be none the wiser."
            him "Yeah, as long as your cows were okay with it."
        "We have an obligation to help RET feed their miners now.": 
            $ miners += 1
            him "Being alone sounds romantic, but we have an obligation to help RET feed their miners now."
            him "If we all went rogue, those miners would starve to death."
            him "And we wouldn't be holding up our end of the bargain. It's expensive to send us out here."
            pete "I do feel bound by my word. But if RET starts askin' more than was in our contracts, I wouldn't feel badly about changing my side of things."
            him "What do you mean?"
            pete "What if we don't have enough food for all these miners?"
            pete "If that happens, you bet I'm going to look after me and my own first."
            pete "We're promised enough food to live off of, but if that doesn't exist, there's no way RET can make it right."
            pete "We're all trying to farm as efficiently as we can. But if RET overestimated our yields, I don't want to pay for it."
            him "Good point. I hope we can mange."
    return

label community7:
    zaina "The fossil record near here contain many animals that do not have shells. If they had been merely eaten to death, we wouldn't have their fossils."
    zaina "One possibility is that an area that used to be part of the ocean became locked into one area, and they ate up all possible prey."
    zaina "Another possibility is that solar flares are a geologically recent event, and that they died quickly once the flares started."
    zaina "However, the existence of other animals at the same time with shells that are resistent to radiation makes it likely that the solar flare problem was cyclic."
    pavel "Thank you, Zaina, for the presentation on Terra's probable geologic history."
    pavel "We want you to feel that your fellow farmers are co-workers, so please use this time to talk to them."
    pavel "I know you're all very busy, so we've arranged for a few extra free carrots for those of you who stay and socialize for fifteen minutes."
    kevin "I'm surprised that you're offering incentives. The excitement of living on a new planet was sufficient payment for Zaina and I to come to Talaam."
    him "At least I know that my parents are taken care of."
    kevin "What do you mean?"
    him "RET gave me a bunch of money that I used for their retirement fund."
    kevin "They made me no such offer."
    thuc "I practically had to pay RET to let me come. What gives?"
    him "Huh. You're basically giving up your lives on Earth, so I'm surprised that they didn't offer you some kind of compensation for that."
    ilian "Maybe some of us were happy to leave our Earth lives behind."
    helen "This is a new one for me. Ilian has a secret past?"
    ilian "There's nothing secret about it. I was about to default on my loans for my restaurant supply store."
    ilian "RET said they would take care of it."
    helen "Do you know if they did?"
    ilian "I haven't heard from any debt collectors since."
    kevin "You may have noticed but it's very difficult for people on Earth to contact you here."
    ilian "It was win-win for me."
    kevin "I was so intent on coming to Terra that I didn't think to negotiate compensation."
    thuc "I wish I had thought of negotiating too. Now that I think about it, they really needed me."
    him "Oh come on. They could have found some other sustainable agriculture specialist with 10 kids."
    thuc "Or 8! Fewer pieces to ship."
    kevin "Did your children suffer developmental delays because of the journey?"
    thuc "One of them is a little shorter than the rest, but other than that I'd say that being on a different planet has accelerated their development."
    thuc "They're not necessarily reading sooner, but we genuinely need their help on the farm."
    thuc "They have more responsibilities than I did at their age, so they have to grow up fast."
    thuc "And none of my family are getting paid for completely transplanting our lives here."
    if is_liason:
        thuc "Hey [his_name], can I make a formal request? I'd like RET to donate $10,000 to the charity of my choice."
        menu:
            "I'll ask them in my next e-mail.":
                $ miners += 1 
                thuc "E-mail? Not an insta-com?"
                him "I only get so many instant communication slots."
                thuc "But by the time they get your e-mail no one will remember me."
                him "I think RET has bigger things to worry about."
                thuc "Fine, an e-mail is fine."
            "From a business standpoint, you're stuck here. You don't have any leverage anymore.":
                $ luddites += 1
                thuc "I sure do have leverage!"
                thuc "I could decide to leave the colony!"
                him "You wouldn't seriously consider that."
                helen "I don't know, he looks pretty serious."
                thuc "I'm joking. Rice cultivation is kind of pointless for just twelve people." 
                thuc "I just don't like the idea that I have no power over my life."
            "I hear you, but let's focus on the here and now.":
                $ colonists += 1
                him "I could ask them in an e-mail. But what about all the rest of the new colonists who didn't receive compensation either?"
                him "Let's leave the past in the past."
                him "Get stinking rich off your enormous farm and have a feast to make us all jealous."
                thuc "You do have a point. With my new crop of fertilizer I'll be stinking at least!"
    else:
        thuc "Hey, Sara, help me out here. Could you ask RET to send my back pay to the charity of my choice?"
        sara "I heard that RET is economizing, but I can ask."
        thuc "Thanks."
        # better non-liason option?
    return


label community8:
    #TODO: define the talked_to variables as false in the defines? document
    if is_liason:
        "Urgent insta-com from RET!"
        $ style = get_parenting_style()
        if (style== "authoritative"):
            "We have extra space on the shuttle. What Earth luxuries would the colony like?"
        elif(style == "authoritarian"):
            "Tell us what extras to put on the shuttle by this evening."
        elif(style == "permissive"):
            "If you want Earth goodies, tell us what to put in the shuttle by tonight!"
        else:
            jump no_luxuries
        "Besides a new battery for my tractor, I'd really like some good Earth toilet paper. [her_name] wants some Gouda cheese culture."
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
                natalia "I don't care what else comes from Earth, but there had better be some medication for Martin in there. The longer he lives, the happier our family will be. [her_name] said he needed Vemurafecholoronib." #TODO:if you want to make this harder, have the player go ask her what the medication is.
                $ talked_about_luxuries_counter += 1
                $ talked_to_Natalia = True
                jump talk_about_luxuries
            "Thuc Nguyen" if not talked_to_Thuc:
                show thuc at left
                with dissolve
                thuc "I'd like to grow peanuts. Regular, unroasted peanuts will work fine for cultivation purposes."
                thuc "Then I can make peanut stew and peanut butter!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Thuc = True
                jump talk_about_luxuries
            "Sara" if not talked_to_Sara:
                show sara at right with dissolve
                sara "Oh, I don't know if this is possible, but I would really, really love a bicycle."
                sara "I'm terrible with horses and I hate how they just eat more of our food."
                sara "A bicycle wouldn't get hurt by radiation and can go faster in some situations."
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
                kevin "I would like the remaining episodes of the show Tulip House."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Kevin = True
                jump talk_about_luxuries
            "Pavel" if not talked_to_Pavel:
                show Pavel at left with dissolve
                pavel "Oh, there are so many things I miss."
                pavel "Sushi, wine, tempura, Krem de la Krem donuts, French fries, falafal, fried chicken,"
                pavel "those really cheap frozen pizzas from Glosemitto's, slow-roasted coffee, Fabrielle brand pelmeni,"
                pavel "sourdough bread, calamari, egg rolls but especially the sweet-and-sour sauce with lots of high fructose corn syrup,"
                pavel "Goods Inside cereal, homogenized milk, cotton candy, cheesecake, tuna salad, Michele's meat-alike paste,"
                pavel "really hot salsa, tortillas, curry powder, Chocolate Confession ice cream, and Swiss cheese, or any cheese really."
                pavel "And that's just the food I miss!"
                him "Wow. Well, it needs to be non-perishable or at least have a long shelf life, so I think that eliminates most of the things on your list."
                him "I could put you down for curry powder though."
                pavel "Oh, well make sure it's PatiPal's Extra Hot Curry Powder. It's the only one worth having."
                him "I'll see what I--"
                pavel "Wait, wouldn't it make more sense to grow the spices so I can make my own curry powder?"
                him "Sure."
                pavel "Okay, so just ask them to send me seeds for all the spices in PatiPal's Extra Hot Curry Powder along with a recipe."
                him "Hmm. I need to put this in an insta-com."
                pavel "Oh dear. How did they not tell you about this sooner?"
                him "I think they only knew about the extra space on the shuttle this morning."
                pavel "You are going to have to cram a lot into that message!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Pavel = True
                jump talk_about_luxuries
            #TODO: Add more people
        label write_report:
            "What will you write? You have a limited amount of characters." #plausible?
            menu:#TODO: Make the options make sense regarding character count and above player decisions. Or just say "you don't have enough space to ask for everything specifically."
                "Toilet paper, Gouda cheese culture, peanuts, a bicycle, and cancer medicine for Martin.":
                    $ pass
                "Vemurafecholoronib for Martin, TP, G-cheese, peanuts, and bicycle.": #this option will help Martin live another year, and Joanna and Tomas don't join the Luddites with this option. Change to a more specific, long name, to justify it having to take up a lot of characters.
                    $ asked_only_medicine = True
                    $ pass
            "I sent the message."
    else:
        sara "RET just told me that they have extra space on their shuttle and they can send some extra things from Earth to us."
        sara "What would you like?"
        him "Let me think about that."
        sara "I need to know right now."
        him "Hmm. How about some good old Earth toilet paper?"
        sara "Great. I can shorted that to TP in the insta-comm."
        him "Hopefully they won't send me a textbook on Topological Planning."
        sara "Don't get your hopes up. But look on the bright side: in four years you probably won't even remember what you asked for!"
        #TODO: Maybe Sara asks you to go ask everyone? better alt?
    return
        
    label no_luxuries:
    show him at left with dissolve
    show her at right with dissolve
    him "Man, I really miss Earth toilet paper."
    her "Wouldn't it be great if RET sent some on the next shuttle?"
    him "Yeah, that's never going to happen."
    
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
        #this feels like it escalated really quickly. Talk with both parties before the menu? depending on your relationship.
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
    #this even doesn't have to be about meat either.
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
    sara "Dr. [her_name], do you have any advice for us?"
    her "For women with regular cycles, tracking the time of ovulation works fairly well."
    her "Couples may wish to exercise their creativity if they wish to avoid conception yet remain intimate during the woman's fertile time."
    her "So, [his_name], is RET trying to grow the colony?"
    him "I honestly think it's just economic. Miranda, do you know if any of the local plants could be used as birth control?"
    #todo: set up Miranda as a character
    #miranda I'm not sure about preventing birth, but I know that fire grass can abort pregnancies in the early stages.
    #consequences if you said not to trade for it in community 21
    # Maybe Kelly offers to perform sterilizations, though she's not an expert. "I'd rather perform sterilizations than abortions".
    
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
