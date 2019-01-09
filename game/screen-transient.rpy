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

# TODO: Add a credits pop out and hide screen
screen show_credits(expense=0):
    window:
        hbox:
            label "Credits: [credits]"

style interscene_window is default:
    xalign 0.0
    yalign 0.0
    padding (45,45)
    background Frame("gui/textbox.png", left=35, right=35, top=35, bottom=35)

style interscene_label is label
style interscene_label_text is label_text:
    color "#fff"
