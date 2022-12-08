import copy
import os
import sys
 

input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        input = file.strip().split("\n")

visible_trees = len(input) + len(input) + len(input[0]) + len(input[0]) -  4
highest_scenic_score = 0

for y in range(1, len(input) - 1):
    for x in range(1, len(input[y]) - 1):
        current_tree_height = input[y][x]
        trees_up = [i[x] for i in input[:y]]
        trees_down = [i[x] for i in input[y+1:]]
        trees_left = input[y][:x]
        trees_right = input[y][x+1:]

        if current_tree_height > max(trees_up) or current_tree_height > max(trees_down) or current_tree_height > max(trees_left) or current_tree_height > max(trees_right):
            visible_trees += 1

        visibility_up = 0
        visibility_down = 0
        visibility_left = 0
        visibility_right = 0
        for i in range(len(trees_up), 0, -1):
            visibility_up += 1
            if (trees_up[i-1]) >= current_tree_height:
                break
        for i in range(len(trees_down)):
            visibility_down += 1
            if (trees_down[i]) >= current_tree_height:
                break
        for i in range(len(trees_left), 0, -1):
            visibility_left += 1
            if (trees_left[i-1]) >= current_tree_height:
                break
        for i in range(len(trees_right)):
            visibility_right += 1
            if (trees_right[i]) >= current_tree_height:
                break

        highest_scenic_score = max(highest_scenic_score, visibility_left * visibility_right * visibility_up * visibility_down)

print("ResultA: ", visible_trees)
print("ResultB: ", highest_scenic_score)
