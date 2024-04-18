
# implementation of hand multiplication

# number1 and number2 should be strings. Used to multiply GIANT numbers. The return is a String representation of ans
def reverse(string):
    ret = ""
    for letter in string:
        ret = letter + ret
    return ret


def sum_all(products):
    #  reverse them all so we can work from ones to tens, etc
    length = 0
    for x in range(len(products)):
        products[x] = reverse(products[x])
        if len(products[x]) > length:
            length = len(products[x])

    ans = ""
    carry = "0"
    for place in range(length):
        place_ans = 0
        for number in products:
            if len(number) < place + 1:
                continue
            place_ans = place_ans + int(number[place])
        if "0" != carry:
            place_ans = place_ans + int(carry)
        ans = str(place_ans % 10) + ans
        carry = str(int(place_ans / 10))
    if 0 != int(carry):
        ans = str(carry) + ans

    return ans


def long_multiply(number1, number2):
    carry_digit = 0
    place = 0
    _number1 = reverse(number1)
    _number2 = reverse(number2)
    products = []
    for digit2 in _number2:
        ans = ""
        for digit1 in _number1:
            ones, carry_digit = multiply_digits(digit2, digit1, carry_digit)
            ans = ones + "" + ans
        if "0" != carry_digit:
            ans = carry_digit + ans
        if 0 != place:
            for x in range(place):
                ans = ans + "0"
        products.append(ans)
        place = place + 1
        carry_digit = 0

    return sum_all(products)


def long_power(base, exponent):
    product = long_multiply(base, base)
    for x in range(int(exponent) - 2):
        product = long_multiply(product, base)
    return product


# ret: (digit, carry)
def multiply_digits(digit1, digit2, carry):
    ans = int(digit1) * int(digit2)
    ans = ans + int(carry)
    return str(ans % 10), str((int(ans / 10)))


def long_factorial(number):
    ans = "1"
    for x in range(0, int(number)):
        ans = long_multiply(ans, str(x + 1))
    return ans

# print("REVERSE: {} is {}".format("abcde", reverse("abcde")))
# print("MULTIPLY_DIGITS: {} times {} is {}".format(2, 7, multiply_digits(2,7,0)))
#print("LONG_MULTIPLY: {} times {} is {}".format("585432662833464866585432662833464866", "585432662833464866585432662833464866", long_multiply("585432662833464866585432662833464866", "585432662833464866585432662833464866")))
#print("     - EXPECTED ANSWER:       {}".format(585432662833464866585432662833464866*585432662833464866585432662833464866))
#print("LONG_POWER: {} to the power of {} is {}".format(216, 216, long_power("216", "216")))
print("LONG_FACTORIAL: {} factorial is {}".format(2000, long_factorial(2000)))

