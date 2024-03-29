##
# CREDITS

label credits:
    play music maintheme

    window hide
    scene black with fade

    show credits01 at tilted, right, driftdown, smallphoto
    show text "Credits" with dissolve
    $ renpy.pause(2.0)
    hide text with dissolve

    show credits02 at tilted, left, driftdown, smallphoto
    show text "Designed and Written by\n\nAndrea Landaker\n\nRachel Helps" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    show credits03 at tilted, right, driftdown, smallphoto
    show text "Character Art and Cutscene Graphics by\n\nClarissa Helps\n\n\nAdditional Art by\n\nInes Ben Najem\nMike Soprano" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve    

    show credits04 at tilted, left, driftdown, smallphoto
    show text "Testing by\n\nWes Landaker\nSapphire Landaker\nPatricia Tan\nAlessio Capurro\nMaud Recover\nAnthony Fonteno\nMilo\nSheila Rombauts\nCatherine White\nLisa Horner" with dissolve
    $ renpy.pause(4.0)
    hide text with dissolve

    if ((total_miners >= total_colonists) and (total_miners >= total_mavericks)):
        show credits05-miners at tilted, right, driftdown, smallphoto
    elif ((total_mavericks >= total_colonists) and (total_mavericks >= total_miners)):
        show credits05-mavericks at tilted, right, driftdown, smallphoto
    else:
        show credits05-colonists at tilted, right, driftdown, smallphoto

    if jellypeople_happy:
        show jellysquid4 at tilted, left, driftdown, flip

    show text "With music by\n\nKen Bonfield\nRay Montford\nJeff Wahl\n\nAmfibia\nBlue Wave Theory\nEhren Starks\nGled Bledsoe\nChristos Anestopoulos\nAmbient Teknology\nJustin St-Pierre\n\nLicensed from {a=http://ilicensemusic.com/}iLicenseMusic{/a}\n\nAlso featuring {a=https://bit.ly/2xNM03K}LonePeakMusic{/a} and {a=https://incompetech.com}Kevin MacLeod{/a}" with dissolve
    $ renpy.pause(5.0)
    hide text with dissolve

    show credits06 at tilted, left, driftdown, smallphoto
    show text "Backgrounds based on images by\nLisa Horner\nMike Soprano\nWes Landaker\nAndrea Landaker\nKuruzovich\nMarcus Budde"
    $ renpy.pause(5.0)
    
    show credits07 at tilted, right, driftdown, smallphoto    
    show text "{a=http://www.flickr.com}Flickr{/a} users:\nMr. Gray\nNASA\nAlbuquerque South Broadway Cultural Center\nPresidencia de la República Mexicana\nFormlabs Inc.\ngavin rice\nWilliam Klos\n\nAnd {a=http://www.pixabay.com}Pixabay{/a} users:\nShannon Anderson, Jacqueline Macou\nSabine van Erp, Shibang\nHumusak,Emslichter\nMilt Ritter, StockSnap\nDavid Mark, hifijohn\nFree-Photos"
    $ renpy.pause(5.0)
    hide text with dissolve

    if (faction_strong(total_mavericks) and faction_strong(total_miners)):
        show credits08-miners-mavericks at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_miners)):
        show credits08-miners at tilted, left, driftdown, smallphoto
    elif (faction_strong(total_mavericks)):
        show credits08-mavericks at tilted, left, driftdown, smallphoto
    else:
        show credits08-colonists at tilted, left, driftdown, smallphoto
    show text "GUI graphics by Andrea Landaker\nResources include images by\nNoto Emoji\n\nAnd Pixabay users:\nOpenClipart-Vectors\nClker-Free-Vector-Images\n\nPublic Domain Sound Effects from {a=http://www.freesound.org}FreeSound.org{/a}\nOther SFX from {a=http://www.soundjay.com}Soundjay{/a}\n\nBaby voice acting by Petra Helps"
    $ renpy.pause(5.0)

    if (total_attachment < ATTACHMENT_HIGH):
        if (total_competence < COMPETENCE_HIGH):
            show credits09-left at tilted, right, driftdown, smallphoto
        else:
            show credits09-doctor at tilted, right, driftdown, smallphoto
    else:
        show credits09-home at tilted, right, driftdown, smallphoto

    show text "Space to Grow was made using the following tools:\n\nthe GIMP (gimp.org)\nCodeOSS (code.visualstudio.com)\njEdit (jedit.org)\nLunaPic (www.lunapic.com)\nAudacity (audacityteam.org)\nCelestia (celestia.space)\ngit (github.com)" with dissolve
    $ renpy.pause(5.0)
    hide text with dissolve
    
    show text "and of course...\n\nRen'py\n{a=http://www.renpy.org}www.renpy.org{/a}" with dissolve
    $ renpy.pause(6.0)
    hide text with dissolve

    return
