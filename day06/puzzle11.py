import sys


def main(infile):
    num_stack = []
    with open(infile) as f:
        for line in f:
            rows = line.split()
            if line.startswith(('+', '*')):
                return process_rows(num_stack, rows)

            for i in range(len(rows)):
                rows[i] = int(rows[i])

            num_stack.append(rows)
        return 0


def process_rows(stack, ops):
    while len(stack) > 1:
        for i in range(len(stack[0])):
            if ops[i] == '+':
                stack[-2][i] += stack[-1][i]
            elif ops[i] == '*':
                stack[-2][i] *= stack[-1][i]
        stack.pop()

    return sum(stack[0])


if __name__ == '__main__':
    print(main(sys.argv[1]))