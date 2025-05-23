VERIF_DIGIT = '0123456789x'


def is_valid(isbn: str) -> bool:
    isbn = isbn.replace('-', '').lower()
    
    if len(isbn) != 10 or isbn[-1] not in VERIF_DIGIT:
        return False
    
    if not isbn[:9].isdigit():
        return False
    
    sum = 0
    for index, mult in enumerate(range(10, 0, -1)):
        try:
            sum += int(isbn[index]) * mult
        except ValueError:
            sum += 10 * mult

    if sum % 11 == 0:
        return True
    return False
