def classify(number: int) -> str:
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    
    if number < 1 or type(number) != int:
        raise ValueError("Classification is only possible for positive integers.")

    factors = []
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)

    sum_factors = sum(factors)

    if sum_factors == number:
        return "perfect"
    
    if sum_factors > number:
        return "abundant"
    
    return "deficient"
