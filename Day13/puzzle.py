import os
import sys
from functools import cmp_to_key
import json

def compare(first, second):
    if isinstance(first, int) and isinstance(second, int):
        return first - second
    if isinstance(first, int):
        return compare([first], second)
    if isinstance(second, int):
        return compare(first, [second])
    
    for x, y in zip(first, second):
        if diff := compare(x, y):
            return diff

    return len(first) - len(second)

input = ""
with open(os.path.join(sys.path[0], 'input.txt')) as f:
    file = f.read()
    input = file.strip().split('\n\n')


good_pairs = []
all_signals = []
for i, pair in enumerate(input):
    first, second = pair.splitlines()
    first_list, second_list = json.loads(first), json.loads(second)
    all_signals.append(first_list)
    all_signals.append(second_list)

    if compare(first_list, second_list) < 0:
        good_pairs.append(i+1)

print("ResultA: ", sum(good_pairs))

all_signals.append([[2]])
all_signals.append([[6]])
sorted_signals = sorted(all_signals, key=cmp_to_key(compare))
print("ResultB: ", (sorted_signals.index([[2]]) + 1) * (sorted_signals.index([[6]]) + 1))