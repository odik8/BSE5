

import math


def integral_sine(x, eps=10 ** -10):
    result = 0
    term = x
    n = 1

    while abs(term) > eps:
        result += term
        term = (-1) ** n * x ** (2 * n + 1) / (math.factorial(2 * n + 1) * (2 * n + 1))
        n += 1

    return result


if __name__ == "__main__":
    user_input = float(input("Введите число x для нахождения Si(x): "))
    print(integral_sine(5))
