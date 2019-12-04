def doubles_count(str):
    return (1 if str[0] == str[1] else 0 +
    1 if str[1] == str[2] else 0 +
    1 if str[2] == str[3] else 0 +
    1 if str[3] == str[4] else 0 +
    1 if str[4] == str[5] else 0) == 1

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
    if doubles_count(x_str) == 1 and ascending(x_str):
        valid = valid + 1

print(valid)