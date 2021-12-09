def dive_position(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    position = [0, 0]

    for line in lines:
        command = line.split()
        if command[0] == "forward": position[0] += int(command[1])
        elif command[0] == "down": position[1] += int(command[1])
        else: position[1] -= int(command[1])

    return position[0]*position[1]

print(dive_position("Day2\input.txt")) #1507611

def dive_position_aim(fname):
    with open(fname, "r") as f:
        lines = f.readlines()
    position = [0, 0, 0] #[x, y, aim]

    for line in lines:
        command = line.split()
        if command[0] == "down": position[2] += int(command[1])
        elif command[0] == "up": position[2] -= int(command[1])
        else:
            position[0] += int(command[1])
            position[1] += (int(command[1])*position[2])

    return position[0]*position[1]

print(dive_position_aim("Day2\input.txt")) #1880593125