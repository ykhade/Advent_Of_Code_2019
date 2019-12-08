def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def indirect(planet):
    if planet == "COM":
        res = 0
    else:
        res = 1 + indirect(space_map[planet])
    return res


space_map = {}

for orbit in read_input():
    temp = orbit.split(sep=')')
    if temp[1] in space_map:
        raise ValueError
    space_map[temp[1]] = temp[0]

count = 0

for key in space_map.keys():
    count += indirect(key)

print(count)