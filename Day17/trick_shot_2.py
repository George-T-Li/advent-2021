from time import sleep

def main():
    with open("Day17\input.txt") as f:
        input = f.readline()
    input = parse_input(input)
    x_range, y_range = input[0], input[1]
    xr_min, xr_max = x_range[0], x_range[-1]
    yr_min, yr_max = y_range[0], y_range[-1]

    vx_range = list(range(0, xr_max+1))

    count = 0
    for vx in vx_range:
        vy = yr_min
        while True:
            landed = fire(vx, vy, x_range, y_range)
            if landed[0]:
                count += 1
            else:
                if vy > abs(yr_min):
                    break
            vy += 1

    return count

def triangle(n):
    return n*(n+1)/2

def step(curr_x, curr_y, vx, vy):
    next_x = curr_x + vx
    next_y = curr_y + vy
    if vx > 0:
        new_vx = vx - 1
    elif vx < 0:
        new_vx = vx + 1
    else:
        new_vx = vx
    new_vy = vy - 1
    return next_x, next_y, new_vx, new_vy

def fire(vx, vy, x_range, y_range):
    xr_max = x_range[-1]
    yr_min = y_range[0]
    pos = (0, 0)
    max_h = 0
    while True:
        s = step(pos[0], pos[1], vx, vy)
        pos = (s[0], s[1])
        if pos[1] > max_h:
            max_h = pos[1]
        vx, vy = s[2], s[3]
        if hit(pos[0], pos[1], x_range, y_range):
            return True, max_h
        if miss(pos[0], pos[1], xr_max, yr_min):
            return False, None

def miss(curr_x, curr_y, x_max, y_min):
    if curr_x > x_max:
        return True
    elif curr_y < y_min:
        return True
    else:
        return False

def hit(curr_x, curr_y, x_range, y_range):
    if curr_x in x_range and curr_y in y_range:
        return True
    else:
        return False

def parse_input(input):
    input = input.split()
    x = input[2].strip(",")[2:]
    y = input[3][2:]
    x = x.split(".")
    y = y.split(".")
    x_range = list(range(int(x[0]), int(x[2])+1))
    y_range = list(range(int(y[0]), int(y[2])+1))
    return x_range, y_range

if __name__ == "__main__":
    print(main())