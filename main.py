from colorama import Back, init

init(autoreset=True)

BLOCK = Back.LIGHTCYAN_EX + '   ' + Back.RESET
SPACE = Back.LIGHTRED_EX + '   ' + Back.RESET

SIZE = 20

for i in range(SIZE):
    print(SPACE * i + BLOCK * (SIZE - i))

print()

for i in range(SIZE):
    print(BLOCK * i)

print()

for i in range(SIZE):
    print(SPACE * i + BLOCK * (SIZE - i * 2))

print()

for i in range(SIZE):
    print(SPACE * (SIZE - i - 1) + BLOCK * ((i + 1 - SIZE // 2) * 2))

print()

# mid = SIZE // 2
#
# for i in range(SIZE):
#     gap = round(math.sin((1 / (SIZE - 1)) * i * math.pi) * (SIZE // 2))
#     print(SPACE * gap + BLOCK * (SIZE - gap))

min_value = 0
max_value = SIZE // 2

for i in range(SIZE):
    normalized_x = i / (SIZE - 1)

    wave_value = 2 * abs(2 * normalized_x - 1)

    gap = round(SIZE - (min_value + wave_value * (max_value - min_value)) / 2) - max_value

    print(SPACE * gap + BLOCK * (SIZE - gap * 2))

print()

min_value = 0
max_value = SIZE // 2

for i in range(SIZE):
    normalized_x = i / (SIZE - 1)

    wave_value = 2 * abs(2 * normalized_x - 1)

    gap = round(SIZE - (min_value + wave_value * (max_value - min_value))) // 2 + 1

    print(BLOCK * gap + SPACE * (SIZE - gap * 2) + BLOCK * gap)

print()

min_value = 0
max_value = SIZE // 2

for i in range(SIZE):
    normalized_x = i / (SIZE - 1)

    wave_value = 2 * abs(2 * normalized_x - 1)

    gap = round(SIZE - (min_value + wave_value * (max_value - min_value))) // 2 + 1

    print(BLOCK * gap)

print()

min_value = 0
max_value = SIZE // 2

for i in range(SIZE):
    normalized_x = i / (SIZE - 1)

    wave_value = 2 * abs(2 * normalized_x - 1)

    gap = round(SIZE - (min_value + wave_value * (max_value - min_value))) // 2 + 1

    print(SPACE * (SIZE - gap) + BLOCK * gap)

print()

for i in range(SIZE):
    print(BLOCK * (SIZE - i))

print()

for i in range(SIZE):
    print(SPACE * (SIZE - i) + BLOCK * i)
