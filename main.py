#!usr/bin/env python3
from Graph import Graph

if __name__ == "__main__": 
    graph = Graph()
    for vertex in ['London', 'Brussels', 'Paris', 'Granada', 'Milan', 'Rome', 'Vienna', 'Athens', 'Oslo', 'Kiev', 'Stockholm', 'Helsinki']:
        graph.add_vertex(vertex)

    # London
    graph.add_edge('London', 'Brussels', 50)
    graph.add_edge('London', 'Paris', 5)
    graph.add_edge('London', 'Granada', 78)
    # Granada
    graph.add_edge('Granada', 'Paris', 30)
    graph.add_edge('Granada', 'Milan', 50)
    graph.add_edge('Granada', 'Athens', 81)
    # Athens
    graph.add_edge('Athens', 'Vienna', 13)
    # Vienna
    graph.add_edge('Vienna', 'Rome', 10)
    graph.add_edge('Vienna', 'Brussels', 16)
    graph.add_edge('Vienna', 'Kiev', 0)
    graph.add_edge('Vienna', 'Stockholm', 1)
    # Stockholm
    graph.add_edge('Stockholm', 'Helsinki', 0)
    # Helsinki
    graph.add_edge('Helsinki', 'Oslo', 12)
    # Oslo
    graph.add_edge('Oslo', 'Brussels', 35)
    # Milan
    graph.add_edge('Milan', 'Rome', 1)

    print(graph.get_shortest_path('London', 'Kiev'))