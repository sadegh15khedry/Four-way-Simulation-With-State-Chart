class Road:
    def __init__(self, id, direction):
        self.id = id
        self.four_ways = []
        # 1 for up
        # 2 for right
        # 3 for down
        # 4 for left
        self.direction = direction
    