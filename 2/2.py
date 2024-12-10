def order_of(f: int) -> int:
    # whether more are increasing or decreasing
    inc = (f[0] < f[1]) + (f[1] < f[2]) + (f[2] < f[3])
    if inc >= 2: return 1
    return -1

def correct(f: int, inc: int) -> bool:
    if 1 <= inc*(f[1] - f[0]) <= 3:
        return True
    return False

def is_safe(report: list[int], inc: int) -> int:
    for i in range(len(report)-1):
        if not correct(report[i:i+2], inc):
            return i
    return -1

def find_safe(reports: list[list[int]]) -> int:
    safe = 0
    for report in reports:
        inc = order_of(report[:4])
        
        unsafe_idx = is_safe(report, inc)
        if unsafe_idx != -1:
            report1 = report.copy()
            report1.pop(unsafe_idx)
            report2 = report.copy()
            report2.pop(unsafe_idx+1)
            if is_safe(report1, inc) != -1 != is_safe(report2, inc):
                safe-=1

        safe+=1

    return safe

with open('input') as f:
    reports = []
    for line in f:
        reports.append(list(map(int, line.strip().split())))
print(find_safe(reports))
