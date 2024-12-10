def find_dist(l: list[int], r: list[int]) -> int:
    l.sort(); r.sort()
    return sum(map(lambda x, y: abs(y-x), l, r))

with open('input.txt') as f:
    l = []
    r = []
    for line in f:
        l_, r_ = map(int, line.strip().split())
        l.append(l_)
        r.append(r_)
print(find_dist(l, r))
