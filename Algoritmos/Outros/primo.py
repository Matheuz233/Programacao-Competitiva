def is_prime(number):
    if number <= 1:
        return 0

    for x in range(2, number):
        if not number % x:
            return 0
    return 1