import random
import math
class FourWay:
    def __init__(self, id, x, y, horizontal_road, vertical_road, default_timer, yellow_timer, blinking_timer, crowded_thresholds):
        self.id = id
        self.x = x
        self.y = y
        self.horizontal_road = horizontal_road
        self.crowded_thresholds = crowded_thresholds
        self.vertical_road = vertical_road
        self.horizontal_traffic_light = None
        self.vertical_traffic_light = None
        self.default_timer = default_timer
        self.yellow_timer = yellow_timer
        self.blinking_timer = blinking_timer
        self.vehicles_history = []


    def initialize_traffic_lights_colors(self, method):
        if method ==  'default':
            self.horizontal_traffic_light.default_timer = self.default_timer
            self.horizontal_traffic_light.yellow_timer = self.yellow_timer
            self.vertical_traffic_light.default_timer = self.default_timer
            self.vertical_traffic_light.yellow_timer = self.yellow_timer
            
            random_number = random.randint(0,1)
            if random_number == 0:
                self.horizontal_traffic_light.state = 1
                self.horizontal_traffic_light.time_remaining = self.default_timer
                
                self.vertical_traffic_light.state = 3
                self.vertical_traffic_light.time_remaining = self.default_timer + self.yellow_timer
                
            elif  random_number == 1:
                self.vertical_traffic_light.state = 1
                self.vertical_traffic_light.time_remaining = self.default_timer
                
                self.horizontal_traffic_light.state = 3
                self.horizontal_traffic_light.time_remaining = self.default_timer + self.yellow_timer
                        
        elif method == 'proposed':
            self.horizontal_traffic_light.state = 0
            self.horizontal_traffic_light.time_remaining = self.blinking_timer
            self.horizontal_traffic_light.blinking_timer = self.blinking_timer
            
            
            self.vertical_traffic_light.state = 0
            self.vertical_traffic_light.time_remaining = self.blinking_timer
            self.vertical_traffic_light.blinking_timer = self.blinking_timer
            
        self.print_four_way_status()
        
    def update_traffic_lights_colors(self, method, time):
        if method == 'default':
            self.vertical_traffic_light.update_colored_timer(method, time)
            self.horizontal_traffic_light.update_colored_timer(method, time)
        
        elif method == 'proposed':
            is_crowded = self.is_crowded(time)
            v_time = self.vertical_traffic_light.time_remaining
            v_state = self.vertical_traffic_light.state
            
            h_time = self.horizontal_traffic_light.time_remaining
            h_state = self.horizontal_traffic_light.state
            
            print(f"v_state:{v_state}, v_time:{v_time}, h_state:{h_state}, h_time:{h_time}, is_crowded:{is_crowded}")
            
            if  h_time > 1 and v_time > 1: # count down
                print('count down')
                self.horizontal_traffic_light.time_remaining = self.horizontal_traffic_light.time_remaining - 1
                self.vertical_traffic_light.time_remaining = self.vertical_traffic_light.time_remaining - 1
                
            elif v_state == 0 and h_state == 0 and v_time == 1 and h_time == 1 and is_crowded == False: # blinking to blinking
                self.horizontal_traffic_light.time_remaining = self.blinking_timer
                self.vertical_traffic_light.time_remaining = self.blinking_timer

            elif  v_state == 0 and h_state == 0 and v_time == 1 and is_crowded == True: # blinking to colors
                print("blinking to colors")
                self.set_initial_smart_four_way_traffic_lights_color(time)

            # elif self.time_remaining == 0 and (self.state == 1 or self.state == 1 or self.state == 1) and is_crowded == True: # color update
            #     self.four_way.set_smart_four_traffic_lights_color(time)
        
    def add_vehicle_to_four_way(self, vehicle, time):
        if vehicle.current_road == self.vertical_road:
            self.vertical_traffic_light.waiting_vehicles.append(vehicle)
            self.vehicles_history.append({'vehicle_id': vehicle.id, 'time': time, 'road_id': vehicle.current_road.id})
            print(f'vehicle: {vehicle.id} added to four_way{self.id}, traffic_light: {self.vertical_traffic_light.id}')
            
        elif vehicle.current_road == self.horizontal_road:
            self.horizontal_traffic_light.waiting_vehicles.append(vehicle)
            print(f'vehicle: {vehicle.id} added to four_way{self.id}, traffic_light: {self.horizontal_traffic_light.id}')
            
            
    
    def remove_vehicle_from_four_way(self, vehicle):
        for traffic_light in [self.horizontal_traffic_light, self.vertical_traffic_light]:
            if vehicle in traffic_light.waiting_vehicles:
                traffic_light.waiting_vehicles.remove(vehicle)
                print(f'vehicle: {vehicle.id} removed from four_way{self.id}, traffic_light: {traffic_light.id}')
                
                
    
    def get_waiting_time(self, vehicle, time):
        traffic_light = None
        waiting_time = None

        if vehicle.current_road == self.horizontal_road:
            # self.horizontal_road.waiting_vehicles.append(vehicle)
            traffic_light = self.horizontal_traffic_light
        elif vehicle.current_road == self.vertical_road:
            # self.vertical_traffic_light.waiting_vehicles.append(vehicle)
            traffic_light =  self.vertical_traffic_light
        
        if traffic_light.state == 0:
            waiting_time = self.get_blinking_delay()
        elif traffic_light.state == 1:
            waiting_time = 0
        elif traffic_light.state == 2:
            waiting_time = traffic_light.time_remaining + self.default_timer
        elif traffic_light.state == 3:
            waiting_time = traffic_light.time_remaining
        print(f"waiting time is {waiting_time}")
        # print(f"traffic {traffic_light.id}")
        
        return waiting_time
    
    def get_other_road(self, road):
        if road == self.horizontal_road:
            return self.vertical_road
        elif road == self.vertical_road:
            return self.horizontal_road
        
    def get_blinking_delay(self):
        number_of_four_way_vehicles = len(self.horizontal_traffic_light.waiting_vehicles) + len(self.vertical_traffic_light.waiting_vehicles)
        
        print(f"number of vehicles:{number_of_four_way_vehicles}")
        return 2 ** number_of_four_way_vehicles
    
   
    def is_crowded(self, time):
        number_of_four_way_vehicles = self.get_vehicle_count_by_duration(time)
        print(f"four_way:{self.id}, number of vehicles:{number_of_four_way_vehicles}")
        if (number_of_four_way_vehicles < self.crowded_thresholds):
            return False
        else:
            return True

    def set_initial_smart_four_way_traffic_lights_color(self, time):
        print("we are right here #############################################################################")
        horizontal_count, vertical_count = self.get_horizontal_and_vertical_vehicle_count(time)
        if horizontal_count > vertical_count:
            smart_timer = self.get_smart_timer_value(horizontal_count)
            print(f'smart_timer: {smart_timer}')
            self.horizontal_traffic_light.state = 1
            self.horizontal_traffic_light.time_remaining = smart_timer
            self.vertical_traffic_light.state = 3
            self.vertical_traffic_light.time_remaining = smart_timer + self.yellow_timer
            print(f'h_time: {self.horizontal_traffic_light.time_remaining}')
            print(f'v_time: {self.vertical_traffic_light.time_remaining}')
            
            
        elif horizontal_count <= vertical_count:
            smart_timer = self.get_smart_timer_value(horizontal_count)
            print(f'smart_timer: {smart_timer}')
            self.vertical_traffic_light.state = 1
            self.vertical_traffic_light.time_remaining = smart_timer
            self.horizontal_traffic_light.state = 3
            self.horizontal_traffic_light.time_remaining = smart_timer + self.yellow_timer
            print(f'h_time: {self.horizontal_traffic_light.time_remaining}')
            print(f'v_time: {self.vertical_traffic_light.time_remaining}')
            
            
    def get_smart_timer_value(self, vehicle_count):
        if vehicle_count < 10:
            return 1
        value = int(math.log10(vehicle_count))
        print(f"smart_timer_value: {value}")
        return value
           
    def get_vehicle_count_by_duration(self, time):
        count = 0
        for row in self.vehicles_history:
            if row['time'] <= time and row['time'] > time - self.blinking_timer:
                count += 1
        return count
    
    def get_horizontal_and_vertical_vehicle_count(self, time):
        horizontal_count = 0
        vertical_count = 0
        for row in self.vehicles_history:
            if row['time'] <= time and row['time'] > time - self.blinking_timer and row['road_id'] == self.horizontal_road.id:
                horizontal_count += 1
            elif row['time'] <= time and row['time'] > time - self.blinking_timer and row['road_id'] == self.vertical_road.id:
                vertical_count += 1
        return horizontal_count, vertical_count

        return count            
    def print_four_way_status(self):
        print (f'four_way: {self.id}, vertical_status:{self.vertical_traffic_light.get_status_color()} v_time_remaining:{self.vertical_traffic_light.time_remaining}, horizontal_status:{self.horizontal_traffic_light.get_status_color()} h_time_remaining:{self.horizontal_traffic_light.time_remaining}')