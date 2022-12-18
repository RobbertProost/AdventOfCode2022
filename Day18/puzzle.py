import os
import sys
import copy

def neighbours(cube):
    x,y,z = cube
    
    return set({(x+1,y,z),
     (x-1,y,z),
     (x,y+1,z),
     (x,y-1,z),
     (x,y,z+1),
     (x,y,z-1)})

cubes = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    file = f.read()
    cubes = set(tuple(int(coordinate) for coordinate in cube.split(',')) for cube in file.strip().split('\n'))

possible_outer_edges = set()
open_edge_count = 0
for cube in cubes:
    for neighbour in neighbours(cube):
        if neighbour not in cubes:
            open_edge_count += 1
            possible_outer_edges.add(neighbour)

print("ResultA: ", open_edge_count)

max_x = max(x for x,_,_ in cubes)
max_y = max(y for _,y,_ in cubes)
max_z = max(z for _,_,z in cubes)

min_x = min(x for x,_,_ in cubes)
min_y = min(y for _,y,_ in cubes)
min_z = min(z for _,_,z in cubes)

for possible_edge in possible_outer_edges:
    visited = set()
    queue = [possible_edge]
    while queue:
        cube = queue.pop()
        if cube in visited or cube in cubes:
            continue
        if (cube[0] < min_x or 
            cube[0] > max_x or 
            cube[1] < min_y or 
            cube[1] > max_y or 
            cube[2] < min_z or 
            cube[2] > max_z):
            break

        visited.add(cube)
        queue.extend(neighbours(cube))

    else:
        for neighbour in neighbours(possible_edge):
            if neighbour in cubes:
                open_edge_count -= 1

print("ResultB: ", open_edge_count)