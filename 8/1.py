with open('input') as f:
    city_map = f.read().splitlines()
    city_map: list[list[str]] = list(map(list, city_map))

antennas: dict[str, list[tuple[int]]] = {}

for y, row in enumerate(city_map):
    for x, cell in enumerate(row):
        if cell != '.':
            if cell not in antennas:
                antennas[cell] = []
            antennas[cell].append((x, y))

# print(antennas)

def distance(a: tuple[int], b: tuple[int]) -> tuple[int]:
    return a[0] - b[0], a[1] - b[1]

def add_dist(a: tuple[int], b: tuple[int]) -> tuple[int] | None:
    return a[0] + b[0], a[1] + b[1]

def valid_pos(pos: tuple[int]) -> bool:
    x, y = pos
    return 0 <= x < len(city_map[0]) and 0 <= y < len(city_map)

antinodes: set[tuple[int]] = set()

from itertools import combinations

for antenna, positions in antennas.items():
    for a, b in combinations(positions, 2):
        if valid_pos(add_dist(a, distance(a, b))):
            antinodes.add(add_dist(a, distance(a, b)))
        if valid_pos(add_dist(b, distance(b, a))):
            antinodes.add(add_dist(b, distance(b, a)))

print(len(antinodes))