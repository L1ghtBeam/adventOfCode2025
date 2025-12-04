import sys

PAPER = "@"
NEIGHBOR_LIMIT = 4


def main(infile):
    grid = []
    with open(infile) as f:
        for line in f:
            grid.append(line.rstrip())

    return count_accessible(grid)


def count_accessible(grid):
    output = 0
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell == PAPER and is_accessible(grid, r, c):
                output += 1
    return output


def is_accessible(grid, r, c):
    M, N = len(grid), len(grid[0])
    count = 0
    for ri in [r-1, r, r+1]:
        for ci in [c-1, c, c+1]:
            if r == ri and c == ci:
                continue
            if ri < 0 or ri >= M or ci < 0 or ci >= N:
                continue
            if grid[ri][ci] != PAPER:
                continue
            count += 1
            if count >= NEIGHBOR_LIMIT:
                return False
    return True



if __name__ == '__main__':
    print(main(sys.argv[1]))