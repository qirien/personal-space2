# Wordpack class for Plugin Poetry
# A Wordpack is some nouns, adjectives, verbs, and other words
# You can combine Wordpacks with add_wordpacks
# You can trim a Wordpack to a certain size by randomly selecting that number of
# words with trim_to_size (destructive)

init -100 python:
    class Wordpack(renpy.store.object):
        NOUN_INDEX = 0
        ADJECTIVE_INDEX = 1
        VERB_INDEX = 2
        OTHER_INDEX = 3

        def __init__(self, wordpack = None):
            if (wordpack is None):
                self.nouns = []
                self.adjectives = []
                self.verbs = []
                self.other = []
            else:
                self.nouns = list(wordpack.get_nouns())
                self.adjectives = list(wordpack.get_adjectives())
                self.verbs = list(wordpack.get_verbs())
                self.other = list(wordpack.get_other())
            return

        def add_words(self, nouns, adjectives, verbs, other):
            self.nouns = list(nouns)
            self.adjectives = list(adjectives)
            self.verbs = list(verbs)
            self.other = list(other)
            return

        # Add all the words from all the wordpacks in args to this wordpack
        def add_wordpacks(self, wordpacks):
            for newwords in wordpacks:
                self.nouns       += newwords.get_nouns()
                self.adjectives  += newwords.get_adjectives()
                self.verbs       += newwords.get_verbs()
                self.other       += newwords.get_other()
            return

        def trim_to_size(self, size_tuple):
            import random
            # Uniquify lists
            self.nouns      = list(set(self.nouns))
            self.adjectives = list(set(self.adjectives))
            self.verbs      = list(set(self.verbs))
            self.other      = list(set(self.other))

            # Take a sample of the proper size
            self.nouns = random.sample(self.nouns, size_tuple[Wordpack.NOUN_INDEX])
            self.adjectives = random.sample(self.adjectives, size_tuple[Wordpack.ADJECTIVE_INDEX])
            self.verbs = random.sample(self.verbs, size_tuple[Wordpack.VERB_INDEX])
            self.other = random.sample(self.other, size_tuple[Wordpack.OTHER_INDEX])

            # Sort words
            self.nouns.sort()
            self.adjectives.sort()
            self.verbs.sort()
            self.other.sort()

            return

        def get_nouns(self):
            return self.nouns

        def get_adjectives(self):
            return self.adjectives

        def get_verbs(self):
            return self.verbs

        def get_other(self):
            return self.other
