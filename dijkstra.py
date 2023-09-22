def dijkstra(graph, source):
  # Initialize the distances to infinity.
  distances = {node: float("inf") for node in graph}
  distances[source] = 0

  # Initialize the set of visited nodes.
  visited = set()

  # While there are still nodes to visit:
  while visited != set(graph.keys()):

    # Find the node with the minimum distance.
    node = min(distances, key=distances.get)

    # Add the node to the set of visited nodes.
    visited.add(node)

    # Update the distances of the node's neighbors.
    for neighbor in graph[node]:
      distances[neighbor] = min(distances[neighbor], distances[node] + graph[node][neighbor])

  return distances
