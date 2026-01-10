#!/usr/bin/python3

import sys

"""
document your thought process here!
"""

# collect input file name
if len(sys.argv) != 2:
    print("Did not receive input file name!")
    exit(0)
input_filename = sys.argv[1]

print(f"Using input file '{input_filename}'")

with open(input_filename, "r") as _input, open("output.txt", "w") as _output:
    # write your solution here
    pass
