operations = {}
with open('input') as f:
    for line in f:
        a,b = line.split(': ')
        operations[int(a)] = list(map(int, b.split()))

possible = set()

def check(current, result, numbers):
    if current == result:
        return True
    if not numbers:
        return False
    return check(current + numbers[0], result, numbers[1:]) or check(current * numbers[0], result, numbers[1:])

for k, v in operations.items():
    if check(0, k, v):
        possible.add(k)

print(sum(possible))