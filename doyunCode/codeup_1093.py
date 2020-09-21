n = int(input())
a = list(map(int, input().split()))

lst = [0] * 23

for i in a:
  lst[a - 1] += 1;

for i in range(0, 23):
   print(lst[i], end=' ');
