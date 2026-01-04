#!/usr/bin/python3

import sys

"""
initial hypothesis:
    if l, curr - rot
    if curr - rot < 0, l = 100 + (curr - rot) where curr - rot < 0
    if r, curr + rot
    if curr + rot > 99, r = 100 - (curr + rot) where curr + rot > 99
does it work?
    start:
        50
    l68:
        50 - 68 = -18; underflow
        100 - 18 = 82
    l30:
        82 - 30 = 52; ok
    r48:
        52 + 48 = 100; overflow
        100 - (52 + 48) = 0
    l5:
        0 - 5 = -5; underflow
        100 + (-5) = 95

logic is working, time to test!
outcome: it failed; breaks when rotating over a value > 100
revising hypothesis:

e.g.
start 50
l 500
50 - 500 = -450; underflow
100 + -450 = -550 which is still underflowing

if we rotate by 100 we end up at same spot
if we rotate by 500 we also end up at same spot

there are 100 positions

end should be 50

implement wrap around; modulo/division

e.g. start 50
r 568

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

start 50

l68:
    new = (100 + 50 - 68) % 100 = 82
l30:
    new = (100 + 82 - 30) % 100 = 52

seems fine, test time
yup this was it!
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

        # these are interchangeable because a direction doesn't have an inherent meaning

        if curr == 0:
            zeros += 1

        # _output.write(f"{_dir}, {_rot}, {curr}, {zeros}\n")
    _output.write(f"ZEROS: {zeros}\n")
