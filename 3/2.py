from re import findall

def solve(memory: str):
    PATTERN = r'(mul\((\d{1,3}),(\d{1,3})\))|(do\(\)|don\'t\(\))'
    sum = 0
    enabled = 1
    for match in findall(PATTERN, memory):
        # print(match)
        if match[3] == 'do()':
            enabled = 1
        elif match[3] == 'don\'t()':
            enabled = 0
        elif enabled:
            sum += (int(match[1]) * int(match[2]))

    return sum

with open('input') as f:
    memory = f.read()

print(solve(memory))