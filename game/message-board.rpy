# These are messages that appear on the colony message board each year
# The comments above say what will happen that year.

# Community: New colonists arrive
# Family: Terra won't stop crying.
label message1:
    nvl clear
    naomi_c "Congratulations to Sara and Ilian on the birth of their son Oleg!"
    him_c "I don't know whether to congratulate you or commiserate with you..."
    sara_c "Maybe both? {emoji=grin}"
    # Natalia and Julia give great, conflicting baby advice
    natalia_c "I hope you can get some time to yourself once in a while still!"
    julia_c "Nonsense. Babies need their mothers' touch. I hope you are snuggling that baby close as often as possible. And breastfeeding. And swaddling. And cosleeping. And sleeping when the baby sleeps."
    natalia_c "Julia, those are all fine things, but babies also need to learn to make do when their parents have to do other things."
    julia_c "Parents should want what's best for their children. And no one can take the place of a loving mother."
    her_c "It's totally fine to let someone take your place sometimes. I would go crazy if I had to be holding [kid_name] every second!"
    him_c "Yeah, give me that baby, it's my turn to snuggle!"
    sara_c "It's good to see SOME dads enjoy snuggling with their babies."
    naomi_c "Sara..."
    julia_c "Anyway, if you want to help Sara and Ilian, we have a signup to bring them a meal."
    natalia_c "And I made a signup for anyone that would like to volunteer to hold the baby for an hour or so to give them a break."
    naomi_c "Thank you, those are both wonderful ideas."
    sara_c "Thank you everyone!! {emoji=happycry}"

    nvl clear
    return

# Community: Bring whole harvest to storehouse?
# Family: Get work done or play with kid?
label message2:
    nvl clear
    # Reference whole harvest problem with convo about crop trading
    thuc_c "We finally got a good crop of rice!"
    sara_c "That's great; I know you worked really hard on that!"
    julia_c "Yes, it only took us three years, but I think we've figured it out."
    thuc_c "So does anyone want to trade?"
    him_c "Sure, I've got potatoes."
    julia_c "I was hoping for something more... flavorful."
    him_c "Potatoes have plenty of flavor!"
    martín_c "I have artichokes."
    julia_c "That sounds perfect!"
    natalia_c "But we don't need any rice. I was hoping to get some potatoes."
    pete_c "This is starting to sound like a riddle."
    him_c "Okay, no problem, I'll send some potatoes to the Perons, and they'll send artichokes to the Nguyens, and the Nguyens can send rice to me."
    ilian_c "IF ONLY THERE WAS A CENTRAL PLACE TO BRING ALL YOUR FOOD WHERE SOMEONE COULD INVENTORY IT AND KEEP TRACK OF IT AND DISTRIBUTE IT!!!!"
    pete_c "No need to get all bent out of shape, it all worked out."
    nvl clear
    return

# Community: Game Night!
# Family: Camping trip, Terra puts everything into her mouth
label message3:
    # Show outside life, reference decision about whole harvest
    nvl clear
    julia_c "We're still doing auditions for The Sound of Music! No experience necessary!"
    natalia_c "Are rehearsals still going to be every night from 7-10pm?"
    julia_c "Yes."
    natalia_c "Wow, who has time for that?"
    julia_c "Obviously only those with refined tastes. Which, you might be interested to know, includes your son Mateo."
    natalia_c "Oh, did he get a part?"
    julia_c "Well, auditions are ongoing... but he does have a fine singing voice."
    natalia_c "And there's probably not too many other kids his age auditioning."
    julia_c "We shall see, we shall see."

    nvl clear
    if (whole_harvest_to_storehouse):
        ilian_c "Please note the attached schedule for canning duty. We've had a good harvest this year..."
        pete_c "...so it means more work for everyone."
        ilian_c "Yes, and more not starving. This is a good thing, people!"
        sara_c "I don't mind canning duty; it's kind of fun to work with everyone and think about eating these delicious foods."
        julia_c "You can put Gardenia in the rotation next time; she's old enough to help."
        ilian_c "I will do that."
    else:
        zaina_c "I just found out about this message area... is this where we can arrange to trade crops?"
        him_c "Yeah, welcome!"
        zaina_c "That would have been nice to know about when we first got here. Anyway, I have extra zucchini? Like, a lot of extra zucchini."
        him_c "I thought Kevin was bringing all your stuff to the storehouse?"
        zaina_c "He was, but there's nothing there to get in exchange. Ilian said you guys all trade on here."
        ilian_c "Despite the inefficiency, that is the current modus operandi."
        zaina_c "Anyway, I've already done zucchini pickles, stuffed zucchini, zucchini noodles, baked zucchini, fried zucchini, and if I have to eat another zucchini I seriously think they might all perish in a tragic 'accident'. So please tell me someone is willing to trade?!"
        natalia_c "I'll trade you some eggs."
        him_c "I'll trade you potatoes!"
        zaina_c "Yeah! You just saved some zucchini from a premature death by Zaina Rage. Thanks, guys."

    nvl clear
    return

# Community: Community Liaison
# Family: Terra's a picky eater!
label message4:
    nvl clear
    # Foreshadow picky eating by looking for pickles/applesauce
    him_c "Wow, who made that applesauce I picked up at the storehouse?!  That was delicious!"
    helen_c "I did."
    pete_c "She's rockin' that applesauce!! Planting those apple trees was the second smartest thing I ever did."
    him_c "Second smartest?"
    pete_c "The first was marryin' Helen. Now, she don't like me to brag about her, but..."
    naomi_c "Would Helen want you to share what you're about to say?"
    pete_c "...probably not. But, holy hand grenade in a hot air balloon, she is one fine woman!"
    helen_c "...anyway, um, Zaina's zucchini pickles are really good, too."
    him_c "Really? I'll have to try them out."
    zaina_c "Thanks! Always glad to share the love when it comes to zucchini."

    nvl clear
    return

# Community: Set aside food for miners?
# Family: Toilet Training!
label message5:
    nvl clear
    # Liaison business -- ratifying charter, objections must be posted by two weeks, blah blah. Kevin feels it's not precise
    # People encouraging liaison, they don't actually do much yet
    if (is_liaison):
        him_c "Hey, we need to ratify the our charter tomorrow at the meeting in two weeks, so please look it over before then. Now is the time if you have any objections."
    else:
        sara_c "If you haven't had a chance to read our new charter, please look it over!  We're ratifying it in two weeks so if you have any issues, let's work them out before then!"

    kevin_c "This clause at the beginning is imprecise. Is biannually based on Earth time or Talaam time?"
    pete_c "Shouldn't decisions have to be voted on or something? This liaison is going to have a lot of power..."
    naomi_c "Perhaps people with specific objections to the charter could post alternative wording for everyone to choose from?"
    kevin_c "I will post an edited copy with more precise language."
    natalia_c "Thanks for being our liaison, BTW - I wouldn't wish that job on anyone, but I think you'll do just fine."
    if (is_liaison):
        him_c "Thank you! I appreciate all the help and support I've received so far."
    else:
        sara_c "Thank you everyone!!! You're so kind! {emoji=happy}~{emoji=heart}"

    nvl clear
    return

# Community: Game Night continued/consequences
# Family: Terra wants to talk and play when everyone else wants to rest, Ready for another baby?
label message6:
    nvl clear
    # busy harvest time - looking forward to holiday Halloween + Thanksgiving
    # Kevin/Zaina asking about local alien meat
    if (is_liaison):
        him_c "Harvest festival coming up next week!"
    else:
        sara_c "Hope you're all planning on coming to the harvest festival next week!!! {emoji=grin}"
    natalia_c "I just hope we can finish the harvest by then."
    julia_c "Having trouble, are you? I expect to be done tomorrow."
    martín_c "It'll work out. It helped having the school kids home for the week."
    natalia_c "Though we might not have time to do a corn maze like last year."
    him_c "No corn maze?! We gotta do something about that!"
    ilian_c "Shouldn't the food be your highest priority?!"
    him_c "Hopefully we can do both!"
    kevin_c "Is it your colony's tradition to eat crabird every year at the harvest festival?"
    him_c "We have done that a lot... I guess it's becoming a tradition?"
    julia_c "It's not set in stone."
    kevin_c "Is any of the local fauna poisonous or inedible?"
    pete_c "A few animals aren't good for eating, but most are alright. You ought to come hunting with me sometime."
    helen_c "Sometime when it's not harvest time."
    nvl clear
    return

# Community: Comparing compensation
# Family: Back Talking & Disobedience
label message7:
    nvl clear
    # Game night discussion - poker?
    julia_c "I'm starting a bunco group. Everyone will bring a snack to share and the host provides a prize. Send me a message if you want to join!"
    natalia_c "Isn't that the dice game with absolutely zero skill involved?"
    julia_c "The main skill involved is social interaction, so you probably wouldn't excel at it."
    natalia_c "If by 'social interaction' you mean 'passive-aggressive jibes' then, no, I certainly don't excel at that."
    pete_c "I don't know; that was a pretty good passive-aggressive jibe right there."
    julia_c "Perhaps the poker group would be of more interest to you."
    thuc_c "We have room for one more player in Maximal Conquest next game night!"
    helen_c "Just come a little early so we can explain the rules."
    him_c "Like, a few hours early."
    nvl clear
    return

# Community: RET will send what luxuries?
# Family: Play group and first day of school. Baby bro born, else pregnant
label message8:
    nvl clear
    # Natalia asking for harvest help as Martín is sick
    if (year6_have_baby):
        sara_c "[her_name], I know your due date is coming up...are you doing okay?"
        her_c "I'm okay. I wish I wasn't having the baby during harvest time, though!"
        sara_c "At least [kid_name] is starting school soon... I'm so excited for her and Oleg to go to kindergarten!"
    else:
        sara_c "I'm so excited for [kid_name] and Oleg to go to kindergarten!"
    julia_c "Those early years are so precious... just cherish every moment while they're small!"
    natalia_c "Hey, grandma, maybe you could cherish your own grandson this week so Tomás can help us out with the harvest."
    julia_c "Of course. I would never turn down an opportunity to hold that precious baby!"
    sara_c "I've seen you guys in town a lot... is Martín sick again? {emoji=surprised}"
    natalia_c "When is he not?"
    kevin_c "Does he have a chronic illness?"
    martín_c "Skin cancer. We keep thinking we got rid of it, but then it comes back somewhere else."
    naomi_c "Can I come over to help you around the house? I'm afraid these old bones aren't much good for harvesting, but I'm sure there's something I can help you with."
    natalia_c "Thank you, Naomi, I'll let you know."

    nvl clear
    return

# Community: Camping with Pete
# Family: Bossing friends around
label message9:
    nvl clear
    # Congrats on baby/pregnant
    # School talent show!
    julia_c "I just wanted to thank everyone who participated in the school talent show."
    sara_c "Van's jokes were so good! He's quite the comedian!"
    helen_c "I loved Gardenia's paintings. Somehow both soft and arresting."
    if (year6_have_baby):
        thuc_c "[kid_name] didn't want to participate?"
        her_c "Things have been pretty busy with the new baby...we kind of forgot about it."
        him_c "I thought about it, but then I fell asleep."
        thuc_c "Next time, then!"
    else:
        thuc_c "And [kid_name] did great impressions of everyone on the colony!"
        sara_c "It was so cute when she pretended to be [her_name] with a baby inside her belly! {emoji=hearteyes}"
        her_c "Yeah, she's been really obsessed with my pregnancy."
        julia_c "Good, she will be a wonderful helper when the baby is born."
        him_c "I hope so..."

    nvl clear
    return

# Community: Peron's over, who should take care of farm?
# Family: Fighting with brother OR playing games on tablet when she's not supposed to. Baby bro born if not already
label message10:
    nvl clear
    # Location of miners discussed: "why so far" "not far enough!"
    # What kind of mining are they doing, anyway?? Why? What are they mining? How is it profitable?
    # Indium is used in LCDs, solar panels, cryogenics. Finding a lot! Also copper is running out
    if (is_liaison):
        him_c "We've designated an area for the miners to live, so please take a look at the map and note where their camp will be located."
    else:
        sara_c "I just got notice of where the miners will be living. Here's a map!"
    helen_c "Wow... that's pretty far away. It'll take them an hour to walk into town."
    pete_c "I don't know; kinda seems not far enough."
    kevin_c "The location was chosen for its proximity to precious minerals and availability of a clear area suitable for landing on."
    her_c "What are they mining, anyway? It'd have to be something pretty valuable to send shuttles light years away for it..."
    kevin_c "Scandium, terbium, indium, copper, phosphorus..."
    thuc_c "I've heard of some of those words."
    him_c "Phosphorus is an important part of fertilizer."
    kevin_c "The rest are mainly used in electronics, solar panels, and cryogenics."
    her_c "Is Earth completely out of them or something?"
    lily_c "No, but here on Talaam they are much easier to access. While on Earth you might need to sift through garbage heaps to sort and recycle individual parts, here they are just below the surface."
    her_c "Things are going to change a lot when they arrive..."
    ilian_c "Personally, I'm excited. No offense to any of you, but I could stand to see a few new faces around here."
    if (year6_have_baby):
        him_c "What, [bro_name] doesn't count?"
    else:
        him_c "What, our soon-to-be-born baby doesn't count?"
    ilian_c "Sorry, no."

    nvl clear
    return

# Community: Miners and Brennan arrive on shuttle; Martín dies
# Family: Dinner Table Manners
label message11:
    nvl clear
    # sports teams for various ages forming
    # literary magazine being compiled by Isabella - write poetry for it??
    ilian_c "Pickup soccer in front of the community center tonight!"
    helen_c "Oh, good, Travis was asking when you guys were going to play again."
    natalia_c "Isabella's putting together a literary magazine and wanted me to ask you guys for stories, poetry, or illustrations."

    if (year11_poem == ""):
        menu:
            "Should I submit a poem?"
            "Yes.":
                him_c "I'll send you one!"
                $ word_board.set_wordpack(basic_words, family_words, farm_words, baby_words, talaam_words)
                call make_poem
                $ year11_poem = word_board.get_poem_as_string(-1)
                natalia_c "Thanks for your poem; I'll pass it along."
            "No.":
                $ pass
    else:
        him_c "Did you get mine?"
        thuc_c "You really sent one in?? I thought you were joking!"
        him_c "No way! I never joke about poetry!"

    nvl clear
    return

# Community: missing cow
# Family: An unknown miner friend, lice
label message12:
    nvl clear
    # Miners appear on msg board; create new colonists-only board
    # People comment on literary magazine
    if (is_liaison):
        him_c "Okay, this area is now private for colonists-only. You can use the old area if you want to talk to everyone on Talaam."
    else:
        sara_c "Okay, I setup this new area for colonists only. The old area was kind of overrun by miners!"

    julia_c "Nothing against the miners, but they don't need to hear all about our crops and things like that."
    ilian_c "And we don't need to hear about all their safety classes and deadlines."
    zaina_c "Hope you don't mind that Kevin and I are on both. I guess we're closer to being miners, but none of them want any zucchini!"
    natalia_c "That's their loss, then!"

    pete_c "I hope y'all took a moment to read the literary magazine. It's the best alien writing you'll ever lay eyes on."
    if (("jellystar" in year11_poem) or
        ("jellysquid" in year11_poem)):
            helen_c "I loved the jellies in [his_name]'s poem!"
    if (("crabird" in year11_poem) or
        ("wolf slug" in year11_poem) or
        ("turtle snail" in year11_poem)):
            pete_c "You'll never see a poem about crabirds, wolf slugs, or turtle snails in Earth writings!"
    if (("baby" in year11_poem) or
        ("father" in year11_poem) or
        ("mother" in year11_poem)):
            natalia_c "I thought [his_name]'s poem was a great reminder of the importance of families."
    if (("goat" in year11_poem) or
        ("dirt" in year11_poem) or
        ("harvest" in year11_poem) or
        ("dig" in year11_poem) or
        ("seed" in year11_poem)):
            thuc_c "We need more farming poems like [his_name]'s!"
    her_c "I loved the story about the brave doctor!"

    nvl clear
    return

# Community: Save the Cave/Mountaintop!
# Family: Sex education, miscarriage
label message13:
    nvl clear
    brennan_c "Please tell me we've exterminated all the lice..."
    her_c "I think we're in the clear. If anyone finds more, please come to me right away so we can limit their spread."
    him_c "I hope you guys didn't bring bed bugs with you, too."
    brennan_c "If we did, we'll be sure to send them your way first."
    her_c "Anyway, I thought I'd let you all know that we're expecting another baby!"
    sara_c "Really?! That's great! {emoji=grin}{emoji=celebrate}"
    natalia_c "Congratulations!"
    thuc_c "Wow, three kids... you'll be outnumbered."
    him_c "Tell me about it!"
    julia_c "After the first two, it's a lot easier."
    natalia_c "I don't know... my last one was my most difficult baby of all."
    julia_c "Oh, is that why you stopped at five?"
    natalia_c "No, actually we wanted more kids but I had to have a hysterectomy right after Mateo. Thanks for bringing it up."
    julia_c "I...I'm sorry. I didn't mean to bring up such a sensitive topic."
    natalia_c "That's okay, now you have no excuse for being insensitive."

    nvl clear
    return

# Community: Pete leaves - NO MORE PETE/HELEN ON MESSAGE BOARD
# Family: Teacher trouble
label message14:
    nvl clear
    # Wait, a shuttle is leaving?? Is anyone leaving?
    # Nope, it's just for cargo. There are no humans on board, so we don't to worry about excessive g-forces and life support and other petty concerns
    natalia_c "Who's coming to the shuttle launch?"
    sara_c "Wait, a shuttle's leaving?! Who's on it??"
    brennan_c "No one's on the shuttle; it's just a load of metal and minerals going back to Earth."
    kevin_c "We will be controlling it remotely. Onlookers are welcome; however, please stay at least 8 kilometers away for safety reasons."
    him_c "I'm going to bring the kids!"
    pete_c "I'll be there."
    natalia_c "I'm bringing a picnic; bring food if you want to trade!"
    her_c "Kevin, don't forget ear protection for anyone in your crew closer than 5km. Everyone else shouldn't need it."
    kid_c "Stellar! A rocket picnic! -=|⁐⁐⁐⁐⁐⁐>"
    ilian_c "I didn't realize this message area was for kids."
    naomi_c "No reason it shouldn't be, if they have something to add to the conversation. But perhaps they would also like their own area."
    oleg_c "I alredy made one no adults allowed tbfy gh gh  q.\_/.p"
    sara_c "We'll see about that."

    nvl clear
    return

# Community: Naomi dies
# Family: Allowance?
label message15:
    nvl clear
    # jumpropes sold by Gardenia, Julia's daughter
    # meal signup for Naomi
    sara_c "Wow, it's so quiet on here without Pete and Helen! {emoji=surprised}"
    julia_c "Perhaps this will remind people to put down their devices and go talk to people in person!"
    ilian_c "Yes, let's talk ON COMPUTERS about HOW IMPORTANT it is to TALK IN PERSON!"
    sara_c "ORRRR, we could do something positive in real life, like sign up to take meals to Naomi and Pavel."
    thuc_c "Is she sick again?"
    sara_c "Yeah..."
    julia_c "I'll bring something tonight, so don't worry about dinner, Pavel."
    pavel_c "Thank you so much. I know she appreciates all of your kind gestures."

    julia_c "Sorry to change the subject, but Gardenia wanted me to let everyone know that she is selling handmade jumpropes for 10 credits each."
    her_c "I remember playing jumprope as a kid..."
    thuc_c "I remember using jumpropes to tie up my siblings."
    ilian_c "We used them to lower buckets from our tree house."
    julia_c "Yes, it is a very versatile toy! And these are woven from the finest plant fibers of Talaam."

    nvl clear
    return

# Community: Trade with mavericks?
# Family: She must clean her room!!
label message16:
    nvl clear
    # How is Pete doing? I never talk to him anymore.
    # Sara went to talk with them, gives update
    kevin_c "I have not seen Pete since he left... how is he faring?"
    sara_c "I went to see them the other day. They are living in a tent up by the mountains; it's really pretty up there! Travis was so happy to see me and Oleg; he misses his friends."
    pavel_c "Do they have enough to eat?"
    sara_c "They're working really hard doing everything all on their own, but they're not starving or anything."
    if (lily_mad_at_RET):
        her_c "What about Dr. Lily? Isn't she getting kind of old?"
        sara_c "She lives near them. She's still getting around great and staying healthy."
    if not (asked_only_medicine):
        natalia_c "Tomás and Joanna like it out there. They've tunneled a house out of the ground and are doing farming and research."

    ilian_c "It's only a matter of time before they come back. They'll need civilization sooner or later."
    sara_c "People have survived for centuries living without 'civilization'."
    ilian_c "Only if they have no other choice."

    return

# Community: Harvest festival with jellyfish!
# Family: Bro has unexplained crying
label message17:
    nvl clear
    # how busy harvest time is, negotiate when things are harvested to help each other, kids get school off to help
    # Julia offers tea to people that help
    # shouldn't the miners help?? We have our own deadlines
    pavel_c "No school for the next month due to harvest!"
    brennan_c "I still think that's a wonky schedule. What about the miner kids? They don't have a harvest."
    pavel_c "They could still use a break."
    him_c "We could use the miners' help. Maybe we could all work together."
    brennan_c "Sorry, we have our own deadlines."
    julia_c "I'll have my special tea brewed for anyone that comes to help on Wednesday!"
    sara_c "That stuff is so good! What's in it, anyway?"
    julia_c "It's my secret recipe."

    nvl clear
    return

# Community: Miners complain about Pete's cattle
# Family: Terra needs more baths!
label message18:
    nvl clear
    # Someone (Zaina? someone who ate jellies, add to community17 if necessary) is doing a documentary about jellystars and wants footage, art, poetry, etc.
    # Lily has some stuff for her, they are working together
    # You can submit a poem!!!
    lily_c "I am putting together a documentary of jellystar material to send to Earth biologists. If you have footage or data about them, please send it to me."
    zaina_c "I'd like to see that. Those creatures are fascinating!"
    him_c "What about poetry?"
    thuc_c "You have jellystar poetry?!"
    lily_c "...Yes, please send me anything you have."
    if (year18_poem == ""):
        menu:
            "Should I submit a poem?"
            "Yes":
                $ word_board.set_wordpack(basic_words, family_words, separation_words, romance_words, talaam_words)
                call make_poem
                $ year18_poem = word_board.get_poem_as_string(-1)
                lily_c "Thank you for the poem, [his_name]."
                thuc_c "I gotta see the jellystar poem!"
                him_c "I thought you hated my poems."
                thuc_c "I love hating your poems."
                him_c "Sorry, wait until they finish the documentary!"
            "No":
                him_c "I don't actually have any jellystar poetry."
    nvl clear
    return

# Community: Crabirds devastate harvest
# Family: What to do about pornography
label message19:
    nvl clear
    him_c "I have some caulk leftover from roof repair if anyone needs it. Trust me, you don't want to wait until the roof's leaking during a solar flare."
    thuc_c "Sounds like you have personal experience there!"
    him_c "Hey, what's everyone planting this season? Anything new?"
    natalia_c "Mostly feed corn, but also beans, summer squash, sweet corn, popping corn, peppers, and tomatoes."
    thuc_c "The usual: rice, onions, garlic, turnips, cabbage, and plenty of hay and clover for the goats."
    pavel_c "I'm expanding my spice garden this year and adding cinnamon!"
    kevin_c "I plan to grow more varieties of fruit in my orchards."
    him_c "Wow, we're going to eat well this year! I'm still thinking about mine..."
    oleg_c "potatoes plz!"
    kid_c "strawberries plz!"
    him_c "I'll think about it."

    nvl clear
    return

# Community: Lily's research, she dies
# Family: Musical instrument?
label message20:
    nvl clear
    # Lily and Zaina finished documentary, screening at community center
    # Why the jellystars? Why not crabirds or wolfslugs??

    sara_c "I just wanted to congratulate Lily, Miranda, and Zaina on such an amazing documentary! I learned so much about the jellystars!"
    ilian_c "Mostly, that we don't know much about them."
    if (ate_jellyfish):
        him_c "We know they are delicious."
    else:
        thuc_c "We know they are delicious!"

    if (year18_poem != ""):
        sara_c "[his_name], would you mind posting your poem? I wanted to read it again."
        him_c "Sure."
        him_c "[year18_poem]"

        if (("sexy" in year18_poem) or
            ("heart" in year18_poem) or
            ("beautiful" in year18_poem) or
            ("love" in year18_poem) or
            ("kiss" in year18_poem)):
                brennan_c "Is this really about the jellystars?"
        if (("unknown" in year18_poem) or
            ("alien" in year18_poem) or
            ("strange" in year18_poem) or
            ("wonder" in year18_poem)):
                ilian_c "That's surprisingly deep."
        if (("grow" in year18_poem) or
            ("dream" in year18_poem) or
            ("ocean" in year18_poem) or
            ("together" in year18_poem) or
            ("joy" in year18_poem)):
                zaina_c "I think you understand them very well."
        thuc_c "...I don't hate it!"
        him_c "That's too bad; I was looking forward to you making fun of it."
        $ first_word = year18_poem.split()[0]
        thuc_c "Well, I thought it was kind of weird that you started off with the word \"[first_word]\", but that's about all I can say."
    pavel_c "How come nobody wants to make a documentary about crabirds?"
    him_c "Or turtle snails!"
    ilian_c "Because they're ugly pests."

    nvl clear
    return

# Community: Visit ocean. Build relationship with miners or mavericks depending on their values. Discuss firegrass w/miners if relationship is high enough.
# Family: Terra's mean and sarcastic
label message21:
    nvl clear
    # Naomi's gone, but Sara needs parenting advice. How to deal with teenagers?!
    # Natalia and Julia give conflicting good advice
    sara_c "I can't believe I'm old enough to have a teenager!! {emoji=scream}"
    her_c  "I know! I still feel like a teenager sometimes..."
    him_c "Like a teenager, except responsible?"
    sara_c "Ouch... speaking of which, every time I talk to Oleg it turns into an argument! I ask him to take out the trash and he blows up in my face!"
    ilian_c "You could just stop talking to him."
    sara_c "I wish I could ask Naomi...{emoji=cry}"
    natalia_c "He still needs you. Look at it from his perspective - strange chemicals are flooding his brain while he's dealing with new social issues, AND people are telling him what to do all the time."
    julia_c "Lay your expectations out clearly with consequences. You shouldn't have to ask him to do these things; he knows what his chores are. If he fails to do them, he faces the consequences. He'll learn soon enough."
    her_c "I think Naomi would remind you to give him lots of love, but maybe in a different way than when he was little?"
    sara_c "Maybe so... I appreciate the advice, guys.{emoji=worried}"

    nvl clear
    return

# Community: Miners moving to mountain near mavericks!
# Family: Apologize when you falsely accuse Terra? Family activities
label message22:
    nvl clear
    # Miners are moving; I wonder if they left anything behind? let's go scavenge!
    # Don't bother; there's mostly just tire tracks and a flat dirt clearing and some toxic ponds and a bunch of slag
    him_c "Hey, somehow I ended up with these socks from the camping trip, but they don't belong to anyone in our family... If they're yours, let me know!"
    natalia_c "Oh, I think those might be Mateo's."
    him_c "Okay, I'll have [kid_name] bring them to school this week."
    ilian_c "By the way, we have a special on salted fish that I bought from Pete, so stop by soon if you want some."
    pavel_c "Ooh, anyone interested in making fish sauce?"
    julia_c "If there's enough demand, we could make some. But it takes months."
    thuc_c "And it makes everything smell like fish."
    pavel_c "Isn't anyone else interested in fish sauce??"
    natalia_c "Not really."
    him_c "I don't know what I'd use it for."
    thuc_c "Maybe we can make a small batch togther, Pavel."

    nvl clear
    return

# Community: Glass shell collecting--shells are worth more if mining stopped in 22 and...
# Family: Screen time, chatting with friends instead of homework
# 14.8 years
label message23:
    nvl clear
    natalia_c "Remember back when we didn't use money? We just helped each other and everyone got along."
    him_c "Everyone except you and Julia."
    julia_c "Money is a universal human invention. There's nothing wrong with rewarding hard work."
    him_c "It's not exactly like Earth, though -- no 401ks, stock markets, or taxes..."
    kevin_c "Perhaps the next shuttle should include some economic analysts to ensure the financial security of Talaam's future."
    sara_c "Ugh, why all the focus on money? We should just help each other and enjoy what we have. {emoji=sad}"
    ilian_c "Sounds like a quick way to pecuniary failure. You have to know how much you have before you know how much you can spare!"
    natalia_c "There's plenty to go around, as long as we help each other!"
    julia_c "And as long as everyone does their fair share of work."
    kevin_c "Which is precisely the reason currency was invented; as a concrete, exchangeable measurement of work."
    him_c "Too bad you can't eat it."
    nvl clear
    return

# Community: Growing luxury good market, especially if mining stopped in 22. The increased demand for shells led to inflation and Ilian fixes the prices of food. You can choose to write a farming guide, which Oleg makes free, babysit (most lucrative and stressful), or be a farming consultant.
# Family: Lettie dies; friends with creepy older brother
label message24:
    nvl clear
    # Julia links to Talaam Times
    # it's expensive! no advertising revenue?
    # She didn't review the oatmeal soap because it competes with her goat milk soap
    julia_c "I hope I can count on all of you to subscribe to Talaam's first newspaper, the Talaam Times!"
    sara_c "Are we really big enough for a newspaper?!"
    thuc_c "It's really more of a newsletter."
    julia_c "Our first issue has a gardening section, cooking section, local news items, miner's update, weather and solar flare predictions, and product reviews."
    zaina_c "That could be useful... where can I get it?"
    julia_c "It's available by subscription only, for the low price of 20 credits per year. Individual issues cost 5 credits each."
    him_c "This is for a monthly newsletter?!"
    sara_c "Why is it so expensive?!"
    julia_c "There's no advertising revenue (yet!), so I have to charge more."
    natalia_c "But... you're not printing it on actual paper, right? This is a digital newsletter."
    julia_c "Yes, obviously."
    natalia_c "So it costs you the same amount to make no matter how many people subscribe. So shouldn't you make it cheap to get lots of subscribers?"
    julia_c "I think it's a fair price."
    natalia_c "We'll see if anyone agrees with you."
    if (bought_tt):
        scene talaam_times with fade
        $ renpy.pause()
        scene stars
    else:
        menu:
            "Should I buy the first issue?"
            "Buy it (5 credits)":
                $ bought_tt = True
                $ colonists += 1
                $ modify_credits(-5)
                scene talaam_times with fade
                $ renpy.pause()
                scene stars
            "Dont' buy it":
                $ pass
    nvl clear
    return

# Community: Brennan’s jellysquid farm. You can talk to Chaco or Pete about the jellysquid farm, depending on your Miner or Luddite relationship scores.
# Family: Making dinner, talking about education and jobs
label message25:
    nvl clear
    sara_c "After you chop it up, do you just sautee it?"
    thuc_c "I like it in a little goat cream with beans and garlic."
    natalia_c "I think Ilian is selling it dried now. Dried jellystar is really good in soup"
    julia_c "It's especially good with a little of my plum syrup! Ten percent off this week!"
    natalia_c "I think everyone has tried your plum syrup by now..."
    sara_c "Jellystar has a pretty high water content... is there anything left after it's dried out?"
    him_c "Why do we suddenly have so much jellystar? I wasn't sure if it was approved for human consumption."
    if ate_jellyfish:
        him_c "Dr. Lily once told me that they contain a parasite which could decrease reaction speed."
        sara_c "Really? I haven't noticed anything like that."
        him_c "Well, she did say it was only a difference of a few milliseconds."
        him_c "Also, I think they're too cute to eat."
        thuc_c "I do feel a twinge of guilt when I eat them. But if they're already processed I don't think about it as much."
        natalia_c "Yeah, I don't like cutting up the carcasses. It just makes me sad."
    ilian_c "Brennan started farming them for their shells. He doesn't need the meat, so he sold it all to the storehouse. It's really cheap right now, and we're still drying more. You can use it for bait when fishing, too."
    him_c "He's farming the form with the shell?"
    ilian_c "I'm not sure if he got them to reproduce but he had a lot of dead jellystar to offload."
    him_c "I'm surprised because I don't think Brennan has much experience in aquatic animal husbandry."
    brennan_c "I have been trying to farm jellysquid, which resulted in surplus jellystars."
    sara_c "Are the jellysquid even the same species? {emoji=surprised}"
    julia_c "Dr. Lily reported that the jellysquid form is an aggregate of the jellystar one, but she never personally witnessed how it happens."
    julia_c "She wrote about it in a paper on them. You should probably read it if you're trying to raise them."
    brennan_c "Thanks, I'll look it up. I've made a few observations of my own."
    julia_c "You should publish them!"
    brennan_c "My information is proprietary."
    julia_c "How much?"
    brennan_c "Message me."
    nvl clear
    return

# Community: You can choose to tell colonists that Pete’s beef contains cancer cells.
# There’s also discussion about how to help a heavy user of firegrass, Carol. Depending on certain values, you can convince Brennan to prevent miners from working too long of hours or grow more tea or nothing. No matter what you choose, Oleg makes an educational app (he or one of his friends has a side-business of their own firegrass dealings).
# ALSO in this long event, a shuttle arrives with material to start an artificial meat plant. You can choose to keep buying meat from Pete or not.
# Family: Talking politics? Terra thinks you're a terrible leader. Either you're too strict, treating one group badly (miners? Jellies?), Or you are clueless and you don't even know what people are doing behind your back.
label message26:
    nvl clear

    him_c "Hey, Thuc, how's Gardenia doing?"
    thuc_c "Good! I thought I would never see her when she got married to that miner, but they actually come around all the time."
    julia_c "Especially when they know there will be lots of food."
    him_c "Your grandkids are getting big now, too! Looks like you're teaching them to juggle?"
    thuc_c "Heh. Yeah, he keeps sneaking off to juggle when he's supposed to be pulling weeds."
    sara_c "Speaking of kids, have you heard from Raúl lately, Natalia?"
    natalia_c "He comes over every weekend or so. Whenever he can get a break from mining."
    her_c "I always thought he'd become a farmer, like you and Martín. He always loved digging in the dirt."
    natalia_c "Since Martín died, he's been trying to help out the family. He can earn so much more as a miner that he feels it's the best way to help out."
    pavel_c "Oh! I have good news! I'm a great-grandfather now!"
    thuc_c "You've always been a great grandfather."
    pavel_c "Yes, but now everybody has to call me that."
    him_c "Congrats, you GREAT grandfather, you!"
    pavel_c "I just wish I could hold the baby and be there with them..."
    natalia_c "I have a couple of grandbabies you can borrow for a while. Come over for dinner tomorrow night, and bring some of your curry spices!"
    pavel_c "Thank you Natalia but... well... yes, perhaps I will."

    nvl clear
    return

# Community: Reckoning with jellypeople. There are several ways to fail the jellypeople. If you agree to help them, you can either farm mudfish or one of their predators, a fish called a Shill. You can also choose to tell Brennan about possible heavy metals in the mud. Miranda reveals that she and Dr. Lily taught the jellysquid how to “read”.
# Family: Terra wants a bike!
label message27:
    nvl clear
    kid_c "save the jellystars! these stellar animals grow into intelligent jellysquids! DON'T eat them!!!!!!!!!!!!!!!!!!!!!!!!!!!! {font=fonts/OpenSansEmoji.otf}(>˛<’!){/font}"
    sara_c "But they're so tasty and cheap..."
    brennan_c "And a good source of protein."
    kid_c "so are babies but we don't eat those do we!!?"
    pavel_c "I appreciate your good intentions, [kid_name], but I don't think eating jellystars is a problem."
    natalia_c "Yeah, we have way more important things to worry about."
    zaina_c "After learning more about them, I decided not to eat them anymore. Go read some of the research."
    kid_c "good! thank you zaina your stellar!!! {font=fonts/OpenSansEmoji.otf}o(^v^)o{/font}"
    pavel_c "It's so important to eat well. Though I do love jelly with peanut butter... that's okay, isn't it?"
    kid_c "Um, yeah, I think so, I was talking about jellystars."
    pavel_c "Is that a new candy?"
    kid_c "no, you know jellystars the creatures that live in the sea?"
    pavel_c "We should ask Dr. Lily about that."
    kid_c "sorry but I think she died."
    pavel_c "Oh, dear. That is distressing news."
    natalia_c "It was several years ago, Pavel. It's okay."
    pavel_c "I'm sorry; it was rude of me to bring it up."

    nvl clear
    return

# Community: Mayor Grayson dies--you can choose to approve of euthanasia or not, which he requests after realizing he suffers from dementia. Also, you can vote for if miners should be allowed to vote for a new mayor. Your relationship values, not your vote, determines this outcome. Higher miner values means that the colonists vote for them to be able to vote, and they elect Kevin. Otherwise the colonists vote NOT to let them vote, and elect Julia.
# Family: Plans for future
label message28:
    nvl clear
    thuc_c "So the jellysquid are like, real live aliens?! That's so cool!"
    sara_c "Does this mean we shouldn't eat them anymore?"
    him_c "We shouldn't eat the jellysquids, but they don't mind if we eat jellystars."
    sara_c "But... aren't the jellystars like their babies?! {emoji=shocked}"
    zaina_c "Their life cycle is not analogous to humans'. The jellystars are not sentient and are more like eggs than babies."
    sara_c "But if they have the possibility to become sentient... I don't think I'm going to eat them anymore. Plus they are just too cute! {emoji=hearteyes}"
    if (ate_jellyfish):
        him_c "They are adorable!"
    kid_c "yay, sara! ur such a stellar mom! {font=fonts/OpenSansEmoji.otf}\(^ O ^)/{/font}"
    oleg_c "only bc she's not ur mom. now she won't cook me jellies. (q n p)"
    nvl clear
    return

# Community: brainstorming: Pete is desperate for more credits after Helen has a high-risk pregnancy. No one is buying fireweed from him anymore… because he’s being undersold by Julia. [If you told Brennan about the heavy metals in the mud, he’s now mining there and making the water silty--so jellysquid no longer appear in the area. Otherwise maybe the jellypeople are helping you, or nothing.]
# Family: Terra blames you for a big crisis!
label message29:
    nvl clear
    # People miss Mayor Grayson - his spice garden is dying but ?? volunteers to take over it as a memorial
    # Someone also mentions how maybe it was a good thing he didn't drag out a demented life for years, people voice opinions
    # Travis opens a restaurant/bar?
    if kevin_elected:
        kevin_c "I received an Earth QEC message from Mayor Grayson's family."
        kevin_c "It says, 'Thank you for taking care of Pavel when we could not. We apologize that he became a burden but appreciate the bonds you shared with him.'"
    else:
        julia_c "I just got a QEC message from Mayor Grayson's family."
        julia_c "It says, 'Thank you for taking care of Pavel when we could not. We apologize that he became a burden but appreciate the bonds you shared with him.'"
    natalia_c "He has a wonderful family..."
    if no_euthanasia_26:
        sara_c "If only I hadn't left him that night... maybe he would still be alive. {emoji=cry}"
        julia_c "If you're going to blame anyone, blame me. I was late for my shift."
        her_c "You might as well blame the new baby you were delivering that was the cause of you being late. It was an accident; it wasn't anyone's fault."
        him_c "I know he didn't remember much at the end... but I do know that we helped him to feel loved and happy when we took care of him."
    else:
        him_c "At least they weren't mad at us for allowing him to commit suicide."
        natalia_c "He was so lonely without Naomi and his family. We tried to be there for him, but nothing can replace your own family."
        her_c "It was what he wanted."
    thuc_c "What's going to happen to his spice garden? It's starting to look a little dead."
    julia_c "Someone should live in that house, too... it needs a little work but it's right in the middle of town."
    travis_c "Hey, is it okay if I move in there? I want a permanent home for my restaurant, and I'd definitely take care of the spice garden."
    if kevin_elected:
        kevin_c "I will put it on the agenda for the next town council meeting."
    else:
        julia_c "We'll have to run it by the town council, but I don't see why not."
    him_c "I'll make a memorial plaque to go in the garden... so we can always remember Pavel, and Naomi."

    nvl clear
    return

# Community: MURDER MYSTERY
# Family: is she taking the shuttle back to Earth??
label message30:
    nvl clear
    # Miner's shuttle is leaving. Most are returning to Earth since contracts are complete; a few have renewed to stay on as senior workers
    sara_c "Is it true there's going to be chocolate coming on the shuttle?!"
    him_c "They are including some coffee, sugar, and chocolate, yes."
    sara_c "Yay! {emoji=hearteyes}"

    brennan_c "It's going to be busy these next few days, so if I don't get a chance, I wanted to say farewell to all of you."
    sara_c "Are you ever coming back?"
    brennan_c "I sure hope not. I thought two years was bad; twelve years is way too long to go without a decent bed, shower, pub, club, restaurant... I could go on and on."
    travis_c "At least we have a restaurant now!"
    brennan_c "That's the only thing that's made this last year bearable."
    him_c "If you can't appreciate the amazing beauty of Talaam, you don't deserve to be here."
    brennan_c "I certainly deserve better than this."
    julia_c "So who's in charge of the miners now?"
    brennan_c "Someone new. Only a few miners are staying on for a second term."
    her_c "We wish you well, Brennan."

    nvl clear
    return



# TODO: redo these with new colors, make icons, etc.
# NVL mode characters for chat rooms, etc
define her_c = Character("her_name", dynamic=True, who_suffix = "  {image=images/icons/her-icon.png} ",
    color="#84b766", image="her", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # mint green # TODO: should this match something in her clothes?
define him_c = Character("his_name", dynamic=True, who_suffix = "  {image=images/icons/him-icon.png} ",
    color="#bc1e0e", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # red of his eyes
define kid_c = Character("kid_name", dynamic=True,
#who_suffix = "  {image=images/icons/kid-icon.png} ",
        color="#ca67ac", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # reddish purple
define naomi_c = Character("Naomi", who_suffix = "  {image=images/icons/naomi-icon.png} ",
    color="#bf98ff", image="naomi", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lavender
define pavel_c = Character("Pavel", who_suffix = "  {image=images/icons/pavel-icon.png} ",
    color="#cccccc", image="pavel_c", kind=nvl, ctc="ctc_blink", ctc_position="nestled")   #gray
define lily_c = Character("Dr. Lily", who_suffix = "  {image=images/icons/lily-icon.png} ",
    color="#655283", image="lily", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #dark purple
define sara_c = Character("Sara", who_suffix = "  {image=images/icons/sara-icon.png} ",
    color="#ff6767", image="sara", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  # salmon pink
define thuc_c = Character("Thuc", who_suffix = "  {image=images/icons/thuc-icon.png} ",
    color="a9ff22", image="thuc", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian_c = Character("Ilian", who_suffix = "  {image=images/icons/ilian-icon.png} ",
    color="d2d099", image="ilian", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #khaki
define brennan_c = Character("Brennan", who_suffix = "  {image=images/icons/brennan-icon.png} ",
    color="119811", image="brennan", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #irish green
define pete_c = Character("Pete", who_suffix = "  {image=images/icons/pete-icon.png} ",
    color="ee7755", image="pete", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia_c = Character("Natalia", who_suffix = "  {image=images/icons/natalia-icon.png} ",
    color="f3ca14", image="natalia", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen_c = Character("Helen", who_suffix = "  {image=images/icons/helen-icon.png} ",
    color="77b8ef", image="helen", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #sky blue
define julia_c = Character("Julia", who_suffix = "  {image=images/icons/julia-icon.png} ",
    color="#e7b1cb", image="julia", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #icy pink
define martín_c = Character("Martín", who_suffix = "  {image=images/icons/martin-icon.png} ",
    color="#9b5b1d", image="martin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #brown
define anya_c = Character("Anya",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="#53b5ab", image="anya", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #cyan
define lewis_c = Character("Mr. Lewis",
    color="f3ca14", image="lewis", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
# TODO: change these colors here and in defines.rpy once we have images for them
define zaina_c = Character ("Zaina",
    #who_suffix = "  {image=images/icons/zaina-icon.png} ",
    color="#d8cd87", image="zaina", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kevin_c = Character ("Kevin",
    #who_suffix = "  {image=images/icons/kevin-icon.png} ",
    color="#324cc5", image="kevin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define oleg_c = Character("Oleg",
#who_suffix = "  {image=images/icons/oleg-icon.png} ",
    color="#d8a687", image="oleg", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #sandstone
define travis_c = Character("Travis",
#who_suffix = "  {image=images/icons/travis-icon.png} ",
    color="#ee7755", image="travis", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #rusty brown
define van_c = Character("Van",
#who_suffix = "  {image=images/icons/van-icon.png} ",
        color="55a0ef", image="van", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #light blue
define ret_c = Character("RET",
#who_suffix = "  {image=images/icons/ret-icon.png} ",
        color="555555", image="ret", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #gray

define computer = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled", what_font="fonts/FreeMono.ttf")

# TODO: make this look like a EULA document
define legalese = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")
