import re
import sys


TURN_ON = "TURNON"
TURN_OFF = "TURNOFF"
TOGGLE = "TOGGLE"


class Grid(object):
    width = 0
    height = 0
    grid = {}

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = self.__create_grid(width, height)

    def __create_grid(self, width, height):
        grid = {}

        for w in range(width + 1):
            for h in range(height + 1):
                grid[self.__get_key_from_width_and_height(w, h)] = 0

        return grid

    def __get_key_from_width_and_height(self, width, height):
        return "{0}.{1}".format(width, height)

    def get_amount_of_enabled_lights(self):
        return sum([v for (k, v) in self.grid.items()])

    def turn_on_lights(self, from_x, from_y, to_x, to_y):
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                key = self.__get_key_from_width_and_height(x, y)
                self.grid[key] = 1

    def turn_off_lights(self, from_x, from_y, to_x, to_y):
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                key = self.__get_key_from_width_and_height(x, y)
                self.grid[key] = 0

    def toggle_lights(self, from_x, from_y, to_x, to_y):
        for x in range(from_x, to_x + 1):
            for y in range(from_y, to_y + 1):
                key = self.__get_key_from_width_and_height(x, y)
                # If the current value is 1, we will turn it off (by setting
                # it to 0), otherwise it was 0 and thus we'll turn it on by
                # setting it to 1.
                new_value = 0 if self.grid[key] == 1 else 1
                self.grid[key] = new_value


def get_user_input():
    print("Paste your puzzle input below, and end with an empty line to start the execution of the program.")
    print("The execution of this script might take a while depending on your input.")
    lines = []

    while True:
        line = input()

        if line:
            lines.append(line)
        else:
            break

    return '\n'.join(lines)


def parse_action_from_command(command):
    if command.startswith("turn on"):
        return TURN_ON
    elif command.startswith("turn off"):
        return TURN_OFF
    elif command.startswith("toggle"):
        return TOGGLE
    else:
        print("Got an unsupported command {0}".format(command))
        return None


def get_coordinates_from_command(command):
    match = re.search(r"(\d+),(\d+) through (\d+),(\d+)", command)

    if match is None or len(match.groups()) is not 4:
        return None

    return [int(coordinate) for coordinate in match.groups()]


if __name__ == "__main__":
    grid = Grid(999, 999)
    user_input = get_user_input()
    commands = user_input.split("\n")

    for command in commands:
        action = parse_action_from_command(command)
        coordinates = get_coordinates_from_command(command)

        if action is None or coordinates is None:
            sys.exit("Got an invalid command '{0}'".format(command))

        if action == TURN_ON:
            grid.turn_on_lights(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        elif action == TURN_OFF:
            grid.turn_off_lights(coordinates[0], coordinates[1], coordinates[2], coordinates[3])
        elif action == TOGGLE:
            grid.toggle_lights(coordinates[0], coordinates[1], coordinates[2], coordinates[3])

    print("Enabled lights: {0}".format(grid.get_amount_of_enabled_lights()))
