import time

def print_matrix(matrix):
    print('\n'.join([''.join(map(lambda x: chr(x&0xFF),row)) for row in matrix]))
    print()
    time.sleep(0.1)

with open('input') as f:
    memory = f.read().split('\n')
    memory = [list(map(ord,row)) for row in memory]

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
    direction = matrix[y][x]
    if direction == ord('^'):
        matrix[y][x] = ord('>')
    elif direction == ord('>'):
        matrix[y][x] = ord('v')
    elif direction == ord('v'):
        matrix[y][x] = ord('<')
    elif direction == ord('<'):
        matrix[y][x] = ord('^')


def move(x, y, matrix):
    _new_pos = new_pos(x, y, matrix)
    if _new_pos is None:
        return None
    new_x, new_y = _new_pos

    if new_x < 0 or new_x >= len(matrix[0]) or new_y < 0 or new_y >= len(matrix):
        return None
    
    # revisiting with same direction
    if matrix[new_y][new_x] & direction[chr(matrix[y][x] & 0xFF)]:
        return None
    
    if matrix[new_y][new_x] & 0xFF == ord('#'):
        turn(x, y, matrix)
        # print('turn')
        # print_matrix(matrix)
        return (x, y)
    
    # move and mark old position
    matrix[new_y][new_x] = (matrix[y][x] & 0xFF) | (matrix[new_y][new_x] & 0xF00)
    d = direction[chr(matrix[y][x] & 0xFF)]
    matrix[y][x] &= 0xF00
    matrix[y][x] |= d | ord('.')
    # print('move')
    # print_matrix(matrix)
    return (new_x, new_y)

(x, y) = find_arrow(memory)

while True:
    print_matrix(memory)
    _new_pos = move(x, y, memory)
    if _new_pos is None:
        break
    x, y = _new_pos
print_matrix(memory)

s=0

for row in memory:
    s += sum(map(lambda x: not not (x&0xF00), row))
s += not memory[y][x] & 0xF00

print(s)