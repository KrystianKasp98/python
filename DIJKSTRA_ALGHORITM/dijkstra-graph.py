graph = {
    'A': {'B': 2, 'D': 4},
    'B': {'C': 3, 'D': 3},
    'C': {'E': 2},
    'D': {'C': 3, 'E': 4},
    'E': {}
}

graph_route = {
    'A': [],
    'B': [],
    'C': [],
    'D': [],
    'E': [],
}


def get_cheapest_node(costs_dict, processed_list):
    cheapest_cost = float('inf')
    cheapest_key = None

    for _name, _cost in costs_dict.items():
        if _name not in processed_list and _cost < cheapest_cost:
            cheapest_cost = _cost
            cheapest_key = _name

    return cheapest_key


costs = {}
parents = {}

# init
for name in graph.keys():
    costs[name] = float('inf')

processed = []
current_node = 'A'
costs[current_node] = 0
parents[current_node] = None

while current_node:
    #  calculate code of the neighbours
    for neighbour in graph[current_node]:
        if costs[neighbour] > costs[current_node] + graph[current_node][neighbour]:
            costs[neighbour] = costs[current_node] + graph[current_node][neighbour]
            parents[neighbour] = current_node

    processed.append(current_node)
    current_node = get_cheapest_node(costs, processed)

for vector, cost in costs.items():
    print(f'The cost for {vector} is {cost}')

    current_vector = vector
    while parents[current_vector]:
        print(current_vector)
        if not vector == current_vector:
            graph_route[vector].append(current_vector)
        current_vector = parents[current_vector]
    else:
        graph_route[vector].append(current_vector)
        graph_route[vector].reverse()
        print(current_vector)

print(processed)
print(costs)
print(parents)
print(graph_route)
