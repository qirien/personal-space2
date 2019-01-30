# These are messages that appear on the colony message board each year
# The comments above say what will happen that year.

# To change appearance, see screens.rpy, screen nvl
label yearly_messages:
    $ message = "message" + `year`
    $ read_messages = True
    nvl clear
    call expression message
    #computer "\n(End of messages)"
    nvl clear
    call screen plan_farm
    return

# Community: New colonists arrive
# Family: Terra won't stop crying.
label message1:
    nvl clear
    naomi_c "Congratulations to Sara and Ilian on the birth of their son Oleg!"
    him_c "I don't know whether to congratulate you or commiserate with you..."
    sara_c "Maybe both? :-D"
    # TODO: finish this?
    # Natalia and Julia give great, conflicting baby advice
    natalia_c "I hope you can get some time to yourself once in a while still!"
    julia_c "Nonsense. Babies need their mothers' touch. I hope you are snuggling that baby close as often as possible. And breastfeeding. And swaddling. And cosleeping. And sleeping when the baby sleeps."
    natalia_c "Julia, those are all fine things, but babies also need to learn to make do when their parents have to do other things."
    julia_c "Parents should want what's best for their children. And no one can take the place of a loving mother."
    her_c "It's totally fine to let someone take your place sometimes. I would go crazy if I had to be holding [kid_name] every second!"
    him_c "Yeah, give me that baby, it's my turn to snuggle!"
    sara_c "It's good to see SOME dads enjoy snuggling with their babies."

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
    martin_c "I have artichokes."
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
    pete_c "...probably not. But, holy hand grenade in a hand basket, she is one fine woman!"
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
    return

# Community: Game Night continued/consequences
# Family: Terra wants to talk and play when everyone else wants to rest, Ready for another baby?
label message6:
    nvl clear
    # busy harvest time - looking forward to holiday Halloween + Thanksgiving
    # Kevin/Zaina asking about local alien meat
    return

# Community: Comparing compensation
# Family: Back Talking & Disobedience
label message7:
    nvl clear
    # Game night discussion - poker?
    return

# Community: RET will send what luxuries?
# Family: Play group and first day of school. Baby bro born, else pregnant
label message8:
    nvl clear
    # Natalia asking for harvest help as Martin is sick
    return

# Community: Camping with Pete
# Family: Bossing friends around
label message9:
    nvl clear
    # Congrats on baby/pregnant
    # School talent show!
    return

# Community: Peron's over, who should take care of farm?
# Family: Fighting with brother OR playing games on tablet when she's not supposed to. Baby bro born if not already
label message10:
    nvl clear
    # Location of miners discussed: "why so far" "not far enough!"
    return

# Community: Miners and Brennan arrive on shuttle
# Family: Dinner Table Manners
label message11:
    nvl clear
    # sports teams for various ages forming
    # literary magazine being compiled by Isabella - write poetry for it??
    return

# Community: missing cow
# Family: An unknown miner friend, lice
label message12:
    nvl clear
    # Miners appear on msg board; create new colonists-only board
    # People comment on literary magazine
    return

# Community: Save the Cave/Mountaintop!
# Family: Sex education, miscarriage
label message13:
    nvl clear
    # What kind of mining are they doing, anyway?? Why? What are they mining? How is it profitable?
    # Indium is used in LCDs, solar panels, cryogenics. Finding a lot! Also copper is running out
    return

# Community: Pete leaves
# Family: Teacher trouble
label message14:
    nvl clear
    # Wait, a shuttle is leaving?? Is anyone leaving?
    # Nope, it's just for cargo. There are no humans on board, so we don't to worry about excessive g-forces and life support and other petty concerns
    return

# Community: Naomi dies
# Family: Allowance?
label message15:
    nvl clear
    # jumpropes sold by Gardenia, Julia's daughter
    # meal signup for Naomi
    return

# Community: Trade with luddites?
# Family: She must clean her room!!
label message16:
    nvl clear
    # How is Pete doing? I never talk to him anymore.
    # Sara went to talk with them, gives update
    return

# Community: Harvest festival with jellyfish!
# Family: Bro has unexplained crying
label message17:
    nvl clear
    # Show how busy harvest time is, negotiate when things are harvested to help each other, kids get school off to help
    # Julia offers tea to people that help
    # shouldn't the miners help?? We have our own deadlines
    return

# Community: Miners complain about Pete's cattle
# Family: Terra needs more baths!
label message18:
    nvl clear
    # Someone (Zaina? someone who ate jellies, add to community17 if necessary) is doing a documentary about jellystars and wants footage, art, poetry, etc.
    # Lily has some stuff for her, they are working together
    # You can submit a poem!!!
    return

# Community: Crabirds devastate harvest
# Family: What to do about pornography
label message19:
    nvl clear
    # him_c I have some caulk leftover from roof repair if anyone needs it. Trust me, you don't want to wait until the roof's leaking during a solar flare.
    # Talk about planting season, Peron's planting corn
    return

# Community: Lily's research, she dies
# Family: Musical instrument?
label message20:
    nvl clear
    # Lily and Zaina finished documentary, screening at community center
    # Why the jellystars? Why not crabirds or wolfslugs??
    return

# Community: Visit ocean. Build relationship with miners or luddites depending on their values. Discuss firegrass w/miners if relationship is high enough.
# Family: Terra's mean and sarcastic
label message21:
    nvl clear
    # Naomi's gone, but Sara needs parenting advice. How to deal with teenagers?!
    # Natalia and Julia give conflicting good advice
    return

# Community: Miners moving to mountain near luddites! If your relationship with both parties is good, you can coordinate and avoid accident. Otherwise bad things can happen (mining stops and you lose your status as RET liason, you scare off the luddites and zero your relationship with them, or you encourage them to stay and Travis loses his leg). This is the second “save the cave” incident; modify the earlier one to be about something other than a cave.
# Family: Apologize when you falsely accuse Terra? Family activities
label message22:
    nvl clear
    # Miners are moving; I wonder if they left anything behind? let's go scavenge!
    # Don't bother; there's mostly just tire tracks and a flat dirt clearing and some toxic ponds and a bunch of slag
    return

# Community: Glass shell collecting--shells are worth more if mining stopped in 22 and...
# Family: Screen time, chatting with friends instead of homework
# 14.8 years
label message23:
    nvl clear
    # natalia_c Remember back when we didn't use money?? We just helped each other and everyone got along
    # Everyone except you and Julia
    # julia_c Hard work should be rewarded!
    # It's still different from Earth
    # Capitalism/socialism/spectrum/something else?  We have no economists (Kevin?)
    # Why are we so focused on money?? We should just hang out and enjoy what we have
    return

# Community: Growing luxury good market, especially if mining stopped in 22. The increased demand for shells led to inflation and Ilian fixes the prices of food. You can choose to write a farming guide, which Oleg makes free, babysit (most lucrative and stressful), or be a farming consultant.
# Family: Lettie dies; friends with creepy older brother
label message24:
    nvl clear
    # Julia links to Talaam Times (write free sample page?)
    # it's expensive! no advertising revenue?
    # She didn't review the oatmeal soap because it competes with her goat milk soap
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
    julia_c "How much?"
    brennan_c "Not discussing this on the public forum. Message me."
    return

# Community: You can choose to tell colonists that Pete’s beef contains cancer cells.
# There’s also discussion about how to help a heavy user of firegrass, Carol. Depending on certain values, you can convince Brennan to prevent miners from working too long of hours or grow more tea or nothing. No matter what you choose, Oleg makes an educational app (he or one of his friends has a side-business of their own firegrass dealings).
# ALSO in this long event, a shuttle arrives with material to start an artificial meat plant. You can choose to keep buying meat from Pete or not.
# Family: Talking politics? Terra thinks you're a terrible leader. Either you're too strict, treating one group badly (miners? Jellies?), Or you are clueless and you don't even know what people are doing behind your back.
label message26:
    nvl clear
    # TODO: pull something out of community26 and put it here
    return

# Community: Reckoning with jellypeople. There are several ways to fail the jellypeople. If you agree to help them, you can either farm mudfish or one of their predators, a fish called a Shill. You can also choose to tell Brennan about possible heavy metals in the mud. Miranda reveals that she and Dr. Lily taught the jellysquid how to “read”.
# Family: Terra wants a bike!
label message27:
    nvl clear
    kid_c "Save the jellystars! They grow into intelligent jellysquids! Don't eat them!"
    sara_c "But they're so tasty and cheap..."
    brennan_c "And a good source of protein."
    kid_c "So are babies but we don't eat them!!!"
    zaina_c "I appreciate your good intentions, [kid_name], but I don't think eating jellystars is a problem."
    natalia_c "Yeah, we have way more important things to worry about."
    helen_c "I don't eat them anymore."
    kid_c "Good! Thank you, Helen!"

    nvl clear
    return

# Community: Mayor Grayson dies--you can choose to approve of euthanasia or not, which he requests after realizing he suffers from dementia. Also, you can vote for if miners should be allowed to vote for a new mayor. Your relationship values, not your vote, determines this outcome. Higher miner values means that the colonists vote for them to be able to vote, and they elect Kevin. Otherwise the colonists vote NOT to let them vote, and elect Julia.
# Family: Plans for future
label message28:
    nvl clear
    thuc_c "So the jellysquid are like, real live aliens?! That's so cool!"
    sara_c "Does this mean we shouldn't eat them anymore?"
    him_c "We shouldn't eat the jellysquids, but they don't mind if we eat jellystars."
    sara_c "But... aren't the jellystars like their babies?! 😧"
    zaina_c "Their life cycle is not analogous to humans'. The jellystars are not sentient and are more like eggs than babies."
    sara_c "But if they have the possibility to become sentient... I don't think I'm going to eat them anymore. Plus they are just too cute! 😍"
    if (ate_jellyfish):
        him_c "They are adorable!"
    nvl clear

# Community: brainstorming: Pete is desperate for more credits after Helen has a high-risk pregnancy. No one is buying fireweed from him anymore… because he’s being undersold by Julia. [If you told Brennan about the heavy metals in the mud, he’s now mining there and making the water silty--so jellysquid no longer appear in the area. Otherwise maybe the jellypeople are helping you, or nothing.]
# Family: Terra blames you for a big crisis!
label message29:
    nvl clear
    # People miss Mayor Grayson - his spice garden is dying but ?? volunteers to take over it as a memorial
    # Someone also mentions how maybe it was a good thing he didn't drag out a demented life for years, people voice opinions
    # Travis opens a restaurant/bar?
    return

# Community: MURDER MYSTERY
# Family: Ending?
label message30:
    nvl clear
    # Miner's shuttle is leaving. Most are returning to Earth since contracts are complete; a few have renewed to stay on as senior workers
    return



# TODO: redo these with new colors, make icons, etc.
# NVL mode characters for chat rooms, etc
define her_c = DynamicCharacter("her_name", who_suffix = "  {image=images/icons/her-icon.png} ",
    color="#84b766", image="her", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # mint green
define him_c = DynamicCharacter("his_name", who_suffix = "  {image=images/icons/him-icon.png} ",
    color="#bc1e0e", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # red of his eyes
define kid_c = DynamicCharacter("kid_name",
#who_suffix = "  {image=images/icons/kid-icon.png} ",
        color="#ca67ac", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # reddish purple
define naomi_c = Character("Naomi", who_suffix = "  {image=images/icons/naomi-icon.png} ",
    color="#bf98ff", image="naomi", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lavender
define pavel_c = Character("Pavel", who_suffix = "  {image=images/icons/pavel-icon.png} ",
    color="#cccccc", image="pavel_c", kind=nvl, ctc="ctc_blink", ctc_position="nestled")   #gray
define lily_c = Character("Dr. Lily", who_suffix = "  {image=images/icons/lily-icon.png} ",
    color="#7580d0", image="lily", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #grayish blue
define sara_c = Character("Sara", who_suffix = "  {image=images/icons/sara-icon.png} ",
    color="#e25057", image="sara", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  # salmon pink
define thuc_c = Character("Thuc", who_suffix = "  {image=images/icons/thuc-icon.png} ",
    color="a9ff22", image="thuc", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian_c = Character("Ilian", who_suffix = "  {image=images/icons/ilian-icon.png} ",
    color="d2d099", image="ilian", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #khaki
define brennan_c = Character("Brennan", who_suffix = "  {image=images/icons/brennan-icon.png} ",
    color="33b533", image="brennan", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #irish green
define pete_c = Character("Pete", who_suffix = "  {image=images/icons/pete-icon.png} ",
    color="ee7755", image="pete", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia_c = Character("Natalia", who_suffix = "  {image=images/icons/natalia-icon.png} ",
    color="f3ca14", image="natalia", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen_c = Character("Helen", who_suffix = "  {image=images/icons/helen-icon.png} ",
    color="77b8ef", image="helen", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #sky blue
define julia_c = Character("Julia", who_suffix = "  {image=images/icons/julia-icon.png} ",
    color="#e7b1cb", image="julia", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #icy pink
define martin_c = Character("Martín", who_suffix = "  {image=images/icons/martin-icon.png} ",
    color="#9b5b1d", image="martin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #brown
define anya_c = Character("Anya",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="anya", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define lewis_c = Character("Mr. Lewis",
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define zaina_c = Character ("Zaina",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="zaina", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kevin_c = Character ("Kevin",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="kevin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define oleg_c = Character("Oleg",
#who_suffix = "  {image=images/icons/oleg-icon.png} ",
    color="#f3e6bc", image="oleg", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #khaki
define travis_c = Character("Travis",
#who_suffix = "  {image=images/icons/travis-icon.png} ",
    color="#ee7755", image="travis", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #rusty brown
define van_c = Character("Van",
#who_suffix = "  {image=images/icons/van-icon.png} ",
        color="55a0ef", image="van", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #light blue

define computer = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")

# TODO: make this look like a EULA document
define legalese = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")
