class TrafficLight:
    def __init__(self, id, four_way, road):
        self.id = id
        self.four_way = four_way
        self.road = road
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
        
        