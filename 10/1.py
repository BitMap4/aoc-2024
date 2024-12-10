with open('input') as f:
    city_map = f.read().splitlines()
    city_map = [list(map(int, row)) for row in city_map]

def find_zero() -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(len(city_map))
        for j in range(len(city_map[0]))
        if city_map[i][j] == 0
    ]

from collections import deque

def bfs(x, y):
    visited = [[False]*len(city_map[0]) for _ in range(len(city_map))]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0
    while queue:
        i, j = queue.popleft()
        if city_map[i][j] == 9:
            count += 1
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = i + dx, j + dy
            if 0 <= ni < len(city_map) and 0 <= nj < len(city_map[0]):
                if not visited[ni][nj] and city_map[ni][nj] == city_map[i][j] + 1:
                    visited[ni][nj] = True
                    queue.append((ni, nj))
    return count

score = 0
for x, y in find_zero():
    score += bfs(x, y)

print(score)