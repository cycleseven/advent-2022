import itertools
import sys

lowercase_alphabet = (chr(n) for n in range(ord('a'), ord('z') + 1))
uppercase_alphabet = (chr(n) for n in range(ord('A'), ord('Z') + 1))
rucksack_items = itertools.chain(lowercase_alphabet, uppercase_alphabet)
priorities = { char: i + 1 for i, char in enumerate(rucksack_items) }

lines = (l.strip() for l in sys.stdin)
priority_sum = 0

for line in lines:
    midpoint = int(len(line) * 0.5)
    first_compartment = set(line[0:midpoint])
    second_compartment = set(line[midpoint:])
    common_item = first_compartment.intersection(second_compartment).pop()
    priority_sum += priorities[common_item]

print(priority_sum)
