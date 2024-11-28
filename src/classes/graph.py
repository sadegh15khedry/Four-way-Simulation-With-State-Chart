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

import heapq
import math
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from node import Node
import heapq
import math
import matplotlib.pyplot as plt
import random
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
import plotly.graph_objects as go


class Graph:
    def __init__(self, min_weight, max_weight):
        self.nodes = []
        self.min_weight = min_weight
        self.max_weight = max_weight

    
    def draw(self):
        # Create a Plotly figure
        fig = go.Figure()

        # Prepare data for edges
        edge_x = []
        edge_y = []
        edge_weights = []

        for node in self.nodes:
            for neighbor, weight in node.neighbors:
                # From current node to neighbor
                edge_x += [node.y, neighbor.y, None]  # y-coordinates
                edge_y += [node.x, neighbor.x, None]  # x-coordinates (flipped for "matrix" style)
                edge_weights.append({
                    "x": (node.y + neighbor.y) / 2,
                    "y": (node.x + neighbor.x) / 2,
                    "weight": weight
                })

        # Add edges to the figure
        fig.add_trace(go.Scatter(
            x=edge_x,
            y=edge_y,
            mode='lines',
            line=dict(color='gray', width=1.5),
            hoverinfo='none'
        ))

        # Prepare data for nodes
        node_x = []
        node_y = []
        node_labels = []
        for node in self.nodes:
            node_x.append(node.y)  # y-coordinates
            node_y.append(node.x)  # x-coordinates (flipped for "matrix" style)
            node_labels.append(f"ID: {node.id}<br>({node.x}, {node.y})")

        # Add nodes to the figure
        fig.add_trace(go.Scatter(
            x=node_x,
            y=node_y,
            mode='markers+text',
            marker=dict(size=20, color='lightblue', line=dict(width=2, color='black')),
            text=[node.id for node in self.nodes],
            textposition='middle center',
            hoverinfo='text',
            textfont=dict(size=10)
        ))

        # Add edge weights
        for weight_info in edge_weights:
            fig.add_trace(go.Scatter(
                x=[weight_info['x']],
                y=[weight_info['y']],
                mode='text',
                text=[str(weight_info['weight'])],
                textposition="top center",
                hoverinfo='none',
                textfont=dict(color='red', size=10)
            ))

        # Flip the y-axis to make row index 0 at the top
        fig.update_layout(
            yaxis=dict(
                autorange='reversed',  # Flip the y-axis
                title="Row Index"
            ),
            xaxis=dict(title="Column Index"),
            showlegend=False,
            title="Graph Visualization",
            plot_bgcolor="white"
        )

        # Show the plot
        fig.show()




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

    
    def shortest_path(self, source_x, source_y, destination_x, destination_y):
        source_node = None
        destination_node = None
        for node in self.nodes:
            if node.x == source_x and node.y == source_y:
                source_node = node
            if node.x == destination_x and node.y == destination_y:
                destination_node = node
        
        if source_node is None or destination_node is None:
            print("Source or destination node not found.")
            return []

        distances = {node: float('inf') for node in self.nodes}
        previous_nodes = {node: None for node in self.nodes}
        distances[source_node] = 0

        queue = [(0, source_node.id, source_node)]
        
        while queue:
            current_distance, _, current_node = heapq.heappop(queue)
            
            if current_node == destination_node:
                break

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in current_node.neighbors:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = (current_node, weight)
                    heapq.heappush(queue, (distance, neighbor.id, neighbor))
        
        path = []
        current = destination_node
        while current != source_node:
            if previous_nodes[current] is None:
                print("No path found.")
                return []
            prev_node, weight = previous_nodes[current]
            step = {
                'x': current.x,
                'y': current.y,
                'weight': weight
            }
            path.append(step)
            current = prev_node
        
        path.append({'x': source_node.x, 'y': source_node.y, 'weight': 0})
        path.reverse()  # Reverse the path to start from the source
        return path


    

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