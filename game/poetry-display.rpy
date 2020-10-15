##
# This is the screen that shows all the poems you've made.
##

# Computer variant
screen poem_display(poem, take_photo=True):
    variant "large"
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        use show_poem(poem, take_photo)

# mobile variant
screen poem_display(poem, take_photo=True):
    frame:
        style_prefix "pps"
        xfill True
        yfill True
        xalign 0.5 
        yalign 0.5
        use show_poem(poem, take_photo)

# Show one poem in the middle, nice and large
screen show_poem(poem, take_photo=True):
    # Make it so you can click anywhere to proceed
    if (take_photo):
        key "mousedown_1" action [Function(take_picture), Hide("poem_display", whitefade)]
    else:        
        key "mousedown_1" action Hide("poem_display")                

    frame:
        xalign 0.5 
        yalign 0.5
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            for i in range(0, len(poem)):
                hbox:
                    xalign 0.5
                    spacing 5
                    for j in range(0, len(poem[i])):
                        textbutton poem[i][j] text_size 40


screen poetry_display(board, call_return=False):
    variant "large"
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "#000"
        use p_display(board, call_return)

# mobile variant
screen poetry_display(board, call_return=False):
    frame:
        style_prefix "pps"
        xfill True
        yfill True
        background "#000"
        use p_display(board, call_return)

screen p_display(board, call_return=False):
    frame:
        #background None
        left_padding 100
        right_padding 50
        ypadding 50
        yfill True
        hbox:
            xfill True
            vbox:
                viewport:
                    xsize 800
                    mousewheel True
                    draggable True
                    scrollbars "vertical"
                    vbox:
                        spacing 30
                        for count in range(0, len(board.poems)):
                            hbox:                                
                                spacing 30
                                yalign 0.5
                                vbox:
                                    spacing 5
                                    imagebutton auto "gui/twitter_%s.png" action TweetPoem(board.poems[count]) tooltip "Share this poem on Twitter" 
                                    textbutton " × " action Confirm("Delete this poem?", DeletePoem(board, count)) tooltip "Delete this poem" xalign 0.5
                                    # TODO: Add action to edit poem: textbutton " ✎ " action 
                                vbox:
                                    spacing 5
                                    for i in range(0, board.MAX_LINES):
                                        hbox:
                                            spacing 5
                                            if (i < len(board.poems[count])):
                                                for j in range(0, len(board.poems[count][i])):
                                                    textbutton board.poems[count][i][j] action Show("poem_display", dissolve, board.poems[count], False) tooltip "Show only this poem"

            vbox:
                xalign 0.8
                spacing 5
                null height 50
                textbutton "Add New Poem" action Show("plugin_poetry", irisout, word_board, False) sensitive (len(board.poems) < board.MAX_POEMS) tooltip "Add another poem"
                #textbutton "Change Wordpacks" action Jump("change_wordpacks") tooltip "Add another poem with a different set of words"
                if (not renpy.mobile):
                    textbutton "Screenshot" action Screenshot() tooltip "Take a screenshot, saved in this game's directory"
                if (call_return):
                    textbutton "Done" action Return() tooltip "Done with Poems"
                else:
                    textbutton "Done" action Hide("poetry_display", irisin) tooltip "Done with Poems"
                null height 50

                fixed:
                    xsize 200
                    $ tooltip = GetTooltip()
                    if tooltip:
                        text tooltip italic True

init python:
    def delete_poem(board, poem_number):
        board.poems.remove(board.poems[poem_number])

    DeletePoem = renpy.curry(delete_poem)

    def tweet_poem(poem):
        import webbrowser, urllib
        pp_url = urllib.quote("https://www.metasepiagames.com/PluginPoetry")
        pp_poem = urllib.quote(stringify(poem))
        webbrowser.open_new("http://twitter.com/intent/tweet?text=" + pp_poem + "&hashtags=PluginPoetry&url=" + pp_url)

    TweetPoem = renpy.curry(tweet_poem)

    # Take a 2d array of a poem and turn it into a string
    def stringify(poem):
        poem_string = ""
        for i in range(0, len(poem)):   
            for j in range(0, len(poem[i])):
                poem_string += poem[i][j]
                poem_string += " "
            poem_string += "\n"
        
        return poem_string.strip()

style pd_button_text is button_text:
    size 16
