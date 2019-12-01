# Day 1: The Tyranny of the Rocket Equation
with open('input.txt') as f:
    arr = [int(line.strip()) for line in f]

def math(x):
    return x//3 - 2


def total_fuel_func(arr, math):
    total_fuel = 0
    for mass in arr:
        fuel = 0
        fuel += math(mass)
        while(fuel > 0):
            total_fuel += fuel
            fuel = math(fuel)

    return total_fuel


print(total_fuel_func(arr, math))



