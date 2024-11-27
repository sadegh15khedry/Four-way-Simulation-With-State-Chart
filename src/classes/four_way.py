import random

class FourWay:
    def __init__(self, id, x, y, horizontal_road, vertical_road):
        self.id = id
        self.x = x
        self.y = y
        self.horizontal_road = horizontal_road
        self.vertical_road = vertical_road
        self.horizontal_traffic_light = None
        self.vertical_traffic_light = None
        self.static_timer_value = None
        self.yellow_duration = 3
        

    def initialize_traffic_lights_colors(self, method, static_timer_value, yellow_light_duration):
        if method ==  'default':
            random_number = random.randint(0,1)
            self.static_timer_value = static_timer_value

            if random_number == 0:
                self.horizontal_traffic_light.state = 1
                self.horizontal_traffic_light.time_remaining = self.static_timer_value
                
                self.vertical_traffic_light.state = 3
                self.vertical_traffic_light.time_remaining = self.static_timer_value + yellow_light_duration
                
            else:
                self.vertical_traffic_light.state = 1
                self.vertical_traffic_light.time_remaining = self.static_timer_value
                
                self.horizontal_traffic_light.state = 3
                self.horizontal_traffic_light.time_remaining = self.static_timer_value + yellow_light_duration
            self.print_four_way_status()
                
    def print_four_way_status(self):
        if(self.vertical_traffic_light == 1):
            v = 'green'
        print (f'four_way: {self.id}, vertical_status:{self.vertical_traffic_light.get_status_color()} v_time_remaining:{self.vertical_traffic_light.time_remaining}, horizontal_status:{self.horizontal_traffic_light.get_status_color()} h_time_remaining:{self.horizontal_traffic_light.time_remaining}')