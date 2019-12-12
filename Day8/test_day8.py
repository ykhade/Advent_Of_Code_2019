import question1
import pytest

H = 6
W = 25
IMAGE_SIZE = H * W
inp = open("Day8/input.txt").read()
layers = []
while inp:
    layers.append(inp[:IMAGE_SIZE])
    inp = inp[IMAGE_SIZE:]












def test_solution():
    assert question1.solution() ==2904