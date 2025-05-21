def steps(number):
    if number < 1:
        raise ValueError('Only positive integers are allowed')
    steps_to_one = 0

    while number != 1:
        if number % 2 == 0:
            number /= 2
            steps_to_one += 1
            print(number)

        else:
            number = number * 3 + 1
            steps_to_one += 1
            print(number)
    
    return steps_to_one
