#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
    try:
        user_input1 = int(input("Enter first number: "))
        user_input2 = int(input("Enter second number: "))
        user_input3 = int(input("Enter third number: "))

        if (user_input1 % 2 == 0) or (user_input2 % 2 == 0) or (user_input3 % 2 == 0):
            return True
        else:
            return False
    except:
        return "Enter a number please"


if __name__ == "__main__":
    print(main())
