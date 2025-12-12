import sys
from collections import deque, defaultdict


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

    paths = defaultdict(int)
    while eval_queue:
        node = eval_queue.popleft()
        if node == "you":
            paths[node] += 1
        elif node == "out":
            return paths[node]

        for edge in graph[node]:
            paths[edge] += paths[node]
            in_degree[edge] -= 1
            if in_degree[edge] == 0:
                eval_queue.append(edge)

    raise RuntimeError("Node 'out' not found")


def parse_line(line):
    node, edges = line.strip().split(':')
    edges = edges.strip().split(' ')
    return node, edges



if __name__ == '__main__':
    main(sys.argv[1])