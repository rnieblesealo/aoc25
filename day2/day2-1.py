import sys


"""
part 1
all about divisibility
    original solution:

    if the subsequence length (lets call it x) divides the total string length,
    it means that it might be a link in the chain
    so we make a string made up of that subsequence n times (n = string length)
    if it matches the original string, then it is made up of that subsequence!
    if not continue trying for all numbers that divide the total string length

    this worked, but i didn't read the problem right!
    the number is invalid if it's made of **exactly 2 repeating sequences of chars**

    this meant that we only had to check if the string length was divisible by 2,
    and if so, all we needed to do was see if the first and second halves matched

    applying this iteratively to all of the ranges yielded the correct result
    (albeit really slow!)
"""


def invalid(n):
    s = str(n)  # work with number as string
    for i in range(1, len(s)):
        if len(s) % len(s[:i]) == 0:
            # sequence length divides total length
            if s[:i] * (len(s) // len(s[:i])) == s:
                # sequence length * chunks matches original string
                return True
    return False


def invalid_2seq(n):
    s = str(n)

    # length of the number must be div by 2
    if len(s) % 2 != 0:
        return False

    # both halves must match
    mid = len(s) // 2
    h1, h2 = s[:mid], s[mid:]
    if h1 != h2:
        return False

    return True


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
                if invalid_2seq(n):
                    print(f"\t{n} seems invalid")
                    _invalid_sum += n
        print(f"Final sum: {_invalid_sum}")
