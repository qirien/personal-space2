﻿## Community Events

# A short event that plays to introduce the community
# Feel free to change this if you want. It should be fairly short and remind
# everyone of the characters and situation.
label community_intro:
    play music community
    scene fields with fade
    "Luckily, we weren't alone on Talaam. There were several hundred other colonists here, now. Enough to feel like a real community, and not just  a few struggling pioneers."
    show pete normal at midleft
    show thuc normal at midright
    show natalia normal at center
    with dissolve
    # show Julia and Ilian?
    "There were some I got along with..."
    # show Thuc and Natalia and Pete?
    hide pete
    hide thuc
    hide natalia
    with dissolve
    show julia normal at midleft
    show ilian normal at midright
    with dissolve
    "...and some I didn't. But we all had one thing in common -- we worked hard to grow the food we all needed to survive on this planet, light years away from Earth."
    "They were our family here, whether we liked it or not, so like a family, we had our fights and jealousies and annoyances -- but we learned to get along."
    return

# New colonists arrive
label community1:
    play music happy
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
    show him normal at center
    "Some new colonists arrived from Earth, sent by Rare Earth Tech."
    "After the introductions, I got in line with my friend Thuc to have some soup."
    show him normal at midright with move
    show thuc normal at center
    show ilian happy at midleft
    with moveinleft
    thuc "It's pretty exciting to have some new faces around!"
    him surprised "Yeah, I hadn't realized how much I'd gotten used to all you guys until these new folks showed up. I'm surprised Julia's not here."
    thuc sad "She was... feeling pretty worn out."
    thuc normal "Is [her_name] still at work?"
    him concerned "Yeah, she wants to give the new colonists their first physical as soon as possible."
    ilian normal "I wish I didn't have to be here. After talking to people all day the last thing I want to see is more people."
    him happy "At least there's free soup."
    ilian "It's not free, it came from all those crops you paid to the storehouse! So if any of you gave subpar stuff, we're going to taste it."
    "We got our soup and I decided to sit with some of the new colonists."
    scene community_center with fade
    show him normal at midleft
    show zaina normal at center
    show kevin normal at midright
    with dissolve
    him "Hi, I'm [his_name]. Welcome to Talaam!"
    zaina "I'm Zaina, and this is my husband Kevin. I'd let him speak for himself but his mouth is full, so I'm socially obligated to be polite in his place."
    him determined "Nice to meet you, Zaina and Kevin. Where will you be living?"
    zaina "We've set up a house out by the radio tower. It's closer to the mountains where I'll be working. Geological studies, mostly."
    kevin "And after Zaina figures out where the goods are, I'm in charge of figuring out if it's even possible for us to mine."
    him surprised "Oh, right, that's Rare Earth Tech's plan to pay for this whole expedition."
    kevin "Yes. Usually when a company invests money into a research project they would do so with the expectation of making a profit."
    him concerned "I understand that from RET's point of view... but they sure aren't sharing any profits with us!"
    zaina "You can't be doing too bad. I haven't seen a single starving waif since I arrived."
    him surprised "That's true, but it's different from Earth. I hope you weren't planning on a life of luxury."
    kevin "No, I was not. I was planning on a life of adventure and discovery."
    show him normal
    menu:
        "What kind of life was I planning on?"
        "I'm going to focus on fulfilling my job to RET.":
            $ miners += 1
            him determined "RET went to the trouble of flying me out here, so I might as well fulfill my end of the bargain."
            him happy "Plus, growing food is essential for our survival!"
            kevin "That sounds like a good plan."
        "I came out here for adventure and discovery too.":
            him determined "I love the feeling I get when I look up at the sky and I can see thousands of stars."
            him happy "When I see plants and animals I've never seen before, I feel the thrill of discovery."
            him normal "I really have to exercise my creativity when I need to find solutions to problems with limited supplies."
            him determined "Nothing on Earth compares."
            kevin "I agree. There's so much to document and try, it's overwhelming."
            $ luddites += 1
        "At the end of the day, working together is what keeps me going.":
            him determined "It's amazing to colonize a new planet. There's nothing quite like looking at the sky and realizing how far away we are."
            him normal "At the same time, it's my relationship with my neighbors that I really cherish."
            him concerned "If we were working together on Earth, I'd be lucky to count one or two of my coworkers among my close friends."
            him normal "Here, there's no choice. We have to be close to one another to survive."
            him flirting "True, we're always in each other's business. But we're always helping one another too."
            kevin "It's kind of like you're a big family then?"
            him determined "No, it's different. Families don't always get to choose to be together."
            him normal "It's more like we're all united by a common goal."
            kevin "So it's like you're always at work."
            him surprised "Kind of, yeah."
            $ colonists += 1
    him happy "You guys are staying here for the rest of your lives, right?"
    zaina "That's right!"
    label ask_zaina_and_kevin:
    menu:
        "What should I ask them about?"
        "Are you planning to have children?" if not asked_kids:
            him determined "So... I know RET is trying to grow the colony..."

            him surprised "Are you planning on having kids?"
            zaina "We'll try. We haven't been able to have kids so far."
            kevin "That is not why RET sent us out here. Our geology and engineering skills are what they are interested in."
            $ asked_kids = True
            jump ask_zaina_and_kevin
        "Do you have family still on Earth?" if not asked_family:
            him surprised "Do you have family still on Earth?"
            zaina "I was an only child, and my parents recently died, so I don't have any family on Earth. I do have some friends still there though."
            kevin "My father and brother are still on Earth, but I do not regret leaving them."
            menu:
                "So you weren't close?":
                    him concerned "Huh. Don't get along with them?"
                    kevin "They are not men of science. They did not understand my passion for engineering, despite its obvious usefulness."
                    him normal "My parents are still on Earth. We have some extremely delayed correspondence."
                "You don't like them?":
                    him concerned "I take it you didn't like them very much."
                    kevin "They did not value me or my work. They ignored my accomplishments."
                    him surprised "How would you expect them to? They're probably not experts like you are."
                    kevin "If they had simply not understood my work, that would have been forgiveable."
                    kevin "They are not men of science."
                    him determined "My parents are still on Earth. We have some extremely delayed correspondence."
            $ asked_family = True
            jump ask_zaina_and_kevin
        "What kind of food will you grow?" if not asked_grow:
            him normal "You have quite a bit of land out there by the radio tower."
            him happy "Any idea what you'll grow on it?"
            zaina "We brought some fruit trees, which I hope will make a nice orchard."
            zaina "Grapes are fairly hardy, and I would love to start a winery sometime!"
            kevin "I am planning to try my hand at a basic vegetable garden."
            him surprised "Have you ever farmed before?"
            zaina "I practiced caring for fruit trees in the simulations on the shuttle."
            kevin "I also raised a magnificent patch of vegetables in the simulations."
            him determined "So the answer is no."
            kevin "The simulations have been updated since you flew over."
            kevin "They're quite lifelike!"
            him normal "Tell me how you feel about them after you harvest your first crops."
            $ asked_grow = True
            jump ask_zaina_and_kevin
        "How was the shuttle ride?" if not asked_shuttle:
            him flirting "Did you start to hate each other a little on the shuttle ride over?"
            kevin "No, I do not believe it is possible for us to hate each other."
            zaina "We got married right before the shuttle ride. So it was kind of like our honeymoon!"
            him happy "I got married right before coming to Talaam too."
            him surprised "Did people give you all kinds of weird survival gear at your wedding?"
            kevin "No, they did not. My friends from work are also engineers and understood the limitations of space travel."
            zaina "His college roommates gave him a custom mix of media! It had everything from the latest datasets to formulae to try."
            him normal "That sounds interesting. You should show Pete, our librarian. He gets excited about research and data."
            zaina "Some of my cousins gave me some hunting goggles. The battery on them wasn't compatible with RET solar technology though."
            $ asked_shuttle = True
            jump ask_zaina_and_kevin
        "I'm done asking them questions.":
            zaina "You've been here for a year, right? Can you tell me about some of the other colonists?" #not sure if this is necessary... too much exposition?
            him surprised "I guess I can."
            scene stars with fade
            label colony_gossip:
            menu:
                "Who should I tell them about?"
                "[her_name] and [kid_name]" if not tell_Kelly:
                    show her normal at center
                    show kid normal at center, baby_pos
                    with dissolve
                    him "I have a daughter, [kid_name] - she's about three Earth months old."
                    him "[her_name] is my wife and she's also the doctor in our clinic."
                    him "She tries to be objective, but she also feels passionate about her job."
                    zaina "I think that describes most of us."
                    show her determined with dissolve
                    him "Some people have complained that her bedside manner is a little callous."
                    him "So her objectivity is more relevant to customer satisfaction than, say, mine."
                    kevin "Are you implying that your carrots cannot feel your love?"
                    him "Correct. Unless that love manifests itself in better care."
                    hide her
                    hide kid
                    with dissolve
                    $ tell_Kelly = True
                    jump colony_gossip
                "Naomi and Pavel" if not tell_Graysons:
                    show naomi normal at midright
                    show pavel normal at midleft
                    him "If over the course of your lifetime you ever feel hopeless or depressed, go talk to Naomi Grayson."
                    him "She can't prescribe medicine for you, but she's very reassuring and can encourage you to get more help."
                    zaina "Reassuring? So she basically tells you to 'hang in there.'"
                    him "Somehow when she says it, it feels like she understands what you're going through. She has some training in cognitive behavioral techniques, too, as a therapist."
                    him "She also holds religious services every Sunday."
                    zaina "Do you go to those?"
                    him "No, but [her_name] does."
                    him "Naomi's husband, Pavel, is the mayor. I think you know him already."
                    hide naomi
                    hide pavel
                    with dissolve
                    $ tell_Graysons = True
                    jump colony_gossip
                "Dr. Lily" if not tell_Lily:
                    show lily normal at center
                    him "Dr. Lily is our resident scientist. She was here before most of the other colonists."
                    him "She tests plants to see if they're edible, and helps think of solutions to problems."
                    zaina "You said scientist, but what kind of scientist is she?"
                    him "Hmm. I guess she's a xenonaturalist? She looks at plants and animals, and does some chemistry on the side."
                    kevin "RET does prefer people who have multiple talents."
                    kevin "I'm also a shuttle pilot, for example."
                    him "Oh, really? When did you have time to learn that?"
                    kevin "Well, my father was an airline pilot, and I was transfixed upon the idea of flying as a youth."
                    kevin "After I obtained my pilot's license, I worked as a pilot for several years."
                    him "But at some point you decided to study engineering."
                    kevin "It wasn't enough to simply pilot a craft. I desired to know how they functioned as well."
                    him "Flying is pretty incredible."
                    hide lily with dissolve
                    $ tell_Lily = True
                    jump colony_gossip
                "Martín and Natalia" if not tell_Perons:
                    show martin normal at midleft
                    show natalia normal at midright
                    with dissolve
                    him "Martín and Natalia Perón grow beans and have chickens, and maybe turkeys, too? They have five kids. Or, well, four now, I guess."
                    zaina "Now?"
                    him "There was an accident... and their daughter died when she was four years old."
                    zaina "What a shame. What happened?"
                    menu:
                        "What should I tell them?"
                        "Pete ran over her with his tractor.":
                            him "Pete was driving his tractor and didn't see her in time..."
                            zaina "How awful. I bet he still feels bad about it."
                            him "The Peróns have a vigil every year to remember her."
                            zaina "Are accidents like that common?"
                            him "No, I mean, usually accidents aren't so bad that someone dies."
                            him "I'm not sure if Natalia will ever forgive Pete."
                        "She got run over by a tractor.":
                            him "She wasn't looking where she was going, and a tractor ran over her."
                            zaina "Was it a self-driving tractor or something?"
                            him "No, one of my friends was driving it."
                            zaina "Oh, I see. You don't want to tell me who it was before I get to know them."
                            him "Yeah. The Peróns are still pretty sad about it and hold a vigil every year where it happened."
                            # TODO: give bonus to luddites here?
                    him "Anyway, their kids are old enough to help around the colony a lot. Their oldest son just got married."
                    hide martin
                    hide natalia
                    with dissolve
                    $ tell_Perons = True
                    jump colony_gossip
                "Pete and Helen." if not tell_Pete:
                    show pete normal at midleft
                    show helen normal at midright
                    with dissolve
                    him "If you ever need to look something up or make something, our library is the place to go."
                    him "Pete is our librarian and also our cattle rancher."
                    him "He has a wife and a son about [kid_name]'s age. Travis, that's his name."
                    hide pete
                    hide helen
                    with dissolve
                    $ tell_Pete = True
                    jump colony_gossip
                "Thuc and Julia." if not tell_Ngyuens:
                    show thuc normal at midleft
                    show julia normal at midright
                    with dissolve
                    him "Thuc and Julia are my neighbors and some of our best friends."
                    him "They grow a lot of crops and are experts on, ah, human waste treatment?"
                    kevin "It is an efficient way to procure more fertilizer."
                    him "Also they have ten kids and Julia is a midwife."
                    zaina "Ten kids? That is a lot."
                    him "They fill our schoolroom nicely. It must have been a real pain on the shuttle though!"
                    zaina "Yeah, there's not exactly a playground on the shuttle."
                    hide thuc
                    hide julia
                    with dissolve
                    $ tell_Ngyuens = True
                    jump colony_gossip
                "I'm done talking about other people.":
                    scene community_center with fade
                    show him normal at midleft
                    show zaina normal at center
                    show kevin normal at midright
                    with dissolve
                    him happy "Well, it was nice to meet you both."
                    kevin "Undoubtedly we shall meet again."
                    zaina "We'll have to have you over for dinner sometime."

    #TODO: make longer discussion based on menu choice (this is the beginning of the game; we want some really dynamic choices at the start, even if they don't affect a lot)
    # Maybe something about building a park/playground for everyone?
    return

# 2 - bring whole harvest in to storehouse?
label community2:
    "I started running out of storage space in my cellar, so I took the extras over to the storehouse."
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
        kevin "Yes, a variety of foodstuffs is beneficial to anyone's diet."
    ilian "You know, Kevin and Zaina brought me everything that they harvested this week. Apparently that's the way we're supposed to have been doing it all along."
    him surprised "Huh, really? How in the world do you have time to farm?"
    kevin "I can't start my engineering calculations until Zaina finishes her assessment, so farming is a useful pastime."
    him annoyed "It might be an amusing pasttime for you, but it's our survival you're talking about here."
    kevin "I must depart, but I will take some of what [his_name] brought, if that's permissible."
    ilian normal "That's what I'm here for."
    hide kevin
    with moveoutleft
    show him normal at midleft with move
    ilian "We probably should start doing things the way it is in the contract."
    ilian "I know it seems less efficient, but it gives us more control in case of famine."
    him concerned "What if the storehouse burns down? Then we'll all have nothing."
    ilian "Or some alien varmint could eat it all no matter where it is."
    ilian "Look, I'm just telling you what our contract says. Do you want to read the fine print? I have it here on my tablet."
    menu:
        "Actually, yes.":
            call contract
        "No, I believe you.":
             $ pass

    ilian "Will you start bringing your whole harvest in or not?"
    menu:
        "Should I bring my whole harvest in to the storehouse?"
        "I can bring in the whole harvest.":
            $ colonists += 1
            $ miners += 1
            $ whole_harvest_to_storehouse = True
            him annoyed "How about I can write down the amount I harvest and I'll bring in the surplus?"
            ilian "I'm pretty sure I could trust you, but it's better if I can measure it all so we can be consistent."
            him determined "I'll weigh it all and document it with photos as well. And I'll bring in everything we don't eat."
            ilian "I suppose it would be silly to bring in crops that you were just going to take right back home with you to eat. As long as everything's accounted for..."
            him normal "Great, I'll do that."
            #TODO: make this add to the future stress variable
        "I will keep storing most of my own crops.":
            $ luddites += 1
            him annoyed "I'm not changing how I do things because of what some lawyer at RET said. I'll do what's efficient and good for everyone."
            ilian "Hmph. Well, we'll see how that works out."
    return

    label contract:
        nvl clear
        legalese "In return for your individually contracted compensation, Rare Earth Tech, hereafter referred to as 'RET', will provide supplies, technology, and infrastructure to RET Colonists."
        legalese "Farmers will farm 3 acres to the best of their ability as weather permits."
        legalese "All food farmed by RET Colonists and all livestock raised by RET Colonists is property of RET, to be rationed out by the Storehouse Manager"
        legalese "to all RET Employees according to the chart in Appendix C based on family size and estimated caloric consumption."
        legalese "Any Colonist not in accordance with this agreement will not be accorded Storehouse rations"
        legalese "and will be expected to return all RET property, including but not limited to technology, vehicles, furniture, tools, etc."
        legalese "Colonist couples of childbearing age must attempt to replace themselves through reproduction."
        legalese "Children of RET employees are also RET employees with regards to the legal status of their surplus goods."
        legalese "RET reserves the right to amend this document as it sees fit."
        nvl clear
        return

# 3 - Game Night!
label community3:
    play music exciting
    scene farm_interior with fade
    show thuc normal at midleft
    show him normal at center
    show pete at midright
    with dissolve
    thuc sad "No. No way! Did you just do that?"
    him happy "Yes, I did. With the bonuses from my cavalry, my legendary general, and my superior navy from starting on an island, I can conquer Russia in one turn!"
    pete "That's the last time I let you start as Tonga!"
    thuc normal "I think you just won the game."
    him surprised "I don't know, there might be a way for you to make a religious conquest!"
    thuc sad "Nope. I resign."
    pete happy "Well, that was a good game. I should have situated myself better from the beginning. I got caught up in collecting gold instead of buildin' an army."
    him normal "Same time next month?"
    pete happy "Yes, I reckon so. I'll remind you on the community bulletin."
    him concerned "Can we call it something other than game night? All the new colonists will think we're a bunch of nerds."
    pete normal "Well, we are a bunch of nerds."
    him determined "Fine, then they'll believe me when I tell everyone we're doing an 'intensive research session.'"
    pete happy "Ha! Fine by me. As long as everyone else calls it that they'll be none the wiser."
    scene fields with fade
    show him normal at midright
    show kevin at midleft
    "A few months later, Kevin asked me about it after I assessed his first batch of crops."
    kevin "I keep seeing people attending 'intensive research sessions' on the colony calendar. What are they?"
    him concerned "Oh, those. It's just people talking to Pete about stuff."
    kevin "Talking to Pete? About fieldwork?"
    him normal "I happen to have some research interests outside of fieldwork."
    kevin "He's a librarian, right? Is your hobby art history or something similar?"
    him happy "No, it's far more mundane. That's just what we call our monthly game night."
    kevin "I would love to play games with others. Why was this information hidden?"
    him concerned "I guess... I didn't want the new colonists to think I was being frivolous with my time."
    kevin "Face-to-face socialization is highly recommended by RET's psychologists."
    kevin "It may feel frivolous, but it can actually increase your productivity."
    him normal "But farmers a long time ago didn't have time to play cards. They worked from sunup to sundown without complaining."
    kevin "That's simply what they told their grandchildren. Let me come to your game night!"
    him happy "Yeah, you should! We need someone to shake things up."
    kevin "Shall I invite the other new colonists as well?"
    menu:
        "Sure, invite them all!":
            him normal "Yes, let's invite them. I can reserve the community center."
            $ colonists += 1
            $ town_hall_games = True
            jump invite_all
        "Don't invite them.":
            him determined "They can make their own game night if they want."
            him normal "I want to enjoy myself, not be teaching other people how to play games the whole time."
            $ luddites += 1 #rationale: the luddites are a product of the colonists becoming more fractured
            jump no_invite
        "Ask Pavel to encourage meetups":
            him normal "I'll ask Pavel, the mayor, to remind them to make socialization a priority."
            jump ask_pavel

    label invite_all:
        scene community_center with fade
        show kevin at left
        show thuc at midleft
        show him at center
        show sara at midright

        "Next month, we invited everyone to town hall to game night."
        "A handful started a poker game at another table, but Kevin wanted to join our game instead."
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
    play music community fadeout 3.0 fadein 3.0
    scene community_center with fade
    show pavel normal at center
    "Pavel, our mayor, called a town meeting."
    pavel "Rare Earth Tech sent us an instantaneous message. It's a bit short, but they only have 250 characters, you know."
    pavel "They said:"
    $ pstyle = get_parenting_style()
    if (pstyle== "authoritative"):
        ret_c "Please elect a liaison to help RET & colonists communicate & resolve conflicts."
    elif(pstyle == "authoritarian"):
        ret_c "You must choose a liaison. Must be someone trustworthy, flexible, to work with colonists and us."
    elif(pstyle == "permissive"):
        ret_c "We think it would facilitate interactions between RET and colonists, if you could pick one person as a liaison..."
    else:
        ret_c "Please elect a liaison to help RET and colonists communicate and resolve conflicts of interest."
    pavel "It's my job to encourage whatever is best for the colony."
    show pavel sad #TODO: this transition is weird... but is it weirder to keep him in the same pose for so long? His arm gets tired!
    pavel "I don't want you to ever question my loyalty. We need someone else for this job."
    pavel normal "The liaison will have to understand what RET will want and tell them what's possible and what's not."
    pavel "They'll have to tell us what RET wants and convince us to change if necessary."
    pavel sad "There may be times when you have to make unpopular decisions, or take the blame for mistakes that weren't yours."
    pavel normal "I doubt anyone will volunteer for extra work, so I'd like everyone to nominate someone tonight."
    pavel "Then we'll vote on the nominations."
    hide pavel with moveoutright
    show thuc normal at midright
    show him normal at center
    show lily normal at midleft
    with dissolve
    thuc "Wow, who has time for that extra work? It's hard enough just raising five goats and ten kids."
    lily "I could take on additional duties, but I anticipate that my personality is not well-suited for liaison work."
    him happy "At least you know your own personality well, although I think that you don't give yourself enough credit."
    lily angry "I may occasionally enjoy the company of others, but I would prefer not to negotiate between two parties."
    show pete normal at quarterleft with moveinleft
    pete normal "We need someone who'll stand up for us. Speak out against their stupid rules."
    him concerned "But it needs to be someone tactful, or else RET won't listen to them..."
    hide pete with moveoutleft
    lily normal "Who do you think would be a good candidate for liaisonship?"
    him determined "Hmm... Naomi seems like someone who could de-escalate conflict well."
    thuc sad "But she's married to Pavel, so she might have a conflict of interest..."
    him surprised "How so?"
    thuc "Like if she had to choose between the best choice for RET or something Pavel would be happy with, she might choose what Pavel would want for the sake of their marriage."
    him determined "I don't think she would do that. She can make tough decisions."
    lily happy "I believe Thuc has a valid point. We're endeavouring to nominate someone independent from Pavel."
    show naomi normal at quarterright with moveinright
    naomi "Hello everyone, have you thought of someone to nominate?"
    him "I was thinking of nominating you, but Thuc and Lily said that would defeat the point of making the liaison separate from Pavel."
    naomi sad "Pavel and I are in frequent, close contact. Also, I would almost certainly choose to put the colonists's needs first."
    him happy "Isn't that what we want from a liaison?"
    lily "What does 'putting the colonists's needs first' mean in this context? Our survival has been RET's main goal with establishing this colony."
    him determined "RET didn't really explain why we need a liaison."
    lily normal "Regardless, I must choose someone. What do you think of Sara?"
    him "Well, she helped Pavel out with some administrative stuff, so she's familiar with the bureaucratic work."
    naomi happy "Now that Oleg is a little older, she might be up to something like this."
    him concerned "Maybe. Oleg is about the same age as [kid_name], and she's still quite the handful."
    naomi "What about you? You don't have close ties to Pavel, so we don't have to worry about a conflict of interest there."
    lily happy "And based on your relationships with other colonists, your socialization skills are at least average."
    thuc happy "Yeah! Let's make [his_name] do it!"
    him surprised "Hang on. I already feel pretty busy just with farming committee meetings, raising [kid_name], and the farming stuff."
    naomi "We're all busy. Someone has to do this."
    lily normal "This discussion has helped me decide who to nominate. Thank you."
    hide lily with moveoutleft
    hide naomi
    hide thuc
    with moveoutright
    menu:
        "Who should I nominate? I can't nominate myself."

        "Sister Naomi. She'll do what's best for everyone.":
            $ colonists += 1
        "Sara. She's familiar with colony politics since she assists the mayor.":
            $ miners += 1
        "Pete. He'll make sure RET doesn't get too much control.":
            $ luddites += 1
    "After the nominations, we voted for our favorite candidate."
    $ pstyle = get_parenting_style()
    if (pstyle== "authoritative"):
        "My fellow colonists elected me to be the new representative."
        $ is_liaison = True
        return
    elif(pstyle == "authoritarian"):
        "Sara, and Sister Naomi and I were nominated. I had the most votes, but not by much."
        $ is_liaison = True
        return
    elif(pstyle == "permissive"):
        "I was nominated, but Sara was elected as the new representative."
        return
    else:
        "Sara is elected as the new representative."
        #TODO: should a leader of the militia be elected here as well?
    return

# 5 - Set aside food for miners?
label community5:
    $ talked_cans = False
    $ talked_credits = False
    $ talked_something = False
    $ talked_canning_dairy = False
    show farm_exterior with fade
    "Zaina and Kevin discovered indium and some other valuable resources nearby and developed a mining plan."
    "They said RET was sending a shuttle of miners that would arrive in several years."
    # It will take 4 Earth years for the miners to arrive. About 8 Talaam years.
    # context/scene for this decision? is it a town meeting? you, Ilian, sara, Pavel?
    if is_liaison:
        "RET sent me an instantaneous communication with advice on how to proceed."
        "It said:"
        $ pstyle = get_parenting_style()
        if (pstyle== "authoritative"):
            "50 new miner neighbors are coming in 4 Earth years. Plz feed them when they come."
        elif(pstyle == "authoritarian"):
            "50 miners are arriving in 4 Earth years. Prepare 2 feed them, and create $ so that they can pay u 4 what they eat."
        elif(pstyle == "permissive"):
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
            ilian "Based on the harvests of those farmers, we can probably grow and store enough food for the miners, but they will have to eat a lot of potatoes and beans."
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
                $ miners -= 1
                jump no_formal_rationing
    else:
        scene community_center with fade
        show sara normal at midright
        show him normal at midleft
        "Sara called you in to discuss the latest news from RET."
        sara "RET is sending miners to start mining the indium that Zaina and Kevin found."
        sara "The miners won't arrive for another four Earth years."
        if (whole_harvest_to_storehouse == True):
            sara "Ilian tells me that we'll have enough food for them if we start storing a little now."
        else:
            sara sad "We're not sure if we'll have enough food for them or not."
        sara normal "We will start storing the surplus of food that keeps the longest. I've started construction of a few silos for dried grains and beans."
        sara "Next harvest we'll start accepting canned goods as well. You can can large amounts in the storehouse, or bring in what you can at home."
        sara "Your hard-won crops won't go unnoticed. Starting today, we'll be issuing encrypted digital currency to pay for your crops, which you can use to buy luxury goods that are coming with the miners."
        sara "I'll be grading your crops against the RET standards."
        show sara sad
        sara "There's something I need your help with though. Some of the other farmers aren't excited about storing their surplus in the storehouse."
        show him surprised
        him "Really? Like who?"
        show sara
        sara "Pete and Martín are the ones you know the best."
        show him determined
        him "I'll talk to them." #this could also be a choice... how neglectful do you want to be
        $ rationing = True
        jump talk_about_food_storage
        # TODO: when/where are crops preserved?  Does Ilian have machines/employees that do this? Or are farmers supposed to do this before taking to the storehouse?
    return

    label whole_harvest_required:
    him determined "Let's have the farmers bring their whole harvest to the storehouse, so you can measure it."
    him normal "I'll ask them to start farming more beans and wheat too, since those store well."
    ilian happy "I'll need some help to build silos for the wheat."
    him surprised "This way we'll definitely have enough for the miners, right?"
    ilian normal "Yes. They won't even need to forage, unless they want some extra meat."
    him normal "Good. I don't want any trouble with RET."

    label ration_harvest:
    ilian "I support your plan, but not everyone' as enthusiastic about this. Some of the other farmers are reluctant to centrally locate food."
    him surprised "Oh? Like who?"
    ilian "Like Pete and Martín."
    show ilian happy
    ilian happy "I think they'd listen to you if you tried to persuade them though."
    him concerned "How do you think I should do that?"
    ilian normal "Make sure they know we'll pay credits for their surplus, which they can use to buy other crops."
    him determined "I'll talk to them."

    label talk_about_food_storage:
    scene farm_exterior with fade
    show him normal at midright
    show pete normal at midleft
    him "Hey Pete. How are your cattle doing?"
    pete happy "Surprisingly hale for living on an alien planet."
    him determined "Great. There's something I want to ask you about."
    him concerned "I heard that you're not storing much surplus in the storehouse."
    jump pete_no_storehouse

    label no_formal_rationing:
    him annoyed "We can figure it out when they get here. Growing food for miners wasn't in our contracts, so it sets a bad precedent to save food for them."
    him "Worst-case scenario, they have to farm for a bit instead of mining all the time."
    ilian normal "Are you sure? I don't really want to be eaten if we run out of food."
    him determined "I think people could survive on the wild resources available, as long as they know what they are."
    ilian "Yeah, I bet if we cross our fingers I'm SURE food will just APPEAR somehow."
    him annoyed "'Somehow' meaning they'll have to work just like we do for food. Nothing wrong with that."
    return

    label pete_no_storehouse:
    show pete
    pete "This climate is so wet that no amount of salting and drying will make jerky last four Earth years."
    pete "Cheese doesn't keep well, either, for the same reasons. The best way to store my surplus is to keep growing this herd."
    label convince_Pete:
    menu:
        "Is that really the best way?"
        "We could can some of the meat." if not talked_cans:
            show him normal
            him "I know canned meat doesn't taste very good compared to fresh, but it will keep for longer."
            him "How about it?"
            pete "I don't think anyone should have to eat canned meat, not when they live next to me! I mean, which would you rather have, spam or steak?"
            him "Good point."
            $ talked_cans = True
            jump convince_Pete
        "You'll need credits to get other food." if not talked_credits:
            him concerned "Even if the best way to store cow meat is on a live cow, you're still going to need to eat something other than milk and meat."
            him surprised "How will you afford vegetables and grain?"
            pete happy "Plenty of people are willing to trade for or buy milk and beef."
            pete normal "Ilian is just acting as a middleman. I don't like that he controls all the prices of food either."
            pete "I prefer to deal directly with my customers."
            $ talked_credits = True
            jump convince_Pete
        "If we canned some beef, then we'd have meat even if your herd died suddenly." if not talked_something:
            him surprised "What if one day you wake up and your whole herd of cattle is gone?"
            him determined "If you canned some meat, then we would at least have something."
            pete happy "That's true. But the herd is so small now that I need every cow and bull for good genetic diversity."
            pete normal "Plus I think canned meat is revolting. I would rather just eat vegetables."
            $ talked_something = True
            jump convince_Pete
        "We could can some of the dairy products." if not talked_canning_dairy:
            him normal "We could try making dried milk powder or clarified butter, which would last a long time."
            pete normal "Why would we do that when we have plenty of fresh stuff?"
            him determined "Well, I know cows don't produce consistently. So you could have some dairy on hand in case your cows don't eat as much."
            him surprised "Or they could end up eating some plant that makes the milk taste bad, so you'd be missing out on an opportunity to sell."
            pete happy "Hmm. That is a good point."
            show pete
            $ talked_canning_dairy = True
            jump convince_Pete
        "Just think about it, okay?":
            him concerned "I know it's difficult to store beef and dairy that long. Just think about maybe storing some long-term."
            pete normal "All right, then."
            jump canning_dairy

    label canning_dairy:
    if talked_canning_dairy:
        pete happy "I'll take a look at canning milk and butter."
        him happy "Great!"
        $ colonists += 1
    scene path with fade
    "Next I had to try to convince Martín..."
    scene fields with fade
    show martin at midleft with dissolve
    show him normal at midright with moveinleft
    him surprised "So Martín, how's your farm doing?"
    martin angry "Not so good. Some of our turkeys got sick, and when they died we couldn't eat them because the meat was contaminated."
    him concerned "Oh man, that's rough. Are your beans doing okay, at least?"
    martin happy "Yes! We eat them about as fast as we can grow them."
    him normal "I was thinking if you had some extras, you could can them and store them in the storehouse."
    show martin
    martin "I would if I we had extras. But we're usually trading them to other people for their crops."
    martin "You should know that. [her_name] usually trades vegetables for our eggs and corn."
    if require_whole_harvest:
        him determined "From now on, you'll need to bring in your harvest to Ilian if you want other crops."
        him concerned "We need to prepare to feed the miners, and this is the easiest way to ensure that everyone has enough food."
        martin angry "What if I don't want to do that?"
        him annoyed "It's in your contract."
        martin normal "Well, the way we've been doing it is working just fine."
        him concerned "We didn't have fifty extra mouths to feed then."
        martin angry "And we don't now! I think you're overreacting. We have plenty of food."
        him determined "How about you prove that I'm overreacting by bringing all your food to Ilian so we know what we have to work with?"
        martin normal "We eat most of our crops soon after harvesting them. We store just a little extra."
        him determined "I get what you're saying. Just write down how much you eat and tell Ilian."
        him normal "Then if you have extra, bring that in and he can calculate our food surplus."
        martin angry "Seems like a lot of work for nothing. But I don't really have a choice, huh?"
    elif rationing:
        him determined "Starting from now on, I need you to bring in twenty percent of your harvest."
        him concerned "That number may change, but this is the easiest way to start storing a little food for the miners."
        martin angry "Twenty percent? I don't have enough food to bring in twenty percent!"
        him concerned "Then bring in ten percent. Just try to keep track so we have an idea of how much food we have collectively."
        martin "Seems like a waste of time... but I'll do it."
        him normal "Thank you. This will help us calculate our food production and surplus."
    else:
        him determined "It works well now, but soon we'll be trading credits instead of food."
        martin happy "I'm happy to take your credits then."
        him normal "Okay, well if you ever need more credits, you can always sell your beans to Ilian."
        martin "Okay, will do."
    return


# 6 - discussion of choice from 5 at game night
label community6:
    play music exciting
    if town_hall_games:
        scene community_center with fade
    else:
        scene farm_interior with fade
    show pete normal at midright
    show him normal at left
    show thuc normal at midleft
    show helen normal at quarterright
    show kevin normal at quarterleft
    with dissolve
    thuc "I brought 'Maximal Conquest' tonight, are you guys up for it?"
    kevin "I have read the rules and watched the tutorial. I am prepared to join you."
    him determined "Yes, and I promise to start in the Northern Hemisphere this time."
    pete happy "Your Antarctica strategy had no sense whatsoever."
    him angry "Trying the same losing strategy every time and hoping it will win has no sense."
    pete normal "I'll make you eat your words."
    him surprised "Hey, if you're both here, where are your kids?"
    helen "They're sleeping. Sister Naomi's there, just in case."
    him normal "Cool. I tried to convince [her_name] to use the radio as a baby monitor, but [her_name] sometimes takes a long time to get to sleep so we didn't think it would work."
    pete normal "Hey, can we keep score on your tablet? Ours is out for repairs."
    him surprised "What do you mean? Don't you both have one?"
    helen "No, because SOMEONE left it out during a solar flare."
    pete happy "And SOMEONE left their tablet in spittin' distance of a cow."
    him concerned "That must be rough."
    pete normal "Nah, it's better. I used to check my tablet for new messages all day long. I haven't checked them for a week and I haven't missed anything."
    pete happy "Instead I'm living more in the moment. I don't even mind doing my feed calculations for the cattle by hand."
    helen happy "I miss watching Skulls of Iron. But at least one of the tablets is repairable, so we should be back to our normal selves soon."
    pete normal "You can keep it. I like feeling like I'm completely on my own, getting away from all the drama in town and online."
    thuc sad "But you're still having game night, and you have your family, too, so it's not like you're completely isolated."
    menu:
        "What do you think?"
        "We need each other to survive.":
            $ colonists += 1
            him determined "We need each other to survive. There's no way one person could survive on their own out here."
            pete happy "Is that really true? I've been out there on my own before--there's good foraging and hunting."
            him surprised "Maybe you could survive on your own, but what about your family?"
            pete normal "They can help forage, too!"
            pete "The most dangerous thing is the solar radiation. Without a radio, we wouldn't know when a solar flare was coming."
            pete happy "And it's handy to have some folks around. Otherwise, who would I crush in Maximal Conquest?"
        "I understand wanting to be away from it all.":
            $ luddites += 1
            him determined "I understand wanting to be away from it all. It's part of the reason I came here."
            pete happy "We don't have to deal with inane government interference or rules made just for the sake of havin' 'em."
            him concerned "Although some of RETs demands have felt that way..."
            pete normal "True. But you can see where they're coming from for the most part."
            pete happy "And they're not in our face about it. I could go set out on my own tonight and they'd be none the wiser."
            helen "You could, as long as you planned it out with your wife first."
        "We have an obligation to help RET feed their miners now.":
            $ miners += 1
            him determined "Being alone sounds romantic, but we have an obligation to help RET feed their miners now."
            him concerned "If we all went rogue, those miners would starve to death. And we wouldn't be holding up our end of the bargain. It was expensive to send us out here."
            pete happy "I do feel bound by my word. But if RET starts askin' more than was in our contracts, I might have to change things, too."
            him surprised "What do you mean?"
            pete normal "What if we don't have enough food for all these miners?"
            pete "If that happens, you bet I'm going to look after me and my own first."
            pete "We're promised enough food to live off of, but if that doesn't exist, there's no way RET can make it right."
            pete happy "We're all trying to farm as efficiently as we can. But if RET overestimated our yields, I don't want to pay for it."
            him concerned "Good point. I hope we can manage."
    if require_whole_harvest:
        $ rationing = True
        $ require_whole_harvest = False
        thuc normal "Speaking of food, Ilian just sent out a message that we don't have to bring in all the surplus anymore."
        thuc "He has enough data, and he sent out a table of who should bring in how much."
        thuc "It ended up being about twenty percent for most farmers." #TODO: is this a reasonable amount?
        pete normal "I deliver directly to my customers, so I've just been sending Ilian my stats."
        thuc sad "I guess it doesn't really make sense to bring in a calf to the storehouse."
        pete happy "Nope."
        him happy "It was a little more work to bring in all my crops, but I think I had a better variety of fresh food that way."
        thuc normal "And in comparison, twenty percent of our crops seems pretty easy to bring in!"
    return

# 7 - Comparing compensation
label community7:
    play music thoughtful
    show community_center with fade
    show zaina normal at center with dissolve
    zaina "The fossil record near here contains many invertebrates that do not have shells. If they had been merely eaten to death, we wouldn't have their fossils."
    zaina "One possibility is that an area that used to be part of the ocean became locked into one area, and they ate up all possible prey."
    zaina "Another possibility is that solar flares are a geologically recent event, and that they died quickly once the flares started."
    zaina "However, the existence of other animals at the same time with shells that are resistent to radiation makes it likely that the solar flare problem was cyclic."
    show zaina at midright with move
    show pavel normal at midleft with moveinleft
    pavel "Thank you, Zaina, for the presentation on Talaam's probable geologic history."
    hide zaina with moveoutright
    show pavel at center with move
    pavel "We want you to feel that your fellow farmers are co-workers, so please use this time to talk to them."
    pavel "I know you're all very busy, so we've provided some delicious snacks to encourage you to stay!"
    hide pavel with moveoutright
    show kevin at midright with moveinright
    show him normal at midleft with moveinleft
    kevin "I'm surprised that they're offering incentives. The excitement of living on a new planet was sufficient payment for Zaina and I to come to Talaam and socialize."
    him surprised "RET didn't give you any money? At least I know that my parents are taken care of."
    kevin "What do you mean?"
    him happy "RET gave me a bunch of money that I used for their retirement fund."
    kevin "They made me no such offer."
    show him at center with move
    show thuc normal at midleft
    show helen normal at quarterleft
    with moveinleft
    show ilian normal at quarterright
    with moveinright
    thuc "I practically had to pay RET to let me come. What gives?"
    him annoyed "Huh. You're basically giving up your lives on Earth, so I'm surprised that they didn't offer you some kind of compensation for that."
    ilian happy "Maybe some of us were happy to leave our Earth lives behind."
    helen happy "This is a new one for me. Ilian has a secret past?"
    ilian normal "There's nothing secret about it. I was about to default on my loans for my restaurant supply store."
    ilian "RET said they would take care of it."
    helen normal "Do you know if they did?"
    ilian happy "I haven't heard from any debt collectors since."
    kevin "You may have noticed it's very difficult for people on Earth to contact you here."
    ilian normal "It was win-win for me."
    kevin "I was so intent on coming to Talaam that I didn't think to negotiate compensation."
    hide ilian with moveoutright
    thuc sad "I wish I had thought of negotiating too. Now that I think about it, they really needed me."
    him flirting "Oh come on. They could have found some other sustainable agriculture specialist with 10 kids."
    thuc normal "Or 8! Fewer pieces to ship."
    kevin "Did your children suffer developmental delays because of the journey?"
    thuc sad "One of them is a little shorter than the rest, but other than that I'd say that being on a different planet has accelerated their development."
    thuc normal "They're not necessarily reading sooner, but we genuinely need their help on the farm."
    thuc "They have more responsibilities than I did at their age, so they have to grow up fast."
    thuc sad "But, unlike [his_name], none of my family are getting paid for our work here."
    if is_liaison:
        thuc normal "Hey [his_name], can I make a formal request? I'd like RET to donate $10,000 to the charity of my choice."
        menu:
            "What will you do for Thuc?"
            "Ask RET in my next e-mail.":
                $ miners += 1
                him normal "I can ask them in my next e-mail."
                thuc sad "E-mail? Not an insta-com?"
                him happy "I only get so many instant communication slots."
                thuc normal "But by the time they get your e-mail no one will remember me."
                him determined "I think RET has bigger things to worry about."
                thuc sad "Fine, an e-mail is fine."
            "From a business standpoint, you're stuck here.":
                $ luddites += 1
                him annoyed "You don't have any leverage over them. It's not like you can quit now."
                thuc sad "I sure do have leverage! I could decide to leave the colony!"
                him concerned "You wouldn't seriously consider that."
                helen happy "I don't know, he looks pretty serious."
                thuc normal "I'm joking. Rice cultivation is kind of pointless for just twelve people."
                thuc sad "I just don't like the idea that I have no power over my life."
            "I hear you, but let's focus on the here and now.":
                $ colonists += 1
                him determined "I could ask them in an e-mail. But what about all the rest of the new colonists who didn't receive compensation either?"
                him happy "Get stinking rich off your enormous farm and have a feast to make us all jealous."
                thuc normal "You do have a point. With my new crop of fertilizer I'll be stinking at least!"
    else:
        hide kevin with moveoutright
        show sara normal at midright with moveinright
        thuc normal "Hey, Sara, help me out here. Could you ask RET to send my back pay to the charity of my choice?"
        sara sad "I heard that RET is economizing, but I can ask."
        thuc sad "Thanks. Do you think RET will do anything, [his_name]?"
        menu:
            "What do you think RET will do for Thuc?"
            "They should make a big donation.":
                $ miners += 1
                him determined "They should make a big donation in your name."
                thuc normal "Right?"
                him surprised "What charity would you choose?"
                thuc sad "Something to promote sustainable agriculture in developing nations like this one."
                him flirting "I think the biggest contribution you can make to our developing nation is to keep your goats out of my spinach."
                thuc normal "Burn!"
            "They won't do anything.":
                $ luddites += 1
                him concerned "You're stuck here. You have no choice but to be an employee of RET."
                thuc sad "I could decide to leave the colony!"
                show him surprised
                him surprised "You wouldn't seriously consider that."
                helen sad "I don't know, he looks pretty serious."
                thuc normal "I'm joking. Rice cultivation is kind of pointless for just twelve people."
                thuc sad "I just don't like the idea that I have no power over my life."
            "They probably won't do anything, but we have more important things to worry about.":
                $ colonists += 1
                him determined "Life isn't fair, but if we work hard, maybe we can eat well while we live it."
                show him happy
                him happy "Get stinking rich off your enormous farm and have a feast to make us all jealous."
                thuc happy "You do have a point. With my new crop of fertilizer I'll be stinking at least!"
    return

# 8 - What luxuries should RET send?
label community8:
    $ talked_to_Natalia = False
    $ talked_to_Thuc = False
    $ talked_to_Sara = False
    $ talked_to_Kevin = False
    $ talked_to_Pavel = False
    $ talked_about_luxuries_counter = 0

    if is_liaison:
        scene farm_exterior with fade
        "Urgent insta-com from RET!"
        $ pstyle = get_parenting_style()
        if (pstyle == "authoritative"):
            "Have 10kg xtra space on the shuttle. What Earth luxuries needed?"
        elif(pstyle == "authoritarian"):
            "Tell us what extras to put on the shuttle by this evening."
        elif(pstyle == "permissive"):
            "If u want Earth goods, tell us what u want by 2night!"
        else:
            $ no_luxuries = True
            jump luxuries_absent
        "RET must be talking about the shuttle coming with the miners."
        "I'm not sure why they couldn't have asked about our preferences sooner."
        "I'd really like some good Earth toilet paper. [her_name] wants some Gouda cheese culture."
        "I need to find out what everyone else wants too, and send a brief message summarizing it. TODAY!"
        label talk_about_luxuries:
            if (talked_about_luxuries_counter >= 4):
                if is_liaison:
                    him surprised "Oh, it's already the afternoon! I need to send in my report right away."
                    jump write_report
                else:
                    "I told Sara what everyone wanted, and she wrote the report."
                    return
        scene farm_exterior flip with fade
        "Who will I talk to about what Earth luxuries they want?"
        menu:
            "Natalia" if not talked_to_Natalia:
                show him normal at midleft
                show natalia normal at midright
                with dissolve
                natalia "I don't care what else comes from Earth, but there had better be some medication for Martín in there. The longer he lives, the happier our family will be."
                him concerned "What medication does he need?"
                natalia "[her_name] said he needed Vemurafecholoronib. Let's see... 500 mg for six months and 1000 mg for another 6 months."
                him surprised "Won't RET be sending this anyway?"
                natalia "They told [her_name] that it wasn't possible, but maybe you can do something."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Natalia = True
                jump talk_about_luxuries
            "Thuc" if not talked_to_Thuc:
                show him normal at midleft
                show thuc normal at midright
                with dissolve
                thuc sad "I'd like to grow peanuts. They have to be raw, though, or I can't plant them."
                thuc normal "Then I can make peanut stew and peanut butter!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Thuc = True
                jump talk_about_luxuries
            "Sara" if not talked_to_Sara:
                show him normal at midleft
                show sara normal at midright
                with dissolve
                sara "Oh, I don't know if this is possible, but I would really, really love a bicycle."
                sara sad "I'm terrible with horses and I hate how they just eat more of our food."
                sara normal "A bicycle wouldn't get hurt by radiation and can go faster in some situations. And maybe Oleg can ride it when he gets older!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Sara = True
                jump talk_about_luxuries
            "Kevin" if not talked_to_Kevin:
                show him normal at midleft
                show kevin normal at midright
                with dissolve
                kevin "This is an extremely inefficient way to gather information. Could you not have contacted me electronically?"
                him determined "Yes, but you might not have responded in time. I need to tell them by the end of the day!"
                kevin "Very well. Are they sending new tablet batteries like I requested?"
                him happy "Yes, yes, don't worry about that. Ask for something that will boost your morale."
                kevin "Wouldn't being reminded of the Earth I'll never return to lower my morale?"
                him normal "It sounds like you don't want anything."
                kevin "I would like the remaining episodes of the show Tulip House."
                $ talked_about_luxuries_counter += 1
                $ talked_to_Kevin = True
                jump talk_about_luxuries
            "Pavel" if not talked_to_Pavel:
                show him normal at midleft
                show pavel sad at midright
                with dissolve
                pavel "Oh, there are so many things I miss."
                pavel normal "Sushi, wine, tempura, Krem de la Krem donuts, French fries, falafal, fried chicken,"
                pavel sad "those really cheap frozen pizzas from Glosemitto's, slow-roasted coffee, Fabrielle brand pelmeni,"
                pavel normal "sourdough bread, calamari, egg rolls but especially the sweet-and-sour sauce with lots of high fructose corn syrup,"
                pavel sad "Goods Inside cereal, homogenized milk, cotton candy, cheesecake, tuna salad, Michele's meat-alike paste,"
                pavel normal "really hot salsa, tortillas, curry powder, Chocolate Confession ice cream, and Swiss cheese, or any cow cheese really."
                pavel sad "And that's just the {b}food{/b} I miss!"
                him surprised "Wow. Well, it needs to be non-perishable or at least have a long shelf life, so I think that eliminates most of the things on your list."
                him normal "I could put you down for curry powder though."
                pavel sad "Oh, well make sure it's PatiPal's Extra Hot Curry Powder. It's the only one worth having."
                him determined "I'll see what I--"
                pavel normal "Wait, wouldn't it make more sense to grow the spices so I can make my own curry powder?"
                him normal "Sure."
                pavel "Okay, so just ask them to send me seeds for all the spices in PatiPal's Extra Hot Curry Powder along with a recipe."
                him concerned "Hmm. I need to put this in an insta-com."
                pavel sad "Oh dear. How did they not tell you about this sooner?"
                him sad "I think they only knew about the extra space on the shuttle this morning."
                pavel normal "You are going to have to cram a lot into that message!"
                $ talked_about_luxuries_counter += 1
                $ talked_to_Pavel = True
                jump talk_about_luxuries
        label write_report:
            if talked_to_Natalia:
                "I don't have enough room to ask for Martín's specific medicine and dosage and all the other things people wanted."
                menu:
                    "What should I write?"
                    "Specify the medication and dosage. Do your best with the other stuff.":
                        $ asked_only_medicine = True
                        return
                    "Maximize happiness and ask for everyone else's stuff specifically.":
                        return
            else:
                "I squeezed in as much as I could."
                return
    else:
        show fields with fade
        show sara normal at midright
        show him normal at midleft
        with dissolve
        sara "RET just told me that they have extra space on their shuttle and they can send some extra things from Earth to us."
        sara sad "What would you like?"
        him determined "Let me think about that."
        sara normal "I need to know right now."
        him happy "Hmm. How about some good old Earth toilet paper?"
        sara "Great. I can shorten that to TP in the insta-comm."
        him flirting "Hopefully they won't send me a textbook on Topological Planning."
        sara sad "Don't get your hopes up. But look on the bright side: in four years you probably won't even remember what you asked for!"
        him determined "How is that looking on the bright side?!"
        sara normal "Hey, could you help me ask everyone else what they want? I have a list here of people you know and could ask pretty easily."
        him normal "Okay, yeah, I can do that."
        jump talk_about_luxuries

    label luxuries_absent:
        scene farm_interior with fade
        show him determined at midleft
        show her normal at midright
        with dissolve
        him concerned "Man, I really miss Earth toilet paper."
        her happy "Wouldn't it be great if RET sent some on the next shuttle?"
        him determined "Yeah, that's never going to happen."

    return

# 9 - camping with Pete
label community9:
    scene pond with fade
    show pete normal at midright
    show him normal at midleft
    pete happy "Hey, [his_name]!"
    him happy "Hi Pete."
    pete normal "Out to catch some fish?"
    him normal "No, just taking a walk."
    pete "How's the farm?"
    him "Not bad. Just finished all the planting for the season."
    pete "Don't see you much since we quit having guy's night."
    him concerned "Yeah, that was fun, we should do that again."
    pete "I'm going hunting this weekend. Come along if you want."
    him surprised "Really? Where?"
    pete happy "I'm gonna hike out a couple klicks, spend the night, then see if I can get one of those big grass crabs."
    him determined "Overnight?"
    pete normal "Yeah, the grass crabs avoid the towns and farms - they like wide grassy areas."
    "What do I tell Pete?"
    menu:
        "Sounds fun! Go with him and invite Thuc.": #you learn the particulars of how to camp safe from radiation.
            $ luddites += 1
            $ colonists += 1
            him normal "That sounds fun. We should invite Thuc, too. Do you have the right equipment?"
            pete normal "We've got two radiation-proof tents from RET. I don't like relying on them for so many things though, so I'm going to try out my own."
            him surprised "And you're testing it on us?"
            pete happy "Nah, we'll bring both. Still gotta test the one I made."
            pete normal "Bring something to sleep on and some food. And get a bow from the community center."
            him determined "Not the rifles?"
            pete normal "With the guns, they all run away when they hear the shot."
            pete happy "And I want to show you the bow I made. You might not be able to draw it, though."
            him annoyed "We'll see about that... though I haven't praticed shooting a bow and arrow since I was a kid..."
            pete happy "You can set up traps, then."
            him normal "Or maybe I'll do both. We'll see which is more effective."
            scene storeroom with fade
            "I told Thuc about the campout and he decided to join us, bringing a crossbow from the storehouse. I picked up some wire and cord for snares, as well as a compound bow."
            scene path with fade
            "Pete led us on a hike that lasted all afternoon. Finally, we found the herd."
            scene plain with fade
            show thuc normal at center
            show pete normal at midright
            show him determined at midleft
            "The grass crabs were about the size of a capybara, but had less meat because of their large shells."
            "They ate a lot of grass, and also the woody parts of plants. Their large beak-like claw could cut through branches, which allowed them to gnaw on it while on the move."
            #makes sense?
            thuc sad "It seems like in the morning, they like to be in the sun, but then in the evening, they like to be in the shade."
            pete normal "They're cold-blooded critters, like insects. The can't make their own body heat."
            show thuc normal
            him surprised "This herd is a pretty good size. There's all different sizes of them."
            scene canyon with fade
            show thuc normal at midright
            show pete normal at center
            show him normal at midleft
            with dissolve
            "We setup a camp nearby, and Pete strung his giant longbow and waxed the string."
            pete "Here, give this baby a try. Aim for that dead tree over there."
            him determined "Isn't there supposed to be some place for the arrow to rest?"
            pete "Don't need it. It just rests on your hand."
            "I picked up the bow and nocked an arrow... but couldn't pull it back more than a few inches. The arrow plinked harmlessly off the tree."
            him normal "Ha ha, at least I hit the tree."
            thuc normal "You made this bow?"
            pete normal "Yup. Carved it from a single branch."
            "He drew an arrow, nocked it, and pulled the string back all the way to his jaw. The arrow flew into the dead tree and almost came out the other side."
            him annoyed "I prefer a compound bow."
            "I got out my own bow and shot an arrow at our target, and it sunk in with a satisfying {i}thunk{/i}."
            "Thuc got out his crossbow and we took turns trying it out, too."
            "We recovered our arrows and bolts, and I noticed it was getting dark."
            show night_overlay
            him normal "I'm going to go setup those snares."
            thuc normal "I saw some trails back there. Might be a good spot."
            pete "I'm going to get a fire going. We'll eat when you get back."
            hide him
            hide thuc
            with moveoutright
            hide pete with moveoutleft

            scene bonfire with fade
            show pete normal at center
            show thuc normal at quarterright
            show him normal at midright
            show night_overlay
            with dissolve

            "When we returned, Pete had some beans cooking on a small fire and was making what looked like a cloak of branches and small pieces of yarn."
            him surprised "What are you making, Pete?"
            pete "A ghillie suit."
            thuc sad "Do you think that will really help camouflage you from the grass crabs?"
            pete happy "These critters have eyes, right? I reckon it'll help."
            thuc normal "I'm going for something a little easier."
            "He dredged his jacket in some ashes from the fire to mottle its coloring."
            show him determined with dissolve
            "I didn't go to quite as great of lengths as Pete, but I did tie some branches to my hat and smudge soot on my clothes."
            pete "They'll never see us coming!"
            # TODO: can we show this?

            scene plain with fade
            show night_overlay
            play music tense
            "The next day, we woke up before the sun to catch the grass crabs while they're still drowsy."
            "By the time we found them, the sun was starting to come up, and the grass crabs were warming themselves and chewing on sticks."
            show pete normal at midleft
            show him determined at quarterleft
            show thuc normal at left
            "At about 100 meters, we stopped to figure out our approach. Pete whispered so quietly I could barely hear him."
            pete "Those two big ones look like good targets."
            show him determined at creepright
            show pete normal at creepright
            show thuc sad at creepright

            "We readied our arrows and snuck closer."
            him determined "Try not to lose any arrows."
            thuc sad "I won't lose them but I will definitely loose them."
            him annoyed "..."
            thuc normal "..."
            "One of the grass crabs looked in our direction. Then another. And another."
            "The herd started slowly moving away."
            "Pete pointed to himself and made a circular motion."
            "He pointed to a different grass crab on the far edge of the herd."
            show him determined at creepreset
            show pete normal at creepreset
            show thuc sad at creepreset

            "We followed him quietly, giving the grass crabs a wide berth. I felt like just shooting from here, but I was worried it would be too far for the arrow to go through their thick shells."
            "So we continued our painfully slow creeping."

            "It would have been faster to just scare the herd towards my snares, but honestly, I wasn't sure they would work. Grass crabs were pretty different from rabbits."
            "It seemed like we were maneuvering all morning. Finally, Pete gave a thumbs-up and drew his bow."
            "I guess he was going to shoot first. He probably had the best chance of piercing their armor. Still, Thuc and I didn't want to be left out. I aimed at the same crab."
            "As soon as I saw him loose his arrow out of the corner of my eye, I let mine loose, too."
            "My arrow sailed over its shell, but Thuc's stuck out of the crab's leg."
            "Pete's hit the crab square in the front part of the shell, but it simply walked off with the arrow sticking out of it."
            thuc sad "It's still alive!"
            show him determined at midleft
            show pete normal at center
            show thuc sad at quarterleft
            with move

            "Together, we stalked the animal to see if it would fall over."
            pete happy "I think I hit it right where its heart should be. Of course, with those shells, it's hard to tell how deep the arrow went."
            play music exciting
            "The animal fell to the ground, motionless. Pete approached it with a large hunting knife."
            show pete at midright with move
            "Suddenly, the animal pinched Pete's leg with its giant front claw!"
            show pete normal at squatting with move
            pete normal "Yeeeowch!"
            # TODO: Should this be a timed menu?
            menu:
                "Tackle the crab.":
                    $ luddites += 1
                    #TODO: I want the injured-hand option to result in making less money that month, if we do the currency thing.
                    show him annoyed at right with move
                    "I tackled the grass crab from behind, easily outweighing it."
                    "The crab tried to get at me with its other, smaller claw, but couldn't reach back that far."
                    "The crab's wild swinging made Pete lose his balance, and he fell forward onto the crab, his knife slicing through my arm and into the top of the crab's shell."
                    show him angry with dissolve
                    "Finally, the crab quit moving and we were able to pry Pete's leg out of the claw."
                    show pete at standing with move
                    show him concerned with dissolve
                    pete happy "We got 'em!"
                    thuc normal "But at what cost? You guys look awful."
                    "I looked down at the blood streaming down my arm, and the blood welling through Pete's pant leg."
                "Stay here.":
                    show thuc at right with move
                    "I froze. Thuc stepped forward onto the crab's claw, and it released its grip on Pete's leg."
                    "However, it brought up its smaller claw and scratched Thuc's cheek."
                    "Pete thrust his knife into the crevice where the crab's shell plates met."
                    show pete at standing with move
                    pete happy "Got 'em!"
                    him concerned "Are you guys okay?"
                    pete normal "It doesn't feel too bad. Let's get back to camp and see how things are."
            him flirting "We may look bad... but he looks worse!"
            "We bound up our wounds and then the three of us hauled the grass crab back to camp. Pete was limping a bit but otherwise seemed okay."
            hide pete
            hide him
            hide thuc
            with moveoutleft

            play music tender
            scene canyon with fade
            show him determined at midleft
            show thuc normal at center
            show pete normal at midright
            with dissolve
            "On our way back, we checked the snares. One of them had a crab leg in it... but there was no sign of the rest of the crab."
            him happy "This is going to be delicious."
            pete happy "Let's cook some up before we head home."
            "Just as we got our fire started, a solar flare warning came up on the radio."
            pete normal "Fantastic. I can test my homemade tent."
            him surprised "How did you make it?"
            pete normal "The fabric is leather. That doesn't do anything for radiation."
            pete happy "But after you set it up just so, you pour water into the top and the water insulates from the radiation."
            "Pete poured the water in, and it gradually filled the tent's lining. He put a radiation monitor inside the tent and we gathered in the other tent for the duration of the solar flare."
            "After about twenty minutes, the radio came on again to say that the flare has abated."
            "Pete checked his monitor to see the results of the test."
            pete happy "And it appears to reduce solar radiation! Too bad it's completely dark in there."
            him annoyed "And there's some water on the floor -- looks like a leak."
            pete normal "Hmmm, yeah, still needs some work."
            him surprised "Hmm. These shells probably protect the crabs from radiation... maybe you could build something out of them?"
            pete happy "Good idea. I'll save them so I can experiment."
            scene bonfire with fade
            show pete normal at center
            show thuc normal at midright
            show him normal at quarterright
            with dissolve
            "Finally, we were able to roast and eat the grass crab. The meat was surprisingly sweet."
            "We couldn't eat all of it, so we split it up between the three of us to bring home."
            pete "Here's some salt water to keep it fresh for the hike home."
            him normal "Thanks, Pete."
            pete "We oughta do this more often."
            thuc normal "Sure, except with less blood next time."
            him happy "Sounds good to me!"
        "Sounds dangerous. I have to focus on farming right now anyway.":
            $ miners += 1 #not sure which side colonists +1 should go on for this one.
            him concerned "What happens if you get pinched by one of those things? It doesn't sound safe."
            pete "That's the whole point! Gets your blood moving."
            show him determined
            him determined "Just seeing if I'll have enough food for the next month is risky enough for my tastes."
            "Pete went hunting on his own. But he brought back some meat from the grass crab he killed, preserved in salt water."
            scene community_center with fade
            show him normal at midleft
            show pete normal at midright
            with dissolve
            him happy "This is delicious!"
            pete happy "It took me nearly all day to finally hit one. Then I had to chase it down!"
            him surprised "Was it worth it?"
            pete "Hell yes! Herding cattle is fine for everyday, but every once in a while a man needs some excitement in his life."
    return

# 10 - Perón's over for dinner, who should take care of their farm?
label community10:
    play music sad
    scene farm_interior with fade
    show him normal at midleft
    show bro normal at quarterleft # TODO: is he a baby here?
    show her normal at midright
    show kid normal at quarterright
    with dissolve
    her normal "I'm leaving for work now. Goodbye honey!"
    him happy "Bye, [her_name]. Don't forget; we're having dinner with the Peróns tonight."
    kid happy "Yay, I get to play with Mateo!"
    her surprised "I wonder what they wanted to talk about..."
    him surprised "Maybe they're just being friendly?"
    scene farm_exterior flip with fade
    show natalia normal at midright
    show martin normal at quarterright
    show bro normal at center # TODO: show Perón's kids? use OPS1 kid sprites?
    with dissolve
    show him normal at midleft
    show her normal at quarterleft
    show kid normal at left
    with moveinleft
    natalia "Thanks for coming over. We're just finishing up the corn."
    martin "We made a turkey bean soup. It should go well with your salad."
    "We ate outside, where the Peróns had built two picnic benches, with some crabbird shells modified to be stools."
    #TODO: If we have sprites for any of their kids, I can insert them into the conversation.
    "After the meal, [kid_name] ran off to play with the other kids."
    hide kid
    hide bro
    with moveoutright
    martin "As you may have heard, I have skin cancer."
    her concerned "I assure you that doctor-patient confidentiality is important to me and I would never discuss your health problems without your consent!"
    martin happy "I know! You are not the only one who knows, however."
    natalia "The more people who know about your disease, the more people who can help us!"
    if (asked_only_medicine):
        martin normal "I can hang on until the medicine arrives, but we're still thinking ahead."
    else:
        martin normal "I have a few more months to live, but I'm already slowing down."
    martin angry "My children are old enough to take care of the farm, but I'm not sure if it's a good idea."
    natalia "They aren't as passionate about the farm as you are."
    him surprised "But now that they're older, don't you have more time to work on the farm?"
    natalia "Absolutely not. I have enough work as it is making food for everyone, washing their clothes, spinning thread and yarn, canning our surplus, making soap, mending and reworking clothes..."
    martin happy "Don't get her started!"
    show him happy
    show her happy
    with dissolve
    natalia "If I were in charge, I would phase out the turkeys and corn. I think I could handle chickens and beans on my own."
    show her surprised with dissolve
    him concerned "Isn't the corn really important for feeding everyone else's animals?"
    martin normal "Yes, it is the main component of feed for the animals. Someone else would need to start growing more corn if that happened."
    show her determined with dissolve
    him surprised "What are your older kids interested in, if not farming?"
    natalia "Tomas is always hanging out in the lab, but I think he just wants to spend more time with his wife, Joanna, who works there."
    martin normal "Isabella wants to be our colony's finest writer. You may have seen the book of poetry she messaged to everyone."
    natalia "Well she can write {b}and{/b} help grow our food!"
    martin angry "Raul is a good helper on the farm, but he isn't responsible enough to be in charge."
    natalia "And Mateo is still too young to do much more than harvest corn and feed the flocks."
    martin normal "What would you do in my position? Who do you think should take care of the farm?"
    show him concerned
    show her concerned
    with dissolve
    $ community11_kidsonfarm = False
    menu:
        "Tomás and Joanna Nguyen should be in charge of the farm and get the other siblings to help.":
            $ community11_kidsonfarm = True
            $ colonists += 1
            $ miners += 1
            him determined "Tomás is your son. It's his duty to help you out."
            martin happy "That's what I keep telling her!"
            natalia "He doesn't enjoy it... but he can do it. It's just hard for me to ask such a sacrifice of him."
            martin normal "We've all had to sacrifice at one time or another... This is something worth sacrificing for."
            natalia "But how will you convince Tomás of that?"
            martin angry "What do you think would convince him, [his_name]?"
            menu:
                "What should I say?"
                "Duty is more important than personal desires.":
                    him concerned "We all have duties. We may not always enjoy them, but only when everyone does their part can we all survive together."
                    martin happy "Exactly!"
                "This is a matter of survival.":
                    him angry "This isn't a buffet where he can just pick the things he likes! This is survival!"
                    natalia "Now that's dramatic!"
                    martin normal "And also true! I'm not sure he realizes that."
                "Train someone else to take your place.":
                    him concerned "If he doesn't want to take over the farm, then he needs to train someone else to do that job. But in the meantime, it's his responsibility."
                    natalia "I like that. That gives him options. And Raúl or Mateo might be more interested in farming, anyway."
                    martin normal "Josephina loved growing things. She would have helped, too."
                    natalia "I know she would have."
                "This is about family.":
                    him concerned "His family needs him. I know you guys are a close family; he'll understand that."
                    natalia "I don't want to make him feel guilty..."
                    martin normal "Maybe he needs to feel a little guilty to do what he needs to do."

            scene black with fade
            "I kind of forgot about our conversation, until one day Natalia sent me a message."
            nvl clear
            natalia_c "Thanks for helping us with Tomás. We talked to him, and he's decided he will help out at the farm, at least for a little while."
            him_c "Glad to hear it! He's a good kid."
            #more investment in older farms; Tomas and Joanna are less likely to join the luddites this way
        "Let Natalia scale back the farm.":
            $ community11_kidsonfarm = False
            $ luddites += 1
            him determined "If nobody wants to do it, you shouldn't force them to."
            natalia "See? It's important for kids to follow their dreams!"
            martin angry "Tomás is perfectly capable of running a farm; he's just lazy!"
            natalia "It's not laziness to prefer working in the lab with his wife."
            her surprised "But what about the corn everyone needs for their animals?"
            martin normal "It's mostly Pete's cows that eat it; the smaller animals could live on kitchen scraps and foraging."
            natalia "Well, then I guess it's Pete's problem."
            him concerned "Just... cut back gradually. It'll take time for everyone to adjust."
            scene black with fade
            nvl clear
            natalia_c "Due to our advancing age and health issues and lack of interest from our offspring, we need to cut back on the amount of corn we grow."
            ilian_c "What?! We need to be increasing our yield, not decreasing it!"
            natalia_c "It's mostly animal feed, anyway."
            pete_c "My cows sure ain't eating any less than they used to. How's that gonna work?"
            martin_c "It can't be helped! I'm dying of cancer and most of my kids aren't becoming farmers!"
            julia_c "You let them choose other things!"
            natalia_c "You should talk! Joanna's no farmer, either!"
            julia_c "But her other siblings are, so we don't have this problem."

            "Natalia's announcement caused such an uproar that finally Tomás came on and stated that he would help with the corn so that there would be enough for everyone."

            "I felt like my advice had caused a big ruckus... but then again, maybe without that he wouldn't have been willing to step up. It certainly made everyone appreciate the corn that the Peróns grew."

            "I felt a little bad for Tomás, but in the end it was his choice. And I admired him for choosing the good of the colony over his own desires."
            #then what happens to the corn everyone needs? they need to decide on how to take care of that. Maybe when Pete leaves it's not as much of an issue, since there is less cattle to feed over the winter.

    nvl clear
    return

# 11 - shuttle arrives with miners & Brennan
label community11:
    $ chaco_questions = 0
    #The shuttle should return to Earth with the mined material as soon as it is full.
    scene farm_interior with fade
    show him normal at midright
    show her normal at midleft
    show kid normal at center
    show bro normal at quarterleft
    her happy "Kevin says the shuttle is on course to arrive today!" #make this a family conversation?
    kid surprised "I wonder what the new people will look like?"
    him happy "Well, they'll look like we do. We're all humans."
    her flirting "Unless aliens have secretly taken over Earth while we were gone!"

    scene plain with fade
    show sara normal at midleft
    show oleg normal at quarterleft
    show her normal at midright
    show him normal at center
    show kid surprised at quarterright
    "Families gather at a safe distance from the landing area to watch the sky."
    "We shared binoculars and cheered as the shuttle landed."
    "I helped take a wagonload of people to the landing area to greet them and transport people and goods."
    "The people in the shuttle exited one by one."
    sara normal "Wow, those guys are built. The women, too -- solid!"
    her concerned "Yeah, I'd expect that miners have to be in good physical condition."
    him surprised "They look pretty strong. Almost as strong as all the farmers we have here."
    her flirting "Farmers have to be in good physical condition too!"
    sara normal "Pavel is already greeting everyone. Let's join him."
    hide sara
    hide oleg
    with moveoutleft
    "I was about to introduce myself to one of the miners when I saw someone with commercial-worthy flowing red hair."
    him annoyed "Wait a minute, I recognize him!"
    #BRENNAN ON SCREEN. he looks the same
    show brennan normal at quarterleft with moveinleft
    # Jack definitely doesn't like him, but doesn't have a great reason.
    him surprised "Brennan!"
    brennan happy "Oh, hello [his_name]. You look surprised. No one mentioned I was coming?"
    him determined "No, no one mentioned it. I hope you're not here to help [her_name]; she has a real nurse assisting her now."
    brennan normal "Oh no. That was never my main objective. Someone here needs to have ties to Earth to care enough to make sure everyone does their jobs."
    brennan angry "Plus, I was the only applicant with relevant experience, having lived here for a year before."
    her happy "Hi Brennan, I didn't think we'd ever see you again! How's it going?"
    brennan happy "I'm really happy to be breathing fresh air, with my feet on solid ground again."
    brennan normal "How is your daughter? How old is she now in Earth years?"
    kid annoyed "I'm seven... well, almost seven. It's complicated. Anyway, I'm going to see if they'll let me look inside the shuttle!"
    hide kid with moveoutright
    her flirting "You still don't look a day over 30."
    brennan normal "I'm not, technically. All this space travel has made me into some kind of ageless Dorian Gray, only instead of an awful painting hiding my age, I just have outdated pop culture references."
    him annoyed "No wonder you didn't want to stay on Earth."
    brennan happy "You don't look like you've aged too badly, considering how much sun you must get."
    him angry "Wow, really? Martin just died of skin cancer last year and you make a sun exposure joke?"
    brennan angry "Sorry...I didn't know."
    her concerned "Of course you didn't."
    brennan normal "Anyway... Can you help me get everyone together? I need to introduce our Miner Welcome program with Pavel."
    "I whistled long and loud."
    him surprised "Hey, listen up! Quiet down, everyone!"
    hide him
    hide her
    hide sara
    with moveoutleft
    show brennan normal at center with move
    brennan happy "Thank you for the warm welcome! We're planning on staying here a good twelve Earth years, and some of us for the rest of our lives."
    brennan normal "In order to facilitate our integration into your community, we've assigned each family a miner or miner family to get to know through weekly dinners."
    brennan normal "I sent out the assignments already, so try to find each other!"
    scene plain with fade
    show him normal at midleft
    show her normal at center
    show chaco normal at midright
    with dissolve
    "After asking around, I found our miner."
    him "Nice to meet you, Chaco."
    # TODO: There are too many of these to show all at once. We can delete some or change how we show menus.
    label chaco_coversation_loop:
        show him normal
        show her normal
        with dissolve
        menu:
            "What should I ask him?"
            "How was the shuttle ride?":
                him surprised "How was the trip over?"
                chaco "Fine."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "Was it hard to adjust?":
                him surprised "Did it take a while to adjust to living in such a small space?"
                chaco "No."
                her happy "I felt so cramped when I came over. Sometimes I just wanted some fresh air so badly, I felt like I would die."
                chaco "They gave us sleeping medicine part of the time."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "Do you have any hobbies?":
                him surprised "What do you like to do in your free time?"
                chaco "Look at the stars."
                him happy "Well, this is a great place for stargazing. We've had to invent several new constellations though."
                chaco "Sounds interesting."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "Do you have a family?":
                him concerned "Is anyone waiting for you back on Earth?"
                chaco "No."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "What is your favorite color?":
                him surprised "What's your favorite color?"
                chaco "Blue."
                him determined "Light blue or dark blue?"
                chaco "Dark blue."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "What do you like to eat?":
                him surprised "What's your favorite food?"
                chaco "Steak."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "What do you think of Brennan?":
                him annoyed "How do you like Brennan?"
                chaco "He talks too much. And he worries too much."
                him normal "Sounds about right."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "Are you religious?":
                him surprised "Are you religious? Do you believe in God?"
                chaco "Yes."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "What is your blood type?":
                him surprised "What's your blood type?"
                chaco "O positive."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "How tall are you?":
                him surprised "How tall are you?"
                chaco "172 centimeters."
                $ chaco_questions += 1
                if (chaco_questions >= 4):
                    jump twenty_questions
                jump chaco_coversation_loop
            "If you were stuck on a desert island with all of your coworkers, who would you eat first?":
                him surprised "If you were stuck on a desert island with all of your coworkers, who would you eat first?"
                chaco "Hmmm. Whoever died first."
                him normal "That's a practical answer."
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
        scene community_center with fade
        show brennan normal at quarterright
        show him normal at center
        with dissolve
        brennan normal "We might need some help unpacking. RET sent a package for you guys, so come unpack it!"
        him determined "I can help with that."
        hide brennan with moveoutright
        him surprised "New batteries for almost everything! And a few new tablets."

        if asked_only_medicine:
            show her normal at quarterleft
            with moveinleft
            show natalia normal at right
            show martin normal at quarterright
            with moveinright
            "The exact medicine for Martín came! They included a bunch of other stuff, but some of it wasn't exactly what we wanted."
            "The Perón family is crying happily and hugging Martín."
            her annoyed "Hey, where's the Gouda cheese culture? I was really looking forward to it."

            hide martin
            hide natalia
            with moveoutright
            hide her with moveoutleft
            show thuc normal at midleft with moveinleft
            show sara normal at midright with moveinright
            #refer back to community8 for this
            if talked_to_Thuc:
                thuc sad "These peanuts are roasted. I thought I told you they needed to be unroasted! I can't grow them this way."
            else:
                thuc normal "Are there any new seeds to grow? I want some of this peanut butter, by the way."

            if talked_to_Sara:
                sara normal "I asked for a bicycle, is that here?"
                him concerned "No, I'm sorry. I couldn't fit everything into the message."
                sara sad "A bike would probably get tons of flat tires around here anyway."
                him normal "This looks like a software upgrade for the 3D printer though!"
            else:
                sara normal "It looks like there's a software upgrade here for the 3D printer."
                him normal "Great!"

            hide sara
            hide thuc
            with dissolve
            show kevin normal at quarterright with moveinright
            show pavel normal at quarterleft, behind him
            with moveinleft

            if talked_to_Kevin:
                kevin "Did they send the rest of Tulip House?"
                him concerned "I'm not sure. There's a big hard drive here for the library though!"
                kevin "There's bound to be something good in there."
            else:
                kevin "I've been wondering what happened in my favorite Earth TV shows. Did they send any media?"
                him happy "It looks like they sent us a hard drive for the library. You and Pete can look over it."
                kevin "Looking forward to it!"

            pavel normal "These look like plastic pages with compartments full of... seeds? Are these spices?"
            him happy "I sure hope so! This garlic looks great!"
            pavel normal "Yes, and it says the cultivation instructions are on the hard drive. I'm looking forward to this!"
            $ enable_crop("garlic")

            if (talked_to_Pavel and is_liaison):
                him normal "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel sad "I'm so happy right now!"

        else:
            show her normal at left
            show sara normal at midleft
            with moveinleft
            show natalia normal at right
            show martin angry at quarterright
            with moveinright
            "RET sent medicine for Martín, but when I gave it to him, he and Natalia looked crestfallen."
            natalia "This isn't the kind of medicine we needed! This is useless!"

            if is_liaison:
                natalia "Did you tell them what kind of medicine Martín needed?"
                him concerned "I told them Martín needed medicine, and I assumed that they knew what kind from the doctor's reports."
            else:
                natalia "Sara, why didn't you tell them the exact kind of medicine Martín needed?"
                sara sad "I'm sorry, I thought they knew what he needed! I just put medicine."

            her happy "Oooh, Gouda cheese culture!"

            hide her
            with moveoutleft
            hide martin
            hide natalia
            with moveoutright

            show thuc normal at midright with moveinright

            if talked_to_Thuc:
                thuc normal "I can start growing these peanuts right away!"
                # TODO: test this
                $ enable_crop("peanuts")
            else:
                thuc "Are there any new seeds to grow? I want some of this peanut butter, by the way."

            if talked_to_Sara:
                sara normal "Oh, are these bicycle tires? Maybe I can make the rest of the bicycle... oh, this looks like a software upgrade for the 3D printer!"
            else:
                sara normal "It looks like there's a software upgrade here for the 3D printer."

            hide sara with moveoutleft
            hide thuc with moveoutright
            show kevin at midright with moveinright
            show pavel at midleft with moveinleft

            if talked_to_Kevin:
                kevin "Did they send the rest of Tulip House?"
                him "I'm not sure. There's a big hard drive here for the library though!"
                kevin "There's bound to be something good in there."
            else:
                kevin "I've been wondering what happened in my favorite Earth TV shows. Did they send any media?"
                him "It looks like they sent us a hard drive for the library. You and Pete can look over it."
                kevin "Looking forward to it!"

            pavel normal "These look like plastic pages with compartments full of... seeds? Are these spices?"
            him surprised "Oh, I hope so! Look, garlic!"
            pavel "Yes, and it says the cultivation instructions are on the hard drive. I'm looking forward to this!"
            $ enable_crop("garlic")

            if (talked_to_Pavel and is_liaison):
                him normal "Oh, there was one month where I didn't have urgent business for the instacom, so I got the curry recipe for you too."
                pavel sad "I'm so happy right now!"

        scene black with fade
        if asked_only_medicine:
            "Thanks to the cancer medicine, Martín was able to work on the farm for six more months before dying a peaceful death."
            scene church with fade
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
        scene community_center with fade
        show brennan normal at midright
        show him normal at center
        show natalia normal at midleft
        show martin normal at quarterleft
        with dissolve
        brennan "Can you help us unpack?"
        him determined "That's what we came out here for."
        natalia "Did RET send any medicine for Martín?"
        brennan normal "No, sorry, I think they just sent some new batteries and stuff."
        natalia "They don't care what happens to us!"
        martin angry "I would have liked to live a little longer, but in the end, we can only do so much."
        $ luddites += 1

        label Martin_dead_sooner:
            scene church with fade
            "Without the medication, Martín's condition swiftly deteriorated, and he died the next week."
            "The family had a small funeral and buried him in the colony graveyard next to Josephina."
            "Tomás and Joanna Nguyen decided to help out their mother, but they weren't prepared to take full responsibility for the farm."
            "We hoped they could learn what they needed to know from Natalia and their neighbors."
    return

# TODO: community editing ends here
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
            him "Great. I think [kid_name] will love that."
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
                scene cabins with fade
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
        #rationing is the default for the non-liaison option, so non-liaisons should not see this event.
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
                                him "I'm not making these decisions on some whim. The colonists elected me to be the liaison to RET."
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
                    brennan "Also, start planting some extra crops for us, otherwise we'll all starve or irradiate to death in this forsaken place."
                    him "Okay, I'll do it right away."
                    legalese "Dear farmers of Talaam."
                    legalese "A few years ago I said that we didn't need to save food to feed the miners."
                    legalese "I thought that the miners would have time to hunt and forage and farm in addition to their mining."
                    legalese "I was wrong. RET needs the ore quickly to avoid bankruptcy."
                    legalese "We need RET to continue to support our colony with batteries and medical supplies."
                    legalese "There isn't enough surplus to feed the miners now, at least not in the storehouse."
                    legalese "If you can spare some crops for our miners, I can compensate you."
                    legalese "We also need several farmers to volunteer to plant fast-growing crops and also regular crops."
                    "Some farmers volunteered to sell extra food, and two or three farmers they'd plant more crops."
                    "After two weeks, we had lots of salad greens and radishes."
                    "But the lettuce and radishes weren't enough to feed the miners."
                    chaco "Thank you so much for dinner tonight."
                    him "You're welcome."
                    chaco "Could you sell me some of your crops?"
                    chaco "I can give you plenty of credits for them."#make this a decision if we have food/money variables
                    him "We don't have a lot of extra food right now, but we can spare a little."
                    chaco "This is great. I'm so sick of radish salad."
                    $ modify_credits(50)
                    him "You know, if you have the credits, I bet Pete could do some hunting for you."
                    chaco "Huh. I'll ask."
                    "Pete went on a quick hunting trip. He had to make several trips back to the hunting site to carry back all the carcasses."
                    "Dr. Lily took a few people out foraging."
                    "The miners lived off the meat and foraged food for almost a month."
                    "After eight weeks, we had zucchini, squash, and turnips for them, with some small potatoes and bigger ones on the way."
                    return

                label community12_choose_foraging:
                    brennan "Fine. I'll go door-to-door tonight to see if I can buy off some food until you can send over your teachers."
                    him "They'll be there tomorrow morning."
                    him_c "Hello Lily and Pete."
                    him_c "We don't have that much food for the miners, so they need to learn how hunt and forage."
                    him_c "Can you, Lily, teach them to forage, and Pete, can you teach them how to hunt?"
                    him_c "They want to start ASAP."
                    him_c "How does tomorrow morning sound?"
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

# 13 - Save your water purity!
label community13:
    $ saddle_partially_explored = False

    "I awoke one morning to knocking on my door, and [kid_name] asking me to answer the door."
    scene farm_exterior with fade
    show lily normal at midright with dissolve
    show him surprised at midleft with moveinleft
    lily "[his_name], we must act at once. In my weekly testing, I found that our water is showing trace amounts of heavy metals!"
    lily angry "Probably due to damage in one of the tailings dams! We must fix the dam and prevent future accidents."
    lily angry "It will probably poison some local wildlife! As well as us!"
    him normal "I certainly don't want heavy metals in my irrigation water."
    him concerned "Can we discuss it later? I just got out of bed and was hoping to sleep a bit more."
    if is_liaison:
        lily angry "I need you to insta-com Earth. If you message them soon, we can get them before working hours are over. Otherwise we need to wait a full fifteen hours."
        him determined "Alright. What do you need me to ask?"
        lily normal "Tell them to delay further ore processing until the tailings dam has been repaired."
        him surprised "Do they already know about contamination?"
        lily angry "Have you told them about it? Then no."
        him concerned "Are you sure it's the tailings dam?"
        lily angry "I am not completely certain, but it is the most likely culprit."
        him concerned "Do you know where it is?"
        lily normal "Yes, Zaina mentioned it, let me look it up."
        lily "She says it's on the mountain's saddle. I have the coordinates."
        him determined "Alright. I wrote: 'Please halt ore processing until tailings dam repaired.'"
        lily angry "I hope that I can still endure climbing to the top of this mountain."
        him normal "I've seen you walking around town. I bet you can handle it."
        lily normal "I can walk, but climbing a mountain is far more strenuous."
        lily happy "Aged bodies do not heal as quickly as young ones like yours."
        him surprised "Oh, they already replied. They said to go with whatever Brennan says."
        lily angry "I can't believe this. Tell them I said to stop ore processing!"
        him concerned "I can't send another message for twenty-four hours."
        lily normal "Then we must inquire with the next person who can stop this contamination."
        him annoyed "Ugh, Are you talking about Brennan?"
        jump community13_talk_to_brennan
    else:
        label community13_nonliaison_talk_to_brennan:
            lily "No, this is urgent and important business. Depending on their schedule, they may already be processing more ore!"
            lily "I need you to ask Brennan if he can delay ore processing until they fix the breach."

        label community13_talk_to_brennan:
            him concerned "You talk to Brennan. I need to make breakfast."
            lily angry "I'm afraid that my concerns may be dismissed due to my age and stature."
            lily normal "Your company would lend my petition credibility."
            him determined "Okay, I'll go. But I want to be done quickly. I have a lot of work to do today."
            "I tried to think about what I would say to Brennan, but my mind was full of the chores I wasn't doing and trying to reschedule the entire week."
            scene cabins with fade
            show lily normal at midright
            show him determined at midleft
            with moveinleft
            "When we arrived, the control station was empty."
            him surprised "Well, we tried, but he's not here. Let's just send him a message."
            lily angry "I don't want to risk them poisoning any more wildlife, or people. Do you know where Brennan sleeps?"
            him determined "I have no idea."
            "Dr. Lily knocked on the door of a nearby hut. She knocked for several minutes until she got an answer."
            lily "He said Brennan lives over here."
            "She knocked on his door. A voice came from behind the door."
            brennan "I am NOT pushing back any deadlines for your personal days, and that's final!"
            lily "We're not here to ask for a personal day."
            brennan "Oh, sorry. I thought you were someone else."
            scene yurt_interior with fade
            show brennan normal at midright with dissolve
            show lily normal at center
            show him determined at midleft
            with moveinleft
            brennan happy "Who do I owe for the pleasure of your visit?"
            lily angry "Me. Your tailings dam is not sufficiently contained and is contaminating river water with heavy metals."
            lily normal "I urge you to delay any more ore processing until the breach is repaired."
            brennan normal "There were some heavy rains and a tiny trickle got out. Kevin is observing and drawing up plans for how to repair it."
            lily angry "But you're not stopping any ore processing?"
            brennan "I don't know. What will RET think?"
            if is_liaison:
                him "We asked them, and they said to defer to your judgement."
            else:
                lily "We don't have time to find out what they think."
            lily "Any amount of heavy metals in drinking water can harm humans and animals who drink it."
            brennan "The thing is, ore processing is one of the bottlenecks in our efficiency."
            brennan "If we delay it by any amount, it will delay our whole timeline."
            brennan "Plus stopping ore processing won't reduce the amount of the leak."
            lily "Yes, but..."
            him "It makes it look like you don't care about other people when you continue with business as usual during a health emergency."
            brennan "If I were more concerned about RET's image, what you're saying would make sense. But we're all RET employees, so we should all want what's best for the company."
            brennan "Even if it makes it look like I don't care about water quality."
            brennan "Lily, how's this: You continue to do testing in a few locations to see how bad the contamination is."
            brennan "As soon as Kevin has those plans, I'll give him as many people as he needs to fix the leak."
            lily "Very well. I will send out a notice to everyone informing them to commence distilling all their water for now, including irrigation water."
            # https://www.sciencedaily.com/releases/2018/03/180314092258.htm an MOF/polymer "can quickly and selectively remove high amounts of heavy metals like lead and mercury from real-world samples"
            him "Wait, seriously?" 
            lily "Yes, seriously. If you ingest enough heavy metals, you could die."
            lily "I have access to a recipe for a metal organic framework polymer that could remove metals, but I will need to fine-tune it to the contamination."
            brennan "That sounds useful to have on hand."
            lily "Do you have anyone trained in chemistry lab work who could help me?"
            brennan "I bet Zaina would help you."
            him "I can't tell a pipette from a pipe cleaner, but if [her_name] is having a slow day, maybe she could help?"
            "Dr. Lily started messaging people and I went home to work."
            nvl clear
            lily_c "Heavy metals have been detected in our water supply." 
            lily_c "Distill all irrigation and culinary water until further notice."
            lily_c "Please tell your neighbors if they do not typically see these messages."
            thuc_c "I don't have a way to distill any water right now."
            ilian_c "We have a few emergency distillers that I'll put out right away, but they'll only make enough for drinking."
            thuc_c "How long has the contamination been going on?"
            lily_c "Sometime in the last week."
            her_c "What metals exactly?"
            lily_c "Arsenic and mercury in trace amounts."
            her_c "Please send me the details." #https://www.medlife.com/blog/heavy-metal-poisoning-symptoms-treatments/ treatment includes chelates, but they can take away other important minerals
            him_c "I don't think we can distill enough water for the crops. Does anyone know of an alternative water supply?"
            brennan_c "Is this really necessary? Dr. Lily's test only detected trace amounts."
            lily_c "Trace amounts can easily concentrate in fruits, vegetables, and roots."
            her_c "Our bodies can handle small amounts of heavy metals... Dr. Lily, I'll be right over to discuss what the health recommendations should be."
            "I set up a small distillery on our stove, but it would only make enough water to drink that night."
            "I consulted the map Zaina had been working on as she scouted the surrounding land for good mining spots."
            "Zaina had climbed other mountains in the same range as the ones close to our river, which also had water flowing from them, but none of them were nearby."
            "It also occured to me that we could gather water upstream from the tailings pond."
            "[kid_name] came back from school with her little brother and I explained that we needed to be careful with our water for now."
            "[her_name] came back from work early. We started preparing dinner together."
            her "There's an emergency town meeting tonight to discuss the water contamination."
            if is_liaison:
                him "I know, I saw the message."
                her "Well, should we just bring the kids along?"
                menu:
                    "No, I'll stay home with them.":
                        him "I'll get the kids to bed on time. You have more expertise with heavy metal poisoning than I do anyway."
                        him "You can tell me all about the meeting, and I'll report it to RET later."
                        jump meeting_abstain
                    "Yeah, we should both go to the meeting.":
                        him "It's my duty to know what's going on so I can represent the interests of the colonists to RET."
                        him "Plus this way the kids can see what local politics are like in action!"
                        her "They're just going to run around and look for other children to play with, and then go to bed late and be cranky all day tomorrow."
                        him "Probably."
                        him "Okay everyone, let's get ready to go!"
                        kid "I hope Oleg is there!"
                        "Oleg was there, along with Sara, Ilian, Mayor Grayson, Dr. Lily, Brennan, and Kevin."
                        "Sara opened the meeting, and Dr. Lily explained her findings."
                        pavel "Were you aware of this leak, Brennan?"
                        brennan "We discovered the leak yesterday afternoon, but since Kevin calculated that the contamination would be minimal, we took a wait-and-see approach."
                        lily "That is irresponsible. Any water contamination should be reported immediately."
                        brennan "To whom? We don't exactly have a utilities commission."
                        lily "To me! I already do routine testing on our water."
                        her "I would like to be notified as well, since it could impact the health of colonists and miners."
                        pavel "I would also like to know of any mining activity that could impact colonists."
                        brennan "In the future I will notify you all."
                        brennan "Now that we have that out of the way, Kevin, could you tell us a little more about why this happened and how we can prevent it in the future?"
                        kevin "Yes, I would be happy to." #see http://www.itv.org/en/research-line/technology-of-dams-and-tailings-disposal/ for info on how tailings dams are made
                        kevin "Several unpredictable factors worked in tandem and resulted in a breach to part of the tailings dam."
                        kevin "The crest of the dam was constructed for foot traffic, but not vehicle traffic, but at some point a vehicle crossed the dam, damaging its structure."
                        kevin "We repaired this and posted new signs. However, heavy rains caused more erosion than expected, possibly because plant and soil types are not analogous to Earth's." 
                        kevin "I also did not anticipate that the nearby resistive rocks would cause extra solar damage to our electronic warning system." # https://www.nationalgeographic.com/science/2019/03/solar-storms-worse-damage-if-you-live-near-certain-rocks-geology/
                        kevin "Because of the damage to the warning system, we did not receive notification when the leak breeched the first and second water lock."
                        kevin "I have been able to stop the leak for now, but I am still researching materials for the repair."
                        brennan "Thank you Kevin. When do you think the repair will be done?"
                        kevin "Definitely by the end of the week." #kevin can leave screen
                        lily "I am working on a polymer that can break down the metal contaminants. I will need to synthesize some chemicals, and it will take at least two days to prepare the necessary amounts."
                        her "I will assist Dr. Lily with the synthesis. Our water only contains trace amounts of metals, and I believe that we can still use it for irrigation water."
                        lily "I completely disagree. We should not knowingly ingest poison."
                        her "We don't have the capacity to distill enough water for crops. If we don't use the river water, we'll starve because we won't have enough food."
                        "What do I think we should do?"
                        menu:
                            "Find an alternate water source.":
                                him "I agree with Dr. Lily. Why risk permanent brain damage when we could avoid it?"
                                him "If samples showed elevated levels of heavy metals, there are probably spots in the river where that amount is even higher."
                                him "Could we divert the mountain stream so that it doesn't pass by the tailings pond?"
                                brennan "We're currently using power from the stream in our ore mill, so no, that is not an option."
                                jump diaper_interruption
                            "Use the tainted water.":
                                him "Kevin said that he stopped the leak for now, so the heavy metal content of the water should be decreasing as we speak."
                                him "Also, [her_name] stated that the levels are low enough for humans to safely consume."
                                lily "It's true that my samples measured at levels low enough for 'safe' human consumption. However, it's likely that parts of the river have more heavy metals than the samples I measured."
                                jump diaper_interruption
                            "Let colonists decide for themselves.":
                                him "Let's give everyone all the information we have and let them decide for themselves."
                                lily "If there is no way to get pure water, colonists will default to using the river water like they always have."
                                lily "Is that really a decision?"
                                her "Let's just tell them it's fine to use the river water then."
                                jump diaper_interruption
                        label diaper_interruption:
                                kid "Dad, [bro_name] has a stinky diaper."
                                him "Thanks for telling me."
                                kid "I think it's leaking..."
                                menu:
                                    "Take care of [bro_name].":
                                        him "I'd better take care of him right away then."
                                    "Ask [her_name].":
                                        him "I looked at [her_name]. She was reading something on her tablet intently."
                                        him "[her_name], could you change [bro_name]'s diaper?"
                                        her "Could you do it please? This discussion is really important to me."
                                "I left the discussion and changed [bro_name]'s diaper."
                                "When I got back, everyone was discussing the best emergency response system."
                                her "We decided to let farmers irrigate with river water, and Zaina will help Dr. Lily and I synthesize the polymer, hopefully by tomorrow."
                                her "Dr. Lily is anxious to continue her work, so I've agreed to go help her tonight."
                                him "I kind of volunteered you. Are you up for it? You could be up all night."
                                her "I know. This way we're both happy, sort of. Can you take the kids home?"
                                him "Sure."
                                "I took [kid_name] and [bro_name] home and put them to bed. [bro_name] took a long time to fall asleep, but it gave me some time to research heavy metal contamination in crops."
                                "The fruits and vegetables would be fine, but if we ate chickens who ate the contaminated food, it could be a problem."
            else:
                label meeting_abstain:
                    "I put [kid_name] and [bro_name] to bed like normal."
                    "I took some time to do more research on heavy metals and the things we eat."
                    "Even if the fruits and vegetables were fine, eating chickens that ate those vegetables could be a problem."
                    nvl clear
                    her_c "Hey, we're done with the meeting, but I'm going to help Dr. Lily tonight, so don't wait up."
                    him_c "How was it?"
                    her_c "Based on the levels in the samples, I told everyone we should be fine to use the river water for irrigation."
                    her_c "Dr. Lily said that we should err on the side of caution and use an alternative water source."
                    her_c "We couldn't really find an alternative, so I'm going to help Dr. Lily and Zaina synthesize a polymer to neutralize the metals."
                    him_c "Wow. Sounds science-y."
                    her_c "It's going to be kind of like making a huge batch of sourdough bread, except with less room for error."
                    her_c "If carefully measuring and combining things is science, then sure, it's science-y."
                    him_c "Good luck then."
            "The next day, [her_name] came home early in the morning."
            "While she was sleeping in, Dr. Lily asked me to help disperse the polymer."
            "I got the kids to school and co-op care, respectively, and got bottles of the polymer and location details from Dr. Lily."
            "One location was out by Pete's farm."
            #change location to Pete's farm
            pete "What brings you out here today? I don't see a wagon, so I'm guessing you don't need manure."
            him "No, I'm on a mission from Dr. Lily. Did you hear about the heavy metal contamination from the mining?"
            pete "No, I haven't heard a thing. Tell me all about it."
            him "The tailings pond in the ore processing area on the saddle of the mountain had a leak."
            pete "A leak that went into our river?"
            him "Yeah. It wasn't very much, and they were able to stop it before it got too bad... but this concoction should neutralize the metals."
            pete "I don't know what's worse, the metals or the stuff you're putting in to fix 'em."
            him "On Earth we ate and drank trace amounts of heavy metals all the time. We just didn't know it."
            pete "I knew about it! All that poison everywhere is part of why I wanted to leave!"
            pete "Didn't take long for big business to sully this planet."
            him "You joined that big business when you signed up to come here!"
            pete "That's a decision I question more and more each day."
            pete "Well, go ahead and do your job."
            him "I will."
            "The last bottle had to be released by the tailings dam, and I hiked halfway up the mountain to deliver it to Kevin, who took it the rest of the way."
            kevin "I do hope there are no long-term consequences of the leak. I feel personally responsible."
            him "We can't change what happened. All we can do now is try to learn from this and do better next time."
            return
    # Pete should be a vocal opponent of the mining to foreshadow next month.

# 14 - Pete leaves
label community14:
    scene plain with fade
    show brennan normal at quarterright
    show pavel normal at left
    show thuc normal at right
    show helen normal at midright
    show pete normal at center
    show him normal at midleft
    show lily normal at quarterleft
    with dissolve

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
    pete "Helen and I are taking our family and moving away."
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
        "Tomás Perón and Joanna Nguyen tell us their plans to go with Pete and his family."
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
            pete "My family's why I'm doing this. I don't like our present condition, so I'm changing it."
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
    if is_liaison:
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
    her "Yeah. I told Pavel to post that everyone should try to give her a last visit, although her symptoms are a lot like severe food poisoning, so..."
    him "We'll understand if she's, ah, indisposed. I'll bring the kids over this afternoon."
    her "Just... check with Pavel first."
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
    $ pstyle = get_parenting_style()
    if (pstyle== "authoritative"):
        naomi "I think you are doing a really good job. It's hard to be patient and not blow up at your kids sometimes."
        naomi "Keep up the good work."
    elif(pstyle == "authoritarian"):
        naomi "I think you're too harsh with your children sometimes. It's true that you make the rules in your home, but you can also decide when to change them or bend them."
        naomi "If you consider [kid_name]'s opinion sometimes, I think she will be happier."
    elif(pstyle == "permissive"):
        naomi "You let [kid_name] do her own thing a lot."
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
    her "I'll take her body today and do a few tests, and we can hold the funeral tomorrow."
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
    her "Oh, no...who's going to talk at her funeral?"
    him surprised "Are you putting that together?"
    her concerned "Yeah... I told Pavel I would; he's in no state to do it himself."
    him "Sara's pretty religious, and I know she's worked with Pavel. She probably knows Naomi pretty well. I mean knew."
    her "Sounds good. Can you ask her for me?"
    him "Has Naomi's death been announced?"
    her "Pavel just posted about it."
    him "I'll ask Sara if she can speak at the funeral then."
    nvl clear
    him_c "Sara, can you speak at Naomi's funeral tomorrow?"
    sara_c "Yes, of course! But I think you should say something, too."
    him_c "I'll think about it."
    nvl clear
    him "Hey, [her_name], Sara thought I should say something at the funeral..."
    if (is_liaison):
        her "Well, you are the liaison. You can do closing remarks; just keep it short."
    else:
        her "You can if you want... somebody needs to speak at the end. Just something short."
    $ c15_funeral = ""
    $ c15_funeral_poem = ""
    menu:
        "Should I participate in the funeral?"
        "Prepare a poem":
            $ c15_funeral = "poem"
            "The best way to keep it short would be to make a poem. I'd better make it good, though..."
            $ word_board.set_wordpack(basic_words, talaam_words, separation_words)
            call make_poem
            $ c15_funeral_poem = word_board.get_poem_as_string(-1)
        "Say a few words":
            $ c15_funeral = "speak"
        "Don't speak at the funeral.":
            him "I really think you should speak instead."
            her concerned "I guess I don't have to say much..."
    "The kids had been playing, but were listening to our conversation." #TODO: actual conversation w/kid?
    scene church with fade
    "Almost everyone came to the funeral the next day."
    #background - multipurpose room or chapel
    show her concerned at center with moveinleft
    her "I hope Naomi felt at peace when she died."
    her "Even though she was miserable, she stayed cheerful and optimistic until the very end."
    hide her with moveoutright
    show pavel sad at center with moveinleft
    pavel "Naomi died of severe radiation sickness. I don't know if it was preventable or not."
    pavel "There were many times where she felt it was more important to attend to the needs of people in our community rather than take shelter from solar radiation."
    pavel "She constantly sacrificed her own needs to fulfill those of others, perhaps to an unreasonable degree. May her work live on in the way we treat each other." #you could have him say different things based on the community variable
    hide pavel with moveoutright
    show sara sad at center with moveinleft
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
    hide sara with moveoutright
    "Some of the children sang one of the songs Naomi taught them when they were young." #does Brennan do anything? What about the miners? Kevin or Zaina?
    if (c15_funeral == "poem"):
        show him determined at center with moveinleft
        "I walked up to the stand and shared the poem I had written."
        him "[c15_funeral_poem]"
        hide him with moveoutright
    elif (c15_funeral == "speak"):
        show him determined at center with moveinleft
        "I walked up to the stand and prepared to speak."
        menu:
            "What should I say?"
            "Naomi was a good woman.":
                him "Sister Naomi helped take care of my kids when I really needed help."
                him "She was honest, kind, and thoughtful. She put others' needs before her own."
                him "We will greatly miss her."
            "Remember her by caring for each other.":
                him "Sister Naomi wouldn't want us to spend a bunch of time talking about her. In fact, she'd probably be embarassed."
                him "She'd want us to remember her by doing the kinds of things she did -- taking time to enjoy the people around us and helping each other."
                him "So let's remember her every day, and let that memory propel us forward to do good to others."
            "Life is hard; then we die.":
                him "Death is a normal part of life."
                him "That doesn't mean we have to like it, but we do need to accept it, and move on."
                him "So today we remember Sister Naomi, but tomorrow, let's not waste her hard work by moping about."
                him "We could die at any time; we need to make the most of whatever time we still have."
        hide him with moveoutright
    else:
        "[her_name] said a prayer of gratitude for Sister Naomi and asking for comfort and the inspiration to know how to help each other."

    "We all helped to bury her body. Ilian provided a laser-engraved headstone, and the Nguyen children put wildflowers on her grave."
    "[kid_name] and [bro_name] planted the saplings we brought."

    #back home
    scene farm_interior with fade
    show him determined at midleft
    show her concerned at midright
    with moveinleft
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
    # Miranda Perón (now about age 26) steps up to take Dr. Lily's spot. She had been studying with Dr. Lily before."
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
            pete "I think Travis gets lonely, but he and the other kids have plenty of work to help with."
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
                        him "She did something similar when [kid_name] went a whole day without poking Oleg."
                        pete "What was her title?"
                        him "Overseer of Restraint."
                        pete "Ha. I doubt I would have even noticed something like that."
                        $ pstyle = get_parenting_style()
                        if (pstyle== "authoritative"):
                            him "I think I would notice!"
                        elif(pstyle == "authoritarian"):
                            him "I would probably only notice when she did poke him."
                        elif(pstyle == "permissive"):
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

# COMMUNITY 17
# Harvest festival; who do you invite? chance to eat jellyfish...
label community17:
    $ community_17_activity = ""
    "It's time for the harvest festival! Usually we eat a big meal and the kids go around begging desserts off everyone."
    if (is_liason):
        "Someone needs to plan it... but who?"
        menu:
            "Plan it yourself.":
                $ community_17_planparty = True
                "I decided to plan it myself. I knew what made a good harvest festival."
                "First, I needed to decide whom to invite."

            "Ask Sara and [her_name] to plan it.":
                "I asked Sara and [her_name] to plan the festival. They made a good team for that sort of thing. But they wanted to know who was invited."
    menu:
        "The miners and Pete's group." if ((luddites >= 7) and (miners >=7)): #TODO: make sure it's possible to get this option
            "Might as well invite everyone on the planet. Then it'd be a really big party!"
            $ invited_luddites = True
            $ invited_miners = True
            jump ludditesandminers
        "Pete's group." if (luddites >= 7):
            "I thought it'd be a good idea to invite Pete's group."
            $ invited_luddites = True
            jump justluddites
        "The miners." if (miners >= 7):
            "I guess we should invite the miners."
            $ invited_miners = True
            jump justminers
        "The usual-- just all the other colonists.":
            "We don't need to invite anyone else. It's a harvest festival, after all, so we should celebrate everyone who did the actual farming."
            jump justcolony

    if (community_17_planparty):
        "We needed some activities."
        menu:
            "What kinds of activities should we have?"
            "Contests.":
                $ community_17_activity = "contests"
                "I decided to ask Julia to organize some contests. She always liked to have a say in things."
            "Icebreaker games.":
                $ community_17_activity = "games"
                "I figured we could play some easy social games to get everyone talking. I asked Thuc to be in charge of that; he was good at making everyone feel relaxed."
            "Performances.":
                $ community_17_activity = "performances"
                "We had a lot of talent in our little community -- it would be a great chance to hear people perform."
                "I asked Ilian to be in charge of that. He loved music, and he's such a critic that he'll only ask people with real talent."
        "Last was the food. I figured I'd just have everyone bring something."

    if (invited_luddites and invited_minters):
        "Pete offered to slaughter a steer for the occasion."
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
        "Pete also brought a strange seafood dish."

    elif invited_luddites:
        "Pete offered to slaughter a steer for the occasion."
        "The colonists brought their best vegetables and fruits, and even some different kinds of bread and pudding."
        "Pete also brought a strange side dish."

    if invited_luddites:
        him "So... what is this?"
        pete "Out by the ocean, sometimes you can find these critters with a bunch of spiny arms."
        pete "They start stacking on top of one another and they send off these giant eggs."
        him "Is it safe to eat?"
        pete "Hasn't killed me yet. Try it; it's real good."
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
        him "Can you come do a class on cattle health? You're the only expert around." #see community 14 for who got the cattle
        pete "I could, if you can help me out with a knife and some twine."
        him "I think we can arrange for that."

    elif invited_miners:
        "We invited the miners to join us. After all, their success is what enables us to continue to live here."
        brennan "We didn't have time to go hunting, but we DO have time to soak beans."
        him "Is this a soup or a dip? It smells... different."
        brennan "Neither. Either. Both! Try some."
        menu:
            "Try it.":
                "You dip your bread into the very organic-appearing, thick brown dip."
                "It tastes like beans, with a strange combination of spices."
                "It's not like anything you've ever tasted before. It's exciting to try something new"
                #TODO: set up the variable for here too?
            "Don't try it.":
                him "I'll pass."
                brennan "You don't like beans?"
                him "I'll stick to what I know."
                brennan "How very... predictable of you."

    scene community_center with fade
    show thuc normal at quarterleft
    show julia normal at left
    show pavel normal at quarterright
    show him normal at midleft
    show natalia normal at midright
    with dissolve
    "I set my dish next to the ones from the other families on the buffet table."
    "Everyone helped themselves and sat down--some at tables and some on the ground."
    natalia "Is this what all those eggs you were buying from me were for? Is it just an omelet?"
    him "Well, it's kind of like a souffle, but I don't have an electric mixer, or a reliable oven."
    natalia "Mmm. It's not bad. But you should be careful not to mix it too much after you add the flour."
    him "I know..."
    natalia "You might have been better off just leaving out the flour completely."
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
    "Thuc and I brought out the special treat we made together. It's made with rice and corn and the kids noticed it eagerly."
    "They started cleaning the serving dishes and I made a show of inspecting their work and giving them the rice-corn treat."
    "Of course, a few other adults were busy saving leftovers and helping the smallest children clean dishes."
    pavel "It's a shame we don't have any chocolate to give them."
    natalia "I miss it too."
    julia "This is better than Halloween. They're actually helping people instead of running around with entitled threats."
    thuc "They still sound pretty entitled to me!"
    him "Some things never change."

    scene community_center with fade
    if (community_17_activity == "contests"):
        show julia normal at center with dissolve
        "After everything was cleaned up, it was time for our contests."
        "Julia announced the different events. I wonder if I should participate...?"
        menu:
            "Which one should I enter?"
            "The seed spitting contest.":
                "I had spent many days sitting on the back porch spitting seeds with my cousins. I knew all the tricks and felt pretty confident I could do well."
                "Kevin apparently had managed to grow a few watermelons, though it wasn't really warm enough for it."
                "The contest was simple: spit two seeds as far as possible. Whoever spits the farthest seed wins."
                julia "Our first contestant will be... Natalia. Huh. Spitting is something you might actually be good at."
                show natalia normal at midleft with moveinleft
                natalia "You bet I am!"
                show natalia at midright with move
                "She got a good seed in mouth, backed up several feet, and then ran up to the line, spitting at the last possible second with an audible 'pbbt'."
                "Natalia's seeds went at least ten meters."
                hide natalia with moveoutright
                "This was going to be a tough contest."
                show sara normal at midleft with moveinleft
                "Sara entered, but her first one ended up dribbling out of her mouth. She tried to spit the second one better, but it ended up hitting Julia on the chin."
                julia angry "Out of bounds!"
                hide sara with moveoutright
                show kid determined at midleft with moveinleft
                show julia normal with dissolve
                "[kid_name] gave it a try. She spat the first one high in the air, but it didn't go very far. The second she spat hard, down at the ground, and it bounced and made it just past Natalia's."
                julia "Well done, [kid_name]! That was spectacular!"
                show kid happy with moveoutright
                show him determined at midleft with moveinleft
                "Then it was my turn. I was the last contestant."
                "I stepped up to the line, got a big fat seed in my mouth, and got ready to spit."
                show kid concerned at left with moveinleft
                "[kid_name]'s face caught my eye and I paused. She looked... worried."
                menu:
                    "What should I do?"
                    "Give it my best effort.":
                        "I had to give it my best effort. If [kid_name] won, I wanted it to be for real."
                        "I flicked my head to give the seed great momentum. It sailed through the air."
                        "The seed bounced once, twice, and then stopped."
                        julia "The first seed is behind Natalia's! So far [kid_name] is still winning!"
                        "No way. I had one seed left. I was going to make this one count!"
                        "I reared my head back, and spat with my whole body."
                        "The seed bounced and rolled... just ahead of [kid_name]'s."
                        julia "We have a winner! [his_name]'s went the furthest!"
                        him happy "And [kid_name]'s a close second!"
                        show kid nervous with dissolve
                        $ demanding += 1

                    "Let [kid_name] beat you.":
                        "I wanted to win... but I wanted [kid_name] to win even more."
                        "I made a big show of spitting hard, but I didn't give it my secret head flick that my cousins and I had worked out."
                        "It landed way behind [kid_name]'s."
                        "My second landed near the first."
                        show kid happy with dissolve
                        him concerned "Oh man! I used to be so good at this!"
                        kid normal "I beat you! I beat you, dad!"
                        him happy "You sure did!"
                        hide him with moveoutleft
                        show kid at midleft with move
                        julia normal "We have a winner!"
                        kid laugh "I can't believe it!"
                        $ responsive += 1

            "The apple peeling contest.":
                "I'm pretty handy with a knife, so I figured I'd try the apple peeling contest. We all got an apple and a knife, and our job was to make as long of a peel as possible without it breaking."
                show pavel normal at left
                show her normal at quarterleft
                show him normal at midleft
                with moveinleft
                show zaina normal at right
                show kevin normal at quarterright
                show thuc normal at midright
                with moveinright
                julia "On your mark... get set... GO!"
                "Even though she made it sound like a race, I tried to take my time. I had to make the peeling narrow enough to be very long, but wide enough that it wouldn't break..."
                "I felt bad for Kevin, whose peel kept breaking. He was trying to make it way too thin."
                kevin "This is more challenging than it appears."
                zaina "Yeah, I think I'm just going to eat mine. None of mine are as long as theirs!"
                hide kevin
                hide zaina
                with moveoutright
                "Pavel kept dropping the knife. He used to be good at this sort of thing, but he just wasn't as dextrous as he used to be."

                hide pavel with moveoutleft
                "[her_name] finished first with a peel about as long as she was tall."
                her happy "I do have a lot of practice with a scalpel!"
                "But her peel was much wider than mine, so I knew my peel would be longer."
                "I was more worried about my real competition - Thuc."
                show him determined with dissolve
                "If he was as good at using knives as he was at juggling them, I was in for a tough challenge."
                "He and I were both cutting slowly and carefully, our eyes fixed on the sharp blade cutting the peel."
                show him annoyed with dissolve
                julia "What a contest we have here! Both evenly matched! Both slicing with such care and precision!"
                natalia "C'mon, we know who you want to win!"
                julia "I am a neutral announcer! I am completely impartial, even if one of the contestants is my husband!"
                if invited_luddites:
                    pete "C'mon, [his_name]! You got this!"
                if invited_miners:
                    brennan "My money's on Thuc. There's no way [his_name] will win this."
                    if (has_strong_marriage()):
                        her normal "Are you talking actual money? How much? Because I'm betting on [his_name]."
                    else:
                        her concerned "They're so evenly matched; either one could win this."
                "I tried to ignore all the comments and concentrate."
                show him concerned with dissolve
                "Finally, we were both finished. We laid the peels out on the ground carefully so they wouldn't break. It was going to be close..."
                julia "And the winner is..."
                show him surprised
                if (invited_miners and invited_luddites and has_strong_marriage()):
                    julia "[his_name]!"
                    him happy "Yes!!!"
                else:
                    julia "Thuc!"
                    thuc "Wow, really?"
                    julia "Good job, sweetie."
            "The arm wrestling contest.":
                "I work hard all day, so I'm probably pretty strong, right? Though I guess a lot of other people do, too..."
                # TODO: Finish this
            "Don't enter any contests.":
                $ pass
    elif (community_17_activity == "games"):
        show thuc normal at center with dissolve
        "Thuc got up and announced we were going to start off with some group juggling."
        him happy "No knives, I hope!"
        thuc "Not for you dinosaurs!"
        "We got into a big circle and tossed around an apple, saying the person's name as we threw it to them."
        "Then he added another apple, and another, and another."
        "When we got to about fifteen it was complete chaos, but everyone was laughing."
        thuc "Okay! For our next game, I need a volunteer to leave the room!"
        "No one was raising their hand except [kid_name]. I figured it might be best if an adult went first to show everyone how it was done, so I raised my hand, too."
        thuc "[his_name]! I can always count on you to be a guinea pig."
        "I left the room, and when I came back, they had formed a line of people."



    elif (community_17_activity == "performances"):
        show ilian normal at center with dissolve
        "Ilian,"

    scene bonfire with fade
    "We ended the night grouped around a blazing bonfire."
    "The flames' warmth warded off the damp chill growing in the night air."

    scene black with fade
    if ate_jellyfish:
        #move to a later, more sparse event?
        "Afterwards, I couldn't stop thinking about the seafood that Pete brought."
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
    # if BOTH luddites and miners are there, they start trade negotiations? affects the firegrass event later.


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

    scene cabins with fade
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
    helen "Yeah, I've got some. It'll cost you though--we only found one this week and it was pretty young."
    him "How much?"
    if c18_no_help_pete:
        helen "80 credits."
        him "Hmm. That's outside my price range. Got any beef bones or nuts?"
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
    him "Yeah, Tomas Perón likes to get his whole family to help plant, which makes it easier to manage, but also harder to harvest."
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
    him "Crabbirds ate all the Perón's corn, so we won't be harvesting it together."
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
        if is_liaison:
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
        if is_liaison:
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
            pavel "That's true, but we're setting a precedent here. What if in 80 years, Pete's group is like 30 people and suddenly want to join back with us?"
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
            $ pstyle = get_parenting_style()
            if (pstyle== "authoritative"):
                "She may stay as a guest but not as a resident, and she must share her findings from her research."
                him "Sounds fair to me."
                "I sent Pavel a message with RET's requests."
                pavel "I'll pass this on. It sounds like calling her a guest is their way of acknowledging that she left."
                jump lily_return
            elif (pstyle == "authoritarian"):
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
            elif(pstyle == "permissive"):
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
            "Lily moved in with her former lab assistant, Miranda Perón."
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
        lily "Zaina and Miranda know about our research, but there are a few things we're working on that I wanted to tell you personally."
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
        "Zaina said that she wanted to see the ocean one last time before she died."
        "We never saw her again."

    return


label community21:
    scene community_center with fade
    "It's predictably overcast this time of year. Lots of people go camping now since there isn't as much danger from solar flare radiation."
    show thuc normal at midright
    show him normal at midleft
    with dissolve

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
    scene stars with fade
    "My family was really excited to see the ocean, even though it would take about a day of walking to get there."
    "We met at the appointed time and place, with rations and blankets in our backpacks."
    scene plain with fade
    show brennan normal with dissolve
    brennan "Thanks for coming out to this joint miner-colonist outing! I'll be laying down a few ground rules."
    brennan "First, always stick with a buddy while we're traveling to the ocean."
    brennan "Don't eat anything unless you are certain it's edible."
    brennan "When you pee, make sure you're far from the river or food. And no smoking in tents!"
    scene path with fade
    "We started walking along."
    her "Wow, it's been so long since I've been this way! I don't think I've been to the ocean since before [her_name] was born."
    her "There's a path here and everything."
    kevin "Yes, I like to visit the ocean at least once a month. And Pete and his cattle are excellent at making a pathway."
    him "Pete comes through here?"
    kevin "Yeah, his family winters near the beach." #TODO: does the player know this some other way? can't remember
    scene canyon with fade
    "We had to climb through some rocky areas, but our progress was good."
    him "What's with the no smoking rule? Is it really a problem?"
    kevin "Firegrass is pretty popular. It's a mild stimulant that the miners use to stay awake so they can work and extended period of time"
    kevin "It's stronger than caffeine."
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
    kid "Oh yeah, I've heard of you. It's your fault Anya's parents are always stressed out."
    brennan "That's one way of looking at it."
    kid "Dad says that you might talk pretty but that underneath you're like a snake."
    brennan "Really? I wonder what that makes you, then..." #is this too weird
    him "A mongoose."
    kid "What's a mongoose?"
    him "A cute, furry mammal that preys on snakes."
    brennan "Interesting..."
    "We kept walking the rest of the day, chatting with each other while we walked."
    scene ocean_sunset with fade
    "We arrived at the ocean in time to frantically set up our tent before sunset."
    "[kid_name] and [bro_name] were actually pretty helpful getting everything setup, though nobody wanted to clear the ground and risk getting stuck with spiny leaves."
    "The moon rose, and we saw glowing lights in the ocean from the jellystars just below the surface."
    if ate_jellyfish:
        "I felt a strange attraction to the lights, and watched them until I fell asleep on the beach."
    else:
        "They were beautiful to watch for a few hours while we set up a fire and warmed up food for dinner."
    scene ocean with fade
    "After a breakfast of mush the next morning, I smelled a smoke that reminded me of curry. It was just some of the miners smoking firegrass in pipes though."
    "We spent time playing on the beach, even though it wasn't especially warm."
    "Some people caught fish or jellystars and tried cooking them."
    "Someone stepped on a sharp rock and [her_name] helped clean and bandage it."
    "That evening, Pete and his family stopped by."
    if luddites > 10: #TODO: calibrate this number and others. don't make this event too easy to trigger.
        #maybe Travis should be in this event too?
        pete "Hey it's good to see you guys!"
        pete "I have a two-way radio now. It turns out communication is good for business."
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
            pete "They can't hurt humans. And the sky looks clear."
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
        pete "Yes, they appear to be English words. Maybe they learned from that waterproof tablet that Lily accidentally dropped in the ocean?"
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
        him "And the firegrass just allows them to be more productive."
        brennan "I don't think it's worth the trade-off. For every extra night a miner works on firegrass, they need a day to recover and catch up on sleep."
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
            pete "I have some cream here that would go really well on these fish."
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
        scene bonfire with fade
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
    if (miners > 10) and (luddites > 9) and (is_liaison):
        nvl clear
        brennan_c "Hi Zaina, Kevin, and [his_name]. I'd like to meet with you and Pete about how we can mine without disturbing his home."
        brennan_c "Except I don't know how to get ahold of Pete."
        him_c "Oh, he has a radio now. I can sort of text him with it."
        brennan_c "How 21st-century. Ask him if he can meet tomorrow evening at the canteen in the miner camp. Around 5pm, if he has a watch."
        him_c "Okay, I sent him the message."
        kevin_c "I am unable to attend, but Zaina will be there."
        "That evening, Pete replied to say he could make it."
        him_c "Pete can come. See you all there."

        "The next evening..."
        scene cabins with fade
        show him at left
        show zaina at midleft
        show pete at midright
        show brennan at center
        with dissolve
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
        # TODO: check usage of Indium/element of shells
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

    elif (miners > 10) and (luddites > 9) and not (is_liaison):
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
        if is_liaison:
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
            sara_c "Brennan is going to start mining in the mountain where Pete and his group are living. Could you give us some advice on how to proceed?"
            sara_c "We're trying to decide if we could get him to leave or if we should cut our losses now."
            sara_c "I just added you to the chat."
            jump Pete_stay_or_go

        label Pete_stay_or_go:
            nvl clear
            zaina_c "Pete's group is currently living in caves in that mountain."
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
                        scene cabins with fade
                        show him normal at midleft
                        show brennan normal at midright
                        him "Okay Brennan, who's coming with me?"
                        brennan "Bandile and Chaco have agreed to come with you."
                        "On the way there, I told them our plan was to intimidate, not kill. I gave them both guns."
                        "We saw Helen as we approached the cave entrance."
                        scene cave with fade
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
                        "They left the caves and started a camp nearby. The mining proceeded, but suffered from so many mysterious setbacks and equipment malfunctions that they stopped halfway through and changed to a different location."
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
                        him_c "But we'll have to sacrifice our relationship with Pete's group to do so."
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
                brennan_c "It's not like Pete has ever stuck it out for us."
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
        pete "What do those damn miners think they're doing?!"
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
        him_c "Pete's group doesn't see it that way."
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
                if is_liaison:
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
            "The mining stopped." #this can happen if you're not the liaison, after the luddites vandalize mining equipment
            if is_liaison:
                "I didn't mention anything to RET, but Brennan must have, because Mayor Grayson sent me an urgent message the next day."
                pavel_c "Please come meet me in my office today."
                him_c "Okay, what's is about?"
                pavel_c "I think you know..."
                "I guess RET probably wasn't happy that the mining had stopped."
                pavel "RET has asked me to designate a new liaison."
                him "Okay. Fine."
                pavel "What did you think would happen? You didn't even consult them."
                him "I know what they would have said."
                pavel "But you have to let them say it. You're not the only one in contact with them."
                pavel "RET asked me to make the nominations for two candidates. I'm sending out a poll tonight to vote for the new liaison."
                him "This will just help me focus on farming--the important work."
                "Sara won the most votes and became the new liaison."

                $ is_liaison = False

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
           #     "Plz elect a liaison 2 help RET & colonists communicate & resolve conflicts."
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
    her "See if you can keep him warm. Maybe a small warm-blooded animal could sneak back there?" # what? I don't get this
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
        # you are never the liaison in this option, since you lose liaisonship in community 22 if you choose to stop mining
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
    bro "Okay..."
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
        $ modify_credits(100)
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
        him "I get plenty from my goats. What are you selling it for, though?"
        thuc "Just 100 credits for a pint."
        menu:
            "That's crazy!":
                him "You're nuts."
                thuc "You'll be back."
                him "Yeah, when you have your goat cheese reduced price for quick sale."
                thuc "You should save some of your best crops and sell them on your own."
                him "So I can buy your premium goat milk? I've got enough to worry about."
                thuc "Suit yourself."
                $ colonists += 1 #arguable
                return
            "How come I don't earn that much?":
                him "I know how good the extra creamy stuff is...But I don't earn that kind of money selling my crops to Ilian."
                thuc "Give me some of your best crops to sell. I bet I can make you a lot more money than you currently make."
                him "Yeah, and how much of the profit are you going to pocket?"
                thuc "I promise I'll only keep ten percent of the sale!"
                $ random_crop = farm.crops.random_crop(include_animals = False)
                him "Okay, I'll let you try selling some [random_crop]. Message me when they sell!"
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
        thuc "No, usually people make it into cheese or lotion or something."
        thuc "Nice lotion sells for even more than goat milk."
        him "I'm surprised Miranda hasn't tried that."
        thuc "She still does some lab work, but she's gotten really into making soap and stuff. She says it's specially formulated to kill microflora on Talaam."
        thuc "She and Julia are making a plum syrup together too. It tastes amazing."
        thuc "The price of Pete's firegrass has gone waaaay up, so I think some teenagers are trying to grow some on their own."
        thuc "Some people have even tried making glass bottles and vases... rumor has it they were trying to make imitation shells."
        him "Ugh, is that still a thing?"
        thuc "Yes, it is."
        thuc "Didn't you read Julia's latest 'Talaam Times' that did an economic analysis of our luxury goods and reviewed select products?"
        him "I didn't want to pay 20 credits for it! That's like the price of beans for a month."
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
            $ modify_credits(400)
            kid "Hey dad, that farming guide you wrote is really popular."
            him "Really?"
            kid "Yeah, Oleg bought it and made an app version!"
            him "Hey, he didn't have my permission to do that."
            kid "He's not making that much money off of it."
            him "Ugh."
            "I guess I wasn't going to fight a kid over copyright law..."
        "Babysit small children and teach them farming.":
            "I offered to babysit a few small children and give them lots of individual attention for a few hours every morning over the summer."
            "I promised to show them the beauties of Talaam and teach them the joy of farming."
            "A few people were interested, and I chose two families with kids to help."
            "I'd go pick up the kids in the morning, and then I'd drop them off at the co-op daycare after lunch."
            "At first it was really difficult. The kids had a hard time changing their routines."
            "I had forgotten how hard it is to do anything with kids in the house, so often I'd still be working on my farm after dinner."
            "I did make a lot of money though!" #+2000/200 credits but more stress?
            $ modify_credits(2000)
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
            $ modify_credits(400)
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

    "I had seen some tasty-sounding jellystar recipes lately."
    if not ate_jellyfish:
        him "Hmm. These jellystar recipes look kind of good."
        him "Maybe I should try them."
        menu:
            "Buy and eat them.":
                "I bought some dried jellystars and we had them in soup."
                $ ate_jellyfish = True
            "Don't eat them.":
                "I decided not to eat them."
    else:
        "I ate them all the time, so it was fun to see even more ways to enjoy one of my favorite foods."
    "The jellystar farm made them quite an economical food."
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
    her "They probably don't, but it hasn't been studied in detail. So it's probably safer not to eat it."
    him "What about the cows from the colony?"
    her "I compared the meat from them with the meat from Pete's cows. The colony's cows also have irregular cells, but not as frequently as Pete's cows do."
    him "Pete's cows are outside more, but they have those UV blankets."
    her "I don't think they don't work very well. I've seen the cows pull them off."
    her "My question for you is if you think I should publish the results of my study, given that Pete's beef might be dangerous."
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
            her "True, my sample size is pretty small, and we don't have any proof that eating cancerous meat is dangerous... I'll keep studying it."
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
    her "Well, they do help her sleep, but then she feels sleepy in the morning and usually uses firegrass to help her feel more awake."
    her "She has frequent panic attacks and has lost an unhealthy amount of weight."
    her "Mayor Grayson agrees that we don't have the resources for a mental hospital."
    her "Sara completed training to do some mental health counseling and has started sessions with her, but she needs more than just therapy."
    him "Like medicine?"
    her "We don't have the kind that would help her."
    him "Hmmm."
    her "She doesn't seem to be getting better anytime soon. She has suicidal tendencies."
    him "We should help her change something in her life to break this cycle."
    her "I feel like I've done everything I can. I'm going to present her case to the town council to see if they have other ideas."

    if is_liaison:
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
        her "The long-term side effects are similar too."
        brennan "I've never heard of someone suffering from a caffeine overdose."
        her "Well, it can happen. Usually with heavy users of energy drinks."
        if miners > 10: #from community21, if you talked about it with Brennan
            her "A few years ago, I gave miners recommended doses of firegrass, but even with those doses, miners have experienced insomnia and reduced appetite."
        else:
            her "Even miners who don't take very much experience side effects like insomnia and reduced appetite."
        her "I think we should discourage the use of firegrass somehow. I don't want to see any more cases of insomnia and depression."
        brennan "I also don't want to see that. But I don't think outlawing firegrass will stop people from using it."
        brennan "Pete is going to sell firegrass no matter what we decide."
        "How do I feel about the issue?"
        menu:
            "We should try to ban firegrass use.":
                $ ban_firegrass = True
                him "Even if people will still use firegrass, we should do everything we can to stop people from abusing it."
                him "I think that we should make a law against using firegrass, and punish those found using it."
                brennan "Punish them? With a fine?"
                him "Yes. And we should search their property and confiscate any firegrass we find there."
                brennan "But we know Pete is going to sell it no matter what we do."
                him "Is he? I think Pete is smart enough to find something else to sell."
                her "What if I arranged to buy some firegrass from him on behalf of RET, and then prescribed it to people who have difficulties staying awake?"
                him "And we can make it against the law to use firegrass without a prescription."
                pavel "But how will we know who is authorized to use it?"
                her "I could flag their record, but if it's public information, that violates patient confidentiality."
                pavel "Maybe you could send them a copy of their prescription, and they could choose to show it to someone enforcing the ban."
                her "That would work."
                him "And the fines can help pay for [her_name] to hire a part-time assistant to help with the prescriptions."
                her "Oh, good thinking."
                him "But who would we choose to enforce the ban?"
                brennan "It should be someone who's part of their respective community, so they won't be resented as much."
                him "Does that mean you're volunteering, Brennan?"
                brennan "No, I do enough hounding. Let someone else experience the social isolation that comes from enforcing rules."
                brennan "I can find someone to check with the miners. We'll probably use a warnings system."
                pavel "I can assign a few people in the colony."
                brennan "What should I recommend to miners who are sleepy on a night shift but can't get a prescription?"
                brennan "I know we have some green tea around, but there never seems to be enough..."
                her "Good point. A ban would be more effective if there were some alternative drug to use."
                menu:
                    "What do I recommend?"
                    "Grow more tea plants.": #change to green tea
                        him "Let's make tea plants a priority this growing season."
                        him "If we plant them around the same time, we can process them together too."
                        pavel "I'm interested in making black tea with the leaves."
                        him "Sounds good. Maybe some people will like black tea more than green tea."
                        $ grow_more_tea = True
                        jump wrap_up_council_26
                    "Don't do anything.":
                        him "I think it's good enough to be able to get a prescription for firegrass."
                        him "It works about as well as tea, and it's a lot easier to grow."
                        brennan "I wonder if firegrass would make a good tea?"
                        her "That sounds like something Julia would know. She loves tea."
                        jump wrap_up_council_26
                    "Ask if the night shift is necessary.":
                        him "Is it really necessary for the miners to work through the night?"
                        brennan "We have a quota from RET we're supposed to meet each year. Sometimes it's not necessary and sometimes it is."
                        pavel "What if you cut down their hours? It could actually increase productivity."
                        if (miners > 10): #is it mean to make this an option where it won't work?
                            brennan "I think it will help with productivity." #he only agrees with you if your relationship with miners is good enough?
                            $ miners += 1
                            $ work_fewer_hours = True
                            jump wrap_up_council_26
                        else:
                            brennan "Send me an e-mail after the meeting and we can talk about it."
                            $ brennan_refuses_fewer_hours = True
                            jump wrap_up_council_26

            "We should try to reduce firegrass use without outlawing it.":
                him "I agree. Let's try to reduce the amount people are using without banning it."
                her "So how would you cut down on firegrass use?"
                brennan "We could educate users about its side effects. Make posters and engaging, informational narratives that show the effects of its use."
                brennan "Maybe Carol could help educate users when she's feeling better."
                sara "I know an enterprising young person who could make an app about how to use firegrass."
                him "Is it Oleg?"
                sara "Yes! He is really interested in educational technology."
                if miners > 10:
                    sara "You could have them access their own health stats from the database and it could tell them their recommended dosage."
                    her "But my recommended dosage levels were incorrect before. Soon my recommended dose is not going to give users any noticable alertness."
                    her "Also, there is no way I'm giving Oleg access to the health database."
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
                    "Grow more tea plants.":
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
            jump wrap_up_council_26

        label wrap_up_council_26:
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
                # TODO: should we unlock tea as a crop?
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
    ilian "We're also to stop eating chicken, goat, turkey, and cow meat and to use the synthetic meat as a replacement."
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
    ilian "That's the final goal. They expect us to halve our herd in two years."
    thuc "Not having bacon or beef or chicken is a terrible blow to our flavor options for meals."
    thuc "What about milk, dairy, and egg products? Are they exposed to the radiation as well?"
    ilian "Um, they didn't specifically say anything about that..."
    thuc "We should keep chickens and turkeys for their eggs and feathers at least."
    # TODO: what about your goats?
    ilian "I agree."
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
        # TODO: Maybe if you did both of those, you don't have any other choice but to engage.
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
                brennan "I need you to be our new alien liaison!"
                $ shell_count += 2
            else:
                brennan "All my jellysquid farms were destroyed anyway. I can't farm them anymore."
                brennan "And I already made promises to the miners based on the shells I have now."
                brennan "Sorry, my hands are tied."
            "I wasn't sure if I had enough shells, so I wrote up my experience and ended with a plea for anyone holding onto a shell to return it to the squid people."
            "I had Julia print it in that week's {i}Talaam Times{/i}" #italics
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
#                           "Why..."
#                            "you":
#                                menu:
#`                                  "Why you..."
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
                "I had a long talk with Zaina about the jellysquids. She chided me for not taking any pictures or recording my 'conversation' with the jellymother."
                "When I mentioned the mudfish, she looked excited."
                zaina "A few years ago I studied that fish."
                him "What eats it?"
                zaina "It's one of the few fish the jellystars won't eat. But a few other, bigger fish will eat it without a problem."
                him "The ones called Shills? Because they make a really cool noise but disappear if you approach them?"
                him "How do they compare to jellysquid shells for metal content?"
                zaina "Well, it's not edible for humans. Let me bring up the report."
                zaina "Some species had a high level of heavy metals. I don't know what kind though."
                him "Wow, this could be big! The same kind of metals that RET wants?"
                him "Maybe instead of taking the shells, Brennan could just mine the mud. The mudfish probably eats some kind of worm that gets the metals from the mud."
                zaina "Or they could just keep doing what's working, which is digging in the mountains."
                zaina "Brennan gave up on the jellysquid farms. Just leave well enough alone."
                him "I told the jellymother I would try to help her!" # TODO: decide if jellymother is her or them. make capitalization consistent.
                zaina "Sometimes the most helpful thing you can do is to go away."
                him "They can sort of write to us Zaina! How are you not curious about that?"
                zaina "We didn't publicize the research, but I've 'spoken' to the jellysquids before."
                zaina "I helped Dr. Lily teach them how to 'write'."
                zaina "Now that I know that the jellymother can use them to communicate, it explains why sometimes they were so much more articulate than others and how they could teach each other new things so quickly."
                zaina "These animals are one of the most interesting beings I've studied. I don't want mining to wipe them out."
                him "They asked for help finding shell food. It sounds like this mud fish could help, but they don't like how it tastes. Is there a way we can make it taste better to them?"
                zaina "I think it's just the skin that tastes bad. So maybe if we caught them and made them into filets, they would eat them?"
                him "Or maybe the Shills that eat the mud fish would have the right minerals in their meat?"
                zaina "I can do some field research this weekend."
                him "Great. Maybe the jellymother will talk to you too."
                zaina "You're not coming with me?"
                him "I've been out there twice already. Message me if there's an emergency."
                "I left feeling like maybe there was hope for reconciliation between us and the jellypeople."
                "I could tell Breannan and Zaina about possibly mining in the mud instead of in the mountains."
                menu:
                    "Tell them.":
                        "I told Brennan and Zaina about the heavy metals in the mud. They sounded exicted to try mining it."
                        #currently there's no follow-up for this decision... remove it?
                    "Don't tell them.":
                        "I decided not to tell Brennan and Zaina about the heavy metals in the mud."
                "Next week, Zaina returned and asked me to meet with her."
                zaina "The jellysquid seemed to remember me, so I didn't have trouble getting them to try a few different foods."
                zaina "I was able to catch a few mudfish and feed their filets to a jellysquid."
                zaina "They did eat it, and I noticed that their shell grew a little the next day. It's an unconscious process for them, so they can't really tell me how much their shell is growing at a given time."
                zaina "I had a hard time catching the Shill, despite using mudfish as bait. Eventually the Jellymother found me and I told her what I was trying to do."
                zaina "She seemed surprised. The Shill is difficult capture, so they rarely eat it."
                zaina "Still, she was curious, so she instructed some of the jellystars to make a net to catch one."
                zaina "She killed a Shill and had jellysquids eat it, and I observed bigger growth patterns in those jellysquid the next day compared to the one that ate the mudfish."
                zaina "That matches my hypothesis that consuming a higher concentration of metals would increase their growth more rapidly. They are usually limited by what minerals their body has on hand."
                him "So what do you think would be best for the jellysquids?"
                zaina "It's hard to say. The jellysquids would need our help to eat the mudfish, since its skin contains toxins. But the mudfish's concentrations are the most similar to what they're used to."
                zaina "The jellysquid can easily eat the Shill, but instructing them to eat a fellow predator could really mess with the food chain ecology. Also, it's possible that their shells would grow more quickly than they're used to."
                him "Hmm. That does sound like a difficult decision. Do you think we could farm either?"
                zaina "Yes, we could. It would take a lot of work to make an aquatic farm, but maybe we could use it for other fish later."
                "What do I think is better?"
                menu: #should this be a decision? remove it?
                    "Serve mudfish to the jellysquids.":
                        him "I think we should encourage them to eat mudfish. If we all work together to catch and skin them, we'll be able to show the jellymother that we really care."
                        him "Also, we won't have to worry about shell overgrowth."
                        zaina "I just hope the colony is strong enough to help with this."
                        $ serve_mudfish = True
                        jump aquaculture
                    "Have them eat Shills.":
                        him "I don't know if we could farm and skin enough mudfish to grow hundreds of shells."
                        him "If they keep eating Shills, they won't have to rely on us to create new shells."
                        zaina "But we're going to try to farm them so we won't accidentally collapse the food chain, right?"
                        him "Right."
                        zaina "I just hope the colony is strong enough to help with this"
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
                                    $ jellypeople_happy = True
                                    return
                                else:
                                    "Shills had a longer incubation period than I anticipated. The jellymother started feeding Shills to emerging jellysquids."
                                    "Farming the Shills took weekly maintence, which we shared. After the Shills were big enough to fend for themselves, we released them into the wild."
                                    "A few of the jellysquid ate too much Shill and ended up with large shells, but they seemed to adapt to it fairly well."
                                    "The Jellymother seemed impressed that we followed up on our promise."
                                    "She presented us with some of the fish we could eat as a token of good will."
                                    $ jellypeople_happy = True
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
            him "There's plenty of enjoyable things in life even if you can't remember them. You don't have to remember anything to appreciate a good meal, or share a joke with someone, or enjoy a sunset."
            her "But is that enough to make life worth living?"
            him "I would still want to live, if only for those everyday moments."
            her "Well, this isn't about what you or I want. It's about what Mayor Grayson might want."
            him "Okay, okay."
            $ against_euthanasia = True
    "The next day, Sara sent out a message saying that Mayor Grayson was ready to retire and that we would be electing a new mayor at a meeting next week."
    if is_liaison:
        "She also invited me and [her_name] to a meeting that night to discuss Mayor Pavel Grayson's future."
        # Julia is here too. Brennan is here if your mining relationship is high enough. explain why Julia is there?
        sara "Thank you all for coming. Pavel has been experiencing early signs of dementia for a while now. Recently his memory and sense of direction has become worse." #TODO: check last three events to see if Pavel is in them
        sara "Pavel has requested that he be allowed to end his own life before his cognitive abilities decline too much more. He agreed on a threshold with [her_name]."
        sara "He wrote down his wishes and signed it, and I witnessed this. He was oriented to time, place, and circumstance at the time."
        sara "[her_name] has agreed to do weekly assessments and determine Pavel's cognitive abilities."
        sara "I've called you here because you have leadership positions in our community. Julia, I figured that it would be easier for you to attend this meeting than to get a report secondhand for your newspaper."
        sara "[her_name], can you take it from here?"
        her "There isn't a guideline about euthanasia in RET's health manual."
        her "I compared a recent assessment to his scores in previous years, and Mayor Grayson's, I mean, Pavel Grayson's dementia appears to be declining."
        her "At this rate, he may need constant supervision in six months to a year."
        her "I wouldn't be able to supervise him and perform my duties as a doctor at the same time."
        her "My assistant could watch him for half of her normal hours, but it would decrease the amount of preventative care visits she makes." #gender check assistant
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
            him "Okay..."
            jump fill_gap
        else:
            him "[her_name], are you ready for this?"
            her "Yes. I'll be helping Pavel avoid an irreversable, extended state of confusion and disability."
            him "I know, but you still have to give him a fatal injection right? Technically you'll be the one killing him."
            her "In a procedure he requested."
            jump fill_gap
    # if is not liaison


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
    julia "Please vote for me! I don't want to oversee Thuc's sewage factory."
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
            $ kevin_elected = True
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
    her "He needs adult-sized diapers... and someone to spoon-feed him. We should probably move him to the hospital."
    him "We can do it."
    "One day Julia was late coming to watch him, and Sara left him alone."
    "Julia couldn't find him that night and we all started searching for him."
    "In the morning, we found his body drowned in the river."
    scene church with fade
    "His funeral was well-attended, and we reminisced about his optimistic spirit."
    return

label euthanasia:
    "After about a month, [her_name] announced that Pavel's euthanasia would be that week, and asked villagers to pay their final respects."
    "Pavel said goodbye to most of us. He wasn't completely present."
    "After [her_name] performed the euthanasia, we held a simple funeral where we celebrated Pavel's lifetime of good-natured optimism."
    return


label community29:
    if kevin_elected:
        "Kevin was a logical mayor, as we'd expect from him. Though he assured us of his objectivity, he helped the miners more often than anyone else."
        "He worked with them and talked with them more than he did to us, so it wasn't surprising."
        "He worked with Brennan to have a work rotation with some of the farmers. Farmers would work in the mines for a day each week while the miners worked in the fields."
        "At first there were a lot of mistakes on both sides, but eventually we farmers learned the basics of mining and got to know the other miners better."

    else:
        "Julia was a behind-the-scenes kind of mayor. Things went smoothly because she talked to everyone privately, and she was able to distribute important information through her newspaper."
        "Eventually interviews with each resident of Talaam were featured in the Talaam Times, including the luddites and the miners."

    if jellypeople_happy:
        "I kept communicating with the jellypeople through the jellysquids. We traded land meat for seafood."

    "I was working in the canning factory after a harvest when [her_name] messaged me."
    nvl clear
    her_c "Helen is pregnant!!!!"
    him_c "Oh, congratulations to her."
    her_c "She's a little older than I am, and she's already in the second trimester."
    him_c "Is that a bad thing?"
    her_c "She's in her mid-forties in Earth years. Even in regular hospitals, that's considered a high-risk pregnancy."
    him_c "Oh... do you think she'll want an abortion?"
    her_c "She didn't ask for one."
    her_c "Since she's no longer a colonist, I have to figure out how to charge her for medical expenses..."
    him_c "Okay..."
    # TODO: wouldn't she stay with Travis at his restaurant?
    if (luddites > 5): #should this number be higher?
        her_c "Which I'll figure out. The reason I'm messaging you is that she wanted to stay with us during the last trimester of her pregnancy so she could be nearby in case of complications."
        him_c "Huh. Where exactly will she sleep?"
        her_c "She said she could bring her sleeping materials. Maybe we can fold them up when she's not using them?"
        him_c "If she's okay with that... maybe we can go camping to have a little privacy now and then *wink*."
        "Helen came to stay with us. She gave us a big wheel of cheese and a string of dried fish the day she arrived."
        jump helen_convo_29
    else:
        her_c "She's didn't want to stay in the colony, so she and her family are staying in their summer house until she has the baby."
        her_c "That way I can help her quickly when she goes into labor."
        "I didn't really see her at all and forgot about her for a few months."
        "I saw Pete dragging her to the hospital on a stretcher. He refused my help."
        "I followed them in case I could help [her_name]. She was working so quickly that I was worried she would poke me with a needle accidentally."
        her "I'm working as fast as possible and I'm not sure she'll make it. Get Julia and Van so they can help me."
        scene cabins with fade
        "Her radio wasn't working, so I ran all the way to the mining camp to find them. Even running back, it took over an hour."
        scene hospital with fade
        "By the time we got back, Helen had delivered the baby, but it was stillborn."
        "[her_name] was still working furiously."
        her "Go find Ilian!"
        him "Why?"
        her "He has O- blood and we're all out! We need to do a blood transfusion if we want Helen to live."
        him "Okay, okay!"
        "The storehouse was close by, and luckily Ilian was still there."
        him "Ilian, come with me! We need you to give blood to Helen."
        ilian "Wait, I need to lock the storehouse."
        him "Just hurry!"
        "As soon as we arrived, [her_name] got the tubes ready for the blood transfusion."
        her "Helen, stay with us for a little longer!"
        pete "Please save her!"
        her "I'm working as quickly as I can!"
        "We heard the heart rate monitor slowing, and then it stopped."
        "[her_name] tried to resucitate Helen for a long time, but was not successful."
        her "We were too late. I'm so sorry Pete."
        "Tears streamed down his face. He stayed with her body until [her_name] locked the hospital for the day."
        "Later Pete came back for the body, which he buried in a grave near the ocean."
        "A few weeks later there were still some loose ends from her hospital stay."
        nvl clear
        her_c "Does anyone know how to contact Pete? I need to talk to him."
        ilian_c "I thought [his_name] was pretty good friends with him?"
        her_c "That was a long time ago."
        kevin_c "I saw him drying fish by the ocean a few days ago."
        her "[his_name], I'm going to take the wagon to find Pete. Want to come with me?"
        him "Why? I doubt he wants to see us."
        her "Pete authorized me to withdraw the credits I needed from his account, but it was completely empty."
        her "I need to talk to him."
        him "Okay. I don't think I can leave the farm this week, but take the radio and keep me updated."
        her "Will do."
        him "Do you need the wagon?"
        her "If he wants to pay in food I want to be able to transport it."
        him "Okay."
        "She left early the next morning. That evening she radioed me."
        her "{i}I found Pete and told him the problem. He was really surprised that he didn't have any credits in his account.{/i}"
        her "{i}He got angry and told me it was my fault that Helen died.{/i}"
        him "{i}It sounds like he's still mourning her death.{/i}"
        her "{i}I'm going to ask him about it again in the morning, otherwise I might just call it a loss.{/i}"
        "I went to bed hoping that [her_name] would figure something out."
        "I didn't hear from [her_name] until she got back the next evening."
        "She gave me a big hug."
        him "Welcome back! How'd it go?"
        her "Thanks. At the crack of dawn Pete told me to leave and that he wasn't going to pay anything to a bunch of murderers."
        him "Huh."
        her "He followed me about halfway back... it was super awkward."
        her "I was afraid he was going to attack me, but I think he just wanted to make sure I was really leaving."
        him "What are you going to do about him not paying?"
        her "I guess I won't give him hospital services until he makes an effort to pay. It's more the principle of the matter now."
        him "Yeah, it's not like you can actually buy more hospital supplies with the credits."
        her "Exactly."
        return

    label helen_convo_29:
        him "How are you liking life back in the colony?"
        helen "Well, there are so many people to talk to. It's kind of overwhelming."
        helen "Some people are so busy that they don't have time to talk to me, but it's also a relief."
        helen "It's funny because I used to read up on all the latest community forum posts when I lived here."
        helen "It made me feel more isolated, because I never had any cool news to share."
        helen "I haven't looked at a forum in ages and it's such a relief. If someone wants to tell me something, they can come find me."
        helen "If it's not important or someone else can take care of it, then no one bothers me!"
        helen "I really miss my family though, and certain foods we like to make."
        him "Really? What kind of food?"
        helen "Well, when we butcher a cow certain cuts sell pretty quickly even at high prices. But other parts aren't as popular."
        helen "I like to make a soup with the feet and tail and some of the innards."
        helen "We even ate the brains a few times! It's not very healthy but it was something different."
        helen "I wonder if that's why I have high blood pressure now..."
        if keep_buying_pete_beef:
            him "How is the herd doing? Pete hasn't come by to butcher or sell meat in a long time."
            helen "The butchery in the colony is actually an artificial meat factory now!"
            helen "We have to do our own butchering, so we only sell raw cuts to people who are willing to come to us to get the food."
            helen "The rest, we dry out or slow-cure."
            helen "Beef definitely isn't as popular now, so our herd is a bit smaller."
            helen "Our cheese and cream are pretty profitable, and our dried fish is the most popular."
        else:
            him "Are you still raising cattle?"
            helen "Oh yes. The herd is getting a little smaller, but we can sell it for more now that we're not competing with the colony's beef."
            helen "Our dried fish is really popular, as is our cheese and cream."
        him "So you have high blood pressure. I heard that's really common in late pregnancy."
        helen "I know. I just keep thinking that I should have been more careful about eating animal fats."
        helen "Or maybe I'm just too stressed out and it would be better if I could just calm down."
        him "There isn't much you can do about it now besides follow [her_name]'s instructions."
        helen "I wish there were something I could do. I feel so unhelpful."
        him "Just try to stay healthy and grow that baby."
        helen "Maybe if I concentrate hard enough, she'll grow an extra eye!"
        him "Do you know what you want to name her?"
        helen "Yes. Before we left, Pete and I agreed to name her Sage."
        if community_22_compromise or community_22_mined_anyway:
            helen "Oh, I brought a set of Talaam chess with me! Want to play?"
            him "Sure, I'll play."
            "The game was very complex and involved a randomized play field made with elaborate wooden cubes."
            "Depending on the design on the cubes and the side they were facing, your pieces could move or interact in different ways and even change the orientation of the cubes themselves."
            "I didn't quite understand it the first time I played it, but after a few times I got really into it."
            helen "I brought a few extra sets of this game if you want to buy a copy!"
            him "With all the handmade components, I think it might be too expensive for me."
            helen "Start saving now! You can't replicate craftsmanship like this with a 3D printer."
        else:
            helen "I've really missed playing board games. Does the library still have 'Plunder, Trial, and Jailbreak'?"
            him "Oh, that game! Some kid checked it out and lost half of the jury deck and all the inventory cards."
            him "No one has bothered to print out replacements, but if you have time, you could probably figure it out."
            helen "Thanks, I will!"
        "For the last month of her pregnancy, Helen was on bedrest in the hospital."
        "I stopped by often to see [her_name] and I played a game or two with Helen."
        "Helen had always been pretty shy, but as a community we completely doted on her as she survived her pregnancy."
        "Natalia made a beautiful quilt for the future baby, and Travis made a wicker cradle."
        "Joanna made a waterproof book with high-contast images, and the elementary school kids made a mobile out of felted plant fibers."
        "Two weeks after she went on bedrest, Helen stopped taking visitors."
        her "Helen wants to be alone right now... she told me to tell everyone that the fetus is dead and she'll be having a stillbirth."
        him "That's so sad. We were all looking forward to meeting Sage."
        her "I wish I could have prevented this. Pete is coming tomorrow, and then we'll induce her labor."
        "Helen delivered her stillborn baby, but started hemmoraging and had to have a blood transfusion until [her_name] could stop the bleeding."
        "Ilian had her same blood type and gave blood to her."
        her "Helen, I'm so glad that you surivived! There were a few times where I wasn't sure if you would make it."
        helen "I'm glad I survived, too."
        pete "Me three."
        her "Unfortunately a blood transfusion is very expensive in terms of using up scarce resources..."
        pete "I think I have enough credits to pay you."
        her "Okay, can you approve the transaction?"
        pete "Sure, just hand me your tablet."
        pete "What gives? It's saying I have insufficient funds."
        her "Let's try charging just one credit."
        pete "What is going on? It still says insufficient funds."
        pete "[his_name], can you try drawing a credit from my account to verify that it's not just something on [her_name]'s tablet?"
        him "Okay, here."
        pete "Still the same problem."
        pete "I know I had over a thousand in there last week."
        pete "Someone stole from me."
        pete "But I guess that's my problem."
        helen "Here, take Sage's things and sell them to the storehouse. That should pay for some of it."
        helen "We can settle the rest later. When can I go home?"
        her "I want to keep you under observation for another two days. At least keep the quilt from Natalia?"
        helen "We don't have any use for those things now... besides selling them."
        "After Helen was well enough, she and Pete left. They buried Sage's body near the base of the mountain."
        return

# many of the endings have Terra going back to Earth. Does a shuttle arrive at the last event? Is it taking some of the miners back at the end of their contracts?
# I think that sounds good.  It's kind of a nice circle and parallel to the first game.  That would make the miners have ~12 year contracts in Earth time.
#Carol's husband dies in what appears to be an accident. He is in a wheelchair and his chair tips in the rain while Carol is nearby. She reports that she was distracted by one of her children.
#Further investigation shows that their family was scheduled to return in the upcoming shuttle. Now that he is dead, the first person on the waitlist was ____.??
#Van was still visiting Carol's family pretty frequently. Can we just use old Thuc character art for Van? He reports that she was recently using fireweed, but seemed short on credits.
#Carol's husband's tablet is retained as evidence. He only used the tablet for a few games--he could no longer read or write. Yet it appears that Carol was using the tablet to message someone...
#Oleg's app is there! It has been modified and her dosage is pretty high.
#JULIA DEALING FIREWEED (transported by your daughter?) bum bum bum
# WHO STOLE PETE'S CREDITS

label community30:
    $ account_checked_counter = 0
    $ know_noel_had_firegrass = False
    $ checked_noel = False
    $ checked_joel = False
    $ checked_julia = False
    $ checked_van = False
    $ checked_sara = False
    $ checked_oleg = False
    $ checked_terra = False
    $ searched_bed = False
    $ searched_cupboard = False
    $ searched_sofa = False
    $ visited_joel_house = False
    $ knows_previous_head_injuries = False
    $ know_noel_received_firegrass_deliveries = False
    $ talked_to_pete = False
    $ accuse_noel_of_murder = False
    if kevin_elected:
        "I was walking home from the library with a fresh load of ebooks in my tablet when I ran into Kevin, headed there himself."
        kevin "Hello [his_name]. I was thinking of e-mailing you but I was unable to formulate a cohesive message."
        kevin "I'd like your help with something that happened in the mining camp."
        him "Okay. Want to tell me about it in the library? I don't really want to stand outside in the rain."
        kevin "It is a sensitive matter, and I would not like to be overheard..."
        him "No one's in there, it's fine."
        #change scene to library, if we have that already, otherwise they can talk outside
        him "What's this all about?"
        kevin "There has been a death in the mining camp. We are not certain if it was an accident or a murder."
        kevin "I would like your assistance in the investigation, as a neutral party."
        him "Sure, yeah, I can help. I don't have much experience with investigation, though."
        kevin "Detectives or police would be best, but as there are none, I am asking you."
        him "Is there a crime scene? A primary suspect?"
        kevin "The woman who almost killed herself about two Earth years ago... do you remember her?"
        menu:
            "Yes":
                him "Sure. There was a town council to see how we could help her."
                kevin "I was reading the documentation from that very town council meeting."
                kevin "They called her Carol, right?"
                him "Yes, [her_name] is big on preserving patient confidentiality."
                kevin "Her real name is Noel."
                him "I always knew [her_name] was secretly a fan of puns."
            "No":
                him "That's not ringing any bells for me."
                kevin "She was consuming an IMMENSE amount firegrass."
                kevin "The drug is not especially habit forming--it's comparable to energy drinks back home."
                kevin "The town council notes referred to her as Carol, but her real name is Noel."
                him "Is that supposed to be some kind of joke?"
                kevin "I believe [her_name] was trying to protect her identity, but did not succeed."
        kevin "Noel's husband, Joel, recently died from blunt head trauma."
        him "Okay. Was Noel with him at the time?"
        kevin "Noel says that she and Joel went just outside their house to look for shooting stars."
        kevin "She said that it started to rain, but Joel wanted to watch a little longer."
        kevin "She says that he dropped his binoculars but told her to keep looking. He reached down to grab them and his wheelchair tipped over."
        kevin "He fell face-first onto the concrete-like material just outside their home."
        kevin "She wasn't able to lift him up, so she rolled him over. She said he was completely unconscious and had stopped breathing."
        kevin "By the time she received assistance from the nearby nurse, he was already dead."
        him "I see. Is [her_name] going to do an autopsy?"
        kevin "Yes, we just delivered the body to the medical wing."
        him "Do I have your official authorization to question Noel and any witnesses?"
        kevin "I recommend that you not question Noel as an authority figure, because she stated to me that she would remain silent in such a situation."
        kevin "Nevertheless, you may officially question any witnesses to Joel's death."
        him "Can I get that in writing?"
        kevin "Certainly. I will send you an e-mail stating such, along with photos of the crime scene."
        kevin "We also have Joel's tablet and a few of his other possessions, which we seized as part of our initial investigation."
        him "You just took his stuff? Why don't you completely believe Noel's story?"
        kevin "I do not wish to bias you. Please, start your own investigation and then I will tell you my ideas."
        him "I'll get started right away."
        jump investigation_start

    else:
        "It's the rainy season. I don't have to worry about irrigation, but weeds grow like they're going out of style."
        nvl clear
        julia_c "Hi [his_name]. Is there a time we could meet? I have an urgent matter to discuss with you."
        him_c "If it's so urgent, maybe you could just tell me now? I just have a few more weeds to pull in this sopping rain and I'd like to be done."
        julia_c "There's been a death in the mining camp."
        julia_c "The primary suspect is someone who was a frequent client of mine, so the town council suggested that I ask an uninvolved party to assist in the investigation."
        him_c "k you can come over in 30 minutes."
        #scene change to house.
        him "Want some hot tea?"
        julia "I love tea. What do you have? Any of my special plum tea?"
        him "Do I look like I'm made of money? I have mint tea. And if you're feeling tired I can add a few green tea leaves."
        julia "Yes, please."
        him "Okay, so tell me more about what happened."
        julia "Do you remember about two Earth years ago, there was a woman who almost killed herself?"
        menu:
            "Yes":
                him "Sure. There was a town council to see how we could help her."
                julia "I was reading about that meeting in my special mayor files."
                julia "[her_name] called her Carol in that meeting. But her real name is Noel."
                him "Yes, [her_name] is big on preserving patient confidentiality. Well, at least I thought she was."
                julia "Not a very good pseudoname for her, was it?"
                him "Nope."
            "No":
                him "Really? I don't remember that."
                julia "She was under a lot of pressure at the time."
                julia "Her husband was recently disabled, they had two small children, and she became the family's main breadwinner."
                julia "In my special mayor files, they referred to her as Carol, but her real name is Noel."
                him "Wow, great pseudoname."
                julia "You can see how it was easy for me to make the connection there."
        julia "Noel's husband, Joel, died from blunt head trauma last night."
        him "Okay. Was Noel with him at the time?"
        julia "Noel says that she and Joel were on their front porch searching the night sky for shooting stars."
        julia "It started raining and they were about to go inside, but Joel wanted to watch a little longer."
        julia "They saw a really spectacular shooting star."
        julia "He dropped his binoculars but told her to keep watching. He reached down to grab them and his wheelchair tipped over."
        julia "He fell face-first onto their porch."
        julia "She rolled him over and attempted CPR when she noticed that he was unconscious."
        julia "By the time she received assistance from the nearby nurse, he was already dead."
        him "I see. Is [her_name] going to do an autopsy?"
        julia "Yes, the body was just delivered to the medical wing this morning."
        him "Do I have your official authorization to question Noel and any witnesses?"
        julia "Yes, of course!"
        him "Can I get that in writing?"
        julia "I've already sent it to you."
        nvl clear
        julia_c "I, Julia Nguyen, hereby officially authorize [his_name] to question Noel and any witnesses about the incidents surrounding Joel's death."
        him "Looks good."
        him "Can I collect evidence?"
        julia "I doubt you'll find any more, but that is permissible."
        julia "We took photos of the body before we moved it, and we took Joel's belongings for further investigation."
        julia "I'll share the photos with you."
        julia "Joel's things are with his body in the hospital."
        julia "Oh, and Noel has a lot of society anxiety and asked not to be questioned in-person."
        him "Hmm. Okay."
        him "What do you think happened?"
        julia "I'm not sure. That's why I'm asking you to do this."
        him "I'll get started right away."
        jump investigation_start

    label investigation_start:
        "I put my rain gear back on and prepared to set out."
        "I opened the image of the crime scene."
        #TODO: a CG here would be great, but not required."
        "There was a photo of Joel's body, and a photo of the porch area where it took place."
        "Joel's face in the photo looked super pale. He was on the floor on his back and his mouth and eyes were open."
        "He had an open gash running horizontally across his forehead, with bruising all around it."
        "In the photo of Joel's yurt, I could see that it had a wooden wraparound porch. The porch was raised maybe two inches from the ground and didn't have a railing."
        "Four rain barrels stood on the side. One was open and catching the rain that poured from the roof of the yurt."
        "Where should I go first in my investigation?"
        menu:
            "Visit where Joel died.":
                label joel_house:
                    $ visited_joel_house = True
                    scene cabins with fade
                    "I made the long walk to the miner's camp. It was rainy, and the path up the mountain was slick."
                    "Over the years, this main path to the mining camps had been fortified with a primitive cement made from mining by-products."
                    "As I walked I thought about Joel. How long had he been disabled? It would be difficult to live in a wheelchair in the mountains."
                    "Since the camps moved around the mountain when the mine moved, the camp itself didn't always have cement paths."
                    "Even in the drier months, the incline going up the mountain was so steep that I'm not sure Joel could leave the camp on his own."
                    "It might even be too steep for someone to help him down in a wheelchair."
                    "This camp was fairly new, and I had to follow the smoke from the chimneys to find its exact location."
                    "The camp itself was in a flat area of the mountain."
                    "I asked where I could find Noel, and an old woman pointed me in the right direction."
                    #knock sound?
                    scene yurt_interior with fade
                    him "Hi, Noel? Hello? Are you here?"
                    thuc "Hi [his_name]! Noel is taking a break in the baths in town. Me and Van are watching her kids while she's away."
                    him "I'm here to examine where Joel died."
                    thuc "Okay, it was just back here."
                    him "Was Van here when Joel died?"
                    thuc "No, but the kids were. They didn't see what happened though."
                    thuc "They don't understand where he is. They think he went back to Earth."
                    him "He might as well be there, for all they know."
                    thuc "Well, they're actually going back to Earth on the shuttle, so we're trying to explain that he's dead."
                    him "Oh, right, that's happening next month! Is Brennan going back?"
                    thuc "Yeah, it's part of his job. About half of the miners are going back too. Every spot is spoken for."
                    # TODO: mention Anya
                    him "Except for Joel's..."
                    thuc "Good point!"
                    him "So what were you doing last night? I'm just trying to rule people out right now."
                    thuc "I am a pretty suspicious person."
                    thuc "I was at home with Julia. She was writing up a 'Where are They Now?' story on the children of the colony while I read through some colony forum posts."
                    him "I haven't checked it in a few days. Is anything going on?"
                    thuc "Not much."
                    him "Do you think you could watch the kids while I ask Van about the family?"
                    thuc "They seem really clingy right now... could you do that later tonight?"
                    him "Okay, okay. Is the wheelchair still here?"
                    thuc "Yeah, it's on the porch."
                    "I went outside to examine the wheelchair."
                    "It was a manually-operated wheelchair and had a well-worn cushion in its seat."
                    "The brakes were engaged, but they weren't preventing the main wheel from spinning."
                    him "Huh."
                    "The brake pad was completely worn out. I took photos of the brake and brake pad with my tablet."
                    "I looked at the rain barrels. I wiggled them to confirm that they were the right weight and sloshiness to contain water."
                    "The open barrel had water in it, with some silt at the bottom. It looked like there were a few rocks down there too."
                    "I didn't have my barrel-opening tools with me, so I didn't open the others."
                    "I went back inside and looked around."
                    "The young children were following me and I told them I was just making sure that everything was where it should be."
                    "Van tried to distract them while I looked under chairs and in the cabinets for anything suspicious."
                label where_next_30:
                    menu:
                        "Where should I look next?"
                        "Around the bed." if not searched_bed:
                            "I felt the pillows and looked under the mattress and didn't see anything unusual. Under the bed were boxes of food and a bunch of dust bunnies."
                            $ searched_bed = True
                            if searched_bed and searched_cupboard and searched_sofa:
                                jump say_goodbye_30
                            else:
                                jump where_next_30
                        "In the storage cupboard." if not searched_cupboard:
                            "One shelf had a few kitchen items, like bowls, a mortar and pestle, and a spice grinder. Another shelf held canned items and an old pipe."
                            "The pipe looked like it hadn't been used for years."
                            $ searched_cupboard = True
                            if searched_bed and searched_cupboard and searched_sofa:
                                jump say_goodbye_30
                            else:
                                jump where_next_30
                        "On the kids' sofa bed." if not searched_sofa:
                            "There were all kinds of things lodged into the crevices of the sofa bed, which looked like it hadn't been packed away for a long time."
                            "I found a clay ring, a few wooden buttons, a doll made out of corn husks and silk, some apple seeds, and a bunch of crumbs."
                            "The kids were pretty excited to see what I unearthed."
                            "I looked at the ring, which was smaller than a bracelet but bigger than a napkin ring, and put it in my pocket."
                            $ searched_sofa = True
                            if searched_bed and searched_cupboard and searched_sofa:
                                jump say_goodbye_30
                            else:
                                jump where_next_30
                label say_goodbye_30:
                    "As I prepared to head out, I noticed a big backpack near the door. It was the kind used for lengthy hiking trips."
                    him "Whose backpack is this?"
                    thuc "Oh, that's Van's. Sometimes he stays overnight with the kids, so he brings his sleeping stuff."
                    him "Seems kind of big just for a sleeping bag."
                    thuc "There's emergency supplies and medicine in there too."
                    him "Huh."
                    "I said goodbye to Thuc and Van and headed back into town."
                    if examined_body:
                        jump olegs_house
                    else:
                        "I still wanted to examine the body."
                        jump examine_body

            "Examine the body and Joel's belongings.":
                label examine_body:
                    $ examined_body = True
                    "I headed over to the medical building."
                    her "Hi [his_name]. I already had lunch, but you can come in and talk to me for a bit while I clean up."
                    him "Actually, I'm here on an official assignment. I'm investigating Joel's death."
                    her "I was just writing up the autopsy."
                    him "What did you find?"
                    her "His blood work was mostly normal."
                    her "It looks like he died from bleeding into his brain."
                    him "Is that consistent with an injury sustained from falling from a wheelchair?"
                    her "Yes..."
                    him "But?"
                    if marriage_strength > 8: #TODO: check if this is a reasonable number
                        $ knows_previous_head_injuries = True
                        her "Most of the time, it takes a while to die from a traumatic brain injury. Usually the person with head trauma goes into a coma for a month or something."
                        her "This seemed really sudden."
                        her "It makes me wonder if he had sustained a brain injury earlier."
                        her "Besides the one that disabled him."
                        him "Huh."
                    else:
                        her "That's all."
                    her "His things are on the other examination table. We can talk more after I finish cleaning up."
                    "I looked at the other examination table. There was his clothing, his tablet, and a ball made from plant fibers." #there could be a menu of what to look at here
                    "His clothing still felt a little damp. He had an RET-issued shirt, but instead of pants, there was a skirt with buttons all the way down. A kilt? Maybe it was easier to put on than pants?"
                    "The ball made of plant fibers was made from a plant that grew near the river. It was a pretty common plant, so we didn't bother growing it in farms."
                    "The fibers weren't all that soft, but with enough teasing, they could make a matted fiber kind of like wool, but not as insulating."
                    "I opened the tablet and started examining the contents."
                    "There was a lot of music and audiobooks on the tablet, as well as some drawings that looked like they were made by a kid."
                    "There were a few photos too, including a few of his kids and of the night sky from a few days ago."
                    "There weren't any photos from the day of his death though."
                    "He messaged Julia occasionally things like 'be there soon' or 'not tonight'. Interesting."
                    "I opened his personal credit account, but I couldn't access it without a code."
                    her "Find anything that explains his death? Like a threatening video or something?"
                    him "No. It does look like he messaged Julia a fair amount."
                    her "Well, there's no way it was him writing those messages. Since the mining accident, he hasn't been able to read or write."
                    her "Noel felt lucky that he could still talk though."
                    her "It makes me wonder who was using the tablet."
                    him "It could have been Noel."
                    her "Yeah. Or Van, he's always helping out over there."
                    him "Would Van do something like that?"
                    her "Maybe if he forgot his own tablet? I'm not sure."
                    him "Do you know if I can access his credit account? I'm just curious if he had a balance."
                    her "Hmmm. I think you'd have to have the code. Maybe Oleg would know?"
                    him "I'll stop by his place before meeting you at home."
                    her "Just let me know if I can help! I love this kind of stuff."
                    if visited_joel_house:
                        jump olegs_house
                    else:
                        "I still wanted to examined the scene of the crime."
                        jump joel_house

        label olegs_house:
            "I walked to Sara and Ilian's house to see if Oleg was there."
            "No one answered the door."
            "I walked over to the storehouse."
            him "I have a computery question for Oleg--is he around?"
            ilian "No idea. I'm not responsibile for where he is or isn't."
            him "Sheesh, did I hit a nerve?"
            ilian "Yeah, Sara's always asking me where Oleg is like I'm some kind of walking Oleg-GPS."
            ilian "If she cares so much, why doesn't she follow him around?"
            ilian "I'm the one stuck here all day."
            him "I have a question for you then."
            "I pull out the ring I found at Noel's house and show it to Ilian."
            him "Any idea what this is? It looks like it came from the 3D printer, and I know that you've been helping to monitor that."
            ilian "Hmm. I have seen this before, come to think of it. Did you get it from Oleg?"
            him "No, from Noel's house."
            ilian "What do you think it is?"
            him "Well, it's too small to be a bracelet, unless it's a bracelet meant for a baby maybe."
            ilian "The one I saw looked just like that. I bet we can see who created the original object in the 3D printer history."
            ilian "Let's look. I think I can access the 3D printer history from here."
            "Ilian connects the 3D printer in the fabrication center to his tablet and brings up the printer history. We have to search for a while to find it."
            ilian "Here it is! It looks like Julia printed five copies about two years ago. It looks like she originally designed it too."
            him "But... why?"
            ilian "Maybe it has something to do with her newspaper business."
            ilian "Or maybe she meant for them to be adult-sized bracelets but messed up on the scaling. Who knows."
            him "Hey earlier it seemed like you felt frustrated by your job here."
            him "If you're feeling burned out, maybe you could get someone to help you so you can have some time off."
            ilian "No. No, no, no. I've already been over this so many times."
            ilian "I can't trust anyone else with my job. Without me, the colony would be in utter chaos."
            him "The colony definitely depends on you doing your job."
            him "I'll just send Oleg a message with my question."
            ilian "While you're asking him that, ask him if he's ever coming back, or if he's just going to stay with his mother the whole rainy season."
            him "Why don't you just ask him yourself?"
            ilian "He's not talking to me right now."
            ilian "Don't just stand there staring at me!"
            ilian "Ask him!"
            him "Uh, okay."
            nvl clear
            him_c "Hey Oleg, do you know if it's possible to open someone's credit program without their passcode?"
            oleg_c "nope, not without wiping everything."
            him_c "Is credit data stored in the library server then? Or would wiping someone's tablet erase all their credits?"
            oleg_c "dunno never tried ghgh {font=fonts/OpenSansEmoji.otf}¯\_(⌣̯̀⌣́)_/¯{/font}" #this is supposed to simulate not know what acronyms or emoji the teenagers are using right now
            oleg_c "now i'm curious tho"
            him_c "It must be stored centrally, because even after Helen lost her tablet, I don't remember her losing her credits."
            him_c "Ilian is asking me to ask you if you're going to stay with your mom the whole rainy season."
            oleg_c "it's laik"
            oleg_c "i'm never comin back ^$^"
            oleg_c "and mom is goin back to earth --> 0"
            oleg_c "tttlt" #touch talaam the last time
            him_c "Are you for real?"
            oleg_c "just tell him that"
            oleg_c "and tell me what he says"
            menu:
                "Tell Ilian what Oleg said.":
                    him "Oleg says he's never coming back and that Sara's going on the shuttle back to Earth."
                "Tell Ilian that Oleg isn't answering your questions.":
                    him "Oleg isn't telling me anything."
                    ilian "Oh yeah? Then what's all that you're typing?"
                    ilian "Give me that."
                    "Ilian took my tablet and read what Oleg had written."
            ilian "WHAT there's no WAY that's possible. Every seat on that shuttle is spoken for."
            him "Since Joel died I think there is an empty seat..."
            ilian "There's no way Sara was next in the waiting list."
            ilian "She'd have had to get on the waitlist like... FIFTEEN YEARS ago."
            ilian "UGHHHH I HATE HER SO MUCH THAT WITCH!"
            him_c "He's freaking out! What the heck?"
            oleg_c "ghgh i knew it"
            "I went home and made cabbage and potato soup for everyone."
            him "Hey [kid_name], do you know where Oleg is staying right now?"
            kid "Yeah I think he's with his mom. There's an outpost halfway up the mountain where he's hanging out." #maybe she only tells you based on relationship variables
            him "That old cabin where we used to leave deliveries in?"
            kid "That's the one."
            him "I need to go talk to Sara and Oleg for my investigation."
            kid "Are you investigating the murder?"
            him "No one said it was a murder!"
            her "So you're saying it wasn't a murder?"
            menu:
                "Do I think Joel died on accident?"
                "Yes.":
                    him "It looks like the brakes on his wheelchair were worn out and so his chair tipped over."
                    him "Accidents happen."
                "It could have been a murder.":
                    him "It could have been an accident, or it could have been a murder made to look like an accident."
                    him "I'm still gathering all the information."
            kid "Okay, but how is Oleg involved? I don't think he even knew Noel."
            #maybe you can only involve Terra if you have a good relationship
            him "Right now I'm trying to figue out who is on the waiting list to go back on the shuttle."
            him "Do you know anything about that?"
            kid "No, everyone I know who is going back was always planning on it."
            kid "Wouldn't Brennan have like a list or something?"
            him "Yes, he would."
            nvl clear
            him_c "Hey Brennan, I'm investigating Joel's death for the mayor."
            him_c "Can you tell me who is on the waiting list to go on the shuttle back to Earth?"
            brennan_c "Sure. Sara is first. Then it's Pavel, but he's dead. The rest are all miners you probably don't know. I'll message you the contact info for them."
            him_c "That would be really helpful. Thank you."
            "I got on my rain gear and went to find Sara."
            "Before we had a delivery system, we used to leave deliveries in this small cabin for the miners, so they wouldn't have to walk into town but we wouldn't have to hike all the way to their camp."
            "I'm pretty sure some stuff got misplaced or stolen. When the miners got more credits they started paying for delivery to the camp."
            "The empty cabin was still used sometimes as a dropoff for equipment or a teen hangout."
            "It had been a while since I went there, so it was hard to find in the rain, but the smoke coming from the chimney clued me in."
            "Sara answered the door when I knocked."
            sara "Yes? Can I help you?"
            him "Hi Sara. Is it okay if I come in?"
            him "I brought soup."
            #sara only lets you in if you have a good relationship w the colony
            sara "Sure. What's up?"
            him "It might take a while... why don't you guys eat while I ask a few questions?"
            sara "Okay..."
            "Sara and Oleg started eating the soup I brought for them."
            him "I'm just doing a little research on who is on the waitlist for the shuttle going back to Earth."
            him "You know, since Joel died, there's an empty spot."
            him "Brennan told me that you're first on the list. Is that right?"
            #she only opens up if your colony value is high enough?
            sara "Oh, is that what this is about. Ha."
            sara "Yes, I am first on the list."
            sara "Back when the miners first arrived, Ilian and I had a big fight over who should get up in the night with Oleg."
            sara "He said that I should take care of it all, because I could take a nap in the afternoon if I needed to."
            oleg "Was I a difficult baby?"
            sara "You were probably normal, but it was still hard for us."
            sara "I got really mad about it. We kept fighting over everything that month."
            sara "I asked Brennan to put me on the list to go back on the shuttle if something opened up."
            sara "Whenever Ilian and I started fighting, I was comforted by the idea going back to Earth."
            oleg "Are you really going to go back?"
            sara "Of course not! I wouldn't leave you here!"
            oleg "I'm grown up now. You can go back if you want to."
            sara "I don't want to go back to Earth."
            sara "I don't even know if any of my family back on Earth would be alive by the time I got back."
            sara "My life is here now. But for a while I just needed to believe I could go back if I wanted to."
            him "I can understand that. You wanted to have a backup plan just in case."
            him "When I was talking to Ilian earlier, he seemed really anxious and angry."
            sara "Yeah, I don't want to be around him when he gets like that."
            sara "Usually it's because he expected me to notice something that he thinks is obvious."
            oleg "Yeah, like when the outhouse got really stinky because you kept forgetting to leave the door open."
            sara "I don't like sitting on a wet toilet!"
            sara "Anyway, I'm tired of trying to guess what it is this time, so I told him he would have to work it out on his own."
            sara "He'll eventually come around."
            # TODO: is Ilian anxious about a secret related to the accident?
            sara "Thanks for the soup."
            him "You're welcome."
            oleg "Yeah, thanks, this is actually good."
            oleg "I thought about what you were saying, about the credit information being stored somewhere."
            oleg "I think it's on the central servers in the library. But I bet it's encrypted and even if Pete knew how to get in he wouldn't help us now."
            him "Hmmm. You might be right."

        "As I was falling asleep in my warm, dry bed, I thought about what I still wanted to investigate."
        "I still wanted to talk to Noel herself, about what happened."
        "I also wanted to ask Van about what Noel and Joel's home life was like."
        "And I wanted to talk to Julia about what those cryptic messages on Joel's tablet meant."
        "I also wanted to go back to the scene of the crime to look in the barrel."
        "And I wanted to ask Pete if it was possible to examine financial records for miners." #if you have a good relationship with pete?

        nvl clear
        him_c "Hi, Noel? I'm investigating Joel's death. Could you tell me what happened when he died?"
        him "She's not answering me."
        "I'll see if Van will talk to me in the meanwhile."
        nvl clear
        him_c "Hi Van, how's it going?"
        van_c "Not bad, I'm just headed out in a few minutes."
        van_c "How are you?"
        him_c "Good. So as you know, I'm investigating Joel's death..."
        him_c "What can you tell me about Joel's home life?"
        van_c "So, as you know, I'm pretty well acquainted with Noel and her family."
        van_c "For a few months while she was trying to quit firegrass I was taking her children to and from the co-op every day and watching them on weekends."
        van_c "Recently I've only been going over there a few times a week, but I'll probably be there all this week."
        him_c "Did you check on Joel during these times?"
        van_c "Oh yeah, sometimes I did food runs for him when Noel was really depressed."
        van_c "He made amazing pancakes."
        van_c "He used to tell me that if I ever decided to lose the use of my legs, I should go back to Earth for that."
        van_c "He was so excited to go back to Earth and buy an exoskeleton."
        if knows_previous_head_injuries:
            him_c "Did you witness him sustaining any head injuries?"
            van_c "Oh yeah, I've seen him fall a few times. It seems like he would fall once a week or so."
            van_c "He was always trying to pick things up off the floor. I even made a grabber thing for him, but the kids were always playing with it and hiding it."
            van_c "He was pretty frustrated with his disability. Sometimes he got tired of asking for help all the time."
            van_c "He could usually tell he was falling and break his fall though."
        else:
            him_c "What do you think happened?"
        van_c "I think when he died, he got so distracted by the shooting star that he didn't think to break his fall with his arm."
        him_c "Makes sense."
        van_c "Is that enough information? I'm actually going over there now, so I should hurry before the kids get into too much trouble."
        him_c "That's fine. Thank you."
        "Now I need to ask Julia about the messages on the tablet..."
        "Maybe this is something I should do in person."
        nvl clear
        him_c "Julia, can I come over and ask you some things related to my investigation?"
        julia_c "Of course! Come right over."
        if not kevin_elected:
            him "I wanted to give you an update."
            him "I examined the wheelchair, and it looks like the breaks were worn and dysfunctional."
            julia "Sounds like an explanation for an accident."
            if marriage_strength > 8: #should match the previous marriage strength check
                him "Possibly. But [her_name] said that it was likely that he had received previous head injuries."
                him "Van also mentioned him falling frequently."
                julia "This is sounding more like neglect?"
            else:
                him "Van says that Joel may have been too distracted by the shooting star to break his fall."
                julia "So it could have been an accident?"
            him "Yes. There are still a few things I want to investigate."
        else:
            julia "So tell me more about this investigation. It's about Joel's death I assume?"
            him "Yes."
            julia "What have you found so far?"
            him "I have some ideas, but I still have a few leads I want to pursue. You can read my final report when I finish it."
            julia "I see."
        him "On Joel's tablet, there were a few messages to you. Do you know anything about that?"
        julia "That must have been Van. Sometimes he forgot his own tablet and used Joel's to tell me if he'd be home for dinner." #she's lying
        him "Okay, that makes sense."
        "Should I ask about the ring?"
        menu:
            "Yes.":
                him "One more thing. I found this ring-like object at Noel's house. Do you know what it is?"
                "It seemed like Julia recognized it."
                julia "Maybe some kind of toy?"
                him "I had Ilian look in the printing history and he said that you printed it."
                julia "Is that right? I've printed a lot of things..."
                julia "Maybe this was an experimental canning lid."
            "No.":
                "I didn't ask her about the ring."
        julia "Do keep me updated about the status of the case."
        if not kevin_elected:
            him "Will do."
        else:
            him "I'll update you at the end of the investigation."

        if (luddites > 10): #check values #does this if have an else?
            "I went back home and made myself some lunch. I ate some broccoli and corn porridge and then radioed Pete."
            pete "{i}What can I help you with?{/i}"
            him "Hey, I'm in kind of a complicated situation."
            him "One of the miners died in what appears to be an accident."
            him "I'm investigating if that's the case and it would be helpful to access their financial records."
            pete "{i}Well normally that kind of information is completely confidential.{/i}"
            pete "{i}RET keeps records of it because they want to see if people are savin' money and whatnot.{/i}"
            pete "{i}I'd sure like to see them so I could figure out where all my credits went.{/i}"
            pete "{i}Normally none of us can access it, but there is a way you can tell how much money is in an account.{/i}"
            pete "{i}Most vendor accounts require the user's permission to withdraw funds.{/i}"
            pete "{i}But Brennan can withdraw funds without the user's permission, at least for the miners.{/i}" #if you want to make this into a puzzle later, you can limit the number of withdrawals. Another possible explanation is making a hold on the money but not charging it.
            pete "{i}Gives him some authority I guess.{/i}"
            pete "{i}If you were Brennan, you could withdraw credits until you can't withdraw no more.{/i}"
            pete "{i}That'll tell you how much is in the account.{/i}"
            pete "{i}Then just pay 'em back the amount you took out and they won't notice unless they dig real deep into the transaction history.{/i}"
            him "Interesting."
            pete "{i}I'm curious. Who was the miner who died?{/i}"
            him "It was a man named Joel, who was married to Noel."
            pete "{i}Oh. I've delt with Noel before.{/i}"
            pete "{i}You can't trust anything she says.{/i}"
            him "What do you mean?"
            if not ban_firegrass:
                pete "{i}She keeps trying to get me to lower the price of firegrass for her.{/i}"
                him "She buys firegrass from you?"
                pete "{i}She insists that she doesn't use it anymore and that it's for a friend.{/i}"
                pete "{i}I give her a discount because she buys in bulk and does more of the processing.{/i}"
                pete "{i}I don't really care who it's for as long as she has the money.{/i}"
                pete "{i}She treats me like her personal therapist.{/i}"
                pete "{i}I feel like I have to listen to her or she might stop buying from me.{/i}"
                him "Who else would she buy firegrass from?"
                pete "{i}[his_name], if you don't know the answer to that question I seriously doubt you're going to figure out what happened to Joel.{/i}"
                him "{i}Come on, give me a hint?{/i}"
                pete "{i}Your daughter might know...{/i}" #In family27, Tera makes deliveries. She doesn't quit even if you ask her to stop.
            else:
                 pete "{i}I can't say exactly what she buys from me but she buys a lot of it, if you catch my drift{/i}"
                 pete "{i}She always has some sob story about why I should give her a better price, but I don't give in!{/i}"
                 pete "{i}Good luck finding out what happened.{/i}"
                 him "About that... do you have any leads?"
                 pete "{i}You seriously don't know? Maybe you should ask [kid_name].{/i}"
            "I said goodbye to Pete and pondered what to do with this information."
            $ talked_to_pete = True
            kid "How's that investigation going?"
            him "Oh, you were being so quiet that I didn't realize you were here. Well, you heard what Pete and I were talking about."
            kid "Yep."
            him "Who else is dealing with firegrass these days?"
            if (is_attached()):
                "[kid_name] sighed and frowned."
                if ban_firegrass:
                    "I don't want to get anyone in trouble. But I can tell you that Noel was involved."
                    him "Involved how?"
                    kid "I don't know exactly how, but she received deliveries that were way larger than any single person would actually consume."
                    him "From Pete?"
                    kid "Yeah, from Pete and some other people."
                    him "Which other people?"
                    kid "..."
                    him "Okay, thanks for your help."
                    $ know_noel_received_firegrass_deliveries = True
                else:
                    kid "You want to know about Noel, right?"
                    kid "Ever since I started my delivery business, Noel has been getting large deliveries of firegrass from everyone."
                    him "Like how large?"
                    kid "Larger than any single person would ever smoke or otherwise consume."
                    him "What did she do with it all?"
                    kid "I don't know! She must have been doing something with it though!"
                    him "And what do you mean by everyone?"
                    kid "Everyone who's in the firegrass business."
                    him "Other than Pete?"
                    kid "Yeah, there are some other people who grow it too."
                    him "Really? Who?"
                    kid "I don't know their names. It's a bunch of miners who don't know what they're doing."
                    him "Is that everyone?"
                    kid "Yeah, everyone currently in the business. The ones I know about, anyway."
                    $ know_noel_received_firegrass_deliveries = True
            else:
                "[kid_name] didn't even look up from her tablet."
                kid "Like I'd tell you."
                him "You're no help."
            "I still wanted to see if I could find out account information relating to the case. How should I approach that problem?"
            menu:
                "Ask Brennan to help you.":
                    "I arranged to meet with Brennan in the community center to ask for his help."
                    brennan "What have you found so far with the investigation?"
                    him "I have a lot of ideas but not very much evidence."
                    him "For various reasons, I want to check how much money some people have in their account."
                    brennan "To see if someone has an unusual amount of money? I can see how that would be useful."
                    brennan "I can withdraw and deposit from accounts--is that why you need my help with this?"
                    him "Yes. You can withdraw money until the account is empty, record the number, and then deposit it back."
                    brennan "Kind of a roundabout way of doing it. Is it the only way?"
                    him "As far as I know."
                    if miners > 10:
                        brennan "I'll help you. But I don't have all day, so let's do this quickly."
                        label account_check:
                            if account_checked_counter > 3:
                                if checked_joel:
                                    brennan "I bet Noel was hiding her money in Joel's account."
                                    brennan "She was still collecting disability pay, based on various factors, including her reduced salary."
                                    him "Huh. So she didn't make this much money working overtime?"
                                    brennan "No, she has only been working in the mines a few days a week since her suicide attempt."
                                    jump back_to_noel
                                brennan "Okay, okay, that's enough."
                                jump back_to_noel

                            menu: #allow players to ask about 3 people
                                "Noel's" if not checked_noel:
                                    brennan "Noel has around 100 credits."
                                    $ checked_noel = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "Joel's" if not checked_joel:
                                    if ban_firegrass:
                                        brennan "Joel has over 10,000 credits."
                                    else:
                                        brennan "Joel has over 5,000 credits."
                                    $ checked_joel = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "Julia's" if not checked_julia:
                                    if ban_firegrass:
                                        brennan "Julia has around 7,000 credits."
                                    else:
                                        brennan "Julia has around 4,000 credits."
                                    $ checked_julia = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "Van's" if not checked_van:
                                    brennan "Van has around 200 credits."
                                    $ checked_van = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "Sara's" if not checked_sara:
                                    brennan "Sara has around 2,000 credits."
                                    $ checked_sara = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "Oleg's" if not checked_oleg:
                                    brennan "Oleg has around 1,000 credits." #decide Oleg's level of involvement
                                    $ checked_oleg = True
                                    $ account_checked_counter + 1
                                    jump account_check
                                "[kid_name]'s" if not checked_terra:
                                    brennan "[kid_name] has about 500 credits."
                                    $ checked_terra = True
                                    $ account_checked_counter + 1
                                    jump account_check

                    else:
                        brennan "I can't do that for you."
                        brennan "If someone finds out I was poking in their accounts, I'll never hear the end of it."
                        brennan "Good luck with the rest of your investigation."
                "Try to use Brennan's account without him knowing.":
                        "I visited Brennan in his office and told him I wanted to know who was on the shift schedule when Joel died so I could rule them out."
                        brennan "Hold on, I can bring it up in just a minute."
                        brennan "Here's the list."
                        brennan "No, don't take a photo of my tablet. I don't want the miners to know that I'm helping you too much."
                        brennan "Oh, it's already time for our evening briefing."
                        brennan "Take a screenshot and sent it to yourself."
                        if miners > 10:
                            "Brennan left the tablet with me while he went to the briefing."
                            "I hurriedly opened the payments program. Whose account should I check first?"
                            label account_check_sneak:
                                if account_checked_counter > 3:
                                    "I saw Brennan coming back and quickly closed the program."
                                    jump back_to_noel
                                menu: #allow players to ask about 3 people
                                    "Noel's" if not checked_noel:
                                        "Noel has around 100 credits."
                                        $ checked_noel = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "Joel's" if not checked_joel:
                                        if ban_firegrass:
                                            "Joel has over 10,000 credits."
                                        else:
                                            "Joel has over 5,000 credits."
                                        $ checked_joel = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "Julia's" if not checked_julia:
                                        if ban_firegrass:
                                            "Julia has around 7,000 credits."
                                        else:
                                            "Julia has around 4,000 credits."
                                        $ checked_julia = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "Van's" if not checked_van:
                                        "Van has around 200 credits."
                                        $ checked_van = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "Sara's" if not checked_sara:
                                        "Sara has around 2,000 credits."
                                        $ checked_sara = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "Oleg's" if not checked_oleg:
                                        "Oleg has around 1,000 credits." #decide Oleg's level of involvement
                                        $checked_oleg = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                                    "[kid_name]'s" if not checked_terra:
                                        "[kid_name] has about 500 credits."
                                        $ checked_terra = True
                                        $ account_checked_counter + 1
                                        jump account_check_sneak
                        else:
                            "Brennan took the tablet with him. I wasn't able to look at anyone's account."
                            jump back_to_noel
                "Explore other options.":
                    jump doctors_privilege

        else: #in this branch, you don't talk to pete or kid, so you don't know that Noel was receiving shipments of firegrass. you have talked to Oleg though, which so far isn't dependent on another variable.
            "I didn't think Pete would want to talk to me, and I didn't really have any way to contact him either."
            label doctors_privilege:
                "Oleg said that he thought Brennan was the only one who could make deposits and withdrawals without the recipient's permission."
                "But maybe [her_name] would also have this right?"
                "I asked [her_name] if she could make deposits and withdrawals automatically."
                nvl clear
                her_c "Yes, I can. I use it to pay people who work in the hospital."
                her_c "I always get verbal permission before charging accounts, but on rare occasions I do use the force-withdrawal feature."
                her_c "Why do you ask?"
                menu:
                    "Tell her about investigating accounts.":
                        him_c "It would be really useful to know how much money people have in their accounts for my investigation..."
                        her_c "I can totally see that."
                        her_c "How does that involve me?"
                        him_c "You can withdraw money from their account in different increments to test how much money is in the account."
                        him_c "Then you can deposit it all right back and no one would know."
                        if marriage_strength > 8:
                            her_c "That's clever. Also highly unethical, but I think in a real investigation you'd have a way to see this kind of thing."
                            her_c "You want to check on Noel and Joel, right? It looks like Noel only has about 100 credits."
                            her_c "Joel on the other hand..."
                            if ban_firegrass:
                                her_c "Joel has over 10,000 credits. Wowza."
                            else:
                                her_c "Joel has over 5,000 credits. Huh."
                            label account_check_her:
                                if account_checked_counter > 4:
                                    her "I think that just about covers everyone."
                                    jump back_to_noel
                                else:
                                    her_c "Did you want to check anyone else's account?"

                                menu:
                                    "Julia's" if not checked_julia:
                                        if ban_firegrass:
                                            her_c "Julia has around 7,000 credits."
                                        else:
                                            her_c "Julia has around 4,000 credits."
                                        $ checked_julia = True
                                        $ account_checked_counter + 1
                                        jump account_check_her
                                    "Van's" if not checked_van:
                                        her_c "Van has around 200 credits."
                                        $ checked_van = True
                                        $ account_checked_counter + 1
                                        jump account_check_her
                                    "Sara's" if not checked_sara:
                                        her_c "Sara has around 2,000 credits."
                                        $ checked_sara = True
                                        $ account_checked_counter + 1
                                        jump account_check_her
                                    "Oleg's" if not checked_oleg:
                                        her_c "Oleg has around 1,000 credits." #decide Oleg's level of involvement
                                        $ checked_oleg = True
                                        $ account_checked_counter + 1
                                        jump account_check_her
                                    "[kid_name]'s" if not checked_terra:
                                        $ checked_terra = True
                                        $ account_checked_counter + 1
                                        her_c "No, let's not check [kid_name]'s account. She deserves some privacy."
                                        jump account_check_her
                                    "I'm done.":
                                        $ account_checked_counter + 4
                                        jump account_check_her

                        else:
                            her_c "That's clever. Also highly unethical..."
                            him_c "It's for a good cause!"
                            her_c "No, sorry. It's too risky."
                            him_c "But if you don't help me, we might never figure out what happened to Joel."
                            her_c "And if I do help you, I could lose the trust of my patients."
                            him_c "I guess I'll have to find some other way to investigate how many credits my suspects have."
                            "When [her_name] was asleep, I tried getting into her tablet, but she had changed the passcode."
                            jump back_to_noel
                    "Keep it a secret.":
                        "After [her_name] went to bed, I got out her tablet and typed in the passcode."
                        "I found the accounts program she used for work and opened it up."
                        "Whose account did I want to check?"
                        label account_check_sneak2:
                            if account_checked_counter > 3:
                                "I thought I heard [her_name] stirring and I quickly put her tablet away."
                                jump back_to_noel
                            menu: #allow players to ask about 3 people
                                "Noel's" if not checked_noel:
                                    "Noel has around 100 credits."
                                    $ checked_noel = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "Joel's" if not checked_joel:
                                    if ban_firegrass:
                                        "Joel has over 10,000 credits."
                                    else:
                                        "Joel has over 5,000 credits."
                                    $ checked_joel = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "Julia's" if not checked_julia:
                                    if ban_firegrass:
                                        "Julia has around 7,000 credits."
                                    else:
                                        "Julia has around 4,000 credits."
                                    $ checked_julia = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "Van's" if not checked_van:
                                    "Van has around 200 credits."
                                    $ checked_van = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "Sara's" if not checked_sara:
                                    "Sara has around 2,000 credits."
                                    $ checked_sara = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "Oleg's" if not checked_oleg:
                                    "Oleg has around 1,000 credits." #decide Oleg's level of involvement
                                    $checked_oleg = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2
                                "[kid_name]'s" if not checked_terra:
                                    "[kid_name] has about 500 credits."
                                    $ checked_terra = True
                                    $ account_checked_counter + 1
                                    jump account_check_sneak2

        label back_to_noel:
            "I decided to go back to Noel's place. This time, I brought my barrel-opening tools."
            "When I got there, Noel was there, along with her two young sons." #about ages 4 and 6
            "I asked her if I could talk to her about Joel's death, but she didn't want to talk about it, especially not with her children needing her."
            "How should I approach the situation?"
            menu:
                "Finish searching the premises.":
                    $ know_noel_had_firegrass = True #this variable name isn't great... you know she received deliveries if you talk to Pete and kid is attached; this is for when you find it at her house
                    "I told her I had been authorized to search her house and that I wanted to look inside her barrels."
                    "She strongly protested, saying that she would lose water, but I reassured her that the rainy season would last another two weeks."
                    "She offered to open the plugs on the sides of them, so I could see that it was just water, but that made me all the more suspicious."
                    "Two of the barrels apeared to be normal, but the third actually had another barrel inside of it."
                    "The inner barrel was full of firegrass."
                    "Noel told me that she didn't smoke it anymore but was just holding it for a friend."
                    "I asked her which friend, but she refused to say."
                    if ban_firegrass:
                        "I told her I would have to report her for possessing firegrass."
                        "She asked me to leave, so I did."
                    jump noel_no_confession
                "Offer to help entertain her children.":
                    "I could tell that she was exhausted. Her kids looked wired."
                    "I offered to take her kids down to the storehouse to see if I could get them some dried fruit."
                    "She started crying and nodded. Her sons refused to go with me intially, but relented after I promised to buy them something."
                    "On the way there, they ran ahead and hid in bushes so they could ambush me as I passed by."
                    "I pretended to be surprised and chased them there."
                    "One of the colonists was selling hot cornbread at the storehouse and I bought some for the boys and some to take back to Noel."
                    "When we got back, Noel was asleep. I read a few stories to her children on my tablet and stayed until they fell asleep."
                    "The next day, Noel sent me an e-mail." #e-mail display for following?
                    "Dear [his_name]. Thank you for taking Jam and Neal to get cornbread yesterday."
                    "Joel's death has been difficult for me to come to terms with."
                    "I know it's difficult for my kids too."
                    "I think I'm ready to talk about what happened. Can I meet you in the community center?"
                    jump noel_confession
                "Come back later.":
                    "I told Noel I would come back later."
                    "She said that she didn't want to talk about it."
                    "I asked if I could come by next time Van was watching her kids."
                    "She said no."
                    "Did I respect her wishes?"
                    menu:
                        "Yes.":
                            "I didn't return to her house."
                            jump noel_no_confession
                        "No.":
                            "I came back to the house when I thought she would be gone."
                            "I opened the water barrels. They were all full of water."
                            jump noel_no_confession

        #TODO: if ban_firegrass
        label noel_confession:
            scene community_center
            "I met Noel in the community center. She thanked me for helping her."
            "She explained that she knew that Joel's wheelchair brakes were wearing out, but that he wanted to fix them himself."
            "Tears streamed down her face as she told me that she kept meaning to fix them when he was asleep, but she never had the energy."
            him "I understand that you felt like you could have prevented his death."
            "Do I have any more questions?"
            menu:
                "Yes":
                    menu:
                        "Why did Joel have so much money in his account?" if checked_joel:
                            him "I found out that Joel has quite a bit of money in his account. Why is that?"
                            "Noel explained that she was simply saving money there in case of an emergency."
                        "What is this clay ring for?": #for portioning bundles of firegrass
                            "Noel stared at it for a few minutes."
                            "She said it must be a children's toy."
                        "Van told me that Joel had previous head injuries. Why is that?" if knows_previous_head_injuries:
                            "Noel explained that Joel often vehemently refused help when it was necessary."
                            "Because of this, he often fell out of his wheelchair and hit his head."
                            "She said that she would have Van check for signs of concussion, and while he had one or two bad ones, he usually got better."
                "No":
                    $pass
            "Before she left, I gave her a half-hug. I didn't completely understand her but I still could see that she was suffering."
            "Afterwards, I met [her_name] in the community center for lunch."
            jump who_suspect

        label noel_no_confession:
            "I tried messaging Noel a few more times, but didn't get any answers."
            "The next day, I met [her_name] in the community center for lunch."
            jump who_suspect

        label who_suspect:
            him "I think I'm done with my investigation."
            her "Okay. What have you found out so far?"
            him "Joel died after falling from his wheelchair."
            him "The broken brakes I found on his wheelchair and the kind of head injury he sustained support the idea that he fell from the chair."
            him "Of course, if someone had pushed him, they would want to make it look like he fell."
            if know_noel_received_firegrass_deliveries:
                him "[kid_name] told me that Noel received unusually large shipments of firegrass."
            if checked_joel:
                him "I knew that Joel had an unusual amount of credits in his account. " #others?
            if knows_previous_head_injuries:
                him "Joel had had previous head injuries, which could explain why he died so quickly after his fall."
            her "Do you think it was an accident or was there foul play?"

            menu:
                "It was a tragic accident following neglect.":
                    him "Van and Noel definitely should have made fixing Joel's brakes a priority."
                    him "Life got in the way, and they procrastinated something that was more important than they thought it was."
                    her "That's it? All that research to find that it was just some accident?"
                    him "That's right. Sometimes the truth is more boring than fiction."
                    if kevin_elected:
                        him "I'm ready to tell Kevin my findings."
                        her "Have fun."
                        "I set up a meeting with Kevin and met him back in the library."
                        him "I've investigated the situation and I believe that Joel's death was a result of chronic neglect."
                        kevin "Please elucidate."
                        him "He fell from the wheelchair because the brakes were broken, and he died from the resulting head injury."
                        kevin "He died from just one head injury?"
                        if knows_previous_head_injuries:
                            him "No, he had fallen before with similar injuries, but they weren't as serious."
                            kevin "I see."
                        else:
                            him "I guess so!"
                            kevin "That's highly unusual. It usually takes several weeks or a month to die of a single head injury, if they are fatal, which is uncommon."
                            him "This must have been one of those uncommon occurances."
                            kevin "I'm still skeptical."
                        kevin "Who would you consider responsible for the neglect of Joel's health?"
                        him "Well, Noel, of course. And Van."
                        kevin "Very well. I will have you testify at their trail next week."
                        "Thuc was appointed to prepare a defense for Noel and Van."
                        "We didn't talk much that week. The day of the trail came, and I presented my case to a jury of twelve people, including Zaina and some other colonists."
                        "I showed the photos of the broken brake and explained how their dysfunction was caused by normal wear and tear."
                        "I had [her_name] testify that Joel's head injury was consistent with his fall."
                        if knows_previous_head_injuries:
                            "She also mentioned that he had sustained similar injuries before this one, which made his final injury fatal."
                        "Thuc talked about how we all forget things from time to time even if we don't want to."
                        "He said it could have been any one of us that forgot to do something that ended up killing someone."
                        "Thuc and I left the room while the jury convened."
                        him "Well, I think we both did our jobs."
                        thuc "I hope we can put this incident behind us soon."
                        "After thirty minutes the jury was still going. Sara told us to go home and come back the next morning."
                        "The next morning, we awaited the verdict."
                        if knows_previous_head_injuries:
                            sara "The jury found Noel and Van guilty of criminal negligance."
                            sara "Together with the mayor, they decided that Noel and Van should attend therapy with me weekly for six months and perform 200 hours of community service, including researching a better wheelchair break system to prevent similar accidents in the future."
                            sara "They also agreed that Thuc could count up to 50 hours of babysitting as community service."
                            thuc "Come on. He makes so little that his whole job should be considered community service."
                            sara "That's what the jury decided. Would you like to make a formal appeal?"
                            thuc "Nah, I guess it could be worse."
                            sara "We'll consider the case closed then."
                            return
                        else:
                            sara "The jury found Noel and Van guilty of negligance, but not to a criminal degree."
                            sara "Together with the mayor, they decided that Noel and Van should attend three months of weekly therapy with me and perform 20 hours of community service, focused on improving wheelchair brakes to prevent future accidents."
                            thuc "Sounds fair."
                            him "A man died and the punishment is therapy and a little service?"
                            sara "Do you have more evidence to submit? It sounded like a one-time mistake that anyone could make."
                            him "No, no more evidence to submit."
                            sara "We'll consider the case closed then."
                            return

                    else:
                        him "I'm ready to tell Julia my findings."
                        her "Enjoy."
                        "I told Julia I was ready to report my findings and she asked me to come over right away."
                        him "I've investigated Joel's death and I believe it was the result of chronic neglect."
                        julia "That's so tragic. What happened, exactly?"
                        him "Well, as I told you earlier, the brakes on his wheelchair weren't working."
                        him "When he reached down to pick up his binoculors, he fell. He died from the resulting head injury."
                        if knows_previous_head_injuries:
                            julia "And what about the previous head injuries?"
                            him "Those exacerbated the injury."
                        else:
                            julia "That's so unfortunate."
                        julia "I'll arrange for Noel to be put on trial for neglect, and you can testify of your findings."
                        him "Okay."
                        label accuse_noel_neglect:
                            "Thuc was appointed to prepare a defense for Noel."
                            "The day of the trail came, and I presented my case to a jury of twelve people, including Zaina and some other colonists."
                            if accuse_noel_of_murder:
                                "I showed how easy it was to replace the brake pads, and that failing to do this was not just neglect, but probably stemming from a desire to kill Joel."
                            else:
                                "I showed the photos of the broken brake and explained how their dysfunction was caused by normal wear and tear."
                            "I had [her_name] testify that Joel's head injury was consistent with his fall."
                            if knows_previous_head_injuries:
                                "She also mentioned that he had sustained similar injuries before this one, which made his final injury fatal."
                            "Thuc talked about how we all forget things from time to time even if we don't want to."
                            "He said it could have been any one of us that forgot to do something that ended up killing someone."
                            "Thuc and I left the room while the jury convened."
                            him "Well, I think we both did our jobs."
                            thuc "I hope we can put this incident behind us soon."
                            "After thirty minutes the jury was still going. Sara told us to go home and come back the next morning."
                            "The next morning, we awaited the verdict."
                            if knows_previous_head_injuries:
                                sara "The jury found Noel guilty of criminal negligance."
                                sara "Together with the mayor, they decided that Noel should attend therapy with me weekly for six months and perform 200 hours of community service, including researching a better wheelchair break system to prevent similar accidents in the future."
                                thuc "Sounds fair."
                                sara "We'll consider the case closed then."
                                return
                            else:
                                sara "The jury found Noel guilty of negligance, but not to a criminal degree."
                                sara "Together with the mayor, they decided that Noel should attend three months of weekly therapy with me and perform 20 hours of community service, focused on improving wheelchair brakes to prevent future accidents."
                                thuc "Sounds fair."
                                him "A man died and the punishment is therapy and a little service?"
                                sara "Do you have more evidence to submit? It sounded like a one-time mistake that anyone could make."
                                him "No, no more evidence to submit."
                                sara "We'll consider the case closed then."
                                return

                "It was a murder made to look like an accident.":
                    him "I suspect foul play. Someone deliberately set this up to kill Joel."
                    her "Who do you think it was?"
                    menu:
                        "Sara.":
                            him "Sara seems the most suspicious."
                            him "Sara said she didn't want to go back on the shuttle anymore, but I think she was lying."
                            him "I think she wanted to go back to Earth and take Oleg with her."
                            him "Which means that she'll probably kill again to make a spot for Oleg."
                            her "Would that really work?"
                            him "I don't know! That's just what makes the most sense to me."
                            her "Is Oleg even on the waitlist?"
                            him "Well, no..."
                            her "And how did Sara kill Joel?"
                            him "She could have sabotaged the brakes on his wheelchair in the middle of the night."
                            her "I don't think she even knows where they live."
                            him "Okay. You have a point. I don't think it was Sara."
                            her "Then who was it?"
                            menu:
                                "Julia and Van":
                                    jump julia_and_van
                                "Noel":
                                    jump noel
                        "Julia and Van.":
                            label julia_and_van:
                                him "Julia and Van had business connections to Noel."
                                him "I think she was processing fireweed from Pete and reselling it to them."
                                him "She wanted to stop, but Julia didn't want her to, and got Van to teach her a lesson."
                                her "By killing her husband? That doesn't seem like Julia."
                                her "And if that's true, what is she doing with it all that fireweed?"
                                him "The most successful murderers are the charismatic and normal-seeming ones."
                                him "I bet she puts it in her tea that she's always selling."
                                her "Hmmm. Maybe we could test that idea."
                                her "And how did Julia and Van kill Joel?"
                                him "It would have been pretty simple for Van to promise to fix Joel's brakes and then conveniently forget."
                                her "It's still a little far-fetched, but I'll concede that it's possible."
                                if kevin_elected:
                                    him "I'm going to tell Kevin my theory."
                                    "I told Kevin my theory, and he agreed to set up a trial charging Julia and Van with conspiring to murder Joel."
                                    jump accuse_julia

                                else:
                                    him "If Julia is involved, how will I report my findings to her?"
                                    her "Don't tell her about your suspicions. Isn't there someone else you could report to?"
                                    him "Hmm. Is Sara still involved in colony business?"
                                    her "She'll know what to do."
                                    nvl clear
                                    him_c "Hi, Sara. I'm wrapping up my investigation with Joel's death and I think Julia might be involved."
                                    him_c "Normally I'd report my findings back to her... but obviously I don't want to do that now."
                                    sara_c "You think Julia had something to do with Joel's death? Wow, I can't wait to hear more."
                                    sara_c "You're right though, it's not appropriate to report to her. I can arrange for a jury at the next town meeting."
                                    sara_c "You can come to report your findings, accuse Julia of whatever, and then we'll have the jury right there."
                                    sara_c "But what are you accusing her of? I need to arrange for the defense as well."
                                    him_c "I'm accusing her of conspiring to murder Joel. And I'm accusing Van of putting that plan into action."
                                    sara_c "Got it. See you next week."
                                    him_c "Sounds like a plan."

                                    him "Sara says she can make it happen."
                                    him "In the meantime, can you really test if the tea has firegrass in it?"
                                    her "I have tools for measuring the amount of caffeine is in a given substance."
                                    her "But don't you know plants well enough to identify firegrass in a course mixture like tea?"
                                    him "It's not a typical tea blend. It's a syrup."
                                    her "I'll test it."

                                    label accuse_julia:
                                        "The day of the trial came. Zaina was acting as the defense."
                                        "Twelve colonists acted as the jury."
                                        if checked_joel:
                                            "I told the jury that Joel had an unusual amount of credits in his account when he died."
                                            "Zaina asked about how I knew this information. When I couldn't explain, Sara dismissed the evidence."
                                        "I showed the photos of the broken brake and explained how their dysfunction was caused by wear and tear."
                                        "I also showed how easy it was to replace the brake pads, and that failing to do this was not just neglect, but probably stemming from a desire to kill Joel."
                                        "Zaina argued that I couldn't prove that anyone wanted to kill Joel, and that it could have been just neglect."
                                        "I had [her_name] testify that Joel's head injury was consistent with his fall."
                                        if knows_previous_head_injuries:
                                            "She also mentioned that he had sustained similar injuries before this one, which made his final injury fatal."
                                        if talked_to_pete:
                                            "I had arranged for Pete to come and testify about how Noel had bought large quantities for firegrass from him."
                                        if know_noel_has_firegrass:
                                            "I testified about how I had found hidden firegrass at Noel's house."
                                        "[her_name] testified to finding elevated caffeine levels in Julia's plum tea syrup, consistent with it containing firegrass."
                                        if not ban_firegrass:
                                            "Zaina emphasized that buying and using firegrass was perfectly legal."
                                        else:
                                            "I emphasized that dealing in firegrass without knowledge from a doctor was against our colony's law."
                                        "I told the jury that the most logical conclusion was that Noel had wanted to stop buying firegrass for Julia, but in retaliation, Julia had Van murder Joel to teach Noel a lesson."
                                        "Zaina said that while Julia and Noel may have been business partners, that the unfortunate loss of Joel was unconnected."
                                        sara "Thank you both for your arguments. Please go home while the jury deliberates, and I'll tell you their verdict in the morning."
                                        "I had trouble sleeping, and eagerly awaited the verdict."
                                        "The next morning I went to the community center, where Zaina joined me."
                                        sara "The jury decided that Julia and Van were not guilty of murder, but that Van was guilty of neglect."
                                        if ban_firegrass:
                                            sara "They also found Julia guilty of selling firegrass-derived products without the oversight of a physician and without notifying her buyers."
                                            if talked_to_pete or know_noel_has_firegrass:
                                                sara "They found Noel guilty of posession of firegrass without a license."
                                        else:
                                            sara "They also found Julia guilty of misrepresenting her plum tea syrup."
                                        sara "Everyone will have to attend weekly therapy sessions with me for a month and do some community service hours."
                                        him "But it's clear that Julia was somehow involved with Noel's buying all that firegrass."
                                        zaina "And you also have no evidence of that!"
                                        sara "Zaina is right. You have evidence for a lot of things, but no real connection between Julia and Noel."
                                        him "But Van is over there all the time!"
                                        sara "I'm sorry, but that's not evidence! The case is closed."
                                        #the most material connection is the plastic measuring ring--this should at least be mentioned in the trial
                                        return


                        "Noel.":
                            label noel:
                                him "I don't know if she considered it euthanasia or if she had another motive, but Noel seems the most likely suspect."
                                him "She knew firsthand how miserable he was. She also suffers from depression."
                                him "Maybe she got tired of taking care of him, or his complaining."
                                her "If she was so tired of him, why wouldn't she just divorce him?"
                                him "He was dependent on her, so maybe she was afraid that if she divorced him, no one else would take care of him."
                                him "It would also explain why she's so sad but doesn't want to talk about it."
                                her "It could also be the case that she was simply neglectful and blames herself for his death."
                                him "Well if he died because of her neglect, isn't that a form of murder?"
                                her "That will be up to the jury."
                                him "I'm ready to give my final report."
                                if kevin_elected:
                                    "I arranged to meet with Kevin in the library."
                                    him "The brakes on Joel's wheelchair were dysfunctional, which directly led to his head injury."
                                    him "I believe Noel purposefully neglected Joel in order to hasten his demise."
                                    kevin "What led you to believe that the neglect was intended?"
                                    him "Fixing the brakes is a simple job that is obviously urgent for someone who spends much of his time in a wheelchair."
                                    him "Why else would someone procrastinate such a simple task?"
                                    kevin "Your argument has logic. Let us see what the jury has to say at the trial."
                                    $ accuse_noel_of_murder = True
                                    jump accuse_noel_neglect

                                else:
                                    "I told Julia I was ready to report and she asked me to come over right away."
                                    him "As you know, the dysfunctional brakes on Joel's wheelchair led to his head injury."
                                    him "I believe that Noel purposefully didn't fix the brakes to make a fatal accident more likely."
                                    julia "What would Noel do something like that?"
                                    him "It's so easy to fix the brakes on a wheelchair. What other reason could there be?"
                                    julia "Sometimes, when you're depressed and you have small children, even simple things are very difficult."
                                    him "Her procrastination still killed Joel. Whether she realized it or not, some part of her wanted him gone."
                                    julia "I completely disagree. I asked you to find evidence, not become an armchair psychologist."
                                    julia "Do you have anything concrete that shows that Noel disliked or resented Joel?"
                                    him "It's more a feeling based on her reticience."
                                    julia "I'm willing to put Noel on trail for neglect, but I don't think she wanted to kill Joel."
                                    him "Very well."
                                    julia "Please present your findings to the jury next week."
                                    jump accuse_noel_neglect



# Noel was buying lots of firegrass from Pete at a low cost and selling it to Julia, with Van transporting it at first unknowingly through informal "deliveries" and then knowingly when he got curious enough. Noel was and is making a good amount of money off of this, buying out Pete the first chance she could.
# Oleg started growing firegrass around three years ago (community 24), and his business started booming around two years ago (Community 26).
# A year ago some miners discovered his field and basically stole it from him, but they didn't know how to take care of it and everything died.
# Did Noel start buying out Oleg as well as Pete? She didn't have enough places to store it. But she would play the two off each other.
# What was Julia doing with all that firegrass? She put it in her secret plum tea syrup, which was very popular!

# If firegrass was banned, then demand for Julia's "secret plum tea" would have increased, making her and Noel richer?

# Why did Noel hide her profits in Joel's account? Out of an anxious desire to store money for their life back on Earth, she wanted to keep collecting disability pay as long as possible after her suicide attempt.
# How did Joel die? Van and Noel knew that Joel's wheelchair brakes were breaking down. In fact, they had repaired them many times in the past. This time Joel wanted to do it himself but he kept putting it off.
# Also, Joel wouldn't let Van or Noel repair the wheelchair for him. He had been acting depressed frequently. So maybe he felt like it wasn't worth fixing.


    "The latest shuttles from RET have arrived."
    if ((luddites >= 12) and (miners >=12)):
        "New miners are arriving to replace the ones who are leaving. I'm kind of sad to see some of them go."
    #TODO: fill in the various endings, figure out what the threshold numbers should be
    return
