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

    # When it's hidden, slide it down and fade it out.
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
    timer 3 action Hide("show_notification")

# Show a summary of changes for the previous year
# TODO: abstract out computer pad stuff somehow
screen yearly_summary():
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    style_prefix "plan_farm"
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User {color=#888}[his_name]{/color} has logged on." size 12 xalign 0.1 ypos 30 color "#fff"
        textbutton "?" xpos 1076 ypos 16 style "computer_button" action Jump("farm_tutorial")
        textbutton "             " xpos 1085 ypos 16 style "computer_button"  action ShowMenu("preferences")
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
                                        xsize 200
                                        xalign 1.0
                                        #label "Year [year] Summary"
                                        #text notifications
                                        label "[kid_name]"
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
                                        
                                    $ kid_type = get_kid_type()
                                    add "family_photo_small " + kid_type xalign 1.0

                            frame:
                                #xsize RIGHT_COLUMN_WIDTH
                                ysize TOP_SECTION_HEIGHT
                                xalign 1.0
                                style "plan_farm_subframe"

                                vbox:
                                    label "Quote"
                                    hbox:
                                        null width 40
                                        text parenting_quotes[year]
                        frame:
                            #xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH + RIGHT_COLUMN_WIDTH
                            style "plan_farm_subframe"
                            vbox:
                                xfill True
                                textbutton "Continue":
                                     xalign 0.5
                                     action Return()

screen show_stat(var):
    vbox:
        spacing 0
        $ old_value = eval("total_" + var)
        $ delta = eval(var)
        $ max = eval(var.upper() + "_MAX") # TODO: or should we use _MAX? What about if 
        $ new_value = old_value + delta
        $ high_value = roundint(year * (eval(var.upper() + "_HIGH")/float(MAX_YEARS)))
        text var.capitalize()
        hbox:
            spacing 5
            #textbutton "{emoji=" + var + "}" tooltip var.capitalize()
            if (new_value >= high_value):
                bar value AnimatedValue(new_value, max, 0.7, old_value) style "summary_bar"
            else:
                bar value AnimatedValue(new_value, max, 0.7, old_value) style "summary_bar_low"
            #use tricolor_bar(high_value, old_value+delta, max, 200, CROP_LAYOUT_BAR_WIDTH*3, False)
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

