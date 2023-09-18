
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
    return distanc
