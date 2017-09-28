##
# Other events that happen outside the work/family/community event structure,
# such as the parenting class.
#

label parenting_class_questions:
        naomi "And now we have some time for individual questions."
        menu:
            "What should I ask?"
            "How do you make your kids do stuff?":
                him surprised "How do you make your kids do stuff?"
                naomi "It sounds like you want [kid_name] to do something she does not want to do."
                him normal "Yeah, like every day!"
                naomi "[kid_name] is an independent, spirited child who likes to make her own choices."
                him concerned "Yeah, tell me about it!"
                naomi "So, I recommend two things. First, whenever possible, give her choices. If framed properly, they will help her feel autonomous but both will be acceptable to you."
                naomi "Second, set specific, related consequences that will occur if she does not do what you ask. Make sure she clearly understands the actions you expect her to take, and what she can expect from you if she does not comply."
                him surprised "And that will make her do what I want?"
                naomi "Not at first. But here is the key: you have to be willing to follow through with the consequences you set without getting angry."
                him concerned "Why shouldn't I get angry?"
                naomi "You want to teach her to control her emotions, correct?"
                him determined "Yes..."
                naomi "A child's first teacher is her parents' example. When you are in control of your emotions, you show her that that is the proper way to behave."
            "How do you teach kids how to get along?"
            "How are teenagers different from little kids?"
            "What should you do when a kid disobeys?"
            "How do you talk to kids about sex?"
            
        return
            

label parenting_class1:
    scene community_center with fade
    naomi "I'm so glad you all want to learn about being better parents."
    natalia "I mostly just have a problem with one kid."
    helen "How is this going to work when all our kids are such different ages?"
    naomi "Even for different ages of children, the principles are the same. I'll make sure to save time for specific questions and discussion at the end."
    naomi "What do you think is the most important thing a child needs? Think about it, and write down your answer."
    menu:
        "What does a child need most?"
        "To survive.":
            "I wrote 'Survival'."
            him "You can't do anything else if you're dead."
            naomi "That is true. What else?"            
            helen "Love."
            natalia "Learning."
        "To be loved.":
            "I wrote 'Love'."
            him "If you feel loved and secure, you have the motivation to do anything else."
            naomi "Good, love is important. What else does a child need?"
            natalia "Survival is important, too. They need to be safe."
            helen "On Earth that might have been a given, but here..."
            naomi "True, parents are responsible for their children's survival!"
            him "They also need to learn how to be adults. Otherwise, what's the point?"
        "To learn.":
            "I wrote 'Learning'."
            him "The whole job of kids is to learn to be responsible adults. Without that, there's no point in having kids."
            naomi "Yes, I see. What else does a child need?"
            natalia "Survival, of course."
            helen "And love."
    naomi "Love is the vehicle through which we deliver a child's needs. Just love won't feed a child, or teach him to work hard. But we provide all these things with love."
    natalia "Not just feeling love, but doing the things your child needs most to grow."
    naomi "And if you try to teach these things without love, a child will not want to learn and will not feel safe making the mistakes he needs to make to learn."
    him surprised "Do we really want our kids to feel safe making mistakes? That sounds dangerous."
    naomi "As parents, part of your job is protect kids from making terrible, life-altering mistakes. But without making small mistakes, they will not learn for themselves."
    helen "I guess Trevor could have never learned to walk without falling so many times."
    natalia "And Tomás could have never learned how to get along so well with his wife without having many disagreements with his siblings." 
    naomi "Yes, that is correct."
    
    "We talked for a while about being patient with kids' mistakes, and common mistakes for different ages. It was reassuring to learn things like wetting the bed and talking back were completely normal."

    call parenting_class_questions    
    return
    
    
