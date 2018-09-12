# These are messages that appear on the colony message board each year

label message1:
    nvl clear
    naomi_c "Congratulations to Sara and Ilian on the birth of their son Oleg!"
    him_c "I don't know whether to congratulate you or commiserate with you..."
    sara_c "Maybe both? :-D"
    nvl clear
    return

# TODO: redo these with new colors, make icons, etc.
# NVL mode characters for chat rooms, etc
define her_c = DynamicCharacter("her_name", who_suffix = "  {image=images/icons/her-icon.png} ",
    color="#84b766", image="her", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # green of her eyes
define him_c = DynamicCharacter("his_name", who_suffix = "  {image=images/icons/him-icon.png} ",
    color="#bc1e0e", image="him", kind=nvl, ctc="ctc_blink", ctc_position="nestled") # red of his eyes
define naomi_c = Character("Naomi", who_suffix = "  {image=images/icons/naomi-icon.png} ",
    color="#bf98ff", image="naomi", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lavender
define pavel_c = Character("Pavel", who_suffix = "  {image=images/icons/pavel-icon.png} ",
    color="#cccccc", image="pavel_c", kind=nvl, ctc="ctc_blink", ctc_position="nestled")   #gray
define lily_c = Character("Dr. Lily", who_suffix = "  {image=images/icons/lily-icon.png} ",
    color="#7580d0", image="lily", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #grayish blue
define sara_c = Character("Sara", who_suffix = "  {image=images/icons/sara-icon.png} ",
    color="#e25057", image="sara", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  # salmon pink
define thuc_c = Character("Thuc", who_suffix = "  {image=images/icons/thuc-icon.png} ",
    color="a9ff22", image="thuc", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #lime green
define ilian_c = Character("Ilian", who_suffix = "  {image=images/icons/ilian-icon.png} ",
    color="d2d099", image="ilian", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #khaki
define brennan_c = Character("Brennan", who_suffix = "  {image=images/icons/brennan-icon.png} ",
    color="33b533", image="brennan", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #irish green
define pete_c = Character("Pete", who_suffix = "  {image=images/icons/pete-icon.png} ",
    color="ee7755", image="pete", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #rusty brown
define natalia_c = Character("Natalia", who_suffix = "  {image=images/icons/natalia-icon.png} ",
    color="f3ca14", image="natalia", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define helen_c = Character("Helen", who_suffix = "  {image=images/icons/helen-icon.png} ",
    color="77b8ef", image="helen", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #sky blue
define julia_c = Character("Julia", who_suffix = "  {image=images/icons/julia-icon.png} ",
    color="#e7b1cb", image="julia", kind=nvl, ctc="ctc_blink", ctc_position="nestled") #icy pink
define martin_c = Character("Martín", who_suffix = "  {image=images/icons/martin-icon.png} ",
    color="#9b5b1d", image="martin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #brown
define miranda_c = Character("Miranda",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define lewis_c = Character("Mr. Lewis",
    color="f3ca14", image="miranda", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow
define zaina_c = Character ("Zaina",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="zaina", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kevin_c = Character ("Kevin",
    #who_suffix = "  {image=images/icons/miranda-icon.png} ",
    color="f3ca14", image="kevin", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now
define kid_c = DynamicCharacter ("kid_name",
    #who_suffix = "  {image=images/icons/kid-icon.png} ",
    color="#e361ef", image="kid", kind=nvl, ctc="ctc_blink", ctc_position="nestled")  #yellow; copied from Miranda for now

define computer = Character(None, kind=nvl, ctc="ctc_blink", ctc_position="nestled")
