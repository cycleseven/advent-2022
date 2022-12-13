import sys

class Coord():
    """An x, y point on the grid. x increases to the right, y increases upwards."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def add(self, other):
        return Coord(self.x + other.x, self.y + other.y)

    def subtract(self, other):
        return Coord(self.x - other.x, self.y - other.y)

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

starting_point = Coord(0, 0)
knots = [starting_point] * 10

directions = {
    'R': Coord(1, 0),
    'L': Coord(-1, 0),
    'U': Coord(0, 1),
    'D': Coord(0, -1),
}

def parse_line(line):
    segments = line.split()
    return segments[0], int(segments[1])

def clamp(value):
    return max(-1, min(value, 1))

visited_coords = set([starting_point])

for line in sys.stdin:
    direction, steps = parse_line(line)

    for step in range(steps):
        for i, knot in enumerate(knots):
            if i == 0:
                knots[0] = knots[0].add(directions[direction])
                continue

            leading_knot = knots[i - 1]
            distance = leading_knot.subtract(knot)
            manhattan_distance = leading_knot.manhattan_distance(knot)
            is_diagonal = leading_knot.x != knot.x and leading_knot.y != knot.y
            threshold = 3 if is_diagonal else 2

            if manhattan_distance >= threshold:
                knots[i] = knot.add(
                    Coord(clamp(distance.x), clamp(distance.y))
                )

            if i == 9:
                visited_coords.add(knots[i])

print(len(visited_coords))
