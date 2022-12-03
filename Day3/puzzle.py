import os
import sys

def GetPriority(item) :
    prio = ord(item.lower()) - ord('a') + 1
    if item.isupper():
        prio += 26
    return prio

def GetPrioritiesOfCommonItems(items) :
    commonItems = set.intersection(*map(set,items))
    return sum(GetPriority(x) for x in commonItems) 

def GetChunks(sequence, size):
    return (sequence[pos:pos + size] for pos in range(0, len(sequence), size))

rucksacks = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    for line in f:
        line = line.split('\n')
        if line:
            rucksacks.append(line[0])

prioritySumA = 0
for rucksack in rucksacks:
    prioritySumA += GetPrioritiesOfCommonItems(GetChunks(rucksack, int(len(rucksack) * 0.5)))

prioritySumB = 0
for group in GetChunks(rucksacks, 3):
    prioritySumB += GetPrioritiesOfCommonItems(group)

resultA = prioritySumA
resultB = prioritySumB

print("Result A: ", resultA)
print("Result B: ", resultB)