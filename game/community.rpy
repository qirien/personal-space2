﻿## Community Events

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
    scene community_center with fade
    show thuc at midright
    show him normal at center
    show ilian happy at midleft
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    "After the introductions, I got in line with my friend Thuc to have some soup."
    thuc "It's pretty exciting to have some new faces around!"
    show him surprised
    him "How's it going? Julia couldn't make it?"
    show thuc sad
    thuc "No, she was too worn out."
    show thuc normal
    thuc "Is [her_name] still at work?"
    show him concerned
    him "Yeah, she wants to give the new colonists their first physical as soon as possible."
    show ilian
    ilian "I wish I didn't have to be here. After talking to people all day the last thing I want to see is more people."
    show him happy
    him "At least there's free soup."
    ilian "It's not free, it came from all those crops you paid to the storehouse! So if any of you gave subpar stuff, we're going to taste it."
    "You get your soup and sit with some of the new colonists."
    scene community_center with fade
    show him normal at midleft
    show zaina at center
    show kevin at midright
    him "Hi, I'm [his_name]."
    zaina "I'm Zaina, and this is my husband Kevin. I'd let him speak for himself but his mouth is full, so I'm socially obligated to be polite in his place."
    show him determined
    him "Nice to meet you, Zaina and Kevin. Where will you be living?"
    zaina "We've set up a house out by the radio tower. It's closer to the mountains where I'll be working."
    kevin "And after Zaina figures out where the goods are, I'm in charge of figuring out if it's even possible for us to mine."
    show him surprised
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
            show him happy
            him "Plus, growing food is essential for our survival!"
            kevin "That sounds like a good plan."
        "I came out here for adventure and discovery too.":
            show him determined
            him "I love the feeling I get when I look up at the sky and I can see thousands of stars."
            him "When I see plants and animals I've never seen before, I feel the thrill of discovery."
            show him normal
            him "I really have to exercise my creativity when I need to find solutions to problems with limited supplies."
            him "Nothing on Earth compares."
            kevin "I agree. There's so much to document and try, it's overwhelming."
            $ luddites += 1
        "At the end of the day, working together is what keeps me going.":
            show him determined
            him "It's amazing to colonize a new planet. There's nothing quite like looking at the sky and realizing how far away we are."
            him "At the same time, it's my relationship with my neighbors that I really cherish."
            him "If we were working together on Earth, I'd be lucky to count one or two of my coworkers among my close friends."
            show him normal
            him "Here, there's no choice. We have to be close to one another to survive."
            him "True, we're always in each other's business. But we're always helping one another too."
            kevin "It's kind of like you're a big family then?"
            show him determined
            him "No, it's different. Families don't always get to choose to be together."
            him "It's more like we're all united by a common goal."
            kevin "So it's like you're always at work."
            show him normal
            him "Kind of, yeah."
            $ colonists += 1
    show him happy
    him "You guys are staying here for the rest of your lives, right?"
    zaina "That's right!"
    label ask_zaina_and_kevin:
    menu:
        "What should I ask them about?"
        "Are you planning to have children?" if not asked_kids:
            show him normal
            him "So... I know RET is trying to grow the colony..."
            show him surprised
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
                    show him determined
                    him "My parents are still on Earth. We have some extremely delayed correspondence."
            $ asked_family = True
            jump ask_zaina_and_kevin
        "What kind of food will you grow?" if not asked_grow:
            show him normal
            him "You have quite a bit of land out there by the radio tower."
            show him happy
            him "Any idea what you'll grow on it?"
            zaina "We brought some fruit trees, which I hope will make a nice orchard."
            zaina "Grapes are fairly hardy, and I would love to start a winery sometime!"
            kevin "I am planning to try my hand at a basic vegetable garden."
            show him normal
            him "Have you ever farmed before?"
            zaina "I practiced caring for fruit trees in the simulations on the shuttle."
            kevin "I also raised a magnificent patch of vegetables in the simulations."
            show him determined
            him "So the answer is no."
            kevin "The simulations have been updated since you flew over."
            kevin "They're quite lifelike!"
            show him normal
            him "Tell me how you feel about them after you harvest your first crops."
            $ asked_grow = True
            jump ask_zaina_and_kevin
        "How was the shuttle ride?" if not asked_shuttle:
            show him flirt
            him "Did you start to hate each other a little on the shuttle ride over?"
            kevin "No, I do not believe it is possible for us to hate each other."
            zaina "We got married right before the shuttle ride. So it was kind of like our honeymoon!"
            show him happy
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
            # TODO: Show sprites for people as we talk about them.
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
                    show him happy
                    him "Some people have complained that her bedside manner is a little callous."
                    him "So her objectivity is more relevant to customer satisfaction than, say, mine."
                    kevin "Are you implying that your carrots cannot feel your love?"
                    him "Correct. Unless that love manifests itself in better care."
                    $ tell_Kelly = True
                    jump colony_gossip
                "Naomi and Pavel" if not tell_Graysons:
                    show him normal
                    him "If over the course of your lifetime you ever feel hopeless or depressed, go talk to Naomi Grayson."
                    him "She can't prescribe medicine for you, but she's very reassuring and can encourage you to get more help."
                    zaina "Reassuring? So she basically tells you to hang in there."
                    him "Somehow when she says it, it feels like she understands what you're going through. She has some training in cognitive behavioral techniques, too."
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
                    show him happy
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
                            # TODO: give bonus to luddites here?
                    him "Their kids are getting older and should be able to help around the colony more."
                    $ tell_Perons = True
                    jump colony_gossip
                "Pete and Helen." if not tell_Pete:
                    show him happy
                    him "If you ever need to look something up or make something, our library is the place to go."
                    him "Pete is our librarian and also our cattle rancher."
                    show him normal
                    him "He has a wife, Helen, but I don't see much of her since their ranch is pretty far out."
                    $ tell_Pete = True
                    jump colony_gossip
                "Thuc and Julia." if not tell_Ngyuens:
                    show him happy
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
    scene storeroom
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
    $ random_crop = farm.crops.random_crop(include_animals = False)
    him "Sure, do you like [random_crop]?"
    if ((random_crop == "tomatoes") or (random_crop == "squash")):
        kevin "Yes, that is why I planted some myself. A popular choice, it seems."
    else:
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
    show him happy at center
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
    show him happy
    him "No, it's far more mundane. That's just what we call our monthly game night."
    kevin "I would love to play games with others. Why was this information hidden?"
    show him concerned
    him "I didn't want the new colonists to think I was being frivolous with my time."
    kevin "Face-to-face socialization is highly recommended by RET's psychologists."
    kevin "It may feel frivolous, but it can actually increase your productivity."
    show him normal
    him "But farmers a long time ago didn't have time to play cards. They worked from sunup to sundown without complaining."
    kevin "That's simply what they told their grandchildren. Let me come to your game night!"
    show him happy
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
    show him happy
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
    show him happy
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
            "We're sending fifty miners ur way, so if u could feed them, that would be gr8. They'll have $."
        else:
            "50 new miner neighbors are coming in 4 Earth years. Feed them."

        "I decided to meet with Ilian to see what he thought."
        scene storeroom with fade
        show ilian at center
        show him normal at midleft
        if (whole_harvest_to_storehouse == True):
            ilian "Well, a few farmers are already bringing their whole harvest to the storehouse."
            show ilian happy
            ilian "Based on the harvests of those farmers, we can probably grow and store enough food for the miners, but they will have to eat a lot of bread and beans."
            show ilian
            ilian "Assuming our chickens are still around in four Earth years, we could have hens ready for them to have eggs as well."
        else:
            ilian "I don't know how much food you guys are storing, so I have no idea if we'll have enough food for them or not."
            ilian "If worst comes to worst, they could farm instead of mining, which I'm sure RET would be THRILLED with."

        ilian "What do you want to do?"
        "How should we prepare?"
        menu:
            "Have the farmers bring their whole harvest instead of storing it individually, and encourage them to grow extra food.":
                $ miners += 2
                $ require_whole_harvest = True
                jump whole_harvest_required
            "Have farmers bring in a certain amount of surplus each harvest, and encourage them to grow more food.":
                him "Let's have the farmers bring their surplus to the storehouse, and I'll ask them to grow extra beans and wheat."
                $ miners += 1
                $ rationing = True
                jump ration_harvest
            "Don't set aside food for the miners. They can hunt and forage. Feeding miners wasn't in our contract.":
                $ pass #rationale: this has pros and cons for luddites, so I don't actually want to subtract from their score. It's easier to simply not add to the miner variable.
                jump no_formal_rationing
    else:
        scene community_center with fade
        show sara at midright
        show him normal at midleft
        "Sara called you in to discuss the latest news from RET."
        sara "RET is sending miners to start mining the Indium that Zaina and Kevin found."
        sara "The miners won't arrive for another four Earth years."
        if (whole_harvest_to_storehouse == True):
            show sara sad
            sara "Ilian tells me that we'll have enough food for them if we start storing a little now."
        else:
            show sara sad
            sara "We're not sure if we'll have enough food for them or not."
        sara "We will start storing the surplus of food that keeps the longest. I've started construction of a few silos for dried grains and beans."
        sara "Next harvest we'll start accepting canned goods as well. You can can large amounts in the storehouse, or bring in what you can at home."
        show sara
        sara "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sara "I'll be grading your crops against the RET standards."
        show sara sad
        sara "There's something I need your help with though. Some of the other farmers aren't excited about storing their surplus in the storehouse."
        show him surprised
        him "Really? Like who?"
        show sara
        sara "Pete and Martin are the ones you know the best."
        show him determined
        him "I'll talk to them." #this could also be a choice... how neglectful do you want to be
        $ rationing = True
        jump talk_about_food_storage
        # TODO: when/where are crops preserved?  Does Ilian have machines/employees that do this? Or are farmers supposed to do this before taking to the storehouse?
    return

    label whole_harvest_required:
    show him determined
    him "Let's have the farmers bring their whole harvest to the storehouse, so you can measure it."
    him "I'll ask them to start farming more beans and wheat too, since those store well."
    show ilian happy
    ilian "I'll need some help to build silos for the wheat."
    show him surprised
    him "This way we'll definitely have enough for the miners, right?"
    show ilian
    ilian "Yes. They won't even need to forage, unless they want some extra meat."
    jump ration_harvest

    label ration_harvest:
    ilian "I support your plan, but I'm worried about how we'll enforce it."
    ilian "Some of the other farmers are reluctant to centrally locate food."
    show him surprised
    him "Oh? Like who?"
    ilian "Like Pete and Martin."
    show ilian happy
    ilian "I think they'd listen to you if you tried to persuade them though."
    show ilian
    ilian "We'll pay credits for their surplus, which they can use to buy other crops."
    show him determined
    him "I'll talk to them."
    jump talk_about_food_storage

    label talk_about_food_storage:
    scene farm_exterior with fade
    show him normal at midright
    show pete at midleft
    him "Hey Pete. How are your cattle doing?"
    show pete happy
    pete "Surprisingly hale for living on an alien planet."
    show him determined
    him "Great. There's something I want to ask you about."
    him "I heard that you're not storing much surplus in the storehouse."
    jump pete_no_storehouse

    label no_formal_rationing:
    show him annoyed
    him "We can figure it out when they get here. Growing food for miners wasn't in our contracts, so it sets a bad precedent to save food for them."
    him "Worst-case scenario, they have to farm for a bit instead of mining all the time."
    show ilian smile
    ilian "Are you sure? I don't really want to be eaten if we run out of food."
    show him determined
    him "I think people could survive on the wild resources available, as long as they know what they are."
    show ilian
    ilian "Okay, whatever you say."
    return

    label pete_no_storehouse:
    show pete
    pete "This climate is so wet that no amount of salting and drying will make jerky last four Earth years."
    pete "I can't make cheese that doesn't mold right away."
    pete "The best way to store my surplus is to keep growing this herd."
    label convince_Pete:
    menu:
        "Is that really the best way?"
        "We could can some of the meat." if not talked_cans:
            show him normal
            him "I know canned meat doesn't taste very good compared to fresh, but it will keep for longer."
            him "How about it?"
            pete "I don't think anyone should have to eat canned meat, not when they live next to me!"
            him "Well, they're your cows."
            $ talked_cans = True
            jump convince_Pete
        "You'll need credits to get other food." if not talked_credits:
            show him normal
            him "Even if the best way to store cow meat is on a live cow, you're still going to need to eat something other than milk and meat."
            him "How will you afford vegetables and grain?"
            show pete happy
            pete "Plenty of people are willing to trade for or buy milk and beef."
            show pete
            pete "Ilian is just acting as a middleman. I don't like that he controls all the prices of food either."
            pete "I prefer to deal directly with my customers."
            $ talked_credits = True
            jump convince_Pete
        "If we canned some beef, then we'd have meat even if your herd died suddenly." if not talked_something:
            show him surprised
            him "What if one day you wake up and your whole herd of cattle is gone?"
            show him determined
            him "If you canned some meat, then we would at least have something."
            show pete happy
            pete "That's true. But the herd is so small now that I need every cow and bull for good genetic diversity."
            show pete
            pete "Plus I think canned meat is revolting. I would rather just eat vegetables."
            $ talked_something = True
            jump convince_Pete
        "We could can some of the dairy products." if not talked_canning_dairy:
            show him happy
            him "We could try making dried milk powder or clarified butter, which would last a long time."
            pete "Why would we do that when we have plenty of fresh stuff?"
            show him determined
            him "Well, I know cows don't produce consistently. So you could have some dairy on hand in case your cows don't eat as much."
            him "Or they could end up eating some plant that makes the milk taste bad, so you'd be missing out on an opportunity to sell."
            show pete happy
            pete "Hmm. That is a good point."
            show pete
            $ talked_canning_dairy = True
            jump convince_Pete
        "I guess that's what Pete is going to do.":
            show him concerned
            him "Yeah, you're right. Sorry, I didn't really think about how difficult it would be to store beef and dairy that long."
            pete "Glad you understand."
            jump canning_dairy

    label canning_dairy:
    if talked_canning_dairy:
        show pete happy
        pete "I'll look into canning some milk and butter though."
        show him happy
        him "Great!"
        $ colonists += 1
    else:
        pass
    scene fields with fade
    show martin at midleft
    show him normal at midright
    him "So Martin, how's your farm doing?"
    show martin angry
    martin "Recently some of our turkeys got sick and we couldn't even eat their meat after they died."
    show him concerned
    him "How about your beans, are they doing well?"
    show martin happy
    martin "Yes! We eat them about as fast as we can grow them."
    show him normal
    him "I was thinking if you had some extras, you could can them and store them in the storehouse."
    show martin
    martin "I would if I thought we would have extras. But we're usually trading them to other people for their crops."
    martin "You should know that. [her_name] usually trades vegetables for our eggs and corn."
    if require_whole_harvest:
        show him determined
        him "Starting from now on, you'll need to bring in your harvest to Ilian if you want other crops."
        him "We need to prepare to feed the miners, and this is the easiest way to ensure that everyone has enough food."
        show martin angry
        martin "What if I don't want to do that?"
        show him annoyed
        him "It's in your contract."
        show martin
        martin "Well the way we've been doing it has been working just fine."
        show him concerned
        him "We didn't have fifty extra mouths to feed then."
        show martin angry
        martin "And we don't now! I think you're overreacting. We have plenty of food."
        show him determined
        him "How about you prove that I'm overreacting by bringing all your food to Ilian so we know what we have to work with?"
        show martin
        martin "We eat most of our crops the same day we harvest them. But we do try to store a little extra."
        show him normal
        him "I get what you're saying. Just write down how much you eat and tell Ilian."
        him "Then if you have extra, bring that in once a week and he can calculate how your crops are doing."
        show martin angry
        martin "Okay, I think I can do that. But I still think this is excessive."
    elif rationing:
        show him determined
        him "Starting from now on, I need you to bring in twenty percent of your harvest."
        him "That number may change, but this is the easiest way to start storing a little food for the miners."
        show martin angry
        martin "What if I don't have enough food to bring in twenty percent?"
        show him concerned
        him "Then bring in ten percent. Just try to keep track so we have an idea of how much food we have collectively."
        show martin
        martin "Alright. I'll do it."
        show him normal
        him "Thank you."
    else:
        show him determined
        him "It works well now, but soon we'll be trading credits instead of food."
        show martin happy
        martin "I'm happy to take your credits then."
        show him normal
        him "Okay, well if you ever need more credits, you can always sell your beans to Ilian."
        show martin
        martin "Good to know."
    return


# 6 - discussion of choice from 5 at game night
label community6:
    if town_hall_games:
        show community_center with fade
    else:
        show farm_exterior with fade
    show pete at midright
    show him normal at left #BUG: his sprite isn't showing up. I'm not sure why not. I tried having him at center as well and had the same problem.
    show thuc at midleft
    thuc "I brought 'Maximal Conquest' tonight, are you guys up for it?"
    show him determined
    him "Yes, and I promise to start in the Northern Hemisphere this time."
    show pete happy
    pete "Your Antarctica strategy had no sense whatsoever."
    show him angry
    him "Trying the same losing strategy every time and hoping it will win has no sense."
    show pete
    pete "I'll make you eat your words. Can we keep track of score on your tablet? Ours is out for repairs."
    show him surprised
    him "What do you mean? Don't you both have one?"
    show helen at right
    helen "No, because SOMEONE left it out during a solar flare."
    show pete happy
    pete "And SOMEONE left their tablet in spittin' distance of a cow."
    show him normal
    him "That must be rough."
    show pete
    pete "Nah, it's better. I used to check my tablet for new messages all day long. Now I know how useless most of them were."
    pete "I can concentrate on what I'm doing."
    pete "I don't even mind doing my feed calculations for the cattle by hand."
    show helen happy
    helen "I miss watching TV. But at least one of the tablets is repairable, so we should be back to our normal selves soon."
    show pete
    pete "I don't know about me. I kind of like feeling like I'm completely on my own."
    show thuc sad
    thuc "But you still are having game night, and you have your family too, so it's not like you're completely isolated."
    menu:
        "What do you think?"
        "We need each other to survive.":
            $ colonists += 1
            show him determined
            him "We need each other to survive. There's no way one person could survive on their own out here."
            show pete hapy
            pete "Is that really true? I've been out there on my own before--there's good foraging and hunting."
            show him surprised
            him "Maybe you could survive on your own, but what about your family?"
            show pete
            pete "They can help forage too!"
            pete "The most dangerous thing is the solar radiation. Without a radio, we wouldn't know when a solar flare was coming."
            show pete happy
            pete "It's definitely more reliable to live in a community where we can help each other."
        "I understand wanting to be away from it all.":
            $ luddites += 1
            show him determined
            him "I understand wanting to be away from it all. It's part of the reason I came here."
            show pete happy
            pete "We don't have to deal with inane government interference or rules made for the sake of havin' 'em."
            show him concerned
            him "Although some of RETs demands have felt that way..."
            show pete
            pete "True. But you can see where they're coming from for the most part."
            show pete happy
            pete "And they're not in our face about it. I could go camping tonight and they'd be none the wiser."
            show him flirt
            him "Yeah, as long as your cows were okay with it."
        "We have an obligation to help RET feed their miners now.":
            $ miners += 1
            show him determined
            him "Being alone sounds romantic, but we have an obligation to help RET feed their miners now."
            him "If we all went rogue, those miners would starve to death."
            show him concerned
            him "And we wouldn't be holding up our end of the bargain. It's expensive to send us out here."
            show pete happy
            pete "I do feel bound by my word. But if RET starts askin' more than was in our contracts, I wouldn't feel badly about changing my side of things."
            show him surprised
            him "What do you mean?"
            show pete
            pete "What if we don't have enough food for all these miners?"
            pete "If that happens, you bet I'm going to look after me and my own first."
            pete "We're promised enough food to live off of, but if that doesn't exist, there's no way RET can make it right."
            show pete happy
            pete "We're all trying to farm as efficiently as we can. But if RET overestimated our yields, I don't want to pay for it."
            show him concerned
            him "Good point. I hope we can mange."
    if require_whole_harvest:
        show thuc
        thuc "Speaking of food, Ilian just sent out a message that we don't have to bring in our whole harvest anymore."
        thuc "He has enough data, and he sent out a table of who should bring in how much."
        thuc "It ended up being about twenty percent for most farmers." #TODO: is this a reasonable amount?
        show pete
        pete "I deliver directly to my customers, so I've just been sending Ilian my stats."
        show thuc sad
        thuc "I guess it doesn't really make sense to bring in a calf either."
        show pete happy
        pete "Nope."
        show him happy
        him "It was a little more work to bring in all my crops, but I think I had a better variety of fresh food that way."
        show thuc
        thuc "And in comparison, twenty percent of our crops seems pretty easy to bring in!"
    else:
        pass
    return

# 7 - Comparing compensation
label community7:
    show community_center with fade
    show zaina at midright
    zaina "The fossil record near here contains many vertebrates that do not have shells. If they had been merely eaten to death, we wouldn't have their fossils."
    zaina "One possibility is that an area that used to be part of the ocean became locked into one area, and they ate up all possible prey."
    zaina "Another possibility is that solar flares are a geologically recent event, and that they died quickly once the flares started."
    zaina "However, the existence of other animals at the same time with shells that are resistent to radiation makes it likely that the solar flare problem was cyclic."
    show pavel center with move
    pavel "Thank you, Zaina, for the presentation on Terra's probable geologic history."
    hide zaina with moveoutright
    pavel "We want you to feel that your fellow farmers are co-workers, so please use this time to talk to them."
    show pavel
    pavel "I know you're all very busy, so we've arranged for a few extra free carrots for those of you who stay and socialize for fifteen minutes."
    hide pavel with moveoutright
    show kevin at midright with move
    show him normal at midleft
    kevin "I'm surprised that you're offering incentives. The excitement of living on a new planet was sufficient payment for Zaina and I to come to Talaam and socialize."
    show him surprised
    him "RET didn't give you any money? At least I know that my parents are taken care of."
    kevin "What do you mean?"
    show him happy
    him "RET gave me a bunch of money that I used for their retirement fund."
    kevin "They made me no such offer."
    show thuc at center with move
    thuc "I practically had to pay RET to let me come. What gives?"
    show him annoyed
    him "Huh. You're basically giving up your lives on Earth, so I'm surprised that they didn't offer you some kind of compensation for that."
    show ilian happy at left with move
    ilian "Maybe some of us were happy to leave our Earth lives behind."
    show helen happy at right with move #too many people!?
    helen "This is a new one for me. Ilian has a secret past?"
    show ilian
    ilian "There's nothing secret about it. I was about to default on my loans for my restaurant supply store."
    ilian "RET said they would take care of it."
    show helen
    helen "Do you know if they did?"
    show ilian happy
    ilian "I haven't heard from any debt collectors since."
    kevin "You may have noticed but it's very difficult for people on Earth to contact you here."
    show ilian
    ilian "It was win-win for me."
    kevin "I was so intent on coming to Talaam that I didn't think to negotiate compensation."
    hide ilian with moveoutleft
    show thuc sad
    thuc "I wish I had thought of negotiating too. Now that I think about it, they really needed me."
    show him flirt
    him "Oh come on. They could have found some other sustainable agriculture specialist with 10 kids."
    show thuc
    thuc "Or 8! Fewer pieces to ship."
    kevin "Did your children suffer developmental delays because of the journey?"
    show thuc sad
    thuc "One of them is a little shorter than the rest, but other than that I'd say that being on a different planet has accelerated their development."
    thuc "They're not necessarily reading sooner, but we genuinely need their help on the farm."
    show thuc
    thuc "They have more responsibilities than I did at their age, so they have to grow up fast."
    show thuc sad
    thuc "And none of my family are getting paid for completely transplanting our lives here."
    if is_liason:
        show thuc
        thuc "Hey [his_name], can I make a formal request? I'd like RET to donate $10,000 to the charity of my choice."
        menu:
            "What will you do for Thuc?"
            "Ask RET in my next e-mail.":
                $ miners += 1
                show him normal
                him "I can ask them in my next e-mail."
                show thuc sad
                thuc "E-mail? Not an insta-com?"
                show him happy
                him "I only get so many instant communication slots."
                show thuc
                thuc "But by the time they get your e-mail no one will remember me."
                show him determined
                him "I think RET has bigger things to worry about."
                show thuc sad
                thuc "Fine, an e-mail is fine."
            "From a business standpoint, you're stuck here.":
                $ luddites += 1
                show him annoyed
                him "You don't have any leverage over them. It's not like you can quit now."
                show thuc sad
                thuc "I sure do have leverage!"
                thuc "I could decide to leave the colony!"
                show him concerned
                him "You wouldn't seriously consider that."
                show helen happy
                helen "I don't know, he looks pretty serious."
                show thuc
                thuc "I'm joking. Rice cultivation is kind of pointless for just twelve people."
                show thuc sad
                thuc "I just don't like the idea that I have no power over my life."
            "I hear you, but let's focus on the here and now.":
                $ colonists += 1
                show him determined
                him "I could ask them in an e-mail. But what about all the rest of the new colonists who didn't receive compensation either?"
                him "Let's leave the past in the past."
                show him happy
                him "Get stinking rich off your enormous farm and have a feast to make us all jealous."
                thuc "You do have a point. With my new crop of fertilizer I'll be stinking at least!"
    else:
        hide kevin with moveoutright
        show sara at midright
        show thuc
        thuc "Hey, Sara, help me out here. Could you ask RET to send my back pay to the charity of my choice?"
        show sara sad
        sara "I heard that RET is economizing, but I can ask."
        thuc "Thanks. Do you think RET will do anything, [his_name]?"
        menu:
            "What do you think RET should do for Thuc?"
            "Make a big donation.":
                $ miners += 1
                show him determined
                him "They should make a big donation in your name."
                thuc "Right?"
                show him surprised
                him "What charity would you choose?"
                show thuc sad
                thuc "Something to promote sustainable agriculture in developing nations like this one."
                show him flirt
                him "I think the biggest contribution you can make to our developing nation is to keep your goats out of my spinach."
                show thuc
                thuc "Burn!"
            "They won't do anything.":
                $ luddites += 1
                show him concerned
                him "You're stuck here. You have no choice but to be an employee of RET."
                show thuc sad
                thuc "I could decide to leave the colony!"
                show him surprised
                him "You wouldn't seriously consider that."
                show helen sad
                helen "I don't know, he looks pretty serious."
                show thuc
                thuc "I'm joking. Rice cultivation is kind of pointless for just twelve people."
                show thuc sad
                thuc "I just don't like the idea that I have no power over my life."
            "They probably won't do anything, but we have more important things to worry about.":
                $ colonists += 1
                show him determined
                him "Life isn't fair, but if we work hard, maybe we can eat well while we live it."
                show him happy
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
    $ talked_about_luxuries_counter = 0

    if is_liason:
        show farm_exterior with fade
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
        label talk_about_luxuries:
            if (talked_about_luxuries_counter >= 4):
                if is_liason:
                    him "Oh, it's already the afternoon! I need to send in my report right away."
                    jump write_report
                else:
                    "I told Sara what everyone wanted, and she wrote the report."
                    return
        show farm_exterior with fade
        "Who will I talk to about what Earth luxuries they want?"
        menu:
            "Natalia" if not talked_to_Natalia:
                show natalia at left
                with dissolve
                natalia "I don't care what else comes from Earth, but there had better be some medication for Martin in there. The longer he lives, the happier our family will be."
                show him concerned
                him "What medication does he need?"
                natalia "[her_name] said he needed Vemurafecholoronib. Let's see... 500 mg for six months and 1000 mg for another 6 months."
                show him surprised
                him "Won't RET be sending this anyway?"
                natalia "They told [her_name] that it wasn't possible, but maybe you can do something."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Natalia = True
                jump talk_about_luxuries
            "Thuc Nguyen" if not talked_to_Thuc:
                show thuc at left
                with dissolve
                show thuc sad
                thuc "I'd like to grow peanuts. Regular, unroasted peanuts will work fine for cultivation purposes."
                show thuc
                thuc "Then I can make peanut stew and peanut butter!"
                # TODO: if you do this, then allow the user to plant peanuts also
                $ talked_about_luxuries_counter += 1
                $ talked_to_Thuc = True
                jump talk_about_luxuries
            "Sara" if not talked_to_Sara:
                show sara at right with dissolve
                sara "Oh, I don't know if this is possible, but I would really, really love a bicycle."
                show sara sad
                sara "I'm terrible with horses and I hate how they just eat more of our food."
                show sara
                sara "A bicycle wouldn't get hurt by radiation and can go faster in some situations."
                # Would she also want one so that her son could use it?
                $ talked_about_luxuries_counter += 1
                $ talked_to_Sara = True
                jump talk_about_luxuries
            "Kevin" if not talked_to_Kevin:
                show kevin at left with dissolve
                kevin "This is an extremely inefficient way to gather information. Could you not have contacted me electronically?"
                show him determined
                him "Yes, but you might not have responded in time. I need to tell them by the end of the day!"
                kevin "Very well. Are they sending new tablet batteries like I requested?"
                show him flirt
                him "Yes, yes, don't worry about that. Ask for something that will boost your morale."
                kevin "Wouldn't being reminded of the Earth I'll never return to lower my morale?"
                show him happy
                him "It sounds like you don't want anything."
                kevin "I would like the remaining episodes of the show Tulip House."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Kevin = True
                jump talk_about_luxuries
            "Pavel" if not talked_to_Pavel:
                show pavel sad at left with dissolve
                pavel "Oh, there are so many things I miss."
                pavel "Sushi, wine, tempura, Krem de la Krem donuts, French fries, falafal, fried chicken,"
                pavel "those really cheap frozen pizzas from Glosemitto's, slow-roasted coffee, Fabrielle brand pelmeni,"
                pavel "sourdough bread, calamari, egg rolls but especially the sweet-and-sour sauce with lots of high fructose corn syrup,"
                pavel "Goods Inside cereal, homogenized milk, cotton candy, cheesecake, tuna salad, Michele's meat-alike paste,"
                pavel "really hot salsa, tortillas, curry powder, Chocolate Confession ice cream, and Swiss cheese, or any cheese really."
                show pavel
                pavel "And that's just the food I miss!"
                show him surprised
                him "Wow. Well, it needs to be non-perishable or at least have a long shelf life, so I think that eliminates most of the things on your list."
                show him happy
                him "I could put you down for curry powder though."
                show pavel sad
                pavel "Oh, well make sure it's PatiPal's Extra Hot Curry Powder. It's the only one worth having."
                show him determined
                him "I'll see what I--"
                show pavel
                pavel "Wait, wouldn't it make more sense to grow the spices so I can make my own curry powder?"
                show him normal
                him "Sure."
                pavel "Okay, so just ask them to send me seeds for all the spices in PatiPal's Extra Hot Curry Powder along with a recipe."
                show him concerned
                him "Hmm. I need to put this in an insta-com."
                show pavel sad
                pavel "Oh dear. How did they not tell you about this sooner?"
                show him sad
                him "I think they only knew about the extra space on the shuttle this morning."
                show pavel
                pavel "You are going to have to cram a lot into that message!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Pavel = True
                jump talk_about_luxuries
        label write_report:
            "What should I write?"
            if talked_to_Natalia:
                "I don't have enough room to ask for Martin's specific medicine and dosage and all the other things people wanted."
                menu:
                    "Specify the medication and dosage. Do your best with the other stuff.":
                        $ asked_only_medicine = True
                        return
                    "Maximize happiness and ask for everyone else's stuff specifically.":
                        return
            else:
                "I sent the message."
                return
    else:
        show fields with fade
        show sara
        sara "RET just told me that they have extra space on their shuttle and they can send some extra things from Earth to us."
        show sara sad
        sara "What would you like?"
        show him determined
        him "Let me think about that."
        show sara
        sara "I need to know right now."
        show him happy
        him "Hmm. How about some good old Earth toilet paper?"
        show sara sad
        sara "Great. I can shorten that to TP in the insta-comm."
        show him flirt
        him "Hopefully they won't send me a textbook on Topological Planning."
        show sara
        sara "Don't get your hopes up. But look on the bright side: in four years you probably won't even remember what you asked for!"
        sara "Can you help me ask everyone else what they want? I have a list here of people you know and could ask pretty easily."
        show him normal
        him "Okay, yeah, I can do that."
        jump talk_about_luxuries

    label luxuries_absent:
        show bedroom with fade
        show him determined at left with dissolve
        show her at right with dissolve
        him "Man, I really miss Earth toilet paper."
        her "Wouldn't it be great if RET sent some on the next shuttle?"
        show him concerned
        him "Yeah, that's never going to happen."

    return

# 9 - camping with Pete
label community9:
    show pond with fade
    show pete at midright
    show him normal at midleft #he isn't appearing in my testing... not sure why not.
    pete "Hey, [his_name]!"
    show him happy
    him "Hi Pete."
    show pete happy
    pete "Out to catch some fish?"
    show him normal
    him "No, just taking a walk."
    show pete
    pete "How's the farm?"
    show him happy
    him "Doing okay I guess."
    show pete happy
    pete "I miss having guy's night!"
    show him concerned
    him "Yeah. Things got really busy with our last harvest and we never really picked it up again."
    show pete
    pete "What do you say to accompanying me on a hunting expedition?"
    show him surprised
    him "Now?"
    show pete happy
    pete "No, this weekend. We can camp overnight so we can get further from the colony."
    show him concerned
    him "Is that really necessary?"
    show pete
    pete "Yes, the hunting is no good around the colony. I think all the strange animal sounds scares off the smaller creatures."
    pete "We'll only go a few miles out. Until we find a herd of those grass crabs."
    "What do I tell Pete?"
    menu:
        "Sounds fun! Go with him and invite Thuc.": #you learn the particulars of how to camp safe from radiation.
            $ luddites += 1
            $ colonists += 1
            show pete
            pete "We have two radiation-proof tents that RET sent with us."
            pete "I don't like relying on them for so many things though, so I'm going to try out my own radiation-proof tent."
            show him surprised
            him "And you're testing it on us?"
            show pete happy
            pete "No, we'll use the RET tents. I will test my homemade tent though."
            show pete
            pete "Bring something to sleep on and some food. And get a bow and arrow from the community center."
            show him determined
            him "Not the rifles?"
            show pete happy
            pete "With the guns, they all run away when they hear the shot. I want to see if the bow and arrow does any better."
            pete "Plus it seems funner to use a bow."
            show him concerned
            him "I haven't praticed shooting a bow and arrow before."
            show pete
            pete "Not even in the simulations on the shuttle ride out here? We had so much time for that!"
            show him angry
            him "I was more concerned about reading the latest research on alien plants and running farm simulations."
            pete "You can set up traps then. I want to fell one of these creatures by my own power!"
            show him concerned
            him "I'll bring some wire for snares I guess."
            scene path with fade
            show thuc at center
            show pete at midright
            show him normal at midleft
            "I tell Thuc about the campout and he joins us that weekend, bringing a bow from the community center."
            "We find a group of grass crabs and observe them for a while."
            "The grass crabs are about the size of a capybara, but have less meat because of their large shells."
            "While they eat grass, they also eat the woody parts of plants. Their large beak-like claw cuts through the woody part, which allows them to suck on it while on the move."
            #makes sense?
            show thuc sad
            thuc "It seems like in the morning, they like to be in the sun, but then in the evening, they like to be in the shade."
            show pete
            pete "They're like insects. The can't make their own body heat so they have to position themselves well."
            show thuc
            him "This herd is a pretty good size. There are some juveniles and also some older animals."
            show pete happy at midleft
            pete "You can see some of the trails they've been on. Wait for them to settle for the night and then put the traps on the trail."
            show thuc sad
            thuc "Here [his_name], let me help set up the snares."
            "After a quick dinner of dried fruit and mashed beans, I set the snares."
            show night_overlay with dissolve
            show pete
            pete "Before we turn in, let's make some camouflage for ourselves."
            show thuc sad
            thuc "I was thinking about that too. We can tie some leaves to our bodies, but it will be noisy."
            show pete happy
            pete "We can at least make our clothing more inconspicuous by making the coloring irregular."
            show pete
            pete "Let's use some of the ashes from the fire to help us blend in with the shadows."
            scene path with fade
            "After sleeping in tents, you wake up early to catch the grass crabs while they're still drowsy."
            "They gather in the sunlight, warming themselves and chewing on sticks"
            "You're about 20 feet away when you stop trying to get closer."
            show pete at midright
            pete "Those two big ones look like good targets."
            show him determined at left
            him "Try not to lose any arrows."
            show thuc sad at midleft
            thuc "I won't lose them but I will definitely loose them."
            show him annoyed
            him "..."
            show thuc
            thuc "   "
            "One of the grass crabs looks in your direction and everyone gets silent."
            "The group starts slowly moving away."
            "Pete points to himself and makes a circular motion."
            "He points to a different grass crab that is a bit further off."
            "You all creep around quietly, giving the grass crabs a wide berth. It's slow and laborious."
            #creative blocking ideas?
            "You wish that you had just scared the herd into your snares, since that would have taken less time."
            "It seems like you're maneuvering all morning. Finally, Pete gives you a thumbs-up and draws his bow."
            "He hits one of the animals, but it simply walks off with an arrow sticking out of it."
            show thuc sad
            thuc "It's still alive!"
            "Together you stalk the animal to see if it will fall over."
            show pete happy
            pete "I think I hit it right where its heart should be. Of course, with those shells, it's hard to tell how deep the arrow went."
            "It's lying down and not moving. Pete approaches, knife in hand."
            "Suddenly, the animal pinches Pete's leg with its front claw!"
            show pete
            pete "Yeeeowch!"
            # TODO: Should this be a timed menu?
            menu:
                "Tackle the crab.":
                    $ luddites += 1
                    #TODO: I want the injured-hand option to result in making less money that month, if we do the currency thing.
                    "You tackle grass crab from behind, easily outweighing it."
                    "The crab releases Pete and tries wildly to pinch you, but the claw isn't flexible enough to reach you while you're on its back."
                    "Pete stabs the crab, but cuts your arm in the process."
                    show pete happy
                    pete "We got 'em!"
                    show him surprised
                    him "Your leg!"
                    show pete
                    pete "I think it looks worse than it is."
                    show him concerned
                    him "Let's get back to camp."
                "Uhhh.":
                    $ pass
                    "You freeze, not knowing what to do. Thuc steps on the crab's claw, and it releases its grip on Pete's leg, but the grass crab scratches Thuc with its smaller, comb-like arm."
                    "Pete thrusts his dagger into the crevice where the crab's shells meet."
                    show pete happy
                    pete "Got 'em!"
                    show him concerned
                    him "Are you guys okay?"
                    show pete
                    pete "It doesn't feel too bad. Let's get back to camp and see how things are."
            "You help Thuc to haul the grass crab back to the camp."
            show fields with fade
            show him determined at midleft
            show pete at midright
            him "Here, sit down, let's clean these wounds."
            show pete happy at midright
            pete "Nothing a bandage can't fix."
            "After everyone is patched up, you find that you've captured a grass crab in one of your snares."
            "Pete gives the grass crab a decoy stick to hold so Thuc can attack it from behind."
            show him happy
            him "This is going to be delicious."
            show pete
            pete "Let's eat some and then head back."
            "After making a fire, a solar flare warning comes up on the radio."
            show pete happy
            pete "Fantastic. I can test my homemade tent."
            show him surprised
            him "What did you make your homemade tent out of?"
            show pete
            pete "The fabric is leather. That doesn't do anything for radiation."
            pete "But after you set it up just so, you pour water into the top and the water insulates from the radiation."
            "Pete pours the water in, and it gradually fills the tent's lining."
            "After about twenty minutes, the radio comes on again to say that the flare has abated."
            show pete happy
            pete "And it appears to reduce solar radiation! Too bad it's completely dark in there."
            "Some water leaked from the tent during the time you were waiting."
            show pete
            pete "It looks like it has a few leaks too."
            show him surprised
            him "Hmm. Aren't these shells radiation-proof? Maybe you could build a house out of them."
            show pete happy
            pete "Good idea. I'll save them so I can experiment."
            "After eating some of the meat, you and Pete and Thuc bring the rest back to the colony."
            show pete
            pete "We process cattle all the time, so we can finish butchering the grass crab. I'll make sure you get some."
            pete "Come by in a few hours if you want something fresh, otherwise it's all going to be jerky."
            show him happy
            him "Thanks Pete."
        "Sounds dangerous. I have to focus on farming right now anyway.":
            $ miners += 1 #not sure which side colonists +1 should go on for this one.
            show him concerned
            him "What happens if you get pinched by one of those things? It doesn't sound safe."
            show pete
            pete "That's the whole point! Gets your blood moving."
            show him determined
            him "Just seeing if I'll have enough food for the next month is risky enough for my tastes."
            "Pete went hunting on his own. But he brought back some jerky from the grass crab he killed."
            #scene change
            show him happy
            him "This is delicious."
            show pete happy
            pete "It took me nearly all day to finally hit one. Then I had to chase it down!"
            show him surprised
            him "Was it worth it?"
            pete "Hell yes! Herding cattle is fine for everyday, but every once in a while I need some excitement in my life."
    return

# 10 - Peron's over for dinner, who should take care of their farm?
label community10:
    show farm_interior with fade
    her "I'm leaving for work now. Goodbye honey!"
    him "Bye [her_name]. Oh, and don't forget that we're having dinner with the Perons tonight."
    her "I wonder what they wanted to talk about..."
    him "Maybe they're just being friendly?"
    "After weeding and clearing out old growth, Terra comes home from school."
    "We make a simple salad together, and when [her_name] arrives we head over to the Peron's."
    show farm exterior
    natalia "Thanks for coming over. We're just finishing up the rice."
    martin "We made a turkey bean soup. It should go well with your salad."
    "We ate outside, where the Perons had built two picnic benches, with some crabbird shells modified to be stools."
    #TODO: If we have sprites for any of their kids, I can insert them into the conversation.
    "After the meal, Terra runs off to play with the kids."
    martin "As you may have heard, I have skin cancer."
    her "I assure you that doctor-patient confidentiality is important to me and I would never discuss your health problems without your consent!"
    martin "I know! You are not the only one who knows, however."
    natalia "The more people who know about your disease, the more people who can help us!"
    if (asked_only_medicine):
        martin "If I can hang on until the medicine arrives, that should help, but we're still thinking ahead."
    else:
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
    show farm_interior with fade
    "The shuttle is set to arrive today!" #make this a family conversation?
    kid "I wonder what the new people will look like."
    him "Well, they'll look like we do. We're all humans."
    her "Unless aliens have secretly taken over Earth!"
    show sage_and_scrub_brush with fade
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
    him "No, no one mentioned it. I hope you're not here to help [her_name]; she has a real nurse assisting her now."
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
    him "Nice to meet you, Chaco."
    # TODO: There are too many of these to show all at once. We can delete some or change how we show menus.
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

            if (talked_to_Pavel and is_liason):
                him "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel "I'm so happy right now!"

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
                # uncomment this when peanut icon available
                # $ enable_crop("peanuts")
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
            # TODO: allow planting spices? garlic at least?
            # enable_crop("garlic")

            if (talked_to_Pavel and is_liason):
                him "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel "I'm so happy right now!"

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

            nvl clear
            pete_c "Thanks for asking about the cattle. A few people have asked so I'm e-mailing all of you right now. I have put tiny screws that look like security cameras at intervals around my fence and I haven't had any more cattle go missing."
            "I rolled my eyes. Like that would fool anyone."
            pete_c "I think it was the miners. There were tracks of two people with boots and the missing cow that went out the gate toward the miners."
            pete_c "They had to wake up the cow and push her; I can tell they had a hard time but I bet they had some treat to get her to move."
            pete_c "I don't know how they'll butcher and slaughter her without the tools for it. Things could get really messy."
            pete_c "We've already butchered this season's bulls, and with the demand for beef so high, I can't justify slaughtering any cows."
            pete_c "We'll have to live without beef for a while so that we can give everyone some next season."
            nvl hide

            "That night we had Chaco over for dinner again as part of our welcome miner program."
            "It was a habit now, and after a few weeks, Chaco got more comfortable with us and talked more."
            him "Thanks for helping with the dishes, Chaco."
            chaco "You're welcome. Thanks for the food."
            chaco "I brought my telescope like you asked. I can show you some stars."
            chaco "We might be able to see Earth's sun if it's clear."
            him "Great. I think Terra will love that."
            "Seeing our old sun, I suddenly felt homesick. I missed grocery stores and delivery services. I missed the way Earth trees silhouetted in the sunset."
            "I missed my parents, and the way my mom made macaroni and cheese with bacon on top. I missed my dad's laugh. I missed roads and trains and restaurants." #believable?
            him "It shows how far away we really are."
            kid "How far away are we?"
            chaco "About four light years." #more precise answer?
            "We looked at the sky."
            him "Oh, a shooting star!"
            kid "I saw it! I saw it!"
            "I pulled myself out of my nostalgia. No point in moping about Earth."
            "Especially when we had problems here... Chaco might know something about the missing cow. What should I ask?"
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
                    brennan "I hope you find the missing cow."
                    brennan "Now if you don't mind, I need to get back to work."

                    "We left and headed down the mountain. Pavel waved and joined us."
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
                    "I left and headed down the mountain. Pavel waved and joined me."
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
                    pavel "Can you tell Pete what we found out?"
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

# 13 - Save the cave!
label community13:
    $ cave_partially_explored = False

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
        $ lily_mad_at_RET = True
    return

    label cave_explored:
        $ cave_explored = True
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
    thuc "So Kevin here can control the shuttle remotely?"
    brennan "Yes, I don't know the details, but it just needs to get into orbit around Talaam. When it's at the right place and speed to get to Earth, Kevin will make adjustments for it to leave orbit."
    thuc "When you flew back, your pilot was in the shuttle. Doesn't it make a difference?"
    brennan "Yes, it does. The main advantage to piloting from inside the shuttle is that you can change things based on how it feels."
    brennan "Since we're just sending back metal, feeling the pain of excessive g-forces isn't a problem our pilots need to worry about."
    brennan "Their acceleration should be a good metric for that anyway."
    "Kevin was broadcasting the launch on the radio."
    kevin "{i} Lift-off in 10{/i}"
    kevin "{i}9{/i}"
    kevin "{i}8{/i}"
    kevin "{i}7{/i}"
    kevin "{i}6{/i}"
    kevin "{i}5{/i}"
    kevin "{i}4{/i}"
    kevin "{i}3{/i}"
    kevin "{i}2{/i}"
    kevin "{i}1{/i}"
    "We watched the shuttle as it started consuming fuel to power its flight."
    kevin "{i}Lift-off, we have lift-off{/i}"
    "Soon the shuttle was just a twinkle in the sky, and it disappeared."
    "Kevin continued his narration. About seven minutes later he said that we'd reached orbit."
    pete "Before y'all go, I have an announcement to make."
    pete "Helen and Travis and me are moving."
    pavel "Is there something wrong with your house?"
    pete "Nothing wrong with the ranch."
    pete "We're tired of working for RET. We want to try to make it on our own."
    pete "Part of the reason I came here was to live off the land."
    pete "'Cept now RET is making all sorts of demands of us. Wants us to spend all our time farming food for other people."
    pete "They haven't treated us fairly."
    if require_whole_harvest or rationing:
        pete "The miners don't respect my property. They stole one of my cows and never returned her."
    else:
        pete "They expect us to feed the miners, but we can barely feed ourselves."
    pete "They don't respect the natural beauty of Talaam, and they destroyed a cave in the course of their mining."
    if lily_mad_at_RET:
        lily "They don't respect the needs of researchers either."
        lily "I came here to study this planet, not destroy it."
        lily "I'm going with Pete and his family."
        $ luddites += 1
    else:
        lily "I plan to visit you often."
        lily "There is so much more to learn about this planet."
    if not (asked_only_medicine):
        pete "They don't even care about us enough to send the right medicines."
        "Tomás Peron and Joanna Nguyen tell us their plans to go with Pete and his family."
        $ luddites += 1
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
            him "But what if you get hurt or develop skin cancer? What are your cows going to eat?"
            pete "We'll figure it out. Seems like half the things [her_name] deals with would heal on their own."
            him "This is your family you're experimenting with."
            pete "I know. I don't like our present condition, so I'm changing it."
        "Tell them that I understand.":
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
                him "Hey, Thuc, can someone in your family look after the rest of the cattle?"
                thuc "It's not our specialty but I'm sure we can learn."
                thuc "Some of the older kids would probably like living on the ranch."
                $ colonists += 1
                $ thuc_has_cattle = True
            #Thuc doesn't feel as loyal to Rare Earth Tech because they didn't compensate him fairly.
            # "Take them for my own farm!":
            #not sure if I want this as a real option.
            # Maybe offer them to the miners?
            #   $ pass
            "Wait for a volunteer.":
                him "Does anyone want to take the rest of the cattle?"
                ilian "I'll take them. I know how to butcher them at least."
                thuc "They'll be a fair bit of work. Want some of my kids to help you out?"
                ilian "Sure."
                $ miners += 1
                $ ilian_has_cattle = True
            #Ilian feels more loyal to Rare Earth Tech, despite his cynical personality?
    else:
        "Pete and Helen's cattle went to Ilian, who wanted to take care of them."
    return


# 15 - Naomi dies
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
    her "We'll be doing palliative care."
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
    him "Someone ought to invent a radiation umbrella or something."
    her "It's not that simple..."
    him "Nothing is."
    menu:
        "What should I say?"
        "I'll miss her.":
            him "I'll miss her."
            her "Me, too."
        "Farewell to a great leader.":
            him "Farewell to a great leader. She loved and worked hard, even for people who didn't agree with her."
            her "Yes . . . I want to be more like that."
        "I'm not going to die like that.":
            him "I'm not going to die like that. And you better not, either."
            her "We all have to die sometime . . . I'd never thought about you dying before."
            him "What would you do if I died? Go back to Earth? Would you get married again?"
            her "I don't know... I'm tied to this planet, now -- too many people need me."
            him "We both have a lot of people depending on us, don't we?"
            her "Yeah, so you better stay healthy! No dying!"
            him "You're not allowed to die yet, either."
            "We joked about it, but inside I was terrified that [her_name] would die and leave me a single dad of two kids. There was no way I could be everything for them on my own."
            him "I love you, [her_name]."
            her "I never get tired of hearing you say that."
            him "Don't you mean, 'I love you, too'?"
            her "I love you, too, [his_name]."
        "(Don't say anything)":
            "I didn't say anything, just sat and held [her_name], both of us lost in our own thoughts."

    # Dr. Lily has a stroke and worries about her progress being lost if she should die.
    # should this go in the next event? what happens if she left with the luddites?
#    "About a month later, Dr. Lily had a stroke."
#    "She announced that Miranda would be the new head scientist."
#    "Miranda had been working with Dr. Lily for the last ten years or so."
    # Miranda Peron (now about age 26) steps up to take Dr. Lily's spot. She had been studying with Dr. Lily before."
    return


label community16:
    $ talked_paid_c16 = False
    $ talked_discoveries_c16 = False
    $ talked_family_c16 = False
    $ talked_TJ_c16 = False
    $ talked_Lily_c16 = False
    scene farm_interior with fade
    show him normal at midright
    "It's a beautiful day out. [her_name] is on her way home for a quick lunch."
    show her at midleft
    her "Thanks for making lunch for us."
    him "No problem. I was outside weeding anyway; it wasn't much trouble to pick some vegetables."
    her "I just got a call from Helen... Pete is really sick."
    show him surprised
    him "Are they going to bring him in?"
    her "Yes. I told them that I would treat him like any other colonist."
    her "But I asked them to pay with some food, and they want to donate a calf."
    show him concerned
    him "But after they left us... is it really okay to act like nothing happened?"
    her "I'm not acting like nothing happened. I'm acting like any empathetic human would and trying to take care of our friends."
    "How did I feel?"
    menu:
        "Do everything you can for Pete.":
            him "Do everything you can for Pete. He's an important part of our community."
            him "We'll lose a lot of hands-on knowledge about cattle if he dies."
            her "I wasn't asking your permission, but I'm glad to know you agree with what I'm doing."
            $ luddites += 1
        "Don't use important resources on him.":
            him "Try to see if you can treat him without using up our medical supplies."
            her "Um, they already tried that. He needs medicine."
            him "I just don't want to use up medicine on someone who left the colony."
            her annoyed "I don't care where someone's from or what they've done; I'm going to give everyone the treatment they need."
            $ miners += 1
    her "I'm sure Pete has learned a lot about survival on Talaam since he left."
    her "You should talk to him while he's in for treatment."
    him "Okay, I can at least do that."
    "That evening I visited the hospital after [her_name] came home."
    scene hospital with fade
    show pete at midright
    show him normal at midleft
    him "So how's it going?"
    pete "Things are both harder and easier away from the colony."
    pete "I feel better about how I'm living though, so it's worth it to me."
    him "Does it look like you'll recover?"
    pete "Yeah, [her_name] just said it was probably an infection that will go away with some antibiotics."
    label c16_convo:
    "What else should we talk about?"
    menu:
        "How will you be paying for your treatment?" if not talked_paid_c16:
            him "I hope you're giving us something in return for that medicine."
            pete "Don't worry! I brought a calf with me. We dropped her off with the herd on our way in."
            $ talked_paid_c16 = True
            jump c16_convo
        "Have you made any discoveries?" if not talked_discoveries_c16:
            him "Did you find any more weird plants and animals out there?"
            pete "Mostly the same ones. There are some bugs I hadn't seen before that look kind of like pill bugs."
            pete "I've been working on some other ways to deflect radiation though!"
            him "Really? It seems like you wouldn't have the technology..."
            pete "Well, I had been working on it before I left. I found out that the shells of all these animals are resistent to radiation."
            him "Huh. Makes sense."
            pete "The main problem is that the shells are brittle, so I can't bend them into other shapes, but I've been experimenting with different treatments for them."
            him "That's really interesting."
            #offer to help prototype
            $ talked_discoveries_c16 = True
            jump c16_convo
        "How is your family?" if not talked_family_c16:
            him "How do Helen and Travis like living in the wild?"
            pete "Helen misses her TV shows sometimes, but we've been singing and dancing a lot more."
            pete "I think Travis gets lonely, but he has plenty of work to help with."
            pete "He's been getting really into wood carving though. He made a really good crabird the other day."
            pete "We really miss some of the tools like shovels and hammers."
            pete "We've tried to make our own, but it's not the same."
            $ talked_family_c16 = True
            jump c16_convo
        "How are Thomas and Joanna?" if ((not asked_only_medicine) and (not talked_TJ_c16)): #this or the next menu option is the problem
            him "Are Thomas and Joanna enjoying it out there?"
            pete "They're not as into camping as I am. Honestly they seem pretty miserable sometimes."
            pete "I know they come back to visit family just about every week though."
            pete "I wonder how much longer they'll last."
            $ talked_TJ_c16 = True
            jump c16_convo
        "How is Lily?" if ((lily_mad_at_RET) and (not talked_Lily_c16)):
            him "Does Lily help out?"
            pete "Oh, she's great. She knows all the best foraging spots."
            pete "She's very concerned about radiation though, and never goes out of earshot of a radio for fear of a solar flare."
            $ talked_Lily_c16 = True
            jump c16_convo
        "Nothing else.":
            jump after_c16_convo

    label after_c16_convo:
        pete "I heard that Naomi passed on."
        pete "Things won't be the same without her."
        him "No, they won't."
        menu:
            "Had she been visiting you often?":
                him "Was she stopping by your place frequently?"
                pete "Yes, she was pretty worried about us. She stopped by at least once a week and sometimes twice."
                pete "It was really important to her that we knew that she still cared about us after we left."
                pete "She helped Travis practice foraging, and she showed me how to knit."
                pete "She'd bring little things for us to feel more at home."
                menu:
                    "So it's kind of your fault that she died.":
                        him "If she was visiting you that much, that explains why she died of radiation poisoning."
                        pete "We warned her to be cautious. It's not like we wanted her to die."
                        him "But if you hadn't left she wouldn't have gone to see you."
                        pete "If ya'll had been a little friendlier she wouldn't have felt so bad for us."
                        him "It's just hard to talk to you since you don't have a tablet."
                        pete "Our doors are always open."
                        him "..."
                        jump pete_neutral_c16

                    "She was good at that.":
                        him "She was always making something for someone's birthday or just celebrating some made-up holiday."
                        pete "That's true. When Travis found a grove of Ringlets, she made him a crown of leaves and called him the explorer prince."
                        him "She did something similar when Terra went a whole day without poking Oleg."
                        pete "What was her title?"
                        him "Overseer of Restraint."
                        pete "Ha. I doubt I would have even noticed something like that."
                        $ style = get_parenting_style()
                        if (style== "authoritative"):
                            him "I think I would notice!"
                        elif(style == "authoritarian"):
                            him "I might notice, but I doubt I would do anything."
                        elif(style == "permissive"):
                            him "I don't think not poking Oleg would ever happen under my watch."
                        else:
                            him "Yeah, I wouldn't notice either"
                        pete "It's been real good talking to you."
                        pete "Come see us sometime after I get healthy!"
                        pete "Bring some vegetables and we can slow-roast some beef."
                        menu:
                             "Sure.":
                                 him "That sounds amazing. I'll be over right away."
                                 pete "See you soon."
                                 $ luddites += 1
                             "I'm busy.":
                                 him "As tempting as that is, I can't spare any time away from the farm."
                                 pete "Come on."
                                 him "I've got more crops to raise with the miners and all. Sorry."
                                 pete "Guess I'll see you next time I have a life-threatening illness."
            "(Say nothing)":
                him "..."
                jump pete_neutral_c16
    label pete_neutral_c16:
        pete "Can't wait to get back to my cattle."
        pete "Thanks for stopping by, I guess."

    return


label community17:
    "It's time for the harvest festival! Usually we eat a big meal and the kids go around begging desserts off everyone."
    "This year I'm in charge of inviting guests. Who will I invite?"
    menu:
        "The miners and the luddites." if ((luddites >= 7) and (miners >=7)): #TODO: make sure it's possible to get this option
            $ invited_luddites = True
            $ invited_miners = True
            jump ludditesandminers
        "The luddites." if (luddites >= 7):
            $ invited_luddites = True
            jump justluddites
        "The miners." if (miners >= 7):
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
        "I write an e-mail to Dr. Lily asking if she has any pictures." #but only if lily went with them? maybe she should go either way?
        if lily_mad_at_RET:
            "She responds via the instant messaging software. Guess she hasn't given up all technology."
        else:
            "She still lives in the colony, but she's been hanging out a lot with Pete to study local flora and fauna."
        lily "I don't have a camera capable of taking photos underwater, but here are some photos of the animal out of water."
        lily "On Earth, jellyfish span various families of creatures, so I think it's safe to call this a kind of jellyfish. But they have five tentacles, so I've been calling them jellystars."
        lily "The creatures are very popular here and children and adults have been drawing them and incorporating their likeness into jewelry."
        "I feel relief just looking at the photos of the creature out of water and the drawings."
        "I start making my own drawings, and send a few back to Lily."
        lily "Did you eat some of this jellystar at the feast?"
        him "Yes, I did. Are they in season?"
        lily "I find your interest in them highly unusual."
        him "Why? Aren't they beautiful creatures?"
        lily "Yes. They are."
        return
    else:
        return

    #more likely to take a later risk if you have the parasite? doesn't have to be just like toxoplasmosis.
    # also if you meet with the luddites, Pete can answer questions about cattle health.
    # if BOTH luddites and miners are there, they start trade negotiations? affects the fire grass event later.


label community18:
    $ c18_waited = False
    $ c18_cows_in_ranch = False
    $ c18_cows_in_street = False
    nvl clear
    natalia_c "there are three stray cattle in my yard eating my crops... I've been trying to scare them away but it's not working."
    if thuc_has_cattle:
        natalia_c "Thuc, did your cattle get out?"
        thuc_c "No, it must be some other cattle!"
    else:
        natalia_c "Ilian, did the cattle get out or something?"
        ilian_c "No, those must be Pete's."
    natalia_c "Any advice on how to scare them away?"
    ilian_c "Yell at them and wave your arms."
    natalia_c "Tried that."
    thuc_c "I didn't hear you so I don't think you're yelling loudly enough!"
    natalia_c "Come over and do it yourself if you like."
    natalia_c "Nevermind, they're coming to you!"
    thuc_c "My fence is goatproof and cattle-proof. Looks like they're after [his_name]'s crops now."
    "My fence isn't robust enough to protect against cattle. I run out to the front yard."
    him "GO HOME COWS! KEEP MOVING!"
    him "YOU DON'T WANT ANY OF THIS TERRIBLE FOOD."
    "They look a little scared, but they start creeping back as soon as a turn my back."
    label cow_options:
        "How will I handle the cows?"
        menu:
            "Herd them to our ranch.":
                "I hop on Lettie and herd the cows over to the ranch."
                "The cows are nervous, but I calmly block their way if they try to escape."
                "It took a few tries to get them to go the direction of the ranch, so I bribed them with a little of Lettie's hay. They seem skittish."
                "A few of them seem to recognize the ranch when we get there and it's easy to let them into the herd."
                if thuc_has_cattle:
                    nvl clear
                    thuc_c "What are Pete's cattle doing out here? I thought he and the others were camped by the sea."
                    him_c "That's where they stay in the rainy and cold months. It's warming up again so they're headed inland."
                    natalia_c "Those cows ate a whole row of crops before I noticed them. He should compensate me for my losses."
                    him_c "Thuc, I herded the escaped cattle into the ranch with yours."
                    thuc_c "Oh, um... that was a good idea, but how are we going to tell them apart when we find Pete?"
                    him_c "Pete's cows are wearing bright blue blankets, probably to protect them from sunburns."
                else:
                    nvl clear
                    thuc_c "What are Pete's cattle doing out here? I thought he and the others were camped by the sea."
                    him_c "That's where they stay in the rainy and cold months. It's warming up again so they're headed inland."
                    natalia_c "Those cows ate a whole row of crops before I noticed them. He should compensate me for my losses."
                    him_c "Ilian, I herded the escaped cattle into the ranch with yours."
                    ilian_c "NOOOOOOOOOOOOOOOOOOO"
                    ilian_c "Quick, see if you can separate them while you still can!"
                    him_c "They're pretty easy to spot. They're wearing bright blue blankets, probably to protect them from sunburns."
                    ilian_c "But they might have parasites or bad habits!"
                    ilian_c "Please separate them somehow. Put them into the barn or something."
                    him_c "Sorry, I don't think I can do that. Hopefully Pete can sort it all out soon."
                    $ c18_cows_in_ranch = True
            "Feed them something so they won't eat my plants.":
                "I take out some of Lettie's hay and feed it to the cows, who happily dig into it."
                "Hopefully that will last long enough for me to find Pete."
                $ c18_cows_in_street = True
            "Wait to see if someone comes for them." if not (c18_waited):
                "I stand guard in front of my house and wait for something to happen."
                "I yell at them whenever they come near, and they start going the other direction."
                "Hmm. This isn't working."
                $ c18_waited = True
                jump cow_options

    "I go out to the miner's camp on Lettie with my binoculars to look for Pete."
    brennan "Hey, we had a few cows come through our settlement about twenty minutes ago."
    brennan "They ate up half of our herb garden."
    brennan "Whose cows are these?"
    him "Well, we think they must be Pete's, because all of ours are accounted for."
    him "I was actually trying to find Pete to ask him about this."
    # Pete comes running in, breathless and sweaty
    pete "Yep, these're my cows. We ran into a swarm of land lobsters while trying to get back to the summer pasture and the herd split."
    pete "The larger part of the herd is happily grazing about a half mile down the river."
    pete "[his_name], you and your horse are just what we need. Can you help me herd the stragglers?"
    brennan "Yes, please, get these cows out of here."
    "Should I help herd the cows?"
    menu:
        "I can help.":
            $ luddites += 1
            $ miners += 1
            him "Sure thing." #make this a choice as well?
            "We work together to herd the cattle into a group."
            if c18_cows_in_ranch:
                him  "I found three of your cows and herded them into the old ranch."
            else:
                him "Three of your cows are eating hay in front of my house."
            pete "Let's pick them up on the way out."
            "Some of the cows were lying down, and we had to wait for them to get up and stretch out."
            pete "Don't push them too hard. They'll get stressed out and are more likely to bolt when they get the opportunity."
            pete "I'm pretty slow, but I know where we're going, so I'll take the front."
            "Eventually, the stragglers joined the rest of the herd."
            pete "Thanks [his_name]."
            pete "I have a cow that is on her last legs. I'll bring her to the butchery and give out some meat as an apology for the trouble."
            him "That would be a good idea."
            "We spent the next month enjoying steak, beef stew, and beef jerky."
        "No, I don't want to.":
            $ c18_no_help_pete = True
            him "Sorry, I can't help you right now. I need to get back to the farm."
            if c18_cows_in_ranch:
                him  "I found three of your cows and herded them into the old ranch."
            else:
                him "Three of your cows are eating hay in front of my house."
            him "Keep better track of your cows, Pete."
            pete "Can I use Lettie to herd them?"
            him "No, I don't let just anyone ride her."
            pete "You're not gonna help one bit?"
            him "No, I'm not."
            pete "I won't forget this."
            if (luddites <= 5):
                him "You need to compensate the miners and colonists for the losses they incurred."
                pete "You need to stop being a jerk."
            "Pete spent all day gently walking his cows out to the pasture land half a mile from the colony."
    return


label community19:
    #you could substitute Pete for Helen in this scene; I just wanted to give Helen some more screen time.
    her "Hey, I told Sara that we could bring something to dinner this weekend."
    her "I know that the fall harvest isn't quite ready yet... can you get some of that wolf slug meat from Pete?"
    him "Sure. Helen usually comes through town on Tuesday selling it."
    her "Oh, so Helen can sully herself with credits instead of Pete trading this and that."
    him "I don't mind. Credits are so much more convenient."
    her "But they're also completely abstract. A credit only represents something because we decide it's valuable."
    him "The same could be said of any object that we sell."
    her "Tell me that when you're hungry! I budgeted up to 20 credits for meat or protein, so see what you can get."
    "That Tuesday I saw Helen coming through town with a large backpack of wares to sell."
    "She had made some chimes out of hollowed-out branches and bull horns that hung from the pack to give an audible signal of her passing."
    "Scarfs and gloves with jellystar patterns on them hang from the top."
    him "Hey Helen! Got any wolf slug meat?"
    helen "Yes, I've got some. It'll cost you though--we only found one this week and it was pretty young."
    him "How much?"
    if c18_no_help_pete:
        helen "80 credits."
        him "Hmm. That's outside my price range. Got any beef bones or beans?"
        helen "Nothing like that."
        if ate_jellyfish:
            him "How much for this jellystar scarf?"
            helen "40 credits."
            him "Augh, it's so cute. Guess I have something to save up for."
        else:
            him "Okay then. See you later."
        "Helen continued her circuit through the colony, stopping to chat to a few people and sell them food."
    else:
        helen "40 credits."
        him "Hmm. That's a lot more expensive than it was before."
        helen "Wolf slugs are getting harder to find."
        him "That's so frustrating. I finally figured out how to prepare them so they kind of tasted like clams."
        helen "That's why we were hunting them so much. They're really good."
        helen "I think the population is dwindling though, so we should probably stop killing them for now."
        him "Got any other meat?"
        helen "Just a few bits of jerky."
        him "That's fine. We can rehydrate it make soup with it."
        helen "15 credits."
        him "Okay, I made the transaction. Here, you can see it on my tablet."
        helen "Looks good. Enjoy!"
        if ate_jellyfish:
            him "Also, how much is the jellystar scarf?"
            helen "It's 30 credits, but for you I could go as low as 25."
            him "Hmm. I'll take it. And do you have any of that jellystar food?"
            helen "Here you go. We stopped eating the jellystar. They're too cute to eat!"
            him "Yeah. See you next time."
        else:
            him "Have a good one!"

    "A few weeks later, we were all gearing up for the fall harvest."
    her "I love this time of year. Harvesting food together makes me feel like we'll live another year."
    her "It does seem more efficient to stagger the crops though."
    him "Yeah, Tomas Peron likes to get his whole family to help plant, which makes it easier to manage, but also harder to harvest."
    him "He said that the corn should be ready in five days. Can you get work off?"
    her "Yeah, I don't have any appointments since everyone else is helping with the harvest!"
    her "And if someone gets injured I'll be right there!"
    "The next day I was checking my messages at breakfast when I saw Natalia posting on the community chat."
    nvl clear
    natalia_c "Thank you everyone for your willingness to help with the harvest, but we won't be needing any extra hands on Wednesday."
    natalia_c "Last night a giant flock of crabbirds came and ate almost all of the corn."
    natalia_c "I know that many of you were depending on our corn to feed your livestock over the rainy season. I'm sorry this happened."
    thuc_c "Wow, that is devastating news."
    nvl clear
    thuc_c "Ilian, do you know if we have enough food stored to make up for this?"
    ilian_c "I'm doing the calculations right now."
    him_c "Aren't there patches of wild alfalfa we could feed them?" #I haven't figured out why they can't do this.
    thuc_c "The wild alfalfa is too far away, and it starts dying as soon as the rainy season starts. Plus it's mixed in with native weeds."
    her "What's going on? Some exciting gossip?"
    him "Crabbirds ate all the Peron's corn, so we won't be harvesting it together."
    her "Whaaaaat? What will the cows eat all winter?"
    him "That's what everyone's wondering. Maybe they can increase the amount of alfalfa in the feed?"
    her "I wonder why there were so many crabbirds. We've never seen this many before, have we?"
    him "Who knows. Maybe since they've been eating our crops, they've been able to reproduce faster."
    her "But wouldn't that mean that their natural predators could eat more of them?"
    him "Huh. I wonder what the natural predators of the crabbirds are."
    her "Well, it's not the land lobsters, because they eat smaller things, right?"
    him "Yeah. I think they are mostly herbivorous."
    her "Maybe... some kind of larger bird that we haven't seen before?"
    him "I think we would have noticed a larger bird by now."
    her "oh..."
    him "Oh?"
    her "I bet it's the wolf slugs."
    him "That makes a lot of sense."
    ilian_c "If we keep feeding the livestock at the same rate as before, we need to lose four cows."
    if thuc_has_cattle:
        thuc_c "Ouch. That's going to impact our herd next year. Maybe I'll make a bunch of jerky."
        if is_liason:
            "{i}Wait. Should we use this as an opportunity to build our relationship with others?{/i}"
            menu:
                "Let's give them to Pete.":
                    $ luddites += 1
                    him_c "Let's give the cows to Pete. His herd seems to be surviving off of nearby rangelands"
                    thuc_c "Are you sure? Cows are worth a lot of money. I'd rather sell them."
                    him_c "You could try that. If you have a bunch of meat all at once, we're not all going to be able to buy it, so keep that in mind."
                    thuc_c "Good point."
                "Let's butcher them, but give a lot of the meat to the miners.":
                    $ miners += 1
                    him_c "We don't need to make it all into jerky. Let's give a bunch of it to the miners."
                    thuc_c "These are my cows you're giving away! And the miners are rich!"
                    thuc_c "I'll offer them a special deal though."
                "Let's keep the meat.":
                    $ colonists += 1
                    him_c "Jerky sounds good. But give me some of the fresh meat before you make it!"
                    thuc_c "Will do."
        else:
            him_c "Jerky sounds good. But give me some of the fresh meat before you make it!"
            thuc_c "Will do."
    else:
        ilian_c "What should we do with those four cows?"
        if is_liason:
            "{i}Wait. Should we use this as an opportunity to build our relationship with others?{/i}"
            menu:
                "Let's give them to Pete.":
                    $ luddites += 1
                    him_c "Let's give the cows to Pete. His herd seems to be surviving off of nearby rangelands"
                    ilian_c "I've been investing quite a bit of credits into these cows. I'll see if Pete wants to buy them though."
                    him_c "Okay. I know that you think you could make jerky out of all of them, but we only want to consume a certain amount of jerky..."
                    ilian_c "Right. I know the basic principles of supply and demand. I'll offer them at a steep discount."
                "Let's butcher them, but give a lot of the meat to the miners.":
                    $ miners += 1
                    him_c "We don't need to make it all into jerky. Let's give a bunch of it to the miners."
                    ilian_c "From the miners' standpoint, we're the ones who are the poor credit-grubbers."
                    ilian_c "I'll offer them a one-time special discount on bulk purchases."
                "Let's keep the meat.":
                    $ colonists += 1
                    him_c "Let's butcher the cows. But give me some of the fresh meat before you make it all into jerky!"
                    ilian_c "Don't worry, I will!"

        else:
            him_c "Let's butcher the cows. But give me some of the fresh meat before you make it all into jerky!"
            ilian_c "Don't worry, I will!"
    nvl clear
    natalia_c "The crabbirds are still around... what are we going to do about them?"
    julia_c "Maybe we could make nets or traps for them."
    sara_c "Oooh, I love crabbird chowder!"
    ilian_c "I do have a yearly stipulation of credits from RET for helping with emergencies..."
    ilian_c "If you process your crabbirds in the cannery, I promise we'll pay a good price for them."
    natalia_c "Since everyone was making arrangements to help with the harvest on Wednesday anyway, let's hunt crabbirds that day instead."
    "We all spent the day hunting crabbirds. Since none of us were very experienced, we didn't catch very many, but Tomas was able to trap a lot of them that week."
    #no follow-up on wolf slug hunting? maybe in a later event?
    return


label community20:

    if lily_mad_at_RET:
        "Pavel called me in to meet with him."
        him "Hi Pavel. How can I help you?"
        pavel "Dr. Lily's health has been declining and she doesn't think she'll last much longer."
        pavel "She wants to move back to the colony."
        pavel "We don't have a precedent for this situation. What do you think RET would want?"
        him "Hmm. I haven't heard much from them so I assume they're happy."
        if luddites > 10:
            him "We could ask them, but if they say no, would we really want to turn Dr. Lily away?"
            pavel "That's true, but we're setting a precedent here. What if in 80 years, the luddites are 15-20 people and suddenly want to join back with us?"
            him "That doesn't sound like a problem."
            pavel "Well, it's like RET is rehiring them, since we grow food for the miners and for ourselves."
            him "They could live near us and not work for RET."
            pavel "But what about treating their illnesses and letting their kids in our school?"
            pavel "RET isn't sending enough materials to support additional people."
            him "I think we should let Dr. Lily move back. That way she'll share more information with us."
            him "We have everything to lose and nothing to gain by denying her return."
            pavel "Very well. I'll tell Dr. Lily that she can return."
            jump lily_return
        else:
            him "I'm a strong believer in communication, so I'll ask."
            him "I'll message you when I hear from them."
            pavel "The sooner I know, the better."
            "I write a quick insta-comm from my tablet and head over to the transmitter to send it."
            # "Dr. Lily wants to return to colony. OK?"
            "Later that day I check to see if they responded."
            #TODO: letter style for their reply
            $ style = get_parenting_style()
            if (style== "authoritative"):
                "She may stay as a guest but not as a resident, and she must share her findings from her research."
                him "Sounds fair to me."
                "I sent Pavel a message with RET's requests."
                pavel "I'll pass this on. It sounds like calling her a guest is their way of acknowledging that she left."
                jump lily_return
            elif (style == "authoritarian"):
                "Don't allow her to return."
                "I told Pavel that RET didn't want to let her to come back."
                pavel "I was afraid of that. Well, do you want to let her back or not?"
                menu:
                    "Let her come back":
                        him "I think RET is being unreasonable. We should let her back anyway."
                        him "She's already sacrificed so much for the colony."
                        pavel "I agree. But I don't know if RET will be happy if they find out."
                        him "Right. If."
                        jump lily_return
                    "Don't let her come back.":
                        him "I think RET made it pretty clear that we shouldn't let her back to the colony."
                        pavel "Okay. I'll send her a message telling her as much."
                        jump lily_not_return
            elif(style == "permissive"):
                "Yes, of course let her back!"
                "I told Pavel that RET wanted her back."
                pavel "I'll tell her what you've decided."
                jump lily_return
            else:
                "They never responded."
                "What should I decide on?"
                menu:
                    "Let her come back":
                        him "RET never got back to me, but I think we should let her come back to the colony."
                        him "She's already sacrificed so much for us."
                        pavel "I agree."
                        jump lily_return
                    "Don't let her come back.":
                        him "I never heard back from RET, so I don't think we should let Lily back."
                        pavel "Really? Why not?"
                        him "It just seems safer not to let her back. You know, uphold the status quo until you hear otherwise."
                        pavel "Okay, if that's what you think is best."
                        jump lily_not_return

        label lily_return:
            "Lily moved in with her former lab assistant, Miranda Peron."
            "One day she called me in to the lab."
            him "Hello Dr. Lily. Welcome back!"
            lily "Thank you. I still do not approve of RET's practices, but I do not believe they felt the gravity of my protest."
            lily "However, thanks to spending more time in the field, I have made many more observations about the flora and fauna of this planet."
            him "Are you going to publish them?"
            lily "Some of my observations have led to theories, but I have not yet tested them."
            lily "I would like to tell you some of my theories."
            jump research_briefing

        label lily_not_return:
            "A few months later I heard from Pete that Dr. Lily had disappeared."
            "They found her clothes on the seashore."

            return

    else:
        "Dr. Lily called me in to meet with her."
        him "Hello Dr. Lily. How can I help you?"
        lily "As you might know, I've had some health problems in the past ten years."
        him "Actually I didn't know that. I'm sorry to hear it."
        lily "Oh. Well, several years ago, I had a heart attack, but I was able to recover fairly quickly, thanks to the many people who came to my aid."
        lily "I had to relearn how to speak. And I've had a droopy eyelid on my right side ever since."
        him "Yeah, I guess it just didn't come up! There were times where [her_name] was really busy and I was really busy and I didn't even check the message board."
        lily "In any case, I feel that I am not going to be around much longer."
        him "Okay..."
        lily "Miranda knows about our research, but there are a few things we're working on that I wanted to tell you personally."
        jump research_briefing

    label research_briefing:
        lily "I've found that a certain flower turns purple several minutes before a solar flare."
        lily "I've tried to isolate the color-changing compound, but have had little success."
        lily "For now, the easiest way to enjoy this technology is to simply plant this flower in areas where people may need another method of detecting solar flares."
        lily "Pete plants them in all his fields, and I think they would be useful in every farm and in recreation areas."
        him "That does sound like a useful plant."
        lily "Here are some seeds. It's fairly common in higher elevations."
        #TODO: make this a variable that affects a future event

        if ate_jellyfish:
            lily "I suspect that the jellystar creature you ate contains a parasite that affects human brains."
            him "And you just let Pete serve it to everyone?"
            lily "I have a suspicion, but no proof. Your fondness for the jellystar seems harmless."
            him "Huh. I just assumed everyone liked them. Come on, they're like the mascot of this planet!"
            lily "They are indeed beautiful. The way they can aggregate and form larger creatures is remarkable."
            him "They... combine to form a bigger animal?"
            lily "Yes, Earth has a few examples. The Portugese Man-of-War is technically an aggregate of many smaller animals."
            him "Huh."
            lily "But unlike the Portugese Man-of-War, these jellystars have a nervous system in aggregate."
            lily "They are constantly sending out synaptic impulses into the ocean to find each other."
            him "That sounds really inefficient."
            lily "It is, but somehow it works. The aggregate is intelligent, but I haven't been able to test how intelligent."
            lily "The open ocean on Talaam is essentially unexplored."
            lily "You should know one more thing about that parasite. It may affect reaction speed."
            him "Is that what you were testing when you went around throwing things at everyone?"
            lily "Yes, I did that to see if it was worth investigating. I asked [her_name] to disclose anonymous results of the yearly physical, and each year after the harvest festival, several people had a sharp dip in reaction times."
            him "I think we should stop eating it."
            lily "Wait until I finish the paper. It's only a few milliseconds of difference."

        else:
            pass

        if cave_explored:
            lily "We have been able to breed the cave newts in captivity."
            lily "We did tests on their skin secretions, and they are remarkably resistent to radiation."
            lily "We have been able to isolate the radiation-resistant compounds. For now, we are unable to duplicate them."
            lily "However, if we continue breeding the newts, we can harvest enough of their skin secretions to make a salve that will protect the wearer from radiation for 12 hours."
            him "Wow. That's fantastic."
            lily "We're also looking into applications to fabrics, but unfortunately they all wash out."
            lily "It's definitely research worth funding."
            him "Oh, undoubtedly. I think we all agree on that."
            lily "I'm glad you feel that way."
        else:
            pass

        "A few months later, Dr. Lily disappeared on a visit to the ocean."
        "Miranda said that she wanted to see the ocean one last time before she died."
        "We never saw her again."

    return


label community21:
    "It's predictably overcast this time of year. Lots of people go camping now since there isn't as much danger from solar flare radiation."
    thuc "A big group is headed to the seashore this weekend. Want to come with your family?"
    him "Yeah, I need a change of pace. Are any of your kids staying behind? I just need someone to take care of a few things while we're gone."
    thuc "Sure, send Gardenia a message. She's staying with Miranda while the rest of us explore."
    him "Who else is going to be there?"
    thuc "I think Kevin and Zaina are going too."
    him "Anyone else?"
    thuc "Yeah, Brennan and some of the miners are going too. And I think Pete might be camping over there now, so it'll be one big party!"
    him "Ugh. Brennan."
    thuc "He can be kind of funny."
    him "I don't trust him."
    thuc "It's not like you're entrusting your farm to him! Just tolerate his presence."
    him "Okay, whatever."
    thuc "We're going to form a caravan up at the fork in the road near the miner's camp."
    "My family was really excited to see the ocean, even though it would take about a day of walking to get there."
    "We met at the appointed time and place, with rations and blankets in our backpacks."
    brennan "Thanks for coming out to this joint miner-colonist outing! I'll be laying down a few ground rules."
    brennan "First, always stick with a buddy while we're traveling to the ocean."
    brennan "Don't eat anything unless you are certain it's edible."
    brennan "When you pee, make sure you're far from the river or food. And no smoking in tents!"
    "We started walking along."
    her "Wow, it's been so long since I've been this way! I don't think I've been to the ocean since before [her_name] was born."
    her "There's a path here and everything."
    kevin "Yes, I like to visit the ocean at least once a month. And Pete and his cattle are excellent at making a pathway."
    him "Pete comes through here?"
    kevin "Yeah, his family winters near the beach." #TODO: does the player know this some other way? can't remember
    "We had to climb through some rocky areas, but our progress was good."
    him "What's with the no smoking rule? I didn't know we had anything to smoke around here."
    kevin "Fire weed. It's a mild stimulant that the miners use to stay awake so they can work and extended period of time"
    kevin "It's stronger than caffeine and more habit-forming."
    kevin "Most miners only use it when they really have to stay up longer, but some smoke every day."
    him "And RET allows that?"
    kevin "To the miners, we are RET. And we don't have an office for the regulation of firegrass."
    her "Sometimes I wish we did... I've seen some of the effects of overdose and depedency."
    him "Huh. What are they?"
    her "Insomnia. Weight loss. That kind of thing."
    her "It hasn't killed anyone... yet."
    her "I think we should study it so that we can educate users about how to use it."
    her "It would be great if we could stop people from using it improperly... but we don't have the resources for that."
    kevin "Yes, and making drugs illegal and punishing people who use them works fantastically."
    him "Do the miners need to work such long hours?"
    kevin "That's up to Brennan, I think. And the individual miners."
    "Brennan did walk near us a few times, but I didn't feel like talking to him."
    brennan "Hi [kid_name], how are you doing?"
    kid "Who are you?"
    brennan "My name is Brennan. I help the miners keep on schedule."
    kid "Oh yeah, I've heard of you. It's your fault my friend's parents are always stressed out."
    brennan "That's one way of looking at it."
    kid "Dad says that you might talk pretty but that underneath you're like a snake."
    brennan "Really? I wonder what that makes you, then..." #is this too weird
    him "A mongoose."
    kid "What's a mongoose?"
    him "A cute, furry mammal that eats snakes."
    brennan "Interesting..."
    "We kept walking the rest of the day, chatting with each other while we walked."
    "We arrived at the ocean in time to frantically set up our tent before sunset."
    #line about what their kids are doing
    "The moon rose, and we saw glowing lights in the ocean from the jellystars just below the surface."
    if ate_jellyfish:
        "I felt a strange attraction to the lights, and watched them until I fell asleep on the beach."
    else:
        "They were beautiful to watch for a few hours while we set up a fire and warmed up food for dinner."
    "After a breakfast of soaked grain the next morning, I smelled a smoke that reminded me of curry. It was just some of the miners smoking firegrass in pipes though."
    "We spent time playing on the beach, even though it wasn't especially warm."
    "Some people caught fish or jellystars and tried cooking them."
    "Someone stepped on a sharp rock and [her_name] helped clean and bandage it."
    "That evening, Pete and his family stopped by."
    if luddites > 10: #TODO: calibrate this number and others. don't make this event too easy to trigger.
        #maybe Travis should be in this event too?
        pete "Guess what! I have a two-way radio now. It turns out communication is good for business."
        him "Really? I thought you were all into a technology-free lifestyle."
        pete "I do want to limit my dependence on technology. But I can't ignore the fact that I also live in a community where other people want to help me sometimes."
        him "That will be so much more convenient than trying to hunt you down."
        pete "It's going to stay in our home base area, so it probably won't be me answering it, but we're going to see how it goes."
        pete "I bet you noticed that it's hunting season for the jellystars."
        him "Yes, it's beautiful."
        pete "It's even better up close. Would you and [kid_name] like to come out on the boat with me?"
        if ate_jellyfish:
            him "Yes, I would love to see them up close!"
        else:
            him "Is it safe?"
            pete "They never hunt during storms. And the sky looks clear."
            him "Okay."
        "[her_name] was a bit concerned but also excited when I told her about it."
        her "Have him take me out next if it's really cool."
        "We went out on Pete's little fishing boat, past the place where the waves started crashing."
        pete "You see that mountain? There's a fantastic cave there where we stay about half the year." #so do they spend winter or summer there? and where are the cows?
        "The lights grew bigger, and when we looked closely, we saw that the animals had a different shape."
        "They were about the size of a toaster. They had eyespots on the sides and tentacles at the opposite end, almost like a squid, only with a see-through shell."
        pete "Now for the fun part!"
        "Pete picked up one of the jellysquids and put it in a bucket in the bottom of the boat."
        "It kept glowing, and changed colors with Pete's touch."
        "At first, the colors changed rapidly."
        "Then words started to appear on its back."
        him "Are those...?"
        pete "Yes, they appear to be English words. I think someone must have lost one of the new waterproof tablets in the ocean."
        pete "They appear to have taught themselves word patterns. I don't think they understand what they're for though."
        kid "Oh, it's just like that game I used to play on my tablet. Here, you just have to..."
        "She moved the word around by touching a dragging it, just like you would on a tablet."
        him "That's... incredible."
        kid "It's not that hard."
        him "No, it's incredible that this animal is replicating the tablet's behavior."
        pete "Travis likes to catch one and sit with it on the beach for a few hours. He says it reminds him of when we lived in the colony."
        kid "That sounds fun. Can I play with it some more?"
        pete "Sure, I bet your mom would love to see it too."
        "When we came back we showed everyone the amazing animal, and [kid_name] demonstrated it to everyone."
        "I was worried about the animal's skin, but it had a shell made of glass, which was very resilient."
        "Brennan took a few photos. He seemed pretty interested in their shells."
        "After everyone had seen it, we let it go back into the ocean."
    else:
        "He chatted to a few people but I didn't get a chance to say hi."
        "The kids played with these weird transparent shells."
    if miners > 10:
        #put Chaco in here somewhere? we haven't seen him in a while
        brennan "Zaina and some of the miners caught a bunch of fish. Want to join us for a little roasting party?"
        her "I saw that earlier. They caught the edible ones? I'm surprised the jellystars couldn't get them all."
        brennan "I think she found a little enclave where it was difficult for the jellies to reach them."
        him "Hmm. As long as fish are the only ones getting roasted."
        brennan "That's up to you!"
        "We sat around eating fish with some flatbread that we cooked on hot stones."
        zaina "I should come here every year. I welcome this dietery variety!"
        brennan "It's nice to have some company. None of the miners want to hang out with their boss's boss."
        him "About that... do the miners have enough time to sleep and eat?"
        brennan "Honestly at this point they've met their quota for the year. The only thing motivating them now is the giant bonuses for more metal ore."
        him "It's not like we have a luxury good market here, so I guess the money they make here will translate into some kind of Earth currency?"
        zaina "Yes. Some of the miners come from incredibly poor backgrounds. They make more money in a day than they do in a month back on Earth."
        zaina "But most of them have gotten it into their head that if they just push themselves for another few years that they can help all their family get out of debt and retire early."
        him "And the fire grass just allows them to be more productive."
        brennan "I don't think it's worth the trade-off. For every extra night a miner works on fire grass, they need a day to recover and catch up on sleep."
        brennan "Most of the time they don't stay home. And they way some of them keep using it can't be healthy."
        brennan "I don't know what Pete is doing with all the credits he's amassing from selling it."
        him "He buys some expensive things, like medicine. But part of me thinks that he's just going to delete it all like some kind of anarchist."
        brennan "I don't care what he does with the money. I do wish that he'd have a dosage guide or something though."
        her "Hmm. I could make up something like that. We have a training program to help adolescents with alcohol use that I might be able to adapt to firegrass."
        her "And if it works, it will mean less work for me in the long run."
        her "But I need more information first. Do you have any idea how prevalent firegrass is?"
        brennan "Most of the miners have tried it at one point or another. I think five or six of them use it daily now."
        brennan "I can usually tell because they're extra grumpy the day after."
        brennan "Some of the teenagers who just started working are curious about it too, but I can't tell if they're just normally grumpy."
        her "Too true. A few of the miners have mentioned it to me. I can give out recommended doses and warn about side effects, but we don't really know what the long-term side effects are right now."
        brennan "Ultimately it's their responsibility."
        her "But we need to make sure they have enough information to make good decisions."
        if luddites > 8:
            pete "What's this I hear about regulating firegrass? Are you trying to reduce my income or something?"
            brennan "It's nothing personal. And telling the miners what a safe dosage is might actually increase their consumption."
            brennan "If I knew how much to take for a little pick-me-up that would still let me sleep at night I use it occasionaly."
            pete "Fair enough."
            pete "I have some yogurt here that would go really well on these fish."
            brennan "Yes, please share some! And take a fish in return. You seem to be familiar with them."
            pete "We usually spend part of the winter near the ocean. The mountain provides some shelter from storms and shade when it's sunny."
            pete "There's a big cave where we usually camp that is a wonderful shelter. There are holes in the top so we can have a fire, but it's enclosed enough that we don't need to worry about radiation."
            pete "The fish are easy to hunt here too, and their bones are good fertilizer"
            pete "The fish you found are actually part of one of my farming experiments... and it looks like it's working."
            pete "Please leave a few to keep reproducing."
            zaina "Oh, you're cultivating them. That explains why there were so many!"
            brennan "A few fish? Like, a male and a female?"
            pete "Actually these fish change sexes based on conditions. But if you leave 5-6 per pool that should be sufficient."
            him "That makes sense. Let's save the bones."
        else:
            "Pete came and asked to talk to Zaina. I couldn't hear exactly what they were talking about, but Pete looked mad and Zaina looked defensive."
            # zaina comes back
            him "What was that about?"
            zaina "Pete says that the pool of fish we found was actually a fish farm and asked us not to steal his fish."
            zaina "He said it was obvious they were being cultivated because there were so many in the pool."
            zaina "But seriously, how was I supposed to know? He wanted us to compensate him for the damages to his stock."
            "That sounds..."
            menu:
                "fair.":
                    $ luddites += 1
                    him "If you came to my farm and picked my tomatoes I would say the same thing."
                    him "It's only fair for us to compensate him for his work."
                    zaina "Okay, how much do you want to pay for the fish your family ate?"
                    him "I don't know, 10 credits? We'll think of something."
                    zaina "I'll pitch in 10 credits then."
                "absurd.":
                    him "There weren't any fences or signs posted."
                    him "How could he expect us to know about his fish farm?"
                    zaina "I know. He needs to realize that he doesn't own everything outside the colony."
                    brennan "He knows he doesn't own everything. But these fish were surprisingly easy to catch, right?"
                    brennan "Let's give him a few fossils or something when we get back. I'll talk to him."

    else:
        "[kid_name] caught a fish with Zaina, and we cooked it over an open fire."
        "It looks like the miners had the same idea. They got a huge bonfire going."
        her "Wow, that bonfire is huge! Let's go check it out."
        him "You can go on ahead. I'll stay here."
        her "I'll be right back."
        "[her_name] came back after a few hours. She smelled even more like smoke than I did."
    "The next day was more relaxing in the shade, playing with jellysquids, and catching fish."
    "I even taught [kid_name] how to swim."
    "We travelled back to the colony without incident."
    #TODO: Does this event need a choice?
    return


label community22:
    if (miners > 10) and (luddites > 9) and (is_liason):
        nvl clear
        brennan_c "Hi Zaina, Kevin, and [his_name]. I'd like to meet with you and Pete about how we can mine without disturbing the luddites' home."
        brennan_c "Except I don't know how to get ahold of Pete."
        him_c "Oh, he has a radio now. I can sort of text him with it."
        brennan_c "How 21st-century. Ask him if he can meet tomorrow evening at the canteen in the miner camp. Around 5pm, if he has a watch."
        him_c "Okay, I sent him the message."
        kevin_c "I am unable to attend, but Zaina will be there."
        "That evening, Pete replied to say he could make it."
        him_c "Pete can come. See you all there."

        "The next evening..."
        brennan "We've almost completely mined the rare metals from the first mountain."
        pete "It's not much of a mountain anymore."
        brennan "That is an unfortunate side effect of mining. A side effect which concerns you, because the next logical place for us to mine is a mountain near your wintering area."
        pete "This planet is so enormous. There must be some other mountain you can dig into."
        zaina "I've gone on several trips over the last few years to look for better prospects. The mountain near the ocean is our best prospect in a 50-mile radius." #I think the mountain should have a name.
        pete "You say that, but I can't help but feel that you're persecuting me and my family. I guess you're going to tell us we have to move now."
        pete "And you're in on this too, [his_name]? It figures."
        him "That's not why we're meeting you. We want you to show Zaina and Kevin exactly where you live so that they can avoid disturbing you."
        pete "Is that... right?"
        brennan "The mountain is enormous. Part of what makes it efficient is that our mining equipment is already close to it. But we don't need to mine the whole thing."
        pete "You say that, but you don't know how much of the mountain we live in."
        zaina "I thought you said it was one cave."
        pete "One main cave. I think you should see it before making any decisions."
        zaina "I'm always up for making informed decisions."
        him "I can't leave my farm right now, but I'm sure Zaina is up for the job."
        zaina "It shouldn't take more than a few days."
        brennan "While you're there, see if you can collect any shells from those tablet-like squids."
        zaina "Oh, the glass ones? Are you thinking they could have high mineral content?"
        pete "There are places where they're common. I can show you."

        "A week later..."
        nvl clear
        zaina_c "So, Pete wasn't kidding when he said that the caves are extensive."
        zaina_c "I think some kind of animal probably made them, because they are much bigger than most Earth caves."
        zaina_c "Maybe when this part of the planet was underwater? There were a lot of vertical tunnels that Pete has put ladders in."
        zaina_c "The caves penetrate about three-quarters of the mountain, but they are only using about half of the caves."
        zaina_c "Pete seemed to expect that we would make them move. But maybe we can work out a compromise."
        zaina_c "The whole mountain is scattered with silicon rock, whereas most other mountains only have a small percentage."
        brennan_c "It's tempting to ask him to leave. Let's see what RET thinks. [his_name], can you ask them if it's okay to only mine part of the mountain?"
        him_c "Yes, I can. I'll send the message at lunch."
        "That evening RET replied that our solution was fine and reminded us not to kill anyone." #could have parenting style affect this outcome, like with Dr. Lily's death
                   #"But I don't really want a group of displaced people to potentially sabotoge future mining projects." #do we need to contrast with his earlier opinion on caves?
        him_c "RET says it's okay to only  mine a portion of the mountain as long as we make sure it's safe for everyone."
        kevin_c "We need to do some explorational mining, but according to my calculations, we'll definitely be able to mine a quarter of the mountain without disturbing the cave system."
        brennan_c "That sounds like a good place to start. We'll be busy for the next few months refining our current ore. Start taking samples now to get a better plan."
        "The mining continues without incident."
        $ community_22_compromise = True
        # does this need a stat +=?
        return

    elif (miners > 10) and (luddites > 9) and not (is_liason):
        nvl clear
        sara_c  "Hi [his_name]. We need to talk to Pete about mining in his winter area. Do you know where he is right now?"
        him_c "Actually, he has a two-way radio now! I can sort of text him."
        sara_c "Great. Can you give me his frequency?"
        him_c "He might be more willing to answer if I ask him."
        sara_c "Tell him to meet us at the canteen in Brennan's mining camp tonight at 5pm."
        him_c "Done."
        "That afternoon, Pete responded that he'd go, and I conveyed his message to Sara."
        him_c "Are you going to be mining in the ocean?"
        sara_c "No, still the mountains. But Brennan said that he knows Pete has a cave over there, so he wanted to make sure not to collapse his cave during the mining."
        him_c "That was considerate of him."
        "The mining continued without incident."
        $ community_22_compromise = True
        #too facile?
        #stat +=?
        return

    elif (miners > 5):
        nvl clear
        if is_liason:
            brennan_c "Hi Zaina, Kevin, and [his_name]. I'd like to meet with you about our future mining prospects."
            kevin_c "I am unable to attend, but Zaina will be there."
            him_c "See you there."

            "The next evening..."
            brennan "We've almost completely mined the rare metals from the first mountain."
            brennan "The next logical place for us to mine is a mountain near the sea."
            zaina "I've gone on several trips over the last few years to look for better prospects. The mountain near the ocean is our best prospect in a 50-mile radius."
            brennan "That seems pretty straightforward. Do you have any concerns, [his_name]?"
            him "So far we haven't experienced any contamination from your ore-refining process."
            zaina "I'll go on an exploratory expedition then. It shouldn't take more than a few days."
            brennan "While you're there, see if you can collect any shells from those tablet-like squids."
            zaina "Oh, the glass ones? Are you thinking they could have high mineral content?"
            brennan "Could be worth investigating."
            "A week later..."
            jump Pete_stay_or_go

        else:
            nvl clear
            sara_c "Hey [his_name]. You knew Pete pretty well, right?"
            sara_c "Brennan is going to start mining in the mountain where Pete and the other luddites are living. Could you give us some advice on how to proceed?"
            sara_c "We're trying to decide if we could get him to leave or if we should cut our losses now."
            sara_c "I just added you to the chat."
            jump Pete_stay_or_go

        label Pete_stay_or_go:
            nvl clear
            zaina_c "The luddites are currently living in caves in that mountain."
            zaina_c "Pete wouldn't let me inside to explore them. He said that they weren't moving under any circumstance and that we should mine somewhere else."
            zaina_c "The whole mountain is scattered with silicon rock, whereas most other mountains only have a small percentage."
            brennan_c "There he goes, acting like he owns the place. Sheesh. I don't really want to force him out, but that mountain is the best place to mine."
            brennan_c "You know Pete, right? What approach should we take?"
        menu:
            "What should I recommend?"
            "Get him to leave.":
                him_c "I know Pete. He's stubborn. I don't think negotiation will get us anywhere."
                him_c "We're trying to run a business here."
                him_c "If he needs somewhere to live there are plenty of other suitable places."
                brennan_c "It still seems kind of harsh. Zaina?"
                zaina_c "I agree with [his_name]. There are plenty of other places to live on this planet."
                zaina_c "He doesn't need to stay in the one place he's obstructing our mining expedition."
                brennan_c "Okay, but how do we force him out?"
                him_c "Natural consequences?"
                brennan_c "It is not going to look good if they all die in a cave-in."
                him_c "Well, they don't spend all of their time in the cave. You can just mine that part of the mountain when he's summering inland."
                brennan_c "The passive-aggressive approach. Works for me."
                zaina_c "We should at least warn him, so he can decide to leave and move his posessions."
                brennan_c "Can you do that, [his_name]?"
                him_c "I don't have time to go personally. But I could write a letter."
                brennan_c "Good enough. We won't actually start mining for a few more months, since we are still processing all the ore we've dug up."
                "I wrote a letter to Pete, warning him that Brennan was going to mine the mountain and that he should leave."
                "A few months later, I saw Pete's herd of cattle off on the hills in his summer area."
                "He came through the village, selling various things, and spoke to me."
                him "Hello Pete."
                pete "Hello. I've been meaning to talk to you."
                pete "You are truly a traitor."
                him "What do you mean?"
                pete "Writing that letter to get me to leave my cave. There's no way I'm leaving."
                him "You're not there now..."
                pete "I'm not, but my family is!"
                pete "I'm telling you, there's no better place for us to live. The cave protects us from solar flares, but lets in enough light to see by."
                pete "There are so many other places to mine."
                him "But that mountain has the highest probability of having a lot of ore."
                pete "I don't care. We're not leaving."
                him "Then you'll die in a cave collapse."
                pete "Better than killing my friendships to serve some company."
                pete "What do you care if RET is slightly less efficient? It's not like money gets you much around here."
                him "Easy for you to say, when you have plenty of it!"
                pete "I'm not hoarding it. Anyone can grow firegrass."
                him "Yeah, but if we all start growing firegrass, we won't have vegetables to eat."
                pete "Fair point. But anyway, I think you guys are bluffing and I am not going to leave my home for RET."

                scene black with fade # convey passage of time with this?
                nvl clear
                brennan_c "Is Pete still in the cave? We started mining on the opposite side of the mountain but we'll be getting close to him soon."
                him_c "Yeah, he's still there. He thinks you're bluffing."
                brennan_c "Maybe I am. I don't actually want to murder him."
                kevin_c "Perhaps he needs encouragement through physical threats."
                menu:
                    "Is that what I want?" #should this be a choice?
                    "Yes, we need to be more forceful.":
                        him_c "I can get some guns from Ilian. Brennan, do you have some intimidating miners who could hold them?"
                        brennan_c "Intimidating, yes. But I don't know if I could trust them not to fire them."
                        him_c "I'll go with them then."
                        "I made arrangements for my farm for the next two days and picked up the guns. Then I met Brennan at his new camp about four miles away from us."
                        him "Okay Brennan, who's coming with me?"
                        brennan "Bandile and Chaco have agreed to come with you."
                        "On the way there, I told them our plan was to intimidate, not kill. I gave them both guns."
                        "After we got there, we couldn't find the cave entrance. We saw Helen, though."
                        helen "Travis, go find the little ones and stay inside."
                        him "Hello Helen. We're looking for Pete."
                        helen "What do you want with him? And why are you carrying those guns?"
                        him "Look, we're not here to shoot anyone."
                        "Before I could finish explaining, Helen kicked Chaco in the crotch and took his gun." #not sure how this should play out.
                        helen "We. Are. Not. Moving."
                        "She flicked off the safety and aimed the gun right at us. The small, usually timid woman had a righteous fire in her eyes as she prepared to defend her home and kids."
                        "Chaco must have sensed my apprehension, because he whispered."
                        chaco "Don't worry; it's not loaded."
                        helen "What?!"
                        "She opened the chamber to check for a round, and Bandile grabbed her arms while she was distracted."
                        "Helen started screaming, and Pete appeared from behind some rocks."
                        pete "What is going on here?"
                        pete "Let her go!"
                        him "Not until you promise to leave the caves!"
                        pete "Wow. Three against one. Is that how this works?"
                        pete "Fine. We'll leave the caves. Just give us five days."
                        him "Okay. Let her go."
                        "Bandile let go of Helen. She looked at me like I was vomit."
                        "The luddites left the caves and started a camp nearby. The mining proceeded, but suffered from so many mysterious setbacks and equipment malfunctions that they stopped halfway through and changed to a different location."
                        #TODO: expand?
                        $ luddites = 0 #or a large minus to the relationship
                        $ miners += 1
                        $ community_22_forced_luddites_leave = True
                        return
                    # "No, this isn't right. "
                    #     him_c "This is getting too intense. I don't think it's worth fighting over."
                    #     brennan_c "We've already starting mining the mountain though."
                    #     him_c "Well Pete isn't living in the whole thing. Can you just mine around him or something?"
                    #     zaina_c "If Pete would let me into the tunnels, we could be sure to avoid him. I just don't know how deep they go..."
                    #     brennan_c "We're making good progress right now. I'll have Zaina make some educated guesses, and we'll try not to kill anyone."
                    #     "A few of the deeper tunnels collapsed, but no one was hurt, and mining was otherwise unobstructed."
                    "Let's mine somewhere else":
#                        him_c "He's too stubborn to leave if we push him out."
#                        him_c "Let's mine somewhere else for now. Who knows, maybe in 15 years he won't even live there anymore."
#                        zaina_c "But that mountain is the best place for mining right now."
#                        brennan_c "I don't want to create an army of potential saboteurs by displacing the luddites."
#                        brennan_c "Let's find the next-best place and mine there."
#                        zaina_c "Alright. I'll send you the details."
#                        $ luddites += 1
#                        jump stopped_mining

#                        if luddites > 5:
#                            him_c "This is getting too intense. I don't think it's worth fighting over."
#                            brennan_c "We've already starting mining the mountain..."
#                            him_c "Well Pete isn't living in the whole thing. Can you just mine around him or something?"
#                            zaina_c "If Pete would let me into the tunnels, we could be sure to avoid him. I just don't know how deep they go..."
#                            him_c "Let me talk to him again. Maybe I can convince him to let someone in to document them."
#                            brennan_c "Go ahead. It would definitely set my mind at ease."
#                            "I convinced Pete to let Zaina image the caves, and they were able to mine around it without disturbing it."

#                            return
                            # should we allow the compromise ending here, or only in the "best stats" ending above?
                            # the other alternative is jump stop_mining, or not have this alternate to the choice
                        # TODO: you will never reach this because of the return above?
                        him_c "It's not worth fighting over."
                        brennan_c "It's not worth it to you, but it's worth it to me."
                        him_c "What have you got against Pete?"
                        brennan_c "It's nothing personal. We've already established that it's the most efficient place to mine for rare metals."
                        brennan_c "The more efficient we are at mining, the better chance RET has to support us for a longer period of time."
                        him_c "But we'll have to sacrifice our relationship to the luddites to do so."
                        zaina_c "It was their decision to leave the colony, and it's our decision to keep mining the mountain."
                        jump mining_anyway

            "Let's mine somewhere else":
                him_c "He's too stubborn to leave if we push him out."
                him_c "Why don't you mine somewhere else for now?"
                zaina_c "Other mountains aren't as dense with the rare metals we seek."

#                if luddites > 5:
#                    label stop_mining:
#                        brennan_c "I'm worried about what RET will say when I tell them we're changing mining locations..."
#                        brennan_c "But I also don't want to create an army of potential saboteurs by displacing the luddites."
#                        him_c "If RET gives you grief you can blame me."
#                        brennan_c "Will do. Let's find the next-best place and mine there."
#                        zaina_c "Alright. I'll send you the details."
#                        $ luddites += 1
#                        jump stopped_mining
#                        #does this seem too easy? maybe each stopped mining branch should also have the luddites vandalizing the equipment?

#                else:
                brennan_c "It's too risky not to mine it. We're going to continue whether they're there or not."
                brennan_c "It's not like the luddites have ever stuck it out for us."
                him_c "Not sure why you asked my advice if you're just going to do what you planned anyway."
                brennan_c "I thought you might have an idea of how to convince him to leave. He obviously doesn't need more money."
                him_c "I don't think anything you do would convince him to leave."
                brennan_c "Which gives me the information I need to carry on without wasting time on negotiation."

                jump mining_anyway

            "Don't make a recommendation.":
                him_c "You guys are on your own."
                him_c "I don't want any part of this."
                "I left the conversation."
                jump mining_anyway

    elif (luddites > 5):
        "Pete called me on the radio one evening."
        pete "We've been hearing and feeling explosions in the mountain a lot lately."
        pete "Are the miners working on our side of the mountain? Seriously, what's going on?" #or would his tone be more indignant?  YES
        him "That's possible. I know they finished mining in the mountain closest to us."
        pete "I am not moving. They can mine somewhere else."
        pete "The cave we have now protects us from radiation but lets in light through cracks in the sides."
        pete "The tunnels are large enough to move around in, and we store food and supplies here."
        pete "There's even a semi-covered area for the cows."
        pete "If they keep mining, someone's going to get hurt."
        him "Let me see what I can find out."
        nvl clear
        him_c "Hey Brennan. Are you guys mining in the mountain near the ocean?"
        brennan_c "Yeah, we started a few weeks ago. Why?"
        him_c "Pete lives in a cave in that mountain. He told me they've been feeling the blasts lately."
        brennan_c "Well, he should probably live somewhere else while we do the mining for safety reasons."
        brennan_c "They're kind of nomadic anyway, right? It seems like it would be pretty easy for them to move."
        him_c "I think they live in two main places, but Pete goes out camping with the cattle to graze them."
        brennan_c "Oh, I thought they all moved together with the cows. They do need to move though, because we are mining the entire mountain."
        him_c "But Pete was there first."
        brennan_c "Can he show me the deed to the land?"
        him_c "You know we don't have deeds for anything here."
        brennan_c "I think we've talked about this before. If we don't mine effectively, we'll lose RET's support. We need the medical supplies and materials they send us periodically."
        him_c "The luddites don't see it that way."
        brennan_c "I don't have much else in my persuasive arsenal. It's dangerous for them to stay, and leaving would help our entire community."
        him_c "Surely there are other mountains you could mine?"
        brennan_c "There are, but Zaina has been exploring and taking samples over the last few years. That mountain has the best chance of having the most rare metals for a 50-mile radius."
        brennan_c "I suppose if Pete let Zaina in the cave, we could see if the mining will actually endanger them or not... but I doubt he'd let her."
        him_c "Okay, okay. I'll talk to Pete, but no promises."
        "I tried paging Pete on the radio, but there was no answer."
        "I left him a sort of text message telling him to call me later."
        pete "So, what's going on?"
        him "You were right. The miners are digging in your mountain."
        pete "I knew it."
        him "I chatted with Brennan, and he said it's the most mineral-rich mountain in a 50-mile radius."
        pete "Really? So that's why I haven't found anything similar in all my travels..."
        pete "We still don't want to move."
        menu: #should this be a choice? or based on a lower level of relationship w/ miners?
            "What should I recommend?"
            "You should resist.":
                him "I don't think you should have to move."
                him "I think that if you refuse to move that they will have to work around you."
                pete "Hmm. So I should call their bluff?"
                him "Yeah. Plus I know you could do a lot of damage just by loosening a few bolts on their mining equipment."
                pete "So I'd be threatening them back, basically."
                him "You're the one who doesn't want to move. I'm just telling you one way I think you could stay."
                pete "I like the way you think."
                nvl clear
                him_c "Pete says he's not going to move."
                brennan_c "Well, he knows what's coming. This is on his head now."
                "A few weeks later, Brennan messaged me again."
                nvl clear
                brennan_c "Our mining equipment keeps breaking down and we suspect someone is sabotaging it."
                brennan_c "Some of the repairs have been seriously difficult to repair."
                brennan_c "Do you know anything about this?"
                him_c "I bet if you starting mining somewhere else it would stop."
                brennan_c "This is ridiculous. You're a traitor to our cause."
                him_c "I didn't have anything to do with it. [her_name] can tell you that I've been home every night for the past few months."
                brennan_c "It isn't worth it to keep mining over there if it jepordizes our chances for future mining."
                brennan_c "Hope you're happy!"
                jump stopped_mining

            "I don't think it's worth fighting over.":
                him "I know you don't want to move. But Brennan has made some good points."
                him "The better mining goes, the longer RET will support our colony by sending us medical supplies and other things we can't make here."
                pete "That's something I've been wondering about. Why can't we make those things here?"
                him "We don't have the infrastructure for it."
                pete "We would if RET would send it to us. They don't want us to be completely independent."
                if is_liason:
                    him "I'll ask RET about it and get back to you."
                    pete "I'd appreciate that."
                him "Maybe there's a different reason. But whatever it is, we can't change RET's mind right away."
                pete "Can they just avoid mining around our cave?"
#                if miners > 5:
#                    him "I think they'd need you to let them in your cave so they could know how deep it goes."
#                    pete "If that's what it comes down to, I think I can let someone in."
#                    "Pete let Zaina map his cave, and the miners were able to dig around it."
#                else:
                him "I don't know. Maybe if they were willing to go in and measure your caves, they would know enough to avoid them."
                pete "I don't think they care enough to make that kind of effort."
                pete "I could just stay here and hope it doesn't hurt us."
                him "That sounds risky."
                jump mining_anyway #the two branches aren't symmetric in possible endings... okay?

        label stopped_mining:
            "The mining stopped." #this can happen if you're not the liason, after the luddites vandalize mining equipment
            if is_liason:
                "I didn't mention anything to RET, but Brennan must have, because Mayor Grayson sent me an urgent message the next day."
                pavel_c "Please come meet me in my office today."
                him_c "Okay, what's is about?"
                pavel_c "I think you know..."
                "I guess RET probably wasn't happy that the mining had stopped."
                pavel "RET has asked me to designate a new liason."
                him "Okay. Fine."
                pavel "What did you think would happen? You didn't even consult them."
                him "I know what they would have said."
                pavel "But you have to let them say it. You're not the only one in contact with them."
                pavel "RET asked me to make the nominations for two candidates. I'm sending out a poll tonight to vote for the new liason."
                him "This will just help me focus on farming--the important work."
                "Sara won the most votes and became the new liason."

                $ is_liason = False

                jump sara_RET_22
                return

            else:
                label sara_RET_22:
                sara_c "Hey, RET is giving me grief because the mining stopped."
                sara_c "What's the big idea? Can we really not do anything?"
                him_c "Well, Pete doesn't want to move, so yes, we really can't do anything to get him to leave."
                sara_c "They're insisting that we resume mining."
                him_c "Tell them we can't because don't want to accidentally hurt the luddites."
                sara_c "And the equipment is getting mysteriously vandalized..."
                him_c "Right? It just isn't worth it."
                sara_c "RET wants to authorize use of force against anyone caught making unauthorized modifications to mining equipment."
                sara_c "There aren't any current plans do that."
                sara_c "Brennan doesn't want to do that and they're getting ready to mine in a different location."
                sara_c "RET isn't happy with us right now though."
                sara_c "They want the miners to make up for the delay and aren't changing their quota."
                him_c "I don't think we can do anything about that."
                sara_c "We can keep giving them food to eat, I guess."
                $ community_22_mining_stopped = True

                return


            #$ style = get_parenting_style()
           # if (style== "authoritative"):
           #     "Plz elect a liason 2 help RET & colonists communicate & resolve conflicts."
            #elif(style == "authoritarian"):
            #    "We need a designated contact with the colony that u trust. Send ur decision."
            #elif(style == "permissive"):
            #    "U shld choose some1 2 represent the colony 2 us."
            #else:

    else:
        #try to calibrate to make this end pretty rare. maybe just compare mining value to luddites in elif?
        "The miners started working in a different mountain this year."
        "It happened to be the same mountain that the luddites wintered in by the ocean."
        jump mining_anyway
        return

label mining_anyway:
    "Brennan continued with the mining even though the luddites were still living in the caves."
    "We were cleaning up after breakfast a few weeks later when we heard Pete on the radio."
    pete "[her_name], do you copy? Please, are you there? We have a medical emergency."
    her "I'm here. What's wrong?"
    "Pete sounds distraught."
    pete "Travis... he was up in one of the higher chambers whittling when the mountain started sh-shaking."
    her "Is he breathing? Does he have a heartbeat?"
    pete "He's alive and he called us for help. But he's completely stuck underneath a rock right now."
    her "See if you can keep him warm. Maybe a small warm-blooded animal could sneak back there?"
    her "The cave is probably unstable. If you try to get him out, you could make it worse or get stuck yourself."
    pete "There must be something we can do. I can't sit and watch him die."
    her "Don't try to move him until I have more information. I'll radio back to you in five minutes."
    "She turned the radio off."
    him "That did not sound good." #would Terra say something here too?
    her "No, it didn't."
    her "I need an expert opinion..."
    "[her_name] radioed Kevin and explained the situation. He was sympathetic and offered to go with her to the cave." #would Kevin be sypathetic? He suggests using force against them in a another option.
    "She told Pete about their plan and he agreed to let them come help Travis."
    her "I'll take the necessary medical supplies with me. It looks like I'll be gone the next two days, but we'll stay in contact over the radio."
    him "Good luck."
    "That night, she told me that Travis was still alive but his leg was probably broken. Kevin was taking measurements and gave some orders for miners on the other side to suspend operations while he worked."
    "The next morning, [her_name] said that they were able to extract Travis."
    "The damage to Travis's leg was bad enough that [her_name] wanted to do surgery."
    "After a day of recovery, [her_name] returned to the colony with Helen and Travis, who rode a cow since he couldn't walk."
    her "His tibia is completely shattered. After looking at the x-ray, I don't know if I can save it." #I tried looking up some information on this
    "She had to amputate the lower leg and knee. Travis's recovery took over a year, but he was able to grow a new knee at least." #maybe it's cooler if I don't explain it
    "Pete and the others stopped living in the caves while the mining continued." #we could change this to them stopping mining; it just affects how upset Brennan is in the next event

    $ community_22_mined_anyway = True
    return

label community23:
    # "Brennan wants to collect jellysquid shells for minerals" He knows about them from the beach event, and has been investigating them ever since he "saw" them.
    # Terra is 14 here
    kid "Can Anya and I go to the beach this weekend?"
    him "By yourselves?"
    kid "No, Anya's parents are going."
    him "What's the occasion?"
    kid "Brennan is paying lots of money for glass shells."
    kid "Anya's family is going to the beach to collect them. I want to try to find some too so I can make some money."
    him "How much money are we talking about here?"
    if community_22_mining_stopped:
        # you are never the liason in this option, since you lose liasonship in community 22 if you choose to stop mining
        kid "50 credits for each shell." #TODO: make this number a fairly high amount, but not so high that it seems ridiculous at first
        him "Really? That seems strange."
        kid "That's what Anya told me."
        him "Let me ask Brennan if that's right."
        nvl clear
        him_c "I heard that you're paying 50 credits for glass shells. Is that right?"
        brennan_c "Yes, you heard correctly."
        him_c "Why are they suddenly so valuable?"
        brennan_c "I had Zaina do an analysis of their mineral composition."
        brennan_c "All the minerals we need are concentrated in them."
        brennan_c "We're really behind quota because of suddenly stopping mining for two months, but with enough of these, we should be able to meet the latest deadline."
        him_c "Interesting."
        him "Anya's absolutely right. Brennan's giving 50 credits each for those shells."
    else:
        kid "I don't know, like 5 credits a shell or something."

    kid "So can I go?"
    him "Let's discuss it when [her_name] gets home."
    "Over dinner, I told [her_name] about Brennan giving out credits for shells, and [kid_name] told her how she wanted to go to the beach with Anya's family."
    her "I think it's good that you're trying to earn money on your own, [kid_name]. But I don't really want you to go without one of us."
    "I knew we were both thinking the same thing -- Anya's parents were... uninvolved with their kids. [kid_name] going with Anya's parents was about the same as going with no adults."
    her "[his_name], can you go with her?"
    him "It's not a good time for me to go. New weeds are coming up every day, and some of my plants are close to harvest time."
    her "I think I could go. Someone will probably get hurt out there anyway."
    him "I can get some quality time with [bro_name]."
    bro "I wanna go to the beach too!"
    her "I need you to stay here and make sure [his_name] takes good care of the farm!"
    her "And we'll bring you some fish."
    bro "okay..."
    "[her_name] and [kid_name] went to the beach, and [bro_name] and I played games and went on a walk."
    "When they got back, they looked tired."
    him "How was it?"
    her "Well, the beach was totally picked over where we normally go, so we did a little exploring."
    if ate_jellyfish:
        him "Did you see any jellystars while you were there?"
        her "No, I didn't. Maybe they move with the currents?"
    if community_22_mining_stopped:
        kid "We only found five shells. Anya's parents didn't find that many either."
        him "Huh. Were there lots of people there?"
        kid "Yeah, tons! We were all looking for shells."
        kid "People were even going out on boats to catch jellysquids just so we could get their shells."
        her "We turned them in on the way home. So we're 250 credits richer!"
        kid "Hey, that's my money you're talking about."
        her "I helped. Some of that money is rightfully mine."
        kid "You can have 100 credits of it. But the rest is mine."
        him "Oh yeah, we need to get some rice to go with dinner tonight."
        her "I know. We stopped by the storehouse on the way home."
        "She handed me a cup of rice."
        him "Why didn't you just buy a whole bag?"
        her "Ilian is keeping the prices for food the same, but it means he has to ration it."
        her "I think he's currently going overboard! Hopefully he'll relax a little next week."
        him "If he's fixing prices, then what's the point of all that money you just made?"
        her "Buying things from Pete?"
        scene black with fade
        "Next week, I was about to do a little buying and selling when I saw Thuc manning a vegetable stand outside the storehouse."
        thuc "Hey, want some extra-creamy goat milk?"
        him "Yeah, are you selling it?"
        thuc "Just 100 credits for a pint."
        menu:
            "No way.":
                him "You're nuts."
                thuc "You'll be back."
                him "Yeah, when you have your goat cheese reduced price for quick sale."
                thuc "You should save some of your best crops and sell them on your own."
                him "So I can buy your premium goat milk? I've got enough to worry about."
                thuc "Suit yourself."
                $ colonists += 1 #arguable
                return
            "Tempting...":
                him "I know how good the extra creamy stuff is..."
                him "But I don't earn that kind of money selling my crops to Ilian."
                thuc "Give me some of your best crop to sell. I bet I can make you enough money to buy some goat milk."
                him "Yeah, and how much of the profit are you going to pocket?"
                thuc "I promise I'll only keep ten percent of the sale!"
                him "Okay, I'll let you try selling these. Message me when they sell!"
                thuc "Oh, I know someone will want them."
                $ luddites += 1
                $ thuc_sells_food = True
                return

    else:
        #(community_22_forced_luddites_leave) OR (community_22_compromise) OR (community_22_mined_anyway)
        kid "We found ten shells!"
        her "That's fifty credits for you!"
        kid "I can finally buy my own fossil! Or maybe I'll get jars and jars of applesauce. Or I could print out lots of things!" #something hipper?
        her "Or you could save it for something you actually need." #could make this a choice if you want to do a parenting crossover
        kid "Bo---ring."
        her "We went pretty far out, and I found a lot of shellfish."
        him "Oh, are they safe to eat?"
        her "They should be... I didn't do a toxicity panel but we've eaten them before."
        her "What should we do with them?"
        menu:
            "Preserve them and keep them.":
                him "Let's keep them! I think we could dry them out in the oven overnight."
                her "Okay, can you and [bro_name] take care of it? I'm super tired."
                "[bro_name] and I spent the next hour shelling and cleaning the shellfish."
                "Well, [bro_name] mostly watched and played with the shells."
                him "Now we'll be able to have clam chowder whenever we want!"
                $ luddites += 1 #also debateable
            "Eat some now and sell the rest.":
                him "Let's have some with dinner and sell the rest tomorrow."
                her "Okay, can you take care of it?"
                him "Sure."
                "[bro_name] and I made a seafood-vegetable soup."
                her "This really hits the spot. Thanks."
                $ colonists += 1


label community24:
    #luxury goods
    "I was walking into town to have lunch with [her_name] when I saw Thuc working in his yard."
    if community_22_mining_stopped: #this means there was inflation from community23 and Brennan paying a lot for shells
        if thuc_sells_food:
            him "Hi Thuc, thanks for selling those premium crops for me."
            thuc "It was no trouble. Miners have tons of credits right now and they're happy to pay more for better goods and services."
        else:
            thuc "Hey, I've been worried about you since you've only been selling your crops to Ilian."
            him "What do you mean?"
            thuc "Everyone else is selling their premium crops to the miners directly."
        thuc "They've been paying so much that Miranda stopped working in the research lab and has been cooking and cleaning for miners instead."
        him "Really? Wow."
        thuc "Yeah, she wants to earn enough to buy my premium goat milk, so I feel partially responsible."
        him "Do people really drink that stuff?"
        thuc "No, usually people make it into yogurt or lotion or something."
        thuc "Nice lotion sells for even more than goat milk."
        him "I'm surprised Miranda hasn't tried that."
        thuc "She still does some lab work, but she's gotten really into making soap and stuff."
        thuc "That's actually how she markets her cleaning business: 'Scientifically proven to work against Talaam microflora!'"
        thuc "The price of Pete's firegrass has gone waaaay up, so I think some teenagers are trying to grow some on their own."
        thuc "I think some kids made a videogame that they are selling for a ridiculous amount too."
        thuc "Some people have even tried making glass bottles and vases... rumor has it they were trying to make imitation shells."
        him "Ugh, is that still a thing?"
        thuc "Yes, it is."
        thuc "Didn't you read Julia's latest 'Talaam Times' that did an economic analysis of our luxury goods and reviewed select products?"
        him "I didn't want to pay 20 credits for it! That's like the price of beans for a week."
        if not thuc_sells_food:
            him "Hmm. Maybe I could make a little money on the side."
            him "My family might enjoy having some nicer things."
            thuc "I'll take the best you have and sell it in my premium marketplace."
            thuc "I'll message you as soon as these sell."
            him "Thanks."
        else:
            pass
        thuc "For the miners though, 20 credits out of thousands is almost nothing."
        thuc "If you can make something that's popular with them, you could stand to make a lot of money!"
        jump luxury_good


    else:
        thuc "Hey [his_name], how's business?"
        him "Same as ever. You?"
        thuc "I'm glad you asked. Miranda decided that she wasn't making enough money from researching plants and she developed a special soap."
        him "Is it that much different from Natalia's soap?"
        thuc "Yes, she says it's formulated to kill Talaam microflora."
        him "This sounds like something I don't actually need."
        thuc "Perhaps not. But in my completely unbiased opinion, it's superior to other soaps."
        thuc "Julia gave it a flourescent review in 'Talaam Times'. The miners love that kind of stuff."
        thuc "The price of firegrass has gone up, and I heard some kids made a videogame together that they want to sell for some ridiculous price."
        thuc "You should consider producing some kind of luxury good or service to make some extra money."
        jump luxury_good

label luxury_good:
    him "Hmm. I'll think about it."
    "I want to try selling something new."
    menu:
        "Write a guide for beginning farmers on Talaam.":
            "I spent a few months writing a comprehensive guide to beginning farming on Talaam."
            "I had [her_name] edit it, and I had Thuc guest write a chapter."
            "I had Julia write a review of it in 'Talaam Times'."
            "Finally I was ready to sell it for 100 credits!"
            "After a month it had sold just four copies." #+400/40 credits
            kid "Hey dad, that farming guide you wrote is really popular."
            him "Really?"
            kid "Yeah, Oleg bought it and made an app version!"
            him "Hey, he didn't have my permission to do that."
            kid "He's not making that much money off of it."
            him "Ugh."
        "Babysit small children and teach them farming.":
            "I offered to babysit a few small children and give them lots of individual attention for a few hours every morning over the summer."
            "I promised to show them the beauties of Talaam and teach them the joy of farming."
            "A few people were interested, and I chose two families with kids to help."
            "I'd go pick up the kids in the morning, and then I'd drop them off at the co-op daycare after lunch."
            "At first it was really difficult. The kids had a hard time changing their routines."
            "I had forgotten how hard it is to do anything with kids in the house, so often I'd still be working on my farm after dinner."
            "I did make a lot of money though!" #+2000/200 credits but more stress?
        "Consult on small farming projects.":
            "I advertised my professional farm consulting in the 'Talaam Times.'"
            "I was surprised when Oleg was my first customer."
            "He had a lot of questions about a hypothetical plant that was a lot like firegrass."
            "I told him that I couldn't give him advice on how to grow imaginary crops and taught him some general farming principles."
            kid "Oleg is telling everyone that you really know your farming stuff."
            him "Sometimes I wasn't even sure he was listening..."
            kid "He's been doing phosphorus measurements and everything."
            "A few other people took me up on it, but I didn't make a lot of money off of it."
            "There were plenty of books and other farmers people could consult for free." #+400/40 credits
    return

label community25:
    #Brennan's Jellysquid farm
    $ new_25 = False
    $ new2_25 = False
    $ eat_25 = False
    $ eat2_25 = False
    $ jellysquid_25 = False
    $ meat_25 = False
    $ effective_25 = False
    $ touch_25 = False
    $ touch2_25 = False

    "Every night after dinner I liked to catch up on the news around town."
    "This week Sara was asking about recipes for the jellystars."
    nvl clear
    sara_c "After you chop it up, do you just sautee it?"
    thuc_c "I like it in a little beef grease with beans and garlic."
    natalia_c "I think Ilian is selling it dried now. Dried jellystar is really good in soup"
    sara_c "This stuff has pretty high water content... is there anything left after it's dried out?"
    him_c "Why do we suddenly have so much jellystar? I wasn't sure if it was approved for human consumption."
    if ate_jellyfish:
        him_c "Dr. Lily told me that they contain a parasite which could decrease reaction speed."
        sara_c "Really? I haven't noticed anything like that."
        him_c "Well, she did say it was only a difference of a few milliseconds."
        him_c "Also, I think they're too cute to eat."
        thuc_c "I do feel a twinge of guilt when I eat them. But if they're already processed I don't think about it as much."
        natalia_c "Yeah, I don't like cutting up the carcasses. It just makes me sad."
    ilian_c "Brennan started farming them for their shells. He doesn't need the meat, so he sold it all to the storehouse."
    ilian_c "It's really cheap right now, and we're still drying more."
    ilian_c "You can use it for bait when fishing, too."
    him_c "He's farming the form with the shell?"
    ilian_c "I'm not sure if he got them to reproduce but he had a lot of dead jellystar to offload."
    him_c "I'm surprised because I don't think Brennan has much experience in aquatic animal husbandry."
    brennan_c "I have been trying to farm jellysquid, which resulted in surplus jellystars."
    sara_c "Are the jellysquid even the same species?"
    julia_c "Dr. Lily reported that the jellysquid form is an aggregate of the jellystar one, but she never personally witnessed how it happens."
    julia_c "She wrote about it in a paper on them. You should probably read it if you're trying to raise them."
    brennan_c "Thanks, I'll look it up. I've made a few observations of my own."
    julia_c "You should publish them!"
    brennan_c "My information is proprietary."
    julia_c "You could sell it for money then!"
    brennan_c "Maybe when I have some information worth selling, I'll publish it."
    if not ate_jellyfish:
        him "Hmm. These jellystar recipes look kind of good."
        him "Maybe I should try them."
        menu:
            "Buy and eat them.":
                "I bought some dried jellystars and we had them in soup."
                $ ate_jellyfish = True
            "Don't eat them.":
                "I decided not to eat them."
    "Every cloudy season, we like to spend more time outside. Usually we end up making the long trek to the beach. It's a lot easier now that the kids are bigger."
    if (miners > 12):
        "I looked around the coast for a bit and found Chaco tending his jellystar farm."
        "Nets with a close weave enclosed a small area off a pier."
        him "Is this the famous jellystar farm?"
        chaco "Yep."
        him "Are you in charge of it?"
        chaco "I'm the one who checks on it every day and takes notes."
        label jelly_convo:
            menu:
                "What's new?" if not new_25:
                    him "Any new developments?"
                    chaco "During the double full moon, if there's a solar flare, it makes the jellystars glow."
                    chaco "Their pigments probably glow in UV light."
                    him "That's incredible. I hadn't thought about how solar flares would affect the moonlight. Is it safe for humans?"
                    chaco "Probably not."
                    him "How do they glow when it's cloudy then?"
                    chaco "Luminescence."
                    $ new_25 = True
                    jump jelly_convo
                "What do they eat?" if not eat_25:
                    him "What do you feed them?"
                    chaco "Nothing. They probably eat plankton."
                    chaco "I've seen them eat tiny fish too."
                    $ eat_25 = True
                    jump jelly_convo
                "Have you made any jellysquid?" if not jellysquid_25:
                    him "Any luck getting them to aggregate into a jellysquid?"
                    chaco "No. But we have a clue."
                    chaco "We found a baby jellysquid."
                    chaco "We put it in the farm. It died, and the jellystars ate its tiny shell."
                    him "Weird."
                    $ jellysquid_25 = True
                    jump jelly_convo
                "Can I touch one?" if not touch_25:
                    "One jellysquid had five tentacles covered with purple spines like an Earth sea urchin."
                    him "Can I touch one?"
                    chaco "You can... sometimes it agitates them."
                    menu:
                        "Touch one.":
                            "I crouched down on the pier and reached out to touch one."
                            "I felt a little spark like static and feel one of the spines poking me."
                            "The jellystars grasped each other and made a long chain to the edge of the net."
                            "I could see and think but it felt like I was in a trance."
                            "Chaco took my hand out of the water."
                            chaco "Weird, huh."
                            $ touched_jellystar_25 = True
                        "Don't touch one.":
                            "I decided to just look at the jellystars."
                    $ touch_25 = True
                    jump jelly_convo
                "Why is there so much extra jellystar meat?" if not meat_25:
                    him "It doesn't look like there are that many jellystars right now."
                    him "Where did all the extra meat come from?"
                    chaco "They reproduce on their own and crowd each other."
                    chaco "Brennan thinks that they can't combine if there are too many of them."
                    him "What do you think?"
                    chaco "I'm not sure."
                    $ meat_25 = True
                    jump jelly_convo
                "I'm done talking.":
                    him "Good seeing you."
                    chaco "You too."
                    jump after_convo_25

    elif (luddites > 10):
        "I looked around the coast for the jellystar farm."
        "I saw Pete standing on a pier and walked down to say hi."
        "Out on the pier, I could see that the jellystars were enclosed by large net walls."
        him "How's it going?"
        pete "Not bad. Just checking out Brennan's jellystar farm."
        label jelly2_convo:
            menu:
                "Is the farm effective?" if not effective_25:
                    him "Is it working?"
                    pete "It's making lots of jellystars, but no jellysquid that I've seen."
                    him "Colonists have been eating lots of jellystar soup thanks to that."
                    $ effective_25 = True
                    jump jelly2_convo
                "What do they eat?" if not eat2_25:
                    him "Do they feed them fish or something?"
                    pete "They're like the goats of the ocean."
                    pete "They can live off of just about anything, including whatever plankton are floating around."
                    $ eat2_25 = True
                    jump jelly2_convo
                "Can I touch one?" if not touch2_25:
                    "One jellysquid had five tentacles covered with purple spines like an Earth sea urchin."
                    him "Is it safe to touch them?"
                    pete "It won't kill you. Go ahead and try it."
                    menu:
                        "Touch one.":
                            "I crouched down on the pier and reached out to touch one."
                            "I felt a little spark like static and feel one of the spines poking me."
                            "The jellystars grasped each other and made a long chain to the edge of the net."
                            "I could see and think but it felt like I was in a trance."
                            "Pete took my hand out of the water."
                            pete "Sometimes they do that."
                            $ touched_jellystar_25 = True
                            $ touch2_25 = True
                            jump jelly2_convo
                        "Don't touch one.":
                            "I decided to just look at the jellystars."
                            $ touch2_25 = True
                            jump jelly2_convo
                "What's new with you?" if not new2_25:
                    him "How are you doing? Still selling firegrass?"
                    if (community_22_mining_stopped):
                        pete "Yes, but the sudden inflation almost gave me a heart attack."
                        pete "My stock was completely wiped out for a few months, because people were stocking up before I figured out what happened."
                        $ new2_25 = True
                        jump jelly2_convo
                    elif (community_22_compromise):
                        pete "Yep. From my secret firegrass fields."
                        pete "Travis and Helen made an interesting game together that they call Talaam chess."
                        pete "You should try it out sometime!"
                        him "That brings back memories. I thought you guys were too busy to play games."
                        pete "Nope. I think I actually have more free time now than when I was the colony's librarian."
                        pete "I was always trying to read everything so I could know how to help everyone."
                        pete "I do miss reading sometimes."
                        $ new2_25 = True
                        jump jelly2_convo
                    elif (community_22_mined_anyway):
                        pete "Well it's been hard for Travis to adjust to not having feet."
                        pete "I shouldn't have been so stubborn and stayed in the caves."
                        pete "I'm just glad Travis didn't die in there."
                        pete "He has mixed feelings about the prosthetics. He feels like he should be able to live without them but he depends on them for certain things."
                        pete "I can't depend on him to do much cattle herding. He keeps busy with wood carving."
                        him "Yeah, I saw he carved some kind of chess set?"
                        pete "He and Helen collaborated on that. She knits little hats for the pyramid-shaped pieces so you can change them around."
                        him "So you still get around to playing board games now and then?"
                        pete "Sure do! You should come by sometime and play Talaamian chess with me."
                        $ new2_25 = True
                        jump jelly2_convo
                    else: #this should be impossible to get, since the other ending resets luddite relationship to 0. it's here as a safety net in case something goes horribly wrong.
                        pete "It's been hard finding a new place to live."
                        pete "We've found a place that I think will be safe from radiation."
                        pete "I don't really want anyone to know where it is though."
                        him "That's understandable."
                        $ new2_25 = True
                        jump jelly2_convo
                "That's all I want to say.":
                    him "It was good seeing you."
                    pete "There's something I'm worried about..."
                    pete "Is it ethical to farm the jellystars like this?"
                    if ate_jellyfish:
                        him "I'm worried about that too."
                        pete "Each arm in a jellystar has its own nerve bundle. Their nerve network is a lot like an octopus's."
                        him "They can probably feel when they're touching something other than themselves... but they don't even have eyes."
                        pete "I wonder if they can sense UV radiation."
                        him "Wow, senses I haven't even thought about."
                        pete "And in jellysquid form, they are definitely intelligent."
                    else:
                        him "What do you mean? They're not that different from cattle, are they?"
                        pete "I've dissected a dead jellystar before. Each arm has its own nerve bundle, like an Earth octopus."
                        him "But can they sense the world around them? Do they even have a brain?"
                        pete "They don't have eyes, or much of a brain. But they can definitely feel things with their tentacles."
                        pete "I wouldn't be surprised if they can sense UV radiation."
                        him "But they're not even as intelligent as a cow!"
                        pete "No, not in the jellystar form. But the jellysquids are definitely intelligent."
                        pete "And the jellysquids are made up of jellystars! They're like baby jellysquids."
                    him "That reminds me--I haven't seen any jellysquid up here."
                    pete "They've all been caught for their shells."
                    him "And there aren't any jellysquids in this farm?"
                    pete "I've been checking it every week or so and there haven't been any jellysquids at all."
                    pete "They must need something else to change."
                    jump after_convo_25

        label after_convo_25: #only if you your relationship with the miners is high enough?
            nvl clear
            him_c "I haven't seen fresh jellystar for a few weeks. Brennan, does that mean you've figured out how to breed jellysquids?"
            brennan_c "Yes, I have."
            julia_c "The jellysquids couldn't make their shells in the presence of so many other jellystars."
            him_c "How do they even know when other jellystars are nearby?"
            julia_c "When they touch each other, they form a rudimentary network if there are at least two other jellystars in arm's reach."
            julia_c "They basically form into a net, which can catch even more food than if they transform into jellysquids."
            him_c "Huh, that's really interesting."
            brennan_c "That information is supposed to be confidential."
            julia_c "I guess you should have had Miranda sign a non-disclosure agreement."
            julia_c "It's not like any of us want to breed them."
            brennan_c "You may not have an interest in that, but the miners would much prefer to farm jellysquids."
            brennan_c "Most of them don't read colonists' chat though."
            julia_c "Well if it's more efficient maybe they should be farming jellysquid."
            brennan_c "I'm still doing research to see if that's the case."
            brennan_c "For the reasons you mentioned, it's difficult to farm them en masse."
            brennan_c "I do have some jellysquid meat, but since it isn't in high demand I was planning to sell it to Pete for fertilizer or fish food."
            return


    else: #if neither miners or luddites is high enough
        "I looked around the coast for the jellystar farm."
        "I found a pier surrounded by nets that enclosed bunches of jellystar."
        "One jellysquid had five tentacles covered with purple spines like an Earth sea urchin."
        menu:
            "Touch one.":
                "I crouched down on the pier and reached out to touch one."
                "I felt a little spark like static and feel one of the spines poking me."
                "The jellystars grasped each other and made a long chain to the edge of the net."
                "I could see and think but it felt like I was in a trance."
                "After a few minutes or an hour, it let me go."
                $ touched_jellystar_25 = True
                return
            "Don't touch one.":
                "I decided to just look at the jellystar."
                jump after_convo_25
                    #what if the secret to making a jellysquid is that after it makes a shell, you have to hold one in each hand and it makes a complete circuit?
                    #have another scene, probably here, where they discover how to make jellysquid.
                    #the jellysquid farms are somewhat successful, but often the jellysquid will die before completely forming a shell, for unknown reasons.

label community26:
    $ study_published_26 = False
    $ work_fewer_hours = False
    $ brennan_refuses_fewer_hours = False
    $ grow_more_tea = False
    $ pete_knows_his_cows_have_cancer = False
    $ keep_buying_pete_beef = False
    $ stop_buying_beef = False
    #artifical meat and firegrass--too much for one event?

    her "So, I was having a slow day and I decided to do some research in the lab on our diet."
    if luddites > 5:
        her "Pete asked me to check on his cows. Some of them are getting cataracts but otherwise they are pretty healthy."
        her "They do have frequent bloating and digestion problems, but that's pretty good considering that they are eating a mixture of alfalfa and foreign plants all day."
    her "I've tested some of the meat that Pete sells. It's remarkably low in bacteria."
    her "He dries it in the sun, usually under a solar flare, so that's no surprise."
    her "However, the cells in Pete's meat are often irregular and probably cancerous."
    him "Okay... but eating cancer doesn't give you cancer, right?"
    her "They probably don't, but it's safer not to eat them. There have been cases where cancer travelled through saliva or injections."
    him "But the cells are dead in meat, so why would it matter?"
    her "It hasn't really been studied before. It's probably safer not to eat cancerous meat."
    him "What about the cows from the colony?"
    her "I compared the meat from them with the meat from Pete's cows. The colony's cows also have irregular cells, but not as frequently as Pete's cows do."
    her "We have moveable shade structures for our cows, and they eat alfalfa during the rainy season."
    him "Yeah, but Pete's cows have those UV blankets, don't they?"
    her "They do, but I think they don't work very well. I've seen the cows take them off."
    her "My question for you is if you think I should publish the results of my study."
    her "If people keep eating this meat, it might shorten their lifespan."
    menu:
        "Yes, definitely.":
            him "People should know the risks of what they're eating. You should definitely tell everyone."
            him "Just be honest about how much we don't know."
            her "Okay."
            "[her_name] wrote up a brief paper summarizing her findings."
            "A few people read it and stopped buying meat from Pete."
            $ study_published_26 = True
            $ colonists += 1
        "No, don't publish the study.":
            him "How many samples have you studied? I think it's too early to draw conclusions."
            her "True, my sample size is pretty small. I'll keep studying it."
        "You should at least tell Pete." if luddites >5:
            him "Pete should know that his cows are developing cancer."
            him "Maybe he can adjust his radiation-shielding measures."
            her "That's a good idea. I'll make that suggestion."
            "Pete started experimenting with different ways to shield his cows from radiation."
            $ pete_knows_his_cows_have_cancer = True
            $ luddites += 1

    her "Also, I met with a miner this week who was a heavy user of firegrass."
    her "She has severe insomnia and depression."
    him "And sleeping pills don't help?"
    her "Well, they do help her sleep, but then she feels sleepy and usually uses firegrass to help her feel more awake."
    her "She has frequent panic attacks and has lost an unhealthy amount of weight."
    her "Mayor Grayson agrees that we don't have the resources for a mental hospital."
    her "Sara completed training to do some mental health counseling and has started sessions with her, but she needs more than just therapy."
    her "She doesn't seem to be getting better anytime soon. She has suicidal tendencies."
    him "We should help her change something in her life to break this cycle."
    her "I feel like I've done everything I can. I'm going to present her case to the town council to see if they have other ideas."


    if is_liason:
        "[her_name] called a town council with me, the mayor, Brennan, and Sara as our spiritual leader."
        her "Thank you for meeting with me today. I would like to discuss a miner who has debilitating insomnia and depression primarily due to her use of firegrass. We can call her Carol although that is not her real name."
        her "Four years ago, her husband was disabled in a mining accident and she cared for him and watched her children during most of the day."
        her "At night, she used firegrass to stay alert for her mining shift. During this time of heavy usage, she got 2-4 hours of sleep every two days or so."
        her "I'd like to discuss how we can help her family and also how we can discourage heavy usage of firegrass."
        her "Right now, Carol is probably lying in bed trying to avoid talking to anyone."
        her "Her biggest accomplishment this week was washing her hair and getting her rations delivered."
        sara "I've been visiting her at home to start her therapy. I think her husband feels like it's his fault that she's depressed."
        brennan "I remember his accident. The perfect storm of several miscommunications." #tie it to an earlier event?
        brennan "He can't walk anymore, but he can still talk and do things with his hands."
        brennan "He did have some brain damage though, so he sometimes makes unpredictable mistakes."
        her "Their family needs intensive care right now. I don't think Van Nguyen is too busy right now, and he did an apprenticeship with me a few years ago."
        brennan "I assume he's one of Thuc and Julia's kids?"
        her "Yes. He's their youngest and has a great sense of humor. He should be able to babysit the kids for a few hours a day."
        brennan "So, they'll have a babysitter/nurse and a psychotherapist visiting them..."
        her "I would like you to keep paying Carol enough to live off of while she recovers."
        brennan "Her husband is already on disability... and what if she never recovers?"
        her "Then we still want to take care of them!"
        brennan "I'm willing to give her a month of paid disability."
        her "Well, that's a start anyway. Let's discuss firegrass and how we can manage it."
        her "It appears that the active compound from firegrass stays in the blood for about as long as caffeine."
        her "However, the long-term side effects are more severe."
        if miners > 10: #from community21, if you talked about it with Brennan
            her "A few years ago, I gave miners recommended doses, but even with those doses, miners have experienced insomnia and reduced appetite."
        else:
            her "Even miners who don't take very much experience side effects like insomnia and reduced appetite."
        her "I think we should discourage the use firegrass somehow. I don't want to see any more cases of insomnia and depression."
        brennan "I also don't want to see that. I don't think outlawing firegrass will stop people from using it."
        brennan "Pete is going to sell firegrass no matter what we decide."
        her "So how would you cut down on firegrass use?"
        brennan "We could educate users about its side effects. Make posters and engaging, informational narratives that show the effects of its use."
        brennan "Maybe Carol could help educate users when she's feeling better."
        sara "I know an enterprising young person who could make an app about how to use firegrass."
        him "Is it Oleg?"
        sara "Yes! He is really interested in educational technology."
        if miners > 10:
            sara "You could have them access their own health stats from the database and it could tell them their recommended dosage."
            her "But my recommended dosage levels were incorrect before. Soon my recommended dose is not going to give users any noticable alertness."
            her "Also there is no way I'm giving Oleg access to the health database."
        else:
            sara "You could make some recommendations for it."
            her "I think my recommendations wouldn't give users the level of alertness they're accustomed to."
        sara "Well, we want to at least try, right? Isn't the placebo effect still real with a low dose?"
        her "How about I just start selling placebo pills then?"
        sara "Better than doing nothing."
        pavel "I think we need to understand what motivates people to use firegrass and address that concern."
        pavel "Brennan, are you still running up against tight deadlines?"
        brennan "Sometimes we're lucky and fill our quota quickly, and sometimes we're working major overtime to just get close."
        brennan "I've asked RET to change their system, but I don't think that will happen anytime soon."
        pavel "They have almost no contact with RET... what if you told them that RET did away with the quota system so that they could work more consistent hours?"
        pavel "It might help prevent accidents and actually increase productivity."
        brennan "I could change the amount of hours they can work." #it might be more interesting if he does want to lie?
        brennan "I am a little worried about what the miners would do if they had more leisure time though."
        sara "Why can't they just drink green tea to help them stay awake?"
        brennan "They do drink tea, and you've probably noticed that it's also in high demand."
        brennan "I can usually get enough for three cups in a week."
        her "Certainly drinking tea would be a safer alternative than smoking firegrass."
        pavel "I don't like to drink tea. I miss coffee."
        him "Well, if we're treating it as a drug, it shouldn't matter what it tastes like."
        pavel "Of course it matters! Do you eat fruits and vegetables because they have the chemicals necessary for you to survive?"
        pavel "Or do you just have no sense of taste?"
        him "Maybe if you weren't such a food snob you would enjoy your life more."
        pavel "Having a discerning palate makes me appreciate good things even more. But we're getting distracted."
        pavel "Certainly growing more tea could help with the alertness issues people usually turn to firegrass for."
        her "But I don't think tea can easily replace firegrass for people who are already using it."
        "What do I recommend?"
        menu:
            "Push for Brennan to change the amount of hours miners can work.":
                him "I think Pavel has the right idea. Maybe if the miners didn't feel so anxious about working every waking second, they wouldn't feel the need to use firegrass."
                her "I agree with you, but I there's a chemical dependence going on here too. Their bodies are used to this drug now, and they use it to feel normnal."
                him "Reducing their work hours should discourage them from using it more."
                if (miners > 10): #is it mean to make this an option where it won't work?
                    brennan "I think it will help with productivity." #he only agrees with you if your relationship with miners is good enough?
                    $ miners += 1
                    $ work_fewer_hours = True
                    jump educational_app
                else:
                    brennan "Send me an e-mail after the meeting and we can talk about it."
                    $ brennan_refuses_fewer_hours = True
                    jump educational_app
            "Grow more tea plants.": #change to green tea
                him "Let's make tea plants a priority this growing season."
                him "If we plant them around the same time, we can process them together too."
                pavel "I'm interested in making black tea with the leaves."
                him "Sounds good. Maybe some people will like black tea more than green tea."
                $ grow_more_tea = True
                jump educational_app
            "Don't do anything.":
                him "I don't think it's our job to tell people how to live."
                him "Let them use firegrass if they want to."
                her "Part of my job is telling people the correct dosage for drugs to take and taking care of people who use too much."
                her "I'd much prefer to prevent people from using too much firegrass to begin with."
                $ luddites += 1
                jump educational_app
        label educational_app:
            her "I'd like to work with Oleg on making that app. Pavel, can you provide us some credits so I can pay him?"
            pavel "I can provide you with some, but I think that some of this should come from Brennan's budget, since miners are the biggest users of firegrass."
            brennan "I think you vastly underestimate the amount of colonists who use it. But this is important and I want to show my support."
            brennan "[her_name], how much do you think it will cost?"
            her "I need to talk to Oleg about that, so I'll message you both a budget estimate next week."
            "She ended the meeting with a summary of what we'd talked about."
            "Many people pitched in to help Carol and her family."
            "Natalia watched Carol's children in the day while Sara took Carol on a tour of the different jobs in the colony."
            "For a while it seemed like even our best efforts weren't helping, and Carol blamed herself for not being appreciative enough."
            "[her_name] gave Carol medicine to help with her depression, and Sara taught her coping techniques."
            "Carol's insomnia and depression were never completely cured, but we helped her endure through this episode of it."
            if work_fewer_hours:
                "Brennan changed the shift schedule from 12 to 8 hours, and set a maximum of sixty hours of working per week."
                "Some of the miners made a soccer team, and a few took on jobs outside of mining."
                jump after_firegrass_26
            elif brennan_refuses_fewer_hours:
                "I e-mailed Brennan about changing the shift schedule but he never replied."
                "When I brought it up with him in-person, he said something about not wanting to upset the miners by changing how much money they could earn."
                jump after_firegrass_26
            elif grow_more_tea and (colonists > 7):
                "I got Thuc and Zaina to help me plant a new field of tea plants in return for part of the profits."
                "Julia started an advertising campaign in her colony newspaper right before our first harvest, which helped with sales."
                "Pavel started experimenting with the most efficient way to make black tea, and developed a loyal following."
                $ colonists += 1
                jump after_firegrass_26
            elif grow_more_tea:
                "I wanted to plant a new field of tea plants, but I couldn't get anyone to help me."
                "Thuc said that he was too stressed out with his own famr, and Zaina said that the site I picked for the plants was too far away from her house."
                jump after_firegrass_26
            else:
                jump after_firegrass_26

    else:
        "After she presented to the town council, she worked with Oleg to make an informational app about firegrass use."
        #better alt?
        jump after_firegrass_26

    # better transition. conversation with RET where they say it's coming? have some of this conveyed through dialogue.
label after_firegrass_26:
    "About once a year, we've been receiving shuttles with supplies from RET, which the miners would send back full of rare ore."
    "This year it seemed like they anticipated [her_name]'s research on meat, even though the shuttle had been sent years beforehand."
    "Ilian called a meeting to discuss the changes that came with the shuttle."
    ilian "The shuttle this year came with equipment and recipes for growing synthetic meat."
    ilian "Some of you may have tried some in the shuttle on the way over but the instructions say that the flavor has improved considerably."
    thuc "Well, that wouldn't take much."
    ilian "We're also to stop eating chicken, turkey, and cow meat and to use the synthetic meat as a replacement."
    him "Can we still eat native meats?"
    ilian "It doesn't mention native jelly stars, fish, wolf slugs, or any other aliens, so I think we're okay there."
    if study_published_26:
        ilian "You may have read [her_name]'s study about Pete's cattle having cancer and their meat possibly being carcinogenic."
        ilian "RET had come to similar conclusions seven years ago, not just about Pete's cattle, but any animals that are exposed to high UV radiation regularly."
    else:
        ilian "Seven years ago RET completed several research studies that led them to believe that the meat of any animal exposed to high UV radiation is carcinogenic."
    if thuc_has_cattle:
        thuc "Well, there goes two-thirds of my income."
    else:
        ilian "After I go to all the trouble to learn how to breed these things..."
    ilian "Also, sending cows to Talaam was a very unpopular decision with environmenal agencies, and RET has made agreements to reduce our cattle herds to zero."
    thuc "Zero? That seems a little extreme."
    ilian "Well, that's the final goal. They expect us to halve our herd in two years."
    if thuc_has_cattle:
        thuc "If I won't be as busy with cattle, I might as well start in on this synthetic meat thing."
        ilian "You can start by building the laboratory to grow the meat in."
    else:
        ilian "I'll be heading up the synthetic meat production, which will be in a laboratory building we'll build near the storehouse."
    ilian "I'm going to to a demonstration for you here which shows you how the meat is grown."
    "Ilian showed us a petri dish.'" #find a picture of a petri dish
    ilian "This is where we grow the meat from bovine stem cells. Every day I feed it a little food, or growth culture."
    ilian "We sprinkle a little xantham gum on top to prevent fungal growth."
    ilian "Workers in the lab will feed the cells and eventually start stretching them out to make the texture more appealing."
    ilian "You can all try a sample here so you know what to expect."
    sara "Hmm, the texture is good. It doesn't have a strong taste."
    ilian "There isn't any fat in it, so it doesn't taste as strong as you might expect it to."
    "Hmm. I could live with this. Do I want to?"
    menu:
        "Keep buying beef from Pete.":
            "I decided to keep buying previously-live beef when I could from Pete. It tasted better."
            "[her_name] didn't eat it."
            $ keep_buying_pete_beef = True
            $ luddites += 1
            return
        "Eat as much synthetic meat as possible.":
            "We stopped buying beef from Pete, although occasionally we ate some previously-live beef when Thuc cut down the herd."
            $ stop_buying_beef = True
            $ colonists += 1
    if (luddites > 8):
        "Pete stopped by to chat one sunny day while I was sowing some new seeds."
        pete "How's it going?"
        him "Not bad. I'm optimistic about this new crop."
        him "How are you?"
        pete "The clouds still drop rain and wolfslugs still fear me."
        pete "But I haven't been selling as much firegrass or beef lately. Did some people make an 'avoid-Pete' club?"
        him "No, nothing so extreme."
        him "One of the miners was a heavy user of firegrass for a few years, and it started to really impact her sleep and mental health."
        him "A bunch of us tried to educate people about its dangers and discourage them from abusing it."
        pete "Hmm. That's not what I heard."
        pete "I heard that someone is selling firegrass for cheaper than I am. So now everyone gets it from him instead of me."
        if stop_buying_beef:
            pete "And I heard that you're growing your own meat now."
            if pete_knows_his_cows_have_cancer:
                pete "I guess it was only a matter of time, seein' how my cows are sick and all."
                pete "I still don't understand why them having cancer makes them bad to eat. That's not how cancer works."
            else:
                pete "What gives?"
                him "Your cows and all our Earth creatures we eat for meat have cancer and eating them can give cancer to humans."
                pete "That's not how cancer works. Eating a cancerous cell doesn't give you cancer."
            him "How do you know?"
            pete "Simple biology! Dead cells don't affect living ones."
            him "They do if you eat those dead cells!"
            pete "I can tell I'm not persuading you. I might just have to invest more in my fish farms. Those are okay to eat still, right?"
            him "Yeah, the water diffuses the radiation."
            pete "Let me know if you want some next time I come 'round"
        else:
            pete "I heard that you're growing meat in a lab now."
            pete "Except you apparently prefer my beef."
            him "Even if it is carcinogenic, it adds so much to my life satisfaction that I don't mind dying a little earlier."
            pete "I doubt it's true. You don't get cancer from eating cancerous cells."
            pete "If that were true I would have arthritis and bloating and all the other things my cattle suffered from before I ate them."
            pete "Instead I just have high blood pressure."
            him "Really? You seem so healthy."
            pete "I know you guys think I'm sitting on a bundle of credits but they all go to medicine these days."
            him "Well, I hope your fish are lucrative."
        return


label community27:
    #JELLYPEOPLE RECKONING
    #if community_22_mining_stopped, the gathering of shells was more intense
    $ shell_count = 0
    $ serve_mudfish = False
    $ serve_Shills = False
    "It was time for our now-annual trip to the ocean."
    "When we got there, we were surprised to see more fish than usual."
    "Brennan's jellysquid farms, which dotted the coastline at regular intervals, were completely empty."
    "I looked at one of the farms, and the nets had been cut."
    him "I wonder if this is Pete's work?"
    "We took a boat out to go fishing past the pier, especially since [kid_name] wanted to play with a jellysquid.."
    "We spent a long time searching. There were a lot of fish in the water eating bits of dead animals... was it dead jellysquid?"
    "I thought I saw a live jellysquid and got out of the boat. The ocean was shallow here and I was able to stand up."
    "I caught the jellysquid in a bucket after some chasing."
    "It wasn't displaying the reading game on its tablet-like shell like it had years before. Instead it said:"
    "Jellysquid" "Sad Sad Sad Sad Sad Sad"
    "[kid_name] touched the jellysquid's shell."
    "Jellysquid" "We children are dying."
    "Jellysquid" "We can't find shells."
    him "What is it trying to say? I thought they made their own shells."
    kid "Maybe they need to see another shell to know how to make it?"
    him "Hmm. They do seem to be intelligent animals, but usually growing a body part isn't a conscious process."
    "Jellysquid" "Help me?"
    "Then the back of the jellysquid looked like the literacy game again."
    "'Grown-ups only! Needs permission to access more content.'"
    "'2+3 = ?'"
    "I answered the question. Then it asked me to 'proceed on the highlighted route' to continue, showing a top-down map. I could tell it was mimicking a GPS, but it didn't adjust to my exact location."
    "I followed the map, which took my little borrowed rowboat past the swell of the waves, which as far as I knew was uncharted territory."
    "My rowing became easier, and I noticed that jellystars were guiding my boat towards my destination."
    "Something under the surface was emitting a light."
    "It came closer to the surface, and I could see part of it."
    "It had way more than ten tentacles and was a little smaller than our rowboat." #this line is optional--if Clarissa wants to draw it. They are not humanoid. DO THEY HAVE SHELLS is the important question
    "Jellystars joined in a chain from it to the jellysquid in my bucket."
    "The jellysquid's surface changed to show a question: 'Why have you killed my children?'"
    menu:
        "Run away.":
            him "I don't want to explain this when I don't really understand it myself."
            him "Let's go home."
            "I tried to leave, but the jellystars kept my boat from moving."
            jump boat_capsized
        # if ate_jellyfish AND touched_jellystar_25: I still want to do something with this variable cluster
        "Engage.":
            him "I am interested in communicating with these aliens."
            kid "Tell it! It can't hear you."
            him "Okay, I'll touch the jellysquid's back."
            jump text_conversation

label text_conversation:
    "It started displaying text."
    "Jellysquid" "Where are the baby's clothes?" #this should come after asking about the babies
    "It displayed several words that I could drag to the answer area."
    "The words were 'I', 'He', 'stole,' 'ate,' 'lost,' and 'them'."
    menu:
        "I":
            him "Brennan is basically a part of my group. I'm partially responsible for his actions."
            menu:
                "stole them":
                    him "We took the shells without proper research or community consensus."
                    kid "Well, Brennan did."
                    him "Didn't you help him?"
                    kid "Yeah. But I needed the money."
                    "Jellysquid"  "Give them back to my children."
                    jump call_to_squid
                "ate them":
                    him "I ate them. Using the minerals inside for technology is like eating to an animal."
                    him "I am part of the animal that consumes technology."
                    kid "I guess I am too."
                    "After I put in this answer, the jellysquid grabbed my shirt and tried to eat it."
                    "Jellysquid" "You say you ate the clothes but it is not in your clothes."
                    "Jellysquid" "Are the clothes inside you?"
                    menu:
                        "Yes.":
                            him "The clothes of my consumerism are in my bones!"
                            kid "I don't think it's talking about consumerism."
                            jump boat_capsized
                        "No.":
                            him "I think it wants to know where the shells are physically."
                            "Jellysquid" "Bring them for my babies to eat"
                            jump call_to_squid
                "lost them":
                    him "We sent them in a shuttle to another planet. They're basically lost, but on purpose?"
                    "Jellysquid" "Find them for my babies to eat."
                    jump call_to_squid

        "He":
            menu:
                "stole them":
                    him "Brennan took the shells without researching the ecosystem thoroughly or gaining a community consensus."
                    him "He basically stole them."
                    kid "We're the same way though. We've been using this planet without knowing how we would change things."
                    "Jellysquid" "Take them from him. Give back to my children."
                    jump call_to_squid
                "ate them":
                    him "Brennan ate them, sort of. Using the minerals inside for technology is like eating to an animal."
                    "Jellysquid" "Bring his clothes here so we can eat them after he's done."
                    kid "Is it talking about the shells?"
                    jump call_to_squid
                "lost them":
                    him "Brennan sent them in a shuttle to another planet. They're basically lost, but on purpose?"
                    "Jellysquid" "Find them for my babies to eat."
                    jump call_to_squid

label call_to_squid:
    menu:
        "Yes, I will bring them.":
            him "I have no idea what we're going to do but we're going to figure something out."
            kid "Maybe Brennan has some shells we could give back."
            "Jellysquid" "Bring them tomorrow."
            "The jellysquid jumped out of the bucket and into the water."
            "The net of jellystars pushed us back towards shore."
            her "What on Earth happened to you?"
            kid "I think you mean 'What on Talaam' happened to us."
            if luddites > 10:
                him "Any idea what happened to the nets?"
                pete "Nope. I figured it was some angry miner or colonist."
                pete "Or maybe Travis on a bad day."
                "I talked to Pete about my meeting with the jellysquid mother."
                pete "Whoa, that sounds completely out there."
                pete "I have a few shells that I collected before it got popular."
                pete "Take these three and see what you can find out."
                $ shell_count += 3
            "I tracked down Brennan and told him my findings."
            him "I noticed that all your nets had been slashed."
            brennan "Yeah, I bet it was Pete. He's such a bleeding heart when it comes to animals."
            him "He's a farmer himself. Would he really sabatoge your efforts?"
            brennan "Do you have a better explanation? The miners prefer working on the jellysquid farms."
            brennan "There were clean cuts. It wasn't done by an animal."
            him "Well... recently I met with a squid... mother? intelligent entity? They seemed really upset about the shells being gone."
            brennan "Really? Did you get a picture? What did it look like and how did it communicate with you?"
            "I told him about what had happened."
            if (miners > 10):
                brennan "I'll give you two shells. Find out more information. What part of the shell do they need?"
                him "I have my own farm to run!"
                brennan "I can give you some credits for someone else to take care of your farm."
                brennan "I need you to be our new alien liason!"
                $ shell_count += 2
            else:
                brennan "All my jellysquid farms were destroyed anyway. I can't farm them anymore."
                brennan "And I already made promises to the miners based on the shells I have now."
                brennan "Sorry, my hands are tied."
            "I wasn't sure if I had enough shells, so I wrote up my experience and ended with a plea for anyone holding onto a shell to return it to the squid people."
            "I had Julia print it in that week's Talaam Times" #italics
            if (colonists > 10):
                "Four families gave me one shell each."
                $ shell_count += 4
            else:
                "Julia gave me a shell her family had been using for decoration."
                $ shell_count += 1
            "I felt like I had done everything I could. I made arrangements for my farm for the weekend and headed back to the ocean."
            # kid can come or not based on parenting style?
            "The jellystars seemed to sense my presence quickly in the boat, and took me to a different place, where I met with the jellysquid parent."
            "They communicated to me through a jellysquid, which I put in a bucket on my boat."
            "Jellysquid" "Did you bring shells?"
            "I held up the bucket that had the shells in it, and a tentacle whipped up from the surface and grabbed it from me."
            if shell_count > 2:
                "Jellysquid" "Good shells. Need more."
                "I traced a question mark on the jellysquid's shell."
                "Jellysquid" "More. Hundreds."
                #change this to integrate with the magnetic poetry app
#                "I kept tracing a question mark."
#                "It displayed the words 'Why, What, Where, you, we, live, shell, food, not.'"
#                him "That's not a lot to work with. Hmmm."
#                #could be a menu here later.
#                menu:
#                    "Why":
#                        menu:
#                            "you":
#                                menu:
#                                    "live shell?":
#                                        "Jellysquid" "Shell save us from enemy."
#                                    "live not?":
#                                        "Jellysquid" "You kill my children and keep their shells."
#                                        "Jellysquid" "Other fish eat us. You do not eat. Give back shells."
#                            "we":
#                                menu:
#                                    "live shell?":
#                                        "Jellysquid" "You don't live in a shell. Your shell is inside you."
#                                    "live not?":
#                                        "Jellysquid" "Do you eat? You need to eat to live."
#                    "What":
#                        menu:
#                            "you?":
#                                "Jellysquid" "I am an animal in the water."
#                                "Jellysquid" "What are you?"
#                                him "Hmm. My options are kind of limited."
#                                menu:
#                                    "We not food.":
#                                        "Jellysquid" "All animals are food."
#                                    "We not shell.":
#                                        "Jellysquid" "Then why do you need shell?"
#                                    "We live not.":
#                                        "That is not possible. Dead things don't move."
#                            "we?":
#                                "Jellysquid" "You are new animals. We do not know what you are."
#                            "shell":
#                                "Jellysquid." "Shell protects children."
#                            "shell food"
#                    "Where":
#                        menu:
#                            "you":
#                                menu:
#                                    "live?":
#                                        "Jellysquid" "We live here, in the ocean."
#                                    "food?":
#                                        "Jellysquid" "Our food is fish, light, and plants."
#                                    "not live?":
#                                        "Jellysquid" "We do not live on land."
#                            "we":
#                                menu:
#                                    "live?":
#                                        "Jellysquid" "You live on land. You know it. Why do you ask?"
#                                    "food?":
#                                        "Jellysquid." "Your food is on land. And water."
#                                    "not live?":
#                                        "Jellysquid." "You do not live in the ocean."

#                him "What are you?"


#                him "What is shell food?"
#                "Jellysquid" "Other shells make shells."
#                "Jellysquid" "Some rocks make shells."
#                "Jellysquid" "Maybe mud fish? Mud fish tastes bad."
#                him "Hmmm. Good to know."
#                him "Why shell food is not?"
#                "Jellysquid" "You took food."
                "The display changed and asked me to bring more shells back."
                "I knew that I probably couldn't find more shells, so instead I promised to look for shell food."
                "I went back to the colony and my farm."
                "I had a long talk with Miranda about the jellysquids. She chided me for not taking any pictures or recording my 'conversation' with the jellymother."
                "When I mentioned the mudfish, she looked excited."
                "Miranda" "A few years ago I studied that fish."
                him "What eats it?"
                "Miranda" "It's one of the few fish the jellystars won't eat. But a few other, bigger fish will eat it without a problem."
                him "The ones called Shills? Because they make a really cool noise but disappear if you approach them?"
                him "How do they compare to jellysquid shells for metal content?"
                "Miranda" "Well, it's not edible for humans. Let me bring up the report."
                "Miranda" "Some species had a high level of heavy metals. I don't know what kind though."
                him "Wow, this could be big! The same kind of metals that RET wants?"
                him "Maybe instead of taking the shells, Brennan could just mine the mud. The mudfish probably eats some kind of worm that gets the metals from the mud, right?"
                "Miranda" "Or they could just keep doing what's working, which is digging in the mountains."
                "Miranda" "Brennan gave up on the jellysquid farms, right? Just leave well enough alone."
                him "I told the jellymother I would try to help her!" # TODO: decide if jellymother is her or them. make capitalization consistent.
                "Miranda" "Sometimes the most helpful thing you can do is to go away."
                him "They can sort of write to us Miranda! How are you not curious about that?"
                "Miranda" "Actually, I've talked to them before. A lot."
                "Miranda" "I helped Dr. Lily teach them how to 'write'. And now that I know that the jellymother can use them to communicate, it explains why sometimes they were so much more articulate than others and how they could teach each other new things so quickly."
                "Miranda" "These animals are one of the most interesting beings I've studied. I don't want mining to wipe them out."
                him "Well, they asked for help finding shell food. It sounds like this mud fish could help, but they don't like how it tastes. Is there a way we can make it taste better to them?"
                "Miranda" "I think it's just the skin that tastes bad. So maybe if we caught them and made them into filets, they would eat them?"
                him "Or maybe the Shills that eat the mud fish would have the right minerals in their meat?"
                "Miranda" "I can do some field research this weekend."
                him "Great. Maybe the jellymother will talk to you too."
                "Miranda" "You're not coming with me?"
                him "I've been out there twice already. Message me if there's an emergency."
                "I left feeling like maybe there was hope for reconciliation between us and the jellypeople."
                "I could tell Breannan and Zaina about possibly mining in the mud instead of in the mountains."
                menu:
                    "Tell them.":
                        "I told Brennan and Zaina about the heavy metals in the mud. They sounded exicted to try mining it."
                    "Don't tell them.":
                        "I decided not to tell Brennan and Zaina about the heavy metals in the mud."
                "Next week, Miranda returned and asked me to meet with her."
                "Miranda" "The jellysquid seemed to remember me, so I didn't have trouble getting them to try a few different foods."
                "Miranda" "I was able to catch a few mudfish and feed their filets to a jellysquid."
                "Miranda" "They did eat it, and I noticed that their shell grew a little the next day. It's an unconscious process for them, so they can't really tell me how much their shell is growing at a given time."
                "Miranda" "I had a hard time catching the Shill, despite using mudfish as bait. Eventually the Jellymother found me and I told her what I was trying to do."
                "Miranda" "She seemed surprised. The Shill is difficult capture, so they rarely eat it."
                "Miranda" "Still, she was curious, so she instructed some of the jellystars to make a net to catch one."
                "Miranda" "She killed a Shill and had jellysquids eat it, and I observed bigger growth patterns in those jellysquid the next day compared to the one that ate the mudfish."
                "Miranda" "That matches my hypothesis that consuming a higher concentration of metals would increase their growth more rapidly. They are usually limited by what minerals their body has on hand."
                him "So what do you think would be best for the jellysquids?"
                "Miranda" "It's hard to say. The jellysquids would need our help to eat the mudfish, since its skin contains toxins. But the mudfish's concentrations are the most similar to what they're used to."
                "Miranda" "The jellysquid can easily eat the Shill, but instructing them to eat a fellow predator could really mess with the food chain ecology. Also, it's possible that their shells would grow more quickly than they're used to."
                him "Hmm. That does sound like a difficult decision. Do you think we could farm either?"
                "Miranda" "Yes, we could. It would take a lot of work to make an aquatic farm, but maybe we could use it for other fish later."
                "What do I think is better?"
                menu: #should this be a decision? remove it?
                    "Serve mudfish to the jellysquids.":
                        him "I think we should encourage them to eat mudfish. If we all work together to catch and skin them, we'll be able to show the jellymother that we really care."
                        him "Also, we won't have to worry about shell overgrowth."
                        "Miranda" "I just hope the colony is strong enough to help with this."
                        $ serve_mudfish = True
                        jump aquaculture
                    "Have them eat Shills.":
                        him "I don't know if we could farm and skin enough mudfish to grow hundreds of shells."
                        him "If they keep eating Shills, they won't have to rely on us to create new shells."
                        "Miranda" "But we're going to try to farm them so we won't accidentally collapse the food chain, right?"
                        him "Right."
                        "Miranda" "I just hope the colony is strong enough to help with this"
                        $ serve_Shills = True
                        jump aquaculture

                        label aquaculture:
                            "I started making plans for a fish farm off the coast."
                            "I wanted it to have a grated opening, so we wouldn't have to worry about changing the water. I also drew in a sluice gate in case we wanted to release all the fish at once."
                            "After I explained my plans to the Jellymother, she said that she could help trap a few of the first fish to start the farm."
                            if colonists > 10:
                                "The other colonists helped me dig the farm-pond and line it with rocks."
                                if serve_mudfish:
                                    "A few months later, we spent a whole day skinning mudfish and feeding them to jellysquids."
                                    "We ended up going every month for a while. It felt like we got to know some of the growing jellysquids."
                                    "After about six months, the Jellymother told us that our efforts at reparation were sufficient."
                                    "She presented us with some of the fish we could eat as a token of good will."
                                    return
                                else:
                                    "Shills had a longer incubation period than I anticipated. The jellymother started feeding Shills to emerging jellysquids."
                                    "Farming the Shills took weekly maintence, which we shared. After the Shills were big enough to fend for themselves, we released them into the wild."
                                    "A few of the jellysquid ate too much Shill and ended up with large shells, but they seemed to adapt to it fairly well."
                                    "The Jellymother seemed impressed that we followed up on our promise."
                                    "She presented us with some of the fish we could eat as a token of good will."
                                    return
                            else:
                                "I didn't have enough help from the other colonists to finish digging the farm-pond."
                                "The Jellymother disappeared and we rarely saw any of the jelly creatures again."
                                return
               #this is getting long. put into next event?
            else: #if shell count is less than 2
                "Jellysquid" "Did you bring more?"
                him "Uhhh"
                "I traced 'no' on the jellysquid's back."
                "Tentacles grasped my boat from below."
                "I heard a sound like a water pump and then my boat was jettisoned toward the shore. My boat skid across the surface like a skipping rock."
                "The jellysquid was still in the boat with me."
                "Jellysquid" "Mom sad."
                him "Well, that was a diplomatic failure."
                "I put the jellysquid back in the ocean and went home."
                "Over the next few months, there were fewer reports of jellysquid sightings."
                "We rarely saw any of them after that year."
                return
                #Similar resistence to the boat_capsized ending next month
                #I don't remember what the above note means

        "No, I will not bring them.":
            jump boat_capsized

label boat_capsized:
    "They capsized my boat, and I fell into the water."
    "We grabbed onto the boat and tried to turn it over."
    if (ate_jellyfish) and (touched_jellystar_25):
        "A jellysquid slapped my neck, and I felt sorry for this bereaved mother."
        "And now I was leaving her without any sort of explanation."
    "[kid_name] slapped the jellysquid off with an oar."
    kid "Come on Dad! Flip the boat with me!"
    "After flinging away a few jellystars, we flipped the boat."
    "I helped [kid_name] in."
    kid "Just hang on the side while I try to get us away!"
    him "Okay, go for it!"
    "Her oars set some of the jellystars flying, and eventually we were close enough to shore for me to stand up."
    kid "That was unreal."
    her "Are you guys okay? What on Earth happened?"
    kid "Moooom, we're not on Earth, we're on Talaam."
    "We told our friends about our alien encounter, but I'm not sure if they believed us."
    "Over the next few months, there were fewer reports of jellysquid sightings."
    "We rarely saw any of them after that year."

    return


# Perhaps Mayor Grayson dies somewhere in here, leading to a power vaccuum and increased internal tensions as well.
# Pete has fewer credits to buy medicines with, including birth control. Helen is now pregnant and in her 40s?
label community28:
    $ against_euthanasia = False
    $ no_euthanasia_26 = False
    "One cloudy day we were eating outside. We noticed Mayor Grayson walking down the road."
    him "Hi Mayor Grayson, what brings you out here?"
    pavel "Hello, er, I was just out for a walk but I think I'd like to head back now. Would you like to come with me?"
    him "We're in the middle of eating, but maybe in a few minutes?"
    her "I'm done. I'll walk with you, Mayor Grayson."
    pavel "Thank you. I appreciate it."
    "[her_name] returned after about half an hour."
    him "Did you have something you wanted to discuss with the mayor?"
    her "No... isn't it obvious?"
    him "The mayor really wants some of our vegetables?"
    her "He's experiencing the early stages of dementia. He didn't know which way was home, but he didn't want to confess to being lost."
    him "He was lost? We've lived here for over 15 years!"
    her "It happens to a lot of people. I was trying to assess him as I talked to him on the way to his house..."
    him "And you found something out and now you won't discuss it because of patient-doctor confidentiality. Okay, okay."
    her "If you were in Mayor Grayson's situation... would you want to live as long as possible, or would you want someone to help you die when you could no longer remember who you were most of the time?"
    menu:
        "I'd want to die before being a burden on others.":
            him "I think I'd rather die prematurely than live without remembering who I was or what I was doing that day."
            her "I think I would too."
            her "But what about people who live like that normally? Are you saying their lives aren't worth living?"
            him "Uhh... I guess that's up to their caretakers. But since I know what my life is like now and what it would be like then, I can make that decision for myself."
            her "I think I agree with you."
        "I'd want to live as long as possible":
            him "I think I'd want to live as long as possible and die a natural death."
            her "Even if it meant you needed other people to watch you all day, bath you and help you go to the bathroom?"
            her "Even if it meant that you wouldn't know who you were or what you were doing?"
            him "You're basically describing the cognitive state and care needs of small babies, and we highly value their lives."
            him "Is there something wrong with being cared for when you're old?"
            her "Babies are easier to take care of because they are small and can't walk anywhere. Plus, their incompetence has a regular timeline."
            her "I've seen cases where a person can suffer from dementia for decades."
            him "I've seen cases where a person takes care of other people for decades."
            her "I guess it depends on what the person wants and if their society has the resources to take care of them."
            him "I think a society that kills its old people if they have dementia is diseased."
            him "What about children born with disabilities? Are you going to kill them too?"
            her "It's different when it's an old person, because they can consent to euthanasia before it gets bad."
            him "That's just giving up."
            her "There's no known cure."
            him "What about all those sweet moments people have with dementia patients? Like when they suddenly remember who you are and it makes you want to cry, you're so happy?"
            her "Those moments are great for caretakers. How often have you heard a patient with dementia mention those moments?"
            him "It's still meaningful, even if you can't remember it."
            her "This isn't about what I want. It's about what Mayor Grayson might want."
            him "Okay, okay."
            $ against_euthanasia = True
    "The next day, Sara sent out a message saying that Mayor Grayson was ready to retire and that we would be electing a new mayor at a meeting next week."
    if is_liason:
        "She also invited me and [her_name] to a meeting that night to discuss Mayor Pavel Grayson's future."
        # Julia is here too. Brennan is here if your mining relationship is high enough. explain why Julia is there?
        sara "Thank you all for coming. Pavel has been experiencing early signs of dementia for a while now. Recently his memory and sense of direction has become worse." #check last three events to see if Pavel is in them
        sara "Pavel has requested that he be allowed to end his own life before his cognitive abilities decline too much more. He agreed on a threshold with [her_name]."
        sara "He wrote down his wishes and signed it, and I witnessed this. He was oriented to time, place, and circumstance at the time."
        sara "[her_name] has agreed to do weekly assessments and determine Pavel's cognitive abilities."
        sara "I've called you here because you have leadership positions in our community. Julia, I figured that it would be easier for you to attend this meeting than to get a report secondhand for your newspaper."
        sara "[her_name], can you take it from here?"
        her "There isn't a guideline about euthanasia in RET's health manual."
        her "I compared a recent assessment to his scores in previous years, and Mayor Grayson's, I mean, Pavel Grayson's dementia appears to be declining."
        her "At this rate, he may need constant supervision in six months to a year."
        her "I wouldn't be able to supervise him and perform my duties as a doctor at the same time."
        her "My assistant could watch her half of her normal hours, but it would decrease the amount of preventative care visits she makes." #gender check assistant
        her "We're putting the question of whether or not to euthanize Pavel Grayson up for discussion."
        if against_euthanasia:
            him "I don't think Pavel should give up so quickly. Maybe his cognitive decline won't be as quick as we think it will be."
            her "That's why I plan to assess his state so frequently."
            him "I feel like helping him commit suicide is criminal."
            her "But who will take care of him if we don't euthanize him? He could easily kill himself by wandering away or eating something inedible."
            menu:
                "I could help":
                    him "I could supervise him eight hours a day."
                    her "I don't think that's a good idea. And who would take the other sixteen hours in a day?"
                    $ marriage_strength -= 1 #not sure if you want this variable to have minuses?
                    sara "He could stay with us from dinner until after midnight. We usually stay up that late anyway."
                    julia "I'm always waking up that early anyway with my chronic pain. I could take the early morning shift, if he's awake then."
                    sara "Oh, or maybe we can set up his tablet to alert you if he wakes up."
                    her "This isn't necessary. He doesn't want to be dependent on others for the last years of his life."
                    him "I don't want to live in the kind of place where people have to die just because they aren't useful anymore."
                    her "It's what Pavel wants."
                    julia "I agree with [his_name]. I want to take care of our sick and elderly."
                    her "Sara?"
                    sara "I do think Pavel's desire is important, but it could bring everyone together if we work together to essentially give him hospice care."
                    her "Brennan?"
                    brennan "I don't see any reason to keep him alive against his wishes, but it appears we are in the minority."
                    her "Sara, what is your final vote?"
                    sara "Let's take care of him."
                    $ no_euthanasia_26 = True
                    jump fill_gap

                "I'm sure someone could help.":
                     him "I don't know, but we haven't even asked yet."
                     her "It's completely unneccessary."
                     her "Most people already feel overworked. It's not fair to ask them to do more for someone who doesn't even want people taking care of him."
                     julia "I agree with [her_name]. It's not fair to assume that other people will volunteer their time when you're not willing to do it yourself."
                     julia "Why don't we have Pavel consent to euthanasia again in a week."
                     brennan "I agree with Julia."
                     her "Sara?"
                     sara "I like Julia's compromise. I'd like to talk to Pavel more about it, but if it really is what he wants..."
                     her "I understand."
                     jump fill_gap
        else:
            him "I'd say have him consent a second time, just to make sure it wasn't a passing suicidal urge."
            julia "Yes, that sounds like a reasonable plan."
            her "Okay, I'll see if I can get another consent next week. Sara and Brennan, how do you feel about it?"
            brennan "Fine with me."
            sara "I'd like to meet with her myself sometime, but overall, I agree with the consensus we have here."
            her "Okay."
            jump fill_gap

    else:
        "[her_name] told me a few days later that she and a few other colony leaders had agreed to allow Pavel Grayson to be euthanized according to his wishes when he reached a certain state of mental decay."
        if against_euthanasia:
            him "Wow, [her_name], you're okay with this?"
            her "It's what Pavel Grayson wanted."
            him "Okay."
            jump fill_gap
        else:
            him "[her_name], are you ready for this?"
            her "Yes. I'll be helping Pavel avoid an irreversable, extended state of confusion and disability."
            him "I know, but you still have to give him a fatal injection right? Technically you'll be the one killing him."
            her "In a procedure he requested."
            jump fill_gap
    # if is not liason


label fill_gap:
    "In the meantime, we held a meeting to decide who would be the new mayor."
    sara "I received your nominations."
    sara "The top nominations for mayor are Julia, Kevin, and myself."
    ilian "Kevin isn't eligible. He's not a colonist."
    sara "I would like to discuss that right now. While it's true that Kevin isn't a farmer, he isn't really a miner either."
    sara "He and Zaina are going to stay here after most of the miners return to Earth, so they have our same long-term goals."
    sara "If you don't want him to be mayor, go ahead and vote for me or Julia."
    sara "Other questions about the candidates?"
    thuc "Don't vote for Julia! I need her to oversee my water treatment plant."
    julia "Please vote for me! I don't want to oversee Thuc's pee factory."
    kevin "Are miners going to be allowed to vote?"
    sara "Good question. Since the mayor is responsible for the well-being of the colonists, he is elected by colonists."
    sara "Are miners interested in voting? What would it mean for miners to be able to vote?"
    kevin "Yes, some of the miners are interested in voting. I think they should be able to vote, since the well-being of the colony directly impacts them."
    ilian "I don't think the miners should be able to vote. A lot of them are leaving in a few years, and they could push for potentially destructive plans."
    kevin "We're not going to start eating seeds instead of planting them. They want basically the same things."
    ilian "There are twice as many miners as colonists. They could easily outvote the colonists on anything."
    kevin "We don't really vote on policies, just who should be in charge of making policy decisions, which probably won't be a miner anyway, because their contracts don't let them have another job."
    sara "Well, I think that covers the main arguments for and against. Please get out your tablets and we'll take a vote on whether the miners should be allowed to vote or not."
    "Which way will I vote?"
    menu:
        "Allow miners to vote for the mayor now and in future elections.":
            $ miners += 1
            jump after_vote
        "Don't allow miners to vote for the mayor now and in future elections.":
            $ colonists += 1
            jump after_vote

    label after_vote:
        if miners > 10:
            sara "The votes are in, and the majority voted to allow miners to vote."
            sara "I'll be coordinating with Brennan to set up the voting program with the miners. We should be able to vote next week though."
            ilian "You guys are going to regret this. Hope you like Kevin as your mayor."
            kevin "I hope that we can work together harmoniously if I am elected mayor."
            "Next week we all voted on who should be the next mayor, and Kevin was elected mayor."
            if no_euthanasia_26:
                jump no_euthanasia
            else:
                jump euthanasia
        else:
            sara "The votes are in, and the majority voted not to allow miners to vote."
            kevin "I hope we can vote again on this topic sometime in the future."
            ilian "You're going to keep bringing it up until we capitulate, huh?"
            "The next week we colonists voted on who should be the next mayor, and Julia was elected mayor."
            if no_euthanasia_26:
                jump no_euthanasia
            else:
                jump euthanasia

label no_euthanasia:
    nvl clear
    sara_c "So, I told Pavel Grayson that we would all look after him."
    sara_c "He was deeply moved and expressed his gratitude."
    sara_c "I told him we could start next week."
    "The next day, I stopped by his house to check on him. Just in case."
    "He seemed to be deeply asleep..."
    "No, he was out cold. Dead?"
    "He left a note."
    "We didn't have a lot of paper, so it was written on a chalkboard."
    #TODO: note thing
    "I'm so grateful that you were willing to look after me. When I think of all the care I will likely need, I find it unbearable to think of the burden I would place on you."
    "Do try to survive, but if you can't survive, please keep your spirit of self-sacrifice and compassion."
    "Don't think of my suicide as a failure on your part. This was my own rational decision in the face of a known future I preferred not to live."
    #end note
    "I quickly messaged [her_name], and she rushed over from across the street."
    "I felt a few tears fall from my eyes. This was how he thanked us?"
    her "He's still alive! It looks like he injected himself with opiates last night, but he's still conscious."
    "I hurridly wiped my face."
    him "Are you going to save him?"
    her "I'm going to try."
    "[her_name] quickly injected him with adrenaline."
    "She treated him the rest of the day."
    "We pitched in to help watch him around the clock."
    pavel "I'm so sorry... I really didn't want to make life harder, and here I am, just making things worse."
    him "I'm just glad you're okay now."
    "Gradually, he got better. He became familiar in our houses and we got to know a different side of him."
    "At first, it was helpful to have another adult around, and I learned some great recipes from Pavel."
    "He had a hard time finding words, and it was kind of frustrating to talk to him about anything abstract."
    "As his disease progressed, it was harder to for him to understand simple commands."
    him "Now wash your hands."
    pavel "I did."
    him "No, you didn't. Put your hands in the water."
    "He would wander through the house fiddling with anything that he happened upon."
    her "Soon you guys are going to need to watch him at the hospital."
    him "Why?"
    her "He'll stop using the bathroom. He'll need to be spoon-fed food."
    him "We can do it."
    "One day Julia was late coming to watch him, and Sarah left him alone."
    "Julia couldn't find him that night and we all started searching for him."
    "In the morning, we found his body drowned in the river."
    "His funeral was well-attended, and we reminisced about his optimistic spirit."
    return

label euthanasia:
    "After about a month, [her_name] announced that Pavel's euthanasia would be that week, and asked villagers to pay their final respects."
    "Pavel said goodbye to most of us. He wasn't completely present."
    "After [her_name] performed the euthanasia, we held a simple funeral where we celebrated Pavel's lifetime of good-natured optimism."
    return


label community29:
    #not sure if I want to end with a battle. It seems cliche. Maybe explore the jellypeople option more?
    "RET reports that they've heard from a miner that the luddites are hurting RET business interests."
    #it's an account from about 7 years ago? about the cattle thing, but indignently whiney and kind of overblown.
    "They give permission to use force against the luddites if they are hindering mining operations."
    #it goes to both the liason and the head miner. If you're not the liason, Sara calls a town meeting to discuss it.
    if ((luddites >= 12) and (miners >=12)):
        "Are the luddites getting out of hand?"
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
