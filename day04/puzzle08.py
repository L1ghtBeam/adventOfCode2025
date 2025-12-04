import sys
from puzzle07 import is_accessible, PAPER

EMPTY = "."


def main(infile):
    grid = []
    with open(infile) as f:
        for line in f:
            grid.append([c for c in line.strip()])

    return remove_paper(grid)


def remove_paper(grid):
    output = 0

    accessible = {True}
    while accessible:
        accessible = mark_accessible(grid)
        for r, c in accessible:
            grid[r][c] = EMPTY
        output += len(accessible)

    return output


def mark_accessible(grid):
    accessible = set()
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == PAPER and is_accessible(grid, r, c):
                accessible.add((r, c))
    return accessible


print(main(sys.argv[1]))