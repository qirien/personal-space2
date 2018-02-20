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
                him annoyed "Yeah, every day!"
                naomi "[kid_name] is an independent, spirited child who likes to make her own choices."
                him concerned "You got that right..."
                naomi "So, I recommend two things. First, whenever possible, give her choices. If framed properly, they will help her feel autonomous, but make sure both choices are acceptable to you."
                naomi "Second, set specific, related consequences that will occur if she does not do what you ask. Make sure she clearly understands the actions you expect her to take, and what she can expect from you if she does not comply."
                him surprised "And that will make her do what I want?"
                naomi "Not at first. But here is the key: you have to be willing to follow through with the consequences you set without getting angry."
                him concerned "Why shouldn't I get angry?"
                naomi "You want to teach her to control her emotions, correct?"
                him determined "Yes..."
                naomi "A child's most influential teacher is her parents' example. When you are in control of your emotions, you show her that that is the proper way to behave."
            "How do you make your kids get along?":
                him surprised "How do you make your kids get along?"
                naomi "First, do you really want to {b}make{/b} your kids get along? Or do you want to teach them how to get along?"
                him concerned "It doesn't seem like it should be that hard not to take someone's toys!"
                naomi "For them, it is hard. This doesn't mean we excuse the behavior; they do need to learn how to share. But understanding this helps us be patient with them and remember to teach the right way."
                him determined "So what do you do if two kids aren't getting along?"
                naomi "Usually if they're not getting along, there is a problem. They need you to teach them how to solve that problem together."
                him concerned "I should have known it wouldn't be simple..."
                naomi "For example, if they both want to play with a toy at the same time, you could suggest several options -- taking turns, using a different toy, playing something else -- and let them discuss it."
                him determined "I don't think they would ever agree on a solution."
                naomi "Then perhaps  neither can play with the toy until they both agree on how they will share it."
                him normal "Okay, I'll try that."
                naomi "Just try to remember to focus on solving problems together, not pointing fingers at each other."
                if (is_liason):
                    him determined "That's good advice for everyone."
                    naomi "Yes, there is much overlap between parenting and leading a community."
                    him normal "Thanks for the leadership training, Sister Naomi."
                    naomi "You're welcome. You're doing a fine job, and I'm glad you are learning even more ways to lead people well."
            "What should you do when a kid disobeys?":
                him surprised "What should you do when a kid deliberately disobeys?"
                naomi "[kid_name] likes to do things her own way, doesn't she?"
                him determined "Yeah, so you know what I'm talking about."
                naomi "If you expect you may have trouble getting her to do something, you may want to decide on a logical consequence ahead of time."
                him surprised "Like what?"
                naomi "For example, you might tell her, 'I expect your room to be clean in two hours. If you choose not to clean your room before two hours is up, you will not be able to play with friends today.'"
                him determined "That sounds reasonable."
                naomi "Contrast this to what many parents end up saying, which is 'Clean your room now, or you'll be grounded for a month!'"
                him concerned "Yeah, and then when they don't clean their room you have to decide if you're really going to ground them for that long."
                naomi "You also need to make sure that she knows exactly what you want her to do, and has the necessary skills to accomplish it."
                him surprised "What do you mean?"
                naomi "Well, you wouldn't ask her to plow the fields without teaching her how, right?"
                him determined "Right..."
                naomi "Sometimes we forget that children also need to learn how to do simple things, like cleaning their room, or washing dishes, or putting away their laundry."
                him concerned "I guess no one's born knowing how to do those things..."
                naomi "And they will learn that best with lots of positive encouragement as they master each small step. It may sound silly to you to say, 'Thank you for putting your socks away,' but it is effective."
            "How do you talk to kids about sex?":
                him surprised "How do you talk to kids about sex?"
                naomi "How do you want your kids to feel about their bodies? About babies? About affection?"
                him determined "Well, those are all good things, I guess."
                naomi "Then let your conversation reflect that as you talk about the parts of human life they are ready to learn about."
                him surprised "How can you tell what they are ready for?"
                naomi "If they trust you and have a curious mind, they will ask you when they are ready to know something."
                him concerned "[kid_name] certainly has a curious mind..."
                naomi "You don't need to give lots of details -- just the facts that are most relevant to her. A toddler may just want to know the proper names for all the body parts. A child may wonder where babies come from. A teenager may want to know how to tell if you love someone."
                him concerned "My parents didn't talk to me much about those things."
                naomi "Then you may need some practice. If you seem embarrassed or upset that she is asking about sex, then she will not want to ask you in the future. You could start by talking to [her_name]."
                him surprised "Can't they just talk to [her_name] about it?"
                naomi "[kid_name] may want to know what you have to say."
                "That thought had never occurred to me before -- that when [kid_name] asked me a question, she didn't just want an answer, she wanted {b}my{/b} answer."
            
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
    her surprised "Do we really want our kids to feel safe making mistakes? That sounds dangerous."
    naomi "As parents, part of your job is protect kids from making terrible, life-altering mistakes. But without making small mistakes, they will not learn for themselves."
    helen "I guess Travis could have never learned to walk without falling so many times."
    natalia "And Tomás could have never learned how to get along so well with his wife without having many disagreements with his siblings." 
    naomi "Yes, exactly."
    
    "We talked for a while about being patient with kids' mistakes, and common mistakes for different ages. It was reassuring to learn things like wetting the bed and talking back were completely normal."

    call parenting_class_questions    
    return
    
    
