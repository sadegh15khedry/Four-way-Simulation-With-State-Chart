class TrafficLight:
    def __init__(self, four_way, road):
        self.four_way = four_way
        self.road = road
        
        # 0 is blinking
        # 1 is green
        # 2 is yellow
        self.state = 0 