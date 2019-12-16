##
# This is the screen that shows all the poems you've made.
##

# Computer variant
screen poetry_display(board):
    variant "large"
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "#000"
        use p_display(board)

# mobile variant
screen poetry_display(board):
    frame:
        style_prefix "pps"
        xfill True
        yfill True
        background "#000"
        use p_display(board)

screen p_display(board):
    frame:
        xpadding 50
        ypadding 50
        yfill True
        hbox:
            xfill True
            vbox:
                spacing 20
                hbox:
                    label "Poems" text_size 50
                vbox:
                    spacing 30
                    for count in range(0, len(board.poems)):
                        vbox:
                            spacing 5
                            for i in range(0, board.MAX_LINES):
                                hbox:
                                    spacing 5
                                    if (i < len(board.poems[count])):
                                        for j in range(0, len(board.poems[count][i])):
                                            textbutton board.poems[count][i][j] action Confirm("Delete this poem?", DeletePoem(board, count)) tooltip "Delete this poem"

            vbox:
                xalign 0.8
                spacing 5
                null height 50
                textbutton "Add New Poem" action Jump("make_poem") sensitive (len(board.poems) < board.MAX_POEMS) tooltip "Add another poem with the same set of words"
                textbutton "Change Wordpacks" action Jump("change_wordpacks") tooltip "Choose different sets of words"
                textbutton "Screenshot" action Screenshot() tooltip "Take a screenshot, saved in this game's directory"
                textbutton "Save" action ShowMenu("save") tooltip "Save Game"
                textbutton "Done" action Confirm("Done with poems?", Return()) tooltip "Done with Poems"
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

style pd_button_text is button_text:
    size 16
