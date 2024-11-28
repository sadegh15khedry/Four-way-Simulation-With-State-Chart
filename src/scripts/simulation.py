from initialization import initialize_roads, initialize_four_ways, initialize_graph, initialize_vehicles, initialize_vertical_and_horizontal_roads, initialize_traffic_lights

class Simulation:
    def __init__(self, method, default_timer, row_count, column_count, max_time_steps, max_vehicle_count, iteration_vehicle_generation, min_road_time, max_road_time, yellow_timer, blinking_timer):
        self.method = method
        self.default_timer = default_timer
        self.yellow_timer = yellow_timer
        self.blinking_timer = blinking_timer
        self.row_count = row_count
        self.column_count = column_count
        self.max_time_steps = max_time_steps
        self.max_vehicle_count = max_vehicle_count
        self.min_road_time = min_road_time
        self.max_road_time = max_road_time
        self.iteration_vehicle_generation = iteration_vehicle_generation
        self.vehicle_id_counter = 1
        self.time = 0
        self.vehicles = []
        self.roads = []
        self.four_ways = []
        self.traffic_lights = []
        self.vertical_roads = []
        self.horizontal_roads = []
        self.graph = None
        
        
        
    def run(self):
        self.roads = initialize_roads(self.row_count, self.column_count)
        self.horizontal_roads, self.vertical_roads = initialize_vertical_and_horizontal_roads(self.roads)
        self.four_ways = initialize_four_ways(self.horizontal_roads, self.vertical_roads,  self.default_timer, self.yellow_timer, self.blinking_timer)
        initialize_traffic_lights(self.four_ways,  self.method)
                
        self.graph = initialize_graph(self.roads, self.four_ways, self.vertical_roads, self.horizontal_roads, self.min_road_time, self.max_road_time)
        self.graph.draw()
        
        print (f"Simulation Started!!--------------------------------------------------------------------------")
        for self.time in range(self.max_time_steps):
            print (f"iteration:{self.time} started-------------------------------------------------")
            
            self.generate_iteration_vehicles()
            self.update_traffic_lights()
            self.print_traffic_lights_status()
            self.check_vehicle_events()
            
            print (f"time: {self.time} ended-------------------------------------------------------")
            print("")
        # print (f"Simulation Ended!!--------------------------------------------------------------------------")
        
            
        
            
            
    def generate_iteration_vehicles(self):
        new_vehicles, new_vehicle_id_counter = initialize_vehicles(self.time, self.roads, self.iteration_vehicle_generation, self.max_vehicle_count, self.vehicle_id_counter, self.row_count, self.column_count, self.graph)
        self.vehicle_id_counter = new_vehicle_id_counter
        for vehicle in new_vehicles:
            self.vehicles.append(vehicle)
            
    def update_traffic_lights(self):
        for four_way in self.four_ways:
            four_way.update_traffic_lights_colors(self.method, self.time)
            
    
    def print_traffic_lights_status(self):
        for four_way in self.four_ways:
            four_way.print_four_way_status()
            
    def check_vehicle_events(self):
        if self.method == 'default':
            for vehicle in self.vehicles:
                vehicle.check_default_event(self.time, self.four_ways, self.roads, self.time)
        elif self.method == 'proposed':
            for vehicle in self.vehicles:
                vehicle.update_vehicle_location(self.time, self.four_ways)
            for vehicle in self.vehicles:
                vehicle.check_proposed_event(self.time, self.four_ways, self.roads, self.time)