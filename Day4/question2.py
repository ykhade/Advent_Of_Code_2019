
def double_exists(str):
    return (str.count('0') == 2 or
    str.count('1') == 2 or
    str.count('2') == 2 or
    str.count('3') == 2 or
    str.count('4') == 2 or
    str.count('5') == 2 or
    str.count('6') == 2 or
    str.count('7') == 2 or
    str.count('8') == 2 or
    str.count('9') == 2)

def ascending(str):
    return (int(str[0]) <= int(str[1]) and
    int(str[1]) <= int(str[2]) and
    int(str[2]) <= int(str[3]) and
    int(str[3]) <= int(str[4]) and
    int(str[4]) <= int(str[5]))

min = 273025
max = 767253

valid = 0

for x in range(min,max):
    x_str = str(x)
    if ascending(x_str) and double_exists(x_str):
        valid = valid + 1

print(valid)