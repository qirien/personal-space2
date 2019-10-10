screen plugin_poetry(board):
    $ display_words = board.get_display_words()
    $ nouns = display_words.get_nouns()
    $ adjectives = display_words.get_adjectives()
    $ verbs = display_words.get_verbs()
    $ other = display_words.get_other()
    frame:
        style_prefix "pp"
        xfill True
        yfill True
        background "bg/stars.png"
        frame:
            xpadding 50
            yfill True
            vbox: # Poem, then words
                vbox: # Title, then poem
                    xfill True
                    spacing 5
                    label "New Poem" text_size 50 xalign 0.5
                    hbox:
                        spacing 20
                        xalign 0.5
                        textbutton "Reset" action Confirm("Delete this poem?", Reset(board, True))
                        textbutton "Done" action Confirm("Are you done with this poem?", [FinishPoem(board), Return()])
                    hbox: # Poem lines
                        spacing 2
                        vbox:
                            yalign 0.5
                            spacing 10
                            textbutton "▲" action PreviousLine(board) sensitive(board.current_line>=1) size_group "nav_buttons"
                            textbutton "×" action Confirm("Delete line?", Reset(board, False)) size_group "nav_buttons"
                            textbutton "▼" action NextLine(board) sensitive(board.current_line< (board.MAX_LINES-1)) size_group "nav_buttons"
                        vbox:
                            for i in range(0, board.MAX_LINES):
                                hbox:
                                    spacing 2
                                    null height 35
                                    if (i < len(board.poem)):
                                        if (i == board.current_line):
                                            label "→"
                                        for j in range(0, len(board.poem[i])):
                                            textbutton board.poem[i][j] action DeleteWord(board,j)
                hbox:
                    spacing 20
                    xfill True
                    vbox:
                        yalign 0.5
                        spacing 10

                        # TODO: this doesn't work anymore.
                        #textbutton "+" action renpy.curried_invoke_in_new_context(textinput) size_group "nav_buttons"
                        textbutton "↔" action ShuffleWordLists(board) size_group "nav_buttons"
                    vbox:
                        label "Nouns"
                        vpgrid:
                            cols board.NOUN_COLUMNS
                            for i in range(0, len(nouns)):
                                textbutton nouns[i] action AddWord(board, nouns[i]) size_group "word"

                    vbox:
                        label "Adjectives"
                        vpgrid:
                            cols board.ADJECTIVE_COLUMNS
                            for i in range(0, len(adjectives)):
                                textbutton adjectives[i] action AddWord(board, adjectives[i]) size_group "word"

                    vbox:
                        label "Verbs"
                        vpgrid:
                            cols board.VERB_COLUMNS
                            for i in range(0, len(verbs)):
                                textbutton verbs[i] action AddWord(board, verbs[i]) size_group "word"

                    vbox:
                        label "Other"
                        vpgrid:
                            cols board.OTHER_COLUMNS
                            for i in range(0, len(other)):
                                textbutton other[i] action AddWord(board, other[i]) size_group "word"

init python:
    def nextline(board):
        board.nextline()
        renpy.restart_interaction()
    NextLine = renpy.curry(nextline)

    def previousline(board):
        board.previousline()
        renpy.restart_interaction()
    PreviousLine = renpy.curry(previousline)

    def addword(board, word):
        board.addword(word)
        renpy.restart_interaction()
    AddWord = renpy.curry(addword)

    def deleteword(board, index):
        board.deleteword(index)
        renpy.restart_interaction()
    DeleteWord = renpy.curry(deleteword)

    def reset(board, fullReset=False):
        board.reset(fullReset)
        renpy.restart_interaction()
    Reset = renpy.curry(reset)

    # Reselect words for lists
    def shuffle_word_lists(board):
        global display_words
        board.generate_display_words()
        display_words = board.get_display_words()
        renpy.restart_interaction()
        return

    ShuffleWordLists = renpy.curry(shuffle_word_lists)

    def textinput():
        new_word = renpy.input("Word?")
        addword(board, new_word)
        return
    # curried up above so we can call it in a new context

    def finishpoem(board):
        board.finish_poem()
        return
    FinishPoem = renpy.curry(finishpoem)
