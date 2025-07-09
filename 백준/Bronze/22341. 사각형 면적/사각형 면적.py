import sys
input = sys.stdin.readline

n, c = map(int, input().split())
width = n
height = n
area = width * height

for _ in range(c):
    x, y = map(int, input().split())

    if x >= height or y >= width:
        continue

    # 가로로 자를 경우
    temp_height = height-(height-x)
    temp_area = width * temp_height
    # print(temp_area)

    # 새로로 자를 경우
    temp_width = width - (width - y)
    temp_area_2 = temp_width * height
    # print(temp_area_2)

    if temp_area >= temp_area_2:
        height = temp_height
        area = temp_area
    else:
        width = temp_width
        area = temp_area_2
print(area)
