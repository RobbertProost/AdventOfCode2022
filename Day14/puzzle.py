import os
import sys
from functools import cmp_to_key

def simulate(grid, max_y, max_y_is_floor):
    x, y = 500, 0
    visited = set()
    stack = []

    while y != max_y:
        for dx, dy in (0, 1), (-1, 1), (1, 1):
            if (nx := x + dx, ny := y + dy) not in grid and (nx, ny) not in visited and (not max_y_is_floor or ny != max_y):
                stack.append((x, y))
                x, y = nx, ny
                break
        else:
            visited.add((x, y))
            if len(stack) == 0:
                break
            x, y = stack.pop()

    return len(visited)


input = ""
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    file = f.read()
    input = file.strip().split('\n')

points = set()
for line in input:
    parts = []
    for part in line.split(" -> "):
        x, y = part.split(",")
        x, y = int(x), int(y)
        parts.append((x, y))
    for (x1, y1), (x2, y2) in zip(parts, parts[1:]):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                points.add((x, y))

max_y = max(y for _, y in points)

print("ResultA: ", simulate(points, max_y, False))

floor = max_y + 2
print("ResultB: ", simulate(points, floor, True))