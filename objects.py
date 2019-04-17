import numpy as np

# City object
class City:
    # Initializes the object
    def __init__(self, x, y, node_id):
        self.x = x
        self.y = y
        self.node_id = node_id

    # Finds distance between two cities
    def distance(self, city):
        dist_x = abs(self.x - city.x)
        dsit_y = abs(self.y - city.y)
        distance = np.sqrt((dist_x ** 2) + (dsit_y ** 2))
        return distance
    # Sends over the node ID
    def __repr__(self):
        return str(self.node_id)

# Crates a fitness object to see how good the route is
class Fitness:
    # Initializes and sets everything to 0
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.fitness = 0

    # Gets distance for the route
    def route_distance(self):
        if self.distance == 0:
            dist = 0
            for i in range(len(self.route)):
                c_from = self.route[i]
                c_to = None
                if (i + 1) < len(self.route):
                    c_to = self.route[i + 1]
                else:
                    c_to = self.route[0]
                dist += c_from.distance(c_to)
            self.distance = dist
        return self.distance

    # Calculates the fitness of the route, higher is better
    def route_fitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.route_distance())
        return self.fitness
