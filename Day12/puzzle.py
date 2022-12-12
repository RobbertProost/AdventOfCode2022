import os
import sys
from collections import deque
from itertools import product


def get_ok_neighbors(grid, current_position):
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        y, x = current_position[0] + dy, current_position[1] + dx
        if not (x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]) or grid[current_position[0]][current_position[1]] + 1 < grid[y][x]):
            yield (y, x)


def find_shortest_path(
    grid, starts, end):
    queue = deque((0, start) for start in starts)
    visited = set()

    while queue:
        dist, (y, x) = queue.popleft()

        if (y, x) == end:
            return dist
        if (y, x) in visited:
            continue

        visited.add((y, x))

        for ny, nx in get_ok_neighbors(grid, (y, x)):
            queue.append((dist + 1, (ny, nx)))


input = ""
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    input = f.read()

grid = []
start = None
end = None

for y, line in enumerate(input.splitlines()):
    row = []
    for x, cur in enumerate(line):
        if cur == "S":
            row.append(1)
            start = (y, x)
        elif cur == "E":
            row.append(26)
            end = (y, x)
        else:
            row.append(ord(cur) - ord("a") + 1)

    grid.append(row)

print("ResultA: ", find_shortest_path(grid, [start], end))

possible_start_locations = [
    (y, x)
    for y, x in product(range(len(grid)), range(len(grid[0])))
    if grid[y][x] == 1
]

print("ResultB: ", find_shortest_path(grid, possible_start_locations, end))