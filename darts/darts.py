from math import sqrt

RADIUS_INNER_CIRCLE = 1
RADIUS_MIDDLE_CIRCLE = 5
RADIUS_OUTER_CIRCLE = 10


def score(x, y):

    # calculates the distance from the center of the circle
    distance = sqrt(abs(x) ** 2 + abs(y) ** 2)
    
    # dart in the inner circle
    if distance <= RADIUS_INNER_CIRCLE:
        return 10
    
    # dart in the middle circle
    if distance <=  RADIUS_MIDDLE_CIRCLE:
        return 5
    
    # dart in the outer circle
    if distance <=  RADIUS_OUTER_CIRCLE:
        return 1
    
    # dart outside the target
    return 0
