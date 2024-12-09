# Vertex class for creating a graph nodes
class Vertex:

    # Vertex constructor
    def __self__(self, key):
        self.id = key
        self.connectedTo = {}

    # Adding a neighbor node connecting to current node
    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    # Return the connecting vertexes/all neighbors
    def get_connections(self):
        return self.connectedTo.keys()

    # Return the id of the node
    def get_id(self):
        return self.id

    # Return the weight of the edge between the vertices
    def get_weight(self, nbr):
        return self.connectedTo[nbr]

class UndirectedGraph:
    # UndirectedGraph constructor
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
    
    # Adds a vertex to the list of vertexs
    def add_vertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    # returns a vertex that's key is equals the parameter
    def get_vertex(self, key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    # Adds an edge from one vertex to another and assigns a weight
    def add_edge(self, from_key, to_key, weight=0):
        if from_key not in self.vertList:
            self.add_vertex(from_key)
        if to_key not in self.vertList:
            self.add_vertex(to_key)

    # Returns a list of vertices
    def get_vertices(self):
        return self.vertList.keys()

    
    # Returns a boolean value based on whether a key is found in the listed survivor
    def contains(self, key):
      if key in self.vertList:
        return True
      else:
        return False

    # Clears the graph
    def clear(self):
        self.vertList = {}
        self.numVertices = 0

    # Checks if the graph is empty
    def is_empty(self):
        if self.numVertices == 0:
            return True
        else:
            return False

    # Returns the size of the graph
    def size(self):
        return len(self.numVertices)

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
