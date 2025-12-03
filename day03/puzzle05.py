import sys


def main(infile):
    output = 0
    with open(infile) as f:
        for line in f:
            output += max_jolt(line.rstrip())
    return output


def max_jolt(s):
    first_digit = 0
    jolt = 0
    for c in s:
        digit = int(c)
        jolt = max(jolt, first_digit * 10 + digit)
        first_digit = max(first_digit, digit)
    return jolt

print(main(sys.argv[1]))