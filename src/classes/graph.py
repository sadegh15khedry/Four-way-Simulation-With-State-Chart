import heapq
import math
import matplotlib.pyplot as plt
import random

from node import Node
class Graph:
    def __init__(self, min_weight, max_weight):
        self.nodes = []
        self.min_weight = min_weight
        self.max_weight = max_weight

    def draw(self):
        fig, ax = plt.subplots()
        
        # Draw edges first (so they appear behind nodes)
        for node in self.nodes:
            for neighbor, weight in node.neighbors:
                # Draw an arrow from node to neighbor
                ax.annotate("",
                            xy=(neighbor.x, neighbor.y),
                            xytext=(node.x, node.y),
                            arrowprops=dict(arrowstyle="->", color='gray', lw=1.5),
                            )
                # Calculate midpoint for the weight label
                mid_x = (node.x + neighbor.x) / 2
                mid_y = (node.y + neighbor.y) / 2
                # Offset the weight slightly above the edge midpoint
                ax.text(mid_x, mid_y + 0.1, f'{weight}', fontsize=8, color='red', ha='center', va='center')
        
        # Draw nodes
        for node in self.nodes:
            # Draw the node as a circle
            circle = plt.Circle((node.x, node.y), 0.2, color='lightblue', ec='black', zorder=3)
            ax.add_patch(circle)
            
            # Add the node's ID inside the node (top line)
            ax.text(node.x, node.y + 0.05, f'{node.id}', fontsize=9, ha='center', va='center', color='black', zorder=4)
            
            # Add the (x, y) coordinates inside the node (below the ID)
            ax.text(node.x, node.y - 0.1, f'({node.x}, {node.y})', fontsize=8, ha='center', va='center', color='green', zorder=4)
        
        # Remove axes
        ax.axis('off')
        plt.axis('equal')  # Keep the aspect ratio of x and y the same
        plt.show()







    def find_neighbors(self, row_index, column_index, road_direction):
        for first_node in self.nodes:
            for second_node in self.nodes:
                if road_direction == 1 and first_node.y == second_node.y and first_node.x == second_node.x -1:
                    weight = random.randint(self.min_weight, self.max_weight)
                    first_node.neighbors.append((second_node, weight))