import sys

interesting_cycles = {20, 60, 100, 140, 180, 220}
x = 1
instruction = None
total_signal_strength = 0

def read_next_instruction():
    line = sys.stdin.readline()

    if line == '':
        return None

    command, *argv = line.split()

    if command == 'noop':
        cycles_remaining = 1
    elif command == 'addx':
        cycles_remaining = 2

    return {
        'command': command,
        'argv': argv,
        'cycles_remaining': cycles_remaining
    }

for cycle in range(1, 221):
    if instruction is None or instruction['cycles_remaining'] < 1:
        instruction = read_next_instruction()

    if cycle in interesting_cycles:
        total_signal_strength += cycle * x

    if instruction is None:
        continue

    if (
        instruction['cycles_remaining'] == 1
        and instruction['command'] == 'addx'
    ):
        x += int(instruction['argv'][0])

    instruction['cycles_remaining'] -= 1

print(total_signal_strength)
