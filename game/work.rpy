## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting." 
    return

# Year 3, 18 mo. old
label work1:
    "Want some bees? They'll permanently use one square but will yield honey with a moderate amount of work and may increase yield of some other squares."
    return

# Year 6, 3.5 years old
label work2:
    "Your family reacts to crops you've been planting."
    return

# Year 9, 5.5 years old
label work3:
    "Making sausage out of goat/crabird meat. Charcuterie!"
    return

# Year 12, 7.4 years old
label work4:
    "You had a decent harvest, but a salesman from RET offers some hybrid wheat seeds that he claims will be the most productive crop you've ever seen."
    "The only problem is, the seeds are infertile, so you'd have to buy them every year."
    "In fact, he'll only sell them to you if you sign a contract to buy some from him every year for the next ten Talaam years."
    menu:
        "Sign a wheat contract?"
        "Yes":
            $ colony += 1
            # you sold your soul but can now grow wheat.
        "No":
            $ luddites += 1
            # the luddites approve and offer to get you started with some of their heirloom wheat instead
    
    return

# Year 15, 9.4 years old
label work5:
    "Take your daughter to work day... is every day."
    $ style = get_parenting_style()
    if (style== "authoritative"):
        "She is pretty helpful and gets a lot done!"
    elif (style == "authoritarian"):
        "She does every thing you ask, but you have to ask her to do each little thing. She doesn't take any initiative to do things on her own."
    else:
        "She sulks and you have to threaten and cajole her to do anything.  It would have been faster to do it yourself!"
    "Terra helps out with some simple things, but she isn't very good at it. Do you redo it, make her redo it, or spend some time teaching her better? Do you have her help in the future?"        
    return

# Year 18, 11.1 years old
label work6:
    "Fungus disaster strikes!"
    return

# Year 21, 13 years old
label work7:
    "Miners want cheap/fast/calorie-dense food. Will you cater to their needs?"
    "Also, Terra likes it as she is eating more and growing taller than ever."
    return

# Year 24, 14.8 years old
label work8:
   "You throw out your back."
   "People from your favorite faction help you, or not."
   return

# Year 27, 16.7 years old
label work9:
    "Work 9"
    return

# Year 30, 18 years old
label work10:

    return

    
