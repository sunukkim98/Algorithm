import sys

class_num = sys.stdin.readline().strip()
if class_num[0] == "F":
    print("Foundation")
elif class_num[0] == "C":
    print("Claves")
elif class_num[0] == "V":
    print("Veritas")
elif class_num[0] == "E":
    print("Exploration")
