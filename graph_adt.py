from linked_adts import LinkedQueue

# Vertex class for creating a graph nodes
class Vertex:

    # Vertex constructor
    def __init__(self, key):
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
        if(self.get_vertex(from_key).get_id in self.get_vertex(to_key).get_connections()):
            print("Duplicates")
        else:
            self.get_vertex(from_key).addNeighbor(to_key, weight)
            self.get_vertex(to_key).addNeighbor(from_key, weight)

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
        edgeList=[]
        for v in self.vertList.values():
            for n in v.get_connections():
                edgeList.append(v.get_id(), n)
        return edgeList            
    
    def remove(self, key):
        pass


    # This is a breadth-first approach to searching
    def bfs(self, start):
        visited = set()  # Set to keep track of visited vertices
        queue = LinkedQueue()  # Initialize a queue for BFS traversal
        traversal_order = LinkedQueue()  # Queue to store the BFS traversal order

        queue.enqueue(start)  # Start BFS with the starting vertex
        visited.add(start)

        while not queue.is_empty():
            current = queue.dequeue()  # Dequeue a vertex

            # Enqueue all unvisited neighbors
            for neighbor in self.get_vertex(current).get_connections():
                if neighbor not in visited:
                    queue.enqueue(neighbor)
                    visited.add(neighbor)

        
        traversal_order = LinkedQueue()  # Initialize a LinkedQueue for storing traversal order
        # Use a temporary LinkedQueue to store the vertex IDs
        temp_queue = LinkedQueue()
        temp_queue = traversal_order

        while not temp_queue.is_empty():
            vertex_id = temp_queue.dequeue()  # Dequeue a vertex ID
            vertex = self.getVertex(vertex_id)  # Get the Vertex object
            # Replace the vertex ID with the UserProfile name
            if vertex:  # Check if the vertex exists in the graph
                user_profile_name = vertex.getId()  # Assuming getId() returns the UserProfile name
                traversal_order.enqueue(user_profile_name)  # Enqueue the UserProfile name

        return traversal_order  # Return the LinkedQueue containing UserProfile names

    # This is a depth-first approach to searching
    def dfs(self, start):
        visited = set()  # Set to keep track of visited vertices
        traversal_order = LinkedQueue()  # Queue to store the DFS traversal order

        def dfs_helper(vertex):
            visited.add(vertex)  # Mark the vertex as visited
            traversal_order.enqueue(vertex)  # Add it to the traversal queue

            # Recursively visit all unvisited neighbors
            for neighbor in self.get_vertex(vertex).get_connections():
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start)  # Call the helper function starting from the given vertex
        temp_queue = LinkedQueue()
        temp_queue = traversal_order
        while not temp_queue.is_empty():
            vertex_id = temp_queue.dequeue()  # Dequeue a vertex ID
            vertex = self.getVertex(vertex_id)  # Get the Vertex object
            # Replace the vertex ID with the UserProfile name
            if vertex:  # Check if the vertex exists in the graph
                user_profile_name = vertex.getId()  # Assuming getId() returns the UserProfile name
                traversal_order.enqueue(user_profile_name)  # Enqueue the UserProfile name


        return traversal_order  # Return the LinkedQueue containing UserProfile names


