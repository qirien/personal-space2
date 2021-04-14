##
# CREDITS

# TODO: include CGs here! a jellysquid image?
label credits:
    window hide
    scene black with fade
    $ skippable = not persistent.times_beaten

    show credits01 at tilted, right, driftdown, smallphoto
    show text "Credits" with dissolve
    $ renpy.pause(2.0, hard=skippable)
    hide text with dissolve

    show credits02 at tilted, left, driftdown, smallphoto
    show text "Designed and Written By\n\nAndrea Landaker\n\nRachel Helps" with dissolve
    $ renpy.pause(3.0, hard=skippable)
    hide text with dissolve

    show credits03 at tilted, right, driftdown, smallphoto
    show text "Character Art by Clarissa Helps" with dissolve
    $ renpy.pause(2.0, hard=skippable)
    hide text with dissolve

    show credits04 at tilted, left, driftdown, smallphoto
    show text "Testing by\n\nWes Landaker\nSapphire Landaker" with dissolve
    $ renpy.pause(2.0, hard=skippable)
    hide text with dissolve

    if ((total_miners >= total_colonists) and (total_miners >= total_mavericks)):
        show credits05-miners at tilted, right, driftdown, smallphoto
    elif ((total_mavericks >= total_colonists) and (total_mavericks >= total_miners)):
        show credits05-mavericks at tilted, right, driftdown, smallphoto
    else:
        show credits05-colonists at tilted, right, driftdown, smallphoto

    show text "With music by\n\nKen Bonfield\nRay Montford\nJeff Wahl\n\nAmfibia\nBlue Wave Theory\nEhren Starks\nChristos Anestopoulos\nAmbient Teknology\n\nUsed with permission from {a=http://www.magnatune.com}Magnatune{/a}" with dissolve
    $ renpy.pause(4.0, hard=skippable)
    hide text with dissolve

    show credits06 at tilted, left, driftdown, smallphoto
    show text "Backgrounds based on images by\nLisa Horner\nMike Soprano\nDorothea Witter-Rieder\nMarcus Budde\nMr. Gray\nNASA\nAlbuquerque South Broadway Cultural Center\nPresidencia de la República Mexicana\nFormlabs Inc.\nAndrea Landaker\nWes Landaker"
    $ renpy.pause(5.0, hard=skippable)
    
    show credits07 at tilted, right, driftdown, smallphoto
    show text "And {a=http://www.pixabay.com}Pixabay{/a} users:\nShannon Anderson\nJacqueline Macou\nSabine van Erp\nShibang\nHumusak\nEmslichter\nMilt Ritter\nStockSnap\nDavid Mark\nhifijohn\nFree-Photos\nStockSnap"
    $ renpy.pause(4.0, hard=skippable)
    hide text with dissolve

    if (faction_strong(total_mavericks) and faction_strong(total_miners)):
        show credits08-miners-mavericks at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_miners)):
        show credits08-miners at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_mavericks)):
        show credits08-mavericks at tilted, left, driftdown, smallphoto
    else:
        show credits08-colonists at tilted, left, driftdown, smallphoto
    show text "GUI graphics based on images by\nNoto Emoji\n\nAnd Pixabay users:\nOpenClipart-Vectors\nClker-Free-Vector-Images"    
    $ renpy.pause(3.0, hard=skippable)
    # TODO: add more credits from Credits.txt SFX?

    if (total_attachment < ATTACHMENT_HIGH):
        if (total_competence < COMPETENCE_HIGH):
            show credits09-left at tilted, right, driftdown, smallphoto
        else:
            show credits09-doctor at tilted, right, driftdown, smallphoto
    else:
        show credits09-home at tilted, right, driftdown, smallphoto

    show text "Space to Grow was made using the following tools:\n\nthe GIMP (gimp.org)\nCodeOSS (code.visualstudio.com)\njEdit (jedit.org)\nLunaPic (www.lunapic.com)\nAudacity (audacityteam.org)\nCelestia (celestia.space)\ngit (github.com)" with dissolve
    $ renpy.pause(5.0, hard=skippable)
    hide text with dissolve
    
    show text "and of course...\n\nRen'py\n{a=http://www.renpy.org}www.renpy.org{/a}" with dissolve
    $ renpy.pause(6.0, hard=skippable)
    hide text with dissolve

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
