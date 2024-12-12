from linked_adts import LinkedDictionary, LinkedQueue

# Vertex class for creating graph nodes
class Vertex:
    def __init__(self, key):
        self.id = key
        self.connected_to = {}

    def add_neighbor(self, nbr, weight=0):
        self.connected_to[nbr] = weight

    def get_connections(self):
        return self.connected_to.keys()

    def get_id(self):
        return self.id

    def get_weight(self, nbr):
        return self.connected_to.get(nbr, None)


class UndirectedGraph:
    def __init__(self):
        self.vertices = LinkedDictionary()

    def add_vertex(self, key):
        if not self.contains(key):
            self.vertices.add(key, Vertex(key))

    def get_vertex(self, key):
        return self.vertices.get_value(key)

    def add_edge(self, from_key, to_key, weight=0):
        if self.contains(from_key) and self.contains(to_key):
            self.get_vertex(from_key).add_neighbor(to_key, weight)
            self.get_vertex(to_key).add_neighbor(from_key, weight)

    def get_vertices(self):
        return self.vertices.get_keys()

    def contains(self, key):
        return self.vertices.get_value(key) is not None

    def bfs(self, start):
        if not self.contains(start):
            return []

        visited = set()
        queue = LinkedQueue()
        order = []

        queue.enqueue(start)
        visited.add(start)

        while not queue.is_empty():
            current = queue.dequeue()
            order.append(current)
            for neighbor in self.get_vertex(current).get_connections():
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        return order

    def dfs(self, start):
        if not self.contains(start):
            return []

        visited = set()
        stack = [start]
        order = []

        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                order.append(current)
                stack.extend(self.get_vertex(current).get_connections())
        return order
