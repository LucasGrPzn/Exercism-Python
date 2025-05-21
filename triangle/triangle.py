def is_triangle(sides):
    if zero_side(sides):
        return False
    
    a, b, c = sides
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    return False


def zero_side(sides):
    if 0 in sides:
        return True
    return False


def equilateral(sides: list) -> bool:
    if is_triangle(sides):
        a, b, c = sides

        if a == b == c:
            return True
    return False


def isosceles(sides: list) -> bool:
    if is_triangle(sides):
        a, b, c = sides

        if a == b or a == c or b == c:
            return True
    return False


def scalene(sides: list) -> bool:
    if is_triangle(sides):
        a, b, c = sides

        if a != b != c != a:
            return True
    return False
