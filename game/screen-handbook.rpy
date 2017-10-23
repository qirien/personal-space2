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
