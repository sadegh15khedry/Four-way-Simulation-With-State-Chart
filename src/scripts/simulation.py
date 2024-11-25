from vehicle import Vehicle
from road import Road
from initialization import initialize_roads
class Simulation:
    def __init__(self, m, n, max_time_steps):
        self.m = m
        self.n = n
        self.max_time_steps = max_time_steps
        self.roads = []
        self.four_ways = []
        self.traffic_lights = []
        
        
        
    def run(self):
        initialize_roads(self.m, self.n)
        
        for i in range(self.max_time_steps):
            pass