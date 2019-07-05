#!usr/bin/env python3
from collections import defaultdict

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
    
    def get_edges(self):
        return len(self.edges)
    
    def print_graph(self):
        print([vertex for vertex in self.vertices])