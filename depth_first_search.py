def dfs(graph, start_node):
  visited_nodes = set()
  stack = [start_node]

  while stack:
    node = stack.pop()
    if node not in visited_nodes:
      visited_nodes.add(node)
      stack.extend(graph[node])

  return visited_nodes
