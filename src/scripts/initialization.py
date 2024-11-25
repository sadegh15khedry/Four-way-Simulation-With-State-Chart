from road import Road
from vehicle import Vehicle
from four_way import FourWay
from traffic_light import TrafficLight

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


def initialize_traffic_lights(four_ways):
    counter = 1
    for four_way in four_ways:
        traffic_light_1 = TrafficLight(counter, four_way, four_way.road1)
        counter += 1
        traffic_light_2 = TrafficLight(counter, four_way, four_way.road2)
        counter += 1
        
        four_way.traffic_light_1 = traffic_light_1
        four_way.traffic_light_2 = traffic_light_2
        print(f"initialized traffic_light {traffic_light_1.id} four_way: {traffic_light_1.four_way.id}, road {traffic_light_1.road.id}")
        print(f"initialized traffic_light {traffic_light_2.id} four_way: {traffic_light_2.four_way.id}, road {traffic_light_2.road.id}")
        