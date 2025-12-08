import heapq
import sys

from day08.puzzle15 import UnionFind
from day08.puzzle15 import build_junction_entries



class UnionFindCount(UnionFind):
    def __init__(self, n):
        super().__init__(n)
        self.count = n

    def union(self, x, y):
        if super().union(x, y):
            self.count -= 1
            return True
        return False

    def __len__(self):
        return self.count



def main(infile):
    junctions = []
    with open(infile) as f:
        for line in f:
            x, y, z = line.rstrip().split(',')
            x, y, z = int(x), int(y), int(z)
            junctions.append((x, y, z))

    i, j = last_pair(junctions)
    return junctions[i][0] * junctions[j][0]


def last_pair(junctions):
    heap = build_junction_entries(junctions)
    heapq.heapify(heap)

    i, j = None, None
    uf = UnionFindCount(len(junctions))
    while len(uf) > 1:
        _, i, j = heapq.heappop(heap)
        uf.union(i, j)
    return i, j



if __name__ == '__main__':
    print(main(sys.argv[1]))