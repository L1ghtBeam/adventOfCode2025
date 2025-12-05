import sys
from itertools import takewhile


def main(infile):
    ranges = []
    with open(infile) as f:
        it = takewhile(lambda line: line.strip() != '', f)
        for line in it:
            a, b = line.strip().split('-')
            a, b = int(a), int(b)
            ranges.append((a, b))

    return count_fresh_ids(ranges)


def count_fresh_ids(ranges):
    ranges.sort()
    last_counted_id = -1

    output = 0
    for a, b in ranges:
        if b <= last_counted_id:
            continue

        left = max(a, last_counted_id+1)
        output += b - left + 1
        last_counted_id = b
    return output


if __name__ == '__main__':
    print(main(sys.argv[1]))