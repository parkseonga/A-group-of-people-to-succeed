a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())

a_sum = sum(a)
b_sum = sum(b)
c_sum = sum(c)

if a_sum == 0:
    print("D")
elif a_sum == 1:
    print("C")
elif a_sum == 2:
    print("B")
elif a_sum == 3:
    print("A")
else:
    print("E")

if b_sum == 0:
    print("D")
elif b_sum == 1:
    print("C")
elif b_sum == 2:
    print("B")
elif b_sum == 3:
    print("A")
else:
    print("E")
    
if c_sum == 0:
    print("D")
elif c_sum == 1:
    print("C")
elif c_sum == 2:
    print("B")
elif c_sum == 3:
    print("A")
else:
    print("E")
