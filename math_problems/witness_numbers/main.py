from millar_rabin_test import is_prime_two


def test_is_prime(number_to_test):
    print(f'{number_to_test} is...')
    if not is_prime_two(number_to_test):
        print("NOT")
    else:
        print("IS")
    print("prime!")


if __name__ == '__main__':
    test_is_prime(58543)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
