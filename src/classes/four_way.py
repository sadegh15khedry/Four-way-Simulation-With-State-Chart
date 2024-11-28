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
        self.vehicles = []


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
        
    
        
    
    def get_waiting_time(self, vehicle):
        if vehicle.current_road == self.horizontal_road:
            return self.horizontal_traffic_light.get_waiting_time()
        elif vehicle.current_road == self.vertical_road:
            return self.vertical_traffic_light.get_waiting_time()
    
    def get_other_road(self, road):
        if road == self.horizontal_road:
            return self.vertical_road
        elif road == self.vertical_road:
            return self.horizontal_road
        
    
    def print_four_way_status(self):
        if(self.vertical_traffic_light == 1):
            v = 'green'
        print (f'four_way: {self.id}, vertical_status:{self.vertical_traffic_light.get_status_color()} v_time_remaining:{self.vertical_traffic_light.time_remaining}, horizontal_status:{self.horizontal_traffic_light.get_status_color()} h_time_remaining:{self.horizontal_traffic_light.time_remaining}')