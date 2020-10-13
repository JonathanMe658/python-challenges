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
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
        elif self.bearing == EAST:
            self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
        elif self.bearing == SOUTH:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
        elif self.bearing == WEST:
            self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])


    def turn_left(self):
        pass

    def turn_right(self):
        pass

    def simulate(self, seq):
        for n in seq:
            if n == "L":
                self.turn_left()
            elif n == "R":
                self.turn_right()
            elif n == "A":
                self.advance()