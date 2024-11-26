class Vehicle:
    def __init__(self, id, current_road, current_position_in_road, travel_start_time, start_road, end_road):
        self.id = id
        self.current_road = current_road
        self.current_position_in_road = current_position_in_road
        self.travel_start_time = travel_start_time
        self.travel_end_time = None
        self.start_road = start_road
        self.end_road = end_road
        self.travel_end = None
        
        