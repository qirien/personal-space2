label interscene_text(year=0, event_type="Work"):
    window hide
    scene stars with fade
    show text "{size=36}Year [year]\n\n[event_type]{/size}" at slideinpausefade
    $ renpy.pause(2.0)
    return

# TODO: Delete this if we end up not using it.
screen interscene(year=0, event_type="Work"):
    style_prefix "interscene"
    window:
        vbox:
            label "Year [year] of [MAX_YEARS]"
            label "[event_type]"

# Pop down and fadein (thanks PyTom!)
transform credits_popdown():
    xalign 0.98 ypos 30

    # When it's shown, slide it down and fade it in.
    on show:
        yoffset -15.0  alpha 0.0
        easein 0.5 yoffset 0.0 alpha 1.0

    # When it's hidden, slide it down and fade it out.
    on hide:
        easeout 0.5 yoffset 15.0 alpha 0.0

# Pop down a little screen that shows when your credits change
screen show_credits(amount=0):
    hbox:
        at credits_popdown
        $ credits_icon = STAT_ICON_BASE + "value.png"
        frame:
            xpadding 10
            ypadding 10
            background "roundrect_lightgray"
            text "{image=" + credits_icon + "} [amount]" size 30

    timer 3 action Hide("show_credits")

# Show a summary of changes for the previous year
# TODO: abstract out computer pad stuff somehow
# TODO: Do we really  need a separate screen for this? Or can we put it on the computer pad screen somewhere? In the parenting manual?
screen yearly_summary():
    key "K_RETURN" action Return()
    key "K_SPACE" action Return()
    style_prefix "plan_farm"
    frame:
        background  "computer_pad_with_screen"
        # TODO: make wallpaper that you can change? Unlock wallpaper pictures as you play the game?
        text "User [his_name] has logged on." size 12 xalign 0.1 ypos 30 color "#fff"
        textbutton "?" xpos 1077 ypos 18 action Jump("farm_tutorial")
        textbutton "             " xpos 1085 ypos 18 action ShowMenu("preferences")
        vbox:
            area (60, 50, 1150, 620)
            yfill True
            hbox:
                xfill True
                yfill True
                frame:
                    yfill True
                    background "roundrect_darkgray"
                    vbox:
                        hbox:
                            frame:
                                xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH
                                ysize TOP_SECTION_HEIGHT
                                style "plan_farm_subframe"
                                hbox:
                                    vbox:
                                        xsize 200
                                        xalign 1.0
                                        label "Year [year] Summary"
                                        null height 10
                                        text notifications
                                        # TODO: include community stats here?
                                    $ parenting_style = get_parenting_style()
                                    # TODO: add in expressions based on parenting style, attachment, competence, independence
                                    $ kid_type = get_kid_type()
                                    add "family_photo_small " + kid_type

                            frame:
                                xsize RIGHT_COLUMN_WIDTH
                                ysize TOP_SECTION_HEIGHT
                                style "plan_farm_subframe"
                                vbox:
                                     label "Quote"
                                     null height 10
                                     text parenting_quotes[year]
                        frame:
                            xsize LEFT_COLUMN_WIDTH + MIDDLE_COLUMN_WIDTH + RIGHT_COLUMN_WIDTH
                            style "plan_farm_subframe"
                            vbox:
                                xfill True
                                textbutton "Continue":
                                     style "round_button"
                                     xalign 0.5
                                     action Return()

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
    background Frame("gui/textbox.png", left=35, right=35, top=35, bottom=35)

style interscene_label is label
style interscene_label_text is label_text:
    color "#fff"
