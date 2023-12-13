#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    try:
        n = int(input("Enter kW: "))
        payment = 0
        for i in range(1, n+1):
            if i <= 250: payment += 7
            elif 250 < i <= 300: payment += 17
            else: payment += 20 

        return payment
    except:
        return "Enter a positive integer"


if __name__ == "__main__":
    print(main())
