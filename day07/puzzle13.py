import sys

EMPTY = '.'
SPLITTER = '^'
START = 'S'



def main(infile):
    matrix = []
    with open(infile) as f:
        for line in f:
            matrix.append(line.rstrip())

    # find starting position
    for c in range(len(matrix[0])):
        if matrix[0][c] == START:
            start_column = c
            break
    else:
        raise RuntimeError('Start position not found')

    return count_splits(matrix, start_column)


def count_splits(matrix, start_column):
    M, N = len(matrix), len(matrix[0])
    stack = [(0, start_column)]
    visited = set()

    splitter_count = 0

    while stack:
        r, c = stack.pop()

        while r < M and 0 <= c < N and (r, c) not in visited:
            visited.add((r, c))

            if matrix[r][c] == SPLITTER:
                stack.append((r, c+1))
                splitter_count += 1
                c -= 1

            r += 1

    return splitter_count



if __name__ == '__main__':
    print(main(sys.argv[1]))