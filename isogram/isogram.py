def is_isogram(string: str) -> bool:
    string = string.replace('-', '').lower()
    string = string.replace(' ', '')

    for i, letter in enumerate(string):
        if not string.find(letter, i + 1) == -1:
            return False
    return True
