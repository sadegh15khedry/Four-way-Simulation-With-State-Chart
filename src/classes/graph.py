import heapq
import math
from node import Node
class Graph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes by id
    
    def add_node(self, node_id, x, y):
        if node_id not in self.nodes:
            self.nodes[node_id] = Node(node_id, x, y)

    