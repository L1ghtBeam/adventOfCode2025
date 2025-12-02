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
            num_str = str(i)
            if len(num_str) % 2 == 1:
                continue

            first, second = num_str[:len(num_str)//2], num_str[len(num_str)//2:]
            if first == second:
                output += i
    return output

print(main(sys.argv[1]))