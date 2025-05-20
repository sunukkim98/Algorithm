import sys
input = sys.stdin.readline

T = int(input().strip())
for i in range(T):
    N = int(input().strip())
    total_unit = 0
    total_grade = 0.0
    for j in range(N):
        unit, grade = input().split()
        total_unit += int(unit)
        total_grade += float(grade) * int(unit)
    print(total_unit, round((total_grade / total_unit), 1))
