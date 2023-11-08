import heapq

def dijkstra(G, s):
    # Initialize distances to all nodes as infinity and to source node s as 0
    d = {v: float('inf') for v in G}
    d[s] = 0
    # Initialize predecessors for all nodes as None
    pi = {v: None for v in G}
    
    # The priority queue to select the node with the smallest distance
    notHandled = [(0, s)]  # (distance, node)
    
    # To keep track of nodes whose shortest path is known
    handled = set()

    while notHandled:
        # Pop a node with the smallest distance d(u)
        _, u = heapq.heappop(notHandled)
        
        # Skip the node if it's already handled
        if u in handled:
            continue
        
        # For each neighbor v of node u
        for v, weight in G[u].items():
            # Calculate the distance to v through u
            foundPathLength = d[u] + weight
            
            # If the calculated distance is less than the known distance
            if foundPathLength < d[v]:
                # Update the distance and predecessor
                d[v] = foundPathLength
                pi[v] = u
                
                # Add the neighbor to the not handled list with the new distance
                heapq.heappush(notHandled, (foundPathLength, v))
        
        # Add u to the handled set
        handled.add(u)

    return d, pi

# Example graph represented with adjacency list and weights
G_example = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 1},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 3},
    'F': {'C': 1, 'E': 3}
}
graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 1},
    'C': {'A': 4, 'B': 1, 'D': 3},
    'D': {'C': 3}
}



# Execute the function with the graph G and source node 'A'
distances, predecessors = dijkstra(graph, 'A')

print("Distances:", distances)
print("Predecessors:", predecessors)
