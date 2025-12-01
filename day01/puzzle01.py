import sys

DIAL_SIZE = 100

def main(infile):
    dial = 50
    output = 0
    with open(infile) as f:
        for line in f:
            direction = 1 if line[0] == 'R' else -1
            count = int(line[1:])
            dial = (dial + count * direction) % DIAL_SIZE
            if dial == 0:
                output += 1
    return output

print(main(sys.argv[1]))