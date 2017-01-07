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
    

# Returns the players current parenting style.
# Should be one of authoritative, authoritarian, permissive, passive, or neglectful
init -100 python:
    def get_parenting_style():
        if (total_attachment >= year):
            if (total_demanding >= year):
                return "authoritative"
            else:
                return "permissive"
        else:
           if (total_demanding >= year):
               return "authoritarian"
           else:
                return "passive"
        return "passive"
        
    
# commenting it out for now until I can come back and think about it some more
# This might have to be calculated on a case-by-case basis, since different "times" of the year will have different total possible stat totals.

# label get_attachment:
#   return $ responsive / 2.0 