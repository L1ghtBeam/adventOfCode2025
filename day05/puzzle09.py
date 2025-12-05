import sys
from itertools import takewhile


def main(infile):
    ranges = []
    ingredients = []
    with open(infile) as f:
        it = takewhile(lambda line: line.strip() != '', f)
        for line in it:
            a, b = line.strip().split('-')
            a, b = int(a), int(b)
            ranges.append((a, b))

        for line in f:
            ingredients.append(int(line.strip()))

    return count_fresh_ingredients(ranges, ingredients)


def count_fresh_ingredients(ranges, ingredients):
    ranges.sort()
    ingredients.sort()

    output = 0
    i, j = 0, 0
    while i < len(ingredients) and j < len(ranges):
        if ingredients[i] > ranges[j][1]:
            j += 1
        elif ingredients[i] < ranges[j][0]:
            i += 1
        else:
            output += 1
            i += 1
    return output



if __name__ == '__main__':
    print(main(sys.argv[1]))