

class MarsRover:

    def __init__ (self):
        self.x = 0
        self.y = 0
        self.direction = 'N'

    def move(self):
        if self.direction == "N":
            self.y += 1
        if self.direction == "E":
            self.x += 1

    def rotate(self, command):
        if command == 'R' and self.direction == 'N':
            self.direction = "E"