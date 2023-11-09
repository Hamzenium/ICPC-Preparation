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



# First, let's define a function that represents the algorithm in Python.

def network_flow(G, s, t):
    # G: graph represented as a dictionary where G[u][v] is the capacity from u to v
    # s: source vertex
    # t: sink vertex
    
    # Initialize flow with zero capacity
    F = {u: {v: 0 for v in G[u]} for u in G}
    
    def find_path(GF, s, t, path):
        # Find path from s to t using DFS
        if s == t:
            return path
        for v in GF[s]:
            if GF[s][v] > 0 and not (s, v) in path:
                res = find_path(GF, v, t, path + [(s, v)])
                if res != None:
                    return res
    
    while True:
        # Construct the residual graph GF
        GF = {u: {v: G[u][v] - F[u][v] for v in G[u]} for u in G}
        
        for u in F:
            for v in F[u]:
                # If there's a backward edge, include it in the residual graph with the flow as capacity
                if F[u][v] > 0 and u != s:
                    GF[v][u] = GF.get(v, {}).get(u, 0) + F[u][v]
        
        # Find path from s to t in the residual graph
        path = find_path(GF, s, t, [])
        if path == None:
            # If no path is found, then we have the max flow and min cut
            break
        # Find the minimum residual capacity along the path
        flow = min(GF[u][v] for u, v in path)
        # Augment the flow along the path
        for u, v in path:
            F[u][v] += flow
            F[v][u] -= flow
    
    # Construct the min cut (U, V)
    U = set([s])
    V = set(G.keys()) - U
    frontier = [s]
    while frontier:
        u = frontier.pop()
        for v in G[u]:
            if GF[u][v] > 0 and v not in U:
                U.add(v)
                V.discard(v)
                frontier.append(v)
    
    C = (U, V)
    return F, C

# Note: This is a basic implementation and may require additional functions or classes to handle more complex graphs.
# It also assumes that the graph G is given in a specific dictionary format with nested dictionaries for capacities.
