from vehicle import Vehicle
import random


def generate_vehicles(iteration_number, roads , iteration_vehicle_generation, max_vehicle_count, vehicle_id_counter):
    vehicles = []
    iteration_vehicle_generation_counter = 1
    while vehicle_id_counter <= max_vehicle_count and iteration_vehicle_generation_counter <= iteration_vehicle_generation:
        
        start_road = random.choice(roads)
        end_road = random.choice(roads)
        
        
        vehicle = Vehicle(vehicle_id_counter, start_road, 0, iteration_number, start_road, end_road)
        vehicles.append(vehicle)
        vehicle_id_counter += 1
        iteration_vehicle_generation_counter += 1
        
        print(f"Vehicle {vehicle.id} start_road:{vehicle.start_road.id}, end_road:{vehicle.end_road.id}, time={vehicle.travel_start_time}")
    return vehicles, vehicle_id_counter