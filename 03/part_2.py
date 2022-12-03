import sys

def get_priority(rucksack_item):
    ascii_code = ord(rucksack_item)

    if ord(rucksack_item) > 90:
        return ascii_code - 96

    return ascii_code - 38

lines = (l.strip() for l in sys.stdin)
priority_sum = 0

elf_group = []

for line in lines:
    elf_group.append(set(line))

    if len(elf_group) == 3:
        common_item = set.intersection(*elf_group).pop()
        priority_sum += get_priority(common_item)
        elf_group = []

print(priority_sum)
