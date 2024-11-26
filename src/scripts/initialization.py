from road import Road
from vehicle import Vehicle
from four_way import FourWay
from traffic_light import TrafficLight
import random

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
    index=1
    direction = 1
    while i <= row_count:
        road = Road(i, None, index, direction)
        road.set_start_location(row_count, column_count)
        road.set_end_location(row_count, column_count)
        roads.append(road)
        print(f"road {i} generated direction {direction}, row_index={road.row_index}, column_index={road.column_index} start_x={road.start_x}, start_y={road.start_y} end_x={road.end_x} end_y={road.end_y}")
        direction = get_new_direction(direction)
        i += 1
        index += 1
    
    direction = 2
    index=1
    while i <= row_count + column_count:
        road = Road(i, index, None, direction)
        road.set_start_location(row_count, column_count)
        road.set_end_location(row_count, column_count)
        
        roads.append(road)
        print(f"road {i} generated direction {direction}, row_index={road.row_index}, column_index={road.column_index} start_x={road.start_x}, start_y={road.start_y} end_x={road.end_x} end_y={road.end_y}")
        direction = get_new_direction(direction)
        i += 1
        index += 1
        
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

def get_start_position(road, row_count, column_count):
        if road.direction == 1:
            return (row_count, road.column_index)
        elif road.direction == 3:
            return (1, road.column_index)
        elif road.direction == 2:
            return (road.row_index, 1)
        elif road.direction == 4:
            return (road.row_index - 1, column_count)

def initialize_vehicles(iteration_number, roads , iteration_vehicle_generation, max_vehicle_count, vehicle_id_counter, row_count, column_count):
    vehicles = []
    iteration_vehicle_generation_counter = 1
    while vehicle_id_counter <= max_vehicle_count and iteration_vehicle_generation_counter <= iteration_vehicle_generation:
        
        start_road = random.choice(roads)
        end_road = random.choice(roads)
        
        # x, y = start_road.start_x , start_y
        # id, current_road, x, y, travel_start_time, start_road, end_road)
        vehicle = Vehicle(vehicle_id_counter, start_road, startx, y, iteration_number, start_road, end_road)
        vehicles.append(vehicle)
        vehicle_id_counter += 1
        iteration_vehicle_generation_counter += 1
        print (f"road:{start_road.id}, direction:{start_road.direction}")
        print(f"Vehicle {vehicle.id} x:{x}, y:{y} start_road:{vehicle.start_road.id}, end_road:{vehicle.end_road.id}, time={vehicle.travel_start_time} ")
    return vehicles, vehicle_id_counter

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
        