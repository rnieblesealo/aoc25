"""
what do we need to do?
    find all ids within a range that are comprised by some sequence of numbers
    e.g.
    123123 -> "123" x2
    55 -> "5" x2
    6464 -> "64" x2

constraints:
    no id will ever have a leading 0

e.g. 95 and 115 contains 99 which is "9" x2

breaking down:
    how can we tell whether a number is comprised of a sequence?
        that is, it is fully made up of **a sequence of numbers repeating at least twice**

        since the number is wholly made up of sequences,
        the start of the number is also the start of the sequence (if valid)

        we can begin looking for the sequence here, but

    how do we know when the sequence restarts?
        rough intuitive approach:
            note down the first digit
            keep reading next digits, keeping track of how many digits we've moved (n)
                also keep track of the sequence
            if we find the first digit again, the sequence might be restarting here
            read the next n digits and compare them with the sequence thus far
            if a match is found, this means we have one repeat!
            read the next n digits again until the end
            if all sequences of n match, then the number is an invalid id

            this seems finnicky though!
            for a number like 12311231, finding the first digit again does NOT mean the start of the next block

        doing more analysis:
            123123
            12311231
            110411104111041

            if we look at these, if the id is invalid,
            **the length of the number is divisible by the length of the subsequence**

            110411104111041 -> 11041x3; 15/3 = 5

            this condition must **always be present**...

            maybe we can use it as an additional check to finding the first digit
            or maybe the only check at all!

            approach:
                iterate over the sequence
                if the current sequence length divides the total length:
                    extract the sequence thus far
                    check the next n blocks of len(sequence)
                    if they all match the original sequence, then we're good!
                    if not, keep moving until we find another offset that divides the total length

                this seems better, but is quite inefficient:
                we need to look for all the other blocks!
                there could also be a huge number of potential sequences if the total length has lots of divisors

        how else could we leverage the divisibility condition?

        "throw a hashmap at the problem"

            what patterns are there if we were to count the digits?

            12311231
            1: 4
            2: 2
            3: 2

            before even going further, i can tell counting won't do anything in regards of order:
            13211231 is not valid but the counts are still the same

            how can we ensure our check preserves order?

        after searching:
            iterate
            if the sequence length divides, obtain chunks the length divides into (n)
            if the sequence string * n matches the original string, then it is invalid!

            this works!

            what i got right:
                identifying the divisibility property
            what i couldn't get but is useful:
                comparing original string against one built from subsequence

now, how do we do this for all numbers in a range?

brute force:
    just test all numbers in a range

    sum = 0
    for n in range(left, right):
        if invalid(n)
            sum += n
    return sum

    this is really slow but i guess it works; the ranges aren't big enough as to make doing a bunch of loops super bad
    but it still sucks

"""


def invalid(n):
    s = str(n)
    for i in range(1, len(s)):
        if len(s) % len(s[:i]) == 0:
            # sequence length divides total length
            if s[:i] * (len(s) // len(s[:i])) == s:
                # sequence length * chunks matches original string
                return True
    return False


print(invalid(123123))
