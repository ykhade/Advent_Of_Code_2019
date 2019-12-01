with open('input.txt') as f:
    masses = [int(line.strip()) for line in f]


print(masses)

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