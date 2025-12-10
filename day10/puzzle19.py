import sys
from collections import deque


def main(infile):
    output = 0
    with open(infile) as f:
        for line in f:
            goal, buttons = parse_machine(line)
            output += min_button_presses(goal, buttons)
    print(output)


def min_button_presses(goal, buttons):
    if goal == 0:
        return 0

    seen = set()
    seen.add(0)
    q = deque()
    q.append(0)

    presses = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()

            for button in buttons:
                adj = node ^ button
                if adj in seen:
                    continue
                if adj == goal:
                    return presses
                seen.add(adj)
                q.append(adj)

        presses += 1

    raise RuntimeError('no solution')


def parse_machine(line):
    parts = line.rstrip().split(' ')

    # parse indicator lights
    lights = len(parts[0])-2
    goal = 0
    for c in parts[0][1:-1]:
        goal <<= 1
        if c == '#':
            goal |= 1

    # parse buttons
    buttons = []
    for button_str in parts[1:-1]:
        num_strs = button_str[1:-1].split(',')
        button = 0
        for num_str in num_strs:
            num = int(num_str)
            button |= (1 << (lights - num - 1))
        buttons.append(button)

    return goal, buttons



if __name__ == '__main__':
    main(sys.argv[1])