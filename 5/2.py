def parse_rule(rules):
    "a|b means a must occur before b if both occur"
    parsed = [[0]*100 for _ in range(100)]
    for rule in rules.split('\n'):
        a, b = rule.split('|')
        # print(a, b)
        parsed[int(a)][int(b)] = 1
        # print(''.join(map(str, parsed[int(a)])))
    return parsed

def parse_indices(indices):
    parsed = []
    for index in indices.split('\n'):
        parsed.append(list(map(int, index.split(','))))
    return parsed

with open('input') as f:
    rules, indices = f.read().split('\n\n')
    rules = parse_rule(rules)
    # print('\n'.join(''.join(map(str, r)) for r in rules))
    indices = parse_indices(indices)

def valid_idx(idx):
    a = update[idx]
    for b in range(len(rules[a])):
        if rules[a][b] and b in update[:idx]:
            return False
    return True

def valid_update(update):
    return all(valid_idx(i) for i in range(len(update)))

def fix_update(update: list[int], rules):
    i = len(update) - 1
    while i:
        if valid_idx(i): i -= 1
        else:
            for j in range(i):
                if rules[update[i]][update[j]]:
                    update[i], update[j] = update[j], update[i]
                    break

sum = 0
for update in indices:
    if not valid_update(update):
        # print(update)
        fix_update(update, rules)
        sum += update[len(update)>>1]

print(sum)