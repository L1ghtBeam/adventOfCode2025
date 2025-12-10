import sys
from collections import deque
import time

UPDATE_INTERVAL = 5.0



def main(infile):
    output = 0
    print("Running..")
    with open(infile) as f:
        inputs = []
        for line in f:
            goal, buttons = parse_machine(line)
            new_buttons = []
            for button in buttons:
                new_button = []
                for i in range(len(goal)):
                    new_button.append(int(i in button))
                new_buttons.append(new_button)
            inputs.append((goal, new_buttons))

        last_update = time.monotonic()
        for i, input_data in enumerate(inputs, 1):
            output += min_button_presses(*input_data)

            if time.monotonic() - last_update > UPDATE_INTERVAL:
                last_update = time.monotonic()
                print(f"Computed {i}/{len(inputs)}")
    print(output)


def min_button_presses(goal, buttons):
    init = tuple([0] * len(goal))
    goal = tuple(goal)

    seen = set()
    seen.add(init)
    q = deque()
    q.append(init)

    presses = 1
    while q:
        for _ in range(len(q)):
            node = q.popleft()
            node_mutable = list(node)

            for button in buttons:
                for i in range(len(node_mutable)):
                    node_mutable[i] += button[i]

                adj = tuple(node_mutable)
                if new_joltage_state(adj, seen, goal):
                    if adj == goal:
                        return presses
                    seen.add(adj)
                    q.append(adj)

                for i in range(len(node_mutable)):
                    node_mutable[i] -= button[i]

        presses += 1

    raise RuntimeError('no solution')


def new_joltage_state(joltage, seen, goal):
    if joltage in seen:
        return False
    for this_j, max_j in zip(joltage, goal):
        if this_j > max_j:
            return False
    return True


def parse_machine(line):
    parts = line.rstrip().split(' ')

    # parse buttons
    buttons = []
    for button_str in parts[1:-1]:
        num_strs = button_str[1:-1].split(',')
        button = []
        for num_str in num_strs:
            button.append(int(num_str))
        buttons.append(button)

    # parse joltage
    joltage_strs = parts[-1][1:-1].split(',')
    joltage = []
    for joltage_str in joltage_strs:
        joltage.append(int(joltage_str))

    return joltage, buttons



if __name__ == '__main__':
    main(sys.argv[1])