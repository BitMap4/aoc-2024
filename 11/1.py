with open('input') as f:
    stones = f.read().split()

def append(stones: list[str], items: list[str]) -> list[str]:
    for item in items:
        stones.append(item)

def modify(stone: str) -> list[str]:
    if stone == '0':
        return ['1']
    length = len(stone)
    if length % 2 == 0:
        return [stone[:length//2], str(int(stone[length//2:]))]
    return [str(int(stone) * 2024)]

def blink(stones: list[str]) -> list[str]:
    new_stones = []
    for stone in stones:
        append(new_stones, modify(stone))
    return new_stones

for _ in range(75):
    stones = blink(stones)

print(len(stones))