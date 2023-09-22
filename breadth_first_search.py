
from collections import defaultdict


def bfs(n, m, edges, s):
    adj = defaultdict(list)
    for (u, v) in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    visited = [False] * (n + 1)
    distance = [0] * (n + 1)
    
    queue = [s]
    visited[s] = True
    while len(queue) > 0:
       u = queue.pop(0) # pop front 
       for v in adj[u]:
           if visited[v]:
              continue
           visited[v] = True
           distance[v] = distance[u] + 6
           queue.append(v)
    for i, d in enumerate(distance):
        if d == 0:
            distance[i] = -1
    del distance[s]
    del distance[0]
    return distance


def bfs(graph, start):
  # Initialize the queue and the set of visited nodes.
  queue = []
  visited = set()

  # Add the starting node to the queue.
  queue.append(start)

  # While the queue is not empty:
  while queue:

    # Remove the next node from the queue.
    node = queue.popleft()

    # Mark the node as visited.
    visited.add(node)

    # Add the node's neighbors to the queue.
    for neighbor in graph[node]:
      if neighbor not in visited:
        queue.append(neighbor)

  # Return the list of visited nodes.
  return list(visited)
