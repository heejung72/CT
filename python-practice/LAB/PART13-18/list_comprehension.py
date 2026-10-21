areas = []
for i in range(1, 11):
    areas = areas + [i*i]
    # 정사각형의 넓이
print(areas)

areas2 = [i*i for i in range(1, 11) if i%2 ==0]
print(areas2)

areas3=[]
for i in range(1, 11):
    if (i%2 ==0):
        areas3 = areas3 + [i*i]
        # 정사각형의 넓이
print(areas)


print([(x,y) for x in range(15) for y in range(20)])
