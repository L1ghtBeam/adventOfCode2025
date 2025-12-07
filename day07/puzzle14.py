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

    return count_timelines(matrix, start_column)


def count_timelines(matrix, start_column):
    M, N = len(matrix), len(matrix[0])
    timelines = [0] * M
    timelines[start_column] = 1

    for r in range(1, M):
        for c in range(N):
            if matrix[r][c] == SPLITTER:
                timelines[c-1] += timelines[c]
                timelines[c+1] += timelines[c]
                timelines[c] = 0

    return sum(timelines)



if __name__ == '__main__':
    print(main(sys.argv[1]))