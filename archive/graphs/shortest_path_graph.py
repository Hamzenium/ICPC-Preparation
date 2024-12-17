from collections import deque

def shortest_path(G, s):
    foundHandled = set()  # Nodes whose shortest path has been found
    foundNotHandled = set([s])  # Nodes seen but whose shortest path not finalized
    d = {s: 0}  # Distance from s to s is 0
    pi = {s: None}  # Predecessor of s is undefined

    queue = deque([s])  # Queue to manage nodes to visit, starting with s

    while queue:
        u = queue.popleft()  # Node u taken from front of queue
        for v in G[u]:  # For each node v connected to u
            if v not in foundHandled and v not in foundNotHandled:
                foundNotHandled.add(v)
                d[v] = d[u] + 1  # Distance to v is one more than distance to u
                pi[v] = u  # Predecessor of v is u
                queue.append(v)  # Add v to queue to process its neighbours
        foundNotHandled.remove(u)
        foundHandled.add(u)  # Move u to handled after processing all its neighbours

    # For nodes not found, set distance to infinity and predecessor to None
    all_nodes = set(G.keys())
    for v in all_nodes - foundHandled:
        d[v] = float('inf')
        pi[v] = None

    return d, pi  # Return distances and predecessors

# Example of a graph represented as an adjacency list
G_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Execute the function with graph G and source node 'A'
distances, predecessors = shortest_path(G_example, 'A')

print("Distances:", distances)
print("Predecessors:", predecessors)
