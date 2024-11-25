from vehicle import Vehicle
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

def initialize(M, N):
    i=0
    direction = 1
    while i < M:
        Road(i, direction)
        print(f"vehicle {i} generated direction {direction}")
        direction = get_new_direction(direction)
        i += 1
    
    direction = 2    
    while i < M + N:
        Road(i, direction)
        print(f"vehicle {i} generated direction {direction}")
        direction = get_new_direction(direction)
        i += 1

        
def simulate(m, n, max_time_steps):
    initialize(m,n)
    for i in range(max_time_steps):
        pass