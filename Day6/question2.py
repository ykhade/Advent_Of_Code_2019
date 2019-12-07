def read_input():
    res = []
    with open("input.txt") as inf:
        for line in inf:
            res.append(line.strip())
    return res


def get_num(name):
    if name in dict_num:
        res = dict_num[name]
    else:
        res = len(dict_num)
        dict_num[name] = res
    return res


def Dijkstra(N, S, matrix):
    valid = [True]*N
    weight = [1000000]*N
    weight[S] = 0
    for i in range(N):
        min_weight = 1000001
        ID_min_weight = -1
        for i in range(N):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(N):
            if weight[ID_min_weight] + matrix[ID_min_weight][i] < weight[i]:
                weight[i] = weight[ID_min_weight] + matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


indata = read_input()
map_size = len(indata) + 1

space_map = [[1000000 for j in range(map_size)] for i in range(map_size)]

dict_num = {"COM": 0}
for planet in indata:
    temp = planet.split(sep=")")
    num_a = get_num(temp[0])
    num_b = get_num(temp[1])
    space_map[num_a][num_b] = 1
    space_map[num_b][num_a] = 1

test = Dijkstra(map_size, dict_num["YOU"], space_map)

print(test[dict_num["SAN"]] - 2)