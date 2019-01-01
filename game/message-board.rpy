# These are messages that appear on the colony message board each year
# The comments above say what will happen that year.

# Community: New colonists arrive
# Family: Terra won't stop crying.
label message1:
    nvl clear
    naomi_c "Congratulations to Sara and Ilian on the birth of their son Oleg!"
    him_c "I don't know whether to congratulate you or commiserate with you..."
    sara_c "Maybe both? :-D"
    nvl clear
    return

# Community: Bring whole harvest to storehouse?
# Family: Get work done or play with kid?
label message2:
    nvl clear
    return

# Community: Game Night!
# Family: Camping trip, Terra puts everything into her mouth
label message3:
    nvl clear
    return

# Community: Community Liaison
# Family: Terra's a picky eater!
label message4:
    nvl clear
    return

# Community: Set aside food for miners?
# Family: Toilet Training!
label message5:
    nvl clear
    return

# Community: Game Night continued/consequences
# Family: Terra wants to talk and play when everyone else wants to rest, Ready for another baby?
label message6:
    nvl clear
    return

# Community: Comparing compensation
# Family: Back Talking & Disobedience
label message7:
    nvl clear
    return

# Community: RET will send what luxuries?
# Family: Play group and first day of school. Baby bro born, else pregnant
label message8:
    nvl clear
    return

# Community: Camping with Pete
# Family: Bossing friends around
label message9:
    nvl clear
    return

# Community: Peron's over, who should take care of farm?
# Family: Fighting with brother OR playing games on tablet when she's not supposed to. Baby bro born if not already
label message10:
    nvl clear
    return

# Community: Miners and Brennan arrive on shuttle
# Family: Dinner Table Manners
label message11:
    nvl clear
    return

# Community: missing cow
# Family: An unknown miner friend, lice
label message12:
    nvl clear
    return

# Community: Save the Cave!
# Family: Sex education, miscarriage
label message13:
    nvl clear
    return

# Community: Pete leaves
# Family: Teacher trouble
label message14:
    nvl clear
    return

# Community: Naomi dies
# Family: Allowance?
label message15:
    nvl clear
    return

# Community: Trade with luddites?
# Family: She must clean her room!!
label message16:
    nvl clear
    return

# Community: Harvest festival with jellyfish!
# Family: Bro has unexplained crying
label message17:
    nvl clear
    return

# Community: Miners complain about Pete's cattle
# Family: Terra needs more baths!
label message18:
    nvl clear
    return

# Community: Crabirds devastate harvest
# Family: What to do about pornography
label message19:
    nvl clear
    return

# Community: Lily's research, she dies
# Family: Musical instrument?
label message20:
    nvl clear
    return

# Community: Visit ocean. Build relationship with miners or luddites depending on their values. Discuss firegrass w/miners if relationship is high enough.
# Family: Terra's mean and sarcastic
label message21:
    nvl clear
    return

# Community: Miners moving to mountain near luddites! If your relationship with both parties is good, you can coordinate and avoid accident. Otherwise bad things can happen (mining stops and you lose your status as RET liason, you scare off the luddites and zero your relationship with them, or you encourage them to stay and Travis loses his leg). This is the second “save the cave” incident; modify the earlier one to be about something other than a cave.
# Family: Apologize when you falsely accuse Terra? Family activities
label message22:
    nvl clear
    return

# Community: Glass shell collecting--shells are worth more if mining stopped in 22 and...
# Family: Screen time, chatting with friends instead of homework
# 14.8 years
label message23:
    nvl clear
    return

# Community: Growing luxury good market, especially if mining stopped in 22. The increased demand for shells led to inflation and Ilian fixes the prices of food. You can choose to write a farming guide, which Oleg makes free, babysit (most lucrative and stressful), or be a farming consultant.
# Family: Lettie dies; friends with creepy older brother
label message24:
    nvl clear
    return

# Community: Brennan’s jellysquid farm. You can talk to Chaco or Pete about the jellysquid farm, depending on your Miner or Luddite relationship scores.
# Family: Making dinner, talking about education and jobs
label message25:
    nvl clear
    return

# Community: You can choose to tell colonists that Pete’s beef contains cancer cells.
# There’s also discussion about how to help a heavy user of firegrass, Carol. Depending on certain values, you can convince Brennan to prevent miners from working too long of hours or grow more tea or nothing. No matter what you choose, Oleg makes an educational app (he or one of his friends has a side-business of their own firegrass dealings).
# ALSO in this long event, a shuttle arrives with material to start an artificial meat plant. You can choose to keep buying meat from Pete or not.
# Family: Talking politics? Terra thinks you're a terrible leader. Either you're too strict, treating one group badly (miners? Jellies?), Or you are clueless and you don't even know what people are doing behind your back.
label message26:
    nvl clear
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
    zaina_c "Their life cycle is not analogous to humans'. The jellystars are not sentient and are more like bacteria than babies."
    sara_c "But if they have the possibility to become sentient... I don't think I'm going to eat them anymore. Plus they are just too cute! 😍"
    if (ate_jellyfish):
        him_c "They are adorable!"
    nvl clear

# Community: brainstorming: Pete is desperate for more credits after Helen has a high-risk pregnancy. No one is buying fireweed from him anymore… because he’s being undersold by Julia. [If you told Brennan about the heavy metals in the mud, he’s now mining there and making the water silty--so jellysquid no longer appear in the area. Otherwise maybe the jellypeople are helping you, or nothing.]
# Family: Terra blames you for a big crisis!
label message29:
    nvl clear
    return

# Community: MURDER MYSTERY
# Family: Ending?
label message30:
    nvl clear
    return



# TODO: redo these with new colors, make icons, etc.
# NVL mode characters for chat rooms, etc
define her_c = DynamicCharacter("her_name", who_suffix = "  {image=images/icons/her-icon.png} ",
    color="#84b766", image="her", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # green of her eyes
define him_c = DynamicCharacter("his_name", who_suffix = "  {image=images/icons/him-icon.png} ",
    color="#bc1e0e", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # red of his eyes
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
define miranda_c = Character("Miranda",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define lewis_c = Character("Mr. Lewis",
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define zaina_c = Character ("Zaina",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="zaina", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kevin_c = Character ("Kevin",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="kevin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kid_c = DynamicCharacter ("kid_name",
    #who_suffix = "  {image=images/icons/kid-icon.png} ",
    color="#e361ef", image="kid", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now

define computer = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")
