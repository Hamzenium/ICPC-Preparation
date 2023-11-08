def depth_first_search(graph, start):
    # This set will contain the nodes we have fully processed
    found_handled = set()

    # Stack for nodes we have found but not yet fully processed
    # Starts with the start node and an initial edge count of 0
    found_not_handled = [(start, 0)]

    # A dictionary to keep track of the parent of each node (the π function in the pseudocode)
    parent = {start: None}

    while found_not_handled:
        # Take the last node and edge count from the stack
        u, edge_count = found_not_handled[-1]

        # Try to find the (edge_count+1)th neighbor of u
        neighbors = list(graph[u])
        if edge_count < len(neighbors):
            v = neighbors[edge_count]
            # Update the edge count for u
            found_not_handled[-1] = (u, edge_count + 1)
            if v not in parent:  # Equivalent to "if v has not been found"
                parent[v] = u  # Set u as the parent of v
                found_not_handled.append((v, 0))  # Add v for processing
        else:
            # If no more neighbors, u has been fully processed
            found_not_handled.pop()
            found_handled.add(u)

    return found_handled, parent

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Running depth-first search on the example graph from node 'A'
dfs_result = depth_first_search(graph, 'A')
print(dfs_result)