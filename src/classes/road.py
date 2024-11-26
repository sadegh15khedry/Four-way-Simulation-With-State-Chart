class Road:
    def __init__(self, id, row_index, column_index, direction):
        self.id = id
        self.four_ways = []
        # 1 for up
        # 2 for right
        # 3 for down
        # 4 for left
        self.direction = direction
        
        self.row_index = row_index
        self.column_index = column_index
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        # self.end_x, self.end_y = self.set_end_location(row_count, column_count)

    
    def set_start_location (self, row_count, column_count):
        # print(f"direction {self.direction} column_index={self.column_index} row_index = {self.row_index} row_count {row_count} column_count {column_count}")
        # print(self.row_index, self.column_index)
        if self.direction == 1:
            self.start_x = row_count+1
            self.start_y = self.column_index
        elif self.direction == 3:
            self.start_x = 0
            self.start_y = self.column_index
            
            
        elif self.direction == 2:
            self.start_x = self.row_index
            self.start_y = 0
        elif self.direction == 4:
            self.start_x = self.row_index
            self.start_y = column_count +1
        
    def set_end_location (self, row_count, column_count):
        # print(self.row_index, self.column_index)
        if self.direction == 1:
            self.end_x = 0
            self.end_y = self.column_index
        elif self.direction == 3:
            self.end_x = row_count+1
            self.end_y = self.column_index
            
            
        elif self.direction == 2:
            self.end_x = self.row_index
            self.end_y = column_count +1
        
        elif self.direction == 4:
            self.end_x = self.row_index
            self.end_y = 0
    
    