import re

lines = open("input.txt").read()
test = list(map(int, re.findall(r"\d+", lines)))

target = 19690720


# Solution
#  a function to solve the intcode program
def test_op(arr):
    for i in range(0, len(arr), 4):
        if arr[i] == 99:
            break
        elif arr[i] != 1 and arr[i] != 2:
            print("error ", i)
        elif arr[i] == 1:
            arr[arr[i + 3]] = arr[arr[i + 1]] + arr[arr[i + 2]]

        elif arr[i] == 2:
            arr[arr[i + 3]] = arr[arr[i + 1]] * arr[arr[i + 2]]

    return (arr[0])


# a function to create the new intcode program with a given noun and verb
def create_new_test(arr, noun, verb):
    new_arr = [arr[0], noun, verb] + arr[3:]
    return (new_arr)


# iterate through all combinations of nouns and verbs, and output the combination(s) that work
for noun in range(0, 99):
    for verb in range(0, 99):
        new_arr = create_new_test(test, noun, verb)
        arr_start = new_arr[0:4]
        test_result = test_op(new_arr)
        if test_result == target:
            print(100 * noun + verb)


