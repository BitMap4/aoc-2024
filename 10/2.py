with open('input') as f:
    city_map = f.read().splitlines()
    city_map = (map(list, city_map))
    city_map = [list(map(int, row)) for row in city_map]

cache = {}

def move(x: int, y: int, prev: int) -> int:
    if (x, y, prev) in cache:
        return cache[(x, y, prev)]
    if x < 0 or y < 0 or x >= len(city_map) or y >= len(city_map[0]):
        return 0
    if city_map[x][y] == 9 and prev == 8:
        return 1
    score = 0
    if city_map[x][y] == prev + 1:
        score += move(x + 1, y, prev + 1)
        score += move(x - 1, y, prev + 1)
        score += move(x, y + 1, prev + 1)
        score += move(x, y - 1, prev + 1)
    # print(x, y, score)
    cache[(x, y, prev)] = score
    return score

def find_zero() -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(len(city_map))
        for j in range(len(city_map[0]))
        if city_map[i][j] == 0
    ]

score = 0

for x, y in find_zero():
    score += move(x, y, -1)

print(score)
# print(cache)