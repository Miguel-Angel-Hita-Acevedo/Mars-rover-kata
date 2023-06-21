from mars_rovers import MarsRover

class MainTerminal():
    def __init__(self, obstacles = None):
        self.obstacles = obstacles
        self.map = [[False for x in range(10)] for y in range(10)] 
        if obstacles:
            self._add_obstacles()

    def _add_obstacles(self):
        for obstacle in self.obstacles:
            self.map[obstacle[0]][obstacle[1]] = True

    def execute(self, input):
        mars_rover = MarsRover()
        for command in input:
            last_x = mars_rover.x
            last_y = mars_rover.y
            mars_rover = self._execute_command(command, mars_rover)
            if self._check_obstacles(mars_rover):
                mars_rover.x = last_x
                mars_rover.y = last_y
                return  "O:" + self._build_result(mars_rover)
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
        mars_rover.x = self._turn_around_for_cardinal_(mars_rover.x)
        mars_rover.y = self._turn_around_for_cardinal_(mars_rover.y)

    def _turn_around_for_cardinal_(self, var):
        if var <= -1:
            var = 9
        if var >= 10:
            var = 0
        return var
    
    def _check_obstacles(self, mars_rover):
        return self.map[mars_rover.x][mars_rover.y]