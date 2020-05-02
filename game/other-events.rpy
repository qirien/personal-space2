##
# Other events that happen outside the work/family/community event structure,
# such as the parenting class.
#

label parenting_class_questions:
    naomi normal "And now we have some time for individual questions."
    menu:
        "What should I ask?"
        "What if your kid lies to you?":
            him surprised "What if your kid lies to you?"
            naomi happy "Very young children don't usually lie intentionally. It's often difficult for them to distinguish what actually happened from what they wish or imagine happened."
            naomi sad "But eventually our children learn how to deceive. Sometimes they learn it from us, when they see us bend the truth to avoid hurting someone's feelings or to avoid an awkward situation."
            naomi normal "You can prevent some lies by making sure you don't punish kids for telling the truth."
            him determined "Why would anyone do that?"
            naomi sad "Many children's lies are to avoid negative consequences for bad behavior. If you yell furiously, 'Did you take the last strawberry?!', don't be surprised if your child hesitates to answer 'Yes'."
            him concerned "I guess that makes sense."
            naomi normal "However, if you praise telling the truth even when it's difficult, and are calm and prepared for answers that you may not like, you are more likely to receive the truth."
            him annoyed "What if they still lie?"
            naomi sad "They may choose to do so. And you will be disappointed and may need to check on things in person instead of just asking them about where they were or whether their chores were done."
            sara sad "I used to ask Oleg if he had taken out the trash when I knew he hadn't. I thought I was getting him to think for himself, but in reality I was being dishonest by acting like I didn't know."
            sara normal "He still doesn't like to do it, but if I just tell him 'Please take out the trash', there's less opportunity for lying."
        "How do you make your kids do stuff?":
            him surprised "How do you make your kids do stuff?"
            naomi happy "It sounds like you want [kid_name] to do something she does not want to do."
            him annoyed "Yeah, every day!"
            naomi normal "[kid_name] is an independent, spirited child who likes to make her own choices."
            him concerned "You got that right..."
            naomi sad "So, I recommend two things. First, whenever possible, give her choices. If framed properly, they will help her feel autonomous, but make sure both choices are acceptable to you."
            naomi normal "Second, set specific, related consequences that will occur if she does not do what you ask. Make sure she clearly understands the actions you expect her to take, and what she can expect from you if she does not comply."
            him surprised "And that will make her do what I want?"
            naomi sad "Not at first. But here is the key: you have to be willing to follow through with the consequences you set without getting angry."
            him concerned "Why shouldn't I get angry?"
            naomi normal "You want to teach her to control her emotions, correct?"
            him determined "Yes..."
            naomi happy "A child's most influential teacher is her parents' example. When you are in control of your emotions, you show her that that is the proper way to behave."
        "How do you make your kids get along?":
            him surprised "How do you make your kids get along?"
            naomi normal "First, do you really want to {b}make{/b} your kids get along? Or do you want to teach them how to get along?"
            him concerned "It doesn't seem like it should be that hard not to take someone's toys!"
            naomi sad "For them, it {b}is{/b} hard. This doesn't mean we excuse the behavior; they do need to learn how to share. But understanding this helps us be patient with them and remember to teach the right way."
            him determined "So what do you do if two kids aren't getting along?"
            naomi normal "Usually if they're not getting along, there is a problem. They need you to teach them how to solve that problem together."
            him concerned "I should have known it wouldn't be simple..."
            naomi happy "For example, if they both want to play with a toy at the same time, you could suggest several options -- taking turns, using a different toy, playing something else -- and let them discuss it."
            him determined "I don't think they would ever agree on a solution."
            naomi normal "Then perhaps neither can play with the toy until they both agree on how they will share it."
            him normal "Okay, I'll try that."
            naomi happy "Just try to remember to focus on solving problems together, not pointing fingers at each other."
            if (is_liaison):
                him determined "That's good advice for everyone."
                naomi normal "Yes, there is much overlap between parenting and leading a community."
                him normal "Thanks for the leadership training, Sister Naomi."
                naomi happy "You're welcome. You're doing a fine job, and I'm glad you are learning even more ways to lead people well."
        "What should you do when a kid disobeys?":
            him surprised "What should you do when a kid deliberately disobeys?"
            naomi happy "[kid_name] likes to do things her own way, doesn't she?"
            him determined "Yeah, so you know what I'm talking about."
            naomi normal "If you expect you may have trouble getting her to do something, you may want to decide on a logical consequence ahead of time."
            him surprised "Like what?"
            naomi normal "For example, you might tell her, 'I expect your room to be clean in two hours. If you choose not to clean your room before two hours is up, you will not be able to play with friends today.'"
            him determined "That sounds reasonable."
            naomi sad "Contrast this to what many parents end up saying, which is 'Clean your room now, or you'll be grounded for a month!'"
            him concerned "Yeah, and then when they don't clean their room you have to decide if you're really going to ground them for that long."
            naomi normal "You also need to make sure that she knows exactly what you want her to do, and has the necessary skills to accomplish it."
            him surprised "What do you mean?"
            naomi happy "Well, you wouldn't ask her to plow the fields without teaching her how, right?"
            him determined "Right..."
            naomi normal "Sometimes we forget that children also need to learn how to do simple things, like cleaning their room, or washing dishes, or putting away their laundry."
            him concerned "I guess no one's born knowing how to do those things..."
            naomi happy "And they will learn that best with lots of positive encouragement as they master each small step. It may sound silly to you to say, 'Thank you for putting your socks away,' but it is effective."
        "How do you talk to kids about sex?":
            him surprised "How do you talk to kids about sex?"
            naomi normal "How do you want your kids to feel about their bodies? About babies? About affection?"
            him determined "Well, those are all good things, I guess."
            naomi happy "Then let your conversation reflect that as you talk about the parts of human life they are ready to learn about."
            him surprised "How can you tell what they are ready for?"
            naomi normal "If they trust you and have a curious mind, they will ask you when they are ready to know something."
            him concerned "[kid_name] certainly has a curious mind..."
            naomi normal "You don't need to give lots of details -- just the facts that are most relevant to her. A toddler may just want to know the proper names for all the body parts. A child may wonder where babies come from. A teenager may want to know how to tell if you love someone."
            him concerned "My parents didn't talk to me much about those things."
            naomi sad "Then you may need some practice. If you seem embarrassed or upset that she is asking about sex, then she will not want to ask you in the future. You could start by talking to [her_name]."
            him surprised "Can't they just talk to [her_name] about it?"
            naomi normal "[kid_name] may want to know what you have to say."
            "That thought had never occurred to me before -- that when [kid_name] asked me a question, she didn't just want an answer, she wanted {b}my{/b} answer."

    naomi normal "That's all we have time for today."
    naomi happy "Thank you all for raising the next generation of humans! They need you and your love."
    return


label parenting_class1:
    scene community_center with fade
    show natalia normal at midright
    show him normal at midleft
    show helen normal at quarterright
    show her normal at quarterleft
    show ilian normal at left
    show sara normal at right
    show naomi normal at center
    with dissolve
    naomi happy "I'm so glad you all want to learn about being better parents."
    natalia "I mostly just have a problem with one kid."
    helen "How is this going to work when all our kids are such different ages?"
    naomi normal "Even for different ages of children, the principles are the same. I'll make sure to save time for specific questions and discussion at the end."
    naomi sad "What do you think is the most important thing a child needs? Think about it, and write down your answer."
    menu:
        "What does a child need most?"
        "To survive.":
            "I wrote 'Survival'."
            him determined "You can't do anything else if you're dead."
            naomi normal "That is true. What else?"
            helen "Love."
            natalia "Stability."
        "To be loved.":
            "I wrote 'Love'."
            him determined "If you feel loved and secure, you have the motivation to do anything else."
            naomi normal "Good, love is important. What else does a child need?"
            natalia "Survival is important, too. They need to be safe."
            helen "On Earth that might have been a given, but here..."
            naomi sad "True, parents are responsible for their children's survival!"
            him annoyed "They also need to learn how to be adults. Otherwise, what's the point?"
        "To learn.":
            "I wrote 'Learning'."
            him determined "The whole job of kids is to learn to be responsible adults. Without that, there's no point in having kids."
            naomi normal "Yes, I see. What else does a child need?"
            natalia "Survival, of course."
            helen "And love."
    naomi happy "Love is the vehicle through which we deliver a child's needs. Just love won't feed a child, or teach him to work hard. But we provide all these things with love."
    natalia "Not just feeling love, but doing the things your child needs most to grow."
    naomi sad "And if you try to teach these things without love, a child will not want to learn and will not feel safe making the mistakes he needs to make to learn."
    her surprised "Do we really want our kids to feel safe making mistakes? That sounds dangerous."
    naomi normal "As parents, part of your job is protect kids from making terrible, life-altering mistakes. But without making small mistakes, they will not learn for themselves."
    helen "I guess Travis could have never learned to walk without falling so many times."
    natalia "And Tomás could have never learned how to get along so well with his wife without having many disagreements with his siblings."
    naomi happy "Yes, exactly."

    "We talked for a while about being patient with kids' mistakes, and common mistakes for different ages. It was reassuring to learn things like wetting the bed and talking back were completely normal."

    call parenting_class_questions
    return

# This is year 14
label parenting_class2:
    scene community_center with fade
    show pete normal at quarterright    
    show natalia normal at midright
    show him normal at midleft
    show her normal at quarterleft
    show thuc normal at left
    show sara normal at right
    show naomi normal at center
    with dissolve

    naomi happy "Welcome to our parenting workshop!"
    naomi normal "I'd like us to start by thinking about one time when you felt like someone was a good parent to you. It doesn't have to be your actual parent. I'll go first and then I'd like to hear from you."
    naomi sad "My grandmother told me many stories. Sometimes they had a moral; sometimes they didn't. Sometimes they were about gods and spirits; sometimes they were about animals or mortals. Some were full of action and adventure, and others were full of loss and longing."
    naomi normal "As a child, I didn't even care what the stories were about. Just the fact that she cared about me enough to share a story made me happy."
    naomi "What about you?"
    natalia "I'll never forget the time I accidentally let all the turkeys out of our family's farm. I had no excuse; I stopped to talk to a friend and didn't close the gate. I was worried my Papa would be furious; so I thought I would lie and say my friend did it."
    natalia "When I told him, he looked at my face. Then he just said, 'Well, we better go get them.'"
    natalia "We chased them all day. I finally admitted that it was me, and he just nodded and we finally got all the turkeys home."
    naomi happy "Sounds like you could really trust your father. Would anyone else like to share?"
    menu:
        "Should I share?"
        "Share a story about my mom.":
            him normal "I don't have anything specific, but my mom could always sense when I was feeling down. We never talked about it, but she would make my favorite dinner, macaroni and cheese with bacon, and I'd know she was thinking about me."
            him happy "And she ended every day with a hug and an 'I love you.' Every day, no matter how old I was."
            naomi normal "She was very good at helping you feel loved."
        "Share a story about my dad.":
            him determined "My dad and I didn't always get along. He expected me to work hard and stay out of his way."
            him annoyed "He was so picky about the rows in the fields... mine never looked as straight as his. I tried, but I'd make one line a little crooked and then all the rest would follow."            
            him surprised "He never said anything, but when I finally managed to get a field perfectly straight, he placed a hand on my shoulder and nodded. I think that was the closest he ever came to saying, 'I love you'."
            naomi sad "His approval was important to you, wasn't it?"
            him concerned "Yeah... sometimes I wish I could show him everything I've made here. Other times I'm glad he can't see my failures!"

        "Don't share.":
            "I couldn't really think of anything specific."


    naomi happy "Thank you, everyone. Sometimes we focus so much on mistakes, but I think it's important to remember positive examples as well."
    call parenting_class_questions
    return