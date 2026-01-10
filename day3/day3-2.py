#!/usr/bin/python3

import sys

"""
OBJECTIVE:
    instead of forming largest joltage with 2 digits, we form it with 12!
BRAINSTORM:
    we should still start our chain at the max() and look in the latter half
    we need to find 11 more numbers
        this needs to be a chain of the 11 largest remaining values that are in order
    **brute force**
        get the overall max
            (for first max(), exclude the rightmost 11 values)
        get the 11 largest values in the latter half
        sort them from smallest to largest index

        could this break?

        i can't really think of any case where it could (brain hurts)
        but i have a feeling...

        i'm going to try it and see where it throws smoke!

        **update 1**

        yeah, this didn't work
        for something like:             818181911112111
            largest 11 by value are:    98821111111
            if we sort by index:        18181911112

            because the ones come first order-wise, they get turned on
            but the larger value is formed by turning on the 8's first

            WILL COME BACK LATER, BRAIN TOAST
"""

# collect input file name
if len(sys.argv) != 2:
    print("Did not receive input file name")
    exit(0)
input_filename = sys.argv[1]

print(f"Using input file '{input_filename}'")

with open(input_filename, "r") as _input, open("output.txt", "w") as _output:
    _total = 0
    for line in _input:
        line = line.strip()
        bank = [int(n) for n in str(line)]  # convert line into number array

        # find first max
        # exclude final 11 values
        max_index, max_val = max(enumerate(bank[:len(bank) - 11]), key=lambda n: n[1])

        # yank the largest 11 values from latter half
        bank = list(enumerate(bank))  # get index info
        latter_half = bank[max_index+1:]
        largest_11 = sorted(latter_half, key=lambda n: n[1], reverse=True)[:11]  # sort by value, not index

        print(f"Largest rem. 11 sorted by VALUE: {''.join(str(n[1]) for n in largest_11)}")

        # sort these 11 values by ascending index
        largest_11 = sorted(largest_11, key=lambda n: n[0])  # sort by index this time

        print(f"Largest rem. 11 sorted by INDEX: {''.join(str(n[1]) for n in largest_11)}")

        # prepend the max to get joltage
        joltage = str(max_val) + ''.join(str(n[1]) for n in largest_11)
        print(f"The joltage is {joltage}")
