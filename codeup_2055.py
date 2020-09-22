x, y = map(int, input().split())

x_measure = []
y_measure = []

for i in range(1, x + 1):
    if x % i == 0:
        x_measure.append(i)
        
for j in range(1, y + 1):
    if y % j == 0:
        y_measure.append(j)

x_y_measure = x_measure + y_measure

measure_set = set(x_y_measure)
measure_list = list(measure_set)
measure_list.sort()

for z in measure_list:
    print(z, end = ' ')
