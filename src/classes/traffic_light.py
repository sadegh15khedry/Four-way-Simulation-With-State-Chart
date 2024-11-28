class TrafficLight:
    def __init__(self, id, four_way, road):
        self.id = id
        self.four_way = four_way
        self.road = road
        self.yellow_timer = 0
        self.default_timer = 0
        self.blinking_timer = 0
        self.time_remaining = None
        self.waiting_vehicles = []
        # 0 is blinking
        # 1 is green
        # 2 is yellow
        # 3 is red
        self.state = 0
        
    def get_status_color(self):
        if self.state == 0:
            return 'blinking'
        elif self.state == 1:
            return 'green'
        elif self.state == 2:
            return 'orange'
        elif self.state == 3:
            return 'red'
    
    def update_colored_timer(self, method, time):
        if method == 'default':
            if self.time_remaining > 1:
                self.time_remaining -= 1
            elif self.state == 1:
                self.state = 2
                self.time_remaining = self.yellow_timer
            elif self.state == 2:
                self.state = 3
                self.time_remaining = self.default_timer + self.yellow_timer
            elif self.state == 3:
                self.state = 1
                self.time_remaining = self.default_timer
        elif method == 'proposed':
            if self.state == 0 and self.time_remaining > 1:
                self.time_remaining = self.time_remaining - 1
            elif self.state == 0 and self.time_remaining == 1:
                self.time_remaining = self.blinking_timer
    
            
    def get_waiting_time(self):
        waiting_time = None
        if self.state == 1:
            waiting_time = 0
        elif self.state == 2:
            waiting_time = self.time_remaining + self.default_timer
        elif self.state == 3:
            waiting_time = self.time_remaining
            
        return waiting_time