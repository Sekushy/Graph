#!usr/bin/env python3
class Vertex():
    def __init__ (self, name = '', neighbours = {}):
        self.name = name
        self.neighbours = neighbours

    def add_neighbour(self, neighbourToBeAdded):
        self.neighbours.update(neighbourToBeAdded)

    def __str__ (self):
        return "Vertex: {} with neighbours {}".format(self.name, self.neighbours)

class Graph():
    def __init__(self, vertices = list()):
        self.vertices = vertices

    def add_vertex(self, vertexToBeAdded):
        if vertexToBeAdded in self.vertices:
            pass
        else:
            self.vertices.append(vertexToBeAdded)

    def remove_vertex(self, vertexToBeRemoved):
        if vertexToBeRemoved in self.vertices:
            self.vertices.remove(vertexToBeRemoved)
        else:
            pass
    
    def get_numberOfVertices(self):
        return len(self.vertices)

    def print_graph(self):
        for vertex in self.vertices:
            print(vertex)