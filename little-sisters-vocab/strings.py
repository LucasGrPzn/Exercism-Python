"""Functions for creating, transforming, and adding prefixes to strings."""


def add_prefix_un(word: str):
    """Take the given word and add the 'un' prefix.

    :param word: str - containing the root word.
    :return: str - of root word prepended with 'un'.
    """

    new_word = "un" + word
    return new_word


def make_word_groups(vocab_words: list) -> str:
    """Transform a list containing a prefix and words into a string with the prefix followed by the words with prefix prepended.

    :param vocab_words: list - of vocabulary words with prefix in first index.
    :return: str - of prefix followed by vocabulary words with
            prefix applied.

    This function takes a `vocab_words` list and returns a string
    with the prefix and the words with prefix applied, separated
     by ' :: '.

    For example: list('en', 'close', 'joy', 'lighten'),
    produces the following string: 'en :: enclose :: enjoy :: enlighten'.
    """

    prefix = vocab_words[0]
    new_vocab_words = []
    new_vocab_words.append(prefix)

    for index, word in enumerate(vocab_words):
        if index == 0:
            continue
        new_vocab_words.append(prefix + word)

    return " :: ".join(new_vocab_words)


def remove_suffix_ness(word: str): 
    """Remove the suffix from the word while keeping spelling in mind.

    :param word: str - of word to remove suffix from.
    :return: str - of word with suffix removed & spelling adjusted.

    For example: "heaviness" becomes "heavy", but "sadness" becomes "sad".
    """

    new_word = word[:-4]
    
    if new_word.endswith("i"):
        return new_word.replace("i", "y")
    return new_word


def adjective_to_verb(sentence: str, index: int) -> str:
    """Change the adjective within the sentence to a verb.

    :param sentence: str - that uses the word in sentence.
    :param index: int - index of the word to remove and transform.
    :return: str - word that changes the extracted adjective to a verb.

    For example, ("It got dark as the sun set.", 2) becomes "darken".
    """

    new_sentence = sentence.replace(".", "")
    sentence_list = new_sentence.split()

        
    return sentence_list[index] + "en"
