# These are messages that appear on the colony message board each month

screen message_board:
    default side_image = None
    
    add "images/bg/stars.jpg"
    add "gui/computer pad.png"
    window:
        style "nvl_window"
        xpadding 50
        ypadding 50

        yfill True
        xfill True

        has vbox:
            style "nvl_vbox"
        $ num_messages = len(dialogue)
        text "{b}Messages{/b}"
        vbox:
            # Display dialogue.
            for who, what, who_id, what_id, window_id in dialogue:
                window:
                    id window_id

                    has vbox:
                        # The author of the message
                        vbox:
                            xpos 30
                            xalign 0.0
                            if who is not None:
                                text who id who_id
                        # The message
                        vbox:
                            xpos 87
                            ypos -20  # put it up next to the icon
                            xmaximum 830
                            xalign 0.0
                            text what id what_id
                
# TODO: redo these with new colors, make icons, etc.                            
# NVL mode characters for chat rooms, etc
define her_c = DynamicCharacter("her_name", who_prefix = "{image=images/icons/her-icon.png} ", 
    color="#84b766", image="her", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # green of her eyes
define him_c = DynamicCharacter("his_name", who_prefix = "{image=images/icons/him-icon.png} ",
    color="#bc1e0e", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # red of his eyes
define naomi_c = Character("Naomi Grayson", who_prefix = "{image=images/icons/naomi-icon.png} ", 
    color="#bf98ff", image="naomi", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lavender
define pavel_c = Character("Mayor Pavel Grayson", who_prefix = "{image=images/icons/pavel-icon.png} ", 
    color="#cccccc", image="pavel_c", kind=nvl, ctc="ctc_blink", ctc_position="nestled")   #gray
define lily_c = Character("Dr. Lily Kealoha", who_prefix = "{image=images/icons/lily-icon.png} ", 
    color="#7580d0", image="lily", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #grayish blue
define sara_c = Character("Sara Andrevski", who_prefix = "{image=images/icons/sara-icon.png} ", 
    color="#e25057", image="sara", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  # salmon pink
define thuc_c = Character("Thuc Nguyen", who_prefix = "{image=images/icons/thuc-icon.png} ", 
    color="a9ff22", image="thuc", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian_c = Character("Ilian Andrevski", who_prefix = "{image=images/icons/ilian-icon.png} ", 
    color="d2d099", image="ilian", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #khaki
define brennan_c = Character("Brennan Callahan", who_prefix = "{image=images/icons/brennan-icon.png} ", 
    color="33b533", image="brennan", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #irish green
define pete_c = Character("Pete Jennings", who_prefix = "{image=images/icons/pete-icon.png} ", 
    color="ee7755", image="pete", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia_c = Character("Natalia Perón", who_prefix = "{image=images/icons/natalia-icon.png} ", 
    color="f3ca14", image="natalia", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen_c = Character("Helen Jennings", who_prefix = "{image=images/icons/helen-icon.png} ", 
    color="77b8ef", image="helen", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #sky blue
define julia_c = Character("Julia Nguyen", who_prefix = "{image=images/icons/julia-icon.png} ", 
    color="#e7b1cb", image="julia", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #icy pink
define martin_c = Character("Martín Perón", who_prefix = "{image=images/icons/martin-icon.png} ", 
    color="#9b5b1d", image="martin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #brown
define miranda_c = Character("Miranda Perón", 
    #who_prefix = "{image=images/icons/miranda-icon.png} ", 
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow

define computer = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")
