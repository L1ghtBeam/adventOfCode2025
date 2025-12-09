import heapq
import sys
import time

from day09.puzzle17 import area
from itertools import pairwise

UPDATE_INTERVAL = 5.0



def main(infile):
    red_tiles = []
    with open(infile) as f:
        for line in f:
            x, y = line.rstrip().split(',')
            red_tiles.append((int(x), int(y)))

    # build outlines
    print("Building outlines..")
    green_tiles = set()
    make_green_outlines(red_tiles, green_tiles)

    # find a position inside the area
    inside_x, inside_y = find_inside_pos(red_tiles)

    # fill in the inside given this starting position
    print("Filling inside..")
    flood_fill(green_tiles, inside_x, inside_y)

    # create heap of rectangles sorted by area in non-ascending order so we can search the biggest
    # rectangles first
    print("Building heap..")
    heap = []
    for i in range(len(red_tiles)-1):
        for j in range(i+1, len(red_tiles)):
            heap.append((-area(i, j, red_tiles), i, j))
    heapq.heapify(heap)

    # main searching loop
    total_entries = len(heap)
    print(f"Starting with {total_entries} entries to check")
    last_update = time.monotonic()
    while heap:
        neg_area, i, j = heapq.heappop(heap)
        if in_green_tiles(red_tiles, green_tiles, i, j):
            print(f"Found! Rectangle between {red_tiles[i][0]},{red_tiles[i][1]} and {red_tiles[j][0]},{red_tiles[j][1]}")
            print(-neg_area)
            return 0

        # updater
        t = time.monotonic()
        if t - last_update > UPDATE_INTERVAL:
            last_update = t
            print(f"Checked: {total_entries - len(heap)}/{total_entries}")

    print("Failed")
    return 1



def in_green_tiles(red_tiles, green_tiles, i, j):
    x1, y1 = red_tiles[i]
    x2, y2 = red_tiles[j]
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    for x in range(x1, x2+1):
        if (x, y1) not in green_tiles or (x, y2) not in green_tiles:
            return False
    for y in range(y1, y2+1):
        if (x1, y) not in green_tiles or (x2, y) not in green_tiles:
            return False
    return True


def flood_fill(tiles, x, y):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if (x, y) in tiles:
            continue
        tiles.add((x, y))
        stack.append((x+1, y))
        stack.append((x-1, y))
        stack.append((x, y+1))
        stack.append((x, y-1))


def find_inside_pos(red_tiles):
    top_border = None
    top_border_y = float('inf')
    for i in range(len(red_tiles) - 1):
        # check for horizontal line
        if red_tiles[i][1] != red_tiles[i + 1][1]:
            continue
        if red_tiles[i][1] < top_border_y:
            top_border = i
            top_border_y = red_tiles[i][1]
    top_border_x = min(red_tiles[top_border][0], red_tiles[top_border + 1][0])
    # position (top_border_x+1, top_border_y+1) is PROBABLY inside the area
    return top_border_x+1, top_border_y+1


def make_green_outlines(red_tiles, green_tiles):
    for r1, r2 in pairwise(red_tiles):
        make_green_line(r1, r2, green_tiles)
    make_green_line(red_tiles[-1], red_tiles[0], green_tiles)


def make_green_line(start, end, green_tiles):
    x, y = start
    x_goal, y_goal = end

    dx = x_goal - x
    if dx != 0:
        dx //= abs(dx)
    dy = y_goal - y
    if dy != 0:
        dy //= abs(dy)

    if dx == 0 and dy == 0:
        raise RuntimeError

    while x != x_goal or y != y_goal:
        green_tiles.add((x, y))
        x += dx
        y += dy



main(sys.argv[1])