n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = 0
for i in range(n):
    mini = min(a)
    maxi = max(b)
    
    s += mini * maxi

    a_index = a.index(mini)
    b_index = b.index(maxi)
    
    a.pop(a_index)
    b.pop(b_index)
    
print(s)

