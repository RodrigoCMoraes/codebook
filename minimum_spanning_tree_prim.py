def prim(graph):
  # Initialize the minimum spanning tree.
  mst = []

  # Initialize the set of vertices that have been added to the minimum spanning tree.
  vertices_in_mst = set()

  # Initialize the vertex that is currently being considered for addition to the minimum spanning tree.
  current_vertex = None

  # While there are still vertices that have not been added to the minimum spanning tree:
  while len(vertices_in_mst) < len(graph):

    # Find the edge with the minimum weight that connects the current vertex to a vertex that is not in the minimum spanning tree.
    min_edge = None
    for edge in graph[current_vertex]:
      if edge[1] not in vertices_in_mst:
        if min_edge is None or edge[0] < min_edge[0]:
          min_edge = edge

    # Add the edge to the minimum spanning tree.
    mst.append(min_edge)

    # Add the vertex that was connected to the edge to the set of vertices that have been added to the minimum spanning tree.
    vertices_in_mst.add(min_edge[1])

    # Set the current vertex to the vertex that was connected to the edge.
    current_vertex = min_edge[1]

  return mst
