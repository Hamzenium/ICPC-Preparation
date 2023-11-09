def ford_fulkerson(graph, source, sink):
    """
    Ford-Fulkerson algorithm to find maximum flow in a network
    graph: dictionary of dictionaries where keys are node names and values are dictionaries of adjacent nodes with their capacities
    source: starting node for flow
    sink: ending node for flow
    Returns the value of the maximum flow
    """

    def dfs(graph, visited, node, flow):
        if node == sink:
            return flow
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                residual_capacity = graph[node][neighbour]['capacity'] - graph[node][neighbour]['flow']
                if residual_capacity > 0:
                    min_flow = min(flow, residual_capacity)
                    result_flow = dfs(graph, visited, neighbour, min_flow)
                    if result_flow > 0:
                        graph[node][neighbour]['flow'] += result_flow
                        # Assuming graph is bidirectional
                        graph[neighbour][node]['flow'] -= result_flow
                        return result_flow
        return 0

    # Initialize flow for each edge to 0
    for node in graph:
        for neighbour in graph[node]:
            graph[node][neighbour]['flow'] = 0

    max_flow = 0
    flow = dfs(graph, set(), source, float('inf'))
    while flow > 0:
        max_flow += flow
        flow = dfs(graph, set(), source, float('inf'))
    return max_flow

# Example graph as a dictionary of dictionaries
graph = {
    'S': {'A': {'capacity': 3, 'flow': 0}, 'B': {'capacity': 2, 'flow': 0}},
    'A': {'C': {'capacity': 3, 'flow': 0}, 'T': {'capacity': 2, 'flow': 0}},
    'B': {'C': {'capacity': 2, 'flow': 0}, 'D': {'capacity': 3, 'flow': 0}},
    'C': {'T': {'capacity': 4, 'flow': 0}, 'D': {'capacity': 1, 'flow': 0}},
    'D': {'T': {'capacity': 3, 'flow': 0}},
    'T': {}
}

max_flow_value = ford_fulkerson(graph, 'S', 'T')
print(f"The maximum possible flow is: {max_flow_value}")