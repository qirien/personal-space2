##
# ENDINGS
#

# Determine which ending the user should receive, depending on Terra's stats.
# TODO: Add community ending
label ending:
    # TODO: remove debug code
    "Reached ending. Attachment: [attachment], Competence: [competence], Independence: [independence]"
    if (attachment < ATTACHMENT_GOOD):
        if (competence < COMPETENCE_GOOD):
            # aci and acI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_aci
            else:
                jump ending_acI
        else:
            # aCi and aCI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_aCi
            else:
                jump ending_aCI
    else:
        if (competence < COMPETENCE_GOOD):
            # Aci and AcI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_Aci
            else:
                jump ending_AcI
        else:
            # ACi and ACI
            if (independence < INDEPENDENCE_GOOD):
                jump ending_ACi
            else:
                jump ending_ACI
            
    call credits
    return
                
#1 aci - Blames you for everything. Clingy. Follows (miner?) boyfriend back to Earth but you know the relationship won't last.
label ending_aci:
    "Ending aci."
    return
    
#2 acI - Rejects your life and joins luddites/returns to Earth to fulfill her dream of becoming a ________, but fails. Moves from one job to the next, but drives away people around her and isn't good at anything.
label ending_acI:
    "Ending acI."
    return
    
#3 aCi - Gets sucked into a crappy marriage on Talaam with the first person who shows affection, but at least she won't die of starvation.
label ending_aCi:
    "Ending aCi."
    return
    
#4 aCI - Rejects your life and returns to Earth to fulfill her dreams and she succeeds, becoming an awesome __________, though you worry about her lack of friends/family
label ending_aCI:
    "Ending aCI."
    return
    
#5 Aci - stays on your farm helping you, though she doesn't work hard enough to be of much help.
label ending_Aci:
    "I kept expecting [kid_name] to get married and leave us, or go off to pursue her own dreams, but so far she seems content to keep things as they are."
    "She helps around the farm sometimes, but I still feel like I have to tell her how to do things and keep a close eye on her."
    "I remember when she was little, she wasn't afraid of anything, and she couldn't wait to do new things like go to school or go to the beach."
    "Now, when I ask her what she sees in her future, she just shrugs."
    "She's changed a lot...but in some ways, she's still a kid."
    "That's fine for now, but part of me wants more for her."
    "Should she want to leave home? Is it my fault that she doesn't? Should I have taught her more, somehow?"
    "I can't stop thinking these kinds of things."
    "I guess that's part of what it means to be a parent."
    
    "Ending 5/8, Forever My Little Girl"
    
    return
    
#6 AcI - like #8, sets out on her own, but you worry she will not know enough or be able to work hard enough
label ending_AcI:
    "Ending AcI."
    return
    
#7 ACi - starts a farm nearby, asks you for help all the time, second-guesses herself
label ending_ACi:
    "Ending ACi."
    return
    
#8 ACI - becomes an expert in her field, starts to form her own happy family on Talaam
label ending_ACI:
    "Ending ACI."
    return
