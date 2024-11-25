from road import Road

def get_new_direction(direction):
    if direction == 1:
        return 3
    elif direction == 3:
        return 1
    elif direction == 2:
        return 4
    elif direction == 4:
        return 2

def initialize_roads(m, n):
    roads = []
    i=0
    direction = 1
    while i < m:
        road = Road(i, direction)
        roads.append(road)
        print(f"vehicle {i} generated direction {direction}")
        direction = get_new_direction(direction)
        i += 1
    
    direction = 2    
    while i < m + n:
        road = Road(i, direction)
        roads.append(road)
        print(f"vehicle {i} generated direction {direction}")
        direction = get_new_direction(direction)
        i += 1
    return roads