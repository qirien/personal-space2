# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
#
# To customize, create your own lists and tell the word_board to use them below.

init python:
    # Basic words that you probably want on every board.
    basic_nouns = ["word", "you", "she", "joy", "I", "we",  "scent", "sound", "me", "pain", "wonder", "dream"]
    basic_adjectives = ["beautiful", "blue", "gray", "crimson", "soft", "feathery",  "pink", "your", "my", "our", "orange", "this", "brown", "dry"]
    basic_verbs = ["jump", "know", "smile", "dance", "sing", "kick", "glow", "is"]
    basic_other = ["in", "on", "after", "before", "for", "of", "and", "the", "-ing", "-ly", "!", "?", "-s", "every", "from", "around", "between", "-y"]
    basic_words = Wordpack()
    basic_words.add_words(basic_nouns, basic_adjectives, basic_verbs, basic_other)

    # Family-related words
    family_nouns = ["blanket", "hair", "nose", "toe", "family", "face", "milk", "father", "mother", "baby", "soul"]
    family_adjectives = ["tiny", "young", "gentle", "old", "rosy", "happy", "personal", "bright", "clever", "cute", "chubby", "jealous", "tender", "tight", "precious", "sweet"]
    family_verbs = ["touch", "feel", "cry", "hold", "grow", "build", "adore", "love", "babble", "cuddle", "nurture", "thank", "help", "frown", "yawn"]
    family_other = ["forever", "oh"]
    family_words = Wordpack()
    family_words.add_words(family_nouns, family_adjectives, family_verbs, family_other)

    # Farm-related words
    farm_nouns = ["breakfast", "sunrise", "plant", "flower", "seed", "fire", "light", "water", "earth", "air", "planet", "space", "fruit", "harvest", "grass", "dirt"]
    farm_adjectives = ["simple", "slow", "green", "sharp", "alive", "dead", "brittle"]
    farm_verbs = ["soar", "grow", "build", "help", "cut", "wrench"]
    farm_other = ["yum"]
    farm_words = Wordpack()
    farm_words.add_words(farm_nouns, farm_adjectives, farm_verbs, farm_other)

label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board)
    return
