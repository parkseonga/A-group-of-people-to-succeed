h, b, c, s = map(int, input().split())

bit = h * b * c * s
byte = bit/8
kb = byte/1024
mb = kb/1024

print(round(mb, 1), "MB")
