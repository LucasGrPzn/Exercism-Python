from operator import mod


def convert(number):
    sounds = [(3, "Pling"), (5, "Plang"), (7, "Plong")]
    sound = ""

    for divisor, pl_sound in sounds:
        if mod(number, divisor) == 0:
            sound += pl_sound

    if not sound:
        return str(number)
    return sound
