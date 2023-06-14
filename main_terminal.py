
class MainTerminal():
    def __init__(self):
        pass

    def execute_command(self, input):
        x = 0
        y = 0
        rotation = 'N'
        if input == "":
            return "0:0:N"
        # "MRMM" = 1:2:E
        for command in input:
            if command == "M":
                if rotation == "N":
                    y += 1
                if rotation == "E":
                    x += 1
            if command == "R" and rotation == "N":
                rotation = "E"
                


        return self._buildResult(x, y, rotation)

    def _buildResult(self,x, y, rotation):
            return str(x) + ":" + str(y) + ":" + rotation
