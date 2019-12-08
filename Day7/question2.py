from itertools import permutations


def read_file(name):
    with open(f"input.txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]


class Test:
    def __init__(self, prog):
        self.prog = prog[:]
        self.ip = 0
        self.output = 0
        self.input_counter = 0
        self.halt = False


def split_instruction(instruction):
    instruction = f"{instruction:05}"
    return instruction[3:], instruction[0:3]


def get_values(input, pos, op, modes):
    mode_a, mode_b, mode_c = modes
    values = []

    if op in ["01", "02", "04", "05", "06", "07", "08"]:
        if mode_c == "0":
            values.append(input[input[pos + 1]])
        else:
            values.append(input[pos + 1])

        if op in ["01", "02", "05", "06", "07", "08"]:
            if mode_b == "0":
                values.append(input[input[pos + 2]])
            else:
                values.append(input[pos + 2])

            if op in []:
                if mode_a == "0":
                    values.append(input[input[pos + 3]])
                else:
                    values.append(input[pos + 3])

    return values


def run_int_mach(phase, value, int_code):
    while int_code.prog[int_code.ip] != 99:
        op, modes = split_instruction(int_code.prog[int_code.ip])
        values = get_values(int_code.prog, int_code.ip, op, modes)

        if op == "01":  # Addition
            int_code.prog[int_code.prog[int_code.ip + 3]] = values[0] + values[1]
            int_code.ip += 4

        if op == "02":  # Multiplication
            int_code.prog[int_code.prog[int_code.ip + 3]] = values[0] * values[1]
            int_code.ip += 4

        if op == "03":  # Read and Store input
            if not int_code.input_counter:
                int_code.prog[int_code.prog[int_code.ip + 1]] = phase
            else:
                int_code.prog[int_code.prog[int_code.ip + 1]] = value

            int_code.input_counter += 1
            int_code.ip += 2

        if op == "04":  # Print Output
            int_code.output = values[0]
            int_code.ip += 2
            return int_code

        if op == "05":  # Jump-if-True
            if values[0]:
                int_code.ip = values[1]
            else:
                int_code.ip += 3

        if op == "06":  # Jump-if-False
            if not values[0]:
                int_code.ip = values[1]
            else:
                int_code.ip += 3

        if op == "07":  # Less than
            if values[0] < values[1]:
                int_code.prog[int_code.prog[int_code.ip + 3]] = 1
            else:
                int_code.prog[int_code.prog[int_code.ip + 3]] = 0
            int_code.ip += 4

        if op == "08":  # Equals
            if values[0] == values[1]:
                int_code.prog[int_code.prog[int_code.ip + 3]] = 1
            else:
                int_code.prog[int_code.prog[int_code.ip + 3]] = 0
            int_code.ip += 4

    int_code.halt = True
    return int_code


def solve():
    code = read_file("07")[0].split(",")
    code = [int(x) for x in code]
    max_thrust = 0

    for phases in permutations(range(5, 10), 5):
        amps = [Test(code) for i in range(5)]
        active = 0

        while not amps[4].halt:
            amps[active] = run_int_mach(phases[active], amps[active - 1].output, amps[active])
            active = (active + 1) % 5

        max_thrust = max(max_thrust, amps[4].output)
    return max_thrust


print(solve())