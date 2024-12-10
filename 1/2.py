from collections import Counter
def find_sim(l: list[int], r: list[int]) -> int:
    l_ = Counter(l)
    r_ = Counter(r)
    sum = 0
    for k in l_:
        sum += k * l_[k] * r_[k]
    return sum

with open('input.txt') as f:
    l = []
    r = []
    for line in f:
        l_, r_ = map(int, line.strip().split())
        l.append(l_)
        r.append(r_)
print(find_sim(l, r))
