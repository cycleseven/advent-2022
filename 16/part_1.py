# 💩

import functools
import sys

def parse_valves():
    valves = {}

    for line in sys.stdin:
        # `tokens` looks like this...
        # ['Valve', 'ZN', 'has', 'flow', 'rate=0;', 'tunnels', 'lead, 'to', 'valves', 'SD,' 'ZV']
        tokens = line.split()

        name = tokens[1]
        flow_rate = int(tokens[4][:-1].split('=')[1])
        neighbours = {x.replace(',', '') for x in tokens[9:]}

        valves[name] = { 'flow_rate': flow_rate, 'neighbours': neighbours }

    return valves

valves = parse_valves()

@functools.cache
def get_distance(a, b):
    """Compute distance via breadth-first search"""
    valves_to_visit = [a]
    distances = {
        a: 0
    }

    while len(valves_to_visit) > 0:
        parent = valves_to_visit.pop(0)
        neighbours = valves[parent]['neighbours']

        for neighbour in neighbours:
            distances[neighbour] = distances[parent] + 1

            if neighbour == b:
                return distances[neighbour]

            valves_to_visit.append(neighbour)

def max_possible_pressure(remaining_valves, init_remaining_minutes):
    remaining_minutes = init_remaining_minutes
    total_pressure = 0

    for _, flow_rate in sorted(remaining_valves.items(), key=lambda item: item[1]):
        remaining_minutes -= 1
        total_pressure += remaining_minutes * flow_rate

    return total_pressure

initial_useful_valves = {
    name: valve['flow_rate']
    for name, valve in valves.items()
    if valve['flow_rate'] > 0
}

solution_space = [
    {
        'path': ['AA'],
        'remaining_minutes': 30,
        'actual_pressure': 0,
        'max_possible_additional_pressure': max_possible_pressure(initial_useful_valves, 30),
        'useful_valves': initial_useful_valves
    }
]

def is_incomplete(solution):
    return solution['remaining_minutes'] > 0 or solution['max_possible_additional_pressure'] > 0

def is_viable(solution):
    return solution['actual_pressure'] + solution['max_possible_additional_pressure'] > best_pressure

best_pressure = 0
best_solution = []

while len(solution_space) > 0:
    print(f'Size of solution space: {len(solution_space)}')
    solution = solution_space.pop(0)

    for valve, flow_rate in solution['useful_valves'].items():
        remaining_minutes = solution['remaining_minutes'] - get_distance(solution['path'][-1], valve) - 1
        remaining_valves = {
            remaining_valve: flow_rate
            for remaining_valve, flow_rate in solution['useful_valves'].items()
            if remaining_valve != valve
        }

        next_solution = {
            'path': solution['path'] + [valve],
            'remaining_minutes': remaining_minutes,
            'actual_pressure': solution['actual_pressure'] + (remaining_minutes * flow_rate),
            'max_possible_additional_pressure': max_possible_pressure(remaining_valves, remaining_minutes),
            'useful_valves': remaining_valves
        }

        if next_solution['actual_pressure'] > best_pressure:
            best_pressure = next_solution['actual_pressure']
            best_solution = next_solution['path']

        if is_incomplete(next_solution) and is_viable(next_solution):
            solution_space.append(next_solution)
        else:
            print('Done exploring path:', next_solution['path'])

print()
print(f'Solution {best_solution} gives the best pressure: {best_pressure}')
