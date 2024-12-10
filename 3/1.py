from re import findall

def solve(memory: str):
    PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'
    sum = 0
    for match in findall(PATTERN, memory):
        sum += int(match[0]) * int(match[1])

    return sum

with open('input') as f:
    memory = f.read()

print(solve(memory))