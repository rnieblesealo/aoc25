#!/usr/bin/python3

import sys

"""
if _dir == "L":
    curr = (100 + curr - _rot) % 100
else:
    curr = (curr + _rot) % 100

count anytime we hit 0 even if we don't land on it
when do we touch 0?
    wrapping around
    landing on 0
    starting on 0
how do we detect each?
    wrapping around:
        integer division: if start at 50 and go left 512, we wrap 5 times; 512 // 100 = 5
            this means we hit zero 5 times **while rotating**
            we then use the remainder in our previous identities and check if we land on 0
            (100 + 50 - 12) % 100 = 38
            we don't, so our total zeros are 5

            another case:
            start at 50, go left 582
            582 // 100 = 5 zeros
            582 % 100 = 82
            (100 + 50 - 82) % 100 = 68

            here, though we didn't land on 0, we crossed it: 50 - 82 = -32
            how can we detect this?
                check if curr - rot is negative or zero
                since it is, we landed/crossed 0 so we add it to our zeros
                we end up with a total of 6 zeros

            summarizing this logic:

            zeros += rot % 100 # count wraps

            if dir == L:
                l_rot = rot % 100
                if curr - l_rot <= 0:  # land on or cross zero
                    zeros += 1
                curr = (100 + curr - l_rot) % 100
            else:
                r_rot = rot % 100
                if curr + r_rot >= 100:  # land on or cross zero
                    zeros += 1
                curr = (curr + r_rot) % 100

            let's try it!

there is a problem when the current iteration starts at 0:
    a 0 start means that if curr + rot or curr - rot overflows, it will register the 0 again
    example:
        start at 0
        go left 5
        0 - 5 = -5 which registers as crossing 0

        **technically speaking** we did cross 0 because we started from it
        but we don't actually wish to count that again

        what can we do?
            **rule** starting at 0 guarantees that we will register at least one zero
            so, every time we start at 0, subtract a zero

        upon testing the above, we got one less zero than we expected

        there was a counterexample to the above **rule**:
            start 0
            go right 14
            0 + 14 = 14 which does not register as a zero but we still take away

        this extra zero seems to only happen when going left and starting at 0
        maybe just adding an exception will fix it?

        THAT WORKED!
"""

if len(sys.argv) != 2:
    exit(0)
input_filename = sys.argv[1]

print(f"input file: {input_filename}")

with open(input_filename, "r") as _input, open("output.txt", "w") as _output:
    zeros = 0
    curr = 50

    _output.write(f"{'DIR':2} {'ROT':4} {'AT':4} {'ZEROS':4}\n")

    for line in _input:
        line = line.strip()
        if not line:
            break

        _dir = line[0]
        _rot = int(line[1:])

        zeros += _rot // 100  # count wraps

        _rot %= 100  # account for wraps

        if _dir == "L":
            if curr != 0 and curr - _rot <= 0:  # land on or cross zero; don't count left turn if starting at 0
                zeros += 1
            curr = (100 + curr - _rot) % 100
        else:
            if curr + _rot >= 100:  # land on or cross zero
                zeros += 1
            curr = (curr + _rot) % 100

        _output.write(f"{_dir:2} {_rot:4} {curr:4} {zeros:4}\n")
    _output.write(f"TOTAL ZEROS {zeros}\n")
