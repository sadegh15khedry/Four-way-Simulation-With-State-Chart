from initialization import initialize_roads, initialize_four_ways, initialize_vehicles, initialize_vertical_and_horizontal_roads, initialize_traffic_lights
from movement_management import vehicles_event_handler
class Simulation:
    def __init__(self, row_count, column_count, max_time_steps, max_vehicle_count, iteration_vehicle_generation):
        self.row_count = row_count
        self.column_count = column_count
        self.max_time_steps = max_time_steps
        self.max_vehicle_count = max_vehicle_count
        self.iteration_vehicle_generation = iteration_vehicle_generation
        self.vehicle_id_counter = 1
        self.iteration_number = 0
        self.vehicles = []
        self.roads = []
        self.four_ways = []
        self.traffic_lights = []
        self.vertical_roads = []
        self.horizontal_roads = []
        
        
        
    def run(self):
        self.roads = initialize_roads(self.row_count, self.column_count)
        self.horizontal_roads, self.vertical_roads = initialize_vertical_and_horizontal_roads(self.roads)
        self.four_ways = initialize_four_ways(self.horizontal_roads, self.vertical_roads)
        initialize_traffic_lights(self.four_ways)
        
        print (f"Simulation Started!!-----------------------------------------------------------------------")
        for self.iteration_number in range(self.max_time_steps):
            print (f"iteration: {self.iteration_number} started-------------------------------------------------")
            
            new_vehicles, new_vehicle_id_counter = initialize_vehicles(self.iteration_number, self.roads, self.iteration_vehicle_generation, self.max_vehicle_count, self.vehicle_id_counter, self.row_count, self.column_count)
            self.vehicle_id_counter = new_vehicle_id_counter
            for vehicle in new_vehicles:
                self.vehicles.append(vehicle)
            
            # vehicles_event_handler(self.vehicles, self.roads, self.four_ways, self.iteration_number)
            print (f"iteration: {self.iteration_number} ended-------------------------------------------------------")
            