#!/usr/bin/python3

import sys

"""
number = joltage of a single battery
line = bank
need to power 2 batteries per bank

joltage of bank is individual joltage numbers stitched together
    e.g.
    if bank is 123 and we turn on 1 and 2, the bank's joltage is 12
    digits cannot be rearranged!
        if we wish for joltage of 32, we can't because we'd have to flip 3 and 2

OBJECTIVE:
        find largest joltage each bank can produce
        sum up the joltages of each bank to find an answer
    TRANSLATION:
        find the largest 2 numbers that make the greatest value
    RESTRICTIONS:
        * numbers must be in order
        * only TWO batteries may be turned on per bank (i.e. find 2 largest sequential nums)

BRAINSTORMING:
    sorting is out the window because we can't rearrange digits

    **a brute force approach**
        1. find the largest number in the bank (max())
        2. find the second largest number in the 2nd half of the bank (split at the num found above)
            no need to do the 1st half since that breaks order

        time comp:
            max() on step 1 -> o(n)
            max() on step 2 -> o(n)

            this gives o(n + n) = o(2n) = o(n)

        let's try this!

    **update 1**
        it fails when the max is at the end of the list
        since there's nothing after it, we can't make a value of 2
        to solve this, we could just exclude this value when looking for the first max
        this ensures that we can use it to form a larger value, but we don't use it to start forming a value
        e.g.
            811119
            first max would be looked for in 81111; it would be 8
            second max would be looked for in whole bank, it would be 9
            max joltage: 89

    **update 2**
        THIS WORKS! onto part 2...
        we could optimize a bit with some algorithms maybe!
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

        # find max and its index
        # exclude final value when looking for first max
        max_joltage_index, max_joltage = max(enumerate(bank[:len(bank) - 1]), key=lambda n: n[1])

        # find second max on second half
        second_max_joltage = max(bank[max_joltage_index + 1:])

        # get joltage for this bank
        bank_max_joltage = int(f"{max_joltage}{second_max_joltage}")

        _output.write(f"Max joltage for bank {line} = {bank_max_joltage}\n")

        _total += bank_max_joltage
    _output.write(f"TOTAL JOLTAGE FOR ALL BANKS: {_total}\n")
