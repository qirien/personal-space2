###############################################################################
# Code for screens that go inbetween scenes.
# This includes the "interscene" screen that shows the year and current phase,
# the "notification" popdown screen,
# as well as the "yearly_summary" screen at the end of each year.
###############################################################################

label interscene_text(year=0, event_type="Work"):
    window hide
    scene stars with fade
    show text "{size=36}Year [year]\n\n[event_type]{/size}" at slideinpausefade
    $ renpy.pause(2.0)
    return

# Pop down and fadein (thanks PyTom!)
transform popdown():
    xalign 0.98 ypos 30

    # When it's shown, slide it down and fade it in.
    on show:
        yoffset -15.0  alpha 0.0
        easein 0.5 yoffset 0.0 alpha 1.0

    # When it's hidden, slide it up and fade it out.
    on hide:
        easeout 0.5 yoffset -15.0 alpha 0.0

# Pop down a little screen that notifies the user about something interesting
# ...such as credits changing, parenting style, etc.
screen show_notification(message=""):
    hbox:
        at popdown
        frame:
            xpadding 10
            ypadding 10
            background "roundrect_lightgray"
            text message size 30
    timer 5.0 action Hide("show_notification")

# Show a summary of changes for the previous year
screen yearly_summary(endgame=False):
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    style_prefix "plan_farm"
    frame:
        background  "computer_pad_with_screen"
        text "User {color=#888}[his_name]{/color} has logged on." size 12 xalign 0.1 ypos 30 color "#fff"
        imagebutton auto "gui/computerpadbutton_%s.png" action ShowMenu("save") xpos 1233 yalign 0.5
        vbox:
            area (60, 50, 1150, 620)
            yfill True
            hbox:
                xfill True
                yfill True
                frame:
                    yfill True
                    xfill True
                    background "roundrect_darkgray"
                    vbox:
                        hbox:
                            frame:
                                xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH
                                ysize TOP_SECTION_HEIGHT
                                style "plan_farm_subframe"
                                hbox:
                                    spacing 10
                                    xfill True
                                    vbox:                                        
                                        xsize 230
                                        #xalign 1.0
                                        if (endgame):
                                            label "Farm"
                                            hbox:
                                                null width 30
                                                vbox: 
                                                    text "Size"
                                                    text "Credits"
                                                    text "Overworked"
                                                    text "Bad Nutrition"
                                                    text "Low Calories"
                                                    text "Kid Overworked"
                                                vbox:
                                                    text "[farm_size]" xalign 1.0 
                                                    text "[credits]" xalign 1.0
                                                    text "[overwork_count]" xalign 1.0
                                                    text "[bad_nutrition_count]" xalign 1.0
                                                    text "[low_calories_count]" xalign 1.0
                                                    text "[terra_overwork_count]" xalign 1.0
                                            null height 10
                                            label "Community"
                                            if is_liaison:
                                                text "Liaison:     [his_name]" xpos 30
                                            else:
                                                text "Liaison:     Sara" xpos 30
                                            if kevin_elected:
                                                text "Mayor:      Kevin" xpos 30
                                            else:
                                                text "Mayor:      Julia" xpos 30
                                            if (ban_firegrass):
                                                text "Firegrass: Banned" xpos 30
                                            else:
                                                text "Firegrass: Legal" xpos 30
                                            if (kevin_elected):
                                                text "Miners:   Can Vote" xpos 30
                                            else:
                                                text "Miners:   Cannot Vote" xpos 30
                                            $ playtime = round(renpy.get_game_runtime() / 60.0 / 60.0, 1)
                                            text "Game Time: [playtime] hours"
                                        else:
                                            hbox:
                                                label "[kid_name]"
                                                $ iconname = bios.getIconName("[kid_name]")
                                                add "images/icons/" + iconname + "-icon.png"
                                            hbox:
                                                null width 40
                                                vbox:
                                                    ysize 10
                                                    for var in ["attachment", "competence"]:
                                                        use show_stat(var)
                                            label "Factions"
                                            hbox:
                                                null width 40
                                                vbox:
                                                    if (year > PETE_LEAVES_YEAR):
                                                        for var in ["miners", "colonists", "mavericks"]:
                                                            use show_stat(var) 
                                                    else:
                                                        for var in ["miners", "colonists"]:  
                                                            use show_stat(var) 
                                        
                                    if (year <= BABY_MAX):
                                        $ kid_type = "baby"
                                    else:
                                        $ kid_type = get_kid_type()
                                    add "family_photo_small " + kid_type xalign 1.0

                            frame:
                                #xsize RIGHT_COLUMN_WIDTH
                                ysize TOP_SECTION_HEIGHT
                                xalign 1.0
                                style "plan_farm_subframe"

                                vbox:
                                    # Screen for at the end of the game
                                    if (endgame):
                                        $ strong_marriage = has_strong_marriage()
                                        $ boyfriend_name = get_boyfriend_name()
                                        $ parenting_style = get_parenting_style().capitalize()
                                        $ bff = strongest_faction().capitalize()
                                        $ adjective = get_kid_adjective().capitalize()
                                        $ att_percent = min(100, int(100.0*total_attachment/ATTACHMENT_MAX))
                                        $ com_percent = min(100, int(100.0*total_competence/COMPETENCE_MAX))
                                        # Info about Jack
                                        label "[his_name]"
                                        text "[parenting_style] parent" xpos 30
                                        if (total_colonists >= COLONISTS_HIGH):
                                            text "Colonists' Friend" xpos 30
                                        if (total_miners >= MINERS_HIGH):
                                            text "Miners' Friend" xpos 30
                                        if (total_mavericks >= MAVERICKS_HIGH):
                                            text "Mavericks' Friend" xpos 30
                                        if (jellypeople_happy):
                                            text "Jellypeople's Friend" xpos 30
                                        # Info about Kelly 
                                        if (strong_marriage):
                                            label "[her_name] {emoji=heart}"
                                        else:
                                            label "[her_name] {emoji=nutrition-half}"
                                        # Info about Terra          
                                        if (total_attachment >= ATTACHMENT_HIGH):
                                            label "[kid_name] {emoji=heart}"
                                        else:
                                            label "[kid_name] {emoji=nutrition-half}"
                                        text "Attachment: [att_percent]%" xpos 30
                                        text "Competence: [com_percent]%" xpos 30
                                        if (total_attachment < ATTACHMENT_HIGH):
                                            if (total_competence < COMPETENCE_HIGH):
                                                text "Occupation:   Drifter" xpos 30
                                            else:
                                                text "Occupation:   Med Student" xpos 30
                                        else:
                                            if (total_competence < COMPETENCE_HIGH):
                                                    text "Occupation:   Delivery Girl" xpos 30
                                            else:
                                                text "Occupation:   Xenologer" xpos 30
                                        if (boyfriend_name != ""):
                                            text "Boyfriend:      [boyfriend_name]" xpos 30
                                        # Info about Aeron
                                        if (total_attachment < ATTACHMENT_HIGH):
                                            label "[bro_name] {emoji=nutrition-half}"
                                        else:
                                            label "[bro_name] {emoji=heart}"
                                    else:
                                        label "Quote"
                                        hbox:
                                            null width 30
                                            text parenting_quotes[year]
                        frame:
                            #xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH + RIGHT_COLUMN_WIDTH
                            style "plan_farm_subframe"
                            vbox:
                                xfill True
                                if (endgame):
                                    textbutton "The End":
                                        xalign 0.5
                                        action Return() 
                                else:
                                    textbutton "Continue":
                                        xalign 0.5
                                        action Return()

screen show_stat(var):
    vbox:
        spacing 0
        $ old_value = eval("total_" + var)
        $ delta = eval(var)
        $ max = eval(var.upper() + "_MAX")
        $ new_value = old_value + delta
        $ high_value = roundint(year * (eval(var.upper() + "_HIGH")/float(MAX_YEARS)))
        text var.capitalize()
        hbox:
            spacing 5
            #textbutton "{emoji=" + var + "}" tooltip var.capitalize()
            #if (new_value >= high_value): - this would be to have red be low and green be high
            if (delta >= 0):
                bar value AnimatedValue(new_value, max, 0.7, old_value) style "summary_bar"
            else:
                bar value AnimatedValue(new_value, max, 0.7, old_value) style "summary_bar_low"
            if (delta != 0):
                if (delta < 0):
                    text str(delta) at delay_fadein color red_dark
                else:
                    text "+" + str(delta) at delay_fadein color green_dark


###############################################################################################################
# Transforms and styles used for these screens
###############################################################################################################

transform bg_crop:
    crop (306,22,675,680)

transform photo_scale:
    zoom photo_scale_factor

transform photo_kid_pos:
    anchor (0, 1.0)
    xpos -200
    ypos 680

style interscene_window is default:
    xalign 0.0
    yalign 0.0
    padding (45,45)

style interscene_label is label
style interscene_label_text is label_text:
    color "#fff"
    font gui.interface_font
    outlines [(1, black, 1, 1)]

style summary_bar:
    ysize 16
    yalign 0.5
    left_bar Frame(Solid(green_med))
    right_bar Frame(Solid(gray_light))

style summary_bar_low:
    ysize 16
    yalign 0.5
    left_bar Frame(Solid(red_med))
    right_bar Frame(Solid(gray_light))

