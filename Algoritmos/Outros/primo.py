def is_prime(number):
    if number <= 1:
        return False

    for x in range(2, number):
        if not number % x:
            return False
    return True