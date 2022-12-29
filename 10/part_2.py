import sys

x = 1
instruction = None

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

for crt_y in range(6):
    for crt_x in range(40):
        if instruction is None or instruction['cycles_remaining'] < 1:
            instruction = read_next_instruction()

        if x - 1 <= crt_x <= x + 1:
            print('#', end='')
        else:
            print('.', end='')

        if instruction is None:
            continue

        if (
            instruction['cycles_remaining'] == 1
            and instruction['command'] == 'addx'
        ):
            x += int(instruction['argv'][0])

        instruction['cycles_remaining'] -= 1

    print()
