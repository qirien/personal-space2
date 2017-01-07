# Library of functions we call that have to do with game variables, etc.

label increase_attachment:
    # if (responsive <= 0):
        # $ attachment += 1
    # else:
        # $ attachment += (responsive/(year/2.0)) * 2
    $ attachment += responsive / 2.0
    return
    
label increase_competence:
   
    $ competence += demanding / 2.0
    return
    
label increase_independence:
    $ independence += (demanding + responsive) / 2.0
    return
    

# I would like community events to be affected by the player's current parenting style. I want to make a function that returns the players current parenting style. 
# commenting it out for now until I can come back and think about it some more
# This might have to be calculated on a case-by-case basis, since different "times" of the year will have different total possible stat totals.

# label get_attachment:
#   return $ responsive / 2.0 