NORTH = "North"
EAST = "East"
SOUTH = "South"
WEST = "West"

class Robot:

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)


    def advance(self):
        if self.bearing == NORTH:
            y = self.coordinates[1] + 1
            self.coordinates = (self.coordinates[0], y)
        elif self.bearing == EAST:
            x = self.coordinates[0] + 1
            self.coordinates = (x, self.coordinates[1])
        elif self.bearing == SOUTH:
            y = self.coordinates[1] - 1
            self.coordinates = (self.coordinates[0], y)
        elif self.bearing == WEST:
            x = self.coordinates[0] - 1
            self.coordinates = (x, self.coordinates[1])


    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def simulate(self):
        pass