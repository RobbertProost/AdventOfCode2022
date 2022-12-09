import copy
import os
import sys


def simulateMotion(knots):
    locations_visited = set()
    locations_visited.add((0,0))

    for line in input:
        dir, steps = line.split()

        for i in range(int(steps)):      
            if (dir == 'U'):
                knots[0][1] += 1
            elif (dir == 'D'):
                knots[0][1] -= 1
            elif (dir == 'L'):
                knots[0][0] -= 1
            elif (dir == 'R'):
                knots[0][0] += 1

            
            for i in range(1, len(knots)):
                diff_x = knots[i-1][0] - knots[i][0]
                diff_y = knots[i - 1][1] - knots[i][1]
                if abs(diff_x) > 1 or abs(diff_y) > 1:
                    if diff_x > 0:
                        knots[i][0] += 1
                    elif diff_x < 0:
                        knots[i][0] -= 1
                    if diff_y > 0:
                        knots[i][1] += 1 
                    elif diff_y < 0:
                        knots[i][1] -= 1 
                
            locations_visited.add((knots[-1][0], knots[-1][1]))

    return len(locations_visited)

input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        input = file.strip().split("\n")


knotsA = [[0,0],[0,0]]
knotsB = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        
print("ResultA:" , simulateMotion(knotsA))
print("ResultB:" , simulateMotion(knotsB))