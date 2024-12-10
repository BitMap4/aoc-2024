with open('input') as f:
    original_map = f.read().split('\n')
    original_map = [list(map(ord,row)) for row in original_map]

ARROWS = list(map(ord,['^', '>', 'v', '<']))

def find_arrow(matrix):
    for y,row in enumerate(matrix):
        for x,cell in enumerate(row):
            if cell in ARROWS:
                return (x,y)
    return None

def new_pos(x, y, matrix):
    direction = matrix[y][x] & 0xFF
    if direction == ord('^'):
        return (x, y-1)
    elif direction == ord('>'):
        return (x+1, y)
    elif direction == ord('v'):
        return (x, y+1)
    elif direction == ord('<'):
        return (x-1, y)
    
direction = {
    '^': 1<<8,
    '>': 1<<9,
    'v': 1<<10,
    '<': 1<<11
}

def turn(x, y, matrix):
    direction = matrix[y][x] & 0xFF
    if direction == ord('^'):
        matrix[y][x] = ord('>') | (matrix[y][x] & 0xF00)
    elif direction == ord('>'):
        matrix[y][x] = ord('v') | (matrix[y][x] & 0xF00)
    elif direction == ord('v'):
        matrix[y][x] = ord('<') | (matrix[y][x] & 0xF00)
    elif direction == ord('<'):
        matrix[y][x] = ord('^') | (matrix[y][x] & 0xF00)

loops = set()
_new = [-1, -1]
def move(x, y, matrix):
    _new_pos = new_pos(x, y, matrix)
    if _new_pos is None:
        return None
    new_x, new_y = _new_pos

    if new_x < 0 or new_x >= len(matrix[0]) or new_y < 0 or new_y >= len(matrix):
        return None
    
    # revisiting with same direction
    if matrix[new_y][new_x] & direction[chr(matrix[y][x] & 0xFF)]:
        loops.add((_new[0], _new[1]))
        return None
    
    if matrix[new_y][new_x] & 0xFF in [ord('#'), ord('O')]:
        turn(x, y, matrix)
        return (x, y)
    
    # move and mark old position
    matrix[new_y][new_x] = (matrix[y][x] & 0xFF) | (matrix[new_y][new_x] & 0xF00) | direction[chr(matrix[y][x] & 0xFF)]
    d = direction[chr(matrix[y][x] & 0xFF)]
    matrix[y][x] &= 0xF00
    matrix[y][x] |= d | ord('.')
    return (new_x, new_y)

def simulate(matrix):
    (x, y) = find_arrow(matrix) or (-1, -1)
    if (x, y) == (-1, -1): return
    while True:
        _new_pos = move(x, y, matrix)
        if _new_pos is None:
            break
        x, y = _new_pos

def copy_map(matrix):
    return [row.copy() for row in matrix]

copy = copy_map(original_map)
simulate(copy)
loops = set()

def visited(cell):
    return not not (cell & 0xF00)

ans = 0

for y, row in enumerate(copy):
    for x, cell in enumerate(row):
        if visited(cell):
            attempted_map = copy_map(original_map)
            attempted_map[y][x] = ord('O')
            _new[0], _new[1] = x, y
            simulate(attempted_map)
    
print(len(loops))