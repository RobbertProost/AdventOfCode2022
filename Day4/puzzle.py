import os
import sys

section_assignments = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split('\n')
        if line:
            section_assignments.append(line[0])

overlapsA = 0
overlapsB = 0

for assignment in section_assignments:
    pair1, pair2 = assignment.split(',')

    start1, end1 = [int(s) for s in pair1.split('-')]
    start2, end2 = [int(s) for s in pair2.split('-')]

    if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
        overlapsA += 1
        overlapsB += 1
    elif (end1 >= start2 and end1 <= end2) or (end2 >= start1 and end2 <= end1):
        overlapsB += 1

print("Result A: ", overlapsA)
print("Result B: ", overlapsB)