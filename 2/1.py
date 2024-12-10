def find_safe(*reports: list[list[int]]) -> int:
    safe = 0
    inc = 0
    for report in reports:
        i = 0
        if report[i] < report[i+1]: inc = 1
        else: inc = -1

        while i != len(report)-1:
            if not (1 <= inc*(report[i+1] - report[i]) <= 3):
                safe -= 1
                break
            i += 1
        safe += 1

    return safe

with open('input') as f:
    reports = []
    for line in f:
        reports.append(list(map(int, line.strip().split())))
print(find_safe(*reports))
