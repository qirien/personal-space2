##
# CREDITS

# TODO: include CGs here as photos? maybe a jellysquid image?
label credits:
    # TODO: Different music? If we don't end up getting a special song, maybe https://lonepeakmusic.bandcamp.com/track/made-in-liverpool
    play music maintheme


    window hide
    scene black with fade
    $ skippable = not persistent.times_beaten

    show credits01 at tilted, right, driftdown, smallphoto
    show text "Credits" with dissolve
    $ renpy.pause(2.0, hard=skippable)
    hide text with dissolve

    show credits02 at tilted, left, driftdown, smallphoto
    show text "Designed and Written By\n\nAndrea Landaker\n\nRachel Helps" with dissolve
    $ renpy.pause(4.0, hard=skippable)
    hide text with dissolve

    show credits03 at tilted, right, driftdown, smallphoto
    show text "Character Art and Cutscene Graphics By\n\nClarissa Helps" with dissolve
    $ renpy.pause(4.0, hard=skippable)
    hide text with dissolve

    show credits04 at tilted, left, driftdown, smallphoto
    show text "Testing by\n\nWes Landaker\nSapphire Landaker" with dissolve # TODO: Add other testers
    $ renpy.pause(2.0, hard=skippable)
    hide text with dissolve

    if ((total_miners >= total_colonists) and (total_miners >= total_mavericks)):
        show credits05-miners at tilted, right, driftdown, smallphoto
    elif ((total_mavericks >= total_colonists) and (total_mavericks >= total_miners)):
        show credits05-mavericks at tilted, right, driftdown, smallphoto
    else:
        show credits05-colonists at tilted, right, driftdown, smallphoto

    show text "With music by\n\nKen Bonfield\nRay Montford\nJeff Wahl\n\nAmfibia\nBlue Wave Theory\nEhren Starks\nGled Bledsoe\nChristos Anestopoulos\nAmbient Teknology\n\nLicensed by {a=http://www.magnatune.com}Magnatune{/a}\n\nAlso featuring {a=https://bit.ly/2xNM03K}LonePeakMusic{/a}" with dissolve
    $ renpy.pause(5.0, hard=skippable)
    hide text with dissolve

    show credits06 at tilted, left, driftdown, smallphoto
    show text "Backgrounds based on images by\nLisa Horner\nMike Soprano\nWes Landaker\nAndrea Landaker\nKuruzovich\nMarcus Budde"
    $ renpy.pause(5.0, hard=skippable)
    
    show credits07 at tilted, right, driftdown, smallphoto    
    show text "{a=http://www.flickr.com}Flickr{/a} users:\nMr. Gray\nNASA\nAlbuquerque South Broadway Cultural Center\nPresidencia de la República Mexicana\nFormlabs Inc.\ngavin rice\nWilliam Klos\n\nAnd {a=http://www.pixabay.com}Pixabay{/a} users:\nShannon Anderson\nJacqueline Macou\nSabine van Erp\nShibang\nHumusak\nEmslichter\nMilt Ritter\nStockSnap\nDavid Mark\nhifijohn\nFree-Photos\nStockSnap"
    $ renpy.pause(5.0, hard=skippable)
    hide text with dissolve

    if (faction_strong(total_mavericks) and faction_strong(total_miners)):
        show credits08-miners-mavericks at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_miners)):
        show credits08-miners at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_mavericks)):
        show credits08-mavericks at tilted, left, driftdown, smallphoto
    else:
        show credits08-colonists at tilted, left, driftdown, smallphoto
    show text "GUI graphics based on images by\nNoto Emoji\n\nAnd Pixabay users:\nOpenClipart-Vectors\nClker-Free-Vector-Images\n\nPublic Domain Sound Effects from {a=http://www.freesound.org}FreeSound.org{/a}\nOther SFX from {a=http://www.soundjay.com}Soundjay{/a}"
    $ renpy.pause(5.0, hard=skippable)

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

    return