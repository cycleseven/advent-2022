import sys

calories_for_current_elf = 0
max_calories = 0

for line in sys.stdin:
    if line == '\n':
        max_calories = max(calories_for_current_elf, max_calories)
        calories_for_current_elf = 0
        continue

    calories_for_current_elf += int(line)

print(max(calories_for_current_elf, max_calories))