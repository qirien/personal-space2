screen poetry_display(board):
    frame:
        style_prefix "pp"
        xfill True
        yfill True
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
                                                textbutton board.poems[count][i][j] action Confirm("Delete this poem?", DeletePoem(board, count))

                vbox:
                    xalign 0.8
                    spacing 5
                    #textbutton "Add New Poem" action Jump("make_poem") sensitive (len(board.poems) < board.MAX_POEMS)
                    textbutton "Screenshot" action Screenshot()
                    textbutton "Share"
                    textbutton "Done" action Confirm("Are you done with your poems?", Return())

init python:
    def delete_poem(board, poem_number):
        board.poems.remove(poems[poem_number])

    DeletePoem = renpy.curry(delete_poem)

style pd_button_text is button_text:
    size 16
