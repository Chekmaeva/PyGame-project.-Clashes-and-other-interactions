x1_1, y1_1, x1_2, y1_2 = map(int, input().split())
x1_2 = x1_1 + x1_2
y1_2 = y1_1 + y1_2

x2_1, y2_1, x2_2, y2_2 = map(int, input().split())
x2_2 = x2_1 + x2_2
y2_2 = y2_1 + y2_2

s1 = (x1_1 >= x2_1 and x1_1 <= x2_2) or (x1_2 >= x2_1 and x1_2 <= x2_2)
s2 = (y1_1 >= y2_1 and y1_1 <= y2_2) or (y1_2 >= y2_1 and y1_2 <= y2_2)
s3 = (x2_1 >= x1_1 and x2_1 <= x1_2) or (x2_2 >= x1_1 and x2_2 <= x1_2)
s4 = (y2_1 >= y1_1 and y2_1 <= y1_2) or (y2_2 >= y1_1 and y2_2 <= y1_2)

if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
    print('YES')
else:
    print('NO')
