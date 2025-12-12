import sys
from collections import deque, defaultdict
from day11.puzzle21 import parse_line


def main(infile):
    # build graph
    graph = {}
    with open(infile) as f:
        for line in f:
            node, edges = parse_line(line)
            graph[node] = edges
    print(count_paths(graph))


def count_paths(graph):
    in_degree = {}
    for edges in graph.values():
        for edge in edges:
            in_degree[edge] = 1 + in_degree.get(edge, 0)

    eval_queue = deque()
    for node in graph.keys():
        if node not in in_degree:
            eval_queue.append(node)

    # index
    # [0] : neither dac or fft
    # [1] : dac
    # [2] : fft
    # [3] : dac and fft
    paths = defaultdict(lambda: [0]*4)
    while eval_queue:
        node = eval_queue.popleft()
        if node == "svr":
            paths[node][0] += 1
        elif node == "dac":
            paths[node][1] += paths[node][0]
            paths[node][0] = 0
            paths[node][3] += paths[node][2]
            paths[node][2] = 0
        elif node == "fft":
            paths[node][2] += paths[node][0]
            paths[node][0] = 0
            paths[node][3] += paths[node][1]
            paths[node][1] = 0
        elif node == "out":
            return paths[node][3]

        for edge in graph[node]:
            for i in range(4):
                paths[edge][i] += paths[node][i]
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                eval_queue.append(edge)

    raise RuntimeError("Node 'out' not found")



if __name__ == '__main__':
    main(sys.argv[1])