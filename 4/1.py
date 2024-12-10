def check(matrix: list[list[str]], x: int, y: int) -> int:
    # XMAS = ['X', 'M', 'A', 'S']
    found = 0
    if y+3 < len(matrix[x]) and matrix[x][y]=='X' and matrix[x][y+1]=='M' and matrix[x][y+2]=='A' and matrix[x][y+3]=='S':
        found+=1
    if y-3 >= 0 and matrix[x][y]=='X' and matrix[x][y-1]=='M' and matrix[x][y-2]=='A' and matrix[x][y-3]=='S':
        found+=1
    if x+3 < len(matrix) and matrix[x][y]=='X' and matrix[x+1][y]=='M' and matrix[x+2][y]=='A' and matrix[x+3][y]=='S':
        found+=1
    if x-3 >= 0 and matrix[x][y]=='X' and matrix[x-1][y]=='M' and matrix[x-2][y]=='A' and matrix[x-3][y]=='S':
        found+=1
    if x+3 < len(matrix) and y+3 < len(matrix[x]) and matrix[x][y]=='X' and matrix[x+1][y+1]=='M' and matrix[x+2][y+2]=='A' and matrix[x+3][y+3]=='S':
        found+=1
    if x-3 >= 0 and y-3 >= 0 and matrix[x][y]=='X' and matrix[x-1][y-1]=='M' and matrix[x-2][y-2]=='A' and matrix[x-3][y-3]=='S':
        found+=1
    if x+3 < len(matrix) and y-3 >= 0 and matrix[x][y]=='X' and matrix[x+1][y-1]=='M' and matrix[x+2][y-2]=='A' and matrix[x+3][y-3]=='S':
        found+=1
    if x-3 >= 0 and y+3 < len(matrix[x]) and matrix[x][y]=='X' and matrix[x-1][y+1]=='M' and matrix[x-2][y+2]=='A' and matrix[x-3][y+3]=='S':
        found+=1
    return found

with open('input') as f:
    memory = f.read().split('\n')

def solve(memory: list[str]) -> int:
    ans = 0
    matrix = [list(i) for i in memory]
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            ans += check(matrix, x, y)
    return ans

print(solve(memory))