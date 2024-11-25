class FourWay:
    def __init__(self, id, row_index, column_index, road1, road2):
        self.id = id
        self.row_index = row_index
        self.column_index = column_index
        self.road1 = road1
        self.road2 = road2
        self.traffic_lights = []