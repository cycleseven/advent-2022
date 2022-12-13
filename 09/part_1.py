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

head_position = Coord(0, 0)
tail_position = Coord(0, 0)

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

visited_coords = set([tail_position])

for line in sys.stdin:
    direction, steps = parse_line(line)

    for _ in range(steps):
        head_position = head_position.add(directions[direction])
        distance = head_position.subtract(tail_position)
        manhattan_distance = head_position.manhattan_distance(tail_position)
        is_diagonal = head_position.x != tail_position.x and head_position.y != tail_position.y
        threshold = 3 if is_diagonal else 2

        if manhattan_distance >= threshold:
            tail_movement = Coord(
                clamp(distance.x),
                clamp(distance.y)
            )
            tail_position = tail_position.add(tail_movement)
            visited_coords.add(tail_position)

print(len(visited_coords))
