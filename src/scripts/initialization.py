from road import Road
from vehicle import Vehicle
from four_way import FourWay

def get_new_direction(direction):
    if direction == 1:
        return 3
    elif direction == 3:
        return 1
    elif direction == 2:
        return 4
    elif direction == 4:
        return 2

def initialize_roads(row_count, column_count):
    roads = []
    i=1
    k=1
    direction = 1
    while i <= row_count:
        road = Road(i, k, None, direction)
        roads.append(road)
        print(f"road {i} generated direction {direction}, row_index={road.row_index}, column_index={road.column_index}")
        direction = get_new_direction(direction)
        i += 1
        k += 1
    
    direction = 2
    k=1
    while i <= row_count + column_count:
        road = Road(i, None, k, direction)
        roads.append(road)
        print(f"road {i} generated direction {direction}, row_index={road.row_index}, column_index={road.column_index}")
        direction = get_new_direction(direction)
        i += 1
        k += 1
        
    return roads

def initialize_vertical_and_horizontal_roads(roads):
    print("initialize_vertical and horizontal _roads")
    horizontal_roads = []
    vertical_roads = []
    for road in roads:
        if road.row_index is not None:
            horizontal_roads.append(road)
            print(f'road{road.id}, added to horizontal roads')
            
        else:
            vertical_roads.append(road)
            print(f'road{road.id}, added to vertical roads')
            
    return horizontal_roads, vertical_roads
def initialize_vehicles(roads):
    pass

def initialize_four_ways(horizontal_roads, vertical_roads):
    four_ways = []
    count = 1
    for h_road in horizontal_roads:
        for v_road in vertical_roads:
            four_way = FourWay(count, h_road.row_index, v_road.column_index, h_road, v_road)
            count += 1
            four_ways.append(four_way)
            print(f"four way {four_way.id} created between road {h_road.id} and road {v_road.id}")
            v_road.four_ways.append(four_way)
            h_road.four_ways.append(four_way)
    
    return four_ways
            # four_way = FourWay(roads.)

            # print(f"vehicle {i * n + j} added to four way {four_way.id}")