# Child Development Tips
#
# For more information, see:
# https://www.cdc.gov/ncbddd/childdevelopment/positiveparenting/index.html

screen parenting_handbook():
    modal True
    zorder 1
    style_prefix "parenting"
    on "show" action [SetVariable("show_year", year), SetVariable("read_handbook", True)]
    key "x" action Hide("parenting_handbook")

    frame:
        xalign 0.5
        yalign 0.5
        vbox:
            hbox:
                label "Parenting Guide"
                textbutton "X":
                    xpos -52
                    xfill False
                    text_font "fonts/Questrial-Regular.otf"
                    text_bold True 
                    text_size 42
                    focus_mask None
                    action Hide("parenting_handbook", irisin) 
            hbox:
                null width 30
                vbox:
                    xsize LEFT_COLUMN_WIDTH-50
                    textbutton "General" selected (show_year < 0) action SetVariable("show_year", -1)
                    textbutton "Baby (0-1)" selected (0 <= show_year <= BABY_MAX) action SetVariable("show_year", BABY_MAX)
                    showif (year > BABY_MAX):
                        textbutton "Toddler (2-5)" selected (BABY_MAX < show_year <= TODDLER_MAX) action SetVariable("show_year", TODDLER_MAX)
                    showif (year > TODDLER_MAX):
                        textbutton "Child (6-9)" selected (TODDLER_MAX < show_year <= CHILD_MAX) action SetVariable("show_year", CHILD_MAX)
                    showif (year > CHILD_MAX):
                        textbutton "Tween (10-13)" selected (CHILD_MAX < show_year <= TWEEN_MAX) action SetVariable("show_year", TWEEN_MAX)
                    showif (year > TWEEN_MAX):
                        textbutton "Young Teen (14-15)" selected (TWEEN_MAX < show_year <= YTEEN_MAX) action SetVariable("show_year", YTEEN_MAX)
                    showif (year > YTEEN_MAX):
                        textbutton "Older Teen (16-18)" selected (YTEEN_MAX < show_year) action SetVariable("show_year", MAX_YEARS)
                null width 5
                vbox:
                    yalign 0.0
                    ysize 480
                    xsize MIDDLE_COLUMN_WIDTH-32
                    use kid_info

screen kid_info():
    tag kid_info
    if (show_year < 0):
        use general_info    
    elif (show_year <= BABY_MAX):
        use baby_info
    elif (show_year <= TODDLER_MAX):
        use toddler_info
    elif (show_year <= CHILD_MAX):
        use child_info
    elif (show_year <= TWEEN_MAX):
        use tween_info
    elif (show_year <= YTEEN_MAX):
        use yteen_info
    else:
        use teen_info

screen general_info():
    tag kid_info
    text childs_mind["general"] 
    
screen baby_info():
    tag kid_info
    text childs_mind["baby"] 

screen toddler_info():
    tag kid_info
    text childs_mind["toddler"]

screen child_info():
    tag kid_info
    text childs_mind["child"]

screen tween_info():
    tag kid_info
    text childs_mind["tween"]

screen yteen_info():
    tag kid_info
    text childs_mind["yteen"]

screen teen_info():
    tag kid_info
    text childs_mind["teen"]

###################################################################
# STYLES FOR PARENTING HANDBOOK
###################################################################

style parenting_frame is computer_sub_frame:
    xsize MIDDLE_COLUMN_WIDTH + LEFT_COLUMN_WIDTH + 48
style parenting_label is computer_sub_label
style parenting_label_text is computer_sub_label_text
style parenting_text is computer_sub_text:
    yalign 0.0
style parenting_vbox is computer_sub_vbox
style parenting_hbox is computer_sub_hbox

style parenting_button is computer_sub_button:
    xfill True
    selected_background green_dark
    padding (4,10)

style parenting_button_text is computer_sub_button_text:
    hover_color green_med
    selected_color white
    idle_color gray_light
    size 24