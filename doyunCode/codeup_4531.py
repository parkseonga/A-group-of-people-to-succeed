a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

x = [a, b, c, d, e]

print(int(sum(x)/len(x)))

x_sort = sorted(x)
print(x_sort[int(len(x)/2)])
