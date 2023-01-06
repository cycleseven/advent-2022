import math
import sys

class Monkey:
    def __init__(self, boost_worry=None):
        self.boost_worry = boost_worry
        self.inspections = 0
        self.items = []

    def parse_operation(self, operation):
        """Make loads of assumptions about the operation string, return a function that executes the arithmetic"""

        left_operand_string, operator, right_operand_string = operation.split()[2:]

        def boost_worry(old):
            nonlocal left_operand_string
            nonlocal right_operand_string

            if left_operand_string == 'old':
                left_operand = old
            else:
                left_operand = int(left_operand_string)

            if right_operand_string == 'old':
                right_operand = old
            else:
                right_operand = int(right_operand_string)

            if operator == '*':
                return left_operand * right_operand
            elif operator == '+':
                return left_operand + right_operand

        self.boost_worry = boost_worry

    def parse_divisor(self, test_string):
        self.divisor = int(test_string.split()[-1])

    def parse_target_monkey(self, branch_string, polarity):
        monkey_id = int(branch_string.split()[-1])

        if polarity:
            self.true_monkey = monkey_id
        else:
            self.false_monkey = monkey_id


def parse_input():
    monkeys = {}
    current_monkey_id = None

    for line in sys.stdin:
        if line.startswith("Monkey "):
            id = int(line.split()[1][:-1])
            current_monkey_id = id
            monkeys[id] = Monkey()
        elif line.startswith("  Starting items: "):
            worry_levels = (int(x.strip()) for x in line[18:].split(","))
            monkeys[current_monkey_id].items += worry_levels
        elif line.startswith("  Operation: "):
            monkeys[id].parse_operation(line[13:])
        elif line.startswith("  Test: "):
            monkeys[id].parse_divisor(line[8:])
        elif line.startswith("    If true: "):
            monkeys[id].parse_target_monkey(line[13:], True)
        elif line.startswith("    If false: "):
            monkeys[id].parse_target_monkey(line[13:], False)

    return monkeys

monkeys = parse_input()

for round in range(20):
    for monkey_id, monkey in monkeys.items():
        for worry_level in monkey.items:
            monkey.inspections += 1
            worry_level = int(monkey.boost_worry(worry_level) / 3)

            if worry_level % monkey.divisor == 0:
                target_monkey = monkey.true_monkey
            else:
                target_monkey = monkey.false_monkey

            monkeys[target_monkey].items.append(worry_level)

        monkey.items = []

sorted_monkeys = sorted(
    monkeys.values(),
    key=lambda m: m.inspections,
    reverse=True
)

monkey_business = math.prod(m.inspections for m in sorted_monkeys[:2])
print(monkey_business)
