import sys


"""
part 2
at least 2 numbers repeating n times now, not just 2
this means that the length must be 2n; a multiple of 2

the first solution is handy here!

we can rework it such that it only counts subsequences of length 2 and on

nvm this doesn't work
it needs to be any subsequence of any length that itself is repeated at least twice!
how do we check for that?
    len(s) // len(s[:i]) (amount of chunks) must be at least 2

outtake: READ THE F***ING PROBLEM RIGHT
    also string manip is your friend :)
    and trying brute force first is cool as well!

improving the solution
    curr solution is too slow because we manually check each number
    what patterns can we leverage?
        * even for ranges of very large numbers, there's never more than 1 invalid id
"""


def invalid_2seq_any(n):
    s = str(n)  # work with number as string
    for i in range(1, len(s)):
        total_length = len(s)
        sub_length = len(s[:i])

        # sequence length must divide total length
        if total_length % sub_length == 0:
            chunks = total_length // sub_length

            # sequence length * chunks matches original string
            # there are also at least 2 chunks (i.e. subsequence repeats at least twice)
            if chunks > 1 and (s[:i] * chunks == s):
                return True
    return False


if len(sys.argv) != 2:
    exit(0)
input_filename = sys.argv[1]
print(f"Got input file: {input_filename}")


with open(input_filename, "r") as _input, open("output.txt", "w") as _output:
    for line in _input:  # doesn't count, just one line
        line = line.strip()
        if not line:
            break

        # this shit is slow as fuck
        ranges = line.split(",")
        _invalid_sum = 0
        for r in ranges:
            _range = r.split("-")

            _min = int(_range[0])
            _max = int(_range[1])

            print(f"Working with range {_min}, {_max}")

            for n in range(_min, _max + 1):
                if invalid_2seq_any(n):
                    print(f"\t{n} seems invalid")
                    _invalid_sum += n
        print(f"Final sum: {_invalid_sum}")
