lines = {
    'BE': ['IT', 'DE'],
    'IT': ['ES', 'PT'],
    'DE': ['PL'],
    'LT': ['SE'],
    'ES': ['DE', 'BE'],
    'PT': ['ES'],
    'PL': ['LT'],
    'SE': []
}

route1 = {
    'IT': ['PT'],
    'PT': ['ES'],
    'ES': ['BE', 'DE']
}

route2 = {
    'BE': ['DE'],
    'DE': ['SE']
}

route3 = {
    'GB': ['BE'],
    'BE': ['DE']
}


def is_subgraph(V, V_sub):
    for v in V_sub.keys():
        # missing vector
        if not v in V.keys():
            print(f'missing node: {v}')
            return False
        else:
            for e in V_sub[v]:
                # missing edge for vector
                if not e in V[v]:
                    print(f'missing connection: {v}, {e}')
                    return False
    return True


print(is_subgraph(lines, route1))
print(is_subgraph(lines, route2))
print(is_subgraph(lines, route3))

