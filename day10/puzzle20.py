import sys
from itertools import combinations



def main(infile):
    output = 0
    with open(infile) as f:
        inputs = []
        for line in f:
            inputs.append(parse_machine(line))

    for buttons, joltage in inputs:
        button_vecs = [button_vector(button, len(joltage)) for button in buttons]
        combos = button_combos(button_vecs)
        cache = {}
        output += min_button_presses(joltage, combos, cache)
    print(output)


# bifurcation strategy using recursion with memoization
# inspired by post by u/tenthmascot
def min_button_presses(joltage, button_combos, cache):
    # base cases
    jolt_tuple = tuple(joltage)
    if jolt_tuple in cache:
        return cache[jolt_tuple]
    if any(x < 0 for x in joltage):
        return float('inf')
    if all(x == 0 for x in joltage):
        return 0

    # find all possible ways to reduce joltage into an even subproblem
    min_cost = float('inf')
    for vector, cost in button_combos:
        result = [j - v for j, v in zip(joltage, vector)]
        # make sure result is all even
        if any(x % 2 == 1 for x in result):
            continue

        # divide by 2
        for i in range(len(result)):
            result[i] = result[i] // 2
        # find minimum way to achieve the half result. This value * 2 = cost of result, and adding on the cost for
        # this button combo makes our current joltage
        min_cost = min(min_cost, cost + 2 * min_button_presses(result, button_combos, cache))

    cache[jolt_tuple] = min_cost
    return min_cost


def button_combos(buttons):
    combos = []
    for r in range(len(buttons)+1):
        for vec_list in combinations(buttons, r):
            result = [0] * len(buttons[0])
            for vec in vec_list:
                for i in range(len(result)):
                    result[i] += vec[i]
            combos.append((result, r))
    return combos


def button_vector(button, size):
    vector = [0] * size
    for i in button:
        vector[i] = 1
    return vector


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

    return buttons, joltage



if __name__ == '__main__':
    main(sys.argv[1])