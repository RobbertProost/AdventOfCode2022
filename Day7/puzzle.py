import copy
import os
import sys
 

input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        input = file.strip().split("\n")

current_dir = ""
directory_sizes = dict()

for line in input:
    if line.startswith('$'):
        arguments = line[2:].split(' ')
        if arguments[0] == 'cd':
            if arguments[1] == '..':
                current_dir = os.path.split(current_dir)[0]
            else:
                current_dir = os.path.join(current_dir, arguments[1])
                if current_dir not in directory_sizes:
                    directory_sizes[current_dir] = 0

    elif not line.startswith('dir') and not line == '':        
        directory_sizes[current_dir] = directory_sizes[current_dir] + int(line.split(' ')[0])

sumA = 0
for directory in directory_sizes:
    for directory2 in directory_sizes:
        if directory == directory2:
            continue
        
        if directory2.startswith(os.path.abspath(directory)):
            directory_sizes[directory] = directory_sizes[directory] + directory_sizes[directory2]

    if directory_sizes[directory] <= 100000:
        sumA = sumA + directory_sizes[directory]

disk_size = 70000000
required_to_free_up = 30000000 - (disk_size - directory_sizes['/'])
smallest_found = disk_size

for directory in directory_sizes:
    size = directory_sizes[directory]
    if size >= required_to_free_up and size < smallest_found:
        smallest_found = size

print("ResultA: ", sumA)
print("ResultB: ", smallest_found)
