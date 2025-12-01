import sys

DIAL_SIZE = 100

def main(infile):
    dial = 50
    output = 0
    with open(infile) as f:
        for line in f:
            direction = 1 if line[0] == 'R' else -1
            count = int(line[1:])

            full_rotations, ticks = divmod(count, DIAL_SIZE)
            output += full_rotations

            new_dial = dial + ticks * direction
            if new_dial <= 0 < dial:
                output += 1
            elif DIAL_SIZE <= new_dial:
                output += 1

            dial = new_dial % DIAL_SIZE

    return output

print(main(sys.argv[1]))