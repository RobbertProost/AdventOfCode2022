import os
import sys

input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        input = file.strip().split("\n")

signal_strenghts = []

cycle_count  = 0
x = 1

display = ""
chars_per_line = 40

for line in input:
    exec_cycles = 1
    increment_by = 0
    if line.startswith('addx'):
        exec_cycles = 2
        increment_by = int(line.split(' ')[1])

    for i in range(exec_cycles):
        display += '#' if abs((cycle_count % chars_per_line) - x) < 2 else '.'
        cycle_count += 1
        if (cycle_count % 40 == 20):
            signal_strenghts.append(x * cycle_count)

    x += increment_by

print("ResultA: ", sum(signal_strenghts))

print("ResultB:")
while display:
    print(display[:chars_per_line])
    display = display[chars_per_line:]