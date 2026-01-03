#!/usr/bin/python3

import sys

"""
INITIAL HYPOTHESIS:
    landing at 0 as well as hitting it during a rotation counts
    intuition tells me any time we wrap around, we go past 0
    so we might just need to also compute the integer division to count the wraps

    e.g.

    START 50
    L500:
        we will hit zero 5 times because we will loop around 5 times
            side note: if we land at 0, counting both that as well as the modulo output
            will result in a duplicate zero; maybe we can fix with a if (curr != 0) check

            anyway,
        as per part 1,
        l new = (100 + curr - rot) % 100

        100 + 50 - 500 % 100 = -50; this shouldn't be negative!

        abs(-50) = 50 <------ should add absolute value

        if we take integer div by 100 of that same thing,

        (100 + 50 - 500) // 100 = -3.5 rotations, so 3 rotations
        but we are doing 5

        seems like we just need to modulo the amount of the rotation:

        500 // 100 = 5 wrap arounds

HAND TESTING:
    START 50
    L68:
        68 // 100 = 0, but we DO point at 0 because it overflows...
        this fails!

REVISING HYPOTHESIS:
    what if we just treat the change as positive-only?
    that is, we add for both left and right to compute our int division

    50 + 68 = 118 // 100 = 1
    zeros += 1

    this seems like it could work!

RETESTING:

START 50
    L68:
        50 + 68 = 118 // 100 = 1 wrap, OK
        (100 + 50 - 68) % 100 = 82, OK

START 95:
    R60:
        95 + 60 = 155 // 100 = 1, OK

REVISED HYPOTHESIS:
    extra_zeros = curr + abs(rotation) // 100

EDGE CASE: REPEATED ZEROS

START 0
    L500:
        we will hit 0 a total of 5 times, including the final land
        does our math hold?

        0 + 500 // 100 = 5; zeros += 5
        curr = 0, so zeros += 1 <--- duplicate!

FINAL HYPOTHESIS:
    extra_zeros = (curr + abs(rotation)) // 100
    zeros += extra_zeros

    if we land at a 0 and we have any extra zeros:
        zeros -= 1
    else:
        zeros += 1

ISSUE:
    
"""

if len(sys.argv) != 2:
    exit(0)
input_filename = sys.argv[1]

print(f"input file: {input_filename}")

with open(input_filename, "r") as _input, open("output.txt", "w") as _output:
    zeros = 0  # amount of times we've hit 0
    curr = 50  # starts by pointing at 50
    for line in _input:
        line = line.strip()
        if not line:  # reach this when parsing ends
            break

        _dir = line[0]
        _rot = int(line[1:])

        if _dir == "L":
            curr = (100 + curr - _rot) % 100
        else:
            curr = (curr + _rot) % 100

        # add zero if we wrap
        extra_zeros = (curr + _rot) // 100  # amount of times we wrapped
        zeros += extra_zeros
        # FIXME: This approach is wrong^

        # add zero if we land on it
        if curr == 0 and extra_zeros == 0:
            zeros += 1

        _output.write(f"{_dir}, {_rot}, {curr}, {zeros} ({extra_zeros})\n")
    _output.write(f"ZEROS: {zeros}\n")
