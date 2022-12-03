import sys

def get_priority(rucksack_item):
    ascii_code = ord(rucksack_item)

    if ord(rucksack_item) > 90:
        return ascii_code - 96

    return ascii_code - 38

lines = (l.strip() for l in sys.stdin)
priority_sum = 0

for line in lines:
    midpoint = int(len(line) * 0.5)
    first_compartment = set(line[0:midpoint])
    second_compartment = set(line[midpoint:])
    common_item = first_compartment.intersection(second_compartment).pop()
    priority_sum += get_priority(common_item)

print(priority_sum)
