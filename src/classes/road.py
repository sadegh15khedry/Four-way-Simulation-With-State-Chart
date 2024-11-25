class Road:
    def __init__(self, id, row_index, column_index, direction):
        self.id = id
        self.four_ways = []
        self.row_index = row_index
        self.column_index = column_index
        # 1 for up
        # 2 for right
        # 3 for down
        # 4 for left
        self.direction = direction
    