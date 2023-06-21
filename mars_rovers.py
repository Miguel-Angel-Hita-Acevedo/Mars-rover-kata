

class MarsRover:

    def __init__ (self):
        self.x = 0
        self.y = 0
        self.cardinals = [ 'N', 'E', 'S', 'W']
        self.cardinal_position = 0

    def move(self):
        if self.direction == "N":
            self.y += 1
        if self.direction == "E":
            self.x += 1
        if self.direction == 'W':
            self.x -= 1
        if self.direction == 'S':
            self.y -= 1

    def rotate(self, command):
        if command == 'R':
            self.cardinal_position += 1
        else:
            self.cardinal_position -= 1

    @property
    def direction(self):
        return self.cardinals[self.cardinal_position % len(self.cardinals)]
