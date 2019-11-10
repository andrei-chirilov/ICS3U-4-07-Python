#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: November 2019
# print integers from 1000 to 2000 with 5 integers per line


def main():
    counter = 1

    for numbers in range(1000, 2000):
        counter += 1
        if counter % 5 == 1:
            print("{} ".format(numbers))
        else:
            print("{} ".format(numbers), end="")


if __name__ == "__main__":
    main()
