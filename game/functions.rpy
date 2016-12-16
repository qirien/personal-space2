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
    
