def search(graph, start):
    found_handled = set()  # Set to keep track of handled nodes
    found_not_handled = {start}  # Set to keep track of nodes found but not handled

    while found_not_handled:
        # Take a node from found_not_handled
        current_node = found_not_handled.pop()
        # Process the current node
        found_handled.add(current_node)
        # Add connected nodes to found_not_handled if they haven't been found yet
        for neighbor in graph[current_node]:
            if neighbor not in found_handled and neighbor not in found_not_handled:
                found_not_handled.add(neighbor)

    return found_handled

# Example usage:
# Define a simple graph as an adjacency list
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Call the search function with the graph and starting node 'A'
reachable_nodes = search(graph_example, 'A')
print("Nodes reachable from 'A':", reachable_nodes)
