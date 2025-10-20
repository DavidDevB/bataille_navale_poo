

class Ship:
    ships = []

    def __init__(self, name):
        self.name = name
        self.coordinates = {}
        Ship.ships.append(self)

    def set_coordinates(self, x, y, length, pos):
        if pos == "horizontal":
            for i in range(length):
                self.coordinates[(x, i + y)] = True
        if pos == "vertical":
            for i in range(length):
                self.coordinates[(i + x, y)] = True



