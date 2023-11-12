#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiplication_table(n):
    print("  ", end='\t')
    for i in range(1, n + 1):
        print(f'{i}', end='\t')
    print("\n----------------------------------------")

    for i in range(1, n + 1):
        print(f'{i} |', end='\t')
        for j in range(1, n + 1):
            print(f'{i * j}', end='\t')
        print()


if __name__ == "__main__":
    n = 9
    multiplication_table(n)
