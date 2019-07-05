#!usr/bin/env python3
from collections import defaultdict, deque

class Graph(object):
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
    
    def get_edges(self):
        return len(self.edges)
    
    def print_graph(self):
        print([vertex for vertex in self.vertices])
    
    def dijkstra(self, origin):
        visited = {origin : 0}
        path = {}
        vertices = set(self.vertices)

        while vertices:
            minimum = None
            for vertex in vertices:
                if vertex in visited:
                    if minimum is None:
                        minimum = vertex
                    elif visited[vertex] < visited[minimum]:
                        minimum = vertex
            if minimum is None:
                break

            vertices.remove(minimum)
            current_weight = visited[minimum]

            for edge in self.edges[minimum]:
                try:
                    weight = current_weight + self.distances[(minimum, edge)]
                except:
                    continue
                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = minimum
        return visited, path

    def get_shortest_path(self, origin, destination):
        visited, paths = self.dijkstra(origin)
        full_path = deque()
        
        _destination = paths[destination]

        while _destination != origin:
            full_path.appendleft(_destination)
            _destination = paths[_destination]

        full_path.appendleft(origin)
        full_path.append(destination)

        return visited[destination], list(full_path)