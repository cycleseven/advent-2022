import sys

is_parsing_stacks = True
stacks = []

for line in sys.stdin:
    # Shit parsing code for initial stack configuration

    # Use the blank line as the boundary between initial stack config
    # and the rearrangement procedure
    if line == '\n':
        is_parsing_stacks = False
        continue

    # Crate letters appear at positions 1, 5, 9... (every 4 characters beginning at position 1).
    if is_parsing_stacks:
        # Just ignore the line with the stack numbers, it's useful for humans,
        # not that useful for this program
        if line.startswith(' 1'):
            continue

        crates = [x for i, x in enumerate(line[1:]) if i % 4 == 0]

        if stacks == []:
            for crate in crates:
                if crate == ' ':
                    stacks.append([])
                else:
                    stacks.append([crate])
            continue

        for i, crate in enumerate(crates):
            if crate == ' ':
                continue
            stacks[i].insert(0, crate)

        continue

    # shit parsing code is over, sorry

    count, from_stack, to_stack = [int(x) for i, x in enumerate(line.split()) if i % 2 == 1]

    # Convert from human readable stack numbers to zero-indexed
    from_stack -= 1
    to_stack -= 1

    stacks[to_stack] = stacks[to_stack] + stacks[from_stack][-count:]
    del stacks[from_stack][-count:]

print(''.join(stack[-1] for stack in stacks))
