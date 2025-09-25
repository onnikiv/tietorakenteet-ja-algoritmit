def dijkstra_shortest_path(source_vertex, destination_vertex, graph):

    unvisited_vertices = graph.get_vertices()
    shortest_path_table = { vertex: {'shortest': float('inf'), 'previous': None } for vertex in unvisited_vertices}

    shortest_path_table[source_vertex]['shortest'] = 0

    while unvisited_vertices:
        current_vertex = min(unvisited_vertices, key=lambda vertex: shortest_path_table[vertex]['shortest'])
        distance_from_source = shortest_path_table[current_vertex]['shortest']
        unvisited_adjacent_vertices = (v for v in graph.get_adjacent_vertices(current_vertex) if v in unvisited_vertices)
        for adjacent_vertex in unvisited_adjacent_vertices:
            edge = graph.get_edge(current_vertex, adjacent_vertex)
            if edge is not None:
                tentative_distance = distance_from_source + edge.value()
                if tentative_distance < shortest_path_table[adjacent_vertex]['shortest']:
                    shortest_path_table[adjacent_vertex]['shortest'] = tentative_distance
                    shortest_path_table[adjacent_vertex]['previous'] = current_vertex
        unvisited_vertices.remove(current_vertex)

    # Reconstruct path from destination to source
    path = []
    current = destination_vertex
    while current:
        path.append(current)
        current = shortest_path_table[current]['previous']
    path = path[::-1]

    min_distance = shortest_path_table[destination_vertex]['shortest']
    if min_distance == float('inf'):
        return (None, [])  # No path found
    return (min_distance, path)
