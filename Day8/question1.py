H = 6
W = 25
IMAGE_SIZE = H * W
inp = open("Day8/input.txt").read()
layers = []
while inp:
    layers.append(inp[:IMAGE_SIZE])
    inp = inp[IMAGE_SIZE:]


def solution():
    row_with_lowest_0s = []
    lowest_num_of_zeros = IMAGE_SIZE
    for layer in layers:
        if layer.count('0') < lowest_num_of_zeros:
            lowest_num_of_zeros = layer.count('0')
            row_with_lowest_0s = layer

    return row_with_lowest_0s.count('1') * row_with_lowest_0s.count('2')


print(solution())