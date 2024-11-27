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

        self.travel_start_time = travel_start_time
        self.travel_end_time = None
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
            print(f'event_counter {self.event_counter}')
            self.set_event(current_time, (step['x'], step['y']), 'moving', reaching_time)
            self.event_counter += .5
            print(f"Vehicle {self.id} is on the way  to ({self.current_x}, {self.current_y})")
            print(self.event)
        
        elif len(self.event) < self.event_counter:
            return 
        
        # reaching a four way
        elif (self.event['type'] == 'moving' and self.event['reaching_time'] == current_time):
            self.current_x = self.event['destination'][0]
            self.current_y = self.event['destination'][1]
            self.event_counter += 0.5
            print(f'event_counter {self.event_counter}')
            self.set_event(current_time, (self.current_x, self.current_y), 'four_way_waiting', current_time + 5) #TODO: Update this
            
            print(f"Vehicle {self.id} reached ({self.current_x}, {self.current_y})")
            print(self.event)
            
        # moving to the next four way    
        elif (self.event['type'] == 'four_way_waiting' and self.event['reaching_time'] == current_time):
            step = self.path[int(self.event_counter)]
            reaching_time = current_time + step['weight']
            print(f'event_counter {self.event_counter}')
            self.set_event(current_time, (step['x'], step['y']), 'moving', reaching_time)
            self.event_counter += .5
            print(f"Vehicle {self.id} is on the way  to ({self.current_x}, {self.current_y})")
            print(self.event)
        
        
            
        
        
    
        
        