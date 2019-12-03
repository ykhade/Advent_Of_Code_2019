import re

import sys
import math

input = open("input.txt", 'r')
strList = input.read().split('\n')


def partOneAndTwo():
    w1 = strList[0].split(',')
    w2 = strList[1].split(',')
    stepC = dict()
    grid = dict()
    grid[(0, 0)] = 'o'
    x, y, steps = 0, 0, 0
    for s in w1:
        for i in range(int(s[1:])):
            if s[0] == 'R':
                x += 1
            elif s[0] == 'L':
                x -= 1
            elif s[0] == 'U':
                y += 1
            elif s[0] == 'D':
                y -= 1
            grid[(x, y)] = '-'
            stepC[(x, y)] = steps
            steps += 1
    points = []
    finalStepC = []
    x, y, steps = 0, 0, 0
    for s in w2:
        for i in range(int(s[1:])):
            if s[0:1] == 'R':
                x += 1
            elif s[0:1] == 'L':
                x -= 1
            elif s[0:1] == 'U':
                y += 1
            elif s[0:1] == 'D':
                y -= 1
            steps += 1
            if (x, y) in grid and grid[(x, y)] == '-':
                points.append((x, y))
                finalStepC.append(stepC[(x, y)] + steps)
    minDist = min([abs(point[0]) + abs(point[1]) for point in points])
    minSteps = min(finalStepC)
    print(minDist)
    print(minSteps + 1)  # off by one? just add one instead of figuring out why


partOneAndTwo()
