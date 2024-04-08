n_list = []
for id in range(28):
    n = int(input())
    n_list.append(n)

not_n_list = []
for i in range(1,31):
    if i not in n_list:
        not_n_list.append(i)

print(min(not_n_list))
print(max(not_n_list))