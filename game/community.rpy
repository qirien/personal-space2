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
    
# New colonists arrive
label community1:
    $ asked_kids = False
    $ asked_family = False
    $ asked_grow = False
    $ asked_shuttle = False
    $ tell_Kelly = False
    $ tell_Graysons = False
    $ tell_Pete = False
    $ tell_Lily = False
    $ tell_Ngyuens = False
    $ tell_Perons = False
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    "After the introductions, you get in line with your friend Thuc to have some soup."
    scene community_center with fade
    show thuc at midright
    show him normal at center
    show ilian at midleft
    thuc "It's pretty exciting to have some new faces around!"
    him "How's it going? Julia couldn't make it?"
    thuc "No, she was too worn out."
    thuc "Is [her_name] still at work?"
    him "Yeah, she wants to give the new colonists their first physical as soon as possible."
    ilian "I wish I didn't have to be here. After talking to people all day the last thing I want to see is more people."
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
    show him concerned
    him "I understand that from RET's point of view... but we farmers aren't really getting rich out here!"
    him "I hope you weren't planning on a life of luxury."
    kevin "No, I was not. I was planning on a life of adventure and discovery."
    show him normal
    "What kind of life was I planning on?"
    menu:
        "I'm going to focus on fulfilling my job to RET.":
            $ miners += 1
            show him determined
            him "RET went to the trouble of flying me out here, so I might as well fulfill my end of the bargain."
            him "Plus, growing food is essential for our survival!"
            kevin "That sounds like a good plan."
        "I came out here for adventure and discovery too.":
            show him determined
            him "I love the feeling I get when I look up at the sky and I can see thousands of stars."
            him "When I see plants and animals I've never seen before, I feel the thrill of discovery."
            him "I really have to exercise my creativity when I need to find solutions to problems with limited supplies."
            him "Nothing on Earth compares."
            kevin "I agree. There's so much to document and try, it's overwhelming."
            $ luddites += 1
        "At the end of the day, working together is what keeps me going.":
            show him determined
            him "It's amazing to colonize a new planet. There's nothing quite like looking at the sky and realizing how far away we are."
            him "At the same time, it's my relationship with my neighbors that I really cherish."
            him "If we were working together on Earth, I'd be lucky to count one or two of my coworkers among my close friends."
            him "Here, there's no choice. We have to be close to one another to survive."
            him "True, we're always in each other's business. But we're always helping one another too."
            kevin "It's kind of like you're a big family then?"
            him "No, it's different. Families don't always get to choose to be together."
            him "It's more like we're all united by a common goal."
            kevin "So it's like you're always at work."
            him "Kind of, yeah."
            $ colonists += 1
    show him smile
    him "You guys are staying here for the rest of your lives, right?"
    zaina "That's right!"
    label ask_zaina_and_kevin:
    menu: 
        "What should I ask them about?"
        "Are you planning to have children?" if not asked_kids:
            show him normal
            him "So... I know RET is trying to grow the colony..."
            him "Are you planning on having kids?"
            zaina "We'll try. I'm not the most fertile of women though."
            kevin "There aren't that many geologist-engineer couples to choose from."
            $ asked_kids = True
            jump ask_zaina_and_kevin
        "Do you have family still on Earth?" if not asked_family:
            show him normal
            zaina "I was an only child, and my parents recently died, so I don't have any family on Earth. I do have some friends still there though."
            kevin "My father and brother are still on Earth, but I do not regret leaving them."
            menu:
                "So you weren't close?":
                    him "Huh. Don't get along with them?"
                    kevin "They are not men of science. They did not understand my passion for engineering, despite its obvious usefulness."
                    him "My parents are still on Earth. We have some extremely delayed correspondence."
                "You don't like them?":
                    him "I take it you didn't like them very much."
                    kevin "They did not value me or my work. They ignored my accomplishments."
                    him "How would you expect them to? They're probably not experts like you are."
                    kevin "If they had simply not understood my work, that would have been forgiveable."
                    kevin "They are not men of science."
                    him "My parents are still on Earth. We have some extremely delayed correspondence."
            $ asked_family = True
            jump ask_zaina_and_kevin
        "What kind of food will you grow?" if not asked_grow:
            show him normal
            him "You have quite a bit of land out there by the radio tower."
            show him smile
            him "Any idea what you'll grow on it?"
            zaina "We brought some fruit trees, which I hope will make a nice orchard."
            zaina "Grapes are fairly hardy, and I would love to start a winery sometime!"
            kevin "I am planning to try my hand at a basic vegetable garden."
            him "Have you ever farmed before?"
            zaina "I practiced caring for fruit trees in the simulations on the shuttle."
            kevin "I also raised a magnificent patch of vegetables in the simulations."
            show him normal
            him "So the answer is no."
            kevin "The simulations have been updated since you flew over."
            kevin "They're quite lifelike!"
            him "Tell me how you feel about them after you harvest your first crops."
            $ asked_grow = True
            jump ask_zaina_and_kevin
        "How was the shuttle ride?" if not asked_shuttle:
            show him flirt
            him "Did you start to hate each other a little on the shuttle ride over?"
            kevin "No, I do not believe it is possible for us to hate each other."
            zaina "We got married right before the shuttle ride. So it was kind of like our honeymoon!"
            show him smile
            him "I got married right before coming to Talaam too."
            him "Did people give you all kinds of weird survival gear at your wedding?"
            kevin "No, they did not. My friends from work are also engineers and understood the limitations of space travel."
            zaina "His college roommates gave him a custom mix of media! It had everything from the latest datasets to formulae to try."
            show him normal
            him "That sounds interesting. You should show Pete, our librarian. He gets excited about research and data."
            zaina "Some of my cousins gave me some hunting goggles. The battery on them wasn't compatible with RET solar technology though."
            $ asked_shuttle = True
            jump ask_zaina_and_kevin
        "I'm done asking them questions.":
            zaina "You've been here for a year, right? Can you tell me about some of the other colonists?" #not sure if this is necessary... too much exposition?
            show him surprised
            him "I guess I can."
            label colony_gossip:
            show him normal
            menu:
                "Who should I tell them about?"
                "[her_name]" if not tell_Kelly:
                    show him normal
                    him "[her_name] is my wife and she's also the doctor in our clinic."
                    him "She tries to be objective, but she also feels passionate about her job."
                    zaina "I think that describes most of us."
                    show him smile
                    him "Some people have complained that her bedside manner is a little callous."
                    him "So her objectivity is more relevant to customer satisfaction than, say, mine."
                    kevin "Are you implying that your carrots cannot feel your love?"
                    him "Correct. Unless that love manifests itself in better care."
                    $ tell_Kelly = True
                    jump colony_gossip
                "Naomi and Pavel" if not tell_Graysons:
                    show him normal
                    him "If over the course of your lifetime you ever feel hopless or depressed, go talk to Naomi Grayson."
                    him "She can't prescribe medicine for you, but she's very reassuring and can encourage you to get more help."
                    zaina "Reassuring? So she basically tells you to hang in there."
                    him "Somehow when she says it, it feels like she understands what you're going through."
                    show him determined
                    him "If you want to talk to her, she holds religious services every Sunday."
                    zaina "Do you go to those?"
                    him "No, but [her_name] does."
                    him "Naomi's husband, Pavel, is the mayor. I think you know him already."
                    $ tell_Graysons = True
                    jump colony_gossip
                "Dr. Lily" if not tell_Lily:
                    show him normal
                    him "Dr. Lily is our resident scientist. She was here before most of the other colonists."
                    him "She tests plants to see if they're edible, and helps think of solutions to problems."
                    zaina "You said scientist, but what kind of scientist is she?"
                    show him determined
                    him "Hmm. I guess she's a xenonaturalist. She looks at plants and animals, and does some chemistry on the side."
                    kevin "RET does prefer people who have multiple talents."
                    kevin "I'm also a shuttle pilot, for example."
                    show him surprised
                    him "Oh, really? When did you have time to learn that?"
                    kevin "Well, my father was an airline pilot, and I was transfixed upon the idea of flying as a youth."
                    kevin "After I obtained my pilot's license, I worked as a pilot for several years."
                    show him normal
                    him "But at some point you decided to study engineering."
                    kevin "It wasn't enough to simply pilot a craft. I desired to know how they functioned as well."
                    show him smile
                    him "Flying is pretty incredible."
                    $ tell_Lily = True
                    jump colony_gossip
                "Martin and Natalia" if not tell_Perons:
                    show him normal
                    him "Martin and Natalia Peron have four kids. Or, well, they used to have five."
                    zaina "Used to?"
                    show him concerned
                    him "There was an accident... and their daughter died when she was four years old."
                    zaina "What a shame. What happened?"
                    menu:
                        "Pete ran over her with his tractor.":
                            him "Pete was driving his tractor and didn't see her in time..."
                            zaina "How awful. I bet he still feels bad about it."
                            him "The Perons have a vigil every year to remember her."
                            zaina "Are accidents like that common?"
                            show him determined
                            him "No, I mean, usually accidents aren't so bad that someone dies."
                            him "I'm not sure if Natalia will ever forgive Pete."
                        "She got run over by a tractor.":
                            him "She wasn't looking where she was going, and a tractor ran over her."
                            zaina "Was it a self-driving tractor or something?"
                            show him determined
                            him "No, one of my friends was driving it."
                            zaina "Oh, I see. You don't want to tell me who it was before I get to know them."
                            him "Yeah. The Perons are still pretty sad about it and hold a vigil every year where it happened."
                    him "Their kids are getting older and should be able to help around the colony more."
                    $ tell_Perons = True
                    jump colony_gossip
                "Pete and Helen." if not tell_Pete:
                    show him smile
                    him "If you ever need to look something up or make something, our library is the place to go."
                    him "Pete is our librarian and also our cattle rancher."
                    show him normal
                    him "He has a wife, Helen, but I don't see much of her since their ranch is pretty far out."
                    $ tell_Pete = True
                    jump colony_gossip
                "Thuc and Julia." if not tell_Ngyuens:
                    show him smile
                    him "Thuc and Julia are my neighbors and some of our best friends."
                    him "We don't talk about it much, but every now and then he collects everything from the latrines, treats it, and turns it into fertilizer."
                    show him normal
                    him "Also they have ten kids and Julia is a midwife."
                    zaina "Ten kids? That is a lot."
                    show him flirt
                    him "They fill our schoolroom nicely. It must have been a real pain on the shuttle though!"
                    zaina "Yeah, there's not exactly a playground on the shuttle."
                    $ tell_Ngyuens = True
                    jump colony_gossip
                "I'm done talking about other people.":
                    show him normal
                    him "Well, it was nice to meet you both."
                    kevin "Undoubtedly we shall meet again."
                    zaina "We'll have to have you over for dinner sometime."
            
            
    "You continue talking and then head home."
    #TODO: make longer discussion based on menu choice (this is the beginning of the game; we want some really dynamic choices at the start, even if they don't affect a lot)
    # Maybe something about building a park/playground for everyone? 
    return

# 2 - bring whole harvest in to storehouse?
label community2:
    "You've run out of storage space in your cellar, so you take the extras over to the storehouse."
    scene storeroom1
    with dissolve
    show kevin at midleft
    show ilian at midright
    kevin "It is part of our contract that I bring you my whole harvest, even if I will consume all of it."
    ilian "I do appreciate your thoroughness. I hope it wasn't too much trouble to show me your buckets of tomatoes and squash."
    ilian "For things that keep a long time, you don't have to bring them right away."
    show him normal at left
    with moveinright
    show ilian happy at midright
    ilian "Hi [his_name]. Maybe your surplus can make it worth Kevin's while to come out here and he can have more variety in his diet."
    show him happy at left
    him "Sure, do you like spinach?" #to do:is there a way to call a vegetable that has been planted?
    kevin "A variety of foodstuffs is beneficial to anyone's diet."
    ilian "You know, Kevin and Zaina brought me everything that they harvested this week. Apparently that's the way we've supposed to have been doing it all along."
    show him surprised at left
    him "Huh, really? How in the world do you have time to farm?"
    kevin "I can't start my engineering calculations until Zaina finishes her assessment, so farming is a useful pastime."
    show him annoyed at left
    him "It might be an amusing pastime for you, but it's our survival you're talking about here."
    kevin "I must depart, but I will take some of what [his_name] brought, if that's permissible."
    ilian "That's what I'm here for."
    hide kevin
    with moveoutleft
    show ilian normal midright
    show him normal at left
    ilian "We probably should start doing things the way it is in the contract."
    ilian "I know it seems less efficient, but it gives us more control in the case of a famine."
    show him concerned midleft
    with moveinleft
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
    show him annoyed midleft
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

# 3 - Game Night!
label community3:
    scene farm_interior with fade
    show thuc sad at midleft
    show him smile at center
    show pete at midright
    thuc "No. No way! Did you just do that?"
    him "Yes, I did. With the bonuses from my cavalry, my legendary general, and my superior navy from starting on an island, I can conquer Russia in one turn!"
    pete "That's the last time I let you start as Tonga!"
    show thuc normal
    thuc "I think you just won the game."
    him "I don't know, there might be a way for you to make a religious conquest!"
    show thuc sad
    thuc "Nope. I resign."
    pete "Well, that was a good game. I should have situated myself better from the beginning. I got caught up in collecting gold instead of buildin' an army."
    show him normal
    him "Same time next month?"
    show pete happy
    pete "Yes, I reckon so. I'll remind you on the community bulletin."
    show him concerned
    him "Can we call it something other than game night? All the new colonists will think we're a bunch of nerds."
    show pete
    pete "Well, we are a bunch of nerds."
    show him determined
    him "Fine, then they'll believe me when I tell everyone I'm going to an intensive research session with you!"
    show pete happy
    pete "Ha! Fine by me. As long as everyone else calls it that they'll be none the wiser."
    scene fields with fade
    show him normal at midright
    show kevin at midleft
    "A few months later, Kevin asks me about it after I assessed his first batch of crops." #why are you talking to Kevin--expand?
    kevin "I keep seeing people attending 'intensive research sessions' on the colony calendar. What are they?"
    show him concerned
    him "Oh, those. It's just people talking to Pete about stuff."
    kevin "How does he assist in research? Pete isn't equipped to help with fieldwork."
    show him normal
    him "I happen to have some research interests outside of fieldwork."
    kevin "He's a librarian, right? Is your hobby art history or something similar?"
    show him smile
    him "No, it's far more mundane. That's just what we call our monthly game night."
    kevin "I would love to play games with others. Why was this information hidden?"
    show him concerned
    him "I didn't want the new colonists to think I was being frivolous with my time."
    kevin "Face-to-face socialization is highly recommended by RET's psychologists."
    kevin "It may feel frivolous, but it can actually increase your productivity."
    show him normal
    him "But farmers a long time ago didn't have time to play cards. They worked from sunup to sundown without complaining."
    kevin "That's simply what they told their grandchildren. Let me come to your game night!"
    show him smile
    him "Okay, come then! We need someone to shake things up."
    kevin "Shall I invite the other new colonists as well?"
    menu:
        "Sure, invite them all!":
            show him normal
            him "Yes, let's invite them. I can reserve the community center."
            $ colonists += 1
            $ town_hall_games = True
            jump invite_all
        "Don't invite them.":
            show him normal
            him "They can make their own game night if they want."
            him "I want to enjoy myself, not be teaching other people how to play games the whole time."
            $ luddites += 1 #rationale: the luddites are a product of the colonists becoming more fractured
            jump no_invite
        "Ask Pavel to encourage meetups":
            show him normal
            him "I'll ask Pavel, the mayor, to remind them to make socialization a priority."
            $ pass
            jump ask_pavel
        
    label invite_all:
        scene community_center with fade
        show kevin at left
        show thuc at midleft
        show him at center
        show sara at midright

        "Next month, we invited everyone to town hall to game night."
        "Only three or four people showed up, including Kevin, but they were happy to play games with us."
        return
        
    label no_invite:
        scene farm_interior with fade
        show kevin at left
        show thuc at midleft
        show him at center
        show pete at midright
        "I told Kevin that I liked the intimate atmosphere of playing games in someone's house, and we couldn't simply invite everyone."
        "He came to a few game nights but I think he ended up hosting his own with some of the other new colonists."
        return
         
    label ask_pavel:
        scene stars with fade #not sure what scene to show for this ending.
        "I asked Pavel to remind everyone to remember to get to know the new colonists."
        "He sent an annoucement to the community bulletin."
        "I don't know if anyone actually did anything about it, but the thought was there."
        return

# 4 - Community Liaison        
label community4:
    scene community_center with fade
    show pavel at center
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
    show pavel sad #this transition is weird... but is it weirder to keep him in the same pose for so long?
    pavel "I don't want you to ever question my loyalty. We need someone else for this job."
    pavel "The liason will have to understand what RET will want and tell them what's possible and what's not."
    pavel "They'll have to tell us what RET wants and convince us to change if necessary."
    pavel "There may be times when you have to make unpopular decisions, or take the blame for mistakes that weren't yours."
    show pavel
    pavel "I doubt anyone will volunteer for extra work, so we'd like everyone to nominate someone tonight."
    pavel "Then we'll vote on the nominations."
    hide pavel with moveoutright
    show thuc at midright
    show him normal at center
    show lily at midleft
    thuc "Wow, who has time for that extra work?"
    thuc "It's hard enough just raising five goats and ten kids."
    lily "I could take on additional duties, but I anticipate that my personality is not well-suited for liason work."
    show him smile
    him "At least you know your own personality well, although I think that you don't give yourself enough credit."
    show lily angry
    lily "I may occasionally enjoy the company of others, but I would prefer not to negotiate between two parties."
    show him normal
    show lily
    lily "Who do you think would be a good candidate for liasonship?"
    show him determined
    him "Hmm... Naomi seems like someone who could de-escalate conflict well."
    show thuc sad
    thuc "But she's married to Pavel, so she might have a conflict of interest..."
    show him surprised
    him "How so?"
    show thuc
    thuc "Like if she had to choose between the best choice for RET or something Pavel would be happy with, she might choose what Pavel would want for the sake of their marriage."
    show him normal
    him "I don't think she would do that. She can make tough decisions."
    show lily happy
    lily "I believe Thuc has a valid point. We're endeavouring to nominate someone independent from Pavel."
    hide thuc with moveoutright
    show naomi sad at midright
    naomi "Hello everyone, have you thought of someone to nominate?"
    him "I was thinking of nominating you, but Thuc and Lily said that would defeat the point of making the liason separate from Pavel."
    show naomi
    naomi "Pavel and I are in frequent, close contact. Also, I would almost certainly choose to put the colonists's needs first."
    show him smile
    him "Isn't that what we want from a liason?"
    show lily
    lily "What does putting the colonists's needs first mean in this context? Our survival has been RET's main goal with establishing this colony."
    show him normal
    him "RET didn't really explain why we need a liason."
    lily "Regardless, I must choose someone. What do you think of Sara?"
    him "Well, she helped Pavel out with some administrative stuff, so she's familiar with the small beaurocratic work we have."
    show naomi happy
    naomi "Now that Oleg is a little older, she might be up to something like this."
    him "Maybe. Oleg is about the same age as Terra, and she's still quite the handful."
    naomi "What about you? You don't have close ties to Pavel, so we don't have to worry about a conflict of interest there."
    show lily happy
    lily "And based on your relationships with other colonists, your socialization skills are at least average."
    show him surprised
    him "Hang on. I already feel pretty busy just with farming committee meetings, raising Terra, and the farming stuff."
    naomi "We're all busy. Someone has to do this."
    show lily
    lily "This discussion has helped me decide who to nominate. Thank you."
    hide lily with moveoutleft
    hide naomi with moveoutright
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

# 5 - Set aside food for miners?
label community5:
    $ talked_cans = False
    $ talked_credits = False
    $ talked_something = False
    $ talked_canning_dairy = False
    show farm_exterior with fade
    "Zaina and Kevin discovered Indium nearby and have a plan for how to mine it."
    # It will take 4 Earth years for the miners to arrive. About 8 Talaam years.
    # context/scene for this decision? is it a town meeting? you, Ilian, sara, Pavel?
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
            "Have farmers bring in a certain amount of surplus each harvest, and encourage them to grow more food.":
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
    

# 6 - discussion of choice from 5 at game night
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

# 7 - Comparing compensation
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

# 8 - What luxuries should RET send?
label community8:
    $ talked_to_Natalia = False
    $ talked_to_Thuc = False
    $ talked_to_Sara = False
    $ talked_to_Kevin = False
    $ talked_to_Pavel = False
    
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

# 9 - camping with Pete
label community9:
    #where is this? Maybe the river?
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

# 10 - Peron's over for dinner, who should take care of their farm?
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

# 11 - shuttle arrives with miners & Brennan
label community11:
    $ chaco_questions = 0
    #The shuttle should return to Earth with the mined material as soon as it is full.
    "The shuttle is set to arrive today!" #make this a family conversation?
    kid "I wonder what the new people will look like."
    him "Well, they'll look like we do. We're all humans."
    her "Unless aliens have secretly taken over Earth!"
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
    brennan "Thank you for the warm welcome! We're planning on staying here a good twelve Earth years, and some of us for the rest of our lives."
    brennan "In order to facilitate our integration into your community, we've assigned each family a miner or miner family to get to know through weekly dinners."
    brennan "I sent out the assignments already, so try to find each other!"
    "After asking around, I found our miner."
    him "Nice to meet you Chaco."
    menu chaco_coversation_loop:
        "What should I ask him?"
        "How was the shuttle ride?":
            him "How was the trip over?"
            chaco "Fine."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop
        "Was it hard to adjust?":
            him "Did it take a while to adjust to living in such a small space?"
            chaco "No."
            him "I felt so cramped when I came over. Sometimes I just wanted some fresh air so badly, I felt like I would die."
            chaco "They gave us sleeping medicine part of the time."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "Do you have any hobbies?":
            him "What do you like to do in your free time?"
            chaco "Look at the stars."
            him "Well this is a great place for stargazing. We've had to invent a lot of new constellations though."
            chaco "Sounds interesting."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "Do you have a family?":
            him "Is anyone waiting for you back on Earth?"
            chaco "No."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "What is your favorite color?":
            him "What's your favorite color?"
            chaco "Blue."
            him "Light blue or dark blue?"
            chaco "Dark blue."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "What do you like to eat?":
            him "What's your favorite food?"
            chaco "Steak."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "What do you think of Brennan?":
            him "How do you like Brennan?"
            chaco "He talks too much. And he worries too much."
            him "Sounds about right."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "Are you religious?":
            him "Do you believe in God?"
            chaco "Yes."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop            
        "What is your blood type?":
            him "What's your blood type?"
            chaco "O positive."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop
        "How tall are you?":
            him "How tall are you?"
            chaco "172 centimeters."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop
        "If you were stuck on a desert island with all of your coworkers, who would you eat first?":
            him "If you were stuck on a desert island with all of your coworkers, who would you eat first?"
            chaco "Hmmm. Whoever died first."
            him "That's a practical answer."
            chaco "I'm practical."
            $ chaco_questions += 1
            if (chaco_questions >= 4):
                jump twenty_questions
            jump chaco_coversation_loop
            
    label twenty_questions:
        "I feel like we're playing 20 questions here! He's probably overwhelmed from the arrival."
        
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
            "The family had a small funeral and buried him in the colony graveyard."
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
            "The family had a small funeral and buried him in the colony graveyard."
            "Tomás and Joanna Nguyen decide to help out, but they aren't prepared to take full responsibility for the farm."
            "Hopefully they can learn what they need to know from Natalia and their neighbors."
            #TODO: should community 10's decision affect this?
        return

# 12 - missing cow
label community12:
    $ sara_investigates = False
    $ know_BBQ = False
    $ community12_RET_bankrupt = False
    $ talked_bankrupt = False
    if require_whole_harvest or rationing:
        label beef_shortage:
            him "Oh, and I need a pound of ground beef."
            ilian "Unfortunately, we are completely out of beef."
            him "What?"
            ilian "We're completely out of beef."
            him "I heard you, but I didn't believe you. I thought we had plenty of beef."
            ilian "Well, first the miners maxxed out their allotment. So we're completely out of canned beef. Then one of Pete's cows went missing."
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
                    if know_BBQ:
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
                    if know_BBQ:
                        sara "Brennan said that the miners's supervisor, Bandile, is in charge of the celebrations."
                        sara "He recommended messaging him. Can you do that [his_name]?"
                        him "Yes. I want to get to the bottom of this."
                        jump message_Bandile
                    else:
                        him "Where do we go from here?"
                        pavel "Can you tell Pete what we found out?"
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
                "I told Pete that one of the miners stole his cow, and that Bandile sent him 100 credits in apology."
                #pete angry
                pete "They think 100 credits is going to replace her?"
                pete "She could have had about three more calves."
                pete "Least I can do is try to find her."
                "I don't think he ever found her."
                return
            
            label tell_Pete:
                him "Okay, I'll tell him what we know."
                #scene change
                him "Pete, we don't know for sure, but it seems pretty likely that some miners took your cow, but she escaped."
                pete "Yeah, that's about what I thought too."
                pete "Are they going to find her for me?"
                him "No. I don't think they even know which direction she went."
                #pete angry
                pete "I don't believe this. They steal my cow and then expect me to find her?"
                pete "She could have had three more calves. That's a pretty valuable cow to my herd."
                pete "Who do they think they are anyway?"
                him "Sorry, I tried, but I couldn't find anything definitive."
                pete "Least I can do is try to find her."
                "Later I heard he never found her."
                return
    else:
        #rationing is the default for the non-liason option, so non-liasons should not see this event.
        #should there be an option to switch to rationing again before this?
        #in your fields
        "I'm working out in the fields when I see a redheaded figure approaching."
        brennan "You have got some explaining to do."
        him "What do you mean?"
        brennan "I can't get food for my miners from Ilian. He's been stalling me over the last month, and we've eaten all our emergency rations." 
        brennan "Finally Ilian told me that there isn't enough extra food for everyone, because you farmers decided not to plant extra crops."
        brennan "What an idiotic decision. Ilian just said it was someone on the colony planning committee."
        brennan "I looked at the minutes. I know exactly who was behind this. You decided not to save food for us? You think we can hunt and forage?"
        him "There's plenty of food if you know where to look."
        brennan "We don't have time to look for food. We need to spend all our time mining to stay on schedule."
        him "Feeding miners wasn't in our contract."
        brennan "Well, employees are supposed to do what their employers ask them to!"
        brennan "The whole reason you guys are farming is to support the miners, so we can send precious metals back and fund this whole thing."
        brennan "I thought you and the other colonists were pretty happy to be away from Earth."
        him "Why don't you try learning how to hunt and then get angry at me?"
        him "There is so much wildlife here and a lot of it is edible. You already have a few people who work in support capacities, like cooking and cleaning, right?"
        brennan "That's just four people."
        him "Maybe they can do some of the foraging too."
        brennan "Okay. Who's going to teach them what they can eat?"
        him "Dr. Lily can. It's half the reason she's here."
        him "As for hunting, I think that your workers will enjoy a change of pace. It might even make them more productive."
        brennan "I've tasted crabbird though. It's not as good as chicken."
        him "We have some really good recipes. Put enough spices on it and you can hardly tell the difference."
        him "You can start growing some spices and potatoes. We'll start you off and then soon you'll be enjoying the joys of farming!"
        him "Pete can teach you how to hunt."
        brennan "If you have enough time to teach us how to hunt and forage and farm, you would have had enough time to plant a few more crops for us to eat."
        him "We probably could have done that. But I think it's more important that you take care of your own food."
        brennan "Every man a farmer, eh? What a primitive philosophy in our modern age of efficient specialization."
        him "I don't want to be feeding miners in twenty years. I want to be enjoying my own family and community."
        brennan "Over half of us are here for life. So we're part of your little community now."
        him "Here for life? You make it sound like a prison sentence."
        brennan "For some of us, it is."
        brennan "There's a very real chance that RET could go bankrupt because of this."
        menu community12_RET_bankrupt:
            "How would they go bankrupt?" if not talked_bankrupt:
                him "What do you mean?"
                brennan "I can't believe you don't understand this."
                brennan "RET makes money from supplying electronics manufacturers with rare metals."
                brennan "They're scraping by right now doing things like buying and scavenging scrap electronics."
                brennan "They've gone ridiculously into debt to try getting metal off this planet. It's already been almost a decade since they started."
                him "I thought they had some government funding and grants and stuff."
                brennan "They did. They still do. But that doesn't cover most of the expenses."
                brennan "My job is to get that shuttle full of metal and send it back ASAP."
                brennan "That way RET can continue supporting our survival."
                $ talked_bankrupt = True
                jump community12_RET_bankrupt
            "Why is RET going bankrupt so bad?":
                him "So RET goes bankrupt. We can survive without them!"
                brennan "You can be blasé about it now. But you guys depend on them for all kinds of stuff."
                brennan "Your tablets, all your medicine and medical equipment, your solar panels, your batteries."
                brennan "And most crucially, the equipment to detect and broadcast solar flares."
                brennan "Could you really live without all that?"
                menu:
                    "It would be difficult, but we could.":
                        # increase luddite relationship?
                        him "More people would die of preventable causes. But I think that overall we could survive."
                        brennan "Why would you want more people to die instead of fewer?"
                        him "Because then we wouldn't be dependent on some possibly-unethical company for our survival."
                        brennan "Yeah, and you're so ethical, you're willing to die to be independent."
                        brennan "You shouldn't be making that decision for everyone else, too."
                        menu:
                            "True enough.":
                                him "I hadn't thought of it that way. You have a good point."
                                jump community12_choose_farming
                            "I can and will make that decision.":
                                him "I'm not making these decisions on some whim. The colonists elected me to be the liason to RET."
                                him "That means they trust my judgement."
                                him "And I think we should stick to what I decided, which was to have the miners hunt and forage for most of their food."
                                jump community12_choose_foraging
                    "No, we couldn't.":
                        him "We couldn't live without all that technology."
                        him "This isn't like Earth where we've evolved to survive in our environment and have centuries of knowledge to lean on."
                        him "Without our solar flare detection technology, we'd probably all die within a few years or be stuck living in caves."
                        brennan "I'm glad you understand the situation then."
                        him "Yes, I understand."
                        jump community12_choose_farming
            "You're right, RET could go bankrupt.":
                him "I know what I'm doing. I know that RET could go bankrupt and then we'd stop getting supplies from them."
                him "We have enough to survive. By the time our solar panels and radios give out, we'll probably have figured out how to fix them."
                him "Especially with all your mining equipment, it won't be long before we can produce our own crude electronics."
                him "We won't have all of the great medicines and medical equipment like they have on Earth."
                him "More of us would die without RET, but I'm prepared to accept that."
                him "There's also a chance that they won't go bankrupt, or that some other company would take over from them if they did."
                him "I know you don't like it, but I'm sticking to my decision."
                jump community12_choose_foraging
                    
                label community12_choose_farming:
                    brennan "I'm glad you agree. I know that a lot of families have their own food storage."
                    brennan "This is a dire situation, so I'll loan you 500 credits of my landing fee."
                    brennan "Gather up what you can find from the other colonists and hopefully it will be enough to last until the next harvest."
                    brennan "Also, start planting some extra crops for us, otherwise we'll all starve or radiate to death in this forsaken place."
                    him "Okay, I'll do it right away."
                    computer "Dear farmers of Talaam."
                    computer "A few years ago I said that we didn't need to save food to feed the miners."
                    computer "I thought that the miners would have time to hunt and forage and farm in addition to their mining."
                    computer "I was wrong. RET needs the ore quickly to avoid bankruptcy."
                    computer "We need RET to continue to support our colony with batteries and medical supplies."
                    computer "There isn't enough surplus to feed the miners now, at least not in the storehouse."
                    computer "If you can spare some crops for our miners, I can compensate you."
                    computer "We also need several farmers to volunteer to plant fast-growing crops and also regular crops."
                    "Some farmers volunteered to sell extra food, and two or three farmers they'd plant more crops."
                    "After two weeks, we had lots of salad greens and radishes."
                    "But the lettuce and radishes weren't enough to feed the miners."
                    chaco "Thank you so much for dinner tonight."
                    him "You're welcome."
                    chaco "Could you sell me some of your crops?"
                    chaco "I can give you plenty of credits for them."#make this a decision if we have food/money variables
                    him "We don't have a lot of extra food right now, but we can spare a little."
                    chaco "This is great. I'm so sick of radish salad."
                    him "You know, if you have the credits, I bet Pete could do some hunting for you."
                    chaco "Huh. I'll ask."
                    "Pete went on a quick hunting trip. He had to make several trips back to the hunting site to carry back all the carcasses."
                    "Dr. Lily took a few people out foraging."
                    "The miners lived off the meat and foraged food for almost a month."
                    "After eight weeks, we had zucchini, squash, and turnips, with some small potatoes and bigger ones on the way."
                    return
                    
                label community12_choose_foraging:
                    brennan "Fine. I'll go door-to-door tonight to see if I can buy off some food until you can send over your teachers."
                    him "They'll be there tomorrow morning."
                    computer "Hello Lily and Pete."
                    computer "We don't have that much food for the miners, so they need to learn how hunt and forage."
                    computer "Can you, Lily, teach them to forage, and Pete, can you teach them how to hunt?"
                    computer "They want to start ASAP."
                    computer "How does tomorrow morning sound?"
                    "Pete agreed to meet the next day, and Dr. Lily the day after."
                    #near the mining camp or outside
                    pete "I know on Earth that hunting is this thing rich people do."
                    pete "Here it's a matter of survival. There's no caddy who's going to show you where to stand and when to shoot."
                    pete "I'll start by describing some of the nearby game."
                    pete "We'll set up some of our big traps and make some snares."
                    pete "Then I'll show you some of my favorite hunting spots, and we'll do basic target practice."
                    pete "I hope you spent some time on the hunting sims because they do teach you how to aim quickly."
                    pete "You guys won't be hunting with guns, since we want to save ammo."
                    pete "But if we can't shoot anything with crossbows today, I'll shoot something so you guys can eat."
                    "There were cheers at the mention of meat."
                    pete "I'll come back next week and we can talk about fishing, too."
                    "I checked back in with them that evening, and they were roasting a whole grass crab."
                    "They were processing a few crabirds too."
                    "The next day, Dr. Lily started her instruction."
                    "Around 20 people showed up for the class."
                    lily "There are at least 20 edible plants on this planet."
                    lily "We haven't studied their effects on the diet long-term, but Earth animal studies are promising."
                    lily "Of those 20 edible plants, six are commonly used in cooking."
                    "One of the miners asked what was wrong with the other fourteen."
                    lily "Some taste very bitter, or have a very strong taste that we haven't found a use for. Others are easy to confuse with lethal plants, or have strange side effects."
                    lily "I've sent you all the most detailed maps we have of foraging locations."
                    lily "I've also made simplified versions based on the current season."
                    lily "It's likely that you will exhaust these locations. Please mark other good foraging locations you find on the map so you can find them again later."
                    lily "The sidebar shows detailed leaf, flower, and root images, but the best way to learn is to practice finding it in the wild."
                    lily "There's a good location about a half mile away. I'll show you some other common plants on the way."
                    "While they hiked around that afternoon, I tilled up some ground near the miners's quarters."
                    him "These seeds don't need to be very deep. One of you can use this stick to make a small hole in the ground, and another person can follow and plant seeds in the holes."
                    "We planted some crops that could be harvested quickly, like green lettuce and radishes."
                    "The next day, I helped set up a rudimentary irrigation system and we planted more long-term crops."
                    "I asked Chaco about how things were going at our weekly dinner."
                    chaco "The meat isn't bad."
                    chaco "I miss bread."
                    him "Do you like hunting?"
                    chaco "We buy our meat from Pete."
                    him "You're not going hunting?"
                    #chaco looks uncomfortable
                    chaco "No. Brennan said we don't have time."
                    him "Okay, so Pete is selling meat on the side."
                    him "What about your farm?"
                    chaco "We paid some other farmers to come take care of it."
                    chaco "Brennan said it would be easier and quicker for us to focus on mining."
                    chaco "He said that we're probably going to be stuck here unless we work hard."
                    him "Yes, he does say that."
                    chaco "Is it true?"
                    him "It's true that I decided to let you be in charge of your own food."
                    him "I was hoping that being connected to your food would help you feel alive."
                    chaco "Eating food definitely helps."
                    "Other colonists told me how they were helping the miners by doing extra work on the side." 
                    "Some of the teenagers from the colony had a great time foraging on the weekends, selling their finds to the miners, and spending their money on the weird crafts they made for each other."
                    "The prices of food from the storehouse started to rise, but we sold crops at a higher price too."
                    "After eight more weeks, the new farm in the miner's camp had some more substantial crops."
                    "They miners seemed pretty happy to eat their carrots and potatoes, and soon the prices of crops started to stabilize."
                    return 

label community13:
    $ cave_partially_explored = False
    $ Lily_mad_at_RET = False
    "I awoke one morning to knocking on my door, and [kid_name] asking me to answer the door."
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
        lily "She says it's the third branch off the descent shaft. The one they call Little Durban." #Durban is a South African town
        him "Alright. I wrote: 'Please halt mining on Little Durban. Natural cave found.'"
        lily "I hope that I can still endure a cave exploration. It has been a long time since I've done any climbing."
        him "I've seen you walking around town. I bet you can handle it."
        lily "I can walk, but I'm unsure of my crawling competence."
        lily "Aged bodies do not heal as quickly as young ones like yours."
        him "Oh, they already replied. They said to go with whatever Brennan says."
        lily "I can't believe this. Tell them I said to stop the mining!"
        him "I can't send another message for twenty-four more hours."
        lily "Then we must inquire with the next person who can give us permission to explore the cave."
        him "Ugh, Are you talking about Brennan?"
        jump community13_talk_to_brennan
    else: 
        jump community13_nonliason_talk_to_brennan
        
        label community13_nonliason_talk_to_brennan:
            lily "No, this is urgent and important business. Depending on their schedule, they may already be setting up the explosives!"
            lily "I need you to ask Brennan if he can delay mining the cave until we can explore it."
            jump community13_talk_to_brennan
        
        label community13_talk_to_brennan:
            him "You talk to Brennan. I need to make breakfast."
            lily "I'm afraid that my concerns may be dismissed due to my age and stature."
            lily "Your company would lend my petition credibility."
            him "Okay, I'll go. But I want to be done quickly. I have a lot of work to do today."
            him "Not to mention a nap to take this afternoon, if I can manage it."
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
            brennan "The one in little Durban? We did run into the cave last night just before quitting for the day."
            lily "Is there any way you can delay mining on that branch?"
            if require_whole_harvest or rationing:
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
                brennan "Yes. You'll need your own rope system and support personnel though."
                lily "I'll go get Zaina now. [his_name], can you be our support person?"
                him "I really need to get back to the farm."
                lily "You can work on your farm. We just need someone to listen to the radio so that we can call for help if something happens."
                him "I can do that."
                "Dr. Lily told me her radio frequency, and I went home to work."
                "I listened to Dr. Lily and Zaina chatting with each other while they explored the cave. Miranda Peron, Dr. Lily's research assistant, came too."
                "She and Zaina took lots of photos, and Zaina took some rock samples." #put in actual conversations? or just summarize it all?
                # TODO: actual conversations are more interesting
                "They were still exploring when [her_name] came back from work and we listened to it in the background."
                "As I was going to bed, they reported that they were done for the day and made it out safely."
                "The next day, I turned the radio on to find that Lily and Zaina were already exploring the cave again."
                "They breathlessly related how they found a pool of water with eyeless snail-like fish."
                "Dr. Lily reported finding a vertebrate without a shell or exoskeleton, which she said was the first of its kind she'd ever seen."
                "She got some video footage, but wasn't able to capture it. She said it looks kind of like a newt."
                lily "[his_name], we need more time to explore this cave. If they mine through this, they might destroy animals that don't exist anywhere else."
                lily "A vertabrate like this without a shell could be invaluable to our research."
                lily "Tell Brennan we can't mine this cave until we explore it further."
                if is_liason:
                    him "Hey, I'm the liason between RET and the colonists, not between the colonists and the miners. Tell him yourself."
                else:
                    him "I'm no research lobbyiest. Tell him yourself."
                lily "I'm not proficient in presuasive rhetoric. And I don't have strong ties to other colonists through friendships or family."
                lily "Brennan worked with your wife. He would be more likely to listen to you since he knows you."
                lily "Would you please talk to Brennan as a personal favor?"
                menu:
                    "Yes.":
                        him "Okay. We've come this far."
                        him "How would Brennan benefit from stopping the mining? Zaina, do you need more data?"
                        zaina "I have about as much as I can use, but I fully support Lily's research."
                        lily "Knowing more about our planet benefits everyone."
                        him "I'm on my way. Let's talk to Brennan together."
                        "I walked over to the camp. We found Brennan reading a book near his hut."
                        brennan "How's the expedition?"
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
                        # Lily looks really upset
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
                            "Pete was especially supportive."
                            "We reached the goal by 11:30pm."
                            "Lily and her research assistant, Miranda Peron, gathered more samples and photographs of the cave before it was destroyed."
                            "They even managed to capture a few of the newt-like creatures."
                            jump cave_explored
                        else:
                            "Pete donated a lot of credits, and there were a few small donations, but it wasn't enough to pay the miners for one day, let alone two."
                            "We gave up around midnight, returning the credits to those who donated."
                            $ cave_partially_explored = True
                            jump cave_unexplored
                            #sit-in protest from Lily and Miranda? Would that make sense?
                        
                    "No.":
                        him "Sorry, I've already talked to Brennan more than I normally would for you."
                        him "I'm happy that you were able to explore the cave, but I don't think we can justify asking Brennan for more time when he's already doing you a favor."
                        lily "I understand. Perhaps Pete will be able to assist me in your stead."
                        "She and Pete made an impassioned plea, but they were not successful."
                        $ cave_partially_explored = True
                        jump cave_unexplored
            else:
                brennan "ABSOLUTELY not."
                brennan "We're far enough behind as it is."
                lily "But demolishing this cave is irreversible."
                lily "There may be flora and fauna unique to the cave that we may never document if you destroy it unexplored."
                brennan "RET going out of business would also be irreversible, which might happen if I don't continue mining right away, thanks to this guy."
                him "At least you have enough to eat, and it's food you grew or found yourself."
                brennan "You imposed your values on how we get our food. I'm imposing my values on when we can spare time to scientific research."
                lily "You are making a mistake."
                him "We're already behind schedule. What difference would a few days make?"
                brennan "I said no. Please leave."
                "Dr. Lily looked furious, but she left."
                jump cave_unexplored
            
    label cave_unexplored:
        "That night, she sent a message to the other colonists about how Brennan refused to let her explore the cave."
        "She invited everyone to join her in a protest the next morning."
        "The next day, Pete, Helen, Natalia, and Joanna joined her."
        "I went too."
        menu:
            "I protested with them.":
                "I marched around yelling."
                him "RET just wants moNEY!"
                pete "Save our cave! Save our cave!"
                lily "Conserve Talaam! Don't end up wrong!"
                "It felt cathartic to express my outrage."
                $ colonists += 1
            "I just wanted to see what would happen.":
                "I watched as the protestors matched in a circle, chanting and yelling."
                "It seemed pretty silly to me. Didn't we have better things to be doing?"
                $ miners += 1
        brennan "Hey, I get that you're upset. you guys should move away from this area. There could be particles in the air that aren't good to breathe." #tried to google this but I'm still not sure if this would happen
        # That's OK, BSing is in-character for him.
        lily "We're not budging an inch!" 
        if cave_partially_explored:
            lily "The cave newts cannot leave! We will endure this pollution in their honor."
        brennan "It's your funeral."
        "A few minutes later, we heard and felt the blasts."
        "Dr. Lily left without saying anything."
        "The next day I saw Dr. Lily to get some test results for my soil."
        him "How's my soil doing?"
        her "Phosphorus levels are low. I recommend that you increase manure levels."
        him "I'll see if I can work some more in."
        menu:
            "Say something about the cave":
                menu:
                    "Too bad they had to demolish that cave.":
                        him "I wish there had been some other way for the mining to continue."
                        if cave_partially_explored:
                            lily "It was indeed disappointing to simply catch a glimpse of what we could have observed."
                        else:
                            lily "I feel incredulous that Brennan decided to throw away this research opportunity."
                        lily "I cannot affect circumstances further, however."
                    "At least you got to see some of the cave." if cave_partially_explored:
                        him "At least you were able to partially explore the cave."
                        lily "I know that I could have gathered more data. I am unable to forget that."
                        lily "What if those cave newts contain the secret to unshelled vertebrate survival?"
                        lily "We may never know."
                    "Brennan is just worried." if (not cave_partially_explored):
                        him "I know it seems like Brennan was being a jerk, but he's just worried about RET's survival."
                        lily "I understand his arguments. I think research is more important to our survival than having a shuttle shipment leave on time."
            "Don't say anything.":
                "I didn't say anything about the cave."
        $ Lily_mad_at_RET = True
    return
    
    label cave_explored:
        "I saw Dr. Lily the day after the miners demolished the cave to get the tests back from my soil samples."
        him "So this soil is fine?"
        lily "Nothing unusual. Phosphorus levels are low, so add more manure next time."
        him "Okay, I'll work in some extra."
        him "Are these the little cave newts you rescued?"
        lily "Yes! They seem to be thriving in captivity."
        lily "They have an interesting secretion that I think helps insulate them against cold temperatures in the cave."
        him "Cool. It's a shame they had to excavate right where the cave was."
        lily "Yes, it was. We did everything we could."
    # Pete should be a vocal opponent of the mining to foreshadow next month.
    # Perhaps something tragic, like someone decides to do a sit-in to protest the mining, but the miners don't know about it, and they get blown up as the excavation continues?
    return

# 14 - Pete leaves
label community14:
    "Brennan and the miners had mined enough rare metal to fill the shuttle they arrived in."
    "Today they're sending it back to Earth so RET can sell it."
    "Everyone gathered to watch the shuttle go off."
    thuc "So one of your pilots here can control it remotely?"
    brennan "Yes, I don't know the details, but it just needs to get into orbit around Talaam. When it's at the right place and speed to get to Earth, the pilot will make adjustments for it to leave orbit."
    thuc "When you flew back, the pilot was in the shuttle though."
    brennan "Yes, he was. The main advantage to piloting from inside the shuttle is that you can change things based on how it feels."
    brennan "Since we're just sending back metal, feeling the pain of excessive g-forces isn't a problem our pilots need to worry about."
    brennan "Their acceleration should be a good metric for that anyway."
    "The pilot was broadcasting the launch on the radio." # maybe this could be Kevin? man of many talents
    "We listened as he counted down, and watched the shuttle as it started consuming fuel to power its flight."
    "Soon the shuttle was just a twinkle in the sky, and it disappeared."
    "The pilot continued his narration. About seven minutes later he said that we'd reached orbit."
    pete "Before y'all go, I have an announcement to make."
    pete "Helen and Travis and me are moving."
    pavel "Is there something wrong with your house?"
    pete "Nothing wrong with the ranch."
    pete "We're tired of working for RET. We want to try to make it on our own."
    pete "Part of the reason I came here was to live off the land."
    pete "'Cept now RET is making all sorts of demands of us. Wants us to sell our food for money so we can buy other people's food, or things we don't really need." #not sure if this makes sense
    pete "They haven't treated us fairly."
    if require_whole_harvest or rationing:
        pete "The miners don't respect my property. They stole one of my cows and never returned her."
    else:
        pete "They expect us to feed the miners, but we can barely feed ourselves."
    pete "They don't respect the natural beauty of Talaam, and they destroyed a cave in the course of their mining."
    if Lily_mad_at_RET:
        lily "They don't respect the needs of researchers either."
        lily "I came here to study this planet, not destroy it."
        lily "I'm going with Pete and his family."
        $ luddites += 1
    else:
        pass
    if not (asked_only_medicine): 
        pete "They don't even care about us enough to send the right medicines."
        "Tomás Peron and Joanna Nguyen tell us their plans to go with Pete and his family."
        $ luddites += 1
    else:
        pass #not sure if I need these else pass things
    pete "I know what my contract says. Basically everything I own belongs to RET unless I made it with my own hands."
    pete "But that was before we had credits."
    pete "We're leaving our house and everything in it. Maybe some newlywed couple will want to live there."
    pete "I will be taking my radio and some metal foam sheeting, which I paid for with some of the credits I own."
    #how does pete plan to deal with credits? he probably has a good amount
    pete "I'll leave the same amount of cattle the ranch started with, plus some, and take a herd with me."
    "Everyone starts talking when Pete sits down."
    "Some families are telling Pete and his family goodbye, while others leave awkwardly."
    "I push through the crowd to tell Pete some parting words."
    "What do I say?"
    menu:
        "Warn them that they are doomed.":
            him "Don't leave! You'll die out there!"
            pete "I've camped out for days on hunting trips. It's not that much more dangerous than living here."
            him "But what if you get hurt or develop skin cancer?"
            pete "We'll figure it out. Seems like half the things [her_name] deals with would heal on their own."
            him "This is your family you're experimenting with."
            pete "I know. I don't like our present condition, so I'm changing it."
            $ pass
        "Tell them that I understand their decision.":
            him "I'm sad to see you go, Pete."
            him "I understand why you're leaving, but I'll miss you guys."
            pete "I'm sure we'll see each other every now and then."
            him "I'd tell you to take pictures, but I guess you won't have your tablet with you."
            pete "I'll see if I can train crabirds to send messages."
            $ colonists += 1
        "Joke that I wish I could join them.":
            him "I wish I could join you, but my crops aren't nearly as portable as your cattle!"
            him "Seriously though, take care of yourselves."
            $ luddites += 1
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
    "In the early morning, [her_name]'s radio went off." #TODO: should we make a special kind of "radio" textbox like with e-mails?
    # in OPS 1 I just had the characters name be "X on the radio", but perhaps italics or something would make the difference more obvious, too?
    pavel "[her_name], I think you should come over here."
    pavel "Naomi is really sick."
    her "What are her symptoms?"
    "[her_name] continued talking on the radio as she put on her boots and coat and took my tractor down the road."
    "I fell back asleep and woke up an hour later and started making breakfast"
    her "Hi, I'm back."
    him "Is she...?"
    her "It's... pretty bad."
    him "Oh. What's wrong with her?"
    her "It's confidential. Pavel said he was going to send out an announcement. What did he say?"
    "I checked my tablet."
    him "He said that she has severe radiation sickness and that she is going to die in the next week or two."
    her "We'll be doing pallative care." 
    him "Just trying to make her suffer less?"
    her "Yeah. I told Pavel to post that everyone should try to give her a last visit, although her symptoms are a lot like severe food poisoning."
    him "I'll bring the kids over this afternoon."
    her "Just... check that she's in a condition to see them."
    "After I picked the kids up from school, we walked to Naomi and Pavel's house."
    "Pavel was outside."
    pavel "Are you here to see Naomi?"
    him "Yes. Is that alright? I don't want to add to her suffering..."
    pavel "It's fine. Now is a good time. Sara is in there right now, so you can go in when she comes out."
    him "Okay. This feels so sudden. Is everything going to be okay?"
    pavel "I am very sad that Naomi is not going to live longer."
    pavel "We all have to die at some point though. Naomi has been ministering to her neighbors and their children, which was what she was passionate about."
    pavel "She likes to say that even though we don't have modern plumbing, we can be civilized by loving each other."
    "Sara stepped out. Tears were streaming down her face."
    "Should I do or say something?"
    menu:
        #this menu might give players a false sense that you have a relationship meter with Sara
        "Pur your arm around her shoulder.":
            "I put my arm around her shoulder."
            sara "It's hard to see her like this. But I'm glad I said goodbye."
            $ colonists += 2
        "Say you're sorry.":
            him "I'm sorry for your loss."
            sara "It's our loss, not just mine."
            $ colonists += 1
        "Say nothing.":
            "Sara walked away quietly sniffing."
            pass
    "I entered the room with the kids."
    kid "It stinks in here."
    him "Sometimes that happens when you're sick."
    naomi "[his_name], did you come to say goodbye too?"
    him "Yeah. Thanks for everything you've done for us." #more detail
    kid "Are you dying?"
    naomi "Yes, I'm dying. When I'm gone, you'll have to help the other kids to be nice to each other, okay?"
    naomi "[his_name], I've been watching how you parent your children."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        naomi "I think you are doing a really good job. It's hard to be patient and not blow up at your kids sometimes."
        naomi "Keep up the good work."
    elif(style == "authoritarian"):
        naomi "I think you're too harsh with your children sometimes. It's true that you make the rules in your home, but you can also decide when to change them or bend them."
        naomi "If you consider Terra's opinion sometimes, I think she will be happier."
    elif(style == "permissive"):
        naomi "You let Terra do her own thing a lot."
        naomi "That can be good sometimes, but children need boundaries, otherwise they won't respect society's rules."
    else:
        naomi "Please don't ignore your children. If you neglect them now, they won't have a relationship with you when they're adults."
        naomi "If you don't like being with your children, what was the point of having them?"
        naomi "You might as well make a lifelong friend who might take care of you when you're old like me."
    #would love some input/edits on this part
    him "Oh, uh, thanks for the advice."
    kid "What happens after you die?"
    naomi "Some people believe that we go to a different world. Some people believe that we come back in another life."
    naomi "Some people believe that our existence ends with death."
    naomi "No matter what happens, I'll be alive in your memories of me."
    kid "I'll forget."
    naomi "Dying is a natural part of life. Your crops don't stay alive forever, do they?"
    kid "We have a tree that's been growing since I was a baby!"
    naomi "Can you plant a tree for me when I die?"
    kid "Yes."
    naomi "You can plant it on my grave, and then you can think about how my body is becoming a tree."
    kid "Gross."
    naomi "And let [bro_name] help." 
    naomi "Come give me a hug."
    "[kid_name] and [bro_name] gave her a hug."
    him "We'll be sure to plant that tree, Naomi. Thank you for letting us visit even though you're sick."
    naomi "It's my pleasure. On your way out, tell Pavel that I'm going to take a break."
    him "I'll tell him."
    "We left, and I told Pavel that Naomi wanted a break."
    pavel "Seriously, thank you for coming by."
    him "Let us know if you need anything."
    pavel "I will."
    "About a week later, Pavel called [her_name] to tell her that Naomi was dead."
    her "I'll take her body today and do a few tests, and we can hold the funeral tonight."
    "She turned the radio off."
    "[her_name] started crying."
    her "It won't be the same without her."
    her "Who will reassure us when we're feeling hopeless?"
    her "Who will give me hope that there's something bigger out there?"
    menu:
        "It'll be okay.":
            him "I'm sure someone will fill the gap."
            her "It's not like you ever liked going to church."
            #another menu choice here
            him "Yeah, but I know she cared about us."
            him "Sometimes she'd stop by our house just to see how we were doing."
            her "I guess that was part of her ministry."
            him "She understood that some of us don't care for organized religion."
            him "She knew that it was about caring for other people."
        "No one can replace her.":
            him "She's irreplaceable. We all are, since we're unique human beings."
            him "But I think other people can inspire us, even if they can't do it the way Naomi did."
            her "I know. But she's just so good at it."
            him "That's true. She could have been just a preacher, but she filled in the gaps."
            him "She watched our children and took care of sick people."
            her "Hey, I make house calls too!"
            her "But I know what you mean. She took care of their spirits, not their bodies."
            #this decision only affects dialogue right now.
    her "Oh, darn. Who's going to talk at her funeral?"
    him "Sarah's pretty religious, and I know she's worked with Pavel. She probably knows Naomi pretty well. I mean knew."
    her "Sounds good. Can you ask her for me?"
    him "Has Naomi's death been announced?"
    her "Pavel just posted about it."
    him "I'll ask Sara if she can speak at the funeral then."
    "The kids had been playing, but were listening to our conversation." #actual conversation w/kid?
    "Almost everyone came to the funeral that evening."
    #background - multipurpose room or chapel
    her "I hope Naomi felt at peace when she died."
    her "Even though she was miserable, she stayed cheerful and optimistic until the very end."
    pavel "Naomi died of severe radiation sickness. I don't know if it was preventable or not."
    pavel "There were many times where she felt it was more important to attend to the needs of people in our community rather than take shelter from solar radiation."
    pavel "She constantly sacrificed her own needs to fulfill those of others, perhaps to an unreasonable degree. May her work live on in the way we treat each other." #you could have him say different things based on the community variable
    sara "Sister Naomi was my mentor and friend. After I had Oleg, I had pretty bad depression for the first year after he was born."
    sara "Sister Naomi visited me every day until I felt normal again. When I felt like it would have been better for me to die and have someone else watch Oleg, she helped me get out of the house to seek treatment." #depression meds available?
    sara "I know I'm not the only one she's helped this way. I'm sure each of you have a story about how Sister Naomi helped you feel like you were a necessary part of our community."
    sara "Now that she's gone, I admit that I feel a little helpless."
    sara "But I decided to learn from Sister Naomi."
    sara "She had a story she used to tell about how she was scared of spiders for a long time."
    sara "You kids might not understand, but spiders are an Earth bug that many people find revolting and terrifying."
    sara "One time she was alone in her house and there was a giant spider in her shower."
    sara "She knew that she could kill it with her shampoo bottle. But instead of killing the spider, she decided to touch it."
    sara "She held it in her hands and looked into its eyes. She said that she could feel that the spider was terrified and curious."
    sara "I'm not sure if I believe this part, but she said they held eye contact for five minutes."
    sara "Then she put it outside. And she wasn't afraid of spiders anymore."
    sara "So instead of hoping that my hopelessness will go away, I am staring it in the face."
    sara "Which is why I will be continuing her tradition of having weekly interfaith discussion groups."
    sara "I may not be as wise or inspiring as Sister Naomi. But I am organized and consistent. So please come and share your life wisdom and experience."
    "Some of the children sang one of the songs Naomi taught them when they were young." #does Brennan do anything? What about the miners? Kevin or Zaina?
    "We all helped to bury her body. Ilian provided a laser-engraved headstone, and the Nguyen children put wildflowers on her grave."
    "[kid_name] and [bro_name] planted the saplings we brought."
    
    #back home
    him "So... How often was Naomi out in the radiation to get severe radiation sickness?"
    her "She was outside during an entire solar flare multiple times."
    her "She didn't say why, but I think she was checking up on Pete and Helen."
    him "So she probably knew there was a flare, but couldn't find shelter in time?" 
    her "That seems likely."
    him "Too bad she wasn't inspired to take a tent with her."
    her "She probably felt that she didn't have time, or maybe someone else had checked them out."
    her "I wish we had something more practical like a radiation umbrella."
    
    # Dr. Lily has a stroke and worries about her progress being lost if she should die.
    # should this go in the next event? what happens if she left with the luddites?
#    "About a month later, Dr. Lily had a stroke."
#    "She announced that Miranda would be the new head scientist."
#    "Miranda had been working with Dr. Lily for the last ten years or so."
    # Miranda Peron (now about age 26) steps up to take Dr. Lily's spot. She had been studying with Dr. Lily before."
    return


label community16:
    "Trade with luddites: is it permitted in the contract?"
    "Luddites want to trade a few calves for medical supplies." # [her_name] is not supposed to treat them at the clinic, but she does anyway?
    "Also, I chat about the hardships of living without tech."
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
        brennan "Credits are the only thing we have!"
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
        # Have some kind of bonfire background?
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
        "I write an e-mail to Dr. Lily asking if she has any pictures."
        "She responds via the instant messaging software. Guess she hasn't given up all technology."
        lily "I don't have a camera capable of taking photos underwater, but here are some photos of the animal out of water."
        lily "On Earth, jellyfish span various families of creatures, so I think it's safe to call this a kind of jellyfish."
        lily "The creatures are very popular here and children and adults have been drawing them and incorporating their likeness into jewelry."
        "I feel relief just looking at the photos of the creature out of water and the drawings."
        "I start making my own drawings, and send a few back to Lily."
        lily "Did you eat some of this jellyfish at the feast?"
        him "Yes, I did. Are they in season?"
        lily "I find your interest in them highly unusual."
        him "Why? Aren't they beautiful creatures?"
        lily "Yes. But when was the last time you took the time to draw an animal?"
        him "..."
        lily "I suspect that the creature contains a parasite that affects human brains."
        him "And you just let Pete serve it to everyone?"
        lily "I have a suspicion, but no proof. Their fondness for the jellyfish seems harmless."
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
