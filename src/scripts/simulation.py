from initialization import initialize_roads, initialize_four_ways, initialize_graph, initialize_vehicles, initialize_vertical_and_horizontal_roads, initialize_traffic_lights

class Simulation:
    def __init__(self, method, default_timer, row_count, column_count, max_time_steps, max_vehicle_count, iteration_vehicle_generation, min_road_time, max_road_time, yellow_light_duration):
        self.method = method
        self.default_timer = default_timer
        self.yellow_light_duration = yellow_light_duration
        self.row_count = row_count
        self.column_count = column_count
        self.max_time_steps = max_time_steps
        self.max_vehicle_count = max_vehicle_count
        self.min_road_time = min_road_time
        self.max_road_time = max_road_time
        self.iteration_vehicle_generation = iteration_vehicle_generation
        self.vehicle_id_counter = 1
        self.iteration_number = 0
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
        self.four_ways = initialize_four_ways(self.horizontal_roads, self.vertical_roads)
        initialize_traffic_lights(self.four_ways)

        for four_way in self.four_ways:
            four_way.initialize_traffic_lights_colors(self.method, self.default_timer, self.yellow_light_duration)        
                
        self.graph = initialize_graph(self.roads, self.four_ways, self.vertical_roads, self.horizontal_roads, self.min_road_time, self.max_road_time)
        self.graph.draw()
        
        print (f"Simulation Started!!-----------------------------------------------------------------------")
        for self.iteration_number in range(self.max_time_steps):
            print (f"iteration: {self.iteration_number} started-------------------------------------------------")
            
            new_vehicles, new_vehicle_id_counter = initialize_vehicles(self.iteration_number, self.roads, self.iteration_vehicle_generation, self.max_vehicle_count, self.vehicle_id_counter, self.row_count, self.column_count, self.graph)
            self.vehicle_id_counter = new_vehicle_id_counter
            for vehicle in new_vehicles:
                self.vehicles.append(vehicle)
            
            for vehicle in self.vehicles:
                vehicle.check_event(self.iteration_number)
                
                
            # vehicles_event_handler(self.vehicles, self.roads, self.four_ways, self.iteration_number)
            print (f"iteration: {self.iteration_number} ended-------------------------------------------------------")
            