import sys

outcomes = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,

    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,

    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

total_score = 0

for line in sys.stdin:
    move = tuple(line.split())
    total_score += outcomes[move] + shape_scores[move[1]]

print(total_score)