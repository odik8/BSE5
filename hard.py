#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def integral_sine(x, epsilon=1e-10):
    result = 0
    term = x
    n = 1

    # Вычисление ряда с учетом заданной точности
    while abs(term) > epsilon:
        result += term
        n += 2
        term *= -1 * (x**2) / (n * (n - 1))

    return result

if __name__ == "__main__":

    x = float(input("Введите значение x для вычисления Si(x): "))

    print(f"Значение Si({x}) = {integral_sine(x)}")
