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
            mars_rover.move()
            self._turn_around(mars_rover)
        else:
            mars_rover.rotate(command)
        return mars_rover
    
    def _turn_around(self, mars_rover):
        mars_rover.x = self.turn_around_for_cardinal_(mars_rover.x)
        mars_rover.y = self.turn_around_for_cardinal_(mars_rover.y)

    def turn_around_for_cardinal_(self, var):
        if var <= -1:
            var = 9
        if var >= 10:
            var = 0
        return var
