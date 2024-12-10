def match(matrix: list[list[str]], x: int, y: int) -> bool:
    # check if "MAS" is in the diagonal where x,y is A
    if matrix[x][y] != 'A':
        return False
    if x+1 >= len(matrix) or y+1 >= len(matrix[x]):
        return False
    if x-1 < 0 or y-1 < 0:
        return False
    if matrix[x+1][y+1]+matrix[x-1][y-1] not in ['MS', 'SM']:
        return False
    if matrix[x+1][y-1]+matrix[x-1][y+1] not in ['MS', 'SM']:
        return False
    return True

with open('input') as f:
    memory = f.read().split('\n')

def solve(memory: list[str]) -> int:
    ans = 0
    matrix = [list(i) for i in memory]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            ans += match(matrix, x, y)
    return ans

print(solve(memory))