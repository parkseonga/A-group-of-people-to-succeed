x, y, z = map(int, input().split())

if x > 170 and y > 170 and z > 170:
    print("PASS")

num = [x, y, z]
for i in num:
    if i <= 170:
        print("CRASH", end = ' ')
        print(i, end = '')
        break

