from itertools import permutations


def read_file(name):
    with open(f"input.txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]


