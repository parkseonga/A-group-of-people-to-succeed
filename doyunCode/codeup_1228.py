h, w = input().split()
h = float(h)
w = float(w)

standard = (h - 100)*0.9
obesity = (w - standard) * 100/standard

if obesity <= 10:
    print("정상")
elif obesity <= 20:
    print("과체중")
else:
    print("비만")
