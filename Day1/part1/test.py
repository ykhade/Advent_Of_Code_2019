with open('input.txt') as data:
    mass = [int(line.strip()) for line in data]


def math(mass):
    total_mass = 0
    for x in mass:
        calculated = (x // 3) - 2  # 5/3
        total_mass += calculated
    return total_mass


print(math(mass))

# mass = input("What is the mass?: ")
# print("calculating for a mass of:", mass)
#
# mass = int(mass)
#
# def math(mass):
#     calculated = (mass // 3) - 2
#     print(f"To launch a mass of {mass} Santa needs {calculated}.")
#     return
#
# math(mass)
#
# # I'm having trouble with printing line 8 outisde of the math function
