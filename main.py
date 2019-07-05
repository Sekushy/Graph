#!usr/bin/env python3
from Graph import Graph

if __name__ == "__main__": 
    graph = Graph()
    for vertex in ['London', 'Brussels', 'Paris', 'Granada', 'Milan', 'Rome', 'Vienna', 'Athens', 'Oslo', 'Kiev', 'Stockholm', 'Helsinki']:
        graph.add_vertex(vertex)
    
    graph.print_graph()
    print(graph.get_edges())
