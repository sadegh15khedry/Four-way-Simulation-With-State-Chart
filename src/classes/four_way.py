import random

class FourWay:
    def __init__(self, id, x, y, horizontal_road, vertical_road, default_timer, yellow_timer, blinking_timer):
        self.id = id
        self.x = x
        self.y = y
        self.horizontal_road = horizontal_road
        self.vertical_road = vertical_road
        self.horizontal_traffic_light = None
        self.vertical_traffic_light = None
        self.default_timer = default_timer
        self.yellow_timer = yellow_timer
        self.blinking_timer = blinking_timer
        self.vehicles_history = []


    def initialize_traffic_lights_colors(self, method):
        if method ==  'default':
            self.horizontal_traffic_light.default_timer = self.default_timer
            self.horizontal_traffic_light.yellow_timer = self.yellow_timer
            self.vertical_traffic_light.default_timer = self.default_timer
            self.vertical_traffic_light.yellow_timer = self.yellow_timer
            
            random_number = random.randint(0,1)
            if random_number == 0:
                self.horizontal_traffic_light.state = 1
                self.horizontal_traffic_light.time_remaining = self.default_timer
                
                self.vertical_traffic_light.state = 3
                self.vertical_traffic_light.time_remaining = self.default_timer + self.yellow_timer
                
            elif  random_number == 1:
                self.vertical_traffic_light.state = 1
                self.vertical_traffic_light.time_remaining = self.default_timer
                
                self.horizontal_traffic_light.state = 3
                self.horizontal_traffic_light.time_remaining = self.default_timer + self.yellow_timer
                        
        elif method == 'proposed':
            self.horizontal_traffic_light.state = 0
            self.horizontal_traffic_light.time_remaining = self.blinking_timer
            self.horizontal_traffic_light.blinking_timer = self.blinking_timer
            
            
            self.vertical_traffic_light.state = 0
            self.vertical_traffic_light.time_remaining = self.blinking_timer
            self.vertical_traffic_light.blinking_timer = self.blinking_timer
            
        self.print_four_way_status()
        
    def update_traffic_lights_colors(self, method, time):
        self.vertical_traffic_light.update_colored_timer(method, time)
        self.horizontal_traffic_light.update_colored_timer(method, time)
        
    def add_vehicle_to_four_way(self, vehicle, time):
        if vehicle.current_road == self.vertical_road:
            self.vertical_traffic_light.waiting_vehicles.append(vehicle)
            self.vehicles_history.append({'vehicle_id': vehicle.id, 'time': time, 'road_id': vehicle.current_road.id})
            print(f'vehicle: {vehicle.id} added to four_way{self.id}, traffic_light: {self.vertical_traffic_light.id}')
            
        elif vehicle.current_road == self.horizontal_road:
            self.horizontal_traffic_light.waiting_vehicles.append(vehicle)
            print(f'vehicle: {vehicle.id} added to four_way{self.id}, traffic_light: {self.horizontal_traffic_light.id}')
            
            
    
    def remove_vehicle_from_four_way(self, vehicle):
        for traffic_light in [self.horizontal_traffic_light, self.vertical_traffic_light]:
            if vehicle in traffic_light.waiting_vehicles:
                traffic_light.waiting_vehicles.remove(vehicle)
                print(f'vehicle: {vehicle.id} removed from four_way{self.id}, traffic_light: {traffic_light.id}')
                
                
    
    def get_waiting_time(self, vehicle, time):
        traffic_light = None
        waiting_time = None

        if vehicle.current_road == self.horizontal_road:
            # self.horizontal_road.waiting_vehicles.append(vehicle)
            traffic_light = self.horizontal_traffic_light
        elif vehicle.current_road == self.vertical_road:
            # self.vertical_traffic_light.waiting_vehicles.append(vehicle)
            traffic_light =  self.vertical_traffic_light
        
        if traffic_light.state == 0:
            waiting_time = self.get_blinking_delay()
        elif traffic_light.state == 1:
            waiting_time = 0
        elif traffic_light.state == 2:
            waiting_time = traffic_light.time_remaining + self.default_timer
        elif traffic_light.state == 3:
            waiting_time = traffic_light.time_remaining
        print(f"waiting time is {waiting_time}")
        # print(f"traffic {traffic_light.id}")
        
        return waiting_time
    
    def get_other_road(self, road):
        if road == self.horizontal_road:
            return self.vertical_road
        elif road == self.vertical_road:
            return self.horizontal_road
        
    def get_blinking_delay(self):
        n1 = len(self.horizontal_traffic_light.waiting_vehicles)
        n2 =  len(self.vertical_traffic_light.waiting_vehicles)
        # print(f"h_id: {self.horizontal_traffic_light.id} has {n1}, v_id: {self.horizontal_traffic_light.id} has {n2}")
        number_of_four_way_vehicles = n1 + n2
        
        print(f"number of vehicles:{number_of_four_way_vehicles}")
        return 2 ** number_of_four_way_vehicles
    
    def print_four_way_status(self):
        print (f'four_way: {self.id}, vertical_status:{self.vertical_traffic_light.get_status_color()} v_time_remaining:{self.vertical_traffic_light.time_remaining}, horizontal_status:{self.horizontal_traffic_light.get_status_color()} h_time_remaining:{self.horizontal_traffic_light.time_remaining}')