import sys

datastream_buffer = sys.stdin.readline().strip()
marker_sequence_length = 4

for i in range(len(datastream_buffer) - marker_sequence_length + 1):
    j = i + marker_sequence_length
    last_four_characters = datastream_buffer[i:j]

    if len(last_four_characters) == len(set(last_four_characters)):
        print(j)
        break