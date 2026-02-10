point1 = (0, 0)
point2 = (3, 4)
x1, y1 = point1[0], point1[1]
x2, y2 = point2[0], point2[1]

distance = ((x2-x1)**2 + (y2-y1)**2) ** 0.5

print(f'점1: {point1}')
print(f'\n점2 : {point2}')
print(f'\n두 점 사이의 거리: {distance}')