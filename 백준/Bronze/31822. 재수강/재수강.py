from sys import stdin as stdin

target_subject = stdin.readline().strip()
num = int(stdin.readline().strip())
subjects = []
for _ in range(num):
    subjects.append(stdin.readline().strip())
cnt = 0
for subject in subjects:
    if subject[0:5] == target_subject[0:5]:
        cnt += 1
print(cnt)