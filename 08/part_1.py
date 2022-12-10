import sys

height_map = [[int(char) for char in row.strip()] for row in sys.stdin]
row_count = len(height_map)
column_count = len(height_map[0])
visible_trees = 0

for i, row in enumerate(height_map):
    for j, height in enumerate(row):
        visibility = {
            'top': True,
            'bottom': True,
            'left': True,
            'right': True
        }

        for i_before in range(0, i):
            if height_map[i_before][j] >= height:
                visibility['top'] = False
                break

        for i_after in range(i + 1, row_count):
            if height_map[i_after][j] >= height:
                visibility['bottom'] = False
                break

        for j_before in range(0, j):
            if height_map[i][j_before] >= height:
                visibility['left'] = False
                break

        for j_after in range(j + 1, column_count):
            if height_map[i][j_after] >= height:
                visibility['right'] = False
                break

        if any(visibility.values()):
            visible_trees += 1

print(visible_trees)
