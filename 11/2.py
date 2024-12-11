from collections import Counter

with open('input') as f:
    stones = f.read().split()

def modify(stone: str, count: int, new_counts: Counter):
    if stone == '0':
        new_counts['1'] += count
    else:
        length = len(stone)
        if length % 2 == 0:
            left = stone[:length//2]
            right = str(int(stone[length//2:]))
            new_counts[left] += count
            new_counts[right] += count
        else:
            new_stone = str(int(stone) * 2024)
            new_counts[new_stone] += count

def blink(stone_counts: Counter) -> Counter:
    new_counts = Counter()
    for stone, count in stone_counts.items():
        modify(stone, count, new_counts)
    return new_counts

stone_counts = Counter(stones)

for _ in range(75):
    stone_counts = blink(stone_counts)

print(sum(stone_counts.values()))