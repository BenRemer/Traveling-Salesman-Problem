
import numpy as np


class Town:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, town):
        dist_x = abs(self.x - town.x)
        dsit_y = abs(self.y - town.y)
        distance = np.sqrt((dist_x ** 2) + (dsit_y ** 2))
        return distance

class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0

    def route_distance(self):
        if self.distance == 0:
            path_distance = 0
            for i in range(len(self.route)):
                from_city = self.route[i]
                to_city = None
                if i + 1 < len(self.route):
                    to_city = self.route[i + 1]
                else:
                    to_city = self.route[0]
                path_distance += from_city.distance(to_city)
            self.distance = path_distance
        return self.distance

    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness
