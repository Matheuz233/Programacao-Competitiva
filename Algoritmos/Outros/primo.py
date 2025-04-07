def is_prime(number):
    if number <= 1:
        return False
    for x in range(2, int(number**0.5) + 1):
        if number % x == 0:
            return False
    return True