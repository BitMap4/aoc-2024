operations = {}
with open('input') as f:
    for line in f:
        a,b = line.split(': ')
        operations[int(a)] = list(map(int, b.split()))

possible = set()

def check(current, result, numbers):
    if not numbers:
        if current == result:
            return True
        else:
            return False
    if current > result:
        return False
    return (False
        or check(current + numbers[0], result, numbers[1:])
        or check(current * numbers[0], result, numbers[1:])
        or check(int(str(current) + str(numbers[0])), result, numbers[1:])
    )

for k, v in operations.items():
    if check(v[0], k, v[1:]):
        possible.add(k)

print(sum(possible))