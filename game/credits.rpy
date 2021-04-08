##
# CREDITS

label credits:
    window hide
    scene black with fade
    $ skippable = not persistent.times_beaten

    show text "Credits" with fade
    $ renpy.pause(2.0, hard=skippable)
    hide text with fade

    show text "Designed and Written By\n\nAndrea Landaker\n\nRachel Helps" with fade
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade

    show text "Character Art by Clarissa Helps" with fade
    $ renpy.pause(2.0, hard=skippable)
    hide text with fade

    show text "Testing by\n\nWes Landaker\nSapphire Landaker" with fade
    $ renpy.pause(2.0, hard=skippable)
    hide text with fade

    show text "With music by\n\nKen Bonfield\nRay Montford\nJeff Wahl\n\nAmfibia\nBlue Wave Theory\nEhren Starks\nChristos Anestopoulos\nAmbient Teknology\n\nUsed with permission from {a=http://www.magnatune.com}Magnatune{/a}" with fade
    $ renpy.pause(4.0, hard=skippable)
    hide text with fade

    show text "Backgrounds based on images by\nLisa Horner\nMike Soprano\nDorothea Witter-Rieder\nMarcus Budde\nMr. Gray\nNASA\nAlbuquerque South Broadway Cultural Center\nPresidencia de la República Mexicana\nFormlabs Inc.\nAndrea Landaker\nWes Landaker"
    $ renpy.pause(3.0, hard=skippable)
    
    show text "And {a=http://www.pixabay.com}Pixabay{/a} users:\nShannon Anderson\nJacqueline Macou\nSabine van Erp\nShibang\nHumusak\nEmslichter\nMilt Ritter\nStockSnap\nDavid Mark\nhifijohn\nFree-Photos\nStockSnap"
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade

    show text "GUI graphics based on images by\nNoto Emoji\n\nAnd Pixabay users:\nOpenClipart-Vectors\nClker-Free-Vector-Images"    
    $ renpy.pause(2.0, hard=skippable)
    # TODO: add more credits from Credits.txt SFX?

    show text "Space to Grow was made using the following tools:\n\nthe GIMP (gimp.org)\nCodeOSS (code.visualstudio.com)\njEdit (jedit.org)\nLunaPic (www.lunapic.com)\nAudacity (audacityteam.org)\nCelestia (celestia.space)\ngit (github.com)" with fade
    $ renpy.pause(4.0, hard=skippable)
    hide text with fade

    show text "and of course...\n\nRen'py\n{a=http://www.renpy.org}www.renpy.org{/a}" with fade
    $ renpy.pause(3.0, hard=skippable)
    hide text with fade

    # Set multi-persistent variables about this playthrough
    if not persistent.times_beaten:
        $ persistent.times_beaten = 1
    else:
        $ persistent.times_beaten += 1

    if renpy.variant('pc'):
        $ mp.jack_name = his_name
        $ mp.kelly_name = her_name
        $ mp.baby_name = kid_name
        $ mp.bro_name = bro_name
        $ mp.save()
    $ renpy.save_persistent()

    scene stars with fade
    show text "{size=140}{font=fonts/SP-Marker Font.otf}The End{/font}{/size}" with dissolve
    stop music fadeout 3.0
    $ renpy.pause(3.0, hard=skippable)

    "Thank you for playing Our Personal Space 2: Space to Grow!"
    "New Game+ unlocked! Bonus section unlocked!"
    # TODO: add link, survey, etc?

    $ renpy.full_restart()
