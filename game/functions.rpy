# Library of functions we call that have to do with game variables, etc.

label attachment_increase:
    if (responsive <= 0):
        $ attachment += 1
    else:
        $ attachment += (responsive/(year/2.0)) * 2
    return
    
label competence_increase:
    if (demanding <= 0):
        $ competence += 1
    else:    
        $ competence += (demanding/(year/2.0)) * 2
    return
    
label independence_increase:
    if (responsive <= 0):
        $ independence += 1
    else:
        $ independence += (responsive/(year/2.0))           
        
    if (demanding <= 0):
        $ attachment += 1
    else:    
        $ independence += (demanding/(year/2.0))
    return
    
