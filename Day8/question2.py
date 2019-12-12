H = 6
W = 25
IMAGE_SIZE = H * W
inp = open("input.txt").read()
layers = []
while inp:
    layers.append(inp[:IMAGE_SIZE])
    inp = inp[IMAGE_SIZE:]



def solution():
    decoded = list(layers[0])
    for layer in layers:
        for i in range(len(layer)):
            if decoded[i] == '2':
                decoded[i] = layer[i]

    image = ''
    while decoded:
        for i in range(W):
            image += decoded[i]
        image += '\n'
        decoded = decoded[W:]

    return image.replace('0', ' ').replace('1', '█')

print(solution())