class TrafficLight:
    def __init__(self, id, four_way, road):
        self.id = id
        self.four_way = four_way
        self.road = road
        
        # 0 is blinking
        # 1 is green
        # 2 is yellow
        # 3 is red
        self.state = 0 