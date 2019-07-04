#!usr/bin/env python3
from Graph import Graph
from Graph import Vertex

if __name__ == "__main__": 
    London = Vertex('London', {'Brussels': 50, 'Paris': 5, 'Granada': 78})
    Paris = Vertex('Paris', {'Brussels': 10, 'Granada': 30, 'London': 5})
    Granada = Vertex('Granada', {'London': 78, 'Paris': 30, 'Milan': 50, 'Athens': 81})
    Brussels = Vertex('Brussels', {'Paris': 10, 'London': 50, 'Oslo': 35, 'Vienna': 16})
    Oslo = Vertex('Oslo', {'Brussels': 35, 'Helsinki': 12})
    Helsinki = Vertex('Helsinki', {'Oslo': 12, 'Stockholm': 0})
    Stockholm = Vertex('Stockholm', {'Helsinki': 0, 'Stockholm': 1})
    Vienna = Vertex('Vienna', {'Stockholm': 1, 'Brussels': 16, 'Kiev': 0, 'Athens': 13, 'Rome': 10})
    Kiev = Vertex('Kiev', {'Vienna': 0})
    Athens = Vertex('Athens', {'Vienna': 13, 'Granada': 81})
    Rome = Vertex('Rome', {'Vienna': 10, 'Milan': 1})
    Milan = Vertex('Milan', {'Rome': 1, 'Granada': 50}) 

    GraphObject = Graph()
    GraphObject.print_graph()    