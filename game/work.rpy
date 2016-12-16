## Work Events

label work_default:
    "I worked hard all year, preparing fields and planting and weeding and harvesting." 
    return

label work1:
    "Want some bees? They'll permanently use one square but will yield honey with a moderate amount of work and may increase yield of some other squares."
    return


label work2:
    "Take your daughter to work day... is every day."
    return


label work3:
    "Making sausage out of goat/crabird meat. Charcuterie!"
    return


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


label work5:
    "Your family reacts to crops you've been planting."
    return


label work6:
    "Fungus disaster strikes!"
    return


label work7:
    "Miners want cheap/fast/calorie-dense food. Will you cater to their needs?"
    return


label work8:
   "You throw out your back."
   "People from your favorite faction help you, or not."
   return


label work9:
    "Work 9"
    return


label work10:
    "Terra helps out with some simple things, but she isn't very good at it. Do you redo it, make her redo it, or spend some time teaching her better? Do you have her help in the future?"
    return

    
