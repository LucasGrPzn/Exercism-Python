def is_armstrong_number(number: int):
    exponent = len(str(number))
    sum = 0
    for i in str(number):
        sum += int(i) ** exponent

    if sum == number:
        return True
    return False
