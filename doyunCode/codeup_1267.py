n = int(input())

list1 = list(map(int, input().split()))

a = 0
b = 0
for i in list1:
    if i % 5 == 0:
        a += i
    else:
        b += i
print(a)
