I = int(input())

for _ in range(I):
    R, S = input().split()
    R = int(R)

    for i in S:
        print(i * R, end='')

    print()