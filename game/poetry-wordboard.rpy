# Board class for PluginPoetry
# A Board has wordpacks, poems, and information about the current poem.
# It has a size for wordpacks, and a maximum number of poems.

init -100 python:
    class Board(renpy.store.object):
        if renpy.mobile:
            MAX_LINE_SIZE = 6
            MAX_LINES = 3
            MAX_POEMS = 30
        else:
            MAX_LINE_SIZE = 8
            MAX_LINES = 5
            MAX_POEMS = 50

        if renpy.mobile:
            NOUN_COLUMNS = 2
            ADJECTIVE_COLUMNS = 2
            VERB_COLUMNS = 2
            OTHER_COLUMNS = 1
        else:
            NOUN_COLUMNS = 3
            ADJECTIVE_COLUMNS = 3
            VERB_COLUMNS = 2
            OTHER_COLUMNS = 2

        if renpy.mobile:
            MAX_ROWS = 7
        else:
            MAX_ROWS = 10
        MAX_NOUNS = NOUN_COLUMNS * MAX_ROWS
        MAX_VERBS = VERB_COLUMNS * MAX_ROWS
        MAX_ADJECTIVES = ADJECTIVE_COLUMNS * MAX_ROWS
        MAX_OTHER = OTHER_COLUMNS * MAX_ROWS

        def __init__(self, *args):
            self.poems = []
            self.poem = [[]]
            self.current_line = 0
            self.wordpacks = list(args)
            self.generate_display_words()
            return

        def set_wordpack(self, *args):
            self.wordpacks = list(args)
            return

        # Generates a Wordpack of the proper size to display, with
        # words from all the wordpacks given to this board.
        def generate_display_words(self):
            self.display_words = Wordpack()
            self.display_words.add_wordpacks(self.wordpacks)
            self.display_words.trim_to_size([Board.MAX_NOUNS, Board.MAX_ADJECTIVES, Board.MAX_VERBS, Board.MAX_OTHER])
            return

        def get_display_words(self):
            return self.display_words

        def add_poem(self, poem):
            self.poems.append(poem)
            return

        def nextline(self):
            self.current_line += 1
            if (self.current_line >= len(self.poem)):
                self.poem.append([])
            return

        def previousline(self):
            self.current_line -= 1
            if (self.current_line < 0):
                self.current_line = 0
            return

        def line_full(self):
            if (len(self.poem[self.current_line]) >= self.MAX_LINE_SIZE):
                return True
            else:
                return False

        def addword(self,word):
            if (word[0] == "-"): # if we have a suffix, add on to last word
                # special case -ing onto a word ending with 'e'
                if (len(self.poem[self.current_line]) > 0):
                    if ((self.poem[self.current_line][-1][-1] == "e") and (word == "-ing")):
                        self.poem[self.current_line][-1] = self.poem[self.current_line][-1][0:-1] + word[1:]
                    else:
                        self.poem[self.current_line][-1] += word[1:]
            else:
                self.poem[self.current_line].append(word)
            return

        def deleteword(self,line, index):
            del self.poem[line][index]
            return

        def reset(self, fullReset):
            if (fullReset):
                self.poem = [[]]
                self.current_line = 0
            else:
                self.poem[self.current_line] = []
            return

        def finish_poem(self):
            self.poems.append(self.poem)
            self.poem = [[]]
            self.current_line = 0
            return

        def get_poem_as_string(self, index=0):
            poem_string = ""
            if ((len(self.poems) >= index) and (len(self.poems) > 0)):
                for poem_line in self.poems[index]:
                    poem_string += " ".join(poem_line)
                    poem_string += "\n"

            return poem_string.rstrip()

        # TODO: change wordpacks?
