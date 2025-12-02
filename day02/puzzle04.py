import sys


def main(infile):
    with open(infile) as f:
        data = f.read()
    data.rstrip()

    ranges = data.split(',')
    ranges = [range_str.split('-') for range_str in ranges]
    ranges = [(int(x[0]), int(x[1])) for x in ranges]

    output = 0
    for start, end in ranges:
        for i in range(start, end+1):
            if invalid_id(i):
                output += i
    return output


def invalid_id(x):
    s = str(x)
    for reps in range(2, len(s)+1):
        size, remainder = divmod(len(s), reps)
        if remainder != 0:
            continue

        snippet = s[:size]
        for i in range(1, reps):
            if s[size*i: size*(i+1)] != snippet:
                break
        else:
            return True
    return False


print(main(sys.argv[1]))