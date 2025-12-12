import sys

while True:
    line = sys.stdin.readline().strip()

    if line == "end":
        break
    elif line == "animal":
        print("Panthera tigris")
    elif line == "tree":
        print("Pinus densiflora")
    elif line == "flower":
        print("Forsythia koreana")
