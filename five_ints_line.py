#!/usr/bin/env python3
# Created by: Patrick Tumbaga
# Created on: 11/28/2025
# This program prints integers from 1000 to 2000, five per line.

def main():
    print("This program prints integers from 1000 to 2000, five per line.")

    for number in range(1000, 2001):
        # Print the number with a space, end="" keeps it on the same line
        print(number, end=" ")

        # Check if we have printed 5 numbers on the current line
        if (number - 999) % 5 == 0:
            print()  # Move to the next line after every 5 numbers

if __name__ == "__main__":
    main()
