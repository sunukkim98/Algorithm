import sys
input = sys.stdin.readline

t = int(input().strip())
for i in range(1, t+1):
    n = int(input().strip())
    sequence = list(map(int, input().split()))

    while True:
        if n == 2:
            print(f"Case #{i}: ", end='')
            if sequence[0] > sequence[1]:
                print("Alice")
            else:
                print("Bob")
            break
        if n % 2 == 0:
            # print((n // 2) - 1)
            temp_seq = []
            for j in range((n // 2)):
                # print(sequence[j])
                # print(sequence[-(j+1)])
                temp_seq.append(sequence[j] + sequence[-(j + 1)])
            # print(temp_seq)
            n = len(temp_seq)
            sequence = temp_seq
        else:
            # print(n // 2)
            temp_seq = []
            for j in range((n // 2)):
                # print(sequence[j])
                # print(sequence[-(j+1)])
                temp_seq.append(sequence[j] + sequence[-(j+1)])
            temp_seq.append(sequence[(n//2)] * 2)
            # print(temp_seq)
            n = len(temp_seq)
            sequence = temp_seq
