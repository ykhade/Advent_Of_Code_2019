def read_file(name):
    with open(f"input.txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]


def gfd(x, y):
    if x is None:
        return abs(y)
    if y is None:
        return abs(x)

    while y:
        x, y = y, x % y
    return abs(x)


def get_direction(station, asteroid):
    direction = set()
    for asteroids in asteroid:
        if asteroids == station:
            continue

        vec = (asteroids[0] - station[0], asteroids[1] - station[1])
        gcd = gfd(vec[0], vec[1])
        vec = (vec[0] // gcd, vec[1] // gcd)

        direction.add(vec)

    return direction

def solution():
    input = read_file('Day10/input.txt')
    sizex, sizey = len(input[0]), len(input)

    asteroid = [(x,y) for y in range(sizey) for x in range(sizex) if input[y][x] == "#"]

    return max([len(get_direction(station, asteroid)) for station in asteroid])

print(solution())