ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(sentence: str):

    for letter in ALPHABET:
        if not letter in sentence.lower():
            return False
    return True
