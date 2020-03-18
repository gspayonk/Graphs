# class Queue():
#     def __init__(self):
#         self.queue = []
#     def enqueue(self, value):
#         self.queue.append(value)
#     def dequeue(self):
#         if self.size() > 0:
#             return self.queue.pop(0)
#         else:
#             return None
#     def size(self):
#         return len(self.queue)

# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)



# class Graph:

#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         self.vertices = {}

#     def add_vertex(self, vertex_id):
#         """
#         Add a vertex to the graph.
#         """
#         # TODO
#         self. vertices[vertex_id] = set()

#     def add_edge(self, v1, v2):
#         """
#         Add a directed edge to the graph.
#         """
#         # TODO
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#         else:
#             raise ValueError("vertex does not exist")

#     def add_undirected_edge(self, v1, v2):
#         """
#         Add an undirected edge to the graph.
#         """
#         if v1 in self.vertices and v2 in self.vertices:
#             self.vertices[v1].add(v2)
#             self.vertices[v2].add(v1)
#         else:
#             raise ValueError("vertex does not exist")

#     def get_neighbors(self, vertex_id):
#         """
#         Get all neighbors (edges) of a vertex.
#         """
#         # TODO
#         if vertex_id in self.vertices:
#             return self.vertices[vertex_id]
#         else:
#             raise ValueError("vertex does not exist")
    
#     def bfs(self, starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         # TODO
#         # Create a queue
#         queue = Queue()
#         queue.enqueue(starting_vertex)
#         # Enqueue A PATH TO the starting vertex
#         queue.enqueue(starting_vertex)
#         # Create a set to store visited vertices
#         paths = dict()
#         paths[starting_vertex] = [starting_vertex]
#         # While the queue is not empty...
#         while queue.size() > 0:
#             # Dequeue the first PATH
#             current_vertex = queue.dequeue()
#             # GRAB THE VERTEX FROM THE END OF THE PATH
#             # Check if it's been visited
#             # If it hasn't been visited...
#                 # Mark it as visited
#                 # CHECK IF IT'S THE TARGET
#                     # IF SO, RETURN THE PATH
#             if destination_vertex in self.get_neighbors(current_vertex):
#                 return paths[current_vertex] + [destination_vertex]
#                 # Enqueue A PATH TO all it's neighbors
#                     # MAKE A COPY OF THE PATH
#                     # ENQUEUE THE COPY
#             for vertex in self.get_neighbors(current_vertex):
#                 if vertex not in paths:
#                     paths[vertex] = paths[current_vertex] + [vertex]
#                     queue.enqueue(vertex)


def earliest_ancestor(ancestors, starting_node):
    # graph = Graph()

    # for vertex in ancestors:
    #     graph.add_vertex(vertex[0])
    #     graph.add_vertex(vertex[1])
    #     graph.add_edge(vertex[1], vertex[0])

    # if not graph.get_neighbors(starting_node):
    #     queue = Queue()
    #     queue.enqueue(starting_node)
    #     path = dict()
    #     path[starting_node] = [starting_node]
    #     while queue.size() > 0:
    #         current_node = queue.dequeue()
    #         for node in graph.get_neighbors(current_node):
    #             path[node] = path[current_node] + node
    #             queue.enqueue(node)

    #     oldest = -1
    #     distance = 0
    #     for p in path:
    #         if len(path[p]) > distance or len(path[p]) == distance and path < oldest:
    #             oldest = path
    #             distance = len(path[p])
    #     return oldest

    #     test_things = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9), (11,8), (10,1)]
    #     earliest_ancestor(test_things, 1)
    
    a_list = []
    path = []
    path.append([starting_node])

    while len(path):
        ancestor = path.pop()
        
        wo_ancestor = True
        for p_child in ancestors:
            if p_child[1] == ancestor[-1]:
                path.append([*ancestor, p_child[0]])
                wo_ancestor = False

        if wo_ancestor:
            a_list.append(ancestor)

    distance = 1
    for ancestor in a_list:
        length = len(ancestor)
        if length > distance:
            distance = length

    if distance == 1:
        return -1
    
    a_list = filter(lambda arr: len(arr) == distance, a_list)

    return min(a_list, key=lambda arr: arr[-1])[-1]