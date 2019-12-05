#Day 5: Sunny with a Chance of Asteroids
filepath = 'input.txt'


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def nextStep(pc):
    if pc == 1:
        return (pc + 4, pc + 1, pc + 2, pc + 3)
    elif pc == 2:
        return (pc + 4, pc + 1, pc + 2, pc + 3)
    else:
        return (pc + 1, pc + 2, 0, 0)


# (op_code, a, b, res)
def treatInput(pc, sequence):
    if sequence[pc] == 99:
        return (99, 0, 0, 0)

    op = str(sequence[pc])
    if len(op) == 1:
        if sequence[pc] == 3 or sequence[pc] == 4:
            return (sequence[pc], sequence[pc + 1], 0, 0)
        else:
            return (sequence[pc], sequence[sequence[pc + 1]], sequence[sequence[pc + 2]], sequence[sequence[pc + 3]])

    if len(op) == 2:
        if op[0] == 1:
            return (sequence[pc], sequence[pc + 1], sequence[pc + 2], sequence[pc + 3])
        else:
            return (sequence[pc], sequence[pc + 1], sequence[pc + 2], sequence[pc + 3])


    elif len(op) == 3:

    elif len(op) == 4:

    elif len(op) == 5:
        if op[0] == 0:
            return (op[1:], sequence[pc + 1], sequence[pc + 2], sequence[pc + 3])
        else:
            return (op[1:], sequence[pc + 1], sequence[pc + 2], sequence[pc + 3])


def IntCode(sequence):
    # init positions
    pc = 0

    while sequence[pc] != 99:

        (op_code, a, b, res) = treatInput(pc, sequence)

        if op_code == 1:
            a = sequence[pc + 1]
            b = sequence[pc + 2]
            res = sequence[pc + 3]
            sequence[res] = add(sequence[a], sequence[b])

        elif op_code == 2:
            a = sequence[pc + 1]
            b = sequence[pc + 2]
            res = sequence[pc + 3]
            sequence[res] = mul(sequence[a], sequence[b])

        # input
        elif op_code == 3:
            a = sequence[pc + 1]
            sequence[a] = 1
            pc += 2

        elif op_code == 4:
            a = sequence[pc + 1]
            print(sequence[a])
            pc += 2

        (pc, a, b, res) = nextStep(pc)

    return sequence


with open(filepath) as fp:
    input = fp.readline().strip().split(',')

    input = [int(i) for i in input]
    # replace position 1 with value 12, and replace position 2 with value 2.
    # input[1] = 12
    # input[2] = 2

    input = IntCode(input)
    print(input[0])
