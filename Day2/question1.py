# Day 2: 1202 Program Alarm
import re

lines = open("input.txt").read()
test = list(map(int, re.findall(r"\d+", lines)))

def op1(arr, point):  # addition
    pos1 = arr[point + 1]  # getting positions
    pos2 = arr[point + 2]
    pos3 = arr[point + 3]
    newpos = arr[pos1] + arr[pos2]
    arr[pos3] = newpos
    return arr


def op2(arr, point):  # multiplication
    pos1 = arr[point + 1]  # getting positions
    pos2 = arr[point + 2]
    pos3 = arr[point + 3]
    newpos = arr[pos1] * arr[pos2]
    arr[pos3] = newpos
    return arr


def alarm(test):
    pointer = 0
    while test[pointer] != 99:
        if test[pointer] == 1:
            op1(test, pointer)
        elif test[pointer] == 2:
            op2(test, pointer)

        pointer += 4
    return test


print()
