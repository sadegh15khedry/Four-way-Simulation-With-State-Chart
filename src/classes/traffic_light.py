class TrafficLight:
    def __init__(self, id, four_way, road):
        self.id = id
        self.four_way = four_way
        self.road = road
        self.yellow_timer = 0
        self.default_timer = 0
        self.time_remaining = None
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
    
    def update_colored_timer(self):
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