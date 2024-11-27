import heapq
import math
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from node import Node
class Graph:
    def __init__(self, min_weight, max_weight):
        self.nodes = []
        self.min_weight = min_weight
        self.max_weight = max_weight



    def draw(self):
        fig, ax = plt.subplots()
        
        # Draw edges with directions
        for node in self.nodes:
            for neighbor, weight in node.neighbors:
                # Draw an arrow from node to neighbor (flipping x and y)
                arrow = FancyArrowPatch((node.y, node.x), (neighbor.y, neighbor.x),
                                        arrowstyle='->', color='gray', lw=1.5,
                                        mutation_scale=15)
                ax.add_patch(arrow)
                
                # Calculate midpoint for the weight label (flipping x and y)
                mid_x = (node.y + neighbor.y) / 2
                mid_y = (node.x + neighbor.x) / 2
                # Offset the weight slightly above the edge midpoint
                ax.text(mid_x, mid_y + 0.1, f'{weight}', fontsize=8, color='red', ha='center', va='center')
        
        # Draw nodes
        for node in self.nodes:
            # Draw the node as a circle (flipping x and y)
            circle = plt.Circle((node.y, node.x), 0.2, color='lightblue', ec='black', zorder=3)
            ax.add_patch(circle)
            
            # Add the node's ID inside the node (top line)
            ax.text(node.y, node.x + 0.05, f'{node.id}', fontsize=9, ha='center', va='center', color='black', zorder=4)
            
            # Add the (x, y) coordinates inside the node (below the ID, flipped to match matrix-like visualization)
            ax.text(node.y, node.x - 0.1, f'({node.x}, {node.y})', fontsize=8, ha='center', va='center', color='green', zorder=4)
        
        # Remove axes
        ax.axis('off')
        plt.axis('equal')  # Keep the aspect ratio of x and y the same
        plt.show()


    def find_neighbors(self, row_index, column_index, road_direction):
        print(f"row{row_index} column:{column_index}, direction{road_direction}")
        for first_node in self.nodes:
            if first_node.y == column_index and (road_direction == 1 or road_direction == 3):
                for second_node in self.nodes:
                    if road_direction == 1 and first_node.y == second_node.y and first_node.x == second_node.x - 1 and first_node != second_node:
                        # print("here is another")
                        weight = random.randint(self.min_weight, self.max_weight)
                        first_node.neighbors.append((second_node, weight))
                    elif road_direction == 3 and first_node.y == second_node.y and first_node.x == second_node.x + 1 and first_node != second_node:
                        # print("here is another")
                        weight = random.randint(self.min_weight, self.max_weight)
                        first_node.neighbors.append((second_node, weight))
            elif first_node.x == row_index and (road_direction == 2 or road_direction == 4):
                for second_node in self.nodes:     
                    if road_direction == 2 and first_node.x == second_node.x and first_node.y == second_node.y - 1 and first_node != second_node:
                        weight = random.randint(self.min_weight, self.max_weight)
                        first_node.neighbors.append((second_node, weight))
                        
                    elif road_direction == 4 and first_node.x == second_node.x and first_node.y == second_node.y + 1 and first_node != second_node:
                        weight = random.randint(self.min_weight, self.max_weight)
                        first_node.neighbors.append((second_node, weight))