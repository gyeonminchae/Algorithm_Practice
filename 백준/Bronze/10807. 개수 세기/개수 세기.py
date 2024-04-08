N = int(input())
s = list(map(int, input().split()))
v = int(input())
i = 0 
for num in s:
    if num == v:
        i += 1
print(i)