class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def earliest_ancestor(ancestors, starting_node):
    
    ancestor_data = {}
    # organizing data into graph
    for parentChild in ancestors:
        parent = parentChild[0]
        child = parentChild[1]

        # if parent has more than one child
        if parent in ancestor_data.keys():
            ancestor_data[parent].append(child)
        else:
            ancestor_data[parent] = [child] 

    # store possible paths in array 
    paths = []

    # longest path (dfs) for earliest ancestor, starts at the root node and explores as far as possible along each branch before backtracking
    s = Stack()
    s.push([starting_node])
    visited = []

    # checking that current vertex is not == to destination vertex
    while s.size() > 0: 
        path = s.pop()
        current = path[-1]
        if current not in visited:
            visited.append(current)
            parents_current = []

            # looking for parents we append
            for parent in ancestor_data:
                if current in ancestor_data[parent]:
                    parents_current.append(parent)

            # if no parents that's the end of the path
            if len(parents_current) == 0:
                # store into paths
                paths.append(path)
            else: 
                # if parents add to stack
                for parent in parents_current:
                    new_path = list(path)
                    new_path.append(parent)
                    s.push(new_path)

    # dfs for all possible paths so now sort to longest one
    paths = sorted(paths)
    longest_path = paths[0]
    earliest = longest_path[-1]
    if earliest == starting_node:
        return -1
    else:
        return earliest

testing = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(testing, 9))