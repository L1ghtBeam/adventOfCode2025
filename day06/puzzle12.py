import sys


def main(infile):
    nums = []
    with open(infile) as f:
        for line in f:
            line = line.rstrip('\n')

            if line.startswith(('+', '*')):
                return process_rows(nums, line)

            read_row(nums, line)

        return 0


def read_row(nums, line):
    for i in range(len(line)):
        num = int(line[i]) if line[i].isdigit() else 0
        if i < len(nums):
            if num != 0:
                nums[i] = nums[i]*10 + num
        else:
            nums.append(num)


def process_rows(nums, op_line):
    problems = []
    func = None
    for i in range(len(nums)):
        if nums[i] == 0:
            # problem is reset
            func = None
            continue

        if i < len(op_line):
            if op_line[i] == '+':
                func = lambda a, b: a + b
                problems.append(0)
            elif op_line[i] == '*':
                func = lambda a, b: a * b
                problems.append(1)

        problems[-1] = func(problems[-1], nums[i])

    return sum(problems)



if __name__ == '__main__':
    print(main(sys.argv[1]))