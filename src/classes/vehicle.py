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
        
        self.travel_start_time = travel_start_time
        self.travel_end_time = None
        self.start_road = start_road
        self.end_road = end_road
        self.travel_end = None
        self.path = []
        self.events = []
        
        
    def add_event(self, time, destination, event_type):
        event = {'type': event_type, 'destination':destination, 'time':time }
        self.events.append(event)
        
    
        
        