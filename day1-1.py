#!/usr/bin/python3

import sys

"""
INITIAL HYPOTHESIS:

if l, curr - rot
if curr - rot < 0, l = 100 + (curr - rot) where curr - rot < 0
if r, curr + rot
if curr + rot > 99, r = 100 - (curr + rot) where curr + rot > 99

TESTING:

START:
    50
L68:
    50 - 68 = -18; underflow
    100 - 18 = 82
L30:
    82 - 30 = 52; OK
R48:
    52 + 48 = 100; overflow
    100 - (52 + 48) = 0
L5:
    0 - 5 = -5; underflow
    100 + (-5) = 95

logic is working, time to test!

OUTCOME: IT FAILED; breaks when rotating over a value > 100

REVISING HYPOTHESIS:

e.g.
START 50
L 500
50 - 500 = -450; underflow
100 + -450 = -550 which is still underflowing

if we rotate by 100 we end up at same spot
if we rotate by 500 we also end up at same spot

there are 100 positions

end should be 50

IMPLEMENT WRAP AROUND; MODULO/DIVISION

e.g. START 50
R 568

should really be 50 + 68 since the 500 rotations will just wrap

568 mod 100 = 68
50 + 68 = 118 mod 100 = 18
ends up pointing at 18

568 + 50 = 618
618 mod 100 = 18

revised hypothesis:

if r:
    new = curr + rot % 100
if l:
    new = (100 + curr - rot) % 100
        must add 100 to account for wrapping below 0

testing:

START 50

L68:
    new = (100 + 50 - 68) % 100 = 82
L30:
    new = (100 + 82 - 30) % 100 = 52

SEEMS FINE, TEST TIME

Yup this was it!
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

        if curr == 0:
            zeros += 1

        _output.write(f"{_dir}, {_rot}, {curr}, {zeros}\n")
    _output.write(f"ZEROS: {zeros}\n")
