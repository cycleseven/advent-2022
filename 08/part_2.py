import math
import sys

height_map = [[int(char) for char in row.strip()] for row in sys.stdin]
row_count = len(height_map)
column_count = len(height_map[0])
max_scenic_score = 0

for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        visibility = {
            'top': 0,
            'bottom': 0,
            'left': 0,
            'right': 0
        }

        for i_before in range(i - 1, -1, -1):
            visibility['top'] += 1
            if height_map[i_before][j] >= height:
                break

        for i_after in range(i + 1, row_count):
            visibility['bottom'] += 1
            if height_map[i_after][j] >= height:
                break

        for j_before in range(j - 1, -1, -1):
            visibility['left'] += 1
            if height_map[i][j_before] >= height:
                break

        for j_after in range(j + 1, column_count):
            visibility['right'] += 1
            if height_map[i][j_after] >= height:
                break

        scenic_score = math.prod(visibility.values())

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score

print(max_scenic_score)
