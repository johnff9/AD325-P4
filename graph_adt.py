# Vertex class for creating a graph nodes
class Vertex:

    # Vertex constructor
    def __self__(self, key):
        pass

    # Adding a neighbor node connecting to current node
    def addNeighbor(self, nbr, weight=0):
        pass

    # Return the connecting vertexes/all neighbors
    def get_connections(self):
        pass

    # Return the id of the node
    def get_id(self):
        pass

    # Return the weight of the edge between the vertices
    def get_weight(self, nbr):
        pass

class UndirectedGraph:
    # UndirectedGraph constructor
    def __init__(self):
        pass
    
    # Adds a vertex to the list of vertexs
    def add_vertex(self, key):
        pass

    # returns a vertex that's key is equals the parameter
    def get_vertex(self, key):
        pass

    # Adds an edge from one vertex to another and assigns a weight
    def add_edge(self, from_key, to_key, weight=0):
        pass

    # Returns a list of vertices
    def get_vertices(self):
        pass

    
    # Returns a boolean value based on whether a key is found in the listed survivor
    def contains(self, key):
        pass

    # Clears the graph
    def clear(self):
        pass

    # Checks if the graph is empty
    def is_empty(self):
        pass

    # Returns the size of the graph
    def size(self):
        pass

    # Returns an edgelist
    def get_edges(self):
        pass


    # This is a breadth-first approach to searching
    def bfs(self, start):
         # This implementation should use a queue.
        pass

    # This is the depth-first
    def dfs(self, start):
        pass
