import sys

overlapping_pairs = 0

for line in sys.stdin:
    # Parse a string like "2-4,6-8\n" into two variables:
    # a = [2, 4]
    # b = [6, 8]
    a, b = [
        [int(x) for x in pair.split('-')]
        for pair in line.strip().split(',')
    ]

    if a[1] < b[0] or a[0] > b[1]:
        continue

    overlapping_pairs += 1

print(overlapping_pairs)
