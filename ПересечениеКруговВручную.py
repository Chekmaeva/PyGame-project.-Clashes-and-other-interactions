x1_center, y1_center, r1 = map(int, input().split())
x2_center, y2_center, r2 = map(int, input().split())
rasst1 = (x2_center - x1_center) ** 2
rasst2 = (y2_center - y1_center) ** 2
d = (rasst1 + rasst2) ** 0.5
if d <= r1 + r2:
    print('YES')
else:
    print('NO')
