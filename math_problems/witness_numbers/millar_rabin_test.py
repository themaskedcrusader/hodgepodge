witness_numbers = [2, 3, 5, 7, 11]


def _get_dress_number(number_to_dress):
    ret = (number_to_dress - 1) / 2
    while ret % 2 == 0:
        ret = ret / 2
    return ret


def _is_prime(number_to_test, witness):
    dress = _get_dress_number(number_to_test)
    modulo = number_to_test
    testimony = witness
    loop = 1
    while loop < dress:
        testimony = (testimony * witness) % modulo
        loop += 1
    return testimony == 1 or testimony + 1 == number_to_test


def is_prime(number_to_test):
    for witness in witness_numbers:
        if not _is_prime(number_to_test, witness):
            return False
    return True


def is_prime_two(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

