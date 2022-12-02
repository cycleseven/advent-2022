import sys

calories_for_current_elf = 0
max_calories = [0, 0, 0]

def update_max_calories(calories_for_current_elf, max_calories):
    for i, impressive_calorie_count in enumerate(max_calories):
        if calories_for_current_elf > impressive_calorie_count:
            max_calories.insert(i, calories_for_current_elf)
            max_calories.pop(-1)
            return

for line in sys.stdin:
    if line == '\n':
        update_max_calories(calories_for_current_elf, max_calories)
        calories_for_current_elf = 0
        continue

    calories_for_current_elf += int(line)

update_max_calories(calories_for_current_elf, max_calories)
print(sum(max_calories))