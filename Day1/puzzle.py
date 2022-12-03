import os
import sys

calories = []
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    calories.append(0)
    for line in f:
        line = line.split()
        if line:
            calories[-1] = calories[-1] + int(line[0])
        else:
            calories.append(0)


calories.sort()

resultA = max(calories)
resultB = sum(calories[-3:])
       
print("Result A: ", resultA)
print("Result B: ", resultB)