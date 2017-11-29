import sys


def parse_elevator_log_line(elevator_log_line, start_floor=0):
    current_floor = start_floor

    for char in elevator_log_line:
        if char == '[':
            current_floor += 1
        elif char == ']':
            current_floor -= 1
        else:
            sys.exit("Got an unsupported character {0}.".format(char))

    return current_floor


def get_user_input():
    print("Paste your puzzle input below, and end with an empty line to start the execution of the program. Please use"
          "a new line per elevator log line.")
    lines = []

    while True:
        line = input()

        if line:
            lines.append(line)
        else:
            break

    return '\n'.join(lines)


if __name__ == "__main__":
    user_input = get_user_input()
    log_lines = user_input.split("\n")

    print("Got the following input:")
    print(log_lines)

    for i, log_line in enumerate(log_lines, start=1):
        print("Container {0} is located at floor: {1}.".format(i, parse_elevator_log_line(log_line)))

