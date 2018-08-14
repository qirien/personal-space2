# Plugin Poetry by Andrea Landaker is licensed CC-BY 4.0
# You can use this code as long as you credit Andrea Landaker.
# See http://creativecommons.org/licenses/by/4.0/
#
#
# To customize, create your own lists and tell the word_board to use them below.

init python:
    # Basic words that you probably want on every board.
    basic_nouns = ["word", "you", "she", "joy", "I", "we",  "scent", "sound", "me", "pain", "wonder", "dream"]
    basic_adjectives = ["beautiful", "blue", "gray", "red", "soft", "feathery",  "pink", "your", "my", "our", "orange", "this", "brown", "dry"]
    basic_verbs = ["jump", "know", "smile", "dance", "sing", "kick", "glow", "is", "are"]
    basic_other = ["in", "on", "after", "before", "for", "of", "and", "the", "-ing", "-ly", "!", "?", "-s", "every", "from", "around", "between", "-y", "a"]
    basic_words = Wordpack()
    basic_words.add_words(basic_nouns, basic_adjectives, basic_verbs, basic_other)

    # Family-related words
    family_nouns = ["hair", "family", "face", "father", "mother", "soul", "eye"]
    family_adjectives = ["young", "gentle", "old", "rosy", "happy", "personal", "bright", "clever", "jealous", "sweet"]
    family_verbs = ["touch", "feel", "grow", "build", "adore", "love", "nurture", "thank", "help", "frown", "sleep", "pout"]
    family_other = ["forever"]
    family_words = Wordpack()
    family_words.add_words(family_nouns, family_adjectives, family_verbs, family_other)

    # Baby-related words
    baby_nouns = ["blanket", "nose", "toe", "milk", "baby", "hand", "fist"]
    baby_adjectives = ["tiny", "cute", "tender", "tight", "precious", "chubby"]
    baby_verbs = ["cry", "hold", "babble", "cuddle", "yawn", "nap", "crawl", "whisper"]
    baby_other = ["oh"]
    baby_words = Wordpack()
    baby_words.add_words(baby_nouns, baby_adjectives, baby_verbs, baby_other)

    # Romance related words
    romance_nouns = ["body", "lips", "soul", "eyes", "legs", "hair", "scent", "baby", "honey", "marriage", "you", "skin", "chocolate", "wine", "sunset", "two", "smile", "heart", "lover", "friend"]
    romance_adjectives = ["smooth", "graceful", "sexy", "sweaty", "hot", "tender", "sparkly", "romantic", "my", "sweet", "crimson", "lonely", "awesome", "fabulous", "gorgeous", "beautiful", "best"]
    romance_verbs = ["sigh", "nibble", "caress", "kiss", "embrace", "taste", "soar", "dance", "entangle", "devour", "drink", "flutter", "hold", "murmur", "whisper"]
    romance_other = ["oh", "together", "with", "alone", "just", "always"]
    romance_words = Wordpack()
    romance_words.add_words(romance_nouns, romance_adjectives, romance_verbs, romance_other)

    # Farm-related words
    farm_nouns = ["breakfast", "sunrise", "plant", "flower", "seed", "fire", "light", "water", "earth", "air", "planet", "space", "fruit", "harvest", "grass", "dirt", "sky", "sunset", "moon", "weed"]
    farm_adjectives = ["simple", "slow", "green", "sharp", "alive", "dead", "brittle"]
    farm_verbs = ["soar", "grow", "build", "help", "cut", "wrench", "dig"]
    farm_other = ["yum", "ugh"]
    farm_words = Wordpack()
    farm_words.add_words(farm_nouns, farm_adjectives, farm_verbs, farm_other)

label make_poem:
    $ word_board.generate_display_words()
    call screen plugin_poetry(word_board)
    return
