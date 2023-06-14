from mars_rovers import MarsRover

class MainTerminal():
    def __init__(self):
        pass

    def execute(self, input):
        mars_rover = MarsRover()
        
        for command in input:
            mars_rover = self._execute_command(command, mars_rover)
        return self._build_result(mars_rover)

    def _build_result(self, mars_rover):
        return str(mars_rover.x) + ":" + str(mars_rover.y) + ":" + mars_rover.direction

    def _execute_command(self, command, mars_rover):
        if command == "M":
            if mars_rover.direction == "N":
                mars_rover.y += 1
            if mars_rover.direction == "E":
                mars_rover.x += 1
        if command == "R" and mars_rover.direction == "N":
            mars_rover.direction = "E"
        return mars_rover
