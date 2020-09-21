a, b, c = input().split()
c = int(c)

print(a, end = '')
print(b, end = '')

if c < 10:
    print(0, end = '')
    print(c, end = '')
else:
    print(c, end = '')
