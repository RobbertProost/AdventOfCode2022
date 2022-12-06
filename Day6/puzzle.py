import copy
import os
import sys

def FindFirstMarker(input_sequence, marker_size) :
    for i in range(marker_size, len(input_sequence)):
        if(len(set(input_sequence[i-marker_size:i])) == marker_size):
            return i     

input = [] 
with open(os.path.join(sys.path[0], 'input.txt')) as f:
        file = f.read()
        input = file.strip()

first_packet_marker = FindFirstMarker(input, 4)
first_message_marker = FindFirstMarker(input, 14)

print("ResultA: ", first_packet_marker)
print("ResultB: ", first_message_marker)