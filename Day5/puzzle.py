import copy
import os
import sys

def ParseStacks(stacks_input) :
    stacks_input = [x.replace('[', ' ') for x in stacks_input]
    stacks_input = [x.replace(']', ' ') for x in stacks_input]
    stacks_input = [[stack[i:i+4] for i in range(0, len(stack), 4)] for stack in stacks_input]

    stack_numbers = stacks_input[-1]

    stacks = []
    for i in range(len(stack_numbers)):
        stacks.append([])
        for x in range(len(stacks_input[:-1])-1, -1, -1):
            crate = stacks_input[x][i].strip()
            if (crate != ''):
                stacks[i].append(crate)

    return stacks

stacks_input = []
moves_input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        stacks_input, moves_input = [x.split('\n') for x in file.split('\n\n')]

stacks = ParseStacks(stacks_input)

moves_input = [x.replace(' from ', ' ') for x in moves_input]
moves_input = [x.replace(' to ', ' ') for x in moves_input]
moves_input = [x.replace('move ', '') for x in moves_input]

stacksA = stacks
stacksB = copy.deepcopy(stacks)

for move in moves_input:
    if (move == ''):
        continue
    
    move_count, src, dst = [int(x) for x in move.split(' ')]

    move_stack_B = []
    for i in range(int(move_count)):
        stacksA[dst-1].append(stacksA[src-1].pop())
        move_stack_B.append(stacksB[src-1].pop())

    for i in range(len(move_stack_B)):
        stacksB[dst-1].append(move_stack_B.pop())

resultA = ""
for stack in stacksA:
    resultA = resultA + stack[-1]

resultB = ""
for stack in stacksB:
    resultB = resultB + stack[-1]

print("Result A: ", resultA)
print("Result B: ", resultB)
