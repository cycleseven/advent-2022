import sys

shape_to_choose = {
    ('A', 'X'): 'C',
    ('A', 'Y'): 'A',
    ('A', 'Z'): 'B',

    ('B', 'X'): 'A',
    ('B', 'Y'): 'B',
    ('B', 'Z'): 'C',

    ('C', 'X'): 'B',
    ('C', 'Y'): 'C',
    ('C', 'Z'): 'A',
}

outcomes = {
    ('A', 'A'): 3,
    ('A', 'B'): 6,
    ('A', 'C'): 0,

    ('B', 'A'): 0,
    ('B', 'B'): 3,
    ('B', 'C'): 6,

    ('C', 'A'): 6,
    ('C', 'B'): 0,
    ('C', 'C'): 3,
}

shape_scores = {
    'A': 1,
    'B': 2,
    'C': 3,
}

total_score = 0

for line in sys.stdin:
    strategy = tuple(line.split())
    move = (strategy[0], shape_to_choose[strategy])
    total_score += outcomes[move] + shape_scores[move[1]]

print(total_score)