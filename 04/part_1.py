import sys

fully_contained_pairs = 0

for line in sys.stdin:
    # Parse a string like "2-4,6-8\n" into two variables:
    # a = [2, 4]
    # b = [6, 8]
    a, b = [
        [int(x) for x in pair.split('-')]
        for pair in line.strip().split(',')
    ]

    a_contains_b = a[0] <= b[0] and a[1] >= b[1]
    b_contains_a = b[0] <= a[0] and b[1] >= a[1]

    if a_contains_b or b_contains_a:
        fully_contained_pairs += 1

print(fully_contained_pairs)
