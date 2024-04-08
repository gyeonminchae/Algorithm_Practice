T = int(input())

for num in range(T):
    R, S = input().split()
    R = int(R)
    S = str(S)
    for i in S:
        print(i * R, end = '')
    print()