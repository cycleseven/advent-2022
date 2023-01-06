import sys

elevation_map = []
shortest_distance_map = []
goal = None
solution_space = []
best_solution = None

for i, line in enumerate(sys.stdin):
    elevation_row = []
    shortest_distance_row = []

    for j, char in enumerate(line.rstrip()):
        if char == 'S':
            elevation_row.append(0)
            shortest_distance_row.append(None)
        elif char == 'E':
            goal = (i, j)
            elevation_row.append(27)
            shortest_distance_row.append(None)
        else:
            elevation_row.append(ord(char) - ord('a') + 1)
            if char == 'a':
                shortest_distance_row.append(0)
                solution_space.append([(i, j)])
            else:
                shortest_distance_row.append(None)

    elevation_map.append(elevation_row)
    shortest_distance_map.append(shortest_distance_row)

while len(solution_space) > 0:
    path = solution_space.pop(0)
    i1, j1 = path[-1]
    neighbours = [
        (i1 - 1, j1), # never
        (i1, j1 + 1), # eat
        (i1 + 1, j1), # shredded
        (i1, j1 - 1), # wheat
    ]

    for i2, j2 in neighbours:
        if (
            i2 < 0
            or i2 >= len(elevation_map)
            or j2 < 0
            or j2 >= len(elevation_map[0])
            or (i2, j2) == path[0]
            or elevation_map[i2][j2] > elevation_map[i1][j1] + 1
            or (
                shortest_distance_map[i2][j2] is not None
                and shortest_distance_map[i2][j2] <= len(path) + 1
            )
        ):
            continue

        next_path = [*path, (i2, j2)]
        shortest_distance_map[i2][j2] = len(next_path)

        if (i2, j2) == goal:
            best_solution = next_path
        else:
            solution_space.append(next_path)

print(len(best_solution) - 1)
