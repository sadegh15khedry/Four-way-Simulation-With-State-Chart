def get_upcoming_four_way(vehicle):
    position = vehicle.current_position_in_road
    if  position == 0:
        four_way = vehicle.current_road.get_next_four_way(position)
    
    return four_way

def vehicles_event_handler(vehicles, roads, four_ways, time):
    for vehicle in vehicles:
        if vehicle.current_position_in_road % 1 == 0:
            four_way = get_upcoming_four_way(vehicle, four_ways, time)
            
            
        