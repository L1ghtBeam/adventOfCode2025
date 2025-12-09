import sys



def main(infile):
    tiles = []
    with open(infile) as f:
        for line in f:
            x, y = line.rstrip().split(',')
            tiles.append((int(x), int(y)))

    max_area = 0
    for i in range(len(tiles)-1):
        for j in range(i+1, len(tiles)):
            max_area = max(max_area, area(i, j, tiles))
    return max_area


def area(i, j, tiles):
    x1, y1 = tiles[i]
    x2, y2 = tiles[j]
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)



print(main(sys.argv[1]))