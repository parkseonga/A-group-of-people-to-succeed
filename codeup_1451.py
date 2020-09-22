n = int(input())

num = []
for i in range(n):
    num.append(int(input()))

num_sort = sorted(num)

for i in num_sort:
    print(i)
