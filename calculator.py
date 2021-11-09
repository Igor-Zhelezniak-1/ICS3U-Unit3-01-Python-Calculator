#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is calculator


def main():
    # This is calculator
    # input

    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))

    # process
    total = first + second

    # output
    print("{0} + {1} = {2}".format(first, second, total))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
