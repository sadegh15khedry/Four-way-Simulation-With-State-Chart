class Vehicle:
    def __init__(self, id, travel_start_time, start_road, end_road):
        self.id = id
        self.current_road = start_road
        
        self.current_x = start_road.start_x
        self.current_y = start_road.start_y
        self.start_x = start_road.start_x
        self.start_y = start_road.start_y
        self.end_x = end_road.end_x
        self.end_y = end_road.end_y
        
        self.event_counter = 1
        self.event = None
        self.has_reached_destination = False
        
        self.travel_start_time = travel_start_time
        self.travel_end_time = None
        self.travel_duration = None
        
        self.start_road = start_road
        self.end_road = end_road
        self.travel_end = None
        self.path = []
        
        
    def set_event(self, current_time, destination, event_type, reaching_time):
        event = {'type': event_type, 'setting time':current_time, 'destination':destination, "reaching_time": reaching_time }
        self.event = event
        
    def check_event(self, current_time):
        
        if self.event_counter == 1:
            step = self.path[int(self.event_counter)]
            reaching_time = current_time + step['weight']
            self.set_event(current_time, (step['x'], step['y']), 'moving', reaching_time)
            self.event_counter += .5
            print(f"Vehicle {self.id} is on the way  to {step['x']}, {step['y']})")
            print(self.event)
        
        elif len(self.path) < self.event_counter:
            return 
        
        # reaching a node
        elif (self.event['type'] == 'moving' and self.event['reaching_time'] == current_time):
            self.current_x = self.event['destination'][0]
            self.current_y = self.event['destination'][1]
            self.event_counter += 0.5
            
            # checking if we reached the end
            if self.event_counter == len(self.path):
                self.has_reached_destination = True
                self.travel_end_time = current_time
                print(f"Vehicle {self.id} has reached the destination location:({self.current_x}, {self.current_y}) start_time:{self.travel_start_time}, end_time:{self.travel_end_time} travel_end_time:{self.travel_end_time} ")
                return
            
            print(f'event_counter {self.event_counter}')
            # four_way_delay_time = self.get_four_way_delay_time()
            self.set_event(current_time, (self.current_x, self.current_y), 'four_way_waiting', current_time + 3) 
            # self.set_event(current_time, (self.current_x, self.current_y), 'four_way_waiting', current_time + four_way_delay_time) #TODO: Update this
            
            
                
            print(f"Vehicle {self.id} reached ({self.current_x}, {self.current_y})")
            print(self.event)
            
        # moving to the next four way    
        elif (self.event['type'] == 'four_way_waiting' and self.event['reaching_time'] == current_time):
            step = self.path[int(self.event_counter)]
            reaching_time = current_time + step['weight']
            print(f'event_counter {self.event_counter}')
            self.set_event(current_time, (step['x'], step['y']), 'moving', reaching_time)
            self.event_counter += .5
            
            print(f"Vehicle {self.id} is on the way to ({self.current_x}, {self.current_y})")
            print(self.event)
    
    def get_four_way_delay_time(self):
        four_way = self.get_four_way_using_location
        traffic_light = None
        
        # if self.current_road == four_way.horizontal_road:
            # traffic_light = self.horizontal_traffic_light
            # pass
        # elif self.current_road == four_way.vertical_road:
            # traffic_light = self.vertical_traffic_light
            # pass
        
           
        
    def get_four_way_using_location(self, four_ways):
        for four_way in four_ways:
            if four_way.x == self.current_x and four_way.y == self.current_y:
                return four_way
    
        
        
    
        
        