class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.neighbors = []  # List of tuples (neighbor, weight)
    
    def add_neighbor(self, neighbor, weight):
        self.neighbors.append((neighbor, weight))
