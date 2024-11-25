from initialization import initialize_roads, initialize_four_ways, initialize_vertical_and_horizontal_roads
class Simulation:
    def __init__(self, row_count, column_count, max_time_steps):
        self.row_count = row_count
        self.column_count = column_count
        self.max_time_steps = max_time_steps
        self.roads = []
        self.four_ways = []
        self.traffic_lights = []
        self.vertical_roads = []
        self.horizontal_roads = []
        
        
        
    def run(self):
        self.roads = initialize_roads(self.row_count, self.column_count)
        self.horizontal_roads, self.vertical_roads = initialize_vertical_and_horizontal_roads(self.roads)
        self.four_ways = initialize_four_ways(self.horizontal_roads, self.vertical_roads)
        # for i in range(self.max_time_steps):
        #     pass