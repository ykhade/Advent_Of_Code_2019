from itertools import permutations


def read_file(name):
    with open(f"input.txt") as f:
        content = f.readlines()
    return [x.strip() for x in content]


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
    input_counter = 0
    ip = 0

    while int_code[ip] != 99:
        op, modes = split_instruction(int_code[ip])
        values = get_values(int_code, ip, op, modes)

        if op == "01":  # Addition
            int_code[int_code[ip + 3]] = values[0] + values[1]
            ip += 4

        if op == "02":  # Multiplication
            int_code[int_code[ip + 3]] = values[0] * values[1]
            ip += 4

        if op == "03":  # Read and Store prog
            if not input_counter:
                int_code[int_code[ip + 1]] = phase
            else:
                int_code[int_code[ip + 1]] = value
            input_counter += 1
            ip += 2

        if op == "04":  # Print Output
            output = values[0]
            ip += 2

        if op == "05":  # Jump-if-True
            if values[0]:
                ip = values[1]
            else:
                ip += 3

        if op == "06":  # Jump-if-False
            if not values[0]:
                ip = values[1]
            else:
                ip += 3

        if op == "07":  # Less than
            if values[0] < values[1]:
                int_code[int_code[ip + 3]] = 1
            else:
                int_code[int_code[ip + 3]] = 0
            ip += 4

        if op == "08":  # Equals
            if values[0] == values[1]:
                int_code[int_code[ip + 3]] = 1
            else:
                int_code[int_code[ip + 3]] = 0
            ip += 4
    return output


def solve():
    code = read_file("07")[0].split(",")
    code = [int(x) for x in code]

    max_thrust = 0

    for phases in permutations(range(5), 5):
        output = 0

        for phase in phases:
            output = run_int_mach(phase, output, code)
        max_thrust = max(max_thrust, output)

    return max_thrust


print(solve())