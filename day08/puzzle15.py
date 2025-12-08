import heapq
import sys

ANS_CIRCUITS = 3



class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return False

        if self.rank[b] > self.rank[a]:
            a, b = b, a

        self.parent[b] = a
        self.rank[a] += 1
        return True



def main(infile, pairs):
    junctions = []
    with open(infile) as f:
        for line in f:
            x, y, z = line.rstrip().split(',')
            x, y, z = int(x), int(y), int(z)
            junctions.append((x, y, z))

    uf = make_junction_pairs(junctions, pairs)
    circuits = {}
    for i in range(len(junctions)):
        p = uf.find(i)
        circuits[p] = 1 + circuits.get(p, 0)

    output = 1
    large_circuits = heapq.nlargest(ANS_CIRCUITS, circuits.values())
    for circuit in large_circuits:
        output *= circuit
    return output


def make_junction_pairs(junctions, pairs):
    entries = build_junction_entries(junctions)
    uf = UnionFind(len(junctions))
    for _, i, j in heapq.nsmallest(pairs, entries):
        uf.union(i, j)
    return uf


def build_junction_entries(junctions):
    entries = []

    for i in range(len(junctions)-1):
        for j in range(i+1, len(junctions)):
            entries.append((sqr_dist(i, j, junctions), i, j))

    return entries


def sqr_dist(i, j, junctions):
    return sum((a-b)**2 for a, b in zip(junctions[i], junctions[j]))



if __name__ == '__main__':
    print(main(sys.argv[1], int(sys.argv[2])))