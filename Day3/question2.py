

import sys
import math

input = open("input.txt", 'r')
strList = input.read().split('\n')


def Two():
    l1 = strList[0].split(',')
    l2 = strList[1].split(',')
    step_c = dict()
    grid = dict()
    grid[(0, 0)] = 'o'
    x, y, steps = 0, 0, 0
    for s in l1:
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
            step_c[(x, y)] = steps
            steps += 1
    points = []
    fine_step_c = []
    x, y, steps = 0, 0, 0
    for s in l2:
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
                fine_step_c.append(step_c[(x, y)] + steps)
    minSteps = min(fine_step_c)
    print(minSteps + 1)  # off by one? just add one instead of figuring out why


Two()
