class Robot:
    NORTH = "North"
    EAST = "East"
    SOUTH = "South"
    WEST = "West"


    def __init__(self, bearing = NORTH, coordinates = (0, 0)):
        self.bearing = bearing
        self.coordinates = coordinates

    def advance(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def simulate(self):
        pass