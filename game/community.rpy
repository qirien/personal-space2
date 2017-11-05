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
    "They were our family here, whether we liked it or not, so like a family, we had our fights and jealousies and annoyances -- but we learned to get along."
    return
    

label community1:
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    "After the introductions, you get in line with your friend Thuc to have some soup."
    scene community_center with fade
    show thuc at midright
    show him normal at center
    show ilian at midleft
    thuc "It's pretty exciting to have some new faces around!"
    him "How's it going? Julia couldn't make it?"
    thuc "No, she was too worn out."
    ilian "I wish I could have stayed home. After talking to people all day the last thing I want to see is more people."
    him "At least there's free soup."
    ilian "It's not free, it came from all those crops you paid to the storehouse! So if any of you gave subpar stuff, we're going to taste it."
    "You get your soup and sit with some of the new colonists."
    scene community_center with fade
    show him normal at midleft
    show zaina at center
    show kevin at midright
    him "Hi, I'm [his_name]."
    zaina "I'm Zaina, and this is my husband Kevin. I'd let him speak for himself but his mouth is full, so I'm socially obligated to be polite in his place."
    him "Nice to meet you, Zaina and Kevin. Where will you be living?"
    zaina "We've set up a house out by the radio tower. It's closer to the mountains where I'll be working."
    kevin "And after Zaina figures out where the goods are, I'm in charge of figuring out if it's even possible for us to mine."
    him "Oh, right, that's Rare Earth Tech's plan to pay for this whole expedition."
    kevin "Yes. Usually when a company invests money into a research project they would do so with the expectation of making a profit."
    "What do I think the colony's purpose is?"
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
    kevin "It is part of our contract that I bring you my whole harvest, even if I will consume all of it."
    ilian "I do appreciate your thoroughness. I hope it wasn't too much trouble to show me your buckets of tomatoes and squash."
    ilian "For things that keep a long time, you don't have to bring them right away."
    ilian "Hi [his_name]. Maybe your surplus can make it worth Kevin's while to come out here and he can have more variety in his diet."
    him "Sure, do you like spinach?" #to do:is there a way to call a vegetable that has been planted?
    kevin "A variety of foodstuffs is beneficial to anyone's diet."
    ilian "You know, Kevin and Zaina brought me everything that they harvested this week. Apparently that's the way we've supposed to have been doing it all along."
    him "Huh, really? How in the world do you have time to farm?"
    kevin "I can't start my engineering calculations until Zaina finishes her assessment, so farming is a useful pastime."
    him "It might be an amusing pastime for you, but it's our survival you're talking about here."
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
    him "How about I can write down the amount I harvest and I'll bring in the surplus? Or I could take a picture."
    ilian "I'm pretty sure I could trust you, but it's better if I can measure it all so we can be consistent."
    him "Okay, I see your point."
    menu:
        "Should I bring my whole harvest in to the storehouse?"
        "I can bring in the whole harvest.":
            $ colonists += 1 
            $ miners += 1
            $ whole_harvest_to_storehouse = True
            #TODO: make this add to the future stress variable
        "I will keep storing most of my own crops.":
            $ luddites += 1
    return
    
    label contract: #to do: make this a different font with a white paper fade-in so it looks all businessy. something weird is happening with it right now.
        computer "In return for your individually contracted compensation, Rare Earth Tech, hereafter referred to as 'RET', will provide supplies, technology, and infrastructure to RET Colonists." 
        computer "Farmers will farm 3 acres to the best of their ability as weather permits."   
        computer "All food farmed by RET Colonists and all livestock raised by RET Colonists is property of RET, to be rationed out by the Storehouse Manager" 
        computer "to all RET Employees according to the chart in Appendix C based on family size and estimated caloric consumption."  
        computer "Any Colonist not in accordance with this agreement will not be accorded Storehouse rations" 
        computer "and will be expected to return all RET property, including but not limited to technology, vehicles, furniture, tools, etc."
        computer "Colonist couples of childbearing age must attempt to replace themselves through reproduction." 
        computer "Children of RET employees are also RET employees with regards to the legal status of their surplus goods."
        computer "RET reserves the right to amend this document as it sees fit."
    jump after_contract


label community3:
    thuc "No. No way! Did you just do that?"
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
        "Plz elect a liason 2 help RET & colonists communicate & resolve conflicts."
    elif(style == "authoritarian"):
        "We need a designated contact with the colony that u trust. Send ur decision."
    elif(style == "permissive"):
        "U shld choose some1 2 represent the colony 2 us."
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
        "Who should I nominate? I can't nominate myself."
        
        "Sister Naomi, our religious leader and childcare leader.":
            $ pass
        "My wife's friend Sara. She's familiar with colony politics since she assists the mayor.":
            $ pass
        "My friend Thuc. I think that would be funny.":
            $ pass
    "After the nominations, we voted for our favorite candidate."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "My fellow colonists elected me to be the new representative."
        $ is_liason = True
        return
    elif(style == "authoritarian"):
        "Sara, and Sister Naomi and I were nominated. I had the most votes, but not the majority."
        $ is_liason = True
        return
    elif(style == "permissive"):
        "I was nominated, but Sara was elected as the new representative."
        return
    else:
        "Sara is elected as the new representative."
        #TODO: does the order of these options matter for variable settings?
        #should a leader of the militia be elected here as well?
    return


label community5:
    $ talked_cans = False
    $ talked_credits = False
    $ require_whole_harvest = False
    $ rationing = False
    $ talked_something = False
    $ talked_canning_dairy = False
    "Zaina and Kevin discovered Indium nearby and have a plan for how to mine it."
    # It will take 4 Earth years for the miners to arrive. About 8 Talaam years.
    if is_liason:
        "RET sent me an instantaneous communication with advice on how to proceed."
        "It said:"
        $ style = get_parenting_style()
        if (style== "authoritative"):
            "50 new miner neighbors are coming in 4 Earth years. Plz feed them when they come."
        elif(style == "authoritarian"):
            "50 miners are arriving in 4 Earth years. Prepare 2 feed them, and create $ so that they can pay u 4 what they eat."
        elif(style == "permissive"):
            "We're sending fifty miners ur way, so if u could feed them, that would be g8. They'll have $."
        else:
            "50 new miner neighbors are coming in 4 Earth years. Feed them."
            
        if (whole_harvest_to_storehouse == True):
            ilian "Well, a few farmers are already bringing their whole harvest to the storehouse."
            ilian "Based on the harvests of those farmers, we can probably grow and store enough food for the miners, but they will have to eat a lot of bread and beans."
            ilian "Assuming our chickens are still around in four Earth years, we could have hens ready for them to have eggs as well."
        else: 
            ilian "I don't know how much food you guys are storing, so I have no idea if we'll have enough food for them or not."
            ilian "If worst comes to worst, they could farm instead of mining, which I'm sure RET would be THRILLED with."
            
        "How should we prepare?"
        menu:
            "Have all the farmers bring their whole harvest to Ilian instead of storing it individually, and encourage them to grow extra grain and beans.":
                $ miners += 2
                $ require_whole_harvest = True
                jump whole_harvest_required
            "Have farmers bring in a certain amount of surplus each harvest.":
                $ miners += 1
                $ rationing = True
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
        sara "Next harvest we'll start accepting canned goods as well. You can can large amounts in the storehouse, or bring in what you can at home."
        sara "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sara "I'll be grading your crops against the RET standards."
        sara "There's something I need your help with though. Some of the other farmers aren't excited about storing their surplus in the storehouse."
        him "Really? Like who?"
        sara "Pete and Martin are the ones you know the best."
        him "I'll talk to them." #this could also be a choice... how neglectful do you want to be
        $ rationing = True
        jump talk_about_food_storage
        # TODO: when/where are crops preserved?  Does Ilian have machines/employees that do this? Or are farmers supposed to do this before taking to the storehouse?
    return
    
    label whole_harvest_required:
    ilian "I'll need some help to build silos for the wheat."
    him "Wait, you mean it's not going into vacuum-sealed cans?"
    ilian "Well, yes it is. It's just a few giant cans instead of lots of little ones."
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
    him "I heard that you're not storing much surplus in the storehouse."
    jump pete_no_storehouse
            
    label no_formal_rationing:
    him "We can figure it out when they get here. Growing food for miners wasn't in our contracts, so it sets a bad precedent to save food for them."
    him "Worst-case scenario, they have to farm for a bit instead of mining all the time."
    ilian "Are you sure? I don't really want to be eaten if we run out of food."
    him "I think people could survive on the wild resources available, as long as they know what they are."
    ilian "Okay, whatever you say."
    return
            
    label pete_no_storehouse:
    pete "This climate is so wet that no amount of salting and drying will make jerky last four Earth years."
    pete "I can't make cheese that doesn't mold right away."
    pete "The best way to store my surplus is to keep growing this herd."
    label convince_Pete:
    menu:
        "Is that really the best way?"
        "We could can some of the meat." if not talked_cans:
            him "I know canned meat doesn't taste very good compared to fresh, but it will keep for longer."
            him "How about it?"
            pete "I don't think anyone should have to eat canned meat, not when they live next to me!"
            him "Well, they're your cows."
            $ talked_cans = True
            jump convince_Pete
        "You'll need credits to get other food." if not talked_credits:
            him "Even if the best way to store cow meat is on a live cow, you're still going to need to eat something other than milk and meat."
            him "How will you afford vegetables and grain?"
            pete "Plenty of people are willing to trade for or buy milk and beef."
            pete "Ilian is just acting as a middleman. I don't like that he controls all the prices of food either."
            pete "I prefer to deal directly with my customers."
            $ talked_credits = True
            jump convince_Pete
        "If we canned some beef, then we'd have meat even if your herd died suddenly." if not talked_something:
            him "What if one day you wake up and your whole herd of cattle is gone?"
            him "If you canned some meat, then we would at least have something."
            pete "That's true. But the herd is so small now that I need every cow and bull for good genetic diversity."
            pete "Plus I think canned meat is revolting. I would rather just eat vegetables."
            $ talked_something = True
            jump convince_Pete
        "We could can some of the dairy products." if not talked_canning_dairy:
            him "We could try making dried milk powder or clarified butter, which would last a long time."
            pete "Why would we do that when we have plenty of fresh stuff?"
            him "Well, I know cows don't produce consistently. So you could have some dairy on hand in case your cows don't eat as much."
            him "Or they could end up eating some plant that makes the milk taste bad, so you'd be missing out on an opportunity to sell."
            pete "Hmm. That is a good point."
            $ talked_canning_dairy = True
            jump convince_Pete
        "I guess that's what Pete is going to do.":
            him "Yeah, you're right. Sorry, I didn't really think about how difficult it would be to store beef and dairy that long."
            pete "Glad you understand."
            jump canning_dairy
            
    label canning_dairy:
    if talked_canning_dairy:
        pete "I'll look into canning some milk and butter though."
        him "Great!"
        $ colonists += 1
    else:
        pass
    #change scene
    him "So Martin, how's your farm doing?"
    martin "Recently some of our turkeys got sick and we couldn't even eat their meat after they died."
    him "How about your beans, are they doing well?"
    martin "Yes! We eat them about as fast as we can grow them."
    him "I was thinking if you had some extras, you could can them and store them in the storehouse."
    martin "I would if I thought we would have extras. But we're usually trading them to other people for their crops."
    martin "You should know that. [her_name] usually trades vegetables for our eggs and corn."
    if require_whole_harvest:
        him "Starting from now on, you'll need to bring in your harvest to Ilian if you want other crops."
        him "We need to prepare to feed the miners, and this is the easiest way to ensure that everyone has enough food."
        martin "What if I don't want to do that?"
        him "It's in your contract."
        martin "Well the way we've been doing it has been working just fine."
        him "We didn't have fifty extra mouths to feed then."
        martin "And we don't now! I think you're overreacting. We have plenty of food."
        him "How about you prove that I'm overreacting by bringing all your food to Ilian so we know what we have to work with?"
        martin "We eat most of our crops the same day we harvest them. But we do try to store a little extra."
        him "I get what you're saying. Just write down how much you eat and tell Ilian."
        him "Then if you have extra, bring that in once a week and he can calculate how your crops are doing."
        martin "Okay, I think I can do that. But I still think this is excessive."
    elif rationing:
        him "Starting from now on, I need you to bring in twenty percent of your harvest."
        him "That number may change, but this is the easiest way to start storing a little food for the miners."
        martin "What if I don't have enough food to bring in twenty percent?"
        him "Then bring in ten percent. Just try to keep track so we have an idea of how much food we have collectively."
        martin "Alright. I'll do it."
        him "Thank you."
    else:
        him "It works well now, but soon we'll be trading credits instead of food."
        martin "I'm happy to take your credits then."
        him "Okay, well if you ever need more credits, you can always sell your beans to Ilian."
        martin "Good to know."
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
    pete "Nah, it's better. I used to check my tablet for new messages all day long. Now I know how useless most of them were."
    pete "I can concentrate on what I'm doing."
    pete "I don't even mind doing my feed calculations for the cattle by hand."
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
    if require_whole_harvest:
        thuc "Speaking of food, Ilian just sent out a message that we don't have to bring in our whole harvest anymore."
        thuc "He has enough data, and he sent out a table of who should bring in how much."
        thuc "It ended up being about twenty percent for most farmers." #TODO: is this a reasonable amount?
        pete "I deliver directly to my customers, so I've just been sending Ilian my stats."
        thuc "I guess it doesn't really make sense to bring in a calf either."
        pete "Nope."
        him "It was a little more work to bring in all my crops, but I think I had a better variety of fresh food that way."
        thuc "And in comparison, twenty percent of our crops seems pretty easy to bring in!"
    else:
        pass
    return

label community7:
    zaina "The fossil record near here contains many animals that do not have shells. If they had been merely eaten to death, we wouldn't have their fossils."
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
    kevin "I was so intent on coming to Talaam that I didn't think to negotiate compensation."
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
            "What will you do for Thuc?"
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
        thuc "Thanks. Do you think RET will do anything, [his_name]?"
        menu:
            "What do you think RET should do for Thuc?"
            "They should make a big donation for you.":
                $ miners += 1 
                thuc "Right?"
                him "What charity would you choose?"
                thuc "Something to promote sustainable agriculture in developing nations like this one."
                him "I think the biggest contribution you can make to our developing nation is to keep your goats out of my spinach."
                thuc "Burn!"
            "They won't do anything. RET has you right where they want you.":
                $ luddites += 1
                him "You're stuck here. You have no choice but to be an employee of RET."
                thuc "I could decide to leave the colony!"
                him "You wouldn't seriously consider that."
                helen "I don't know, he looks pretty serious."
                thuc "I'm joking. Rice cultivation is kind of pointless for just twelve people." 
                thuc "I just don't like the idea that I have no power over my life."
            "They probably won't do anything, but we have more important things to worry about.":
                $ colonists += 1
                him "Life isn't fair, but if we work hard, maybe we can eat well while we live it."
                him "Get stinking rich off your enormous farm and have a feast to make us all jealous."
                thuc "You do have a point. With my new crop of fertilizer I'll be stinking at least!"
    return


label community8:
    $ talked_to_Natalia = False
    $ talked_to_Thuc = False
    $ talked_to_Sara = False
    $ talked_to_Kevin = False
    $ talked_to_Pavel = False
    $ no_luxuries = False
    
    if is_liason:
        "Urgent insta-com from RET!"
        $ style = get_parenting_style()
        if (style== "authoritative"):
            "Have 10kg Xtra space on the shuttle. What Earth luxuries u like?"
        elif(style == "authoritarian"):
            "Tell us what extras to put on the shuttle by this evening."
        elif(style == "permissive"):
            "If u want Earth goods, tell us what u want by 2night!"
        else:
            $ no_luxuries = True
            jump luxuries_absent
        "RET must be talking about the shuttle coming with the miners."
        "I'm not sure why they couldn't have asked about our preferences sooner."
        "I'd really like some good Earth toilet paper. [her_name] wants some Gouda cheese culture."
        "I need to find out what everyone else wants too, and send a brief message summarizing it. TODAY."
        $ talked_about_luxuries_counter = 0
        label talk_about_luxuries:
            if (talked_about_luxuries_counter >= 4):
                if is_liason: 
                    him "Oh, it's already the afternoon! I need to send in my report right away."
                    jump write_report
                else:
                    "I told Sara what everyone wanted, and she wrote the report."
                    return
        menu:
            "Who will I talk to about what Earth luxuries they want?"
            "Natalia" if not talked_to_Natalia:
                show natalia at left
                with dissolve
                natalia "I don't care what else comes from Earth, but there had better be some medication for Martin in there. The longer he lives, the happier our family will be." 
                him "What medication does he need?"
                natalia "[her_name] said he needed Vemurafecholoronib. Let's see... 500 mg for six months and 1000 mg for another 6 months." 
                him "Won't RET be sending this anyway?"
                natalia "They told [her_name] that it wasn't possible, but maybe you can do something."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Natalia = True
                jump talk_about_luxuries
            "Thuc Nguyen" if not talked_to_Thuc:
                show thuc at left
                with dissolve
                thuc "I'd like to grow peanuts. Regular, unroasted peanuts will work fine for cultivation purposes."
                thuc "Then I can make peanut stew and peanut butter!"
                # TODO: if you do this, then allow the user to plant peanuts also
                $ talked_about_luxuries_counter += 1
                $ talked_to_Thuc = True
                jump talk_about_luxuries
            "Sara" if not talked_to_Sara:
                show sara at right with dissolve
                sara "Oh, I don't know if this is possible, but I would really, really love a bicycle."
                sara "I'm terrible with horses and I hate how they just eat more of our food."
                sara "A bicycle wouldn't get hurt by radiation and can go faster in some situations."
                # Would she also want one so that her son could use it?
                $ talked_about_luxuries_counter += 1
                $ talked_to_Sara = True
                jump talk_about_luxuries
            "Kevin" if not talked_to_Kevin:
                show kevin at left with dissolve
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
                show pavel at left with dissolve
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
            #TODO: Add more people?
        label write_report:
            "What should I write?"
            if talked_to_Natalia:
                "I don't have enough room to ask for Martin's specific medicine and dosage and all the other things people wanted."
                menu:
                    "Specify the medication and dosage. Do your best with the other stuff.":
                        $ asked_only_medicine = True
                    "Maximize happiness and ask for everyone else's stuff specifically.":
                        $ pass
            else:
                "I sent the message."
                return
    else:
        sara "RET just told me that they have extra space on their shuttle and they can send some extra things from Earth to us."
        sara "What would you like?"
        him "Let me think about that."
        sara "I need to know right now."
        him "Hmm. How about some good old Earth toilet paper?"
        sara "Great. I can shorten that to TP in the insta-comm."
        him "Hopefully they won't send me a textbook on Topological Planning."
        sara "Don't get your hopes up. But look on the bright side: in four years you probably won't even remember what you asked for!"
        sara "Can you help me ask everyone else what they want? I have a list here of people you know and could ask pretty easily."
        him "Okay, yeah, I can do that."
        jump talk_about_luxuries
        
    label luxuries_absent:
    show him at left with dissolve
    show her at right with dissolve
    him "Man, I really miss Earth toilet paper."
    her "Wouldn't it be great if RET sent some on the next shuttle?"
    him "Yeah, that's never going to happen."
    
    return


label community9:
    #where is this
    pete "Hey, [his_name]!"
    him "Hi Pete."
    pete "How's the farm?"
    him "Doing okay I guess."
    pete "I miss having guy's night!"
    him "Yeah. Things got really busy with our last harvest and we never really picked it up again."
    pete "What do you say to accompanying me on a hunting expedition?"
    him "Now?"
    pete "No, this weekend. We can camp overnight so we can get further from the colony."
    him "Is that really necessary?"
    pete "Yes, the hunting is no good around the colony. I think all the strange animal sounds scares off the smaller creatures."
    pete "We'll only go a few miles out. Until we find a herd of those grass crabs."
    "What do I tell Pete?"
    menu:
        "Sounds fun! Go with him and invite Thuc": #you learn the particulars of how to camp safe from radiation.
            $ luddites += 1
            $ colonists += 1
            pete "We have two radiation-proof tents that RET sent with us."
            pete "I don't like relying on them for so many things though, so I'm going to try out my own radiation-proof tent."
            him "And you're testing it on us?"
            pete "No, we'll use the RET tents. I will test my homemade tent though."
            pete "Bring something to sleep on and some food. And get a bow and arrow from the community center." 
            him "Not the rifles?"
            pete "With the guns, they all run away when they hear the shot. I want to see if the bow and arrow does any better."
            pete "Plus it seems funner to use a bow."
            him "I haven't praticed shooting a bow and arrow before."
            pete "Not even in the simulations on the shuttle ride out here? We had so much time for that!"
            him "I was more concerned about reading the latest research on alien plants and running farm simulations."
            pete "You can set up traps then. I want to fell one of these creatures by my own power!"
            him "I'll bring some wire for snares I guess."
            "You tell Thuc about the campout and he joins you, bringing a bow from the community center."
            "You find a group of grass crabs and observe them for a while."
            "The grass crabs are about the size of a capybara, but have less meat because of their large shells."
            "While they eat grass, they also eat the woody parts of plants. Their large beak-like claw cuts through the woody part, which allows them to suck on it while on the move."
            #makes sense?
            thuc "It seems like in the morning, they like to be in the sun, but then in the evening, they like to be in the shade."
            pete "They're like insects. The can't make their own body heat so they have to position themselves well."
            him "This herd is a pretty good size. There are some juveniles and also some older animals."
            pete "You can see some of the trails they've been on. Wait for them to settle for the night and then put the traps on the trail."
            thuc "Here [his_name], let me help set up the snares."
            "After a quick dinner of dried fruit and mashed beans, you set the snares."
            pete "Before we turn in, let's make some camouflage for ourselves."
            thuc "I was thinking about that too. We can tie some leaves to our bodies, but it will be noisy."
            pete "We can at least make our clothing more inconspicuous by making the coloring irregular."
            pete "Let's use some of the ashes from the fire to help us blend in with the shadows."
            "After sleeping in tents, you wake up early to catch the grass crabs while they're still drowsy."
            "They gather in the sunlight, warming themselves and chewing on sticks"
            "You're about 20 feet away when you stop trying to get closer."
            pete "Those two big ones look like good targets."
            him "Try not to lose any arrows."
            thuc "I won't lose them but I will definitely loose them."
            him "..."
            "One of the grass crabs looks in your direction and everyone gets silent."
            "The group starts slowly moving away."
            "Pete points to himself and makes a circular motion."
            "He points to a different grass crab that is a bit further off."
            "You all creep around quietly, giving the grass crabs a wide berth. It's slow and laborious."
            "You wish that you had just scared the herd into your snares, since that would have taken less time."
            "It seems like you're maneuvering all morning. Finally, Pete gives you a thumbs-up and draws his bow."
            "He hits one of the animals, but it simply walks off with an arrow sticking out of it."
            thuc "It's still alive!"
            "Together you stalk the animal to see if it will fall over."
            pete "I think I hit it right where its heart should be. Of course, with those shells, it's hard to tell how deep the arrow went."
            "It's lying down and not moving. Pete approaches, knife in hand."
            "Suddenly, the animal pinches Pete's leg with its front claw!"
            pete "Yeeeowch!"
            # TODO: Should this be a timed menu?
            menu:
                "Tackle the crab.":
                    $ luddites += 1
                    #TODO: I want the injured-hand option to result in making less money that month, if we do the currency thing.
                    "You tackle grass crab from behind, easily outweighing it."
                    "The crab releases Pete and tries wildly to pinch you, but the claw isn't flexible enough to reach you while you're on its back."
                    "Pete stabs the crab, but cuts your arm in the process."
                    pete "We got 'em!"
                    him "Your leg!"
                    pete "I think it looks worse than it is."
                    him "Let's get back to camp."
                "Uhhh.":
                    $ pass
                    "You freeze, not knowing what to do. Thuc steps on the crab's claw, and it releases its grip on Pete's leg, but the grass crab scratches Thuc with its smaller, comb-like arm."
                    "Pete thrusts his dagger into the crevice where the crab's shells meet."
                    pete "Got 'em!"
                    him "Are you guys okay?"
                    pete "It doesn't feel too bad. Let's get back to camp and see how things are." 
            "You help Thuc to haul the grass crab back to the camp."
            him "Here, sit down, let's clean these wounds."
            pete "Nothing a bandage can't fix."
            "After everyone is patched up, you find that you've captured a grass crab in one of your snares."
            "Pete gives the grass crab a decoy stick to hold so Thuc can attack it from behind."
            him "This is going to be delicious."
            pete "Let's eat some and then head back."
            "After making a fire, a solar flare warning comes up on the radio."
            pete "Fantastic. I can test my homemade tent."
            him "What did you make your homemade tent out of?"
            pete "The fabric is leather. That doesn't do anything for radiation."
            pete "But after you set it up just so, you pour water into the top and the water insulates from the radiation."
            "Pete pours the water in, and it gradually fills the tent's lining."
            "After about twenty minutes, the radio comes on again to say that the flare has abated."
            pete "And it appears to reduce solar radiation! Too bad it's completely dark in there."
            "Some water leaked from the tent during the time you were waiting."
            pete "It looks like it has a few leaks too."
            him "Hmm. Aren't these shells radiation-proof? Maybe you could build a house out of them."
            pete "Good idea. I'll save them so I can experiment."
            "After eating some of the meat, you and Pete and Thuc bring the rest back to the colony."
            pete "We process cattle all the time, so we can finish butchering the grass crab. I'll make sure you get some."
            pete "Come by in a few hours if you want something fresh, otherwise it's all going to be jerky."
            him "Thanks Pete."
        "Sounds dangerous. I have to focus on farming right now anyway.":
            $ miners += 1 #not sure which side colonists +1 should go on for this one.
            him "What happens if you get pinched by one of those things? It doesn't sound safe."
            pete "That's the whole point! Gets your blood moving."
            him "Just seeing if I'll have enough food for the next month is risky enough for my tastes."
            "Pete went hunting on his own. He brought you back some jerky from the grass crab he killed."
            him "This is delicious."
            pete "It took me nearly all day to finally hit one. Then I had to chase it down!"
            him "Was it worth it?"
            pete "Hell yes! Herding cattle is fine for everyday, but every once in a while I need some excitement in my life."
    return


label community10:
    her "I'm leaving for work now. Goodbye honey!"
    him "Bye [her_name}. Oh, and don't forget that we're having dinner with the Perons tonight."
    her "I wonder what they wanted to talk about..."
    him "Maybe they're just being friendly?"
    "After weeding and clearing out old growth, Terra comes home from school."
    "We make a simple salad together, and when [her_name] arrives we head over to the Peron's."
    natalia "Thanks for coming over. We're just finishing up the rice."
    martin "We made a turkey bean soup. It should go well with your salad."
    #TODO: If we have sprites for any of their kids, I can insert them into the conversation.
    "After the meal, Terra runs off to play with the kids."
    martin "As you may have heard, I have skin cancer."
    her "I assure you that doctor-patient confidentiality is important to me and I would never discuss your health problems without your consent!"
    martin "I know! You are not the only one who knows, however."
    natalia "The more people who know about your disease, the more people who can help us!"
    martin "I have a few more months to live, but already I'm experiencing fatigue and pain that hamper my work."
    martin "My children are old enough to take care of the farm, but I'm not sure if it's a good idea."
    natalia "The don't seem as passionate about the farm as you are."
    him "But now that they're older, don't you have more time to work on the farm?"
    natalia "Absolutely not. I have enough work as it is making food for everyone, washing their clothes, spinning thread and yarn, canning our surplus, making soap, and knitting new clothes."
    natalia "If I were in charge, I would phase out the turkeys and corn. I think I could handle chickens and beans on my own."
    him "Isn't the corn really important for feeding everyone else's animals?"
    martin "Yes, it is the main component of feed for the animals. Someone else would need to start growing more corn if that happened."
    him "What are your older kids interested in, if not farming?"
    natalia "Tomas is always hanging out in the lab, but I think he just wants to spend more time with his wife, Joanna, who works there."
    natalia "Isabella wants to be our colony's finest writer. You may have seen the book of poetry she messaged to everyone."
    martin "And she is a fine writer."
    natalia "Well she can write and help grow our food!"
    natalia "Raul is a good helper on the farm, but he isn't responsible enough to be in charge."
    martin "And Mateo is still too young to do much more than harvest corn and feed the flocks."
    martin "What would you do in my position? Who do you think should take care of the farm?"
    menu:
        "Tomás and Joanna Nguyen should be in charge of the farm and get the other siblings to help.":
            $ colonists += 1
            $ miners += 1
            #more investment in older farms; Tomas and Joanna are less likely to join the luddites this way
            #another possible way to improve the iteractivity here would be to help martin compose an argument about why Tomas and Joanna should care about the farm.
        "Let Natalia scale back the farm. Let their children pursue their dreams.":
            $ luddites += 1
            #then what happens to the corn everyone needs? they need to decide on how to take care of that. Maybe when Pete leaves it's not as much of an issue, since there is less cattle to feed over the winter.
        #Possibly an option (would have work event ramifications): "I can help plan the crops, but I need help from Martin's children to execute the plans."
        #Perhaps a miner wants to switch jobs and be a farmer?  I guess that require this event to be later?
        #right now this choice doesn't affect who gets the farm.
    return


label community11:
    #The shuttle should return to Earth with the mined material as soon as it is full.
    "The shuttle is set to arrive today!" #make this a family conversation?
    "Families gather at a safe distance from the landing area to watch the sky."
    "We shared binoculars and cheered as the shuttle landed."
    "I helped take a wagonload of people to the landing area to greet them and transport people and goods."
    "The people in the shuttle exited one by one."
    sara "Wow, those guys are built. The women, too -- solid!"
    her "Yeah, I'd expect that miners have to be in good physical condition."
    him "They look pretty strong. Almost as strong as all the farmers we have here."
    her "Farmers have to be in good physical condition too!"
    sara "Pavel is already greeting everyone. Let's join him."
    "I was about to introduce myself to one of the miners when I saw someone with amazing red hair."
    "Wait a minute, I recognize him!"
    #BRENNAN ON SCREEN. he looks the same
    # Jack definitely doesn't like him, but doesn't have a great reason.
    # Is Kelly here, too? Could be interesting...
    him "Brennan!"
    brennan "Oh, hello [his_name]. You look surprised. No one mentioned I was coming?"
    him "No, no one mentioned it. Are you here to help [her_name] with her job again?"
    brennan "Oh no. That was never my main objective. Someone here needs to have ties to Earth to care enough to make sure everyone does their jobs."
    brennan "Plus, I was the only applicant with relevant experience, having lived here for a year before."
    her "Hi Brennan, I didn't think we'd ever see you again! How's it going?"
    brennan "I'm really happy to be breathing fresh air, with my feet on solid ground again."
    brennan "How is your daughter? How old is she now in Earth years?"
    him "She's almost seven. You still don't look a day over 30."
    brennan "I'm not, technically. All this space travel has made me into some kind of ageless Dorian Gray, only instead of an awful painting hiding my age, I just have outdated pop culture references."
    him "..."
    brennan "You don't look like you've aged too badly, considering how much sun you must get."
    brennan "Can you help me get everyone together? I need to introduce our Miner Welcome program with Pavel."
    "I help gather everyone, and the wagon makes for an improptu stage."
    brennan "Thank you for the warm welcome! We're planning on staying here a good eight Earth years, and some of us for the rest of our lives." #check years
    brennan "In order to facilitate our integration into your community, we've assigned each family a miner or miner family to get to know through weekly dinners."
    brennan "I sent out the assignments a while ago, so try to find each other!"
    "After asking around, I found our miner."
    #make this a menu
    him "Nice to meet you Chaco. How was the trip over?"
    chaco "Fine."
    him "Did it take a while to adjust to living in such a small space?"
    chaco "No."
    him "What do you like to do in your free time?"
    chaco "Look at the stars."
    "I feel like we're playing 20 questions here! He's probably overhwelmed from the arrival."
    #TODO:no luxuries option
    if no_luxuries:
        jump no_luxuries
    else:
        brennan "We might need some help unpacking. RET sent a package for you guys, so come unpack it!"
        him "I can help you with that."
        him "New batteries for almost everything! And a few new tablets."
        if asked_only_medicine:
            "The exact medicine for Martin came! They included a bunch of other stuff, but some of it wasn't exactly what wanted."
            "The Peron family is crying happily."
            her "Hey, where's the Gouda cheese culture? I was really looking forward to it."
            
            #refer back to community8 for this
            if talked_to_Thuc:
                thuc "These peanuts are roasted. I thought I told you they needed to be unroasted! I can't grow them this way."
            else:
                thuc "Are there any new seeds to grow? I want some of this peanut butter, by the way."
                
            if talked_to_Sara:
                sara "I asked for a bicycle, is that here?"
                him "No, I'm sorry. I couldn't fit everything into the message."
                sara "A bike would probably get tons of flat tires around here anyway."
                him "This looks like a software upgrade for the 3D printer though!"
            else:
                sara "It looks like there's a software upgrade here for the 3D printer."
                
            if talked_to_Kevin:
                kevin "Did they send the rest of Tulip House?"
                him "I'm not sure. There's a big hard drive here for the library though!"
                kevin "There's bound to be something good in there."
            else:
                kevin "I've been wondering what happened in my favorite Earth TV shows. Did they send any media?"
                him "It looks like they sent us a hard drive for the library. You and Pete can look over it."
                kevin "Looking forward to it!"
            
            pavel "These look like plastic pages with compartments full of... seeds? Are these spices?"
            him "Oh, I hope so!"
            pavel "Yes, and it says the cultivation instructions are on the hard drive. I'm looking forward to this!"
            
            if talked_to_Pavel:
                him "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel "I'm so happy right now!"
            else:
                pass
            
        else:
            "RET sent medicine for Martin, but when I gave it to him, he and Natalie looked crestfallen."
            natalia "This isn't the kind of medicine we needed! This is useless!"

            if is_liason:
                natalia "Did you tell them what kind of medicine Martin needed?"
                him "I told them Martin needed medicine, and I assumed that they knew what kind from the doctor's reports."
            else:
                natalia "Sara, why didn't you tell them the exact kind of medicine Martin needed?"
                sara "I'm sorry, I thought they knew what he needed! I just put medicine."
                
            her "Oooh, Gouda cheese culture!"
                
            if talked_to_Thuc:
                thuc "I can start growing these peanuts right away!"
            else:
                thuc "Are there any new seeds to grow? I want some of this peanut butter, by the way."
            
            if talked_to_Sara:
                sara "Oh, are these bicycle tires? Maybe I can make the rest of the bicycle... oh, this looks like a software upgrade for the 3D printer!"
            else:
                sara "It looks like there's a software upgrade here for the 3D printer."
                
            if talked_to_Kevin:
                kevin "Did they send the rest of Tulip House?"
                him "I'm not sure. There's a big hard drive here for the library though!"
                kevin "There's bound to be something good in there."
            else:
                kevin "I've been wondering what happened in my favorite Earth TV shows. Did they send any media?"
                him "It looks like they sent us a hard drive for the library. You and Pete can look over it."
                kevin "Looking forward to it!"
                            
            pavel "These look like plastic pages with compartments full of... seeds? Are these spices?"
            him "Oh, I hope so!"
            pavel "Yes, and it says the cultivation instructions are on the hard drive. I'm looking forward to this!"
            
            if talked_to_Pavel:
                him "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel "I'm so happy right now!"
            else:
                pass
        if asked_only_medicine:
            "Thanks to the cancer medicine, Martin is able to work on the farm for six more months before dying a peaceful death."
            "Tomás and Joanna took a break from working in the lab to learn all they could from him."
            "They promised to help with the corn and turkeys."
            $ miners += 1
            $ colonists += 1
        else:
            jump Martin_dead_sooner
            $ luddites += 1
    return

    label no_luxuries:
        brennan "Can you help us unpack?"
        him "That's what we came out here for."
        natalia "Did RET send any medicine for Martin?"
        brennan "No, sorry, I think they just sent some new batteries and stuff."
        natalia "They don't care what happens to us!"
        martin "I would have liked to live a little longer, but in the end, we can only do so much."
        jump Martin_dead
        $ luddites += 1
        
        label Martin_dead_sooner:
            "Without the medication, Martin's condition swiftly deteriorates, and he dies later that week."
            "Tomás and Joanna Nguyen decide to help out, but they aren't prepared to take full responsibility for the farm."
            "Hopefully they can learn what they need to know from Natalia and their neighbors."
            #TODO: should community 10's decision affect this?
        return

label community12:
    $ sara_investigates = False
    $ know_BBQ = False
    #if require_whole_harvest
    # if rationing
    #else
                
    label beef_shortage:
        him "Oh, and I need a pound of ground beef."
        ilian "Unfortunately, we are completely out of beef."
        him "What?"
        ilian "We're completely out of beef."
        him "I heard you, but I didn't believe you. I thought we had plenty of beef."
        ilian "Well, first the miners maxxed out their alottment. So we're completely out of canned beef. Then one of Pete's cows went missing."
        ilian "It was also a dairy cow, so we're low on milk."
        him "Well, did it just wander off?"
        ilian "I just know what Pete told me, which is that a cow is gone and he isn't going to slaughter any more until he builds the herd back up."
        him "Is there going to be an investigation or something?"
        ilian "Not my problem. We've got lots of chicken meat if you're desperate for meat."
        him "Well I happen to really like beef, and my family likes butter. I want to find out what happened."
        ilian "Go ahead and ask Pete, he knows what happened."
        
        "Since Pete lives far away, I e-mailed him to get the details."
        "In Pete's reply, he e-mailed me, Pavel, Sara, and Natalia." #integrate in e-mail UI-looking thing?

        pete "Thanks for asking about the cattle. A few people have asked so I'm e-mailing all of you right now. I have put tiny screws that look like security cameras at intervals around my fence and I haven't had any more cattle go missing."
        "I rolled my eyes. Like that would fool anyone."
        pete "I think it was the miners. There were tracks of two people with boots and the missing cow that went out the gate toward the miners."
        pete "They had to wake up the cow and push her; I can tell they had a hard time but I bet they had some treat to get her to move."
        pete "I don't know how they'll butcher and slaughter her without the tools for it. Things could get really messy."
        pete "We've already butchered this season's bulls, and with the demand for beef so high, I can't justify slaughtering any cows."
        pete "We'll have to live without beef for a while so that we can give everyone some next season."
        
        "That night we had Chaco over for dinner again as part of our welcome miner program."
        "It was a habit now, and after a few weeks, Chaco got more comfortable with us and talked more."
        him "Thanks for helping with the dishes, Chaco."
        chaco "You're welcome. Thanks for the food."
        chaco "I brought my telescope like you asked. I can show you some stars." 
        chaco "We might be able to see Earth if it's clear."
        him "Great. I think Terra will love that."
        "Seeing Earth, I suddenly felt homesick. I missed grocery stores and delivery services. I missed the way Earth trees silouetted in the sunset."
        "I missed my parents, and the way my mom made macaroni and cheese with bacon on top. I missed my dad's laugh. I missed roads and freeways and the bustle of cities." #believable?
        him "It shows how far away we really are."
        kid "How far away are we?"
        chaco "About four light years." #more precise answer?
        "We looked at the sky."
        him "Oh, a shooting star!"
        kid "I saw it! I saw it!"
        "I want to see if he knows anything about the missing cow. What should I ask?"
        menu:
            "Do you eat beef often?":
                him "Do you eat beef often?"
                chaco "Yes, I do. We usually have a barbeque when we get past our mining quota."
                him "That sounds fun."
                chaco "It is."
                $ miners += 1
                $ know_BBQ = True
            "Do you know about the missing cow?":
                him "Hey did you hear about the missing cow?"
                "Chaco keeps looking at the sky, his face inscrutible."
                chaco "No?"
                him "Pete said that one of his cows went missing."
                him "He said the cow's tracks were going towards the miner camp."
                chaco "Hmmm. I don't know anything about that."
                him "Pete said there wouldn't be any more beef this season."
                chaco "No more beef? That's not good."
        "Chaco packed up his telescope and went home."
        
        "Later on, Pavel sent me a message."
        pavel "[his_name], we have to find out what happened to that cow."
        if know_BBQ:
            him "I heard from Chaco that they have barbeques when they mine over quota."
        else:
            pass
        pavel "Hmm. We need to ask the miners what they know."
        pavel "I know beef is really popular in South African and Chilean cuisine, and I think most of the miners are from those two countries."
        pavel "Can you come with me tomorrow morning? I was able to arrange a meeting with Brennan."
        him "...sure. Did you invite Sara or Natalia? They also seemed invested in the fate of Pete's cow."
        pavel "You were the first person I asked."
        him "Is it because I'm a guy?"
        pavel "And you're interested in what happened to the cow! Three-quarters of the miners are men, so it just seemed like a guy's thing."
        menu:
            "Let's ask Sara if she wants to come too.":
                $ colonists += 1
                $ sara_investigates = True
                "You messaged Sara about meeting Brennan tomorrow morning, and she agreed to come with you."
            "Let's go by ourselves.":
                pass
        
        if sara_investigates:
            "The next day, you meet Pavel and Sara on the road to the miner's village."
            sara "You guys can talk to Brennan. I'll say I'm really into cooking and ask one of the wives what she knows about the cow."
            pavel "Actually, most of the couples who came along are both miners."
            pavel "There are a few people who don't work in the mines though."
            pavel "I think I can talk at length about cooking better than you can. How about I do the recipe swap thing and you can grill Brennan?"
            sara "Yeah, I think you're right. What about you [his_name], does that sound like a good plan?"
            him "Sounds good."
            jump mining_village
        else:
            "The next day, you meet Pavel on the road to the miner's village."
            him "I think one of us should talk to Brennan while the other tries to talk to some of the other people in the miners' village."
            pavel "I've been meaning to ask one of the cooks about her recipes. Are you comfortable talking to Brennan?"
            him "I guess. Sometimes I want to punch his pretty face, but I can restrain myself."
            pavel "He means well."
            jump mining_village
            
        label mining_village:
            "As we approach the mining village for the first time, we see a few columns of smoke rising in the wet morning air."
            pavel "Brennan said he'd meet us just outside the mine. I think that's where their control station is."
            "We walk through the village on the way to the control station, which is higher up on the foothill."
            "Rivulets of waste water flow down the road as we approach. It doesn't smell like urine, so it's probably leftovers from washing."
            "The village consists of a few large communal cabins and some single-family cabins. The single-family cabins are even smaller than mine, if that's even possible."
            "We walk by a short, old woman in the middle of doing her laundry." #wasn't planning for this to be a drawn character
            "Pavel stops and asks her a question about her laundry, and they start talking. He motions for me to continue without him."
            "I arrive at the control station. It looks like one of the houses repurposed for a small two-person office."
            brennan "Yes, and keep going for another 10 meters. Get back to me when you're halfway through and I'll give you an air update."
            
            if sara_investigates:
                brennan "Hello, and welcome. We don't have any extra chairs, so I'm afraid you'll have to stand."
                brennan "I do have some tea though, if you would like some."
                sara "I would like some."
                him "No thanks."
                "Brennan serves Sara some tea."
                brennan "So there's a missing cow, is there?"
                sara "Yes. Have you seen any cows around here? The cow's tracks came this way."
                brennan "Sorry, but I haven't. I'm mostly concerned with how the mining is going, if we're on schedule for our next shipment, and things like that."
                if know_BQQ:
                    sara "I heard that your team likes to have a barbeque when they make it past their mining quota. It seems like you might help supply the beef for that?"
                    brennan "Actually, I don't have anything to do with that. That's their supervisor's job. I'm the project manager."
                    sara "Okay, who is their supervisor then?"
                    brennan "His name is Bandile. He's down in the mines all day though. You could try messaging him."
                else:
                    pass
                brennan "I hope you find the missing cow."
                brennan "Now if you don't mind, I need to get back to work."
                
                "We exit and head down the mountain. Pavel waves and joins us."
                pavel "How was your conversation with Brennan?"
                him "Not great. I can't tell if he's hiding something or just defensive."
                sara "Brennan acts like it doesn't matter what they eat, as long as they're alive."
                pavel "I imagine that's how most employers feel about their miners."
                sara "I don't know why he's playing it so cool. Everyone loves food, right?"
                him "If he acted too concerned about food, then he'd have to admit the missing cow is partially his problem."
                pavel "For what?"
                pavel "They wanted to celebrate one of the local teenagers passing tests to operate heavy machinery."
                sara "Aww, they have community events too!"
                if know_BQQ:
                    sara "Brennan said that the miners's supervisor, Bandile, is in charge of the celebrations."
                    sara "He recommended messaging him. Can you do that [his_name]?"
                    him "Yes. I want to get to the bottom of this."
                    jump message_Bandile
                else:
                    him "Where do we go from here?"
                    pavel "I'll tell Pete what I found out. Circumstantial evidence."
                    jump tell_Pete
                
            else:
                brennan "Hello, [his_name].  We don't have any extra chairs, so I'm afraid you'll have to stand."
                brennan "I do have some tea though, if you would like some."
                him "No thanks."
                "Brennan sipped his tea."
                brennan "How's [her_name] doing? I haven't seen her much since I arrived."
                him "Just fine, thanks."
                brennan "So there's a missing cow, is there?"
                him "Yeah. Pete says that he thinks it was one of your miners. Is that possible?"
                brennan "I think we would have noticed if someone had stolen a cow."
                him "No, but you could have slaughtered it already."
                brennan "How would we have slaughtered it? We have plenty of heavy machinery for cutting through stone but they are too big for cutting up one small cow. Also it would completely mangle the meat."
                him "I don't know how you would have slaughtered it."
                if know_BBQ:
                    him "Chaco told me that you often have barbeques. Is that right?"
                    brennan "Yeah, the miners's supervisor organizes them every so often. Keeps morale up."
                    him "I thought you were the supervisor."
                    brennan "No, I'm the project manager."
                    him "What's the difference?"
                    brennan "I tell everyone how fast the mining has to go for us to be on schedule."
                    brennan "It's not just a monthly check-in kind of thing. I have daily plans for our project, and have to make changes on the fly based on what the miners find, or if someone gets injured."
                    brennan "It's like if we all went on a long walk to the ocean. Probably one of us would be the navigator, making sure we were going the right direction and ready to camp at nightfall. That's me."
                    brennan "Another person would notice if someone was lagging behind, or unhappy for some reason. That's the supervisor."
                    brennan "Surely you have a project manager for the colony's agricultural work?"
                    him "We all trust each other to do our jobs."
                    brennan "Of course. How... quaint."
                else:
                    pass
                brennan "I need to get back to work. I hope you can find the missing cow."
                him "I hope so too."
                "I exit and head down the mountain. Pavel waves and joins me."
                pavel "How was your conversation with Brennan?"
                him "Not great. I can't tell if he's hiding something or not."
                pavel "Understandable."
                pavel "I met Lisa and she seemed to know something, but didn't say exactly what she knew."
                him "Do they have the cow hiding in one of these communal buildings?"
                pavel "I don't know. I do know that they were planning to celebrate a special occasion, probably with some meat."
                him "Oh. What was the occasion?"
                pavel "One of their teenagers passed some complicated tests and they're going to allow her to operate heavy machinery."
                him "Wow. I mean, that does seem worth celebrating. But she didn't say if they had the cow?"
                pavel "No, just that they wished they had some beef."
                him "Where do we go from here?"
                pavel "I'll tell Pete what I found out. Circumstantial evidence."  
                jump tell_Pete
                
        label message_Bandile:
            # $ luddites += 1 not sure if this makes sense
            "I sent Bandile a message asking about the cow." #e-mail/message UI thing
            "Hello [his_name]. Please excuse me for not meeting in person. I do know about the cow."
            "While our miners are making lots of credits, they don't have very many luxuries to spend them on."
            "We were buying beef and having barbeques almost fortnighly, and everyone really enjoyed them."
            "After the best meat was gone, everyone wanted to continue the tradition. Some of our miners felt that it wasn't a real barbeque without beef."
            "I heard that two of our miners went on a renegade mission to steal the cow."
            "They were able to get the cow into camp, but another miner started arguing with them, trying to explain why they shouldn't kill it."
            "Some of our miners completely understand why we need to save the cows for calving. A few either don't understand or don't care."
            "Someone let the cow go the next day and no one has seen it since."
            "I'm so sorry for our community's loss of the cow. My uncle had a ranch when I was growing up and I know how important each cow is when you're growing a herd."
            "I talked to the men who took the cow and they agreed to give Pete 100 credits each as an apology."
            "That was the end of the message."
            "I told Pete what I found out. He was happy about the credits, but still unhappy that his cow was gone."
            "I don't think he ever found her."
        
        label tell_Pete:
            pavel "I'll explain the situation to Pete. He'd want to know what we found out."
            "Later I heard that Pete went looking for the cow but never found her."
        
        
    #Do the miners resort to stealing? Elect a sherriff?
    #Is there a skewed male:female ratio now that the miners have arrived?  That could cause people to be more suspicious of them.
    return


label community13:
    "I awoke one morning to knocking on my door, and Terra asking me to answer the door."
    lily "[his_name], we must act at once. Zaina told me about an enormous natural cave that the miners are set to run into tomorrow."
    lily "We must explore it! There could be unique flora and fauna. The structures in the cave could help us understand this planet's geology."
    lily "Not to mention that a natural cave could be an exciting destination for family day trips!"
    lily "Although the mile-long descent might be a bit much for young children."
    him "That sounds really interesting, but can we discuss it later? I'd like to get some more sleep."
    if is_liason: 
        lily "I need you to insta-com Earth. If you message them soon, we can get them before working hours are over. Otherwise we need to wait a full fifteen hours."
        him "Alright. What do you need me to ask?"
        lily "Tell them to delay the mining on that branch of the mine until we can fully explore it."
        him "Do they already know about the cave?"
        lily "Have you told them about it? Then no."
        him "Do you know what specific branch it is?"
        lily "Yes, Zaina mentioned it, let me look it up."
        lily "She says it's the third branch off the descent shaft. The one they call little Durban." #Durban is a South African town
        him "Alright. I wrote: 'Please halt mining on little Durban. Natural cave found.'"
        lily "I hope that I can still endure a cave exploration. It has been a long time since I've done any climbing."
        him "I've seen you walking around town. I bet you can handle it."
        lily "I can walk, but crawling around is a completely different thing."
        lily "Aged bodies do not heal as quickly as young ones like yours."
        him "Oh, they already replied. They said to go with whatever Brennan says."
        lily "I can't believe this. Tell them I said to stop the mining!"
        him "I can't send another message for twenty-four more hours."
        lily "Fine. Let's go find Brennan then."
        him "You talk to Brennan. I need to make breakfast."
        lily "I'm afraid that my concerns may be dismissed due to my age and stature."
        lily "Your company would lend my petition credibility."
        him "Okay, I'll go. But I want to be done quickly. I have a lot of work to do today."
        "Not to mention a nap to take this afternoon, if I can manage it."
        "It's still dark outside. As we walk to the mines, Dr. Lily tells me about her latest research."
        "When we arrive, the control station is empty."
        him "Well, we tried, but he's not here. Let's just send him a message."
        lily "I don't want to risk them destroying the cave. Do you know where Brennan sleeps?"
        him "I have no idea."
        "Dr. Lily knocks on the door of a nearby hut. She knocks for several minutes until she gets an answer."
        lily "He said Brennan lives over here."
        "She knocks on his door. A voice comes from behind the door."
        brennan "I am NOT pushing back any deadlines for your personal days, and that's final!"
        lily "We're not here to ask for a personal day."
        "He opens the door."
        brennan "Oh, sorry. I thought you were someone else."
        brennan "Who do I owe for the pleasure of your visit?"
        lily "Zaina. She told me that you are about to mine through an underground cave today or tomorrow."
        lily "I would like to explore the cave. Once you reach the cave, I urge you to delay mining activity in order to allow for data collection."
        brennan "Oh dear. The one in little Durban? We did run into the cave last night just before quitting for the day."
        lily "Is there any way you can delay mining on that branch?"
        brennan "I don't know. What will RET think?"
        him "We asked them, and they said to defer to your judgement."
        lily "I've never had the opportunity to study a cave here before. I believe it would be beneficial for our entire community."
        brennan "The thing is, it's off of the descent tunnel. If it were just a branch it would be fine to leave for a few days or months."
        brennan "But the most promising deposits are still deeper down! Even if I have all of our miners work on branches, their mining won't be as effective as digging deeper and then branching."
        brennan "Zaina made a bunch of frequency tables if you're curious."
        lily "But an opportunity like this is unprecedented. And what we study may impact those frequency tables."
        brennan "More data is good for mining, definitely. How long do you need to explore the caves?"
        lily "How long can you give me?"
        brennan "I can definitely give you 8 hours."
        lily "I need at least two days. Depending on how extensive the cave is, I might need months."
        brennan "I'm willing to give you and Zaina two days. And I want updated frequency tables from Zaina."
        lily "I will inform Zaina. Can you supply us with headlamps and radios?"
        brennan "Yes. You'll need your own rope system and support personelle though."
        lily "I'll go get Zaina now. [his_name], can you be our support person?"
        him "I really need to get back to the farm."
        lily "You can work on your farm. We just need someone to listen to the radio so that we can call for help if something happens."
        him "I can do that."
        "Dr. Lily told me her radio frequency, and I went home to work."
        "I listened to Dr. Lily and Zaina chatting with each other while they explored the cave. Miranda Peron, Dr. Lily's research assistant, came too."
        "She and Zaina took lots of photos, and Zaina took some rock samples." #put in actual conversations? or just summarize it all?
        "They were still exploring when [her_name] came back from work and we listened to it in the background."
        "As I was going to bed, they reported that they were done for the day and made it out safely."
        "The next day, I turned the radio on to find that Lily and Zaina were already exploring the cave again."
        "They breathlessly related how they found a pool of water with eyeless snail-like fish."
        "Dr. Lily reported finding a vertebrate without a shell or exoskeleton, which she said was the first she'd ever seen."
        "She got some video footage, but wasn't able to capture it. She said it looks kind of like a newt."
        lily "[his_name], we need more time to explore this cave. If they mine through this, they might destroy animals that don't exist anywhere else."
        lily "A vertabrate like this without a shell could be invaluable to our research."
        lily "Tell Brennan we can't mine this cave until we explore it further."
        him "Hey, I'm the liason between RET and the colonists, not between the colonists and the miners. Tell him yourself."
        lily "I'm not proficient in presuasive rhetoric. And I don't have strong ties to other colonists through friendships or family."
        lily "Would you please talk to Brennan as a personal favor?"
        menu:
            "Yes.":
                him "Okay. We've come this far."
                him "How would Brennan benefit from stopping the mining? Zaina, do you need more data?"
                zaina "I have about as much as I can use, but I fully support Lily's research."
                lily "Knowing more about our planet benefits everyone."
                him "I'm on my way. Let's talk to Brennan together."
                "I walked over to the camp. We found Brennan reading a book near his hut."
                brennan "How the expedition?"
                zaina "It was fantastic. The cave's beauty is beyond the capacity of verbal description."
                lily "We found a very unusual species that could help us understand life on this planet."
                brennan "Great. I'm glad that no one was hurt and that you could collect some data."
                zaina "I have updated frequency tables for you--small tweaks, mostly."
                brennan "Thank you!" #winning smile
                him "Oh, can I see some of the pictures of the cave? Brennan, do you want to see too?"
                brennan "Sure."
                "Zaina showed us the photos of the cave on her tablet."
                zaina "Unfortunately the newt-thing's habitat and the cave pond are in the mining trajectory."
                zaina "Normally I would have been able to see the water with my imaging tools, but some layers were very resistant to radiation."
                brennan "I see. We'll have to watch out for the water and drain it when we get to that point."
                "Lily looks like she's about to cry."
                him "Maybe you could go around it? Then you wouldn't have to worry about all that water."
                brennan "We're bound to hit the water sooner or later. Might as well get it over with."
                him "Lily really, really wants a few more days to study the cave. Is there any kind of side tunnel you could work on?"
                brennan "That's what we've been doing the last two days. We really need to get back to the main descent tunnel so we can get to the right level for the metals we need."
                him "What would it take to halt the mining for two days?"
                brennan "If you compensated the miners with credits for the days they couldn't work, they would probably be happy. But I would still be two days behind schedule."
                zaina "But if you go ahead with the mining, it might damage your relations with the other colonists, who are very much in favor of research."
                brennan "Look, if you can get the credits together by midnight, I'll tell the miners that they can have paid vacation for the next two days."
                "We hurriedly messaged everyone, and started going door-to-door to explain the situation."
                if (colonists >= 10):
                    #if we implement currency, ask how much to donate
                    "The support was overwhelming. Maybe everyone was just relieved to have something to spend their hard-earned credits on."
                    "We reached the goal by 11:30pm."
                    "Lily and her research assistant, Miranda Peron, gather more samples and photographs of the cave before it is destroyed."
                    "They even managed to capture a few of the newt-like creatures."
                    jump cave_explored
                else:
                    "A lot of people donated a few credits here and there, but it wasn't enough to pay the miners for one day, let alone two."
                    "We gave up around midnight, returning the credits to those who donated."
                    #sit-in protest from Lily and Miranda? Would that make sense?
                
            "No.":
                him "Sorry, I've already talked to Brennan more than I normally would for you."
                him "I'm happy that you were able to explore the cave, but I don't think we can justify asking Brennan for more time when he's already doing you a favor."
                lily "I understand."

    else:
        "Sara asked Rare Earth Tech to halt the mining on Dr. Lily's behalf, but they didn't stop."
        jump cave_unexplored
            
    label cave_unexplored: 
        "The miners end up exploding the cave to access more minerals deeper down. Dr. Lily is furious."
    return
    
    label cave_explored:
        "The miners explode the cave to access more minerals deeper down. At least Dr. Lily got to document the life forms there."
        "Next weekend, some miners are gambling away their new fortunes."
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
    "What do I say?"
    menu:
        "Warn them that they are doomed.":
            $ pass
        "Tell them that I  understand their decision but that am sad to see them go.":
            $ colonists += 1
        "Joke that I wish I could join them.":
            $ pass
    if is_liason:
        "What do I do with Pete and Helen's remaining cattle?"
        menu:
            "Ask Thuc if any of his kids can look after them.":
                $ colonists += 1
            #Thuc doesn't feel as loyal to Rare Earth Tech because they didn't compensate him fairly.
            "Take them for my own farm!":
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
    "Also, I chat about the hardships of living without tech."
    #if the mode of currency stays a choice, how does it play in here?
    "Do I trade with the luddites?"
    menu:
        "yes.":
            $ luddites += 1
            $ trade_with_luddites = True
        "no.":
            $ pass
    return


label community17:
    $ ate_jellyfish = False
    "It's time for the harvest festival! Usually we eat a big meal and the kids go around begging desserts off everyone."
    "This year I'm in charge of inviting guests. Who will I invite?"
    menu:
        "The miners and the luddites." if ((luddites >= 10) and (miners >=10)):
            $ invited_luddites = True
            $ invited_miners = True
            jump ludditesandminers
        "The luddites." if (luddites >= 10): 
            $ invited_luddites = True
            jump justluddites
        "The miners." if (miners >= 10): 
            $ invited_miners = True
            jump justminers
        "The usual--all the other colonists.":
            $ pass
            jump justcolony
            
    label ludditesandminers:
        "Pete offered to host, and slaughtered a bull for the occasion."
        "Almost all the miners came, bringing some bean stew."
        brennan "This beef is amazing. Do you have any extra I could buy from you?"
        pete "You know, credits are not worth that much too me right now."
        pete "We can always use more beans though."
        brennan "Credits are the one thing we have!"
        pete "I don't have a tablet, and I asked RET to delete my name from their records when I left, so I actually have no way of using credits."
        brennan "We've also got lots of rocks?"
        pete "Any metals?"
        brennan "Oh, lots. Next time you want any ore, just come over with a cow and wagon."
        pete "Great. Now I just need to figure out how to make a bellows!"
        "The luddites brought a strange seafood dish."
        jump jellyfishside
        
    label justluddites:
        "Pete offered to host, and slaughtered a bull for the occasion."
        "He also brought a strange side dish."
        jump jellyfishside
        
    label jellyfishside:
        him "So... what is this?"
        pete "Out by the ocean, sometimes you can find these critters with a bunch of spiny arms."
        pete "They start stacking on top of one another and they send off these giant eggs"
        him "Is it safe to eat?"
        pete "As far as I can tell, it is."
        pete "Try some. It's delicious."
        menu:
            "Try it.":
                "It tastes cool and slippery, and a little fishy."
                "It's been so long since you've had anything that tasted unusual."
                "You can't decide if you love it or hate it."
                "But before you know it, you've eaten the whole thing."
                $ ate_jellyfish = True
            "Don't try it.":
                him "I'll pass."
                pete "Suit yourself."
                $ pass
        him "Can you come do a class on cattle health? You're the only expert around." #see community 14 for who got the cattle
        pete "I could, if you can give me a few more tools."
        pete "I can live without most things, but I could use another good knife and some twine."
        him "I think we can arrange for that."
        jump justcolony
        
    label justminers:
        "We invited the miners to join us. After all, their success is what enables us to continue to live here."
        brennan "We didn't have time to go hunting, but we DO have time to soak beans."
        him "Is this a soup or a dip? It smells... different."
        brennan "Neither. Either. Both! Try some."
        menu:
            "Try it.":
                "You dip your bread into the very organic-appearing, thick brown dip."
                "It tastes like beans, with a strange combination of spices."
                "It's not like anything you've ever tasted before. It's exciting to try something new"
                $ pass
                #TODO: set up the variable for here too?
            "Don't try it.":
                him "I'll pass."
                brennan "You don't like beans?"
                him "I'll stick to what I know."
                brennan "How very... predictable of you."
                $ pass
        jump justcolony
        
    label justcolony:
        #which background? this is the end for all the other events as well. maybe don't have the luddites host if it's too complicated, or devise alternate small talk.
        "I set my dish next to the ones from the other families on the buffet table."
        "Everyone helps themselves and sits down--some on tables and some on the ground."
        martin "Is this what all those eggs you were buying from me were for? Is it just an omelet?"
        him "Well, it's kind of like a souffle, but I don't have an electric mixer, or a reliable oven."
        "Martin takes a bite."
        martin "It's not bad. But you should be careful not to mix it too much after you add the flour."
        him "I know..."
        martin "You might have been better off just leaving out the flour completely."
        him "Did you try Thuc's goat curry? Where did he get the spices for that?"
        pavel "We got a bunch of spice seeds in the last crop, and I've been growing them!"
        him "It's been so long since I've had these kinds of spices. It tastes amazing."
        pavel "I'm not a farmer, but Thuc helped me to at least get more seeds from the plants I grew. I gave him some and it's a whole side project for his kids now."
        thuc "Thanks to you my children know the difference between cumin and cardamom!"
        him "Which goat are we eating tonight?"
        thuc "Shorts."
        pavel "That's a weird name for a goat."
        thuc "When the baby goats start eating solid food, we name them after the first non-food thing they try to eat. Our other goats are Shoe, Finger, Stick, and Shirt."
        thuc "Actually, we have a Shirt 1 and a Shirt 2, since that is a popular choice!"
        julia "Oh, and don't forget Cape!"
        julia "Last year Gardenia insisted on wearing this cape she made everywhere."
        julia "She brought it out today to dress up for the begging."
        "After the children finished eating, they ran around with pails of water."
        "After cleaning my plate, they held their hands out expectantly yelling: 'treat for trick!'" #should they LICK the plates clean instead?? too weird?
        "I hand out corn fritters to the children who clean your plate, cup, and utensils."
        "Thuc and I bring out the special treat we made together. It's made with rice and corn and the kids notice it eagerly."
        "They start cleaning the serving dishes and you make a show of inspecting their work and giving them the rice-corn treat."
        "Of course, a few other adults are busy saving leftovers and helping the smallest children clean dishes."
        pavel "It's a shame we don't have any chocolate to give them." 
        julia "I miss it too."
        julia "This is better than Halloween. They're actually helping people instead of running around with entitled threats."
        thuc "They still sound pretty entitled to me!"
        him "Some things never change."
            
    if ate_jellyfish:
        #move to a later, more sparse event?
        "After the dinner, you can't stop thinking about the seafood that Pete brought."
        him "I wonder what they look like." #to self
        "I write an e-mail to Dr. Naomi asking if she has any pictures."
        "She responds via the instant messaging software. Guess she hasn't given up all technology."
        naomi "I don't have a camera capable of taking photos underwater, but here are some photos of the animal out of water."
        naomi "On Earth, jellyfish span various families of creatures, so I think it's safe to call this a kind of jellyfish."
        naomi "The creatures are very popular here and children and adults have been drawing them and incorporating their likeness into jewelry."
        "I feel relief just looking at the photos of the creature out of water and the drawings."
        "I start making my own drawings, and send a few back to Naomi."
        naomi "Did you eat some of this jellyfish at the feast?"
        him "Yes, I did. Are they in season?"
        naomi "I find your interest in them highly unusual."
        him "Why? Aren't they beautiful creatures?"
        naomi "Yes. But when was the last time you took the time to draw an animal?"
        him "..."
        naomi "I suspect that the creature contains a parasite that affects human brains."
        him "And you just let Pete serve it to everyone?"
        naomi "I have a suspicion, but no proof. Their fondness for the jellyfish seems harmless."
        him "Huh. Well let me know if you guys start selling jellyfish sweaters."
        return
    else:
        return
    
    #more likely to take a later risk if you have the parasite? doesn't have to be just like toxoplasmosis.
    # also if you meet with the luddites, Pete can answer questions about cattle health.
    # if BOTH luddites and miners are there, they start trade negotiations? affects the fire grass event later.


label community18:
    "The miners complain that a herd of cattle ran through their camp, making a huge mess and eating their scant herb gardens."
    "Then a farmer complains that a similar thing happened, only the cows ate some young crops."
    "How should I approach the problem? I know it was probably the luddites."
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
    "How do I deal with this problem?"
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
    "Dr. Lily tells me her findings living with the luddites."
    "She tells me more about the vertebrates living in the caves, and the parasite in the thready jellyfish."
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
    "What do I do about it?"
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
    "What do I do?"
    menu:
        #this feels like it escalated really quickly. Talk with both parties before the menu? depending on your relationship.
        "Form a militia with the miners to force the luddites out of the cave.":
            $ miners += 1
        "Not my problem. Do nothing.":
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
    "I hate how it tastes."
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
    "How will I word the query?"
    menu:
        "A miner overworked while pregnant and the fetus died before birth; will she receive compensation?":
            $ miners += 1
        "Please compensate the miner who lost her baby due to overwork.":
            $ miners += 2
        "We're experiencing health setbacks due to overwork. May colonists and miners take paid vacation days?":
            $ colonists += 1
    
    him "That reminds me, RET told me that due to the cost of shipping, they will no longer provide temporary birth control."  # in month 14 of OPS1, Kelly says that there's only enough birth control for 6 more months. I guess we are assuming that more arrived with the shuttle that arrived, but none will be coming on future shuttles?
    him "RET recommends using the rhythm method."
    her "Are they serious? Does that include the miner's families?"
    him "Yes, although children born on Talaam must stay here."
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
    # Using sheep intestines as condoms?  TMI?
    
    return

label community25:
    "Miners have a lot more money than farmers. They start employing young people as servants to do their household chores and look after their children."
    return


# Miranda predicts increased solar flare activity this year; how do you prepare?  Do you believe her?  Do you warn miners/luddites/everyone?
label community26:
    "Miranda predicts increased solar flare activity this year."
    "How do we prepare?"
    menu:
        "Plant more beets.":
            $ colonists += 1
        "Ask Pete for some brewer's yeast" if (luddites >= 10):
            $ colonists += 2
        "Ask Zaina if the miners have found any calcium or magnesium" if (miners >= 10):
            $ colonists += 2
        #these are all "natural" ways to help the body get rid of toxins
    "Will I warn people outside the colony about the solar flares?"
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
    "What do I advise? They aren't even using it anymore."
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
    "He asked me to not let him be a burden on the colony."
    "I schedule a town meeting with the other colonists to decide who the new mayor should be."
    "Also... who is going to take care of Mayor Grayson?"
    #TODO:Go to past if_liason events and have some consultation with the mayor so that it's more clear what the mayor actually does. He makes decisions that will help the colonists the most in the long run.
    "Colonists are divided about if the new mayor should be a farmer with firsthand experience of growing food, or someone more detached from farming."
    "They decide on some basic qualifications and reconvene the next night to decide."
    "The next evening, some miners arrive and ask why they weren't invited?"
    "Their logic is that since they're also RET employees, they should be allowed to nominate a candidate for mayor."
    "There are more miners than colonists; if the miners act together they could control who becomes the mayor."
    "Should I let them join the election?"
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
    "I explain to RET that force isn't necessary" 
    if ((luddites <= 5) and (miners <=5)): 
        "I hear gunshots. The miners are attacking the luddites!?"
    #Lm - you can warn the luddites and some of them take shelter with you
    #lM - you can join the miners in driving away the luddites (do you actually kill them?)
    return

# Rebuilding, aftermath of big fight.
# many of the endings have Terra going back to Earth. Does a shuttle arrive at the last event? Is it taking some of the miners back at the end of their contracts?  
# I think that sounds good.  It's kind of a nice circle and parallel to the first game.  That would make the miners have ~12 year contracts in Earth time.
label community30:
    "The latest shuttles from RET have arrived."
    if ((luddites >= 12) and (miners >=12)): 
        "New miners are arriving to replace the ones who are leaving. I'm kind of sad to see some of them go."
    #TODO: fill in the various endings, figure out what the threshold numbers should be
    return
