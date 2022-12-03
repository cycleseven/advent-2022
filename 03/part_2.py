import itertools
import sys

lowercase_alphabet = (chr(n) for n in range(ord('a'), ord('z') + 1))
uppercase_alphabet = (chr(n) for n in range(ord('A'), ord('Z') + 1))
rucksack_items = itertools.chain(lowercase_alphabet, uppercase_alphabet)
priorities = { char: i + 1 for i, char in enumerate(rucksack_items) }

lines = (l.strip() for l in sys.stdin)
priority_sum = 0

elf_group = []

for line in lines:
    elf_group.append(set(line))

    if len(elf_group) == 3:
        common_item = set.intersection(*elf_group).pop()
        priority_sum += priorities[common_item]
        elf_group = []

print(priority_sum)
