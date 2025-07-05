import sys
input = sys.stdin.readline

x, y = map(int, input().split())
k = int(input().strip())
route = input().strip()
x_t, y_t = 0, 0
time_step = 0
heard = False
for direction in route:
    # print(x_t, y_t)
    if (x_t > x-2) and (x_t < x+2) and (y_t > y-2) and (y_t < y+2):
       print(time_step)
       heard = True

    if direction == 'I':
        x_t += 1
    elif direction == 'S':
        y_t += 1
    elif direction == 'Z':
        x_t -= 1
    elif direction == 'J':
        y_t -= 1

    time_step += 1
if (x_t > x-2) and (x_t < x+2) and (y_t > y-2) and (y_t < y+2):
   print(time_step)
   heard = True

if heard == False:
    print(-1)
