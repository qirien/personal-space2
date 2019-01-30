# Child Development Manual
#
# Write wiki-style like this:
# https://patreon.renpy.org/wiki.html
#
# Include information from this:
# https://www.cdc.gov/ncbddd/childdevelopment/positiveparenting/index.html

screen parenting_handbook:
    modal True
    zorder 1
    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            label "Parenting Handbook"
            hbox:
                vbox:
                    label "Table of Contents"
                    textbutton "Infant (0-1)"
                    textbutton "Toddler (2-3)"
                    textbutton "Preschooler (4-5)"
                    textbutton "Young Child (6-8)"
                    textbutton "Tween (9-11)"
                    textbutton "Young Teen (12-14)"
                    textbutton "Teenager (15-18)"
                vbox:
                    label "Infant"
                    text "Development\nNeeds"
            textbutton "Return" yalign 1.0 action Hide("parenting_handbook")

$ inside_the_mind = [
["baby", "My world is small -- my family, blanket, and milk. So when something goes wrong it's like my whole world is collapsing! That's why I cry so much. I am learning so much every day, but it probably seems slow to my parents. I'm learning to focus my vision, touch and grab things, make sounds and decode their meaning, and who I can trust to take care of me. Soon I'll even move my whole body and understand a little of what you are saying, and make sounds that mean things. Please be patient with me and show me a lot of love; I'm learning as fast as I can!"],
["toddler", "Now that I'm crawling and walking, my world is so much bigger! There's new foods, new faces, and new sensations every day. All this stuff is old to you, but to me it's all new -- the sound of a spoon on a pot, or the touch of sand, or the funny look on your face when I blow a raspberry. I want to do things myself but I am still clumsy and learning, so please help me explore safely and teach me even when it takes a long time for me to learn. I don't understand water, fire, electricity, or poison so help me be safe from these dangerous things while letting me explore as much as possible!"],
["preschooler", "I am learning how to do even cooler things! I can hop on one foot and name colors and sort toys! I have a great imagination and can benefit from playing with other kids and talking to lots of different people. I am still learning about politeness and what behavior is okay for different situations. I love rules because then I know what to do, but I get mad if other people don't follow them! Sometimes I think I can do things I can't really do yet, so help me improve my skills while still watching me. I am learning how to decide some things for myself, so please help me learn to make good choices by letting me decide some things!"],
["child", "I can do a lot of things that you can do! I can learn complex skills like doing math, playing sports, and making crafts. I am starting to think more about other people and what will happen in the future, but I'm not very good at it yet. Friends are important to me, but sometimes I don't get along with other people, so help me learn how to be a good friend and fix my mistakes. Please support my growing independence by letting me do things for myself and giving me responsibilities!"],
["tween", "I am starting to think more abstractly. I am learning not just about what the world is, but why it is the way it is. When I was little, I thought I was the best person ever, but now I'm starting to see that I'm not. Please help me to recognize my strengths and deal with my weaknesses. What my friends think is becoming more important, but I still want to hear what you have to say. I might argue with you, but please be patient and love me and I'll think about what you say. My body is changing a lot now, too, and I'm starting to wonder what kind of person I want to be."],
["young teen", "I might be rude to you and push you away when you try to show me affection like you did when I was a kid. I don't want you to tell me what to do. I will probably make some stupid choices and be hard on myself. Usually I don't need you to rescue me, but I need you to support and love me no matter what. I need to separate myself from you as I'm learning independence, so my words, appearance, music, and friends might seem really strange! Please be interested in me and my world without trying to rule over it, and keep loving me and setting limits to protect me while I'm learning."],
["young adult", "I often have difficult questions, and I don't want easy answers. I am really thinking about these things and looking at a lot of different perspectives. If you listen to me, I will show you the same respect and hear what you have to say. If you are rude or try to tell me what to do, I will go somewhere else for answers. I want to find things out for myself. I'm learning about how to love and be a good friend and be on my own, and a lot of my emotions are still very strong. Please recognize my feelings and help me prepare to live on my own."]
]
